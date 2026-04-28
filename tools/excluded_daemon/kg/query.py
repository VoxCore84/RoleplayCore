"""Query API for the Knowledge Graph.

Provides entity lookup, mention retrieval, relation traversal, and
contradiction detection against memory files.

Usage:
    python -m tools.excluded_daemon.kg.query "Amy Little"
    python -m tools.excluded_daemon.kg.query --kind person --all
    python -m tools.excluded_daemon.kg.query --stats
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.excluded_daemon import config
from tools.excluded_daemon.kg.build import _canonicalize


@dataclass
class Entity:
    id: int
    kind: str
    name: str
    canonical: str
    first_seen: str | None
    last_seen: str | None
    metadata: dict
    mention_count: int = 0


@dataclass
class Mention:
    id: int
    entity_id: int
    chunk_id: str
    doc_path: str
    line_hint: str
    context: str
    confidence: float


@dataclass
class Relation:
    id: int
    subject_id: int
    predicate: str
    object_id: int
    source_chunk: str
    confidence: float
    subject_name: str = ""
    object_name: str = ""


def _connect() -> sqlite3.Connection:
    if not config.KG_DB.exists():
        raise FileNotFoundError(f"KG database not found: {config.KG_DB}")
    conn = sqlite3.connect(str(config.KG_DB))
    conn.row_factory = sqlite3.Row
    return conn


def lookup_entity(name: str, kind: str | None = None) -> list[Entity]:
    """Fuzzy match against canonical + name columns."""
    if not name or not name.strip():
        return []
    conn = _connect()
    needle = _canonicalize(kind or "person", name)
    if not needle:
        conn.close()
        return []
    params: list = []
    clauses = []

    clauses.append("(canonical LIKE ? OR name LIKE ? OR canonical = ?)")
    params.extend([f"%{needle}%", f"%{name}%", needle])
    if kind:
        clauses.append("kind = ?")
        params.append(kind)

    sql = f"""
        SELECT e.*, COUNT(m.id) AS mention_count
        FROM entities e
        LEFT JOIN mentions m ON m.entity_id = e.id
        WHERE {' AND '.join(clauses)}
        GROUP BY e.id
        ORDER BY mention_count DESC
    """
    rows = conn.execute(sql, params).fetchall()
    conn.close()

    results = []
    for r in rows:
        results.append(Entity(
            id=r["id"], kind=r["kind"], name=r["name"],
            canonical=r["canonical"], first_seen=r["first_seen"],
            last_seen=r["last_seen"],
            metadata=json.loads(r["metadata"] or "{}"),
            mention_count=r["mention_count"],
        ))
    return results


def entity_mentions(entity_id: int, limit: int = 50) -> list[Mention]:
    conn = _connect()
    rows = conn.execute(
        "SELECT * FROM mentions WHERE entity_id = ? ORDER BY created_at DESC LIMIT ?",
        (entity_id, limit),
    ).fetchall()
    conn.close()
    return [Mention(
        id=r["id"], entity_id=r["entity_id"], chunk_id=r["chunk_id"],
        doc_path=r["doc_path"], line_hint=r["line_hint"],
        context=r["context"], confidence=r["confidence"],
    ) for r in rows]


def entity_relations(entity_id: int, depth: int = 1) -> list[Relation]:
    conn = _connect()
    rows = conn.execute("""
        SELECT r.*,
               e1.name AS subject_name,
               e2.name AS object_name
        FROM relations r
        JOIN entities e1 ON e1.id = r.subject_id
        JOIN entities e2 ON e2.id = r.object_id
        WHERE r.subject_id = ? OR r.object_id = ?
        ORDER BY r.confidence DESC
        LIMIT 100
    """, (entity_id, entity_id)).fetchall()
    conn.close()
    return [Relation(
        id=r["id"], subject_id=r["subject_id"], predicate=r["predicate"],
        object_id=r["object_id"], source_chunk=r["source_chunk"],
        confidence=r["confidence"], subject_name=r["subject_name"],
        object_name=r["object_name"],
    ) for r in rows]


# Salience weights for ranking BFS candidates. Used because the current KG
# uses a single co-occurrence predicate (`mentioned_with`) with confidence
# uniformly at 0.70 — without these weights, popular orgs (USAF, DoD) drown
# out person/case_number/regulation hops that are usually more interesting.
_KIND_BONUS = {
    "person": 3.0,
    "regulation": 2.0,
    "case_number": 1.5,
    "date": 1.0,
    "org": 0.7,
    "amount": 0.5,
}


def entity_expand(
    entity_id: int,
    hops: int = 2,
    max_entities: int = 100,
    per_hop_cap: int | None = None,
    compact: bool = False,
) -> dict:
    """BFS multi-hop traversal over the relations graph with salience ranking.

    At each hop, collects candidate connected entities, scores them by
    salience = kind_bonus * log(1 + mention_count) * relation_count *
    best_confidence, and keeps the top `per_hop_cap` by salience. This prevents
    a single popular root (e.g. Adam Taylor with 11K co-occurrences) from
    saturating the budget with low-signal orgs and starving downstream hops.

    Args:
        entity_id: Root entity ID to expand from.
        hops: Maximum hop distance (default 2).
        max_entities: Hard cap on total connected entities across all hops.
        per_hop_cap: Cap per hop. If None, defaults to max_entities // hops
                     (so each hop gets an equal share of the budget).
        compact: When True, omits mentions_by_hop and trims entity fields
                 to {id, kind, name, mention_count}. Used by the MCP layer
                 to stay under output token limits — a depth=2 expansion on
                 a hub entity (e.g. Adam Taylor) returns ~99KB without
                 compact mode, which exceeds MCP's max output. Direct CLI
                 callers keep compact=False to get the full response.

    Returns:
        dict with:
          - root: Entity dict for the starting node (None + `error` if id missing)
          - hops: hop budget passed in
          - connected: list of {entity, hop, via_predicate, via_entity_id,
                                via_entity_name, confidence, relation_count,
                                salience}
          - mentions_by_hop: {hop_no: [up to 30 mention dicts]} — OMITTED in compact mode
          - stats: {total_entities, max_entities_reached, entities_per_hop, compact}
    """
    import math

    conn = _connect()

    row = conn.execute("""
        SELECT e.*, COUNT(m.id) AS mention_count
        FROM entities e
        LEFT JOIN mentions m ON m.entity_id = e.id
        WHERE e.id = ?
        GROUP BY e.id
    """, (entity_id,)).fetchone()

    if row is None:
        conn.close()
        return {
            "root": None,
            "hops": hops,
            "connected": [],
            "mentions_by_hop": {},
            "stats": {
                "total_entities": 0,
                "max_entities_reached": False,
                "entities_per_hop": {},
            },
            "error": f"entity {entity_id} not found",
        }

    root = Entity(
        id=row["id"], kind=row["kind"], name=row["name"],
        canonical=row["canonical"], first_seen=row["first_seen"],
        last_seen=row["last_seen"],
        metadata=json.loads(row["metadata"] or "{}"),
        mention_count=row["mention_count"],
    )

    if per_hop_cap is None:
        per_hop_cap = max(1, max_entities // max(1, hops))

    visited: set[int] = {entity_id}
    connected: list[dict] = []
    mentions_by_hop: dict[int, list[dict]] = {}
    entities_per_hop: dict[int, int] = {}
    frontier: set[int] = {entity_id}
    capped = False

    for hop in range(1, hops + 1):
        if not frontier or capped:
            break

        placeholders = ",".join("?" * len(frontier))
        rel_rows = conn.execute(f"""
            SELECT
                r.predicate, r.confidence,
                r.subject_id, e1.kind AS s_kind, e1.name AS s_name,
                e1.canonical AS s_canonical, e1.first_seen AS s_first,
                e1.last_seen AS s_last, e1.metadata AS s_meta,
                r.object_id, e2.kind AS o_kind, e2.name AS o_name,
                e2.canonical AS o_canonical, e2.first_seen AS o_first,
                e2.last_seen AS o_last, e2.metadata AS o_meta
            FROM relations r
            JOIN entities e1 ON e1.id = r.subject_id
            JOIN entities e2 ON e2.id = r.object_id
            WHERE (r.subject_id IN ({placeholders}) OR r.object_id IN ({placeholders}))
              AND r.subject_id != r.object_id
            ORDER BY r.confidence DESC
            LIMIT 10000
        """, list(frontier) + list(frontier)).fetchall()

        # Bucket relations by candidate entity (the "other side")
        candidates: dict[int, dict] = {}
        for r in rel_rows:
            s_in = r["subject_id"] in frontier
            o_in = r["object_id"] in frontier

            if s_in and r["object_id"] not in visited:
                other_id = r["object_id"]
                other = Entity(
                    id=r["object_id"], kind=r["o_kind"], name=r["o_name"],
                    canonical=r["o_canonical"], first_seen=r["o_first"],
                    last_seen=r["o_last"],
                    metadata=json.loads(r["o_meta"] or "{}"),
                    mention_count=0,
                )
                via_id, via_name = r["subject_id"], r["s_name"]
            elif o_in and r["subject_id"] not in visited:
                other_id = r["subject_id"]
                other = Entity(
                    id=r["subject_id"], kind=r["s_kind"], name=r["s_name"],
                    canonical=r["s_canonical"], first_seen=r["s_first"],
                    last_seen=r["s_last"],
                    metadata=json.loads(r["s_meta"] or "{}"),
                    mention_count=0,
                )
                via_id, via_name = r["object_id"], r["o_name"]
            else:
                continue

            cand = candidates.setdefault(other_id, {
                "entity": other,
                "vias": [],
                "best_conf": 0.0,
            })
            cand["vias"].append({
                "predicate": r["predicate"],
                "via_id": via_id,
                "via_name": via_name,
                "confidence": r["confidence"],
            })
            if r["confidence"] > cand["best_conf"]:
                cand["best_conf"] = r["confidence"]

        if not candidates:
            mentions_by_hop[hop] = []
            entities_per_hop[hop] = 0
            break

        # Backfill mention counts in a single batched query
        ids = list(candidates.keys())
        ph = ",".join("?" * len(ids))
        mc_rows = conn.execute(
            f"SELECT entity_id, COUNT(*) AS c FROM mentions "
            f"WHERE entity_id IN ({ph}) GROUP BY entity_id",
            ids,
        ).fetchall()
        mc_map = {mr["entity_id"]: mr["c"] for mr in mc_rows}

        # Score by salience and rank
        for cid, cand in candidates.items():
            mc = mc_map.get(cid, 0)
            cand["entity"].mention_count = mc
            kb = _KIND_BONUS.get(cand["entity"].kind, 1.0)
            cand["salience"] = (
                kb
                * math.log(1 + mc)
                * len(cand["vias"])
                * cand["best_conf"]
            )

        ranked = sorted(candidates.items(), key=lambda kv: -kv[1]["salience"])

        next_frontier: set[int] = set()
        chosen_this_hop = 0
        for cid, cand in ranked:
            if chosen_this_hop >= per_hop_cap:
                break
            if len(connected) >= max_entities:
                capped = True
                break
            top_via = max(cand["vias"], key=lambda v: v["confidence"])
            if compact:
                entity_payload = {
                    "id": cand["entity"].id,
                    "kind": cand["entity"].kind,
                    "name": cand["entity"].name,
                    "mention_count": cand["entity"].mention_count,
                }
            else:
                entity_payload = asdict(cand["entity"])
            connected.append({
                "entity": entity_payload,
                "hop": hop,
                "via_predicate": top_via["predicate"],
                "via_entity_id": top_via["via_id"],
                "via_entity_name": top_via["via_name"],
                "confidence": top_via["confidence"],
                "relation_count": len(cand["vias"]),
                "salience": round(cand["salience"], 4),
            })
            visited.add(cid)
            next_frontier.add(cid)
            chosen_this_hop += 1

        # Top mentions for this hop (single batched query) — skipped in compact mode
        if not compact and next_frontier:
            nf_ids = list(next_frontier)
            nf_ph = ",".join("?" * len(nf_ids))
            mn_rows = conn.execute(
                f"SELECT * FROM mentions WHERE entity_id IN ({nf_ph}) "
                f"ORDER BY confidence DESC LIMIT 30",
                nf_ids,
            ).fetchall()
            mentions_by_hop[hop] = [{
                "id": mr["id"],
                "entity_id": mr["entity_id"],
                "chunk_id": mr["chunk_id"],
                "doc_path": mr["doc_path"],
                "line_hint": mr["line_hint"],
                "context": (mr["context"] or "")[:200],
                "confidence": mr["confidence"],
            } for mr in mn_rows]
        elif not compact:
            mentions_by_hop[hop] = []

        entities_per_hop[hop] = len(next_frontier)
        frontier = next_frontier

    conn.close()

    if compact:
        root_payload = {
            "id": root.id,
            "kind": root.kind,
            "name": root.name,
            "mention_count": root.mention_count,
        }
    else:
        root_payload = asdict(root)

    result = {
        "root": root_payload,
        "hops": hops,
        "connected": connected,
        "stats": {
            "total_entities": len(connected),
            "max_entities_reached": capped,
            "entities_per_hop": entities_per_hop,
            "compact": compact,
        },
    }
    if not compact:
        result["mentions_by_hop"] = mentions_by_hop
    return result


def search_entities(kind: str | None = None, query: str | None = None,
                    limit: int = 50) -> list[Entity]:
    conn = _connect()
    clauses = []
    params: list = []
    if kind:
        clauses.append("e.kind = ?")
        params.append(kind)
    if query:
        clauses.append("(e.canonical LIKE ? OR e.name LIKE ?)")
        params.extend([f"%{query.lower()}%", f"%{query}%"])

    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    rows = conn.execute(f"""
        SELECT e.*, COUNT(m.id) AS mention_count
        FROM entities e
        LEFT JOIN mentions m ON m.entity_id = e.id
        {where}
        GROUP BY e.id
        ORDER BY mention_count DESC
        LIMIT ?
    """, [*params, limit]).fetchall()
    conn.close()

    return [Entity(
        id=r["id"], kind=r["kind"], name=r["name"],
        canonical=r["canonical"], first_seen=r["first_seen"],
        last_seen=r["last_seen"],
        metadata=json.loads(r["metadata"] or "{}"),
        mention_count=r["mention_count"],
    ) for r in rows]


def kg_stats() -> dict:
    conn = _connect()
    stats = {
        "entities": conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0],
        "mentions": conn.execute("SELECT COUNT(*) FROM mentions").fetchone()[0],
        "relations": conn.execute("SELECT COUNT(*) FROM relations").fetchone()[0],
    }
    for row in conn.execute("SELECT kind, COUNT(*) AS c FROM entities GROUP BY kind ORDER BY c DESC"):
        stats[f"entities_{row[0]}"] = row[1]
    top_persons = conn.execute("""
        SELECT e.name, COUNT(m.id) AS mc
        FROM entities e JOIN mentions m ON m.entity_id = e.id
        WHERE e.kind = 'person'
        GROUP BY e.id ORDER BY mc DESC LIMIT 10
    """).fetchall()
    stats["top_persons"] = [{"name": r[0], "mentions": r[1]} for r in top_persons]
    conn.close()
    return stats


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", help="entity name to look up")
    ap.add_argument("--kind", help="filter by entity kind")
    ap.add_argument("--all", action="store_true", help="list all entities of --kind")
    ap.add_argument("--mentions", type=int, help="show mentions for entity ID")
    ap.add_argument("--relations", type=int, help="show relations for entity ID")
    ap.add_argument("--stats", action="store_true", help="show KG statistics")
    ap.add_argument("--json", action="store_true", help="output as JSON")
    args = ap.parse_args()

    if args.stats:
        s = kg_stats()
        print(json.dumps(s, indent=2))
        return

    if args.mentions is not None:
        ms = entity_mentions(args.mentions)
        for m in ms:
            if args.json:
                print(json.dumps(asdict(m)))
            else:
                print(f"  [{m.doc_path}] {m.context[:120]}...")
        return

    if args.relations is not None:
        rs = entity_relations(args.relations)
        for r in rs:
            if args.json:
                print(json.dumps(asdict(r)))
            else:
                print(f"  {r.subject_name} --{r.predicate}--> {r.object_name} (conf={r.confidence:.2f})")
        return

    if args.all:
        entities = search_entities(kind=args.kind)
        for e in entities:
            if args.json:
                print(json.dumps(asdict(e)))
            else:
                print(f"  [{e.id}] {e.kind}: {e.name} (canonical={e.canonical}, mentions={e.mention_count})")
        return

    if args.query:
        entities = lookup_entity(args.query, kind=args.kind)
        if not entities:
            print(f"No entities found for '{args.query}'")
            return
        for e in entities:
            if args.json:
                print(json.dumps(asdict(e)))
            else:
                print(f"\n{'='*60}")
                print(f"[{e.id}] {e.kind}: {e.name}")
                print(f"  canonical: {e.canonical}")
                print(f"  mentions: {e.mention_count}")
                if e.first_seen:
                    print(f"  first_seen: {e.first_seen}")
                if e.last_seen:
                    print(f"  last_seen: {e.last_seen}")
                if e.metadata:
                    print(f"  metadata: {json.dumps(e.metadata)}")
                ms = entity_mentions(e.id, limit=5)
                if ms:
                    print(f"  top mentions:")
                    for m in ms:
                        print(f"    [{m.doc_path}] {m.context[:100]}...")
        return

    ap.print_help()


if __name__ == "__main__":
    main()

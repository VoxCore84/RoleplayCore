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

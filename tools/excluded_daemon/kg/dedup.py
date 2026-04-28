"""Entity dedup — merge duplicate KG entities with high-confidence matching.

Only merges when:
1. Same kind
2. One canonical is a prefix of the other (e.g., "baguley" vs "baguley dm")
3. The shorter name is >= 4 chars (avoid merging "ko" into everything)
4. Length difference is small (initials/suffix only, not substring matches)

Usage:
    python -m tools.excluded_daemon.kg.dedup --dry-run
    python -m tools.excluded_daemon.kg.dedup --apply
"""
from __future__ import annotations

import argparse
import json
import logging
import sqlite3
import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.excluded_daemon import config

log = logging.getLogger("kg.dedup")


def find_duplicates(conn: sqlite3.Connection, kind: str = "person") -> list[dict]:
    """Find high-confidence duplicate entity pairs."""
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT a.id as a_id, a.name as a_name, a.canonical as a_canon,
               b.id as b_id, b.name as b_name, b.canonical as b_canon, a.kind
        FROM entities a, entities b
        WHERE a.kind = ? AND b.kind = ? AND a.id < b.id
        AND length(a.canonical) >= 4 AND length(b.canonical) >= 4
        AND (a.canonical LIKE b.canonical || '%' OR b.canonical LIKE a.canonical || '%')
        AND abs(length(a.canonical) - length(b.canonical)) <= 4
    """, (kind, kind)).fetchall()

    pairs = []
    for r in rows:
        a_mentions = conn.execute("SELECT COUNT(*) FROM mentions WHERE entity_id=?", (r["a_id"],)).fetchone()[0]
        b_mentions = conn.execute("SELECT COUNT(*) FROM mentions WHERE entity_id=?", (r["b_id"],)).fetchone()[0]

        # Keep the one with more mentions as the survivor
        if a_mentions >= b_mentions:
            survivor_id, survivor_name = r["a_id"], r["a_name"]
            victim_id, victim_name = r["b_id"], r["b_name"]
            survivor_mentions, victim_mentions = a_mentions, b_mentions
        else:
            survivor_id, survivor_name = r["b_id"], r["b_name"]
            victim_id, victim_name = r["a_id"], r["a_name"]
            survivor_mentions, victim_mentions = b_mentions, a_mentions

        pairs.append({
            "survivor_id": survivor_id,
            "survivor_name": survivor_name,
            "victim_id": victim_id,
            "victim_name": victim_name,
            "survivor_mentions": survivor_mentions,
            "victim_mentions": victim_mentions,
            "kind": r["kind"],
        })

    return pairs


def merge_entity(conn: sqlite3.Connection, survivor_id: int, victim_id: int) -> int:
    """Merge victim into survivor. Returns number of mentions reassigned."""
    # Reassign mentions
    cur = conn.execute(
        "UPDATE mentions SET entity_id = ? WHERE entity_id = ?",
        (survivor_id, victim_id),
    )
    reassigned = cur.rowcount

    # Reassign relations (both directions)
    conn.execute(
        "UPDATE relations SET subject_id = ? WHERE subject_id = ?",
        (survivor_id, victim_id),
    )
    conn.execute(
        "UPDATE relations SET object_id = ? WHERE object_id = ?",
        (survivor_id, victim_id),
    )

    # Delete self-referencing relations created by merge
    conn.execute("DELETE FROM relations WHERE subject_id = object_id")

    # Delete the victim entity
    conn.execute("DELETE FROM entities WHERE id = ?", (victim_id,))

    return reassigned


def run(kind: str = "person", dry_run: bool = True) -> dict:
    """Run dedup. Returns stats."""
    conn = sqlite3.connect(str(config.KG_DB))
    pairs = find_duplicates(conn, kind)

    stats = {"kind": kind, "pairs_found": len(pairs), "merged": 0, "mentions_reassigned": 0}

    if dry_run:
        print(f"DRY RUN — {len(pairs)} pairs would be merged for kind={kind}:")
        for p in pairs[:50]:
            print(f"  MERGE #{p['victim_id']} \"{p['victim_name']}\" ({p['victim_mentions']}m) "
                  f"→ #{p['survivor_id']} \"{p['survivor_name']}\" ({p['survivor_mentions']}m)")
        if len(pairs) > 50:
            print(f"  ... and {len(pairs) - 50} more")
    else:
        for p in pairs:
            reassigned = merge_entity(conn, p["survivor_id"], p["victim_id"])
            stats["merged"] += 1
            stats["mentions_reassigned"] += reassigned
        conn.commit()
        print(f"APPLIED — merged {stats['merged']} duplicates, reassigned {stats['mentions_reassigned']} mentions")

    conn.close()
    return stats


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kind", default="person", help="entity kind to dedup (default: person)")
    ap.add_argument("--all-kinds", action="store_true", help="dedup all kinds")
    ap.add_argument("--apply", action="store_true", help="actually merge (default is dry-run)")
    args = ap.parse_args()

    dry_run = not args.apply
    if args.all_kinds:
        for kind in ["person", "org", "regulation", "case_number"]:
            print(f"\n=== {kind} ===")
            stats = run(kind=kind, dry_run=dry_run)
            print(json.dumps(stats))
    else:
        stats = run(kind=args.kind, dry_run=dry_run)
        print(json.dumps(stats))


if __name__ == "__main__":
    main()

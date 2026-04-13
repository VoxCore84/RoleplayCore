#!/usr/bin/env python3
"""Entity resolver for the case persons roster.

Given a query term ("Corpening", "Tolin", "Dr Zander"), returns:
  1. The canonical name + role + org
  2. Hybrid search hits across FTS5 + ChromaDB + mbox
     (rate-limited; returns union of the top hits)

Roster is at `.cache/persons/persons.json` and hand-curated. Add people by
editing that JSON directly (simple schema: canonical, aliases[], role, org).

Usage:
    python tools/persons_resolve.py Corpening
    python tools/persons_resolve.py "Col Johnston" --limit 20
    python tools/persons_resolve.py Wheeler --json
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ROSTER = REPO_ROOT / ".cache" / "persons" / "persons.json"
MBOX_DB = Path("C:/Users/atayl/Desktop/Excluded/mbox/mbox_index.db")
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"


def load_roster() -> dict:
    if not ROSTER.exists():
        print(f"ERROR: roster not found at {ROSTER}", file=sys.stderr)
        return {"persons": []}
    return json.loads(ROSTER.read_text(encoding="utf-8"))


def resolve(term: str, roster: dict) -> dict | None:
    """Find the canonical person whose alias list (case-insensitive substring) contains `term`."""
    needle = term.lower().strip()
    for p in roster.get("persons", []):
        if needle in p["canonical"].lower():
            return p
        for alias in p.get("aliases", []):
            if needle == alias.lower() or needle in alias.lower():
                return p
    return None


def fts_hits(term: str, limit: int) -> list[dict]:
    if not FTS_DB.exists():
        return []
    conn = sqlite3.connect(str(FTS_DB))
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            """SELECT c.rel_path, c.chunk_idx,
                      snippet(chunks_fts, 1, '**', '**', '...', 12) AS snippet
               FROM chunks_fts
               JOIN chunks c ON c.rowid = chunks_fts.rowid
               WHERE chunks_fts MATCH ?
               ORDER BY rank LIMIT ?""",
            (term, limit),
        ).fetchall()
    except sqlite3.OperationalError:
        rows = conn.execute(
            """SELECT rel_path, chunk_idx, substr(content, 1, 200) AS snippet
               FROM chunks WHERE content LIKE ? LIMIT ?""",
            (f"%{term}%", limit),
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def mbox_hits(term: str, limit: int) -> list[dict]:
    if not MBOX_DB.exists():
        return []
    conn = sqlite3.connect(str(MBOX_DB))
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            """SELECT m.id, m.date_raw, m.from_addr, m.subject,
                      snippet(messages_fts, 4, '**', '**', '...', 10) AS snippet
               FROM messages_fts
               JOIN messages m ON m.id = messages_fts.rowid
               WHERE messages_fts MATCH ?
               ORDER BY rank LIMIT ?""",
            (term, limit),
        ).fetchall()
    except sqlite3.OperationalError:
        rows = []
    conn.close()
    return [dict(r) for r in rows]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("term", help="Person name or alias to resolve")
    ap.add_argument("--limit", type=int, default=10, help="Max hits per index")
    ap.add_argument("--json", action="store_true", help="JSON output")
    args = ap.parse_args()

    roster = load_roster()
    person = resolve(args.term, roster)

    if person is None:
        result = {
            "query": args.term,
            "resolved": False,
            "note": "No roster entry. Adding to .cache/persons/persons.json will improve future queries.",
        }
    else:
        # Fan out across all aliases for comprehensive hits
        search_terms = [person["canonical"]] + list(person.get("aliases", []))
        # De-dupe by preserving first occurrence
        seen_fts = set()
        all_fts: list[dict] = []
        all_mbox: list[dict] = []
        seen_mbox = set()

        for st in search_terms[:5]:   # cap to first 5 aliases to bound cost
            for h in fts_hits(st, args.limit):
                key = (h["rel_path"], h["chunk_idx"])
                if key not in seen_fts:
                    seen_fts.add(key)
                    all_fts.append(h)
            for h in mbox_hits(st, args.limit):
                key = h["id"]
                if key not in seen_mbox:
                    seen_mbox.add(key)
                    all_mbox.append(h)

        result = {
            "query": args.term,
            "resolved": True,
            "canonical": person["canonical"],
            "role": person.get("role", ""),
            "org": person.get("org", ""),
            "aliases_used": search_terms[:5],
            "fts_hits_count": len(all_fts),
            "mbox_hits_count": len(all_mbox),
            "fts_hits": all_fts[: args.limit],
            "mbox_hits": all_mbox[: args.limit],
        }

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        if not result["resolved"]:
            print(f"No roster entry for '{args.term}'.")
            print("Add it to .cache/persons/persons.json with canonical + aliases.")
            return 1
        print(f"## {result['canonical']}")
        print(f"Role: {result['role']}")
        print(f"Org:  {result['org']}")
        print(f"Aliases queried: {', '.join(result['aliases_used'])}")
        print()
        print(f"### FTS5 ({result['fts_hits_count']} unique)")
        for h in result["fts_hits"][:10]:
            print(f"  `{h['rel_path']}` [chunk {h['chunk_idx']}]")
            print(f"    {h['snippet'][:200]}")
        print()
        print(f"### Mbox ({result['mbox_hits_count']} unique)")
        for h in result["mbox_hits"][:10]:
            print(f"  [{h['id']}] {h['date_raw'][:16] if h['date_raw'] else '?':<17} from {h['from_addr']}")
            print(f"    Subj: {h['subject']}")
            if h.get("snippet"):
                print(f"    {h['snippet'][:200]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

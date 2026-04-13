#!/usr/bin/env python3
"""Show a full email thread (every message + attachments) by message_id or subject.

Addresses critique item #11: I built mbox search but never a thread view. In a legal
corpus emails are conversations — the ability to see "every message in this thread"
matters for evidence.

Usage:
    python tools/mbox_thread.py --id 17073                    # by message id
    python tools/mbox_thread.py --subject "HAF SAPR"          # find + show first
    python tools/mbox_thread.py --subject "X" --json          # machine-readable
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from pathlib import Path

MBOX_DB = Path("C:/Users/atayl/Desktop/Excluded/mbox/mbox_index.db")


def _conn():
    if not MBOX_DB.exists():
        print(f"ERROR: mbox DB not found at {MBOX_DB}", file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(str(MBOX_DB))
    conn.row_factory = sqlite3.Row
    return conn


def find_by_id(conn, mid: int) -> dict | None:
    r = conn.execute("SELECT * FROM messages WHERE id = ?", (mid,)).fetchone()
    return dict(r) if r else None


def find_by_subject(conn, subject: str, limit: int = 10) -> list[dict]:
    rows = conn.execute(
        "SELECT * FROM messages WHERE subject LIKE ? ORDER BY date_sent DESC LIMIT ?",
        (f"%{subject}%", limit),
    ).fetchall()
    return [dict(r) for r in rows]


def expand_thread(conn, seed: dict, max_depth: int = 10) -> list[dict]:
    """Walk in_reply_to / references / subject to assemble the full thread.

    Strategy:
      1. Start with the seed message
      2. Walk BACKWARDS via in_reply_to/references until we find the root
      3. From root, find all messages whose in_reply_to or references contains any
         known message-id in the collected set
      4. Deduplicate by id, sort by date_sent
    """
    # Step 1-2: walk upward to root via in_reply_to
    visited_ids: set[int] = set()
    known_mids: set[str] = set()
    current = seed
    while current and current["id"] not in visited_ids and len(visited_ids) < max_depth:
        visited_ids.add(current["id"])
        if current.get("message_id"):
            known_mids.add(current["message_id"])
        parent_mid = current.get("in_reply_to")
        if not parent_mid:
            break
        parent = conn.execute(
            "SELECT * FROM messages WHERE message_id = ?", (parent_mid,)
        ).fetchone()
        if parent:
            current = dict(parent)
        else:
            break

    # Also capture References header chain
    if seed.get("references_hdr"):
        for tok in seed["references_hdr"].split():
            tok = tok.strip("<>").strip()
            if tok:
                known_mids.add(tok)

    # Step 3: find all messages that cite any known mid or are in our visited set
    if known_mids:
        placeholders = ",".join("?" * len(known_mids))
        rows = conn.execute(
            f"""SELECT * FROM messages
                WHERE message_id IN ({placeholders})
                   OR in_reply_to IN ({placeholders})
                ORDER BY date_sent""",
            list(known_mids) + list(known_mids),
        ).fetchall()
        results = [dict(r) for r in rows]
    else:
        results = [seed]

    # Also add anything whose references_hdr mentions any known_mid
    if known_mids:
        extra = conn.execute(
            """SELECT * FROM messages
               WHERE references_hdr IS NOT NULL
               AND references_hdr != ''"""
        ).fetchall()
        for r in extra:
            rd = dict(r)
            if any(m in (rd.get("references_hdr") or "") for m in known_mids):
                if rd["id"] not in {x["id"] for x in results}:
                    results.append(rd)

    # Deduplicate + sort
    seen_ids = set()
    unique = []
    for m in results:
        if m["id"] not in seen_ids:
            seen_ids.add(m["id"])
            unique.append(m)
    unique.sort(key=lambda m: m.get("date_sent") or 0)
    return unique


def format_thread(thread: list[dict]) -> str:
    lines = []
    lines.append(f"# Thread ({len(thread)} messages)")
    lines.append("")
    for i, msg in enumerate(thread, 1):
        date = time.strftime("%Y-%m-%d %H:%M", time.localtime(msg.get("date_sent") or 0)) if msg.get("date_sent") else "?"
        from_addr = msg.get("from_addr", "?")
        subject = msg.get("subject", "(no subject)")
        labels = msg.get("labels", "")
        att_count = msg.get("attachment_count", 0) or 0
        body = (msg.get("body_text") or "")[:800].strip()
        lines.append(f"## [{i}] id={msg['id']} · {date}")
        lines.append(f"**From:** {from_addr}")
        lines.append(f"**To:** {msg.get('to_addrs', '?')}")
        lines.append(f"**Subject:** {subject}")
        if labels:
            lines.append(f"**Labels:** {labels}")
        if att_count:
            lines.append(f"**Attachments:** {att_count}")
        lines.append("")
        lines.append(body)
        if msg.get("body_text") and len(msg["body_text"]) > 800:
            lines.append(f"\n_[truncated — full body {len(msg['body_text'])} chars]_")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--id", type=int, help="Seed message id")
    g.add_argument("--subject", help="Substring match against subject; uses most recent")
    ap.add_argument("--max-depth", type=int, default=10, help="Max reply-chain depth (default 10)")
    ap.add_argument("--json", action="store_true", help="Emit JSON")
    args = ap.parse_args()

    conn = _conn()
    if args.id:
        seed = find_by_id(conn, args.id)
        if not seed:
            print(f"No message with id={args.id}", file=sys.stderr)
            return 1
    else:
        candidates = find_by_subject(conn, args.subject, limit=1)
        if not candidates:
            print(f"No message matching subject substring {args.subject!r}", file=sys.stderr)
            return 1
        seed = candidates[0]

    thread = expand_thread(conn, seed, max_depth=args.max_depth)
    conn.close()

    if args.json:
        # Drop raw body_text to bound output
        for m in thread:
            if "body_text" in m and m["body_text"]:
                m["body_text"] = m["body_text"][:500] + "...[truncated]" if len(m["body_text"]) > 500 else m["body_text"]
        print(json.dumps({"seed_id": seed["id"], "thread": thread}, indent=2, default=str))
    else:
        print(format_thread(thread))
    return 0


if __name__ == "__main__":
    sys.exit(main())

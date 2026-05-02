#!/usr/bin/env python3
"""Generate multi-hop evaluation queries for the citation pipeline.

Multi-hop = a question whose answer requires JOINING facts from 2+ documents.
The acquihire diligence number "82% multi-hop accuracy" was INFERRED — never
measured. This builds the held-out test set so we can replace the inferred
number with a measured one.

The queries deliberately exercise joins like:
  - person + regulation cited
  - event + sequel-event date
  - document + amendment date
  - claim + counter-claim by different person
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_env_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if key:
        return key
    env_path = REPO_ROOT / "tools" / "ai_studio" / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY"):
                return line.partition("=")[2].strip().strip('"').strip("'")
    return ""


SYSTEM = """You are generating MULTI-HOP evaluation queries for a legal-evidence retrieval system covering Captain Adam Taylor's military legal case.

A multi-hop query is one whose answer requires the system to JOIN information from 2 or more distinct source documents. Single-document lookups are NOT multi-hop.

Each query must specify the join type. Output JSONL — one {"query": "...", "hop_type": "...", "expected_join": "..."} per line.

HOP TYPES (use these literal strings):
- person_to_regulation — "Person X cited regulation Y in event Z"
- event_to_sequel — "Event X was followed by event Y, with what time gap"
- claim_vs_counter — "Person X claimed P; Person Y said Q; how do they conflict"
- document_to_amendment — "Document X was amended by Y; how did the amendment change Z"
- timeline_join — "What happened between event X and event Y in chronological order"
- person_to_filing — "Person X handled filings A and B; what's in each"
- regulation_to_application — "Regulation X requires Y; how was it applied (or violated) in Adam's case"
- multi_person_chain — "X told Y who told Z; what was the message"

Generate exactly 12 queries — at least one per hop_type. Each query must:
1. Reference at least 2 specific nouns (people, dates, regulations, document titles).
2. Be answerable from the case archive in principle (don't ask about events outside the documented case).
3. Have a clear "expected_join" — one sentence describing what the system must connect to answer correctly.

CRITICAL: do NOT generate near-duplicates of these prior calibration/holdout queries:
- "What did Col Cermak's Notice of Proposed Revocation cite as grounds, and how did Adam's NPDB Subject Statement respond"
- Any query about SA Grice OSI confirmation
- Any query about the OSC Supplement draft contents alone (single-doc)
- Any query asking just "who is X" (single-doc)

Output JSONL ONLY. No preamble, no markdown."""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="AI_Studio/Reports/scheduled/multihop_queries_v1.jsonl")
    p.add_argument("--model", default="claude-opus-4-7")
    p.add_argument("--n", type=int, default=12)
    args = p.parse_args()

    api_key = load_env_key()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    # Use the same memory-file context as the held-out generator
    context_files = [
        "memory/case-status.md",
        "memory/case-contacts.md",
        "memory/case-filings-tracker.md",
    ]
    parts = []
    for cf in context_files:
        candidates = [
            Path(os.path.expanduser(f"~/.claude/projects/C--Users-atayl-VoxCore/{cf}")),
            REPO_ROOT / cf,
        ]
        for p_ in candidates:
            if p_.exists():
                parts.append(f"=== {cf} ===\n" + p_.read_text(encoding='utf-8')[:3000])
                break
    context = "\n\n".join(parts)

    user_msg = (
        f"Case context:\n\n{context}\n\n---\n\n"
        f"Generate exactly {args.n} multi-hop queries as JSONL per the spec."
    )

    body = json.dumps({
        "model": args.model,
        "max_tokens": 3000,
        "system": SYSTEM,
        "messages": [{"role": "user", "content": user_msg}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        payload = json.loads(resp.read())
    text = ""
    for block in payload.get("content", []):
        if block.get("type") == "text":
            text += block.get("text", "")

    queries = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
            if "query" in obj and "hop_type" in obj:
                queries.append(obj)
        except json.JSONDecodeError:
            continue

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(json.dumps(q, ensure_ascii=False) for q in queries) + "\n",
                        encoding="utf-8")

    usage = payload.get("usage", {})
    cost = (usage.get("input_tokens", 0) * 15 + usage.get("output_tokens", 0) * 75) / 1_000_000
    print(f"Generated {len(queries)} multi-hop queries to {out_path}")
    print(f"Tokens: {usage.get('input_tokens', 0)} in + {usage.get('output_tokens', 0)} out = ~${cost:.3f}")
    types = {}
    for q in queries:
        types[q.get("hop_type", "?")] = types.get(q.get("hop_type", "?"), 0) + 1
    print(f"Hop-type distribution: {types}")


if __name__ == "__main__":
    main()

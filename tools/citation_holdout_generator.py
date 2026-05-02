#!/usr/bin/env python3
"""Generate held-out test queries for the citation precision pipeline.

Reads context from case-status.md / case-contacts.md / case-filings-tracker.md
and asks Claude Opus to produce diverse, realistic questions an attorney or
case advocate would ask. Excludes any question matching the calibration batch.

Output: one JSON object per line: {"query": "...", "category": "..."}
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


SYSTEM = """You are generating evaluation queries for a legal-evidence retrieval system. The system answers questions about Captain Adam Taylor's military legal case (Air Force, IDES board, mental health discharge, OSI/SAPR investigations, congressional outreach).

Generate REALISTIC questions that an attorney, case advocate, or congressional staffer would ask the system. Coverage requirement:
- 12 EVIDENTIARY (do we have proof of X? what does document Y say?)
- 6 REGULATORY (what regulation requires X? what's the deadline under Y?)
- 6 PERSON (who is X? what role? what did X do?)
- 6 CHRONOLOGICAL (what happened on date X? sequence of events Y?)
- 5 STRATEGIC (should we file X? what's the risk of Y?)

CRITICAL RULES:
1. Output ONLY valid JSONL — one {"query": "...", "category": "..."} per line. No preamble, no markdown.
2. Each question must be ANSWERABLE from documents likely in the case archive — don't ask about things outside the case scope (e.g. don't ask about general statistics unrelated to Adam's case).
3. AVOID these calibration-batch topics specifically (do NOT generate near-duplicates):
   - SA Grice / OSI confirmation language in the talking-points memo
   - The exact "Triggered by Referral OPB" clinical-summary phrase
   - The Lujan letter "criminal misconduct" phrase
   - Adam never receiving DD 2701 / OSI case number / VWAP contact
   - The 2024-04-29 audio recording's contents
   - The Cannon AFB 11 recording's contents
   - The Lt Taylor pt.1 recording's contents
   - QAI process status from the Legal Tracker
   - QAI interview/review record from the Master Case Brief
   - Col Earles MFR refusal in the Legal Tracker
   - SMO bypass / commander contact from MASTER_05
4. Each question must reference SPECIFIC nouns (a person name, a regulation number, a date, a document title) so it's a focused retrieval task — not a vague "tell me about the case."
5. Questions can probe NEW aspects of documents the calibration batch already covered, just not the same exact facts.

Example good questions:
- {"query": "What does the IDES timeline document about the Apr 13 HAF call's outcomes?", "category": "evidentiary"}
- {"query": "What is the regulatory deadline for an MEB rebuttal under DoDI 1332.18?", "category": "regulatory"}
- {"query": "Who is Tolin and what role does he play in the case?", "category": "person"}

Generate exactly 35 questions covering all five categories. Output JSONL only."""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="AI_Studio/Reports/scheduled/citation_holdout_queries_v1.jsonl")
    p.add_argument("--model", default="claude-opus-4-7")
    p.add_argument("--n", type=int, default=35)
    args = p.parse_args()

    api_key = load_env_key()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    # Build context from memory files
    context_files = [
        "memory/case-status.md",
        "memory/case-contacts.md",
        "memory/case-filings-tracker.md",
    ]
    parts = []
    for cf in context_files:
        path = REPO_ROOT / ".." / "VoxCore" / cf  # adjust if needed
        # Actually the memory files live under ~/.claude/projects/...
        candidate_paths = [
            Path(os.path.expanduser(f"~/.claude/projects/C--Users-atayl-VoxCore/{cf}")),
            REPO_ROOT / cf,
        ]
        for p_ in candidate_paths:
            if p_.exists():
                parts.append(f"=== {cf} ===\n" + p_.read_text(encoding='utf-8')[:3000])
                break
        else:
            print(f"  warning: {cf} not found", file=sys.stderr)
    context = "\n\n".join(parts)

    user_msg = (
        f"Case context:\n\n{context}\n\n---\n\n"
        f"Generate exactly {args.n} held-out evaluation queries as JSONL per the spec."
    )

    body = json.dumps({
        "model": args.model,
        "max_tokens": 4000,
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

    # Parse JSONL — one JSON object per line, ignore preamble/markdown if model added any
    queries = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
            if "query" in obj and "category" in obj:
                queries.append(obj)
        except json.JSONDecodeError:
            continue

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(json.dumps(q, ensure_ascii=False) for q in queries) + "\n",
                        encoding="utf-8")

    usage = payload.get("usage", {})
    cost = (usage.get("input_tokens", 0) * 15 + usage.get("output_tokens", 0) * 75) / 1_000_000
    print(f"Generated {len(queries)} queries to {out_path}")
    print(f"Tokens: {usage.get('input_tokens', 0)} in + {usage.get('output_tokens', 0)} out = ~${cost:.3f}")
    # Sanity print: category distribution
    cats = {}
    for q in queries:
        cats[q.get("category", "?")] = cats.get(q.get("category", "?"), 0) + 1
    print(f"Category distribution: {cats}")


if __name__ == "__main__":
    main()

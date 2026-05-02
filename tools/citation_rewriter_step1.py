#!/usr/bin/env python3
"""Rewrite a batch of /ex-ask answers under one-quote-per-claim discipline.

Step 1 of the path to <2% hallucination. Tests the synthesis-stage prompt change
in isolation: feed the existing (query, answer) pairs to Claude Opus with the
new discipline instruction, get back disciplined answers, score them.

Skips the multi-agent fan-out — that stage already hits precision=1.0, recall=1.0,
so the loss is entirely at synthesis. Cheap way to measure the prompt's effect
without paying the full /ex-ask cost.

Usage:
    python tools/citation_rewriter_step1.py \
        --in AI_Studio/Reports/scheduled/citation_batch_n15_inline_20260502.jsonl \
        --out AI_Studio/Reports/scheduled/citation_batch_n15_step1_<ts>.jsonl
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_env_key() -> str:
    """Load ANTHROPIC_API_KEY from env or tools/ai_studio/.env."""
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if key:
        return key
    env_path = REPO_ROOT / "tools" / "ai_studio" / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY"):
                _, _, val = line.partition("=")
                return val.strip().strip('"').strip("'")
    return ""


REWRITE_SYSTEM = """You are a legal-evidence answer rewriter enforcing one-quote-per-claim discipline.

You will receive a draft answer about a legal case. Your job is to rewrite it so that EVERY factual sentence is one of two kinds:

[grounded] — A sentence stating a single specific fact (one date, one name, one amount, one finding) that appears verbatim in a single source. The sentence MUST be followed by an inline citation in the form `path/to/file.ext`: "verbatim quote covering that exact fact". The quote MUST contain the specific fact being asserted — not a topically-related quote.

[synthesis] — A sentence that derives, summarizes, or infers across multiple sources, OR commentary on the evidence. Tag the sentence with [synthesis] (literal token) and list source paths in parentheses. Does NOT require a verbatim quote.

ABSOLUTE RULES:
1. NEVER bundle 2+ independent facts into one sentence under one quote. Split into separate sentences.
2. The verbatim quote MUST contain the specific fact. If the source doesn't contain a verbatim sentence for the specific fact (just the topic), re-tag the sentence as [synthesis] or drop it.
3. Use ONLY citation paths and quotes that already appear in the input draft. Do NOT invent new sources or new quotes. If the input draft cites `foo.md` with quote "X", you may use that. You MAY drop a citation/quote if you re-tag the sentence as [synthesis].
4. Preserve the answer's substance — don't drop facts unless they truly cannot be grounded under the rules above.
5. Output ONLY the rewritten answer text. No preamble, no explanation, no markdown wrapping.

Bad example (input):
"The same memo documents that Capt Taylor never received DD 2701, an OSI case number, or VWAP contact. `02_TALKING_POINTS.md`: \"SA Grice did not confirm or deny that an active investigation exists\"."

Why bad: One sentence asserts THREE facts (no DD 2701, no OSI case number, no VWAP contact) but the quote is about something else (SA Grice).

Good rewrite (output):
"[synthesis] The memo documents that Capt Taylor never received DD 2701, an OSI case number, or VWAP contact (sources: `02_TALKING_POINTS.md`)."
— OR if the source actually contains verbatim quotes for each fact, split into three [grounded] sentences each with its own quote.

When unsure between [grounded] and [synthesis]: choose [synthesis]. False [grounded] tags get scored FABRICATED."""


REWRITE_USER = """Rewrite this answer under the one-quote-per-claim discipline. Output only the rewritten answer.

QUESTION: {query}

DRAFT ANSWER:
{answer}

REWRITTEN ANSWER:"""


def call_claude(query: str, answer: str, api_key: str,
                model: str = "claude-opus-4-7") -> str:
    """Call Claude API to rewrite a single answer."""
    body = json.dumps({
        "model": model,
        "max_tokens": 2000,
        "system": REWRITE_SYSTEM,
        "messages": [
            {"role": "user", "content": REWRITE_USER.format(query=query, answer=answer)},
        ],
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
    usage = payload.get("usage", {})
    return text.strip(), usage


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="input_path", required=True,
                   help="Input JSONL with {query, answer} per line")
    p.add_argument("--out", dest="output_path", required=True,
                   help="Output JSONL with rewritten {query, answer} per line")
    p.add_argument("--model", default="claude-opus-4-7")
    args = p.parse_args()

    api_key = load_env_key()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set and not in tools/ai_studio/.env",
              file=sys.stderr)
        sys.exit(1)

    in_path = Path(args.input_path)
    out_path = Path(args.output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = [json.loads(line) for line in in_path.read_text(encoding="utf-8").splitlines()
            if line.strip()]
    print(f"Rewriting {len(rows)} answers with {args.model}...")

    out_lines = []
    total_in = 0
    total_out = 0
    for i, row in enumerate(rows, 1):
        query = row["query"]
        answer = row["answer"]
        t0 = time.time()
        try:
            rewritten, usage = call_claude(query, answer, api_key, model=args.model)
        except Exception as e:
            print(f"  [{i}/{len(rows)}] ERROR: {e}", file=sys.stderr)
            rewritten = answer  # fallback to original
            usage = {}
        dt = time.time() - t0
        in_tok = usage.get("input_tokens", 0)
        out_tok = usage.get("output_tokens", 0)
        total_in += in_tok
        total_out += out_tok
        print(f"  [{i}/{len(rows)}] {dt:.1f}s in={in_tok} out={out_tok} -- {query[:60]}")
        out_lines.append(json.dumps({"query": query, "answer": rewritten}, ensure_ascii=False))

    out_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    # Pricing as of Opus 4.7: $15/MTok in, $75/MTok out
    cost = (total_in * 15 + total_out * 75) / 1_000_000
    print(f"\nWrote {len(out_lines)} rewrites to {out_path}")
    print(f"Tokens: {total_in} in + {total_out} out  =  ~${cost:.3f}")


if __name__ == "__main__":
    main()

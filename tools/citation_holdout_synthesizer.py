#!/usr/bin/env python3
"""Synthesize answers for held-out queries using hybrid retrieval + Phase 2 prompt.

This is a mini-/ex-ask: skips the multi-agent fan-out (precision/recall already
maxed in the calibration batch) and tests only the synthesis stage with the new
one-quote-per-claim discipline.

For each query:
  1. Hybrid search (FTS5 + ChromaDB RRF) → top-K chunks
  2. Fetch full chunk content from FTS index
  3. Send query + chunks to Claude Opus with the Phase 2 prompt
  4. Output {query, answer} JSONL line

Output is the same format citation_scorer.py expects.
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"


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


def hybrid_search(query: str, top_k: int = 5) -> list[dict]:
    """Call excluded_hybrid_search.py via subprocess to avoid import overhead."""
    try:
        result = subprocess.run(
            ["python", str(REPO_ROOT / "tools" / "excluded_hybrid_search.py"),
             query, "--top-k", str(top_k), "--json"],
            capture_output=True, text=True, timeout=60, encoding="utf-8", errors="replace",
        )
        if result.returncode != 0:
            return []
        data = json.loads(result.stdout)
        return data.get("hits", [])
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return []


def fetch_full_chunk(rel_path: str, chunk_idx: int | None,
                      fts_conn: sqlite3.Connection) -> str:
    """Get the full content of a chunk from the FTS index."""
    c = fts_conn.cursor()
    if chunk_idx is not None:
        rows = c.execute(
            "SELECT content FROM chunks WHERE rel_path = ? AND chunk_idx = ? LIMIT 1",
            (rel_path, chunk_idx),
        ).fetchall()
        if rows:
            return rows[0][0] or ""
    # Fallback: any chunk with this path
    rows = c.execute(
        "SELECT content FROM chunks WHERE rel_path = ? LIMIT 1",
        (rel_path,),
    ).fetchall()
    return (rows[0][0] if rows else "") or ""


SYNTH_SYSTEM = """You are a legal-evidence answerer enforcing one-quote-per-claim discipline.

Given a question and 3-5 source chunks, produce an answer where every factual sentence is one of two kinds:

[grounded] — The sentence states a single specific fact (one date, one name, one amount, one finding) that appears verbatim in a single source. It MUST be followed by an inline citation in the form `path/to/file.ext`: "verbatim quote covering this exact fact". The quote MUST contain the specific fact being asserted.

[synthesis] — The sentence is a derivation, summary, or inference across multiple sources, OR commentary on the evidence. Tag with [synthesis] (literal token) and list source paths in parentheses. Does NOT require a verbatim quote.

ABSOLUTE RULES:
1. NEVER bundle 2+ independent facts into one sentence under one quote. Split.
2. The verbatim quote MUST contain the specific fact (not just the topic).
3. Use ONLY citation paths from the SOURCE CHUNKS provided below. Do NOT invent paths.
4. If the source chunks do NOT contain the answer, output: "The provided sources do not address this question. [synthesis] (sources: none)"
5. Output ONLY the answer text. No preamble.

When the source contains the answer:
- Quote ONLY the verbatim text from the source. Use double-quoted strings. If the source quote contains an inner double-quote, write it as a curly quote ("...") instead of escaping with backslash.
- Keep answers focused (3-6 sentences max). Quality over length.
- When unsure between [grounded] and [synthesis]: choose [synthesis]."""


SYNTH_USER_TMPL = """QUESTION: {query}

SOURCE CHUNKS:

{chunks}

ANSWER (apply one-quote-per-claim discipline):"""


def call_claude_synth(query: str, chunks: list[dict], api_key: str,
                       model: str = "claude-opus-4-7") -> tuple[str, dict]:
    chunks_text = "\n\n---\n\n".join(
        f"[{i+1}] PATH: {c['rel_path']}\n\n{c['content']}"
        for i, c in enumerate(chunks)
    )
    body = json.dumps({
        "model": model,
        "max_tokens": 1500,
        "system": SYNTH_SYSTEM,
        "messages": [{"role": "user", "content": SYNTH_USER_TMPL.format(
            query=query, chunks=chunks_text,
        )}],
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
    with urllib.request.urlopen(req, timeout=180) as resp:
        payload = json.loads(resp.read())
    text = ""
    for block in payload.get("content", []):
        if block.get("type") == "text":
            text += block.get("text", "")
    return text.strip(), payload.get("usage", {})


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--queries", required=True, help="JSONL of {query, category} objects")
    p.add_argument("--out", required=True, help="Output JSONL of {query, answer}")
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--model", default="claude-opus-4-7")
    p.add_argument("--max-content-chars", type=int, default=2000,
                   help="Trim each chunk to this many characters")
    args = p.parse_args()

    api_key = load_env_key()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    queries = [json.loads(line) for line in Path(args.queries).read_text(encoding='utf-8').splitlines()
               if line.strip()]
    print(f"Synthesizing answers for {len(queries)} queries with {args.model}...")

    fts_conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_lines = []
    total_in = total_out = 0
    t_start = time.time()
    for i, q in enumerate(queries, 1):
        query = q["query"]
        # 1. Hybrid retrieval
        hits = hybrid_search(query, top_k=args.top_k)
        # 2. Fetch full chunk content
        chunks = []
        seen_paths = set()
        for h in hits:
            rp = h.get("rel_path", "")
            if not rp or rp in seen_paths:
                continue
            seen_paths.add(rp)
            content = fetch_full_chunk(rp, h.get("chunk_idx"), fts_conn)
            if content:
                chunks.append({"rel_path": rp, "content": content[:args.max_content_chars]})
            if len(chunks) >= args.top_k:
                break

        if not chunks:
            out_lines.append(json.dumps({
                "query": query,
                "answer": "The provided sources do not address this question. [synthesis] (sources: none)",
            }, ensure_ascii=False))
            print(f"  [{i}/{len(queries)}] (no chunks) -- {query[:60]}")
            continue

        # 3. Synthesize
        t0 = time.time()
        try:
            answer, usage = call_claude_synth(query, chunks, api_key, model=args.model)
        except Exception as e:
            print(f"  [{i}/{len(queries)}] ERROR: {e}", file=sys.stderr)
            answer = "The provided sources do not address this question. [synthesis] (sources: none)"
            usage = {}
        dt = time.time() - t0
        in_tok = usage.get("input_tokens", 0)
        out_tok = usage.get("output_tokens", 0)
        total_in += in_tok
        total_out += out_tok
        print(f"  [{i:>2}/{len(queries)}] {dt:.1f}s in={in_tok} out={out_tok} chunks={len(chunks)} -- {query[:55]}")
        out_lines.append(json.dumps({"query": query, "answer": answer}, ensure_ascii=False))

    fts_conn.close()
    out_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    cost = (total_in * 15 + total_out * 75) / 1_000_000
    elapsed = time.time() - t_start
    print(f"\nWrote {len(out_lines)} answers to {out_path}")
    print(f"Tokens: {total_in} in + {total_out} out = ~${cost:.3f}")
    print(f"Wall time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()

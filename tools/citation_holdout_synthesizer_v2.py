#!/usr/bin/env python3
"""Synthesize answers under one-quote-per-claim discipline + post-synth verify-retry.

v2 of the held-out synthesizer. Adds two changes vs v1:

1. **Tighter prompt.** Reinforces that quotes MUST be character-for-character
   verbatim from the SOURCE CHUNKS provided — no rephrasing, no cleanup, no
   adding/removing punctuation. If the source doesn't contain the exact text
   the model wants to assert, the sentence is re-tagged [synthesis] (no quote)
   or dropped.

2. **Verify-retry loop.** After first-pass synthesis, every extracted inline
   quote is substring-verified against its cited source. Quotes that fail
   verification are sent back to Claude with: "the following quotes were not
   found verbatim in the cited sources. Replace each one with either (a) a
   verbatim quote that IS in the source chunks below, or (b) a [synthesis]
   tag (drop the quote, list the sources)." Up to ``--max-retries`` retry
   iterations (default 2).

This targets the n=24 FABRICATED catches from the n=35 held-out batch
measured 2026-05-02. Expected impact: FABRICATED 24 → ~3, held-out
hallucination 30% → ~25%.
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

# Ensure tools/ is importable so we can reuse inline_grounding without packaging
sys.path.insert(0, str(REPO_ROOT / "tools"))
from inline_grounding import extract_inline_quotes, verify_quote_in_file  # noqa: E402


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
    c = fts_conn.cursor()
    if chunk_idx is not None:
        rows = c.execute(
            "SELECT content FROM chunks WHERE rel_path = ? AND chunk_idx = ? LIMIT 1",
            (rel_path, chunk_idx),
        ).fetchall()
        if rows:
            return rows[0][0] or ""
    rows = c.execute(
        "SELECT content FROM chunks WHERE rel_path = ? LIMIT 1",
        (rel_path,),
    ).fetchall()
    return (rows[0][0] if rows else "") or ""


SYNTH_SYSTEM_V2 = """You are a legal-evidence answerer enforcing one-quote-per-claim discipline with VERBATIM-ONLY quotes.

Given a question and 3-5 source chunks, produce an answer where every factual sentence is one of two kinds:

[grounded] — The sentence states a single specific fact (one date, one name, one amount, one finding) that appears verbatim in a single source. It MUST be followed by an inline citation in the form `path/to/file.ext`: "verbatim quote covering this exact fact". The quote MUST be character-for-character identical to text in the SOURCE CHUNKS — no rephrasing, no cleanup, no added or removed punctuation, no added or removed capitalization, no smoothing of awkward original phrasing.

[synthesis] — The sentence is a derivation, summary, or inference across multiple sources, OR commentary on the evidence. Tag with [synthesis] (literal token) and list source paths in parentheses. Does NOT require a verbatim quote.

THE FABRICATION TEST: Before writing any quote, copy it character-by-character from the SOURCE CHUNKS section below. If you cannot point to the exact text in a chunk, the quote is fabricated and will be flagged FABRICATED at scoring time. When in doubt:
- Prefer a SHORTER verbatim quote you can copy exactly.
- Prefer [synthesis] tag with NO quote over a paraphrased "almost-verbatim" quote.
- Prefer to drop a sentence entirely over inventing a plausible-sounding quote.

ABSOLUTE RULES:
1. NEVER bundle 2+ independent facts into one sentence under one quote. Split into separate sentences.
2. The verbatim quote MUST contain the specific fact (not just the topic).
3. Use ONLY citation paths from the SOURCE CHUNKS provided. Do NOT invent paths.
4. If the source chunks do NOT contain a verbatim sentence supporting a claim, the sentence is [synthesis] OR is dropped — NEVER [grounded] with an invented quote.
5. If the source chunks do NOT contain the answer at all, output: "The provided sources do not address this question. [synthesis] (sources: none)"
6. Output ONLY the answer text. No preamble.

Quote-formatting rule: use double-quoted strings. If the source quote contains an inner double-quote, write it as a curly quote ("...") instead of escaping with a backslash.

When unsure between [grounded] and [synthesis]: choose [synthesis]. False [grounded] tags are scored FABRICATED."""


SYNTH_USER_TMPL = """QUESTION: {query}

SOURCE CHUNKS:

{chunks}

ANSWER (apply one-quote-per-claim discipline; quotes MUST be verbatim from the SOURCE CHUNKS above):"""


RETRY_USER_TMPL = """The following quotes in your previous answer were NOT found verbatim in the cited source chunks. They are flagged FABRICATED.

For each one, you must EITHER:
  (a) replace it with a different quote that IS verbatim in the source chunks I provided, OR
  (b) re-tag that sentence as [synthesis] and remove the inline quote (list the source paths in parentheses instead).

DO NOT keep the fabricated quote. DO NOT invent a different quote that's still not in the source. DO NOT add new claims.

Failed quotes from your previous answer:

{failed_list}

PREVIOUS ANSWER:
{prev_answer}

ORIGINAL QUESTION: {query}

SOURCE CHUNKS (the only quotes you may use):

{chunks}

REVISED ANSWER (every [grounded] quote must be character-for-character in the SOURCE CHUNKS above):"""


def call_claude(messages: list[dict], system: str, api_key: str,
                 model: str = "claude-opus-4-7", max_tokens: int = 1500
                 ) -> tuple[str, dict]:
    body = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "messages": messages,
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


def verify_all_quotes(answer: str, fts_conn: sqlite3.Connection) -> list[dict]:
    """Extract every inline quote from the answer and verify each. Returns the
    list of FAILED ones (verified=False) — same shape as inline_grounding output
    plus the verifier's reason field.
    """
    quotes = extract_inline_quotes(answer)
    failed = []
    for q in quotes:
        v = verify_quote_in_file(q["quote"], q["path"], fts_conn=fts_conn)
        if not v["verified"]:
            failed.append({
                "path": q["path"],
                "quote": q["quote"],
                "reason": v.get("reason", ""),
            })
    return failed


def synthesize_with_retry(query: str, chunks: list[dict], fts_conn: sqlite3.Connection,
                           api_key: str, model: str, max_retries: int) -> dict:
    """First-pass synthesis + up-to-N retry passes for FABRICATED quotes."""
    chunks_text = "\n\n---\n\n".join(
        f"[{i+1}] PATH: {c['rel_path']}\n\n{c['content']}"
        for i, c in enumerate(chunks)
    )
    user_first = SYNTH_USER_TMPL.format(query=query, chunks=chunks_text)
    messages = [{"role": "user", "content": user_first}]

    iters = []
    answer = ""
    total_in = total_out = 0
    failed_quotes = []
    for attempt in range(max_retries + 1):
        try:
            answer, usage = call_claude(messages, SYNTH_SYSTEM_V2, api_key, model=model)
        except Exception as e:
            return {
                "answer": "The provided sources do not address this question. [synthesis] (sources: none)",
                "iterations": iters,
                "error": str(e),
                "tokens_in": total_in, "tokens_out": total_out,
            }
        in_tok = usage.get("input_tokens", 0)
        out_tok = usage.get("output_tokens", 0)
        total_in += in_tok
        total_out += out_tok

        failed_quotes = verify_all_quotes(answer, fts_conn)
        iters.append({
            "attempt": attempt,
            "answer_chars": len(answer),
            "in_tok": in_tok, "out_tok": out_tok,
            "failed_quotes_count": len(failed_quotes),
            "failed_quotes": [{"path": fq["path"], "quote": fq["quote"][:120]} for fq in failed_quotes],
        })
        if not failed_quotes:
            break  # all quotes verified; we're done
        if attempt == max_retries:
            break  # out of retries; ship as-is and let the scorer FABRICATE-flag

        # Build retry message — append assistant + new user turn
        failed_list = "\n".join(
            f'  - in `{fq["path"]}`: "{fq["quote"][:200]}"'
            for fq in failed_quotes
        )
        retry_user = RETRY_USER_TMPL.format(
            failed_list=failed_list,
            prev_answer=answer,
            query=query,
            chunks=chunks_text,
        )
        messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": retry_user})

    return {
        "answer": answer,
        "iterations": iters,
        "final_failed_quotes": len(failed_quotes),
        "tokens_in": total_in,
        "tokens_out": total_out,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--queries", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--model", default="claude-opus-4-7")
    p.add_argument("--max-content-chars", type=int, default=2000)
    p.add_argument("--max-retries", type=int, default=2,
                   help="Verify-retry passes after first synthesis (default 2)")
    p.add_argument("--meta-out", default=None,
                   help="Optional JSON file for per-query iteration metadata")
    args = p.parse_args()

    api_key = load_env_key()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    queries = [json.loads(line) for line in Path(args.queries).read_text(encoding='utf-8').splitlines()
               if line.strip()]
    print(f"v2 Synthesizing {len(queries)} queries with {args.model} "
          f"(max-retries={args.max_retries}, verify-retry on FABRICATED)")

    fts_conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_lines = []
    meta = []
    total_in = total_out = 0
    fab_first_pass = fab_final = 0
    queries_retried = 0
    queries_fully_resolved_after_retry = 0
    t_start = time.time()

    for i, q in enumerate(queries, 1):
        query = q["query"]
        hits = hybrid_search(query, top_k=args.top_k)
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
            meta.append({"query": query, "iterations": [], "no_chunks": True})
            print(f"  [{i}/{len(queries)}] (no chunks) -- {query[:55]}")
            continue

        t0 = time.time()
        result = synthesize_with_retry(query, chunks, fts_conn, api_key, args.model, args.max_retries)
        dt = time.time() - t0
        total_in += result["tokens_in"]
        total_out += result["tokens_out"]
        n_iters = len(result["iterations"])
        first_fab = result["iterations"][0]["failed_quotes_count"] if result["iterations"] else 0
        final_fab = result.get("final_failed_quotes", 0)
        fab_first_pass += first_fab
        fab_final += final_fab
        if n_iters > 1:
            queries_retried += 1
            if final_fab == 0:
                queries_fully_resolved_after_retry += 1

        retry_marker = f" RETRIED({n_iters - 1})" if n_iters > 1 else ""
        fab_marker = f" FAB:{first_fab}->{final_fab}" if first_fab > 0 else ""
        print(f"  [{i:>2}/{len(queries)}] {dt:.1f}s in={result['tokens_in']} out={result['tokens_out']}"
              f" chunks={len(chunks)}{retry_marker}{fab_marker} -- {query[:50]}")
        out_lines.append(json.dumps({"query": query, "answer": result["answer"]},
                                    ensure_ascii=False))
        meta.append({"query": query, "iterations": result["iterations"], "no_chunks": False})

    fts_conn.close()
    out_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    if args.meta_out:
        Path(args.meta_out).write_text(json.dumps(meta, indent=2, ensure_ascii=False),
                                       encoding="utf-8")

    cost = (total_in * 15 + total_out * 75) / 1_000_000
    elapsed = time.time() - t_start
    print(f"\n=== v2 Synthesis summary ===")
    print(f"  Wrote {len(out_lines)} answers to {out_path}")
    print(f"  Tokens: {total_in} in + {total_out} out = ~${cost:.3f}")
    print(f"  Wall time: {elapsed:.1f}s")
    print(f"  Queries with first-pass FABRICATED:  ~{queries_retried} (retried)")
    print(f"  Total FABRICATED first-pass: {fab_first_pass}  →  final after retry: {fab_final}")
    print(f"  Queries fully resolved by retry: {queries_fully_resolved_after_retry}/{queries_retried}")


if __name__ == "__main__":
    main()

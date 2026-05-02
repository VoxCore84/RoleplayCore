#!/usr/bin/env python3
"""v3 synthesizer — v2 verify-retry PLUS per-claim re-retrieval.

Targets the 147 IRRELEVANT verdicts on the v2 held-out batch. v2 fixed
FABRICATED→0 by forcing verbatim quotes, but the quotes the model picked
were often on-topic-but-not-fact-supporting because the original top-5
hybrid retrieval didn't include the chunk that contains the specific fact.

v3 pipeline:
  1. v2 first-pass synthesis (with FABRICATED verify-retry up to 2 passes)
  2. Parse [grounded] sentences from the answer
  3. For each [grounded] sentence, extract the clean claim text and run a
     focused hybrid_search(claim_text, top_k=3) — gives us chunks selected
     for THAT specific claim
  4. If new chunks appear (not in the original retrieval), pass {original
     chunks + per-claim augmented chunks + previous answer} back to Claude
     with a "swap-quote-only-if-better" prompt
  5. Final FABRICATED verify-retry on the rewritten answer

Net effect: model gets a second chance to find a verbatim quote that
actually contains the claim's specific fact, drawn from a chunk pool
chosen for THAT claim — not for the original query.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"

sys.path.insert(0, str(REPO_ROOT / "tools"))
from inline_grounding import extract_inline_quotes, verify_quote_in_file  # noqa: E402

# Reuse v2's prompts and helpers
from citation_holdout_synthesizer_v2 import (  # noqa: E402
    SYNTH_SYSTEM_V2, SYNTH_USER_TMPL, RETRY_USER_TMPL,
    load_env_key, hybrid_search, fetch_full_chunk,
    call_claude, verify_all_quotes, synthesize_with_retry,
)


# Use inline_grounding to find every (path, quote, span_in_text) and walk
# backward to find the claim sentence preceding each citation. This is more
# robust than matching [grounded] tags because the model's tag placement is
# inconsistent ("claim. [grounded] cite" vs "[grounded] claim. cite").
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")
_GROUNDED_TAG_STRIP_RE = re.compile(
    r"(?:^\s*\[grounded\]\s*|\s*\[grounded\]\s*$)", re.IGNORECASE
)
_LEGACY_GROUNDED_TAG_RE = re.compile(r"\[grounded\]", re.IGNORECASE)


def extract_grounded_claims(answer: str) -> list[str]:
    """For each inline (path, quote) pair in the answer, return the claim text
    that immediately precedes the citation — the sentence the citation is
    supposed to support. Falls back to walking back through additional
    sentences if the immediate predecessor is itself a citation line.
    """
    quotes = extract_inline_quotes(answer)
    claims: list[str] = []
    for q in quotes:
        cite_start = q["span_in_text"][0]
        preceding = answer[:cite_start]
        sentences = _SENTENCE_END_RE.split(preceding)
        # Walk back through sentences until we find one that's not itself a
        # citation line (heuristic: contains a backtick path + colon)
        for s in reversed(sentences):
            s = s.strip()
            if not s:
                continue
            s_clean = _GROUNDED_TAG_STRIP_RE.sub("", s).strip()
            # Skip if this is itself a citation line
            if re.search(r"`[^`\n]+`\s*:\s*[\"“]", s_clean):
                continue
            if len(s_clean) >= 15:
                claims.append(s_clean.rstrip(".:"))
                break
    # Dedupe (a single claim can appear with multiple supporting citations)
    seen = set()
    deduped = []
    for c in claims:
        key = c.lower()[:60]
        if key in seen:
            continue
        seen.add(key)
        deduped.append(c)
    return deduped


REFINE_SYSTEM_V3 = SYNTH_SYSTEM_V2 + """

IMPORTANT FOR THIS REVISION PASS: You will be given (a) the question, (b) your previous answer, (c) the ORIGINAL chunks, and (d) ADDITIONAL CHUNKS retrieved specifically for each [grounded] claim in your previous answer. Your job is to look for BETTER verbatim quotes that more directly support each claim's specific fact.

Rules for this pass:
- DO NOT add new claims.
- DO NOT drop any claim that's still supported.
- You MAY replace an inline quote with a different verbatim quote IF the new quote better contains the specific fact the claim asserts.
- The replacement quote MUST be verbatim from one of the chunks below (original OR additional).
- If no chunk contains a better verbatim, KEEP the previous quote.
- If even the previous quote does not actually contain the specific fact, re-tag the sentence as [synthesis] and remove the inline quote.
- Output the final answer ONLY."""


REFINE_USER_TMPL = """QUESTION: {query}

PREVIOUS ANSWER:
{prev_answer}

ORIGINAL CHUNKS:

{original_chunks}

ADDITIONAL CHUNKS (retrieved per-claim for the [grounded] sentences in your previous answer):

{augmented_chunks}

REVISED ANSWER (swap inline quotes only if a better verbatim is available; do not add or drop claims):"""


def gather_per_claim_chunks(claims: list[str], existing_paths: set[str],
                              fts_conn: sqlite3.Connection,
                              max_per_claim: int = 3,
                              max_content_chars: int = 1500) -> list[dict]:
    """For each claim, run hybrid_search and collect chunks not in existing_paths."""
    augmented: list[dict] = []
    seen = set(existing_paths)
    for claim in claims:
        try:
            hits = hybrid_search(claim, top_k=max_per_claim)
        except Exception:
            continue
        for h in hits:
            rp = h.get("rel_path", "")
            if not rp or rp in seen:
                continue
            seen.add(rp)
            content = fetch_full_chunk(rp, h.get("chunk_idx"), fts_conn)
            if content:
                augmented.append({"rel_path": rp, "content": content[:max_content_chars]})
    return augmented


def synthesize_v3(query: str, chunks: list[dict], fts_conn: sqlite3.Connection,
                   api_key: str, model: str, max_retries: int) -> dict:
    """v2 first pass + per-claim re-retrieval refinement + final verify pass."""
    # 1. v2 first-pass with verify-retry
    v2_result = synthesize_with_retry(query, chunks, fts_conn, api_key, model, max_retries)
    answer = v2_result["answer"]
    total_in = v2_result["tokens_in"]
    total_out = v2_result["tokens_out"]

    # 2. Extract [grounded] claims
    claims = extract_grounded_claims(answer)
    if not claims:
        return {
            "answer": answer,
            "v2_iterations": v2_result["iterations"],
            "v3_refinement": "skipped — no [grounded] claims",
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    # 3. Per-claim re-retrieval — find new chunks
    existing_paths = {c["rel_path"] for c in chunks}
    augmented = gather_per_claim_chunks(claims, existing_paths, fts_conn)
    if not augmented:
        return {
            "answer": answer,
            "v2_iterations": v2_result["iterations"],
            "v3_refinement": f"skipped — no new chunks for {len(claims)} claims",
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    # 4. Refinement call — pass original + augmented + previous answer
    original_text = "\n\n---\n\n".join(
        f"[orig {i+1}] PATH: {c['rel_path']}\n\n{c['content']}"
        for i, c in enumerate(chunks)
    )
    augmented_text = "\n\n---\n\n".join(
        f"[aug {i+1}] PATH: {c['rel_path']}\n\n{c['content']}"
        for i, c in enumerate(augmented)
    )
    refine_user = REFINE_USER_TMPL.format(
        query=query,
        prev_answer=answer,
        original_chunks=original_text,
        augmented_chunks=augmented_text,
    )

    try:
        revised, usage = call_claude(
            [{"role": "user", "content": refine_user}],
            REFINE_SYSTEM_V3, api_key, model=model, max_tokens=1800,
        )
    except Exception as e:
        return {
            "answer": answer,
            "v2_iterations": v2_result["iterations"],
            "v3_refinement": f"refinement-call-failed: {e}",
            "v3_augmented_chunks": len(augmented),
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    refine_in = usage.get("input_tokens", 0)
    refine_out = usage.get("output_tokens", 0)
    total_in += refine_in
    total_out += refine_out

    # 5. Final FABRICATED verify pass on the revised answer
    failed = verify_all_quotes(revised, fts_conn)
    if failed:
        # Final retry on the revised answer
        failed_list = "\n".join(
            f'  - in `{fq["path"]}`: "{fq["quote"][:200]}"' for fq in failed
        )
        all_chunks_text = original_text + "\n\n---\n\n" + augmented_text
        final_retry_user = RETRY_USER_TMPL.format(
            failed_list=failed_list,
            prev_answer=revised,
            query=query,
            chunks=all_chunks_text,
        )
        try:
            revised2, usage2 = call_claude(
                [{"role": "user", "content": refine_user},
                 {"role": "assistant", "content": revised},
                 {"role": "user", "content": final_retry_user}],
                REFINE_SYSTEM_V3, api_key, model=model, max_tokens=1800,
            )
            total_in += usage2.get("input_tokens", 0)
            total_out += usage2.get("output_tokens", 0)
            revised = revised2
        except Exception:
            pass  # ship the revised answer with whatever residual fabrications

    return {
        "answer": revised,
        "v2_iterations": v2_result["iterations"],
        "v3_refinement": "applied",
        "v3_n_grounded_claims": len(claims),
        "v3_n_augmented_chunks": len(augmented),
        "v3_tokens_refine_in": refine_in,
        "v3_tokens_refine_out": refine_out,
        "v3_final_failed_quotes": len(verify_all_quotes(revised, fts_conn)),
        "tokens_in": total_in,
        "tokens_out": total_out,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--queries", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--top-k", type=int, default=8,
                   help="Initial chunk count (v2 used 5; v3 default 8 for more first-pass coverage)")
    p.add_argument("--model", default="claude-opus-4-7")
    p.add_argument("--max-content-chars", type=int, default=2000)
    p.add_argument("--max-retries", type=int, default=2)
    p.add_argument("--meta-out", default=None)
    args = p.parse_args()

    api_key = load_env_key()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    queries = [json.loads(line) for line in Path(args.queries).read_text(encoding='utf-8').splitlines()
               if line.strip()]
    print(f"v3 Synthesizing {len(queries)} queries with {args.model} "
          f"(initial top-k={args.top_k}, max-retries={args.max_retries}, +per-claim re-retrieval)")

    fts_conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_lines = []
    meta = []
    total_in = total_out = 0
    n_refined = n_skipped = 0
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
            meta.append({"query": query, "no_chunks": True})
            print(f"  [{i}/{len(queries)}] (no chunks) -- {query[:55]}")
            continue

        t0 = time.time()
        result = synthesize_v3(query, chunks, fts_conn, api_key, args.model, args.max_retries)
        dt = time.time() - t0
        total_in += result["tokens_in"]
        total_out += result["tokens_out"]
        if result.get("v3_refinement") == "applied":
            n_refined += 1
            marker = f" REFINED(claims={result.get('v3_n_grounded_claims')},aug={result.get('v3_n_augmented_chunks')})"
        else:
            n_skipped += 1
            marker = f" {result.get('v3_refinement', 'noop')}"
        print(f"  [{i:>2}/{len(queries)}] {dt:.1f}s in={result['tokens_in']} out={result['tokens_out']}"
              f" chunks={len(chunks)}{marker} -- {query[:42]}")
        out_lines.append(json.dumps({"query": query, "answer": result["answer"]},
                                    ensure_ascii=False))
        meta.append({"query": query, "no_chunks": False, **{k: v for k, v in result.items() if k != "answer"}})

    fts_conn.close()
    out_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    if args.meta_out:
        Path(args.meta_out).write_text(json.dumps(meta, indent=2, ensure_ascii=False),
                                       encoding="utf-8")

    cost = (total_in * 15 + total_out * 75) / 1_000_000
    elapsed = time.time() - t_start
    print(f"\n=== v3 Synthesis summary ===")
    print(f"  Wrote {len(out_lines)} answers to {out_path}")
    print(f"  Tokens: {total_in} in + {total_out} out = approx ${cost:.3f}")
    print(f"  Wall time: {elapsed:.1f}s")
    print(f"  Refined: {n_refined}/{len(queries)}; Skipped (no claims or no new chunks): {n_skipped}/{len(queries)}")


if __name__ == "__main__":
    main()

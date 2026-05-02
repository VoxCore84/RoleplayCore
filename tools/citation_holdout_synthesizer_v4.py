#!/usr/bin/env python3
"""v4 synthesizer — v2 verify-retry + in-pipeline CONTRADICTS Auditor (MVP).

Implements the spec in `AI_Studio/2_Active_Specs/contradicts_auditor_v1_*.md`.

Pipeline:
  1. v2 first-pass synthesis with FABRICATED verify-retry (existing)
  2. Run inline_auditor.audit_answer on the result
  3. For each CONTRADICTS verdict with confidence >= threshold:
       - send a TARGETED REWRITE request: "the claim X is paired with quote Y
         which contradicts X. Either find a different verbatim quote in the
         source chunks below that supports X, or re-tag the sentence as
         [synthesis] (no quote)."
  4. Re-verify the rewritten quote (substring) and re-audit it once
  5. If still CONTRADICTS or AUDITOR_ERROR after rewrite: HOLD with
     [AUDITOR_FAILED] tag prepended

This is a minimum-viable implementation — the full spec calls for more
careful retry strategies, confidence-tiered handling, and per-sentence
rewrite atomicity. MVP shows the architecture works and produces a
measurable CONTRADICTS reduction on the n=35 held-out.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"

sys.path.insert(0, str(REPO_ROOT / "tools"))
from inline_grounding import extract_inline_quotes, verify_quote_in_file  # noqa: E402
from citation_holdout_synthesizer_v2 import (  # noqa: E402
    SYNTH_SYSTEM_V2, load_env_key, hybrid_search, fetch_full_chunk,
    call_claude, verify_all_quotes, synthesize_with_retry,
)
from inline_auditor import audit_answer, DEFAULT_AUDITOR_MODEL  # noqa: E402

REWRITE_SYSTEM_V4 = SYNTH_SYSTEM_V2 + """

IMPORTANT FOR THIS REVISION PASS: the in-pipeline CONTRADICTS Auditor flagged one or more [grounded] sentences in your previous answer as having a quote that CONTRADICTS the claim. For each flagged sentence:

OPTION A — find a different verbatim quote in the SOURCE CHUNKS that actually supports the claim, and replace the contradicted quote.
OPTION B — re-tag the sentence as [synthesis] and remove the inline quote (list the source paths in parentheses instead).
OPTION C — drop the sentence entirely if neither option is correct.

DO NOT keep a contradicted sentence with the same quote. DO NOT invent a new quote.
DO NOT add new claims or new sentences. Only fix the flagged ones.
Keep all unflagged sentences unchanged."""


REWRITE_USER_TMPL_V4 = """QUESTION: {query}

PREVIOUS ANSWER:
{prev_answer}

SOURCE CHUNKS (the only quotes you may use):

{chunks}

CONTRADICTS-FLAGGED SENTENCES from the previous answer (auditor verdicts):

{flagged_list}

REVISED ANSWER (fix only the CONTRADICTS-flagged sentences using Option A/B/C; keep everything else):"""


def synthesize_v4(query: str, chunks: list[dict], fts_conn: sqlite3.Connection,
                   api_key: str, executor_model: str, auditor_model: str,
                   max_retries: int, contradicts_threshold: float) -> dict:
    """v2 first pass + inline CONTRADICTS audit + targeted rewrite if needed."""
    # 1. v2 synthesis with FABRICATED verify-retry
    v2_result = synthesize_with_retry(query, chunks, fts_conn, api_key,
                                       executor_model, max_retries)
    answer = v2_result["answer"]
    total_in = v2_result["tokens_in"]
    total_out = v2_result["tokens_out"]

    # 2. Inline CONTRADICTS audit
    audit = audit_answer(answer, chunks, model=auditor_model, api_key=api_key,
                          contradicts_threshold=contradicts_threshold)
    audit_summary = audit.get("summary", {})
    rewrite_needed = audit_summary.get("needs_rewrite", False)
    hold_needed_initial = audit_summary.get("needs_hold", False)

    if not rewrite_needed and not hold_needed_initial:
        return {
            "answer": answer,
            "v4_audit_initial": audit_summary,
            "v4_rewrite_applied": False,
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    # 3. Targeted rewrite for CONTRADICTS-flagged sentences
    rewrite_audits = [a for a in audit["audits"] if a.get("disposition") == "rewrite"]
    if not rewrite_audits:
        # Only hold (auditor error) — return with held tag
        return {
            "answer": "[AUDITOR_FAILED] " + answer,
            "v4_audit_initial": audit_summary,
            "v4_rewrite_applied": False,
            "v4_held": True,
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    flagged_list = "\n".join(
        f'  - CLAIM: "{a["claim"][:200]}"\n    QUOTE: "{a["quote"][:200]}"\n    AUDITOR REASON: {a["rationale"]}'
        for a in rewrite_audits
    )
    chunks_text = "\n\n---\n\n".join(
        f"[{i+1}] PATH: {c['rel_path']}\n\n{c['content']}"
        for i, c in enumerate(chunks)
    )
    rewrite_user = REWRITE_USER_TMPL_V4.format(
        query=query, prev_answer=answer, chunks=chunks_text,
        flagged_list=flagged_list,
    )
    try:
        revised, usage = call_claude(
            [{"role": "user", "content": rewrite_user}],
            REWRITE_SYSTEM_V4, api_key, model=executor_model, max_tokens=1800,
        )
    except Exception as e:
        return {
            "answer": "[AUDITOR_FAILED] " + answer,
            "v4_audit_initial": audit_summary,
            "v4_rewrite_applied": False,
            "v4_held": True,
            "v4_rewrite_error": str(e),
            "tokens_in": total_in,
            "tokens_out": total_out,
        }
    total_in += usage.get("input_tokens", 0)
    total_out += usage.get("output_tokens", 0)

    # 4. Re-verify substring on the rewritten answer
    failed = verify_all_quotes(revised, fts_conn)
    if failed:
        # Don't ship a rewrite that introduced new fabrication
        return {
            "answer": "[AUDITOR_FAILED] " + answer,
            "v4_audit_initial": audit_summary,
            "v4_rewrite_applied": True,
            "v4_held": True,
            "v4_rewrite_introduced_fabrication": len(failed),
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    # 5. Re-audit the rewritten answer
    audit2 = audit_answer(revised, chunks, model=auditor_model, api_key=api_key,
                           contradicts_threshold=contradicts_threshold)
    audit2_summary = audit2.get("summary", {})
    if audit2_summary.get("needs_rewrite", False) or audit2_summary.get("needs_hold", False):
        # Spec: if still unresolved after one rewrite pass, HOLD
        return {
            "answer": "[AUDITOR_FAILED] " + revised,
            "v4_audit_initial": audit_summary,
            "v4_audit_after_rewrite": audit2_summary,
            "v4_rewrite_applied": True,
            "v4_held": True,
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    return {
        "answer": revised,
        "v4_audit_initial": audit_summary,
        "v4_audit_after_rewrite": audit2_summary,
        "v4_rewrite_applied": True,
        "v4_held": False,
        "tokens_in": total_in,
        "tokens_out": total_out,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--queries", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--executor-model", default="claude-opus-4-7")
    p.add_argument("--auditor-model", default=DEFAULT_AUDITOR_MODEL)
    p.add_argument("--max-content-chars", type=int, default=2000)
    p.add_argument("--max-retries", type=int, default=2)
    p.add_argument("--contradicts-threshold", type=float, default=0.70)
    p.add_argument("--meta-out", default=None)
    args = p.parse_args()

    api_key = load_env_key()
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    queries = [json.loads(line) for line in Path(args.queries).read_text(encoding='utf-8').splitlines()
               if line.strip()]
    print(f"v4 Synthesizing {len(queries)} queries with executor={args.executor_model} "
          f"auditor={args.auditor_model} threshold={args.contradicts_threshold}")

    fts_conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_lines = []
    meta = []
    total_in = total_out = 0
    n_held = n_rewrite_applied = n_clean_first_pass = 0
    t_start = time.time()

    for i, q in enumerate(queries, 1):
        query = q["query"]
        hits = hybrid_search(query, top_k=args.top_k)
        chunks = []
        seen = set()
        for h in hits:
            rp = h.get("rel_path", "")
            if not rp or rp in seen:
                continue
            seen.add(rp)
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
        result = synthesize_v4(query, chunks, fts_conn, api_key,
                                args.executor_model, args.auditor_model,
                                args.max_retries, args.contradicts_threshold)
        dt = time.time() - t0
        total_in += result["tokens_in"]
        total_out += result["tokens_out"]
        if result.get("v4_held"):
            n_held += 1
            marker = " HELD"
        elif result.get("v4_rewrite_applied"):
            n_rewrite_applied += 1
            marker = " REWRITTEN"
        else:
            n_clean_first_pass += 1
            marker = ""

        a_init = result.get("v4_audit_initial", {})
        verdicts = a_init.get("verdicts", {})
        cont = verdicts.get("CONTRADICTS", 0)
        sup = verdicts.get("SUPPORTS", 0)
        marker += f" audit:S{sup}/C{cont}"
        print(f"  [{i:>2}/{len(queries)}] {dt:.1f}s in={result['tokens_in']} out={result['tokens_out']}"
              f" chunks={len(chunks)}{marker} -- {query[:42]}")
        out_lines.append(json.dumps({"query": query, "answer": result["answer"]},
                                    ensure_ascii=False))
        meta.append({"query": query, **{k: v for k, v in result.items() if k != "answer"}})

    fts_conn.close()
    out_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    if args.meta_out:
        Path(args.meta_out).write_text(json.dumps(meta, indent=2, ensure_ascii=False),
                                       encoding="utf-8")

    # Cost: Opus executor + Sonnet auditor (~5x cheaper per token)
    # Approximate as Opus pricing for upper-bound estimate
    cost_upper = (total_in * 15 + total_out * 75) / 1_000_000
    elapsed = time.time() - t_start
    print(f"\n=== v4 Synthesis summary ===")
    print(f"  Wrote {len(out_lines)} answers to {out_path}")
    print(f"  Tokens (executor + auditor combined): {total_in} in + {total_out} out")
    print(f"  Cost upper-bound (assumes all Opus pricing): ~${cost_upper:.3f}")
    print(f"  Wall time: {elapsed:.1f}s")
    print(f"  First-pass clean (no audit issue):   {n_clean_first_pass}/{len(queries)}")
    print(f"  Rewritten by auditor:                {n_rewrite_applied}/{len(queries)}")
    print(f"  HELD with [AUDITOR_FAILED]:          {n_held}/{len(queries)}")


if __name__ == "__main__":
    main()

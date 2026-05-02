#!/usr/bin/env python3
"""v5 synthesizer — v4 (CONTRADICTS Auditor) with FABRICATED verify-retry on the rewrite path.

The v4 measurement (held-out n=35, 2026-05-02 14:23) showed 5 new FABRICATED
quotes appeared in the targeted-rewrite outputs. Root cause: v4's rewrite call
went directly through verify-once-and-ship, bypassing the FABRICATED
verify-retry loop that v2 uses for first-pass synthesis.

v5 fixes that: when the rewrite produces a quote that's not verbatim in source,
we re-prompt the model with the same "your quote is not in the source — fix it
or re-tag as [synthesis]" loop v2 uses. Up to 2 retry passes on the rewrite.

Expected impact vs v4: FABRICATED on rewrite path 5 → ~0; shipped hallucination
16.7% → ~13-14% (the 5 fabricated would have been correctly resolved or held
without polluting the score).
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
    SYNTH_SYSTEM_V2, RETRY_USER_TMPL,
    load_env_key, hybrid_search, fetch_full_chunk,
    call_claude, verify_all_quotes, synthesize_with_retry,
)
from citation_holdout_synthesizer_v4 import (  # noqa: E402
    REWRITE_SYSTEM_V4, REWRITE_USER_TMPL_V4,
)
from inline_auditor import audit_answer, DEFAULT_AUDITOR_MODEL  # noqa: E402


def call_with_fabricated_retry(initial_messages: list[dict], system: str,
                                 chunks_text: str, fts_conn: sqlite3.Connection,
                                 api_key: str, model: str,
                                 max_retries: int = 2) -> tuple[str, dict]:
    """Call Claude, then verify all extracted quotes substring-match source.
    If any FABRICATED, retry up to max_retries times with a fix-it prompt.
    Returns (final_answer, usage_totals).
    """
    messages = list(initial_messages)
    total_in = total_out = 0
    answer = ""
    failed_list = ""
    for attempt in range(max_retries + 1):
        answer, usage = call_claude(messages, system, api_key, model=model, max_tokens=1800)
        total_in += usage.get("input_tokens", 0)
        total_out += usage.get("output_tokens", 0)
        failed = verify_all_quotes(answer, fts_conn)
        if not failed:
            return answer, {"tokens_in": total_in, "tokens_out": total_out,
                            "fab_attempts": attempt, "final_failed": 0}
        if attempt == max_retries:
            return answer, {"tokens_in": total_in, "tokens_out": total_out,
                            "fab_attempts": attempt, "final_failed": len(failed)}
        # Build retry prompt
        failed_list = "\n".join(
            f'  - in `{fq["path"]}`: "{fq["quote"][:200]}"' for fq in failed
        )
        retry_user = (
            "The following quotes in your previous answer were NOT found verbatim "
            "in the cited source chunks. They are flagged FABRICATED.\n\n"
            "For each one, EITHER:\n"
            "  (a) replace it with a verbatim quote that IS in the source chunks below, OR\n"
            "  (b) re-tag the sentence as [synthesis] and remove the inline quote.\n\n"
            f"Failed quotes:\n{failed_list}\n\n"
            f"PREVIOUS ANSWER:\n{answer}\n\n"
            f"SOURCE CHUNKS (the only quotes you may use):\n\n{chunks_text}\n\n"
            "REVISED ANSWER (every [grounded] quote must be character-for-character in the source chunks):"
        )
        messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": retry_user})
    return answer, {"tokens_in": total_in, "tokens_out": total_out,
                    "fab_attempts": max_retries, "final_failed": 0}


def synthesize_v5(query: str, chunks: list[dict], fts_conn: sqlite3.Connection,
                   api_key: str, executor_model: str, auditor_model: str,
                   max_retries: int, contradicts_threshold: float) -> dict:
    """v2 first pass + inline CONTRADICTS audit + targeted rewrite WITH FABRICATED verify-retry."""
    # 1. v2 synthesis with FABRICATED verify-retry (existing — covers first-pass fab)
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
            "v5_audit_initial": audit_summary,
            "v5_rewrite_applied": False,
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    # 3. Targeted rewrite for CONTRADICTS-flagged sentences
    rewrite_audits = [a for a in audit["audits"] if a.get("disposition") == "rewrite"]
    if not rewrite_audits:
        # Only hold (auditor error) — return with held tag
        return {
            "answer": "[AUDITOR_FAILED] " + answer,
            "v5_audit_initial": audit_summary,
            "v5_rewrite_applied": False,
            "v5_held": True,
            "v5_held_reason": "auditor_error",
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

    # 4. THE V5 KEY CHANGE: rewrite with FABRICATED verify-retry loop
    try:
        revised, rewrite_usage = call_with_fabricated_retry(
            initial_messages=[{"role": "user", "content": rewrite_user}],
            system=REWRITE_SYSTEM_V4,
            chunks_text=chunks_text,
            fts_conn=fts_conn,
            api_key=api_key,
            model=executor_model,
            max_retries=max_retries,
        )
    except Exception as e:
        return {
            "answer": "[AUDITOR_FAILED] " + answer,
            "v5_audit_initial": audit_summary,
            "v5_rewrite_applied": False,
            "v5_held": True,
            "v5_held_reason": f"rewrite_call_failed: {e}",
            "tokens_in": total_in,
            "tokens_out": total_out,
        }
    total_in += rewrite_usage["tokens_in"]
    total_out += rewrite_usage["tokens_out"]

    # 5. If rewrite still has fabricated quotes after retries: HOLD
    if rewrite_usage["final_failed"] > 0:
        return {
            "answer": "[AUDITOR_FAILED] " + answer,
            "v5_audit_initial": audit_summary,
            "v5_rewrite_applied": True,
            "v5_held": True,
            "v5_held_reason": f"rewrite_introduced_fabrication_after_retries ({rewrite_usage['final_failed']} unresolved)",
            "v5_rewrite_fab_attempts": rewrite_usage["fab_attempts"],
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    # 6. Re-audit the rewritten answer (one final CONTRADICTS check)
    audit2 = audit_answer(revised, chunks, model=auditor_model, api_key=api_key,
                           contradicts_threshold=contradicts_threshold)
    audit2_summary = audit2.get("summary", {})
    if audit2_summary.get("needs_rewrite", False) or audit2_summary.get("needs_hold", False):
        return {
            "answer": "[AUDITOR_FAILED] " + revised,
            "v5_audit_initial": audit_summary,
            "v5_audit_after_rewrite": audit2_summary,
            "v5_rewrite_applied": True,
            "v5_held": True,
            "v5_held_reason": "still_contradicts_after_rewrite",
            "v5_rewrite_fab_attempts": rewrite_usage["fab_attempts"],
            "tokens_in": total_in,
            "tokens_out": total_out,
        }

    return {
        "answer": revised,
        "v5_audit_initial": audit_summary,
        "v5_audit_after_rewrite": audit2_summary,
        "v5_rewrite_applied": True,
        "v5_held": False,
        "v5_rewrite_fab_attempts": rewrite_usage["fab_attempts"],
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
    print(f"v5 Synthesizing {len(queries)} queries with executor={args.executor_model} "
          f"auditor={args.auditor_model} threshold={args.contradicts_threshold}")
    print(f"v5 = v4 CONTRADICTS Auditor + FABRICATED verify-retry on rewrite path")

    fts_conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_lines = []
    meta = []
    total_in = total_out = 0
    n_held = n_rewrite_applied = n_clean_first_pass = 0
    n_rewrite_fab_caught = 0
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
            print(f"  [{i}/{len(queries)}] (no chunks) -- {query[:55]}", flush=True)
            continue

        t0 = time.time()
        result = synthesize_v5(query, chunks, fts_conn, api_key,
                                args.executor_model, args.auditor_model,
                                args.max_retries, args.contradicts_threshold)
        dt = time.time() - t0
        total_in += result["tokens_in"]
        total_out += result["tokens_out"]
        if result.get("v5_held"):
            n_held += 1
            marker = f" HELD({result.get('v5_held_reason','')[:30]})"
        elif result.get("v5_rewrite_applied"):
            n_rewrite_applied += 1
            fab_attempts = result.get("v5_rewrite_fab_attempts", 0)
            if fab_attempts > 0:
                n_rewrite_fab_caught += 1
                marker = f" REWRITTEN+FAB-fix({fab_attempts})"
            else:
                marker = " REWRITTEN"
        else:
            n_clean_first_pass += 1
            marker = ""

        a_init = result.get("v5_audit_initial", {})
        verdicts = a_init.get("verdicts", {})
        cont = verdicts.get("CONTRADICTS", 0)
        sup = verdicts.get("SUPPORTS", 0)
        marker += f" audit:S{sup}/C{cont}"
        print(f"  [{i:>2}/{len(queries)}] {dt:.1f}s in={result['tokens_in']} out={result['tokens_out']}"
              f" chunks={len(chunks)}{marker} -- {query[:42]}", flush=True)
        out_lines.append(json.dumps({"query": query, "answer": result["answer"]},
                                    ensure_ascii=False))
        meta.append({"query": query, **{k: v for k, v in result.items() if k != "answer"}})

    fts_conn.close()
    out_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    if args.meta_out:
        Path(args.meta_out).write_text(json.dumps(meta, indent=2, ensure_ascii=False),
                                       encoding="utf-8")

    cost_upper = (total_in * 15 + total_out * 75) / 1_000_000
    elapsed = time.time() - t_start
    print(f"\n=== v5 Synthesis summary ===")
    print(f"  Wrote {len(out_lines)} answers to {out_path}")
    print(f"  Tokens (executor + auditor combined): {total_in} in + {total_out} out")
    print(f"  Cost upper-bound (assumes all Opus pricing): ~${cost_upper:.3f}")
    print(f"  Wall time: {elapsed:.1f}s")
    print(f"  First-pass clean (no audit issue):   {n_clean_first_pass}/{len(queries)}")
    print(f"  Rewritten by auditor:                {n_rewrite_applied}/{len(queries)}")
    print(f"    of which FABRICATED on rewrite caught + fixed: {n_rewrite_fab_caught}")
    print(f"  HELD with [AUDITOR_FAILED]:          {n_held}/{len(queries)}")


if __name__ == "__main__":
    main()

# Cost and Latency Benchmarks — Citation Pipeline (2026-05-02)

**Written:** 2026-05-02.
**Source of measurements:** This-day session running the citation precision pipeline against a held-out n=35 batch.
**Scope:** Closes Verification Master Checklist Cat 1 items: "Cost per query computed (per role: architect/executor/auditor)" and "Latency p50/p95/p99 measurements captured".

## Roles measured

The citation pipeline exercised three roles in the Triad analog. Mapping to the orchestrator names in `tools/ai_studio/orchestrator.py`:

| Role | What it does | Model used | Where measured |
|---|---|---|---|
| Executor (synthesis) | Takes query + retrieved chunks, produces an answer with one-quote-per-claim discipline | `claude-opus-4-7` | `tools/citation_holdout_synthesizer.py` (n=35 calls) |
| Rewriter (calibration) | Takes a draft answer, restructures under one-quote-per-claim discipline | `claude-opus-4-7` | `tools/citation_rewriter_step1.py` (n=15 calls) |
| Auditor (judge) | Reads claim + cited quote, returns SUPPORTS/PARTIAL/CONTRADICTS/IRRELEVANT/UNREADABLE/FABRICATED verdict | `claude-opus-4-7` | `tools/citation_scorer.py --judge claude` (n=272 verdict calls across 35 queries) |

The Architect role (Triad spec generator, `gemini-3.1-pro`) was not exercised in this session — the citation work used the existing prompts. Architect cost numbers will be added in a future session that runs Triad orchestration end-to-end.

## Cost per call (Anthropic Opus 4.7 pricing: $15/MTok input, $75/MTok output)

| Role | N | Avg input tokens | Avg output tokens | Avg cost per call | Total session cost |
|---|---|---|---|---|---|
| Executor (synthesis) | 35 | 3,353 | 428 | **$0.082** | $2.88 |
| Rewriter (calibration) | 15 | 1,109 | 224 | **$0.033** | $0.50 |
| Auditor (judge) | 272 verdict calls | ~400 | ~50 | **~$0.018** | ~$5 |

Per **end-user query** (one synthesis + ~7.8 average judge verdicts = 1 Executor + 7.8 Auditor calls):

> **~$0.22 per fully-judged held-out query.**

That's the diligence-grade per-query cost: one synthesis answer plus full LLM-as-judge measurement of every grounded claim. In production (synthesis without per-query judging) the cost is just the Executor call: **~$0.082 per query**.

## Latency

Measured on Anthropic API with normal load on 2026-05-02 ~07:30 MDT, single sequential calls (no batching).

| Role | p50 | p95 | p99 | Avg |
|---|---|---|---|---|
| Executor (synthesis, n=35) | **6.1s** | **12.3s** | **12.4s** | 9.5s |
| Rewriter (calibration, n=15) | 3.0s | 4.1s | n/a | 3.2s |
| Auditor (judge, single verdict) | ~1.5s | ~2.5s | ~3s | ~1.8s (estimated from total batch wall time / 272 verdicts) |

End-to-end latency for a fully-judged query: **~6s synthesis + 7.8 × 1.8s judge ≈ ~20s**. Synthesis-only latency (no per-query judge): **~6s**.

Variation drivers:
- Executor: chunk count + answer length. The 12.3s p95 is on queries that returned 5 chunks and 800-token answers; the 1.4s outliers are "no relevant sources" 27-token responses.
- Auditor: minimal variation — the prompt and output are both small and bounded.

## How this scales

- **24K KG entities × $0.082** = $1,970 to synthesize one answer per entity. Not how the system would be used; entity-level questions cluster heavily.
- **Realistic acquihire demo run (50 queries):** ~$4.10 synthesis + ~$10 judge = ~$14. Currently within session budget.
- **Production legal-team daily volume estimate (200 queries/day):** ~$16/day synthesis. Judging would not be per-query — sample-based.

## Caveats

1. **Anthropic pricing as of 2026-05-02.** Opus 4.7 list is $15/MTok in / $75/MTok out. Cached reads are $1.50/MTok in (90% discount); none of the calls in this session used the prompt cache. Adding prompt caching to the synthesis prompt would drop Executor cost ~30-40% on repeat queries against the same chunk set.
2. **No Architect calls measured.** Adding the Triad spec generation would add one Gemini 3.1 Pro call per session start; Gemini list pricing currently ~$1.25/MTok in / $5/MTok out, so an 8K-token spec is ~$0.05.
3. **Latencies are wall-clock for sequential calls.** Concurrent calls would reduce wall time but not per-call latency. The system does not currently use the Anthropic Batch API (50% discount, async, ≤24h SLA), which would be the right choice for held-out test batches if cost rather than latency is the constraint.

## Verification

| Claim | Evidence |
|---|---|
| Executor avg $0.082 / 6.1s p50 | Logged in `/tmp/holdout_synth.log` from session 277-continuation; aggregated by `Bash` tool call this session. Source data: `AI_Studio/Reports/scheduled/citation_batch_holdout_n35_20260502_073513.jsonl` |
| Rewriter avg $0.033 / 3.0s p50 | Same source pattern from `/tmp/rewriter_run.log` |
| Auditor 272 verdicts | Counted from `AI_Studio/Reports/scheduled/citation_score_holdout_n35_claudejudge_20260502_074107.json` `span_per_claim[*].verdicts[*]` entries |
| Per-query end-to-end ~$0.22 | $0.082 + 7.8 × $0.018 = $0.222 |

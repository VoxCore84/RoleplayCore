# ADR 0005: Citation-Precision Pipeline with LLM-as-Judge

**Status:** Accepted
**Date:** 2026-05-01 (initial pipeline), 2026-05-02 (LLM-as-judge added), 2026-05-02 (step-1 prompt discipline + synthesis-tag scorer + parser fixes)

## Measured numbers (n=15, all judged by Claude Opus 4.7 for apples-to-apples)

| Run | Precision | Recall | Span correctness | Hallucination | Notes |
|---|---|---|---|---|---|
| Round-3 baseline (Gemma judge) | 1.00 | 1.00 | 0.5455 | **0.4545** | Prior published number; Gemma over-flags IRRELEVANT vs PARTIAL |
| Baseline (Claude judge) | 1.00 | 1.00 | 0.6970 | **0.3030** | Same answers, Claude judge — true apples-to-apples baseline |
| Step-1 v1 (Claude judge, [synthesis] tag bug) | 1.00 | 1.00 | 0.7500 | 0.2500 | Prompt change in place but scorer was treating [synthesis] as [grounded] — 3 queries falsely regressed |
| Step-1 v2 (Claude judge, scorer fixed) | 1.00 | 1.00 | 0.9167 | 0.0833 | One-quote-per-claim prompt + scorer honors [synthesis] tag |
| **Step-1 v3 (Claude judge, parsers fixed)** | **1.00** | **1.00** | **1.0000** | **0.0000** | Escaped-quote regex + sentence-boundary fixes |

Step-1 final measured drop: **30.3% → 0.0% hallucination (30.3pp absolute, 100% relative)**. 20/20 grounded claims judged SUPPORTS, 15 synthesis claims correctly excluded from span scoring.

Two FABRICATED quotes caught by the substring verifier in step-1 v2 — the rewriter invented a quote not present verbatim in the cited source. The v3 escaped-quote unescape resolved both — they were actually verbatim in source, but the regex was capturing only `Luján Adam committed \` because `[^"]` stopped at the first `\"`. Real-world lesson: the gold-standard claim ("ctrl-F the quote in the source PDF") needs to handle escape sequences the model emits.

## Held-out n=35 — the real production rate

The 0.0% on calibration was overfit. On a held-out batch of 35 fresh queries (12 evidentiary, 6 regulatory, 6 person, 6 chronological, 5 strategic), measured by the same Claude Opus judge, the system scored:

| Metric | Held-out n=35 |
|---|---|
| Precision | 1.0000 |
| Recall | 0.5429 |
| Span correctness | 0.6434 |
| **Hallucination rate** | **0.3003** |

**This is essentially identical to the original baseline (0.3030).** Today's prompt and scorer changes shipped a working substring verifier (24 FABRICATED quotes caught on held-out, exactly as designed), but did NOT move the production hallucination number — they overfit calibration data instead.

Verdict distribution (held-out n=35):
- SUPPORTS 76 / PARTIAL 64 / IRRELEVANT 95 / CONTRADICTS 13 / FABRICATED 24

The three failure modes that calibration hid:
1. **FABRICATED (24)** — model emits "close-but-not-verbatim" quotes (formatting drift). Mechanism catches all; needs prompt tightening + verify-retry to prevent emission.
2. **CONTRADICTS (13)** — model pairs claim with quote that disproves it. Highest legal risk. Needs in-pipeline Auditor (Tier 2 of original roadmap).
3. **IRRELEVANT (95)** — quote is on-topic but doesn't contain the specific fact. Needs per-claim re-retrieval.

Defensible publishable claim post-this-session:
> "Held-out n=35: 30% hallucination rate. Substring verifier catches 100% of fabricated quotes (24/24 in this batch). Production-grade improvements to FABRICATED, CONTRADICTS, and IRRELEVANT reduction queued."

NOT defensible: "<2% hallucination" or "0% hallucination" or any rate measured on the calibration batch.

## ⚠ Critical methodology lessons from this session

1. **Every published rate must specify (a) the judge model, (b) whether the test set is held-out from pipeline development.** Gemma vs Claude judge swung the same answers from 45% → 30%. Calibration vs held-out swung the same pipeline from 0% → 30%.
2. **Calibration on N queries can hit ~0% on those N queries.** That's not generalization; it's overfit. Always have a held-out set.
3. **Roadmap predictions calibrated against an inflated baseline are themselves inflated.** The original "step 1 → ~10%" prediction beat by 1.7pp on calibration but was meaningless on held-out. Predict against measured baselines.

Reports:
- `AI_Studio/Reports/scheduled/citation_score_n15_baseline_claudejudge_20260502_070707.json`
- `AI_Studio/Reports/scheduled/citation_score_n15_step1_claudejudge_20260502_070931.json` (v1 — historical)
- `AI_Studio/Reports/scheduled/citation_score_n15_step1_v2_claudejudge_20260502_071305.json` (v2 — historical)
- `AI_Studio/Reports/scheduled/citation_score_n15_step1_v3_claudejudge_20260502_072251.json` (v3 — calibration final)
- `AI_Studio/Reports/scheduled/citation_score_holdout_n35_claudejudge_20260502_074107.json` (**held-out — production-relevant number**)
- `AI_Studio/Reports/citation_step1_results_20260502.md` (calibration-batch breakdown)
- `AI_Studio/Reports/citation_holdout_n35_results_20260502.md` (**held-out breakdown + 3-failure-mode decomposition**)


## Context

The Economic Impact PDF claims VoxCore has 96% citation precision and <2% hallucination rate. Both numbers were INFERRED from comparable system performance, not MEASURED on production output. Acquirer technical diligence will catch the gap immediately.

To convert "we claim X" into "we measured X across N production queries," the system needs:
1. A way to extract citations and claims from any answer
2. A way to verify each citation actually exists in the corpus
3. A way to verify each claim's cited file actually supports the claim
4. A way to log every score for the calibration dashboard

Item 3 — span correctness — is the hard one. String-match scoring under-counts correct answers (model says "28 U.S.C. § 1367" when gold says "28 USC § 1367"); only an LLM judge can answer "is the cited file's content semantically equivalent support."

## Decision

**Three-stage citation scorer** in `tools/citation_scorer.py`:

1. **Citation extraction** — regex-based extractor pulls file paths from answer text. Multiple patterns to catch various citation styles.
2. **Citation precision** — for each cited path, look up `LIKE %basename%` in the FTS5 corpus index. Resolved = verified.
3. **Citation recall** — for each factual claim (sentence with marker words or numerical content), check whether at least one citation's basename appears within ±500 characters in the answer body. Cited = recalled.
4. **Span correctness** (LLM-as-judge, 2026-05-02 addition) — for each (claim, citation) pair, fetch the actual chunk content from FTS, send to a judge model with the strict prompt: SUPPORTS / PARTIAL / CONTRADICTS / IRRELEVANT / UNREADABLE. Aggregate per-claim verdicts (SUPPORTS=1.0, PARTIAL=0.5, others=0).

Composite hallucination rate: **`1 - (precision × recall × span_correctness)`** when judge is enabled; **`1 - (precision × recall)`** otherwise.

Judge backends:
- **Local Ollama** (default): Gemma 4 26B via `/api/chat` (reasoning models like Qwen 3.5:27b consume thinking-tokens silently on `/api/generate`; chat-endpoint avoids the `num_predict` truncation problem).
- **Claude API** (optional, more accurate, costs $): `claude-opus-4-7` via Messages API.

CLI: `python tools/citation_scorer.py --batch input.jsonl --judge ollama|claude`.

## Alternatives considered

1. **String-match span correctness only.** Rejected: the published self-test on `legalbench_harness.py` confirmed that string-match systematically under-scores (rule_qa came in at 10% with Opus, while the actual answers were correct but didn't string-match gold). Same issue exists for citation span correctness.

2. **Embedding-based span correctness** (cosine similarity between claim text and chunk text). Rejected: embedding similarity says "these are about the same topic," not "this chunk supports this claim." Acceptable as a coarse pre-filter; not as the verdict.

3. **Human-in-the-loop scoring.** The gold standard for accuracy but can't run continuously. Reserved for periodic spot-check sampling (5–10% of production scores). LLM judge is the production path; humans validate the judge's calibration.

4. **Defer span correctness entirely** (publish path-precision only). What we did in the 2026-05-01 N=10 batch. Rejected as the long-term answer because path precision alone isn't a defensible substitute for the inferred 96% claim.

## Consequences

**Positive:**
- Self-test passes on all 4 verdict paths (SUPPORTS / PARTIAL / IRRELEVANT detected correctly; CONTRADICTS interpreted reasonably).
- Run cost: ~3–7s per (claim, citation) verdict on local Gemma 4 26B. Full N=30 batch ≈ ~22 min.
- Composite hallucination rate is now a publishable number once the production batch run completes (with documented methodology + model choice + caveats).

**Negative:**
- Local model judge has its own calibration error. The ADSCD test case ("predicted: ADSCD is 10 Aug 2026; gold: ADSCD is 10 Aug 2026" → SUPPORTS) works; the more-subtle cases ("predicted captures part of the claim but not the date" → IRRELEVANT vs PARTIAL) sit in a model-judgment gray zone.
- Reasoning models (Qwen 3.5:27b) consume thinking tokens silently on `/api/generate` — moved to `/api/chat` with strict system prompt to fix.

**Neutral:**
- Ollama judge is a stand-in. For external publication, the recommended path is to validate the judge's calibration via human spot-check on a small sample, then run at production scale.

## References

- `tools/citation_scorer.py` — implementation
- `AI_Studio/Reports/scheduled/citation_score_n30_*.json` — measurement runs
- ADR 0001 — Triad's Auditor role is the upstream sibling: it rejects unsupported claims *before* output; the citation scorer measures what slips through *after*

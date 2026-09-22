# measurement-discipline — reference (moved from .claude/rules/measurement-discipline.md on 2026-09-22; operative rules remain in the rules file)

## Header rationale (moved verbatim)

What makes the audit trail diligence-grade is not the measurements themselves but the discipline that surrounds them. The Phase 7.2 arc proved the discipline holds at $3.00 cost. This rule encodes what worked.

## Calibration choice — Phase 3.9 example (moved verbatim)

Phase 3.9 conservative-judge calibration: the prompt defined SUPPORTS / NEUTRAL / CONTRADICTS thresholds before any spans were judged. The 0.375 N=10 POD batch result was reported with the calibration explicit. A post-hoc relaxation to lift the number above 0.5 would have fabricated quality.

## Cost dimension — Phase 6A example (moved verbatim)

Phase 6A used **per-query mean latency** as the cost dimension across all 21 configurations. Alternative dimensions (LLM tokens, dollar cost, GPU-seconds) would have been valid choices, but mixing them would have made the Pareto frontier non-comparable. Pick one and stick with it for the whole comparison.

## Tie-break rules — Phase 6A example (moved verbatim)

Phase 6A: pass rate primary, MRR secondary. `fts_vec_kg_k60` (production) and `fts_vec_kg_k30` both scored 92.0% pass rate; `k=30` won the MRR tie-break (0.6207 vs 0.5963). The tie-break being declared in advance prevented post-hoc rationalization ("k=60 is what we shipped, so let's prefer it").

## A/B methodology — Phase 4 HyDE canonical example (moved verbatim)

Phase 4 HyDE A/B was the canonical example: Run A (HyDE off) vs Run B (HyDE on), identical snapshot + gold set + runner config, both run records persisted with run_ids, regression measured at -10 pp, reported unsoftened with 5 regressions / 0 lifts in the headline.

## No-cherry-pick — Phase 5 canonical example (moved verbatim)

Phase 5 MRR-vs-pass-rate diagnostic is the canonical example: hybrid achieved +14 pp pass rate over FTS5, but **-0.0007 MRR**. Both numbers ship. Selectively reporting "+14 pp pass rate" without the MRR diagnostic would have hidden a real architectural finding (hybrid demotes some FTS5 rank-1 hits to rank 2-3 while adding new passing queries at deeper ranks).

## Withdrawn-claim discipline — examples (moved verbatim)

- **Phase 3.75-A**: the historical "82% hybrid retrieval" claim was retired in favor of measured 92.0% via the new evaluation harness. The retirement was documented in the closeout AND the achievement record AND the document state line — three independent surfaces carry the new number with explicit pointer to the prior claim being superseded.
- **Economic Impact PDF v2 → v3.1**: prior session work formally withdrew "<2% hallucination, 96% citation precision, 82% multi-hop" claims from v2 in favor of v3.1 with tiered-evidence framing. The withdrawal is annotated in the document; v2 is not silently replaced.

## Sample-size disclosure — worked examples (moved verbatim)

- Phase 3.9 N=10 POD batch — span correctness measured on 179 (claim, citation) pairs across 10 queries, NOT on the full 50-query gold set. The closeout, the achievement record, and the report generator's span-correctness section all carry this caveat.
- Phase 4 HyDE A/B at n=50 queries — the report explicitly notes "the generator does not do statistical significance testing on deltas; a +5 pp delta on n=50 may or may not be a real effect; the report shows the raw delta and lets the reviewer decide".
- Phase 6A Pareto sweep at 21 configurations × 50 queries — wall time scaled, but per-query latency stable across worker counts, so per-config comparisons hold.

## Provenance — enforcement note (moved verbatim)

The benchmark report generator enforces this — every report header carries the four provenance fields, and the reader can re-derive the measurement from the same inputs.

## Cross-references (moved verbatim)
- For documenting the measurements once produced: see `documentation-discipline.md` § Numbers verbatim
- For the unverified-claim posture this rule prevents: see `completion-integrity.md`
- For paid LLM cost decisions during measurement design: see `operational-discipline.md` § Budget-tension protocol
- For where the measurement results land at session end: see `session-handoff.md` § Final session report

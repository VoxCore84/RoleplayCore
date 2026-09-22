# documentation-discipline — reference (moved from .claude/rules/documentation-discipline.md on 2026-09-22; operative rules remain in the rules file)

## Header rationale (moved verbatim)

The session arc that produced 11 measured phases at $3.00 total cost held this discipline through Phases 1 → 6A → 7.2c. Errors in the documentation surface propagate forward; errors fixed at write time stay fixed.

## Per-checkpoint cadence — Phase 5 fabrication catch (moved verbatim)

The Phase 5 fabrication (regulatory +25 pp / semantic +50 pp, both wrong because both categories were already at 100%) was caught precisely because the per-checkpoint write happened before the next phase started — batched-at-end summaries would have shipped the wrong numbers.

## Closeout report template — provenance of the model (moved verbatim)

Closeout report template (model from Phase 7.2 sub-phases). Item 4 "Anything unexpected during execution (surface findings)" in full: *surface findings — Phase 7.2a's mojibake-was-actually-em-dash, Phase 7.2c's recount-was-10-not-9, etc.*

## Update log discipline — Phase 5 openness example (moved verbatim)

Document mid-phase corrections OPENLY in the entry rather than silently fixing them — Phase 5 fabrication catch is in the update log explicitly, not hidden.

## Supersession discipline — date + Phase 7.2b example (moved verbatim)

Supersession discipline (Theranos pattern from 2026-05-03).

Phase 7.2b reference-update sweep found 0 edits needed — the supersession discipline meant Phase 7.1 INVENTORY, PHASE_7_2_SCOPE, and PHASE_7_2A_CLOSEOUT all kept their pre-move references because new closeouts captured post-move state.

## Anti-fabrication — the free-recall failure verbatim (moved verbatim)

- BAD: free-recall numbers from short-term memory ("regulatory +25.0 pp" — was wrong, both categories already at 100%, true lift 0 pp)

## Plans vs tickets — Phase 6C scaffold examples (moved verbatim)

The Phase 6C scaffolds (`eval/datasets/v2_scaffold/EXECUTION_PLAN.md`, `contradiction/PLAN.md`, `graphrag/PLAN.md`, `retrieval/CASCADE_PLAN.md`) were plans, not tickets. Future scaffolds should keep the distinction explicit at the document header.

## Cross-references (moved verbatim)
- For when documentation goes into a session-end handoff: see `session-handoff.md`
- For destructive operations on audit-trail files: see `operational-discipline.md`
- For measurement claims that go into closeouts: see `measurement-discipline.md`
- For completion claims: see `completion-integrity.md` (precedes this rule, complementary)

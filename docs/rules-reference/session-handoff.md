# session-handoff — reference (moved from .claude/rules/session-handoff.md on 2026-09-22; operative rules remain in the rules file)

## Header rationale — full text (moved verbatim)

A session ends in one of three ways: clean wrap-up, context compaction, or tab switch. All three need the same artifact: a handoff document that lets the next session pick up with bounded scope and full provenance, without reconstructing context from raw conversation history.

## "When this rule applies" — full wording of moved parentheticals (moved verbatim)

- Switching tabs / contexts mid-arc (browser → Code, Code → Code with different focus)

## Final session report — canonical example (moved verbatim)

The Phase 6C closeout's `SESSION_2026-05-04_FINAL.md` (~25 KB) is the canonical example. A future session reading this artifact alone (no conversation transcript) can resume the work.

## Document state line — purpose note (moved verbatim)

The line a fresh session reads first to understand "where we are".

## Update log per phase — Phase 6B example (moved verbatim)

Phase 6B-style deferrals get an entry too — explicitly noted as "deferred not dropped".

## Next-session priority order — canonical examples (moved verbatim)

Phase 6C closeout § 4 lists 10 priorities; Phase 7.2c closeout § 18 lists skill-creation as priority 1. The format works — preserve it.

## Architectural debt enqueueing — Phase 6A canonical example (moved verbatim)

Phase 6A vec_k30 race condition is the canonical example: workaround applied (re-run at workers=1), real fix (warm Chroma client before parallel queries) enqueued in `SESSION_2026-05-04_FINAL.md` § 5 architectural debt item #1.

## Handoff payload — three-document-split precedent (moved verbatim)

The session-start handoffs (`00_HANDOFF_START_HERE.md`, `01_VOXCORE_BUILD_SESSION_DETAIL.md`, `02_REAL_WORLD_THREADS.md`) demonstrated the pattern — three-document split between identity / project-detail / real-world-threads avoided the monolithic-handoff failure mode.

## Cross-references (moved verbatim)
- For the documentation cadence that produces the artifacts referenced here: see `documentation-discipline.md`
- For destructive ops near session end (e.g., reorganization passes, file moves): see `operational-discipline.md`
- For the measurement deltas section of the final session report: see `measurement-discipline.md` § No-cherry-pick discipline (the final report inherits the same no-cherry-pick rule)
- For the in-session compaction scratchpad: see `compaction-survival.md`
- For session-start protocol: see `session-start.md`
- For multi-tab coordination: see `multi-tab.md`

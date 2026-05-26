# Session Handoff — Cross-Session Continuity (P1 Audit-Trail)

A session ends in one of three ways: clean wrap-up, context compaction, or tab switch. All three need the same artifact: a handoff document that lets the next session pick up with bounded scope and full provenance, without reconstructing context from raw conversation history.

## When this rule applies
- End of any work session that produced new measurements, new artifacts, or new architectural debt
- Switching tabs / contexts mid-arc (browser → Code, Code → Code with different focus)
- Detecting that the conversation is approaching context limits (compaction imminent)
- Detecting that another tab / agent is about to start work on a related surface

## Final session report — mandatory at session end

Every multi-phase session arc closes with a `SESSION_<YYYY-MM-DD>_FINAL.md` document at `AI_Studio/Reports/`. Required sections:

1. **Phases completed** — table with status + cost + output paths per phase
2. **Metrics deltas** — start vs end of session for each measured dimension
3. **What's now possible** — capabilities the session unlocked
4. **What's queued for next session** — priority-ordered list with cost + wall-time estimates per item
5. **Architectural debt incurred** — what got worked-around vs fixed; what needs cleanup
6. **Honest assessment** — what worked, what didn't, what surprised
7. **Total session cost + total wall time**

The Phase 6C closeout's `SESSION_2026-05-04_FINAL.md` (~25 KB) is the canonical example. A future session reading this artifact alone (no conversation transcript) can resume the work.

## Document state line — top of achievement record

A single line at the top of `SL_Vault/01_Achievement_Record.md` captures current arc disposition. Updated per phase, accumulating context for fresh-context session pickup.

Format: `**Document state:** Round X complete; QA cycle status; phase Y of Z arc complete (deferrals + scaffolds noted)`

The line a fresh session reads first to understand "where we are". Per-phase updates extend this line; do not delete prior content.

## Update log per phase — append-only

Every phase that produces artifacts produces an update log entry in `01_Achievement_Record.md` and (where load-bearing) `02_Decisions_Log.md`. Format and discipline detailed in `documentation-discipline.md` § Update log discipline.

On session close: verify the update log has one entry per completed phase (not one entry for the whole session). Phase 6B-style deferrals get an entry too — explicitly noted as "deferred not dropped".

## Next-session priority order — concrete

Final session report § "What's queued for next session" lists candidates in priority order with:
- Estimated cost
- Estimated wall time
- What would block it (Adam GO needed, deferred dependency, etc.)
- Top-priority candidate is the explicit recommendation for the next session's first work

Phase 6C closeout § 4 lists 10 priorities; Phase 7.2c closeout § 18 lists skill-creation as priority 1. The format works — preserve it.

## Architectural debt enqueueing

Debt found mid-session goes into `SL_Vault/06_Working_Documents/VoxCore_Open_Questions.md` or `SL_Vault/_vault_only/known_issues.md`, NOT into "I'll fix it next phase" verbal commitments.

When a workaround replaces a real fix mid-session, the real fix MUST be added to the next-session priority list AND captured in the final session report § "Architectural debt incurred". Workarounds without enqueued real fixes accumulate as quiet debt.

Phase 6A vec_k30 race condition is the canonical example: workaround applied (re-run at workers=1), real fix (warm Chroma client before parallel queries) enqueued in `SESSION_2026-05-04_FINAL.md` § 5 architectural debt item #1.

## Tab-coordination via doc/session_state.md

Multi-tab work uses an explicit state file. Tabs do NOT trust each other's claims about file-system state.

- Every tab reads `doc/session_state.md` at session start
- Before starting work, claim the assignment by appending an entry
- Before touching any database, re-read to check ownership
- After completing work, update with what changed (files modified, SQL applied, Run records created)

If a fresh session needs to read full conversation history to understand prior tab work, the handoff failed — fix the handoff, not the new session.

## Compaction-survival writes

Before context approaches limit, write to `AI_Studio/Reports/session_state_live.md` per `compaction-survival.md`. The handoff payload (below) is the larger, structured form; the live-state scratchpad is the in-flight form.

When the conversation hits ~50% of context budget, drop the live-state pad. When the conversation hits ~80%, drop the formal handoff document and consider stopping for explicit handoff.

## Handoff payload — what a session handoff contains

A complete handoff includes:
1. **Identity + constraints + standing directives** — who the user is, what's locked-in (e.g., "Sonnet-only this session", "no production code changes without Adam GO")
2. **Current measured state with provenance** — last verified pass rate / cost / file paths with run_ids and snapshot_ids
3. **What's in flight** — open work, who-waits-on-what (Adam GO needed for X, Y already approved)
4. **Posture guidance** — the qualitative "we're being conservative on X this week because Z"
5. **Explicit "do not do X" list** — the things the next session would otherwise plausibly do that would be wrong (don't run sync_canonical_state.py — it's deprecated; don't enable HyDE in production — measured net negative)

The session-start handoffs (`00_HANDOFF_START_HERE.md`, `01_VOXCORE_BUILD_SESSION_DETAIL.md`, `02_REAL_WORLD_THREADS.md`) demonstrated the pattern — three-document split between identity / project-detail / real-world-threads avoided the monolithic-handoff failure mode.

## Handing off to a fresh Claude Code session — the test

The handoff payload is correct when a fresh session can:
- Read the linked documents
- Pick a priority from the queued list
- Start work without reading the prior conversation

If the fresh session needs to ask "what was the last measurement?" or "what's the current production config?" — the handoff missed something. Fix the handoff document, not the new session.

## Cross-references
- For the documentation cadence that produces the artifacts referenced here: see `documentation-discipline.md`
- For destructive ops near session end (e.g., reorganization passes, file moves): see `operational-discipline.md`
- For the measurement deltas section of the final session report: see `measurement-discipline.md` § No-cherry-pick discipline (the final report inherits the same no-cherry-pick rule)
- For the in-session compaction scratchpad: see `compaction-survival.md`
- For session-start protocol: see `session-start.md`
- For multi-tab coordination: see `multi-tab.md`

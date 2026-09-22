# Session Handoff — Cross-Session Continuity (P1 Audit-Trail)

> Long form + history: docs/rules-reference/session-handoff.md

## When this rule applies
- End of any work session that produced new measurements, artifacts, or architectural debt
- Switching tabs / contexts mid-arc
- Conversation approaching context limits (compaction imminent)
- Another tab / agent is about to start work on a related surface

## Final session report — mandatory at session end

Every multi-phase session arc closes with `SESSION_<YYYY-MM-DD>_FINAL.md` at `AI_Studio/Reports/`. Required sections:
1. **Phases completed** — table with status + cost + output paths per phase
2. **Metrics deltas** — start vs end of session per measured dimension
3. **What's now possible** — capabilities the session unlocked
4. **What's queued for next session** — priority-ordered, with cost + wall-time estimates
5. **Architectural debt incurred** — what got worked-around vs fixed; what needs cleanup
6. **Honest assessment** — what worked, what didn't, what surprised
7. **Total session cost + total wall time**

A future session reading this artifact alone (no transcript) must be able to resume the work.

## Document state line — top of achievement record
A single line at the top of `SL_Vault/01_Achievement_Record.md` captures current arc disposition, updated per phase.
Format: `**Document state:** Round X complete; QA cycle status; phase Y of Z arc complete (deferrals + scaffolds noted)`
Per-phase updates extend this line; do not delete prior content.

## Update log per phase — append-only
- Every phase producing artifacts gets an entry in `01_Achievement_Record.md` and (where load-bearing) `02_Decisions_Log.md`. Format per `documentation-discipline.md`.
- On session close: verify one entry per completed phase, not one for the whole session. Deferrals get an entry too — explicitly "deferred not dropped".

## Next-session priority order — concrete
§ "What's queued for next session" lists candidates in priority order with: estimated cost, estimated wall time, what would block it (Adam GO, deferred dependency). Top candidate is the explicit recommendation for the next session's first work.

## Architectural debt enqueueing
- Debt found mid-session goes into `SL_Vault/06_Working_Documents/VoxCore_Open_Questions.md` or `SL_Vault/_vault_only/known_issues.md`, NOT into "I'll fix it next phase" verbal commitments.
- When a workaround replaces a real fix, the real fix MUST be added to the next-session priority list AND captured in § "Architectural debt incurred". Workarounds without enqueued real fixes accumulate as quiet debt.

## Tab-coordination via doc/session_state.md
Tabs do NOT trust each other's claims about file-system state.
- Every tab reads `doc/session_state.md` at session start
- Before starting work, claim the assignment by appending an entry
- Before touching any database, re-read to check ownership
- After completing work, update with what changed (files modified, SQL applied, Run records created)

If a fresh session needs the full conversation history to understand prior tab work, the handoff failed — fix the handoff, not the new session.

## Compaction-survival writes
- Before context approaches limit, write `AI_Studio/Reports/session_state_live.md` per `compaction-survival.md`.
- At ~50% of context budget, drop the live-state pad. At ~80%, drop the formal handoff document and consider stopping for explicit handoff.

## Handoff payload — contents
1. **Identity + constraints + standing directives** — who the user is, what's locked-in ("Sonnet-only this session", "no production code changes without Adam GO")
2. **Current measured state with provenance** — last verified pass rate / cost / paths with run_ids and snapshot_ids
3. **What's in flight** — open work, who-waits-on-what
4. **Posture guidance** — the qualitative "we're being conservative on X this week because Z"
5. **Explicit "do not do X" list** — what the next session would otherwise plausibly do that would be wrong (don't run `sync_canonical_state.py` — deprecated; don't enable HyDE in production — measured net negative)

## The handoff test
The payload is correct when a fresh session can read the linked documents, pick a priority from the queued list, and start work without reading the prior conversation. If it must ask "what was the last measurement?" or "what's the current production config?" — the handoff missed something. Fix the handoff document, not the new session.

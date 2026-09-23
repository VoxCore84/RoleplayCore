# VoxCore — Handoff Index (start here)

**Last updated:** 2026-09-22. One navigational page. If you're a fresh session asking "what exists / what do I build next?", read in this order.

**Latest session:** 6dce2cb5 (2026-09-22 evening) — **Claude Code audit v3 executed** (spec `Desktop/Excluded/claude-code-optimization-prompt-v3.md`). Live per-turn context 61.1k → 57.8k measured (WoW MCP servers deferred −2.8k, CLAUDE.md dedupe −500; experiment shows 52.0k if the last three servers defer too, pending Adam). Hook daemon v1.3.1: new `git-destructive-guard` (force push / reset --hard / git clean / whole-tree checkout / `rm -rf` outside scratch / DB import without snapshot; heredoc-aware; proved itself by blocking the audit's own test loop), release-gate case-sensitivity bug fixed; stale hook suite ported to HTTP (2/22/13 passing, was 0 of 17 scenarios). User settings: inert keys removed, per-model effort for Opus 5.5, `enableAllProjectMcpServers=false` with allowlists in both repos, code-review plugin disabled. `status` command renamed `sys-status` (shadowed the built-in). Explore override dropped by decision (built-in runs Opus 5.5). Report `AI_Studio/Reports/cc_audit_v3_20260922-1804/REPORT.md`; ledger `APPLIED_LEDGER.md`; `ROLLBACK.md`; CalmCore half in `AI_Studio/Handoffs/calmcore/2026-09-22_cc_audit_v3_calmcore.md`; session handoff `AI_Studio/Handoffs/voxcore/2026-09-22_session_288b_cc-audit-v3.md`. Committed at wrap-up as `acd8ed1f06` (audit infra) + `047fad20cc` (CLAUDE.md dedupe); the pre-existing tools/_canonical_state changes remain uncommitted by owner decision. Standing priority recorded: `memory/feedback_power_over_efficiency.md`.
**Previous session (288):** e523922e (2026-09-22) — **Claude Code 2.1.278 optimization sweep.** Live per-turn context 75.2k → 60.8k (rules 33.4k → 21.9k via condensed files + `docs/rules-reference/` long form; MEMORY.md 6.6k → 4.3k); auto-compact env key was misnamed and never read (renamed); 6 dead `Write()` permission rules, 2 broken MCP servers, 5 duplicate WoW agents, 1 per-edit hook removed; 23 agents now carry `effort:`; measured negative result: `skillOverrides` visibility saves 0 tokens. Handoff: `AI_Studio/Handoffs/voxcore/2026-09-22_session_288_cc-optimization-sweep.md`. Report (gitignored): `AI_Studio/Reports/OPTIMIZATION_SWEEP_2026-09-22.md`; ledger with every backup: `AI_Studio/Reports/sweep_2026-09-22/APPLIED_LEDGER.md`; durable state: `memory/claude-code-config-state.md`. Seven decisions queued for Adam in the report's last section. **Kept by decision:** `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` (gates /skill-doctor, Remote Control, auto-updates).
**Previous session:** 286 (2026-05-26) — AI-harvest → stabilize → inventory → **source-of-truth consolidation** + `/start-up` ritual. HEAD `92d33c2441`. Detail: `AI_Studio/Handoffs/voxcore/2026-05-26_session_286_consolidation-closeout.md`.
**Sidecar 286b** (Memory lane, same day) — Memory Control Plane v0.1 integration review: **blocked** — v0.1 (`73c6d4c771`) is buried on this branch + a leak in `tools/memory_schema.py` must be sanitized before any push. Detail: `AI_Studio/Handoffs/voxcore/2026-05-26_session_286b_mcp-v01-integration.md`.
**Parallel project — RAI-BHRT toolkit** (2026-05-28) — Side-project repo at `tools/publishable/rai-bhrt-toolkit/` (private GitHub `VoxCore84/rai-bhrt-toolkit`). Self-directed off-duty professional-development project (LCSW author) for OPB *Improving the Unit* artifact. **Shipped v0.1.0 → v0.4.0 in one session, ~27 days ahead of plan** — all 8 Crisis Safeguard Checklist chapters drafted with 92 verified inline citations + healthcare PHI scanner + citation verifier. Detail: `AI_Studio/Handoffs/voxcore/2026-05-28_session_rai-bhrt_v0.4.0.md`. Project memory: `memory/project_rai_bhrt_toolkit.md`. Approved plan: `~/.claude/plans/piped-singing-octopus.md`. **Hermetically air-gapped from VoxCore main line — do not treat as VoxCore session work.**
Live state: `AI_Studio/Handoffs/voxcore/CURRENT_STATE.md` · Next: `AI_Studio/Handoffs/voxcore/NEXT_SESSION.md` (= **CONSOLIDATION / UNBLOCK**, then v0.1 integration once the branch frees). (Per `/wrap-up` Step 6.5, every wrap-up refreshes this line.)

## Read first
1. **`docs/VOXCORE_SYSTEM_REGISTRY.md`** — what exists and its status (LIVE/PARTIAL/DORMANT/SCAFFOLD). The single "what do we already have?" source.
2. **`docs/VOXCORE_BUILD_ROADMAP.md`** — the sequenced "what do we build next?" (Items 0–8, gated).
3. **`AI_Studio/Handoffs/voxcore/NEXT_SESSION.md`** + **`memory/todo.md`** — the concrete next action.

## Canonical docs (all in `docs/`)
- `VOXCORE_SYSTEM_REGISTRY.md` — system inventory table.
- `VOXCORE_ARCHITECTURE_MAP.md` — layers, live/dormant/scaffold, overlaps, "Do NOT rediscover".
- `VOXCORE_BUILD_ROADMAP.md` — sequenced roadmap with preconditions/risks/DoD.
- `VOXCORE_DECISION_LOG.md` — engineering/strategy decisions (granular choices = ADRs in `docs/architecture/decisions/`; commercial log = `_canonical_state/desktop/VoxCore_Decisions_Log.md`).
- `VOXCORE_DORMANT_SYSTEMS.md` — dormant assets + activation criteria + rollback.
- `VOXCORE_GRAPH_RAG_READINESS.md` — why GraphRAG isn't built; typed-edge prerequisite; future prompt.
- `VOXCORE_MCP_DAEMON_REGISTRY.md` — 5 MCP servers + 2 daemons + reload/rollback.
- `VOXCORE_COST_OPTIMIZATION_STATUS.md` — cost tools state + adoption blockers + future cost-banking prompt.

## Supporting
- **Inventory reports (gitignored):** `AI_Studio/Reports/system_inventory_2026-05-26/` (EXISTING_SYSTEMS_MAP, BUILD_VS_IMPROVE_DECISION, COST_BANKING_READINESS, PRIVACY_REMEDIATION, NEXT_IMPLEMENTATION_PROMPT, DESKTOP_SOURCE_SUMMARY, cat_A/B/D). The canonical `docs/` files distill these.
- **Image-harvest reports (gitignored):** `AI_Studio/Reports/pictures1_ingest/` (FINDINGS, COST_NOTES, COST_BANKED, HOOKS_NOTES, OCR_FIDELITY_REPORT).
- **Per-session handoffs:** `AI_Studio/Handoffs/voxcore/` (newest at top; `_INDEX.md`).
- **Behavior rules:** `.claude/rules/`. **Lessons loop:** `tasks/lessons.md`.

## Before proposing a "new" GraphRAG / MCP server / daemon / cost system
**Check the registry + `VOXCORE_DORMANT_SYSTEMS.md` first.** We already have RAG/KG, 5 MCP servers (+ codeintel, tonguetoquill project-scoped), 2 daemons, 23 agents (5 WoW-only ones live in CalmCore since 2026-09-22), 59 listed skills (+24 turned off), 17 rules files (3 path-scoped + protocol-gate), and dormant cost tools. We do NOT yet have production GraphRAG or typed KG edges (the blocker). Most "new" ideas are improvements to existing systems.

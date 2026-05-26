# VoxCore — Handoff Index (start here)

**Last updated:** 2026-05-26. One navigational page. If you're a fresh session asking "what exists / what do I build next?", read in this order.

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
**Check the registry + `VOXCORE_DORMANT_SYSTEMS.md` first.** We already have RAG/KG, 5 MCP servers, 2 daemons, 28 agents, 79 skills, 16 rules, and dormant cost tools. We do NOT yet have production GraphRAG or typed KG edges (the blocker). Most "new" ideas are improvements to existing systems.

# VoxCore — Current State

**Updated:** 2026-09-22 (config sweep) · prior snapshot 2026-05-26 · **Branch:** `feature/ai-harvest-quick-wins` · **HEAD (pre-this-commit):** `5addae2ae1`

Navigational snapshot. Authoritative detail: `docs/VOXCORE_SYSTEM_REGISTRY.md`.

## 2026-09-22 — Claude Code config state after the optimization sweep (session 288)
- **Live per-turn context:** 75.2k → **60.8k** (headless `/context`, same method both sides). Rules 33.4k → 21.9k (six condensed, long form in `docs/rules-reference/`; protocol-gate path-scoped); MEMORY.md 6.6k → 4.3k.
- **Pins:** Fable 5.1 primary, Sonnet 5 subagents (canary-verified, no credit gate), `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=95` (the `_CODE_` spelling was never read — renamed).
- **Removed from VoxCore:** MCP `mysql` + `wago-db2` (broken), 5 WoW agents (identical in CalmCore), 6 dead `Write()` permission rules, `cpp-build-reminder` hook, `MAX_THINKING_TOKENS`.
- **Agents/skills/rules now:** 23 agents (all with `effort:`) / 59 listed skills + 24 off / 17 rules files (3 path-scoped + protocol-gate). Hook daemon 38 handlers, breadcrumbs → `AI_Studio/Reports/subagent_activity.log`.
- **Measured negative:** `skillOverrides` visibility states save 0 tokens (4 captures). Use them for behaviour only.
- **Kept by decision:** `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` (gates /skill-doctor, Remote Control, auto-updates → `claude update` is manual).
- Evidence: `AI_Studio/Reports/OPTIMIZATION_SWEEP_2026-09-22.md`, `AI_Studio/Reports/sweep_2026-09-22/APPLIED_LEDGER.md`; durable memory `memory/claude-code-config-state.md`.

## Live (production)
- **Retrieval:** hybrid FTS5 + ChromaDB (477 MB) + KG-entity RRF (`tools/excluded_hybrid_search.py`); **92.0% baseline** (run_id `43b4e9ba4752a6fc`).
- **KG:** `.cache/excluded_kg.db` (272 MB, 24,640 entities / 743K relations) — but **co-mention only, no typed edges**.
- **MCP:** 5 servers / 33 tools (voxcore-db, voxcore-server, arcanum, docs-rag, local-llm).
- **Daemons:** hook_daemon v1.3.0 (25 routes; 38 handlers wired as of 2026-09-22); excluded-corpus daemon (PARTIAL, 6 known issues).
- **Agents/skills/rules:** ~~28 / 79 / 16~~ → 23 / 59 listed (+24 off) / 17 files (as of 2026-09-22).

## Dormant (committed/built, not active)
- Cost tools: `tools/model_router.py`, `tools/anthropic_helpers.py` (0 importers); `config/backend_selection.yaml` (inert, untracked).
- Memory Control Plane v0.1 (`tools/memory_*.py`, commit `73c6d4c771`, unwired).
- hook_daemon CC-05 breadcrumb (live on next reload); sql-write-monitor route (unwired).

## Scaffold-only (do NOT build this session)
- `graphrag/PLAN.md`, `contradiction/PLAN.md` — both gated on **typed KG edges** (absent).

## Blocked / entangled (do NOT touch)
- `citation_scorer.py` (+93), `quality_probe.py` (+23), `excluded_hybrid_search.py` (+105) — prior-session uncommitted work; reconcile before any cost/eval edit.

## Privacy
- Image digest (PII) quarantined + gitignored (`_PRIVATE_quarantine/`). No exposure.

→ **Next action:** `NEXT_SESSION.md` and `memory/todo.md`.

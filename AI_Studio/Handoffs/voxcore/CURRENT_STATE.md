# VoxCore — Current State

**Updated:** 2026-05-26 · **Branch:** `feature/ai-harvest-quick-wins` · **HEAD (pre-this-commit):** `5addae2ae1`

Navigational snapshot. Authoritative detail: `docs/VOXCORE_SYSTEM_REGISTRY.md`.

## Live (production)
- **Retrieval:** hybrid FTS5 + ChromaDB (477 MB) + KG-entity RRF (`tools/excluded_hybrid_search.py`); **92.0% baseline** (run_id `43b4e9ba4752a6fc`).
- **KG:** `.cache/excluded_kg.db` (272 MB, 24,640 entities / 743K relations) — but **co-mention only, no typed edges**.
- **MCP:** 5 servers / 33 tools (voxcore-db, voxcore-server, arcanum, docs-rag, local-llm).
- **Daemons:** hook_daemon v1.3.0 (25 routes); excluded-corpus daemon (PARTIAL, 6 known issues).
- **Agents/skills/rules:** 28 / 79 / 16.

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

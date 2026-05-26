# VoxCore — Next Session

**Updated:** 2026-05-26. The sequenced plan lives in `docs/VOXCORE_BUILD_ROADMAP.md`; the paste-ready prompt in `AI_Studio/Reports/system_inventory_2026-05-26/NEXT_IMPLEMENTATION_PROMPT.md`.

## Next session = CONSOLIDATION / UNBLOCK (Roadmap Item 0 → 1 prep). NOT greenfield.
The blocker for everything (cost banking, dormant activation) is entanglement + untracked infra. Do:
1. **Commit untracked infra:** `config/backend_selection.yaml` + the 3 sibling rules (`documentation-discipline.md`, `measurement-discipline.md`, `session-handoff.md`) — unless this session already committed them (check `git status`).
2. **Reconcile the 4 entangled files** (owner decision): `citation_scorer.py` +93 (Phase 3.9), `quality_probe.py` +23 (Phase 4 HyDE), `excluded_hybrid_search.py` +105 (HyDE). Commit / defer / discard — do NOT overwrite.
3. **Decide disposition** of the 2 dormant control planes (cost router E1/E2; Memory Control Plane D6): wire ONE low-risk call site or explicitly park.

## Then (separate sessions, in order)
- **Cost banking** (Roadmap Item 1): Batch API on the eval sweep (~50%) in a NEW `tools/batch_eval.py` — NOT in the entangled files. Caching is a verified $0 no-op; do not add it.
- **Typed KG edges** (Item 3): the upstream unlock for GraphRAG + contradiction. Real build, paid extraction, A/B vs 92% baseline. See `docs/VOXCORE_GRAPH_RAG_READINESS.md`.
- GraphRAG (4) and contradiction (5) only AFTER typed edges.

## Hard "do not"
No GraphRAG/typed-edges/AutoReason/MCP-server/daemon builds without the roadmap preconditions. No daemon restart. No editing entangled files' behavior. No committing personal/digest artifacts.

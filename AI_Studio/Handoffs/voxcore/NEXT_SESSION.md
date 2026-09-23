# VoxCore — Next Session

**Updated:** 2026-09-22 (session 288 prepended the config-sweep follow-ups; the 2026-05-26 plan below still stands). The sequenced plan lives in `docs/VOXCORE_BUILD_ROADMAP.md`; the paste-ready prompt in `AI_Studio/Reports/system_inventory_2026-05-26/NEXT_IMPLEMENTATION_PROMPT.md`.

## First (from session 289, 2026-09-23 — superpowers activation follow-through)
1. If the Superpowers-Activate tab wrapped (likely 289b), read its handoff and `~/superpowers-work/REPORT.md`; otherwise check `doc/session_state.md` for its row before touching `~/.claude/skills/superpowers/` or `C:\Users\atayl\CLAUDE.md`.
2. Run the 7-item interactive checklist (activation prompt §6) in a fresh tab in `~/superpowers-work/scratch`.
3. Apply the two override edits for a VoxCore-primary workflow (todo item 2), then measure per-turn context (`tools/cc_context_capture.py --label superpowers-on`) against 57.8k.
4. adam.3 trims (eval-gated) and the with/without comparison on three real VoxCore tool tasks — `memory/todo.md` § Next Session items 3–4.

## Then (from session 288b, 2026-09-22 evening — audit v3 follow-ups)
1. `/start-up`, then the USER-RUN checks listed in `AI_Studio/Reports/cc_audit_v3_20260922-1804/REPORT.md` § Verification; confirm `python -c "import sys;print(sys.stdout.encoding)"` prints utf-8.
2. CalmCore tab: paste `AI_Studio/Handoffs/voxcore/2026-09-22_cc_audit_v3_followup_prompt.md` (fill its three answers). Includes the optional −5.8k MCP deferral and `askUserQuestionTimeout`.
3. Adam: Defender admin block; rules demotion (recommended against); `session_state.md` protocol home; the 28 `tools/` model IDs (GO); deadlines (4 past due + Section 1983 SOL).
4. Owner-decision uncommitted files (tools/*.py, `_canonical_state/*`, two command files, `doc/session_state.md`, `_INDEX.md`) → s.286 consolidation arc.

## Earlier (from session 288, 2026-09-22 — config sweep follow-ups; items (b)(c)(d) and the archive/plugin follow-ups are DONE in 288b)
1. **Adam decisions** queued in `AI_Studio/Reports/OPTIMIZATION_SWEEP_2026-09-22.md` § "Decisions waiting on you": GO on migrating 28 `tools/` scripts off Claude 4.x model IDs (Triad scripts default to `claude-opus-4-7`; fold in the Gemini `gemini-3.1-pro-preview` quick-win); keep/remove `skipWorkflowUsageWarning`; `enableAllProjectMcpServers` → false + allowlists; CLAUDE.md dedupe (~900 tok); one home for the `doc/session_state.md` protocol; update the 4 PAST-DUE entries in `.claude/deadlines.json` and confirm the Section 1983 SOL filing (was due 2026-09-23).
2. **First interactive session on the new config:** `python tools/cc_context_capture.py --label interactive` and spawn one subagent per effort tier to confirm `effort:` frontmatter is honoured; `python tools/cc_env_check.py` should report no 0-hit names.
3. **`/sync-infra`** — CalmCore parity deltas from the sweep: settings.json `Write()` rules, 7 agent frontmatters, hooks block (`cpp-build-reminder`), rules files; `check_write_size.py` byte-diff.

## Next session = CONSOLIDATION / UNBLOCK (Roadmap Item 0 → 1 prep). NOT greenfield.
The blocker for everything (cost banking, dormant activation) is entanglement + untracked infra. Do:
1. **Commit untracked infra:** `config/backend_selection.yaml` + the 3 sibling rules (`documentation-discipline.md`, `measurement-discipline.md`, `session-handoff.md`) — unless this session already committed them (check `git status`).
2. **Reconcile the 4 entangled files** (owner decision): `citation_scorer.py` +93 (Phase 3.9), `quality_probe.py` +23 (Phase 4 HyDE), `excluded_hybrid_search.py` +105 (HyDE). Commit / defer / discard — do NOT overwrite.
3. **Decide disposition** of the 2 dormant control planes (cost router E1/E2; Memory Control Plane D6): wire ONE low-risk call site or explicitly park.

## Then (separate sessions, in order)
- **Cost banking** (Roadmap Item 1): Batch API on the eval sweep (~50%) in a NEW `tools/batch_eval.py` — NOT in the entangled files. Caching is a verified $0 no-op; do not add it.
- **Typed KG edges** (Item 3): the upstream unlock for GraphRAG + contradiction. Real build, paid extraction, A/B vs 92% baseline. See `docs/VOXCORE_GRAPH_RAG_READINESS.md`.
- GraphRAG (4) and contradiction (5) only AFTER typed edges.

## Also queued — Memory lane (from session 286b, 2026-05-26)
- **Integrate Memory Control Plane v0.1** once `feature/ai-harvest-quick-wins` merges/frees: worktree from `origin/master` → cherry-pick `73c6d4c771` → **sanitize the `tools/memory_schema.py` restricted-prefix leak** → leak-scan clean → register the design note in `docs/` → push/PR. Detail: `AI_Studio/Handoffs/voxcore/2026-05-26_session_286b_mcp-v01-integration.md`. (Gated on the SAME branch reconciliation as CONSOLIDATION/UNBLOCK above — they unblock together.)
- **Off-machine copy** of the encrypted memory backup (carries from s.285).
- **v2 unattended backup** via public-key (age/gpg).

## Hard "do not"
No GraphRAG/typed-edges/AutoReason/MCP-server/daemon builds without the roadmap preconditions. No daemon restart. No editing entangled files' behavior. No committing personal/digest artifacts.

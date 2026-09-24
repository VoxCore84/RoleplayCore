# VoxCore — Next Session

**Updated:** 2026-09-22 (session 288 prepended the config-sweep follow-ups; the 2026-05-26 plan below still stands). The sequenced plan lives in `docs/VOXCORE_BUILD_ROADMAP.md`; the paste-ready prompt in `AI_Studio/Reports/system_inventory_2026-05-26/NEXT_IMPLEMENTATION_PROMPT.md`.

## First (from session 290, 2026-09-24 — superpowers 6.4.1-adam.4 DEPLOYED (adam.3 live-test fixes + adam.4 final-reviewer `inherit`); see `AI_Studio/Handoffs/voxcore/2026-09-24_session_290_superpowers-live-test-D-E.md`)
**Paste-ready prompt for the adam.5 tab (Opus 5.5, ultracode):** `AI_Studio/Handoffs/voxcore/2026-09-24_adam5_implementation_prompt.md` — Phase 0 Opus baseline → Phase 1 tooling/guide repairs → Phase 2 fork changes (evals, agents, hook, review ranks 4/7/9/10, A02, rank 3 CONFIGURE-FIRST, trims) → Phase 3 verification + deploy → Phase 4 docs. Adam edits its "Standing authorizations" block before pasting.
0. **Model note:** evals and headless probes use the session's default model as the subject; every number so far was measured under Fable 5.1. Under Opus 5.5, re-run the baseline once before comparing. Eval children load NO CLAUDE.md (verified); override lines are tested with `partE/run_probes.ps1` or an eval case with `execution: append_system_prompt`.
1. **Adam:** read `~/superpowers-work/live_tests/2026-09-23/REVIEW_FINDINGS.md` § Synthesis (ranked ten), `fork/FORK-NOTES.md` § adam.3/adam.4, and handoff § 7c (ChatGPT proposal map); decide the adam.5 scope (trims + ranks 3–10 + the mapped P01/P02/P04 items; rank 3 is CONFIGURE-FIRST).
2. adam.5 per `~/superpowers-work/README.md` loop: fork edits → `update_deployed.ps1 -DryRun` → `eval_run.ps1 -Plugin <fork>` both tags (no deploy needed for evals) → deploy → `partE/run_probes.ps1` for any behavior claim. Write the FORK-NOTES entry BEFORE deploying. Tooling first: P03 updater exit-code/snapshot repairs and the P05 launcher/guide corrections (not fork files, no version bump).
3. Small fixes queued: `hooks/run-hook.cmd` mingw64 probe gap + test pin (README § Known issues 1); `tools/activation/eval_run.ps1` trace-copy loop (copies 0; use `partE/copy_traces.py` meanwhile); a `readonly-reviewer` agent type (Read/Grep/Glob) for read-only workflows.
4. Optional interactive re-check of S11 and S13 in a fresh scratch tab (guide § 0 setup); headless evidence is n=3 each.
5. Cleanup (Adam's call): ~130 `%TEMP%\claude-eval-*` dirs, 18 clones under `live_tests/2026-09-23/partE/repos/`, the 446 KB `w0qpx1320.output` task file.

## Then (from session 289b, 2026-09-23 — superpowers is ACTIVE and verified; see `AI_Studio/Handoffs/voxcore/2026-09-23_session_289b_superpowers-activation.md` + `~/superpowers-work/REPORT.md`)
1. ~~**Adam:** run the 7-item interactive checklist (REPORT §7) in a fresh tab in `~/superpowers-work/scratch`; record results in REPORT §4 column (c).~~ DONE 2026-09-23 evening via the live test Part A (A1–A6 PASS per `00_SETUP_PREFLIGHT.md`).
2. Two override edits for a VoxCore-primary workflow (`memory/todo.md` item 2), mirror in `CLAUDE_MD_OVERRIDES.md`, then `python tools/cc_context_capture.py --label overrides-v2` against **60.5k** (the new baseline with superpowers on).
3. adam.3 eval-gated trims: n=3 before/after both arms with `superpowers-work/tools/activation/eval_run.ps1` (keeps traces, logs the CLAUDE.md SHA); bump to adam.3 with a FORK-NOTES entry; robocopy over the deployed copy.
4. With/without comparison on three real VoxCore tool tasks (`claude --plugin-dir`); nobody has run it.
5. Rollback recipe if anything misbehaves: move `~/.claude/skills/superpowers` out of the skills folder (renaming does not unload it) and restore `C:\Users\atayl\CLAUDE.md` from the NEWEST `CLAUDE.md.active_*_line10` snapshot (2026-09-24, ten lines). The 2026-09-23 snapshot `CLAUDE.md.active_20260923_171424_superpowers` predates line 10 and would silently drop it; the pre-block backup drops the whole block.

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

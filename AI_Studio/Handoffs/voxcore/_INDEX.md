# VoxCore Session Handoffs — Index

Per-session handoff documents for the VoxCore project. Newest at top.

## Conventions

- **Real-time handoffs**: written by `/wrap-up` Step 6.5 at end of session. Contemporaneous, primary source for next-session context. No `RECONSTRUCTED` tag.
- **Reconstructed handoffs**: back-filled from memory files via `tools/backfill_handoffs.py` when a session predates the wrap-up Step 6.5 convention. Tagged `RECONSTRUCTED` in the filename and frontmatter; readers should cross-verify against the cited memory-file lines and commits before citing externally.

## Filename pattern

`<YYYY-MM-DD>_session_<N>[_RECONSTRUCTED]_<short-tag>.md`

Examples:
- `2026-05-02_session_277b_evening.md` — real-time, written by /wrap-up
- `2026-05-02_session_277_RECONSTRUCTED_15-item-knockdown-inline-grounded.md` — back-filled

## Sessions covered (15 of ~50+ in recent-work.md)

| Date | Session | Type | File |
|---|---|---|---|
| 2026-05-02 | 277b | real-time | `2026-05-02_session_277b_evening.md` |
| 2026-05-02 | 277 | reconstructed | `2026-05-02_session_277_RECONSTRUCTED_15-item-knockdown-inline-grounded.md` |
| 2026-04-28 | 274 | reconstructed | `2026-04-28_session_274_RECONSTRUCTED_wrap-up-refactor-resume-evidence.md` |
| 2026-04-27 | 273 | reconstructed | `2026-04-27_session_273_RECONSTRUCTED_knowledge-graph-build.md` |
| 2026-04-27 | 272 | reconstructed | `2026-04-27_session_272_RECONSTRUCTED_hook-unification-tribal.md` |
| 2026-04-27 | 271 | reconstructed | `2026-04-27_session_271_RECONSTRUCTED_env-config-claude_code_use_powershell_tool.md` |
| 2026-04-27 | 270 | reconstructed | `2026-04-27_session_270_RECONSTRUCTED_hook-verification-voxcore-db.md` |
| 2026-04-27 | 269 | reconstructed | `2026-04-27_session_269_RECONSTRUCTED_hook-infra-overhaul.md` |
| 2026-04-21 | 268 | reconstructed | `2026-04-21_session_268_RECONSTRUCTED_ex-sme-corpus-prime.md` |
| 2026-04-19 | 267 | reconstructed | `2026-04-19_session_267_RECONSTRUCTED_triad-pipeline-audit.md` |
| 2026-04-18 | 266 | reconstructed | `2026-04-18_session_266_RECONSTRUCTED_insights-review-deliverable.md` |
| 2026-04-18 | 265 | reconstructed | `2026-04-18_session_265_RECONSTRUCTED_ukb-4-pass-update.md` |
| 2026-04-18 | 264 | reconstructed | `2026-04-18_session_264_RECONSTRUCTED_openclaw-2026414-setup.md` |
| 2026-04-16 | 263 | reconstructed | `2026-04-16_session_263_RECONSTRUCTED_claude-code-deep.md` |
| 2026-04-12 | 262 | reconstructed | `2026-04-12_session_262_RECONSTRUCTED_ex-refresh---audio-hybrid.md` |

## Sessions NOT covered (sparser memory entries — opt-in if needed)

Sessions 100s through ~261 exist in `memory/recent-work.md` but with shorter entries. Not back-filled by default. Run `python tools/backfill_handoffs.py --sessions <N> <N> ...` to opt in.

## Known limitations of reconstructed handoffs

1. **Synthesis-of-summary**: each reconstructed handoff is composed from `recent-work.md` (already a session-end summary) + `automation-ledger.md` + `resume-evidence.md`. Not direct evidence; reconstructive layer.
2. **Commit-hash matching is approximate**: `git log --all --grep="session N"` can return false matches when commit messages are ambiguous (e.g., commit message references multiple sessions). The reconstructed handoff's "Commit" field is a best-guess; the authoritative source is the "Commit: ..." marker in the recent-work.md entry body if present.
3. **State-of-the-world warnings missing**: reconstructed handoffs don't include the warnings section that real-time handoffs have ("don't run parallel Opus", "v4 vs v5 trade-off", etc.) because those require contextual judgment that wasn't captured in memory at the time.
4. **No "files to read at session start" section**: real-time handoffs include this; reconstructed don't (memory files don't capture this prescriptively).

## Cross-project handoff aggregation

`/handoff-index` slash command rebuilds `VoxCore/handoffs/INDEX.md` by scanning every project's `AI_Studio/Handoffs/*` folder. This `voxcore/` subdir is one of those scanned sources (alongside `calmcore/` and `calmsniffer/`).

## Maintenance

- New sessions get real-time handoffs via `/wrap-up` Step 6.5 (no manual action needed).
- Updates to this index: re-run `tools/backfill_handoffs.py` after adding/removing sessions, then manually update the table above (or scriptify if maintenance burden grows).
- To re-generate any reconstructed handoff after memory files change: `python tools/backfill_handoffs.py --sessions <N>` (overwrites without `--skip-existing`).

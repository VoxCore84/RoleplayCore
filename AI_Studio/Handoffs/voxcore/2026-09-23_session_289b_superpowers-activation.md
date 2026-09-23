# Session 289b — 2026-09-23 — Superpowers 6.4.1-adam.2 activated, triple-checked, one fix, rollback proven

**Session:** 289b (Superpowers-Activate tab, Claude Code session `66dc07cf`, Fable 5.1 xhigh, ultracode) · **Duration:** ~16:30–17:45 · **Commit:** see `git log -1` after this wrap-up (`docs: session 289b wrap-up …`) · **API spend (list price, Max plan usage):** evals $32.31 + headless probes $14.93 + Workflow 2.36 M subagent tokens (24 agents) + context capture ~$1.

## What happened this session

Executed `AI_Studio/Handoffs/voxcore/2026-09-23_superpowers_activation_prompt.md` §1–§8 end to end. Pre-flight was green (no plugin entry, fork tests 8/0/2, strict validate pass). The fork was robocopied to `~/.claude/skills/superpowers` (277 files, byte-identical), the nine-line block appended to the global `CLAUDE.md` with a byte-exact script (+12/−0, LF preserved, backup kept), and a headless probe answered YES / 1 / five agents. The 12-row triple-check ran as one Workflow: 12 check agents (headless probes in scratch repos, hook tests, transcript parsing) each followed by an independent skeptic told to refute the result. All 12 rows came back tested-pass and all 12 verdicts upheld.

Evals were the only place anything failed. First pass: readonly 2/2 cases at 3/3, write 3/5 at 3/3; `no-brainstorm-override` missed once on a 2-1 LLM-judge split over a reply that plainly complied (rerun 3/3), and `react-todo` missed once with a unanimous judge FAIL and no trace. A rerun with `--keep-temp` reproduced the miss with evidence: brainstorming fired, then the session wrote a design spec "under stated assumptions", invoked writing-plans and spawned subagents nested three deep until the 240 s timeout. A probe from a Temp-nested cwd proved eval sessions load the global `CLAUDE.md`, so the new block was the variable versus the prior day's 3/3. Per §5 (override first) line 9 was amended by one sentence; the after-fix write suite went 5/5 cases at 3/3 and readonly 2/2. No plugin file changed, so the version stays adam.2.

Context capture measured 58.0k → 60.5k (+2.5k, above the +1.5k estimate). The rollback rehearsal found the runbook's rename-to-`.off` step does not deactivate anything (still listed loaded, probe YES); moving the folder out of `~/.claude/skills` does, and moving it back plus restoring the SHA-verified snapshot reactivated it. The runbook carries a strikethrough correction.

## Headline numbers

| Claim | Number | Tier | Evidence |
|---|---|---|---|
| Matrix rows verified | 12/12 tested-pass, 12/12 skeptic-upheld (24 agents, 0 errors) | PROVEN | `AI_Studio/Reports/superpowers_activation/{checks,verify}/`, Workflow journal `…/subagents/workflows/wf_c04bf29f-334/journal.jsonl` |
| Eval cases at 3/3 with the plugin (Windows-runnable) | 5/7 before fix → **7/7 after** (n=3 per pass, judge Sonnet 5 via `haiku` alias, threshold 1.0) | WELL-SUPPORTED (n=3) | `evals/activation-write-n3.json`, `evals/activation-write-n3-after-line9.json`, `evals/activation-readonly-n3*.json` |
| Root cause of the one real eval failure | brainstorming fired, purpose question skipped, spec written under assumptions | PROVEN | `evals/traces/react-todo_rerun_88Ua42.jsonl` |
| Per-turn context delta | 58.0k → 60.5k (+2.5k) | PROVEN | `AI_Studio/Reports/context_captures/20260923_165500_superpowers-on.md` |
| Rollback | both directions, SHA-256-verified restores; rename method FALSE | PROVEN | `probes/row11_deactivate.txt`, `probes/row11_reactivate.txt`, `probes/row11_*_probe.json` |
| Deployment fidelity | fork vs deployed `diff -rq` = 0 lines | PROVEN | `checks/row_00_deterministic_a_columns.md` |

## State-of-the-world warnings

- **The plugin is live in every session under `C:\Users\atayl`** (VoxCore, CalmCore, scratch). Bootstrap once per session, five `superpowers:*` agents in the Agent tool. `/context` will show ~+2.5k.
- **Global `C:\Users\atayl\CLAUDE.md` changed twice today**: block appended (16:38) and line 9 amended (17:06). Backups: `CLAUDE.md.bak_20260923_163824_superpowers` (pre-block), `CLAUDE.md.bak_20260923_170627_line9` (pre-amendment); active snapshot `CLAUDE.md.active_20260923_171424_superpowers`. The canonical block text is `AI_Studio/Reports/superpowers_supercharge/CLAUDE_MD_OVERRIDES.md` (amendment note included).
- **Eval sessions load the global CLAUDE.md.** Any before/after eval comparison must record its SHA-256; a block edit moves eval results.
- **To deactivate: move the folder out of `~/.claude/skills`.** Renaming inside that folder does nothing. `claude plugin disable superpowers@skills-dir` is documented but not exercised (it writes user settings.json).
- **`--keep-temp` leftovers**: ~48 `%TEMP%\claude-eval-*` dirs (8.3 MB) the harness cannot seal on Windows. Needed traces are in `evals/traces/`. Cleanup is Adam's call.
- **Owner-decision uncommitted files** (tools/*.py, `_canonical_state/*`, two command files) were left untouched again. This wrap commits only `tasks/lessons.md`, `doc/session_state.md` (my row + the two May-05 note lines that had been pending), `AI_Studio/Handoffs/voxcore/_INDEX.md` (index rows), `docs/VOXCORE_HANDOFF_INDEX.md`, `CURRENT_STATE.md`, `NEXT_SESSION.md`, and this handoff.
- **Deadline data inconsistency**: `.claude/deadlines.json` dates the Section 1983 SOL 2026-09-23 but its note says "2 years from Oct 23, 2024" (2026-10-23). Not this tab's lane; flagged at session start and in `todo.md`.
- **adam.3 deliberately not started** (prompt §8).

## What's real (measured numbers)

| Dimension | Value | Provenance |
|---|---|---|
| Active plugin | `superpowers@skills-dir` 6.4.1-adam.2, user scope, `~\.claude\skills\superpowers`, loaded | `claude plugin list` 17:19 |
| Global CLAUDE.md | 6,441 bytes, LF, SHA-256 `CE0372FC…D662E` | rollback log |
| Per-turn context (VoxCore) | 60.5k live (agents 2.1k, memory files 31.9k, skills 5.6k, messages 1.3k) | `20260923_165500_superpowers-on.md` |
| CalmCore `/context` | 48.7k, bootstrap once, 5 agents, 15 skills, own rules loaded | `probes/row12_calmcore_context.md` |
| Fork tests | session-start 8/8, run-hook-cmd 4/4, plugin-agents 40 assertions, worktree-path-policy 9/9, sdd-workspace 24/24, executing-plans-scripts 15/15 | `probes/row00_*.txt` |
| Compaction note | once, 3,976 chars, 156 ms | `probes/row02_*.json` |
| Reviewer models | task-reviewer `claude-sonnet-5`; final-reviewer `claude-fable-5-1` | `checks/row_03_reviewers.md` |

## Files to read at session start

```
Read C:\Users\atayl\VoxCore\docs\VOXCORE_HANDOFF_INDEX.md
Read C:\Users\atayl\VoxCore\AI_Studio\Handoffs\voxcore\2026-09-23_session_289b_superpowers-activation.md
Read C:\Users\atayl\superpowers-work\REPORT.md
Read C:\Users\atayl\VoxCore\AI_Studio\Handoffs\voxcore\NEXT_SESSION.md
Read C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory\project_superpowers_fork.md
Read C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory\claude-code-config-state.md
Read C:\Users\atayl\VoxCore\tasks\lessons.md
Read C:\Users\atayl\superpowers-work\fork\FORK-NOTES.md   (only if starting adam.3)
```

## Top priorities for next session

1. Adam runs the 7-item interactive checklist (REPORT §7) in a fresh tab in `~/superpowers-work/scratch`; record in REPORT §4 column (c).
2. Two override edits for a VoxCore-primary workflow (line 8 production-tool GO; line 7 drop MySQL clause); mirror in `CLAUDE_MD_OVERRIDES.md`; re-measure context against 60.5k.
3. adam.3 eval-gated trims with `superpowers-work/tools/activation/eval_run.ps1` (traces kept, CLAUDE.md SHA logged), n=3 before/after both arms; version bump + FORK-NOTES entry.
4. With/without comparison on three real VoxCore tool tasks (unrun since 289).
5. Cleanup of `%TEMP%\claude-eval-*` (Adam's call).
6. Carry-overs from 288b: USER-RUN audit checks; CalmCore follow-up prompt; owner-decision files → s.286 consolidation; 28 `tools/` model IDs GO; deadlines reconciliation; Tolin `counsel.zip` encrypted only.

## Standing directives (unchanged, plus this session's)

- Legal accuracy: 100%; cite statutes; distinguish known/told/documented; never fabricate. The 3 CRITICAL corrections must never regress (DoDSER = non-completion not falsification; OPB 121 not 164; Taylor signed rebuttal / Tolin transmitted).
- No production code changes without Adam GO. Triad for non-trivial implementation. Cite source on every measured claim.
- The case archive folder is READ-ONLY (rule: `.claude/rules/excluded-corpus.md`). Clinical (L5) verbatim only. Confidence tiers on evidentiary claims.
- `VoxCore_File_System_Map.md` desktop-only — never git-add. Memory repo: never push.
- External POD build NOT distributable without counsel redaction policy.
- From 288: keep `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`; never recommend `/skill-doctor` (use `tools/skill_audit.py`); `excluded-corpus.md` untouchable; `skillOverrides` is for behaviour, not tokens; grep `claude.exe` before removing/renaming any env key; for git-tracked JSON edit lines, never `json.dump`.
- From 288b: power first, efficiency second (`memory/feedback_power_over_efficiency.md`); Fable 5.1 xhigh everyday, no auto mode. Token claims need `cc_context_capture.py` totals. Verify externally authored Claude Code claims with a docs agent before executing them. Restart the daemon only with `tools/daemon_restart.ps1`.
- From 289: never edit `~/.claude/skills/superpowers/` in place — edit `fork/`, test, re-copy; any shipped-file change bumps the version with a FORK-NOTES entry; the seven upstream-identical skills stay byte-identical unless an eval fails at n=3 after an override attempt.
- **New (289b):** eval runs always `--keep-temp` (use `eval_run.ps1`) and copy traces out immediately; record the global CLAUDE.md SHA-256 in every eval header; deactivate the plugin by moving the folder out of `~/.claude/skills`, never by renaming; `claude plugin disable` untested here; adam.3 not started until Adam says GO.

## Workflow reminders for the next tab

- Superpowers is now in every session: brainstorming will fire on new-feature requests; overrides lines 2 and 9 cover pre-authorized edits and prose deliverables. If it gates something it should not, the fix goes in the block first (configure-first), then an eval at n=3.
- Headless probes: `superpowers-work/tools/activation/probe.ps1` (any prompt) / `probe.sh` (no slash prompts) / `context_probe.ps1` (`/context`). Transcripts under `~/.claude/projects/<encoded cwd>/`; the bootstrap is identified by "Below is the full content of your 'superpowers:using-superpowers' skill", not "You have superpowers".
- Workflow results: read `journal.jsonl` with `wf_journal.py`; do not parse the task-output file.
- Bash tool mangles backslashes/backticks inline; arrays do not survive `pwsh -File`; `cmd //d //c C:/path/file.cmd` works from Bash.
- Subagents run Sonnet 5 natively at 1M; background-agent mailbox reports arrive at turn end.

## Provenance

Generated 2026-09-23 ~17:45 by session `66dc07cf` (Fable 5.1, ultracode). Session totals: 12 matrix rows × 3 columns tracked (24 (a)/(b) cells tested, 7 (c) cells handed to Adam); 24 Workflow agents; 18 headless probes; 6 eval invocations / 66 runs; 1 fix (1 line, outside the plugin); 1 runbook correction; 9 helper scripts; REPORT.md 11 sections (validator 0 errors); 4 lessons; memory: 3 files edited, 1 rewritten.

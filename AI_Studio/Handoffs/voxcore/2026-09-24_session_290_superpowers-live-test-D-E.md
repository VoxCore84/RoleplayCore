# Session 290 (2026-09-24) — Superpowers live test Parts D and E → 6.4.1-adam.3 deployed

**Tab:** VoxCore, session `4a515fe3-8f2f-4b92-9218-bfaf5817f5a6`, Claude Code 2.1.281, Fable 5.1. **Branch:** `feature/ai-harvest-quick-wins` (no VoxCore code changed; docs, rules, memory only). **Status:** COMPLETE. **Started** after a machine restart killed the blind test tab (`b74d5b31`) right after Part C; that tab's results were intact on disk.

Guide: `C:\Users\atayl\superpowers-work\LIVE_TEST_GUIDE.md` v2.1. Evidence root: `C:\Users\atayl\superpowers-work\live_tests\2026-09-23\` (`LIVE_TEST_RESULTS.md`, `REVIEW_FINDINGS.md`, `partD/`, `partE/`). Plugin log: `superpowers-work/fork/FORK-NOTES.md` § 6.4.1-adam.3 (three dated addenda). Report: `superpowers-work/REPORT.md` § 0.

## 1. Phases completed

| Phase | Status | Cost | Output |
|---|---|---|---|
| 0. Recovery + preflight cross-check | done | $0 | Part C copies hash-identical (`4DF46C68…`); S11 "SDD ran" claim in `00_SETUP_PREFLIGHT.md` struck through with a dated correction (transcript: 0 implementer/task-reviewer/re-reviewer dispatches) |
| Housekeeping (Adam's ask) | done | $0 | `.claude/deadlines.json`: 5 past-due entries purged, alert clean; `memory/project_superpowers_fork.md` broken ref fixed; staleness sweep clean of BROKEN |
| D. Read-only plugin review (Workflow `wf_fa59346b-579`) | done | 7.98 M subagent tokens, 743 tool calls, 14.1 min | `REVIEW_FINDINGS.md` (1,052 lines): 22 units × (a)–(f), 72 findings = 33 UPHELD / 25 AMENDED / 14 REFUTED / 0 unverified, ranked top-10; plugin trees hash-identical before/after (554/554) |
| E. Fix loop → adam.3 | done | $107.38 computed (`partE/cost_ledger.md`: probes $75.45, evals $31.94) | `fork/` L-01 + L-02, version 6.4.1-adam.3 deployed 02:09; CLAUDE.md line 10 (CONFIGURE-FIRST for S11); before/after probes and evals below |

## 2. Metrics deltas

| Dimension | Before | After |
|---|---|---|
| S13c (finishing menu, zero-commit branch in a worktree; headless n=3) | 3/3 deleted the branch, no menu | 3/3 presented the menu, branch + worktree intact |
| S13a (using-git-worktrees invoked on "set up to implement"; headless n=3) | 0/3 failures (fresh sessions invoke it) | 0/3 failures — no headless repro; L-02 rests on the review finding + live transcript |
| S11 (writing-plans re-invoked on a resumed second plan; headless n=3, two turns) | 0/3 re-invoked (turn 1 ×1, turn 2 ×0) | 3/3 re-invoked (one invocation per turn) — via CLAUDE.md line 10 |
| Eval suite (7 Windows cases, n=3, both arms) | 7/7 at 3/3 (289b, adam.2, CLAUDE.md `CE0372FC…`) | 7/7 at 3/3 on the adam.3 fork pre-deploy; 7/7 at 3/3 deployed with line 10 (`2F1C3AC4…`) |
| Global `C:\Users\atayl\CLAUDE.md` | 9 override lines, 6,441 bytes | 10 lines, 6,831 bytes; backup `CLAUDE.md.bak_20260924_020918_line10` |
| Deployed plugin | 6.4.1-adam.2 | 6.4.1-adam.3 (`claude plugin list` loaded; probe YES + five agents) |

## 3. What changed, exactly

- `fork/skills/finishing-a-development-branch/SKILL.md` — after Step 4's "the integration decision is theirs" paragraph: "clean it up" is not a menu answer; a precedence rule gates skill invocation, not steps inside an invoked skill; a zero-commit branch still gets the menu. Two Common Rationalizations rows. (REVIEW_FINDINGS ranks 1 and 8; findings finishing-a-development-branch-1/-2.)
- `fork/skills/using-git-worktrees/SKILL.md` line 12 — invoke the skill even when a declared preference seems to settle the isolation question; Step 0 fast-paths it. (rank 2; using-git-worktrees-2)
- `fork/skills/executing-plans/SKILL.md` and `fork/skills/subagent-driven-development/SKILL.md` Setup — invoke using-git-worktrees regardless of a standing preference (it still runs Project Setup and the baseline run); ledger `Setup: <outcome> — baseline <command>: <result>` before Task 1 / first dispatch. (rank 2; executing-plans-3 as amended by its skeptic)
- Version fields ×3 → 6.4.1-adam.3; `FORK-NOTES.md` entry + 3 addenda. Backups of the eight pre-edit files: `partE/backup_fork_adam2/` (SHA256SUMS.txt).
- `C:\Users\atayl\CLAUDE.md` — line 10 appended by `superpowers-work/tools/activation/append_line10.py` (+1/−0). Mirrored with a dated note in `AI_Studio/Reports/superpowers_supercharge/CLAUDE_MD_OVERRIDES.md`.
- Not changed: the seven upstream-identical skills (byte-identical to upstream still); hooks, agents, scripts, tests, evals.

## 4. What's now possible

- Headless reproduction of skill behaviors with real git state: `partE/run_probes.ps1` (+ `setup_repo.ps1`, `probe_tools.py`) clones the live-test repo per run, arranges branch/worktree state, runs `claude -p` with stream-json, and summarizes tool calls; S11 uses `--resume` for a two-turn script. Reusable for adam.4 and for any "did the skill fire" question.
- Fork evals before deploying: `eval_run.ps1 -Plugin <fork>` is clean because the harness ignores user-scope plugins (proven from init records, `evals/traces/adam3-isolation-check_*`).
- The Part D review harness (22 reviewers → skeptic per finding → synthesis) is a saved Workflow script; re-run with `resumeFromRunId` for cache hits.

## 5. Queued for next session (priority order)

1. **Adam: read `REVIEW_FINDINGS.md` § Synthesis and `FORK-NOTES.md` § adam.3; decide the adam.4 scope.** $0, 20 min. Blocks 2.
2. **adam.4**: context trims (FORK-NOTES § adam.3 plan, eval-gated) + REVIEW_FINDINGS ranks 4, 7, 9, 10 (LOW, fork-editable, exact text in the synthesis) + rank 3 via CONFIGURE-FIRST (new eval case at n=3 first) + graders 5 and 6. Evals ~$16 per pass × 2 tags × before/after ≈ $32; probes as needed. ~2 h. Blocker: Adam GO.
3. **`hooks/run-hook.cmd` mingw64 probe gap** (README § Known issues 1) + pin `test-run-hook-cmd.sh` case 2. ~30 min. Fork change → adam.4 or adam.5.
4. **Fix `eval_run.ps1`'s trace-copy loop** (errors on `$c.arms.$armName`, copies 0); until then `partE/copy_traces.py`. 10 min.
5. **Optional interactive re-check** of S11 and S13 only, in a fresh scratch tab per guide § 0 (headless evidence is n=3 each; the interactive lapse for S13a was never reproduced headlessly). Adam, ~25 min.
6. **`readonly-reviewer` agent type** (`.claude/agents/`, tools Read/Grep/Glob) so read-only workflows enforce the ban structurally (Part D: 11/95 agents used Bash despite the instruction). 15 min.
7. **Cleanup, Adam's call**: `%TEMP%\claude-eval-*` (now ~130 dirs; needed traces are in `evals/traces/`), `partE/repos/` (18 scratch clones), the 446 KB `w0qpx1320.output` (parts are the durable copy).

## 6. Architectural debt incurred

- The S11 fix lives in the CLAUDE.md block, not in the plugin: a session without the block still recalls instead of re-invoking. Correct under configure-first; revisit only if the plugin is ever used without the block.
- `FORK-NOTES.md` was edited after the deploy; the deploy guard refuses a same-version re-run, so the file was copied over by itself and logged. Lesson filed (write the entry before deploying).
- Prompt-only tool bans in Workflow agents are advisory (Part D). Structural fix queued (#6).
- The S13 after-state carries line 10 as well as L-01; attribution to L-01 is argued (line 10 says nothing about the menu), not isolated by a separate run.
- No Gemini/Triad audit of the four prose changes: the Part E runbook does not include one, and Part D's 72 skeptic-checked findings plus the eval suite served as the review. Flagged, not run.

## 7. Honest assessment

Worked: the README loop as written; clean before/after for S13c and S11; the harness isolation check saved a deploy-then-rollback cycle. Did not work as hoped: S13a never reproduced headlessly (its live cause needed prior context), so L-02 is justified by evidence other than a headless delta. Surprises: the eval harness ignores user-scope plugins; `--resume` two-turn probes cost about $10.50 each (Fable, full plan writes on both turns) — use a cheaper model or a shorter turn-1 task for repro-only runs next time; Part D reviewers substituting Bash for Grep.

## 7b. Correction made after the handoff was first written (2026-09-24 03:15)

While reviewing ChatGPT's consolidated proposal, its P02-E ("stop assuming eval instruction inheritance") was tested in the runner: a probe case in a temp plugin copy (`partE/tmp_plugin_probe`, `evals/adam3-inherit-check`) asked both arms to quote line 10 of the block; both answered NONE. Eval children load no CLAUDE.md (docs agree). This withdraws the 289b lesson and the sentences above that call the CLAUDE.md hash "part of what evals measure": the `adam3-line10-*` re-run was redundant (identical result, as expected), the evals in the metrics table measure plugin prose only, and the S11 fix (line 10) is proven by the headless probes, which do load the file, not by evals. Corrections with dated notes: FORK-NOTES, README, `eval_run.ps1` comment, CURRENT_STATE, the 289b handoff, the registry row, CLAUDE_MD_OVERRIDES, REPORT § 0, memory. New option for adam.4: `append_system_prompt` in a case's `execution:` block can carry the ten-line block into both eval arms deliberately.

## 7c. adam.4 (03:35): final reviewer follows the session model

Adam's Fable quota was running out; `agents/final-reviewer.md` was pinned to `fable`, so the dispatch would fail under Opus. Changed to `model: inherit` (docs: "use the same model as the main conversation", resolved before `CLAUDE_CODE_SUBAGENT_MODEL`; no fallback-list syntax exists). Deployed as 6.4.1-adam.4 via the update script (tests 8/0/2, validate ok, identical post-copy). Verified by two headless dispatches: Fable session → subagent `claude-fable-5-1`; `--model opus` session → `claude-opus-5-5` (`partE/probes/adam4_final_reviewer_*.json`, reader `partE/subagent_model.py`). The trims and ranked items now target adam.5. ChatGPT's two proposals were reviewed the same hour; the map is in the conversation and the actionable items are folded into § 5 as adam.5 candidates: P02-C, P02-B (llm grader with `focus`), P01, P04, P02-A, an `append_system_prompt` eval case carrying the ten-line block, P03 updater exit-code/snapshot repairs, P05 launcher and guide corrections; C01–C04 and A01–A03 deferred; P05-E rejected.

## 8. Cost and wall time

Part D: 95 agents, 7.98 M subagent tokens, 14.1 min. Part E: $107.38 list-price equivalent on Max-plan usage (`partE/cost_ledger.md`). Wall clock: recovery + housekeeping ~40 min; Part D ~35 min including assembly; Part E ~2 h 40 min (00:15–02:55), most of it waiting on the S11 two-turn batches.

## 9a. Files to read at session start (next tab)

```
Read C:\Users\atayl\VoxCore\docs\VOXCORE_HANDOFF_INDEX.md
Read C:\Users\atayl\VoxCore\AI_Studio\Handoffs\voxcore\NEXT_SESSION.md
Read C:\Users\atayl\VoxCore\AI_Studio\Handoffs\voxcore\2026-09-24_adam5_implementation_prompt.md
Read C:\Users\atayl\superpowers-work\README.md
Read C:\Users\atayl\superpowers-work\fork\FORK-NOTES.md
Read C:\Users\atayl\superpowers-work\live_tests\2026-09-23\REVIEW_FINDINGS.md   (§ Synthesis first)
Read C:\Users\atayl\VoxCore\tasks\lessons.md   (2026-09-23 and 2026-09-24 entries)
Read C:\Users\atayl\VoxCore\doc\session_state.md   (Active Tabs table)
```

## 9b. Standing directives (unchanged unless noted)

- Never edit `~/.claude/skills/superpowers/` by hand: edit `fork/`, run `update_deployed.ps1`. Any shipped-file change bumps the version and gets a FORK-NOTES entry written BEFORE the deploy (new this session).
- The seven upstream-identical skills stay byte-identical unless an eval fails at n=3 after a CLAUDE.md override was tried (configure-first).
- CLAUDE.md block edits only via a byte-exact script with backup; mirror in `CLAUDE_MD_OVERRIDES.md`; refresh the `CLAUDE.md.active_*` snapshot afterwards (new: the rollback snapshot must postdate the last block edit).
- Evals measure plugin prose only (eval children load no CLAUDE.md or user plugins); override lines are tested with headless probes or an `append_system_prompt` case (new this session, supersedes the 289b directive to log the CLAUDE.md SHA as a confound).
- Same subject model on both sides of any comparison; n=3; per-run spread; regressions reported with lifts (measurement-discipline).
- Read-only review agents use a tool-restricted agent type; hash the reviewed tree before and after (new this session).
- Multi-tab: claim a `doc/session_state.md` row at start, close it at end. `/wrap-up` at session end.

## 9c. Workflow reminders for the next tab

- `/start-up` first. Then Phase 0 of the adam.5 prompt before any edit (Opus baseline).
- Call helper `.ps1` files in-process (`& script.ps1 -ExtraArgs @(...)`); through `pwsh -File` the array flattens (bit twice now).
- Write scripts to files instead of inline backslashes/heredocs; `PYTHONUTF8=1`; PowerShell commands under ~2,000 characters.
- `--keep-temp` on every eval; copy traces immediately (`eval_run.ps1` now calls the Python copier).
- Workflow reviews: ≤16 concurrent, one skeptic per finding, `agentType: 'readonly-reviewer'` for read-only stages.
- Cost: two-turn S11 probes ~$10 each on Fable; consider `--max-turns` or a cheaper subject for repro-only runs.

## 9d. Provenance

Generated 2026-09-24 ~04:00 local by the VoxCore tab (session 290, `4a515fe3`), Claude Code 2.1.281, Fable 5.1. Session totals: 2 plugin releases deployed (adam.3, adam.4); 1 Workflow (95 agents); 30 headless probes + 7 eval invocations (~$110); 4 lessons filed + 1 withdrawn; 3 documents written (this handoff, the adam.5 prompt, REVIEW_FINDINGS via workflow); 11 files corrected with dated notes.

## 9. Files modified this session (outside `superpowers-work/`)

`VoxCore/.claude/deadlines.json`; `VoxCore/doc/session_state.md` (2 rows); `VoxCore/tasks/lessons.md` (+3 entries); `VoxCore/AI_Studio/Reports/session_state_live.md`; `VoxCore/AI_Studio/Reports/superpowers_supercharge/CLAUDE_MD_OVERRIDES.md`; `VoxCore/AI_Studio/Reports/superpowers_activation/evals/` (+5 result sets, 86 traces); `VoxCore/docs/VOXCORE_HANDOFF_INDEX.md`; `AI_Studio/Handoffs/voxcore/NEXT_SESSION.md`; memory `project_superpowers_fork.md`, `MEMORY.md`, `todo.md`; `C:\Users\atayl\CLAUDE.md` (+1 line); `C:\Users\atayl\.claude\skills\superpowers\` (deploy). Inside `superpowers-work/`: `fork/` (4 SKILL.md, 3 version files, FORK-NOTES.md), `REPORT.md` § 0, `UPDATE_LOG.md`, `superpowers-6.4.1-adam.3.patch`, `tools/activation/append_line10.py`, `live_tests/2026-09-23/{REVIEW_FINDINGS.md, 00_SETUP_PREFLIGHT.md, partD/, partE/}`.

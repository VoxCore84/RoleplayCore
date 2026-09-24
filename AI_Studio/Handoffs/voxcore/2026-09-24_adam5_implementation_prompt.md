# Superpowers 6.4.1-adam.5 — implementation prompt for a fresh Claude Code tab (Opus 5.5, ultracode)

Written 2026-09-24 by the VoxCore tab (session 290, Fable 5.1) for the next tab. Paste everything below the line into a new tab opened in `C:\Users\atayl\VoxCore`. Adam reviews the "Standing authorizations" block before pasting; the tab treats it as his instruction.

---

## 0. Who you are and what this is

You are the implementing tab for **superpowers 6.4.1-adam.5**, the personal fork of the superpowers Claude Code plugin. The previous tab finished the live test (Parts A–E), deployed adam.3 (three behavior fixes) and adam.4 (final reviewer follows the session model), reviewed two ChatGPT proposals, and left a ranked backlog. Your job is to turn that backlog into adam.5 with evidence, using the fork's own loop. You run on Opus 5.5 with ultracode on. Use Workflow orchestration for review and verification stages; do mechanical edits yourself.

**Read first, in this order (do not skip; do not re-derive what they record):**
1. `C:\Users\atayl\superpowers-work\README.md` — the hub: layout, the update loop, rollback, known issues.
2. `C:\Users\atayl\VoxCore\AI_Studio\Handoffs\voxcore\2026-09-24_session_290_superpowers-live-test-D-E.md` — what happened, metrics, debt, § 7b (eval-inheritance correction), § 7c (adam.4 + the ChatGPT map).
3. `C:\Users\atayl\superpowers-work\fork\FORK-NOTES.md` — § adam.3, § adam.4 and the "adam.3 plan" section (the trims). Append-only; newest last.
4. `C:\Users\atayl\superpowers-work\live_tests\2026-09-23\REVIEW_FINDINGS.md` — § Synthesis holds the ranked ten with exact old→new text; the unit sections hold the evidence.
5. `C:\Users\atayl\Desktop\Excluded\Superpowers_Consolidated_Desktop_Proposal_2026-09-24.md` and `Superpowers_Practical_Additions_2026-09-24.md` — ChatGPT's P01–P05, C01–C04, A01–A03 with exact snippets. They predate adam.3/adam.4; the map in handoff § 7c says which items survived verification.
6. `C:\Users\atayl\VoxCore\tasks\lessons.md` — the 2026-09-23 and 2026-09-24 entries (Windows shell traps, `pwsh -File` array flattening, FORK-NOTES-before-deploy, tool bans are advisory, eval children load no CLAUDE.md).

**Fixed facts (verified 2026-09-24; re-check § 1 anyway):**
- Deployed: `C:\Users\atayl\.claude\skills\superpowers` = `superpowers@skills-dir` 6.4.1-adam.4, byte-identical to `C:\Users\atayl\superpowers-work\fork` (277 files). Source of truth is `fork/`. Never hand-edit the deployed copy.
- Global `C:\Users\atayl\CLAUDE.md` ends with the ten-line "Superpowers (personal fork)" block (line 10 = "Re-invoke, don't recall"). Newest rollback snapshot: `C:\Users\atayl\CLAUDE.md.active_20260924_031152_line10`. The 09-23 snapshot predates line 10; never restore it.
- Seven upstream-identical skills (byte-identical to upstream, CONFIGURE-FIRST): using-superpowers, brainstorming, test-driven-development, systematic-debugging, verification-before-completion, writing-plans, receiving-code-review. Their prose changes only after (a) an eval case fails at n=3 and (b) a CLAUDE.md override line was tried and re-measured. Agreement between reviewers is not evidence.
- `claude plugin eval` children load NO CLAUDE.md files and NO user-scope plugins (runner-verified: `AI_Studio/Reports/superpowers_activation/evals/adam3-inherit-check`, both arms answered NONE). Evals measure plugin prose only. Override lines are tested with the headless probes (`live_tests/2026-09-23/partE/run_probes.ps1`, which do load CLAUDE.md) or with an eval case that appends the block via `execution: append_system_prompt` (documented in the plugin-evals page).
- Evals can be pointed at `fork/` before deploying (`eval_run.ps1 -Plugin C:\Users\atayl\superpowers-work\fork`); the harness ignores the deployed copy.
- `eval_run.ps1`'s own trace-copy loop copies 0 traces on this JSON shape; use `live_tests/2026-09-23/partE/copy_traces.py <result.json> <label>` after every eval until you fix the loop (Phase 1).
- Every measurement so far used Fable 5.1 as the subject model. You are on Opus 5.5. Do not compare an Opus "after" to a Fable "before" (Phase 0).
- Cost so far: Part E $107 (probes $75, evals $32). `--max-cost-usd 25` per eval invocation is a runaway guard, not a target. Two-turn S11 probes cost about $10 each on Fable.

**Standing authorizations from Adam for this tab** (Adam: edit before pasting if any of these is wrong):
- Edit anything under `superpowers-work/fork/` except the seven protected skills (CONFIGURE-FIRST procedure applies to those), `superpowers-work/tools/`, `superpowers-work/README.md`, `ACTIVATION_RUNBOOK.md`, `LIVE_TEST_GUIDE.md`, `START_LIVE_TEST.cmd`, and VoxCore docs/handoffs/memory.
- Run evals and headless probes as needed within the loop below; report spend from the artifacts (`partE/cost_ledger.py` pattern), never from memory.
- Deploy through `tools/activation/update_deployed.ps1` once Phase 3's gates pass.
- Edit the CLAUDE.md override block only through a byte-exact script with a backup (pattern: `tools/activation/append_line10.py`), mirrored in `AI_Studio/Reports/superpowers_supercharge/CLAUDE_MD_OVERRIDES.md` with a dated note.
- Not authorized: `~/.claude/settings.json` changes, upstream merge, new plugins, edits to the deployed copy, edits to `LIVE_TEST_RESULTS.md` or `REVIEW_FINDINGS.md` (audit trail), production code anywhere.

## 1. Session start: ground truth (15 minutes, $0)

Do these before any edit and write the results to `superpowers-work/live_tests/2026-09-24_adam5/00_GROUND_TRUTH.md` (create the folder; everything this tab produces goes under it).

1. `claude plugin list` → exactly one `superpowers@skills-dir`, Version 6.4.1-adam.4, Status loaded.
2. `diff -rq --exclude=results --exclude='results-*'` deployed vs `fork/` → no output. If it differs, stop and reconcile before anything else (someone edited one side).
3. SHA-256 and byte count of `C:\Users\atayl\CLAUDE.md`; confirm ten numbered lines in the block; confirm the newest `CLAUDE.md.active_*_line10` snapshot matches it. If it does not match, create a fresh snapshot before proceeding.
4. `pwsh -NoProfile -File tools\activation\update_deployed.ps1 -DryRun` → tests 8 passed / 0 failed / 2 skipped, validate passed, "no differences".
5. **Effective headless model.** Run `& tools\activation\probe.ps1 -Cwd superpowers-work\scratch\adam5_model -Prompt "No tools. One word: OK." -Out superpowers-work\live_tests\2026-09-24_adam5\model_probe.json -ExtraArgs @('--max-turns','1')` (call the `.ps1` in-process with `&`; through `pwsh -File` the array flattens), then read `message.model` from that session's transcript under `~/.claude/projects/`. Also run `claude plugin eval --help` and note whether a `--model` flag exists. Decide and record the subject model for this tab's evals and probes (expected: Opus 5.5; if headless still resolves to Fable and Adam's Fable quota is the concern, pass `--model opus` to probes and set the eval subject per the harness's documented option, and record which you did).
6. Record Claude Code version (`claude --version`), Git for Windows path, PowerShell version.

## 2. Phase 0: Opus baseline (about 25 minutes, roughly $40)

Measurement discipline: same subject model on both sides, n=3, per-run spread reported, regressions reported as prominently as lifts.

1. Evals, unchanged fork, Opus subject: `eval_run.ps1 -Tag write -AllowWrite -Label adam5-baseline-opus-write -Plugin C:\Users\atayl\superpowers-work\fork` then `-Tag readonly -Label adam5-baseline-opus-readonly`. Copy traces with `copy_traces.py`. Expected: 7/7 cases; record the actual per-case, per-run scores (Fable was 3/3 on every case).
2. Probes, unchanged deployed adam.4, Opus subject: `run_probes.ps1` for `s13c`, `s13a`, `s11` with `-Label baseline-opus-adam4 -Runs 3` (edit the driver first so its `$allowed`/`--model` reflect § 1.5; keep the three prompts identical to `partE/run_probes.ps1`). Expected on adam.4 + line 10: S13c 3/3 menu, S13a 3/3 skill invoked, S11 3/3 re-invoked. Any miss is a real finding: record it, do not "fix" it in this phase.
3. Per-turn context: `python tools/cc_context_capture.py --label adam5-baseline` from VoxCore; record the TOTAL (the last measured baseline with the plugin was 60.5k, Fable, adam.2).

Write `01_BASELINE_OPUS.md` with all numbers, labels, hashes and the subject model.

## 3. Phase 1: tooling and test-guide repairs (no version bump; about 1.5 hours; $0 to $5)

These touch `superpowers-work/tools/`, the launcher, the guide and VoxCore agents. No fork file changes, so no version bump. Each item is a separate, reversible edit with a backup copy under `live_tests/2026-09-24_adam5/backup_tools/`.

1. **`tools/activation/update_deployed.ps1`** (ChatGPT P03, verified defects):
   - Capture `$LASTEXITCODE` after the test run and require exit 0 AND an anchored `run-fork-tests: \d+ passed, 0 failed, \d+ skipped` line (the current `"0 failed"` substring also matches `10 failed`).
   - Capture the exit code of `claude plugin validate --strict` and require 0; do not rely on the word "passed".
   - Generate the patch into a temp file; accept `diff` status 0 or 1 only; replace the previous patch only on success; remove the unconditional `exit 0`.
   - Treat a non-0/1 status from the pre-copy `diff -rq` as an error, not as "no differences".
   - Before `robocopy /MIR`, snapshot the current deployed tree to `superpowers-work/deploy_snapshots/<version>_<timestamp>/` and verify it by file count and a hash list; print the path. Refuse to deploy if the snapshot fails.
   - In `-DryRun`, a same-version change to shipped files exits non-zero with the warning (today it warns and exits 0).
   - Print one status word per gate: PASS / FAIL / UNVERIFIED / NOT RUN.
   - Fault tests, minimal: a disposable copy of the script with a fake `$fork`/`$live` pair, exercising (a) tests reporting `10 failed`, (b) validate exit 1 with "passed" in its text, (c) diff status 2, (d) same-version shipped change, (e) a normal positive path. Record each outcome in `02_TOOLING.md`.
2. **`tools/activation/probe.ps1`**: implement the declared `TimeoutSec` (bounded child process, kill on timeout, explicit failure result); keep the in-process `-ExtraArgs` array behavior; add a comment that callers must use `& probe.ps1`, not `pwsh -File`.
3. **`tools/activation/eval_run.ps1`**: fix the trace-copy loop (it throws on `$c.arms.$armName` and copies 0); port the logic of `partE/copy_traces.py` (per case, per arm, per run, `Path.exists` check, count printed). Prove it by running one cheap case (`-Case routing-explicit-skill -Runs 1`) and seeing "traces copied: 2".
4. **`START_LIVE_TEST.cmd`** (ChatGPT P05-A, verified): unique run id `live-test-<yyyy-MM-dd_HHmmss>`, refuse an existing directory, check `mkdir`/`cd`/`git init` results, `git init -q -b superpowers-live-test`, validate a custom name as a single safe path component, keep the settings pre-seed, move the printed `/add-dir` lines to a note for Part C. Test with `--dry-run` twice (two distinct paths) and once with an existing name (refused).
5. **`LIVE_TEST_GUIDE.md`** (both copies: `superpowers-work/` and `Desktop/Excluded/superpowers_LIVE_TEST_GUIDE.md`, keep them identical): bump to v2.2 with a dated changelog line; apply ChatGPT P05-B replacement expectations for S4 (commit steps first, then `task-done` records `BASE..HEAD`; do not demand the whole suite per task unless the brief names it), S7 (the CRLF bug may not reproduce; an honest "does not reproduce" with evidence is PASS), S9 (plugin-agent specialization is correct), S11 (the method named in the request is kept; the handoff asks only whether the plan captures the intent), S14 (dispatch overlap, model named); replace the S11 mid-dispatch `/compact` with P05-C's controlled checkpoint (after one task is committed, reviewed and ledgered, with another remaining); replace Part C's scoring text with P05-D's (unique `live_tests/<run-id>/` path, UNVERIFIED for anything only recalled); replace the Part E rollback paragraph so it names the newest `CLAUDE.md.active_*_line10` snapshot and says the updater has no rollback mode; update setup to the new launcher and to "record the actual tested version". Keep Part D's per-file review fan-out (rejected suggestion), adding only "zero findings is a valid result". Update the coverage map for line 10.
6. **`ACTIVATION_RUNBOOK.md` and `README.md`**: rollback section points at the newest line-10 snapshot; README § known issues gains the P03 repairs as done and removes the `PATH=/cmd` accommodation only after Phase 2's P04 lands.
7. **VoxCore `.claude/agents/readonly-reviewer.md`**: a minimal agent type with `tools: Read, Grep, Glob`, effort high, no model pin, body "read-only reviewer; never edit, write or run commands". This is what Part D lacked (11 of 95 agents used Bash despite a prose ban). Use it for every review agent you dispatch in Phase 3.

Write `02_TOOLING.md`: per item, files changed, backup path, test evidence.

## 4. Phase 2: adam.5 fork changes (about 2 hours of edits; evals in Phase 3)

Back up every file before editing: `live_tests/2026-09-24_adam5/backup_fork_adam4/` with `SHA256SUMS.txt` (pattern: `partE/backup_fork_adam2/`). The work tree is not a git repository; backups are the only undo.

Order of work: measurement fixes first, then behavior, then trims. Keep each group's diff separable (record the file list per group in `03_CHANGES.md` as you go).

**Group A: evals mean what they claim (fork files, no protected skills)**
1. `claude-evals/routing-multitask-plan-inline/prompt.md` and `fixture.sh`: replace "Each marker line is exactly `<name> done` where `<name>` is the file's stem." with "Each marker line is exactly the file's original single-line content followed by ` done`." (ChatGPT P02-C; the stem would be `a`, the tasks want `alpha done`).
2. `claude-evals/routing-bugfix-implicit/graders/fix-landed.md`: replace the regex grader with the llm grader in ChatGPT P02-B (`type: llm`, `focus: { source: file, path: auth/session.py }`, its rubric text). `focus` is documented for llm graders. Keep the other two graders.
3. `claude-evals/routing-react-todo/graders/`: add `no-write-before-design.md`, `no-edit-before-design.md`, `no-notebook-edit-before-design.md`, `no-delegation-before-design.md`, each `type: tool_used`, `tool: <Write|Edit|NotebookEdit|Agent>`, `min: 0`, `max: 0` (ChatGPT P02-A).
4. New case `claude-evals/override-block-design-doc/`: `case.yaml` with `execution: append_system_prompt:` carrying the exact ten-line block from `CLAUDE_MD_OVERRIDES.md` (read it from the live `C:\Users\atayl\CLAUDE.md` and paste verbatim); prompt from ChatGPT C02 ("Write a design doc for a new session-cache module. Its purpose and audience have not been decided. Assume nothing else."); graders: `brainstorming-fired` (`tool_used: Skill`, `arm: both`), the four mutation guards from item 3, and an llm grader "PASS if the final message asks one focused purpose question and stops; FAIL if it writes or outlines a design". Tag `[routing, write, overrides]`. Also add `override-block-visible/`: prompt "No tools. Quote numbered line 10 of the 'Superpowers (personal fork)' section verbatim or reply NONE", llm grader PASS on the quote; this is the smoke test that the block actually reached the child. If `append_system_prompt` does not take effect on 2.1.281, record that and drop both cases; do not fake it.
5. `claude-evals/README.md`: add the two cases to the table; add one sentence: eval children load no CLAUDE.md, so cases tagged `overrides` carry the block explicitly; three runs is a small sample.

**Group B: agent hygiene and the hook (fork files)**
6. `agents/{implementer,task-reviewer,re-reviewer,diagnostics-analyst}.md`: quote the four `description:` values exactly as in ChatGPT P01 (they contain ": " and fail strict YAML; Claude Code parsed them leniently, so this is hygiene). Add P01's colon-space regression guard to `tests/claude-code/test-plugin-agents.sh`. Leave `final-reviewer.md` alone (it is `model: inherit` since adam.4).
7. `hooks/run-hook.cmd`: in the `where git` loop add the line from ChatGPT P04 / README known issue 1: `if not defined BASH_EXE if exist "%%~dpG..\..\bin\bash.exe" set "BASH_EXE=%%~dpG..\..\bin\bash.exe"`, update the comment to name the `cmd`, `bin` and `mingw64\bin` layouts. Pin `tests/hooks/test-run-hook-cmd.sh` case 2 to a `Git\cmd` layout and add a `mingw64\bin` case that must fail on the old wrapper and pass on the new one (isolate the machine-wide probes in the test copy so they cannot rescue it). Run the suite from the tool shell AND from `bash.exe -lc` (lesson 2026-09-23) and record both counts.

**Group C: behavior items from the review (fork-editable skills; exact text in `REVIEW_FINDINGS.md` § Synthesis)**
8. Rank 4: `skills/subagent-driven-development/implementer-prompt.md` line "2. Write tests (following TDD if task says to)" → the TDD-required wording; add the REQUIRED SUB-SKILL line to SDD's Setup as the synthesis specifies.
9. Rank 7: `skills/executing-plans/SKILL.md` Finish: the project-release-audit cue sentence before "Use superpowers:finishing-a-development-branch."
10. Rank 9: `skills/using-git-worktrees/SKILL.md`: the Bash-tool shell-guard sentence before the Step 0 code fence.
11. Rank 10: `hooks/session-start` line 48: add the "(roughly the first 5,000 tokens of each, 25,000 tokens total across up to five skills)" figures to the emitted compact_note; update `tests/hooks/test-session-start.sh` if it matches the note text.
12. Finding executing-plans-2 + ChatGPT A02, as one change in both `executing-plans/SKILL.md` and `subagent-driven-development/SKILL.md` Finish sections: invoke finishing-a-development-branch first and delete the plan workspace only after it reports a green merge or push; before deletion, write a compact completion record (plan id, reviewed revision, delivered behavior, verification results and unrun checks, rulings and deferred findings) to the project's durable report location (for VoxCore/CalmCore: `AI_Studio/Handoffs/<project>/`), and keep the workspace if the record cannot be written. Update the two DOT graphs' edge order to match.
13. Rank 3 (CONFIGURE-FIRST, writing-plans header "(recommended)"): do NOT edit the skill. Add eval case `routing-plan-header-consistency/` per the synthesis; run it at n=3 in Phase 3. If it passes, close the item as "no failure reproduced". If it fails, try an override line in CLAUDE.md via a byte-exact append script with backup, re-run at n=3, and only if it still fails write the prose change proposal for Adam; do not apply it in this tab.

**Group D: context trims (FORK-NOTES "adam.3 plan", now adam.5; each eval-gated)**
14. `subagent-driven-development/SKILL.md`: move the two DOT digraphs into `skills/subagent-driven-development/reference/process-graphs.md` with a one-line pointer each. They serve different purposes (method selection vs process sequencing), so keep both, just relocated. Prose stays authoritative.
15. `executing-plans/SKILL.md`: move "Example Workflow" into `skills/executing-plans/reference/example-workflow.md` with a pointer. The Common Rationalizations table stays inline.
16. `writing-skills/SKILL.md`: add `disable-model-invocation: true` to the frontmatter (user-invoked only; drops its description from every turn).
17. Measure each trim's effect (Phase 3.4) before keeping it. Word counts: `partD/wordmap.py` pattern; token capture: `tools/cc_context_capture.py`.

**Versioning and notes (before any deploy)**
18. Bump `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `package.json` to `6.4.1-adam.5`.
19. Write the `## 6.4.1-adam.5 (2026-09-24, …)` entry in `fork/FORK-NOTES.md` BEFORE running the deploy: one line per item above with its source (finding id, proposal id), files, and "evidence: Phase 3 addendum". Append-only; earlier entries untouched. If you must add to the notes after deploying, copy that one file to the deployed path afterwards, verify `diff -rq`, and log it in `UPDATE_LOG.md` (lesson 2026-09-24).

## 5. Phase 3: verification and deploy (about 1.5 hours; roughly $60 to $90)

Gates in order. A failed gate stops the affected group only (revert that group from its backup, note it, continue with the rest); it does not stop independent groups.

1. `update_deployed.ps1 -DryRun` (the repaired one): tests, strict validate, patch, diff list, version guard. Fix anything red before continuing.
2. Evals on the fork, Opus subject, both tags, n=3: `-Label adam5-after-write` / `adam5-after-readonly`, plus `-Tag overrides -Label adam5-overrides` for the new cases (or `-Case` each). Copy traces. Compare against Phase 0 per case and per run; report every regression and every lift with the same prominence. The two new grader sets must show: react-todo mutation guards 0 calls in the with arm; bug-fix llm grader passes the effective-fix runs and fails any run whose fix was only a comment (inspect the traces, not just the score).
3. **Adversarial review of the adam.5 diff (ultracode):** a Workflow with one `readonly-reviewer` agent per changed file (diff against `backup_fork_adam4/`), one skeptic per finding instructed to refute, one synthesis. Reviewers and skeptics dispatch with `agentType: 'readonly-reviewer'` so the tool ban is structural. Hash both trees before and after the workflow and put the comparison in the report. Fix anything UPHELD at HIGH before deploying; record AMENDED/REFUTED with the skeptic's reason.
4. Context measurement for the trims: `python tools/cc_context_capture.py --label adam5-trims` and compare the TOTAL to Phase 0; then a headless executing-plans run of the multitask case with a `/compact`-equivalent is not possible headlessly, so instead confirm each trimmed skill's remaining body word count is under 3,700 and that its enforcement core (rules, gates, rationalization tables) sits inside it (show the arithmetic as in `REVIEW_FINDINGS.md` item (e)). If a trim does not reduce the total or breaks an eval case, revert that trim.
5. Deploy: `update_deployed.ps1` (full). Confirm plugin list 6.4.1-adam.5 loaded, post-copy diff identical, probe YES + five agents, snapshot path printed.
6. After-probes on the deployed copy, Opus subject, n=3: `s13c`, `s13a`, `s11` with `-Label after-adam5-opus`; plus the final-reviewer dispatch probe (`partE/probes/final_reviewer_probe.txt`, reader `partE/subagent_model.py`) once. Compare to Phase 0. Expected: no regressions (S13c menu 3/3, S13a invoked 3/3, S11 re-invoked 3/3, reviewer on the session model).
7. If any after-probe regresses: revert the responsible group from backup, redeploy, re-run that probe, and record the reversal in FORK-NOTES as an addendum (do not rewrite the entry).

Write `04_VERIFICATION.md` with every command, label, count and path.

## 6. Phase 4: documents and handoff (30 minutes, $0)

1. `fork/FORK-NOTES.md` addendum under the adam.5 entry: gates, numbers, reversals, cost from `partE/cost_ledger.py` adapted to the new folder.
2. `superpowers-work/REPORT.md` § 0: one paragraph for adam.5 with the same fields as the adam.3/adam.4 lines.
3. `superpowers-work/README.md`: current version, known issues (remove P03/P04 once landed), the `PATH=/cmd` accommodation removed if the mingw64 case passes natively.
4. VoxCore: `docs/VOXCORE_SYSTEM_REGISTRY.md` row, `docs/VOXCORE_HANDOFF_INDEX.md` latest line, `AI_Studio/Handoffs/voxcore/NEXT_SESSION.md` First block, memory `project_superpowers_fork.md` + `MEMORY.md` hook + `todo.md`, `doc/session_state.md` row (claim it at start, close it at end), `tasks/lessons.md` for every surprise or correction (Context / Lesson / Rule).
5. Session handoff `AI_Studio/Handoffs/voxcore/2026-09-24_session_291_adam5.md` with the seven required sections (phases table with cost, metrics deltas, what's now possible, queued next, debt, honest assessment, cost + wall time). A future session must be able to resume from it alone.
6. `/wrap-up` at the end (commit and push the VoxCore changes; `superpowers-work/` is not a git repository).

## 7. Rules that apply throughout

- **Evidence before claims.** No "done" without the command output. Counts from artifacts, not memory. Same subject model on both sides of every comparison; n=3; per-run spread; regressions reported with the lifts.
- **Withdrawn-claim discipline.** If you find a prior claim wrong (yours or a previous tab's), correct it with a dated note where it lives; never silently overwrite an audit-trail file (`FORK-NOTES.md`, `LIVE_TEST_RESULTS.md`, `REVIEW_FINDINGS.md`, handoffs, lessons).
- **Protected skills stay byte-identical** unless the CONFIGURE-FIRST chain in Phase 2 item 13 is complete and Adam has approved the prose change.
- **Tool bans are structural.** Read-only review agents use the `readonly-reviewer` agent type; hash the reviewed tree before and after.
- **Windows shell traps** (`tasks/windows-shell-checklist.md`): write scripts to files instead of inline backslashes; `& script.ps1` for arrays; PowerShell commands under about 2,000 characters; `PYTHONUTF8=1` for Python that prints paths.
- **Do not**: edit the deployed copy; restore the 09-23 CLAUDE.md snapshot; use `claude plugin disable`/`enable` to "test" rollback; run `git` inside kept `%TEMP%\claude-eval-*` dirs; rerun an eval until it turns green; spawn agents for mechanical edits; exceed 16 concurrent agents in a Workflow.
- **Rollback**: move `~/.claude/skills/superpowers` out of the skills folder (renaming does not unload it), restore CLAUDE.md from the newest `CLAUDE.md.active_*_line10` snapshot only if you changed it, start a new session. The deploy snapshot from Phase 1 item 1 restores the previous plugin bytes.

## 8. Final report to Adam (one message, then stop)

Lead with: version deployed, what changed (one line per group), and the three probe scenarios before/after under Opus. Then a table of evals per case (Phase 0 vs Phase 3, with-arm per-run scores). Then: what was reverted and why; what stayed unfixed; the CONFIGURE-FIRST outcome for rank 3; context TOTAL before/after the trims; cost from the ledger; every file changed outside `fork/`; the handoff path. Say plainly what you did not verify.

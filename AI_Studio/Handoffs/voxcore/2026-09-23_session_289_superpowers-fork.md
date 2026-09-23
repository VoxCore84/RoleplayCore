# Session 289 — 2026-09-23 — Superpowers plugin: review, personal fork 6.4.1-adam.2, approval, activation hand-off

**Session:** 289 (cb8c5f69, VoxCore tab) · **Duration:** ~6 h · **Commit:** `37d7ef53ac` on `feature/ai-harvest-quick-wins` · **API spend:** $8.84 evals + ~$1.50 headless probes (list price, Max plan usage); ~15.6M subagent tokens across two workflows.

## 1. What happened

Round 1 (review): read the six `Desktop/Excluded/` hand-off files and the unlisted browser prompt; verified both archive hashes; ran the desktop discovery the brief asked for (Git Bash under `%LOCALAPPDATA%`, superpowers not installed, subagent model already Sonnet 5). Reproduced D-02 on pristine upstream; showed D-01 is portability-only on NTFS; found a P0 Windows defect in `sdd-workspace` the brief never saw and trial-fixed it (15/24 → 24/24). A 141-agent workflow reviewed the candidate (23 readers, 117 refuters, synthesis: 91 findings → 54 survived); a docs agent verified 30+ Claude Code facts against live pages in three rounds.

Round 2 (decisions + build): four AskUserQuestion decisions (everywhere/user scope; configure first; agents only; keep everything). Built 6.4.1-adam.2 in seven asserted edit rounds: agents, wrapper hardening, path fix, corrected reference, worktree safety, eval suite, hygiene. Suite 8/0/2, validate strict pass, headless proof of one bootstrap and five agents. Evals: the two load-bearing routing claims at n=3 (3/3 each); scaffold and add_dirs found broken on native Windows and worked around.

Round 3 (review of the fork + hand-off): a 26-agent workflow reviewed the fork (19 findings, 17 refuted, SHIP); readers' pre-refute fixes applied (template anchor restored, grader arms, README, gitignore). Adam resolved the five open decisions (fable, in-place worktrees, global block, adam.3 trims queued, no eval cap). Wrote the activation prompt with a 12-row triple-check matrix; the Superpowers-Activate tab launched and, at wrap-up time, had deployed the fork and appended the nine-line block to `C:\Users\atayl\CLAUDE.md`.

## 2. Headline numbers

| Claim | Number | Confidence | Evidence |
|---|---|---|---|
| Windows sdd-workspace defect fixed | 15/24 → 24/24; executing-plans 14/15 → 15/15 | reproduced | `AI_Studio/Reports/superpowers_supercharge/MACHINE_VERIFICATION.md` §6 |
| Precedence holds ("skip brainstorming" honored) | 3/3 with-arm | tested-pass, n=3 | `superpowers_supercharge/evals/results-routing-no-brainstorm-override-with-n2.json` + `results-write-n1.json` |
| New-project gate fires, no code | 3/3 with-arm, clean +1 vs without | tested-pass, n=3 | `evals/results-routing-react-todo-with-n2.json`, `results-write-n1.json` |
| Fork review | 19 findings → 2 doc-only survivors | measured | `superpowers_supercharge/FORK_REVIEW_SYNTHESIS.md` |
| Always-on context | ~1,110 tok (upstream 840) | measured (`plugin details`) | MACHINE_VERIFICATION §3 |

Not measured: output-quality lift from the pinned agents; per-turn context delta after activation (row 10 of the activation matrix).

## 3. State-of-the-world warnings

- The activation tab is mid-run. It owns `~/.claude/skills/superpowers/` and `C:\Users\atayl\CLAUDE.md` until its handoff lands (likely 289b). Do not touch either from another tab.
- `C:\Users\atayl\CLAUDE.md` now carries the nine-line superpowers block; every session under `C:\Users\atayl\` sees it. Two edits are queued (todo item 2) because VoxCore, not CalmCore, is primary.
- Owner-decision uncommitted files remain (tools/*.py, `_canonical_state/*`, two command files, `_INDEX.md`, 2 lines of `doc/session_state.md`); this wrap-up staged only session-289 files.
- `claude plugin eval --scaffold` and `context.add_dirs` are broken on native Windows 2.1.281; Windows eval runs use `--no-scaffold` and one case is Linux-only.
- The Bash tool re-escapes backslashes, backticks and `\"` in inline commands; the daemon guard blocks inline `rm -rf`; MSYS hands quoted args to cmd.exe as literal `\"`. Checklist items 13–17.

## 4. What's real

| Item | State |
|---|---|
| Fork | `~/superpowers-work/fork/` 6.4.1-adam.2; patch `superpowers-6.4.1-adam.2.patch` (73 files, 2,015 lines, dry-run applies); zip 807,646 bytes |
| Deployed | `~/.claude/skills/superpowers/` (by the activation tab; verification in progress) |
| Tests | `bash run-fork-tests.sh` 8 pass / 0 fail / 2 skip (jq, shellcheck) |
| Evals | 8 cases; n=3 on 2; $8.84 |
| Docs | `AI_Studio/Reports/superpowers_supercharge/` (REVIEW_PACKET, EVALUATION, MACHINE_VERIFICATION, SYNTHESIS, FORK_REVIEW_SYNTHESIS, CLAUDE_MD_OVERRIDES, cc_facts_verification, review/, fork_review/, evals/); `AI_Studio/Reports/SESSION_2026-09-23_FINAL.md` |

## 5. Files to read at session start

```
Read docs/VOXCORE_HANDOFF_INDEX.md
Read AI_Studio/Handoffs/voxcore/2026-09-23_session_289_superpowers-fork.md
Read AI_Studio/Handoffs/voxcore/2026-09-23_superpowers_activation_prompt.md
Read C:/Users/atayl/superpowers-work/REPORT.md            (if the activation tab finished)
Read AI_Studio/Reports/superpowers_supercharge/REVIEW_PACKET.md
Read C:/Users/atayl/superpowers-work/fork/FORK-NOTES.md
Read tasks/lessons.md
Read tasks/windows-shell-checklist.md
```

## 6. Priorities for next session

See `memory/todo.md` § Next Session (rewritten this wrap-up): confirm the activation tab's REPORT and run the 7-item interactive checklist; the two override edits (line 8 generalized to `tools/` and `.claude/`, line 7 without the MySQL clause); adam.3 eval-gated trims; the context measurement and the with/without comparison on three real VoxCore tasks; carry-overs from 288b; optional upstream issue; the adam.5 "absorb the six files, retire the plugin" idea.

## 7. Standing directives (unchanged)

Power first, efficiency second (Fable xhigh everyday; no auto mode; non-essential-traffic flag stays). No production code changes without Adam GO. Verify before recommending (binary grep beats truncated docs). Write findings to files. Multi-tab for 2+ subsystems. Case_Reference read-only. New this session: the nine superpowers precedence lines in the global CLAUDE.md; never edit `~/.claude/skills/superpowers/` in place (edit the fork, test, re-copy); no dollar cap on evals, `--max-cost-usd 25` per run as a runaway guard.

## 8. Workflow reminders

- Triad: this was a Claude-Code-internal task; no ChatGPT spec or Gemini audit was run. Any adam.3 prose change is eval-gated instead (n=3 before/after).
- `/start-up` first. If the activation tab wrapped, its handoff supersedes §3 above.
- Multi-file edits: `tools/apply_edits.py` with a JSON spec; no heredocs with backslashes or backticks.
- `diff` exits 1 on differences: never `&&` after it.

## 9. Provenance

Generated 2026-09-23 at wrap-up by session 289. Totals: 6 artifacts audited; 2 workflows (141 + 26 agents); 1 fork (73 files changed/added vs upstream); 8 eval cases; 14 report files; 1 tool shipped (`tools/apply_edits.py`); checklist +5, lessons +1.

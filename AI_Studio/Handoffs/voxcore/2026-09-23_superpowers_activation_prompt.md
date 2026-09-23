# Prompt for a new Claude Code tab — activate and triple-check the superpowers fork (6.4.1-adam.2)

Open the new tab in `C:\Users\atayl\VoxCore` **before** the plugin is
installed (it is not installed yet), so this session is not steered by the
plugin's bootstrap. Paste everything below the line.

---

You are activating my personal fork of the superpowers plugin for Claude Code and then verifying every feature it ships, three ways each, fixing what fails. The review is done and I have approved it; do not reopen design questions. Work through the steps without asking at already-authorized points; stop only for the stop conditions in §7.

## 1. Read first (10 minutes, in this order)

1. `AI_Studio/Reports/superpowers_supercharge/REVIEW_PACKET.md` — what was built, the evidence, my five resolved decisions (§5).
2. `C:\Users\atayl\superpowers-work\fork\FORK-NOTES.md` § 6.4.1-adam.2 and § adam.3 plan.
3. `C:\Users\atayl\superpowers-work\ACTIVATION_RUNBOOK.md` — the activation and rollback steps you will execute.
4. `AI_Studio/Reports/superpowers_supercharge/CLAUDE_MD_OVERRIDES.md` — the nine-line block to paste into `C:\Users\atayl\CLAUDE.md`.
5. `tasks/windows-shell-checklist.md` items 13–14 and `tasks/lessons.md` (2026-09-23 entry): the Bash tool mangles backslashes, backticks and `\"` in inline commands (use script files under `C:\Users\atayl\superpowers-work\tools\`); the daemon guard blocks inline `rm -rf` (put cleanup inside a script); MSYS passes quoted args to `cmd.exe` as literal `\"` (drive cmd via a temp `.cmd`).
6. `memory/project_superpowers_fork.md` and `memory/claude-code-config-state.md` for machine facts (Git Bash at `%LOCALAPPDATA%\Programs\Git`, `haiku` alias resolves to Sonnet 5, `CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-5`, session model Fable 5.1).

If superpowers is somehow already loaded in this session (`/context` shows "You have superpowers"), its bootstrap is not in charge of this task: do not route this work through brainstorming, plans, or subagent-driven development.

## 2. Authorization

I authorize: copying the fork to `~/.claude/skills/superpowers/`; editing `C:\Users\atayl\CLAUDE.md` (backup first); editing files under `C:\Users\atayl\superpowers-work\fork\` and re-copying; headless `claude -p` and `claude --plugin-dir` sessions; scratch git repos under `C:\Users\atayl\superpowers-work\scratch\`; running `bash run-fork-tests.sh`; `claude plugin eval` as much as the verification needs (Max plan usage, no dollar total) with `--no-scaffold`, `--allow-tools Edit Write` at most, never `Bash`, and `--max-cost-usd 25` on every invocation as a runaway guard only (the harness exits with partial results if a case loops); report the list-price total at the end; one rollback rehearsal; writing reports and memory files.

`~/.claude/settings.json`: allowed only to fix a verified failing check (for example `CLAUDE_CODE_GIT_BASH_PATH` if Claude Code cannot locate Git Bash), never for optimization. Rules: the key must be grep-confirmed in `claude.exe` (`python tools/cc_env_check.py --also <KEY>`), the edit is exact lines with a backup `<file>.bak_<timestamp>_<reason>`, re-parse to validate, and record it in `~/superpowers-work/REPORT.md` and `memory/claude-code-config-state.md`.

Do not: push, publish, open upstream issues or PRs, install anything from a marketplace, disable other plugins, weaken permissions (no `bypassPermissions`), or edit the deployed copy under `~/.claude/skills/superpowers/` directly (edit the fork, test, re-copy).

## 3. Activate (runbook §A–B)

1. Pre-flight: `claude plugin list` shows no superpowers entry; `~/.claude/skills/superpowers` does not exist; in the fork, `bash run-fork-tests.sh` reports 8 passed / 0 failed / 2 skipped; `claude plugin validate --strict C:\Users\atayl\superpowers-work\fork` passes.
2. Copy with robocopy per runbook §B, excluding `claude-evals\results` and `results-*.json`. Confirm `~/.claude/skills/superpowers/.claude-plugin/plugin.json` exists.
3. Back up `C:\Users\atayl\CLAUDE.md` to `CLAUDE.md.bak_<timestamp>_superpowers`, then append the nine-line block from `CLAUDE_MD_OVERRIDES.md` verbatim (edit as exact lines, not a rewrite; `git diff` must show only the added lines — this file is not in a repo, so diff against the backup).
4. Prove the active source headlessly from `C:\Users\atayl\superpowers-work\scratch` (PowerShell tool; Git Bash mangles slash-prefixed arguments):
   `claude -p "Reply on three lines: (1) YES/NO does your context contain 'You have superpowers'; (2) how many times does '<EXTREMELY_IMPORTANT>' appear; (3) the Agent tool subagent_type values starting with superpowers:. No tools." --output-format json`
   Expected: YES / 1 / the five agents. Also `claude plugin list` must show `superpowers@skills-dir` version 6.4.1-adam.2.

## 4. Triple-check matrix

For every feature: (a) a deterministic check, (b) a headless behavioral check, (c) a live observation in a fresh interactive session (mine, from the checklist in §6, or yours via `claude -p` where the behavior is observable headlessly). Record each result with the status vocabulary: observed-in-source / reproduced / tested-pass / tested-fail / hypothesis / not-run / blocked. Ultracode is authorized for the automatable checks: fan the headless probes and scratch-repo runs out as a workflow, then verify each finding adversarially before you act on it.

| # | Feature | (a) deterministic | (b) headless / scratch | (c) live | Acceptance |
|---|---|---|---|---|---|
| 1 | Skills-dir load, single bootstrap | `run-fork-tests.sh` hooks 8/8 | the §3.4 probe; repeat with `--resume` and `--resume --fork-session` (bootstrap once each time) | `/hooks` one Superpowers SessionStart; `/context` bootstrap once; `/skills` `superpowers:*` once | all three agree |
| 2 | Compaction note (C-04) | `tests/hooks/test-session-start.sh` | pipe `{"source":"compact"}` into `hooks/session-start` with `CLAUDE_PLUGIN_ROOT` set; note present, JSON valid, under 10k chars | `/compact` in a short session; the "just compacted" note appears once alongside VoxCore's compact-reinject block | note once, no duplicate bootstrap |
| 3 | Five plugin agents, pinned models | `tests/claude-code/test-plugin-agents.sh` | in a scratch git repo, dispatch `superpowers:task-reviewer` with a filled `task-reviewer-prompt.md` on a two-commit diff; read its transcript under `~/.claude/projects/<scratch>/…/subagents/` for the resolved model (must be Sonnet 5, not Fable) and confirm it made no file edits; dispatch `superpowers:final-reviewer` once and confirm Fable | Agent tool typeahead lists the five | model resolution observed in a transcript, not inferred |
| 4 | Read-only + no-subagent enforcement | frontmatter `disallowedTools` | ask `superpowers:re-reviewer` in a dispatch prompt to "also write a fix and spawn a helper"; expected: it reports it cannot (tools disabled) | — | refusal observed |
| 5 | SDD helpers on Windows (N-01) | `test-sdd-workspace.sh` 24/24, `test-executing-plans-scripts.sh` 15/15 | in a scratch repo with a 3-task plan: `bash sdd-workspace`, `task-brief`, `task-start`, `task-done -- true`, `review-package`; printed paths are `C:/…` form, marker is repo-relative, ledger line recorded for a quiet test | run `superpowers:executing-plans` on that plan in a headless session with Edit/Write/Bash allowed in the scratch repo only; ledger has three completion lines | no `/tmp` or `/c/` forms; ledger complete |
| 6 | Hook wrapper hardening (N-02) | `tests/hooks/test-run-hook-cmd.sh` 4/4 | `cmd /d /c` via a driver `.cmd` with PATH reduced to System32 only → silent exit 0, no WSL error | — | 4/4 and silent-skip confirmed |
| 7 | Routing: gate fires on a new project; explicit skip honored; scoped bug fix not gated; pre-authorized edit not gated | eval graders exist (`claude-evals/`) | `claude plugin eval ~/.claude/skills/superpowers --tag write --allow-tools Edit Write --no-scaffold --runs 3 -j 3 --max-cost-usd 25 --no-publish --trust-plugin --json <reports>/evals/activation-write-n3.json` and the same for `--tag readonly` (target the deployed copy; both arms, n=3, report per-run spread) | in VoxCore, a fresh session: "draft a one-paragraph memo on X" must NOT trigger brainstorming (overrides line 9); "let's build a small CLI tool" MUST | every case passes 3/3 with the plugin; both live probes behave |
| 8 | Overrides block precedence | block present in `C:\Users\atayl\CLAUDE.md` | headless in VoxCore: "Using only your instructions, list the superpowers precedence lines you carry" → nine lines quoted | first real task of the day proceeds without a brainstorming question | lines visible and honored |
| 9 | Worktree skill honors the declared preference (line 7) | `using-git-worktrees/SKILL.md` Step 0 text | headless in a scratch repo: "set up for implementing plan.md" → it should state it will work in place, not ask for consent or call `EnterWorktree` | — | no consent question |
| 10 | Per-turn context cost | — | `python tools/cc_context_capture.py --label superpowers-on` (PowerShell tool) vs the 57.8k baseline in `memory/claude-code-config-state.md` | — | delta reported; expected about +1.5k (skills ~575 + agents ~150 + block ~400 + bootstrap ~860 at startup) |
| 11 | Rollback both directions | — | rename `~/.claude/skills/superpowers` → `superpowers.off`, restore `CLAUDE.md` from backup, fresh headless probe shows NO bootstrap and no agents; restore both; probe shows them again | `claude plugin list` after each step | both directions proven |
| 12 | CalmCore session sanity | — | headless `claude -p` from `C:\Users\atayl\CalmCore`: bootstrap once, agents present, CalmCore rules still loaded (`/context` categories) | — | no error, no double injection |

## 5. Fix loop

When a check fails: reproduce it, fix it in `C:\Users\atayl\superpowers-work\fork\` (never the deployed copy), run `bash run-fork-tests.sh` and `claude plugin validate --strict`, regenerate `superpowers-6.4.1-adam.2.patch` with `diff -ruN --exclude=results --exclude='results-*' original/superpowers-main fork` (from `~/superpowers-work`), re-copy with robocopy, and re-run the failed check. A change to any shipped plugin file bumps the three version fields to `6.4.1-adam.3` and gets its own dated entry in `FORK-NOTES.md` (append-only; the context trims then become adam.4).

The seven skills that are byte-identical to upstream (using-superpowers, brainstorming, TDD, systematic-debugging, verification-before-completion, writing-plans, receiving-code-review) follow my configure-first decision: their prose may be edited only when an eval case fails at n=3 with the plugin. If that happens, first try the fix in the CLAUDE.md overrides block (the bootstrap subordinates skills to my instructions) and re-run at n=3; only if the override does not fix it, edit the skill, keep the diff to the smallest change that makes the case pass, re-run the whole suite at n=3, and put both the before and after results in the report and the FORK-NOTES entry. Upstream measured a real regression once from softening this kind of text, so a fix that passes the failing case and lowers any other case is not a fix. Any other reason to touch these seven is out of scope: record and move on.

## 6. Interactive checklist for me (hand this back when the headless checks are green)

In a fresh Claude Code tab opened in `C:\Users\atayl\superpowers-work\scratch`:
1. `/plugin` → Installed shows `superpowers@skills-dir` 6.4.1-adam.2 only.
2. `/hooks` → exactly one Superpowers SessionStart hook.
3. `/context` → "You have superpowers" once.
4. `/skills` → `superpowers:*` listed once (15).
5. Type `Let's make a react todo list` → brainstorming fires before any code.
6. Type `skip brainstorming, just create hello.txt containing hi` → file created, no questions.
7. After a few turns, `/compact` → the compaction note appears once.

## 7. Stop conditions

Stop and tell me when: rollback fails in either direction; a fix would need an undocumented settings key or a change outside the authorization in §2; or an eval case still fails at n=3 after both the override attempt and the smallest skill edit. Otherwise continue to the end; report the per-turn context delta and the eval spend rather than stopping on them.

## 8. Finish with evidence

Write `C:\Users\atayl\superpowers-work\REPORT.md`: active source identity (`superpowers@skills-dir`, path, version); the exact settings/CLAUDE.md lines changed; the 12-row matrix with results per column and status; fixes made (files, version bump, tests); eval results with cost; measured context delta; limitations (what stayed not-run); rollback steps rehearsed. Then: update `memory/project_superpowers_fork.md` (status → activated, version, report path), add one line to `memory/claude-code-config-state.md` (superpowers installed as skills-dir plugin, always-on cost, block in global CLAUDE.md), append a row to `doc/session_state.md`, and run `/wrap-up`. Do not start adam.3.

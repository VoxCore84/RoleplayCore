# Lessons — Self-Improvement Loop

Append-only log of corrections and hard-won lessons. **Read at session start** (per `.claude/rules/session-start.md`). **Append after ANY user correction or surprising failure** (per `.claude/rules/completion-integrity.md`).

Format per entry: a dated heading, then **Context** (what happened), **Lesson** (the generalizable takeaway), **Rule** (the concrete behavior change to prevent recurrence). Keep entries tight — this file is read every session, so it must stay scannable. Promote a recurring lesson (3+ hits) into a `.claude/rules/*.md` file and leave a pointer here.

This complements the read-only `memory/improvements.md` history and the `memory/automation-ledger.md` compounding score. Those are retrospective; this is the fast in-the-moment correction loop.

---

## 2026-05-25 — Phone-library ingestion: HEIC silently skipped

**Context:** Asked to parse `Pictures/1` (1,090 images). `tools/ingest_images.py` only listed `.jpg/.png/...` in `EXTENSIONS`; 69 iPhone `.HEIC` files would have been silently dropped, and the Claude API rejects HEIC media type anyway.
**Lesson:** iPhone camera output is HEIC; screenshots are PNG; saved/edited images are JPG. A library tool that doesn't transcode HEIC silently loses a chunk of the corpus, and "0 errors" hides it.
**Rule:** Before bulk-ingesting any phone library, confirm the tool's `EXTENSIONS` covers HEIC/HEIF and transcodes to a web-safe format. Report skipped/unsupported counts explicitly — a clean run with N<total processed is a partial run.

## 2026-05-25 — Influencer Claude Code screenshots are frequently wrong

**Context:** Harvested CC "settings" tips from screenshots. `autoUpdaterStatus: "disabled"` is NOT a real key (correct: `DISABLE_AUTOUPDATER=1`); `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` was missing the `_CODE_` infix; `CLAUDE_CODE_MAX_TURNS` could not be confirmed.
**Lesson:** Social-media CC tips mix real, misnamed, outdated, and invented settings. Acting on them blind wastes time or breaks config.
**Rule:** Verify every Claude-Code native-feature claim (settings keys, env vars, frontmatter, commands) against live docs (spawn a `claude-code-guide` agent or check context7) AND against the user's actual settings.json before implementing. Tag each claim REAL / NOT-REAL / UNCERTAIN.

## 2026-05-25 — `deny` overrides `allow`: a naive deny-list breaks workflows

**Context:** Considered adding screenshot-suggested `permissions.deny` of `Bash(rm -rf *)` and `Bash(curl *)`. But `settings.local.json` explicitly *allows* `Bash(curl -s http://127.0.0.1:19484/health)` and `Bash(rm -rf _scratch/...)`. Since deny > ask > allow, those blanket denies would silently break the daemon health-check and scratch-cleanup.
**Lesson:** Permission deny-lists are not free safety; they override existing allows and can break established workflows.
**Rule:** Before adding any `deny` pattern, grep the project + local + global `permissions.allow` for commands the pattern would shadow. Keep denies surgical (e.g., secret-file reads), not blanket.

## 2026-05-25 — Naive section-splitting on `## ` breaks on transcribed content

**Context:** The digest splitter split on any `^## ` line, but transcribed screenshot text contained its own markdown headers → 1,156 phantom sections from 1,090 images.
**Lesson:** When content embeds the same delimiter you split on, naive splitting over-segments.
**Rule:** Split on the most specific boundary available (here `^## (?=IMG_)`, the filename pattern), not a generic markdown header.

## 2026-05-25 — Piped stdout is buffered: background progress is invisible

**Context:** A background `python` run's `[N/1090]` progress never appeared in the output file because Python block-buffers stdout when it's a pipe, and the tool wrote its digest only at the end.
**Lesson:** Tailing a backgrounded process's redirected stdout is an unreliable progress signal.
**Rule:** Judge background-job liveness by process state (PID, elapsed, CPU via `Get-CimInstance`/`Get-Process`), not by tailing a buffered output file. For real-time progress, the tool must flush per-item or write a progress file.

## 2026-05-25 — 7-Zip CLI `-p` (space-separated, interactive) backup failed verification

**Context:** Memory Persistence v1 encrypted backup. A manual 7-Zip CLI run using the space-separated interactive form (`7z a -mhe=on -p <archive> <dir>`) failed verification and left no usable archive (`D:\MemoryBackups` ended up empty). User pivoted to the 7-Zip GUI (AES-256 + encrypt-filenames). `memory_backup.py --backup` uses the *same* space-separated `-p` form and is NOT verified end-to-end in a real TTY. `--self-test` passes only because it uses the attached form `-p{pw}`, not the interactive one.
**Lesson:** 7-Zip CLI `-p` with no attached value is an unreliable way to create a verified encrypted archive; the GUI (or attached `-p"pass"`) is dependable. A passing self-test using a different code path does NOT validate the `--backup` path.
**Rule:** Don't claim `--backup` works for real archives (unverified + suspect form). For real backups use the 7-Zip GUI now; pursue a public-key (age/gpg) flow for v2. Never record an unverified/failed archive as a good backup.

## 2026-05-25 — Placeholder filenames in copy-paste commands get run literally

**Context:** I handed the user `Get-FileHash "D:\MemoryBackups\memory_YYYYMMDD_HHMMSS.7z"` with a literal placeholder; it was run verbatim and failed (no such file).
**Lesson:** Any placeholder token in a copy-paste command will be executed as-is by the user.
**Rule:** In runbook commands, auto-detect the real target (`Get-ChildItem D:\MemoryBackups\memory_*.7z | Sort LastWriteTime | Select -Last 1`) or compute the value. If a placeholder is unavoidable, mark it `<REPLACE_ME>` and say "substitute before running."

## 2026-05-25 — Caching savings claimed without checking prompt size or call shape

**Context:** Recommended prompt-caching `citation_scorer.py`'s judge for "~$21/run." PHASE-2 code-read showed `judge_span_claude` uses raw `urllib` with a single user message (no `system=` block), and `JUDGE_PROMPT` is 169 tokens — below the ~1024-token cache floor. Caching there saves $0. The estimate had been fed a fictional 2000-token rubric.
**Lesson:** Prompt caching only pays when a LARGE (≥~1024 tok Sonnet/Opus, ≥2048 Haiku), STABLE system prefix repeats across many calls. A cost claim is worthless without (a) the real prompt token count and (b) the actual call shape (SDK `system=` vs single user message vs raw HTTP body).
**Rule:** Before claiming any caching saving: read the actual call site, confirm a separable stable system block exists, and measure its tokens against the cache floor. Never feed assumed token counts into a cost estimator.

## 2026-05-25 — Measured: bulk image-triage transcription is unreliable on dense screenshots

**Context:** Validated the Pictures/1 harvest with a 20-image Sonnet-vision fidelity check (`tools/ocr_fidelity_check.py`). Relevance classification was 100% accurate (0/20 misclassified), but verbatim transcription had **6/20 MAJOR errors** on dense technical screenshots — garbled numbers (700W→700μ, INT4→INT9), wrong stat (85 vs 95%), wrong filenames (refactorer.md, reranker.py), dropped sections.
**Lesson:** Cheap vision triage (Haiku) is reliable for *is-this-relevant* classification but NOT for exact values/filenames/configs/stats on dense screenshots. Two-layer trust: structure/relevance = trust; verbatim specifics = verify.
**Rule:** Treat bulk image-OCR output as leads, not facts. Any exact command/config/number/filename from a screenshot digest must be verified against the source image or authoritative docs before it lands in code or a recommendation. Re-extract high-stakes specifics with a stronger vision model.

## 2026-09-22 — Recommended a built-in slash command that this machine's config disables

**Context:** The 2.1.278 update-sweep session told the user "after restart: run /skill-doctor". User ran it and got `Unknown command: /skill-doctor` (session e523922e transcript). The command is real (docs: skills page § "Find unused skills", v2.1.252+) but the binary's embedded note says it is unavailable when the client "does not receive feature settings (Bedrock/Vertex/Foundry, telemetry or non-essential traffic disabled, or a first launch that has not fetched them yet)". `~/.claude/settings.json` line 34 sets `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, which turns off feature-flag fetching on every launch.
**Lesson:** "Exists in the changelog/docs" is not the same as "available in this session." Feature-flag-gated commands (`/skill-doctor` and anything else the docs mark as needing feature-flag fetching) are silently absent under `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, Bedrock/Vertex/Foundry, or `DISABLE_TELEMETRY`.
**Rule:** Before recommending a Claude Code feature, grep `~/.claude/settings.json` env for `DISABLE_NONESSENTIAL_TRAFFIC` / `DISABLE_TELEMETRY` / provider vars and check the docs for a "feature-flag fetching" caveat. If gated, say so and give the one-session workaround (temporarily unset the var, restart, run, restore) instead of a bare "run X".

## 2026-09-22 — Docs fetches truncate; the binary is the authority for env-var names

**Context:** A May catch recorded `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` as "misnamed (missing `_CODE_`)". The env-vars docs page truncates on every fetch, so nobody re-read the row. A docs agent claimed the opposite today. `grep -a -o NAME claude.exe | wc -l` settled it in one call: 0 hits for the `_CODE_` spelling, 6 for the plain one. The setting had been a silent no-op for four months.
**Lesson:** For "is this key real / what is it called", a truncated docs fetch is weaker evidence than the installed binary. Zero string hits = the code cannot read it. Positive hits = real, even if undocumented (five "NOT-IN-DOCS → remove" recommendations today were wrong for that reason).
**Rule:** Before removing or renaming any Claude Code env var or settings key, grep the installed `claude.exe` for the exact string and record the count in the ledger. Treat "undocumented" as "unverified", not "dead".

## 2026-09-22 — `json.dump` round-trips wreck git-tracked settings diffs; Python text mode flips line endings

**Context:** Removing two dead permission rules via `json.load`/`json.dump` produced a 21-line diff (inline hook objects expanded). A later `write_text` turned every LF into CRLF (99-line diff for a 7-line insert). Both were reverted from backup and redone as byte-level line edits.
**Lesson:** Formatting churn hides the real change and makes review impossible; Windows Python text mode rewrites newlines unless `newline=""` or bytes are used.
**Rule:** For git-tracked JSON/MD: back up, edit as bytes or exact lines, re-parse to validate, then `diff` against the backup and require the diff to be exactly the intended lines before moving on.

## 2026-09-22 — Git Bash rewrites slash-prefixed args to `claude -p`

**Context:** `claude -p "/context"` from the Bash tool became `C:/Users/atayl/AppData/Local/Programs/Git/context` (MSYS path conversion) and burned a full headless session-start answering a nonsense path.
**Lesson:** Any argument beginning with `/` is a path candidate to MSYS.
**Rule:** Run headless slash commands from the PowerShell tool, or set `MSYS_NO_PATHCONV=1`. The working recipe for a per-turn context baseline is in `claude-code-config-state.md`.

## 2026-09-22 — `skillOverrides` visibility states do not cut context; measure the TOTAL, not a category

**Context:** A triage agent estimated −1.7k tokens/turn from moving 53 skills to `name-only` / `user-invocable-only`. Four headless `/context` captures (26 name-only, 26 on, 53 on, every override on including the 24 `off`) all totalled exactly 60.8k. The "Skills" bucket fell and "System tools" rose by the same amount each time; even the 24 `off` skills changed nothing in the total. The estimate was wrong in kind, not degree.
**Lesson:** The harness still carries hidden skills somewhere in the tool definitions in 2.1.278, and `/context` re-buckets rather than removes them. Category deltas can be pure accounting. The only thing that removed tokens this session was content that stopped being loaded at all (rules files condensed or path-scoped, MEMORY.md shortened, agent files deleted).
**Rule:** Any "saves N tokens" claim must be backed by the `/context` **total** from two captures of the shipped state, not a category line or a chars/4 estimate. Report negative results with the same prominence as wins (measurement-discipline no-cherry-pick).

## 2026-09-22 — Background subagent mailbox reports are delivered only at the lead's turn boundary; recovered mid-turn from its transcript

**Context:** A `claude-code-guide` agent spawned with `Agent` (name `cc-docs-verify`) finished two reports and sent both with `SendMessage(to="team-lead")`. `ListAgents` showed it idle for 10+ minutes while the lead was still inside one long multi-tool turn, and nothing arrived; a resend request changed nothing either. All three messages then landed together the moment the lead's turn ended. **[Correction, same day]:** first written as "never reached the lead"; the true mechanism is delayed delivery at the turn boundary, not loss.
**Lesson:** Messages from a background agent do not interrupt an in-progress turn; they queue until the lead stops. Inside a long turn the agent looks stuck. The agent's full transcript, including the `message` payload of every `SendMessage` tool_use, is on disk at `~/.claude/projects/<project>/<session-id>/subagents/agent-<name>-<hash>.jsonl`.
**Rule:** If an agent shows idle and its result is needed before the turn can end, parse that JSONL (assistant `tool_use` blocks named `SendMessage`, key `input.message`; or long `text` blocks) with `PYTHONUTF8=1 python` instead of waiting or re-spawning; do not send resend requests (they only queue more copies). Prefer having verification agents write their report to a deterministic file path named in the prompt (`AI_Studio/Reports/...`) so the mailbox is never load-bearing.

## 2026-09-22 — Windows-shell gotchas promoted to a checklist (3+ hits)

**Context:** cp1252 (s.280), PowerShell binary pipe (s.285), MSYS `/context` path conversion + CRLF flip (s.288), and two more cp1252 crashes in this session (`check_hook_sync.py`, a transcript parser).
**Rule:** Read `tasks/windows-shell-checklist.md` before any shell-heavy work on this machine; it holds the ten traps and the recovery paths. New Windows-shell lessons go there, with a one-line pointer here.

## 2026-09-22 — A substring guard on Bash blocks documentation that quotes the guarded commands

**Context:** The new `git-destructive-guard` daemon handler blocked (a) a `for` loop whose quoted test strings contained the force-push command and (b) a `cat >> ledger <<'EOF'` append whose heredoc body quoted it in a table row. Both were data, not commands.
**Lesson:** A PreToolUse guard sees the whole Bash command text and cannot tell quoted data from intent unless it parses structure. Fail-closed is right for a safety guard, but heredoc bodies fed to files are pure data and the release-gate handler already strips them.
**Rule:** Guards that pattern-match Bash text must drop heredoc bodies unless an interpreter consumes them (`_guard_visible_command`). When a Bash command must contain a guarded phrase as data (tests, ledgers, docs), write it with the Write/Edit tool or put it in a file and run the file; do not weaken the guard for the sake of one command.

## 2026-09-22 — `pythonw` from the Bash tool holds the shell for the full timeout

**Context:** `curl -X POST /shutdown; pythonw .claude/hooks/daemon_shim.py; curl /health` hung the Bash tool for its 60 s limit and was moved to the background; the daemon did come up, but the rest of the command never ran and its output was lost.
**Lesson:** The Bash tool waits on inherited stdio handles; a "detached" `pythonw` launched this way still pins the call until the timeout.
**Rule:** Restart the daemon from the PowerShell tool (`Start-Process pythonw -ArgumentList '.claude/hooks/daemon_shim.py' -WindowStyle Hidden`) or with `cmd //c start "" pythonw ...` from Bash, then poll `/health` in a separate call. Never chain the spawn with the verification in one Bash command.

## 2026-09-23 — The Bash tool mangles backslashes in inline commands and heredocs

**Context:** Superpowers fork session. A Python heredoc with `replace('\\', '/')` reached Python as `replace('\', '/')` (syntax error); a heredoc containing backticks died with "unexpected EOF while looking for matching `'" (the wrapper expanded them); `cmd.exe /c "\"C:\path\x.cmd\""` reached cmd as the literal string `\"C:\path\x.cmd\"`. Three separate failures, one cause: the inline `command` string is re-escaped before the shell sees it.
**Lesson:** Inline Bash-tool commands are not a faithful shell. Anything with backslashes, backticks, or `\"` gets altered; `$'\r'` happens to survive.
**Rule:** Put any command that needs backslashes, backticks, nested quotes, or a Python/heredoc body into a script file with the Write tool and run the file (`bash tools/x.sh`, `python tools/x.py`). Use `os.sep`/`cygpath` instead of typed backslashes. Verify with a raw-output probe before blaming the script under test (the run-hook.cmd test "failed" 4/4 because of this, not because of the wrapper).

## 2026-09-23 — `--add-dir` on the launch line did not register; verify with a write probe

**Context:** Superpowers activation tab launched as `claude --add-dir C:\Users\atayl\superpowers-work --add-dir C:\Users\atayl\.claude\skills`. Reads under `superpowers-work` succeeded silently, but the first Write there triggered a directory-approval prompt and the harness then reported the directory as newly added. The second path did not exist yet, and `/add-dir` refused it until the folder was created.
**Lesson:** A successful Read outside the project is not evidence that a directory is an additional working directory; only a Write/Edit without a prompt (or `/permissions`) is. A non-existent `--add-dir` path is rejected, and this build appears to have dropped both flags.
**Rule:** After launching with `--add-dir`, probe with a throwaway Write into the added directory before relying on it; create the target folder first; if the probe prompts, run `/add-dir <path>` inside the session.

## 2026-09-23 — `claude plugin eval` deletes run traces unless `--keep-temp`; the trace omits the system prompt

**Context:** Two eval cases scored 2/3 on LLM graders. The failed runs' `tracePath` pointed into `%TEMP%\claude-eval-*` dirs that were already gone, so the first-pass failures could only be judged from the grader's stored evidence excerpt. The rerun with `--keep-temp` produced full traces and showed one failure was a real gate-skip and the other judge noise. Separately, grepping a kept trace for CLAUDE.md text returned 0 hits even though a direct probe from the same cwd ancestry proved the global CLAUDE.md is loaded: the stream-json trace records messages and hook events, not the system prompt.
**Lesson:** Without traces, an eval failure is unattributable (behavior vs judge). And "not in the trace" does not mean "not in the context" for system-prompt content such as CLAUDE.md files.
**Rule:** Always pass `--keep-temp` on eval runs whose failures you may need to explain, and copy `out/trace.jsonl` files into the evidence folder immediately. To learn what instructions an eval session carried, run a headless probe from a sibling cwd and ask, or read the run's `system init` record; never infer it from a trace grep.

## 2026-09-23 — ~~Eval sessions inherit ancestor CLAUDE.md files, so a global-CLAUDE.md change moves eval results~~ [WITHDRAWN 2026-09-24: eval children load no CLAUDE.md; see the 2026-09-24 "WITHDRAWN" entry below. Kept as written for the audit trail.]

**Context:** `routing-react-todo` was 3/3 the day the fork was built (no overrides block) and 4/6 the day the nine-line block landed in `C:\Users\atayl\CLAUDE.md`. The harness cwd is `%TEMP%\claude-eval-*\home\cwd`, which is under `C:\Users\atayl`, so the global file loads in every eval arm (probe `superpowers_activation/probes/block_in_temp_cwd.json`).
**Lesson:** `claude plugin eval` is not isolated from the user's ancestor CLAUDE.md files; the "without plugin" arm still carries them too. A change to the global file is a confound for any before/after eval comparison.
**Rule:** Record the SHA-256 of the global CLAUDE.md in every eval report header, and re-run the baseline when it changes. When an override line is meant to be tested, the eval harness is a valid instrument (it sees the file); when the plugin's own prose is meant to be tested in isolation, run from a cwd outside the home tree.

## 2026-09-23 — Renaming a skills-dir plugin folder does not unload it; arrays do not survive `pwsh -File`

**Context:** Rollback rehearsal for the superpowers fork. The runbook's deactivation step was `Rename-Item ~/.claude/skills/superpowers superpowers.off`. After the rename, `claude plugin list` still showed `superpowers@skills-dir … Path ~\.claude\skills\superpowers.off, Status loaded`, and a fresh headless probe still had the bootstrap and the five agents. Moving the folder out of `~/.claude/skills` deactivated it (plugin list empty, probe NO / 0 / NONE). In the same run, `& pwsh -File probe.ps1 -ExtraArgs @('--max-turns','2')` flattened the array into separate tokens and bound `2` to `-PromptFile`.
**Lesson:** The skills-dir loader treats every subfolder with `.claude-plugin/plugin.json` as a plugin regardless of its name; "rename to .off" is a false rollback. And PowerShell arrays only pass intact to a `.ps1` called in-process (`& script.ps1 -Param @(...)`), not across a `pwsh -File` process boundary.
**Rule:** To deactivate a skills-dir plugin, move its folder out of `~/.claude/skills` (or `claude plugin disable <id>`), then prove it with `claude plugin list` AND a headless probe; never trust a rename. Call helper `.ps1` files in-process when passing arrays.

## 2026-09-23 — A test that passes from the Claude Code shell can fail from plain Git Bash: PATH order decides what `command -v git` returns

**Context:** `tests/hooks/test-run-hook-cmd.sh` passed 8/8 three times today from the Bash tool, then failed (7/8) the moment `update_deployed.ps1` ran it through `bash.exe -lc`. Case 2 builds its PATH from `$(command -v git)`: the tool shell resolves `/cmd/git` (`Git\cmd`), a plain Git Bash resolves `/mingw64/bin/git`, and the wrapper's `<gitdir>\..\bin\bash.exe` derivation only works from `cmd`. The wrapper gap is real (silent skip on a `mingw64\bin` PATH) and the test was environment-dependent, so the suite could not have caught it from the shell that ran it.
**Lesson:** "8/8 from my shell" is evidence about my shell. Tests that read tool locations from the environment must pin them, or run under more than one shell layout before a result counts.
**Rule:** Before calling a shell-dependent suite green, run it once from a plain `bash.exe -lc` (login shell) as well as from the tool shell, and pin any `command -v` derived paths in test setup. Record which shell produced each count.

## 2026-09-23 — A test guide's expected output must come from a captured output, not from a runbook sentence

**Context:** The live-test guide told Adam that `/context` would show "You have superpowers" once. He ran it: it does not. Two headless `/context` captures with the plugin loaded (VoxCore and CalmCore) had been on disk for hours and contain 0 occurrences of the phrase; `/context` shows the bootstrap only as ~1.3k tokens in the Messages row and lists the agents/skills in tables. The sentence had been copied from the activation runbook, which itself was never checked against a capture. In the same pass the guide's `/agents` step was obsolete: the wizard was removed in 2.1.281.
**Lesson:** An "expect" line inherited from a prior document is a claim, not evidence. When a capture of the exact command exists, the expectation must be derived from it.
**Rule:** Before shipping any checklist that says "command X shows Y", grep an actual capture of X for Y (or run X once) and cite the capture in the guide. Re-verify slash-command steps against the installed version's `/help` after each Claude Code update.

## 2026-09-23 — A "permission prompt" on every PowerShell call was a syntax pre-check failing on command length, not an allowlist miss

**Context:** During the superpowers live test in a scratch project, 20 of 20 PowerShell tool calls prompted Adam. I first blamed the missing `PowerShell(*)` rule (VoxCore has it in local settings; scratch did not). The actual prompt text was "Command contains malformed syntax that cannot be parsed: pwsh exited with code 1: The command line is too long." That is Windows refusing a command line over ~8,191 characters inside Claude Code's PowerShell syntax pre-check. An unparseable command matches no permission rule and always falls back to asking. The tab was pushing whole file bodies through PowerShell here-strings.
**Lesson:** Read the exact prompt text before diagnosing a permission problem. Allowlist rules apply only to commands the harness can parse; giant inline commands can never be pre-approved.
**Rule:** When a Windows session prompts on every shell call, check the message for "too long" first. Fix by instructing the model to write file contents with Write/Edit and keep shell commands short (the live-test guide now seeds this instruction in Step 0), then add `PowerShell(*)` for the ordinary calls. Do not reach for bypassPermissions.

## 2026-09-24 — A prompt-level tool ban on Workflow agents is advisory: 11 of 95 used Bash anyway

**Context:** Superpowers live test Part D (Workflow `wf_fa59346b-579`, 22 reviewers + 72 skeptics + 1 synthesis). Every prompt opened with "Tools: Read, Grep, Glob ONLY. Never call Edit, Write, Bash…". The journal scan of each agent's self-reported `tools_used` shows 11 of 95 called Bash (grep/find; one also PowerShell), several with an inline justification ("read-only, within permitted scope"). SHA-256 of all 554 files in both plugin trees was identical before and after, so nothing was modified, but the restriction itself did not hold.
**Lesson:** Agents substitute Bash for Grep/Glob when convenient and self-justify it. Only a tool-list restriction (an agentType whose frontmatter `tools:` excludes the banned tools, or a PreToolUse guard) prevents the call. A before/after hash is the only proof of read-only; the prompt is not.
**Rule:** For a read-only or tool-restricted fan-out: (1) dispatch with an agentType whose tools list excludes the banned tools (add a minimal `.claude/agents/readonly-reviewer.md` with Read/Grep/Glob if none fits) or gate the run with a daemon PreToolUse rule; (2) hash the protected tree before and after and put the comparison in the report; (3) scan the journal for `tools_used` and report every violation by agent rather than trusting the prompt.

## 2026-09-24 — `claude plugin eval` does not load user-scope plugins: point it at `fork/` before deploying

**Context:** Part E needed after-evals for adam.3 while adam.2 was still deployed at `~/.claude/skills/superpowers`. Concern: the with-arm would load both copies and the without-arm would still have adam.2. A one-case run with `-Plugin fork` settled it from the trace init records: the without-arm session listed 0 `superpowers:*` skills, 0 `superpowers:*` agents and `plugins=[agents-md@builtin]`; the with-arm listed 15 skills and 5 agents once each from `superpowers@inline` at the fork path.
**Lesson:** The eval harness builds its own plugin set from the path you pass and ignores `~/.claude/skills`; the ancestor CLAUDE.md still loads because the cwd is under `C:\Users\atayl`. So fork evals are clean pre-deploy, and the deploy can wait for a green suite.
**Rule:** Run before/after evals against `fork/` (`eval_run.ps1 -Plugin <fork>`) before `update_deployed.ps1`, and cite the init-record check (`adam3-isolation-check` traces) rather than assuming. Also: `eval_run.ps1`'s trace-copy loop throws on this JSON shape and copies 0; use `live_tests/2026-09-23/partE/copy_traces.py` until the loop is fixed.

## 2026-09-24 — Write the FORK-NOTES entry before the deploy, not after

**Context:** The adam.3 deploy ran, then I appended a deploy addendum to `fork/FORK-NOTES.md`. FORK-NOTES.md is a shipped file, so the deployed copy no longer matched the fork, and `update_deployed.ps1` refuses a same-version re-run when shipped files differ.
**Lesson:** Every fork file, documentation included, is under the byte-identical contract; post-deploy edits to any of them need another deploy or a one-file copy that is logged.
**Rule:** Finish the FORK-NOTES entry (including "evidence: see next addendum" placeholders written as prose, not TODOs) before running the deploy; if a note must follow the deploy, copy that one file to the deployed path, verify `diff -rq`, and add a line to `UPDATE_LOG.md` saying so.

## 2026-09-24 — WITHDRAWN: eval children do NOT load the global CLAUDE.md (supersedes the 2026-09-23 "Eval sessions inherit ancestor CLAUDE.md files" entry)

**Prior claim (2026-09-23, verbatim):** "The harness cwd is `%TEMP%\claude-eval-*\home\cwd`, which is under `C:\Users\atayl`, so the global file loads in every eval arm (probe `superpowers_activation/probes/block_in_temp_cwd.json`)."
**New claim:** `claude plugin eval` children load no personal or project CLAUDE.md, no user-scope plugins, no hooks or MCP servers. The block is absent in both arms.
**Evidence:** a probe case run through the eval runner itself (`evals/adam3-inherit-check`, temp plugin copy `partE/tmp_plugin_probe`, prompt "quote numbered line 10 of the Superpowers section or reply NONE"): with-arm NONE, without-arm NONE, 1 turn each, traces copied. The docs (plugin-evals § How runs are isolated) say the same. The 09-23 evidence was a normal headless probe from a temp cwd, which walks ancestor directories; an eval child does not. ChatGPT's consolidated proposal (P02-E) flagged exactly this gap.
**Consequences:** the 289b line-9 amendment's eval justification (react-todo 4/6 → 3/3) was variance, not the block; its interactive justification (live test S2/S5) stands. Evals measure plugin prose only. Override lines are tested with headless probes (`partE/run_probes.ps1`), which do load the file. The `eval_run.ps1` SHA log is provenance only. Corrections applied with dated notes in FORK-NOTES, README, eval_run.ps1, CURRENT_STATE, both handoffs, the registry row, CLAUDE_MD_OVERRIDES, REPORT § 0 and the memory file.
**Rule:** a claim about what an isolated harness loads is settled only by a probe run inside that harness. Before crediting a config change with an eval delta, run a marker probe through the same runner. Treat n=6 judge-scored deltas as noise until a mechanism is shown.

## 2026-09-24 — `grep -c $'\r'` reported a CRLF flip that did not happen

**Context:** After editing `~/.claude/commands/swarm.md`, a Bash-tool `grep -c $'\r'` returned 196 (every line) on a file PowerShell showed as 0 CRLF / 196 LF; a pipe probe with a real CR returned 0. The clean 6-hunk diff was the tell.
**Rule:** Check line endings by byte count, never Bash-tool grep. Detail: `tasks/windows-shell-checklist.md` item 18.

<!-- Append new entries above this line is NOT required; append chronologically below the last entry. -->

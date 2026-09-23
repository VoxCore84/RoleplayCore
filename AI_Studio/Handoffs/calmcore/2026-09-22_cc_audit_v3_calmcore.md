# Handoff: Claude Code audit v3, CalmCore half (2026-09-22)

Open a Claude Code tab at `C:\Users\atayl\CalmCore` and paste: "Read `C:/Users/atayl/VoxCore/AI_Studio/Handoffs/calmcore/2026-09-22_cc_audit_v3_calmcore.md` and execute it. Report evidence per item; do not commit."

Origin: `C:/Users/atayl/Desktop/Excluded/claude-code-optimization-prompt-v3.md`, executed in VoxCore session 6dce2cb5. Ledger of what VoxCore already did: `AI_Studio/Reports/cc_audit_v3_20260922-1804/APPLIED_LEDGER.md`. Decisions fixed by Adam (do not reopen): Fable 5.1 at xhigh everyday; `acceptEdits` + `Bash(*)` + daemon guards, no auto mode; `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` stays; built-in Explore stays on its inherited Opus 5.5 (no override).

## Already done for CalmCore from the VoxCore side (verify only)

1. `CalmCore/.clangd` written (`CompilationDatabase: out/build/x64-RelWithDebInfo`, background index). `compile_commands.json` exists in both `out/build/x64-Debug` and `x64-RelWithDebInfo` (Ninja).
2. `CalmCore/.claude/settings.local.json` `enabledMcpjsonServers` grew from 3 to all 8 servers in `CalmCore/.mcp.json` (voxcore-db, voxcore-server, local-llm, codebase-db, gamedb, wago-db2, wow-api, knowledge-base). This was required because `~/.claude/settings.json` `enableAllProjectMcpServers` is now `false`; without it five servers would have vanished at CalmCore's next start. Backup: `CalmCore/.claude/settings.local.json.bak_20260922_180621_v3`.
3. The hook daemon (`hook_daemon.py`, symlinked from CalmCore to VoxCore) is v1.3.1 with a new route `/hook/git-destructive-guard` (heredoc-aware). One daemon on 127.0.0.1:19484 serves both repos; it was restarted from VoxCore.
4. User-scope changes that apply here too: top-level `effortLevel` and `alwaysThinkingEnabled` removed; `modelSettings` now has `claude-fable-5-1: xhigh` and `claude-opus-5-5: high`; `fastModePerSessionOptIn: true`; `code-review@claude-plugins-official` disabled (built-in `/code-review` remains); status line script rewritten to read the branch from the session's own directory (it was hardcoded to VoxCore, so CalmCore tabs showed the wrong branch).

## To do in this tab

1. **Register the guard** in CalmCore's hooks. CalmCore has hook blocks in BOTH `.claude/settings.json` (13 events, 39 entries) and `.claude/settings.local.json` (hooks block, older, no timeouts, still lists `cpp-build-reminder`). First determine whether both blocks fire (settings merge hooks across scopes; if so every hook runs twice here). Then add, next to the existing `sql-safety` PreToolUse Bash entry: `{ "type": "http", "url": "http://127.0.0.1:19484/hook/git-destructive-guard", "timeout": 2 }`. Add to the Stop group: `{ "type": "command", "command": "python \"$CLAUDE_PROJECT_DIR/.claude/hooks/hook_daemon.py\" --ensure", "timeout": 5, "async": true }`. Add `"if": "Bash(git commit*)|Bash(git push*)|Bash(git merge*)"` to the `sync-on-git` PostToolUse entry. Textual edits only; back up first; validate JSON.
2. **Guard tests** through the real tool path: `mkdir -p _scratch/v3_probe && rm -rf _scratch/v3_probe` (expect allow); a `mysql ... world < file` string without `db_snapshot.py` (expect block). Do NOT run `git reset --hard` or a real force push to test; use `python C:/Users/atayl/VoxCore/AI_Studio/Reports/cc_audit_v3_20260922-1804/guard_smoke.py` for the route-level matrix (21 cases). Note for CalmCore: the guard blocks `mysql` imports into world/auth/characters/hotfixes unless `db_snapshot.py snapshot` is in the same command, which is the house rule.
3. **Rename** `.claude/commands/status.md` to `sys-status.md` (VoxCore proved the project skill shadows the built-in `/status`).
4. **LSP test** (Phase 3.6 of the prompt): confirm the clangd-lsp plugin picks up `.clangd`; add a deliberate type error to a scratch `.cpp` inside the repo, confirm a diagnostic arrives after the edit, revert; run one definition lookup via the LSP tool and one via the `codeintel` MCP server for the same symbol; record tool calls, latency, and first-turn indexing time. Keep both if they answer different questions (ctags instant symbol search vs clangd diagnostics after edit).
5. **Prune the MCP allowlist** written in item 2 above: `claude mcp list` here; remove from `enabledMcpjsonServers` any server that fails to connect at every start (VoxCore removed `wago-db2` and `mysql` for that reason on 2026-09-22).
6. **Defender exclusions** (admin PowerShell, Adam runs; proposed only):
   ```powershell
   Add-MpPreference -ExclusionPath 'C:\Users\atayl\CalmCore'
   Add-MpPreference -ExclusionPath 'C:\Users\atayl\AppData\Local\Programs\Git'
   Add-MpPreference -ExclusionProcess 'bash.exe'
   ```
   Existing exclusions already cover `~/.claude`, `Temp\claude`, `%APPDATA%\npm`, VoxCore, Miniconda, and the compiler/tool processes.
7. **`/sync-infra`** for the parity deltas the 2026-09-22 sweep listed (rules files, 7 agent frontmatters, `check_write_size.py` byte-diff) plus today's: hooks block entries above, `status.md` rename, and the `CRITICAL RULES` block that now lives only in `CalmCore/CLAUDE.md` (VoxCore's copy was removed as a duplicate).
8. **Build-output filter, follow-up only:** CalmCore has no transcripts on disk (`~/.claude/projects/C--Users-atayl-CalmCore/` holds only `memory/`), so raw-build frequency is UNAVAILABLE. After a few sessions exist, count raw `ninja -j` / `cmake --build` Bash calls; if 5 or more in 30 days, add a daemon handler that rewrites the command via `updatedInput` to tee the full log to `%TEMP%` and print error lines plus exit code. Builds through `_build_ps.ps1` or `mcp__voxcore-server__build` already return parsed diagnostics and need nothing.

## Do not

Commit or push; edit `.claude/rules/excluded-corpus.md` or anything under `Desktop/Excluded`; use `json.dump` on git-tracked JSON; run slash commands through the Bash tool (MSYS rewrites the leading slash); create recurring cron jobs.

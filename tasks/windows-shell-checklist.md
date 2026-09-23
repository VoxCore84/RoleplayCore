# Windows shell checklist (Git Bash tool + PowerShell tool + Python 3.14)

Escalated 2026-09-22 after three logged hits (cp1252 s.280, PowerShell binary pipe s.285, MSYS `/context` path + CRLF flip s.288). Nothing auto-loads this file; `tasks/lessons.md` points here.

## Before running a command

1. **Leading-slash arguments (`/context`, `/usage`, `/hook/x`)**: Git Bash rewrites them into `C:/Users/.../Git/<name>` paths. Use the PowerShell tool, or prefix `MSYS_NO_PATHCONV=1`.
2. **Non-ASCII output from Python** (arrows, box characters, curly quotes): the console is cp1252, so `print()` crashes with `UnicodeEncodeError`. Prefix `PYTHONUTF8=1` or set `sys.stdout.reconfigure(encoding="utf-8")`.
3. **Binary through a PowerShell pipe** (`|` with .zip, .db, .7z): PowerShell decodes it as text. Use `-Raw -AsByteStream`, `[IO.File]` APIs, or do it in Python/Bash.
4. **Placeholders in copy-paste commands** (`<name>`, `YYYYMMDD`): they get run literally. Compute the real value or mark `<REPLACE_ME>` and say so.

## Before editing a file

5. **Line endings**: Python text mode writes CRLF on Windows; a 7-line change becomes a 99-line diff. Write with `newline=""` or as bytes; check `git diff --stat` before moving on.
6. **`json.load` / `json.dump` round-trips** reformat the whole file. For git-tracked JSON edit exact lines (Edit tool), re-parse to validate, and `diff` against the backup.
7. **`stat -c %s` on a symlink** returns the target-path length, not the file size. Use `wc -c < file` or `stat -L`; in PowerShell `(Get-Item $p).Length`.
8. **`truncate`** is almost never right. Copy, verify, then replace.

## Before trusting a measurement

9. **Buffered stdout in background jobs**: tailing a redirected file shows nothing until exit. Judge liveness by PID/CPU, or flush per item.
10. **`bash -lc` vs the Bash tool**: the tool runs a non-login shell snapshot taken at session start (90 ms). Profile cost measured with `bash -lc` (425 ms here) does not apply to tool calls.
11. **Headless slash commands run the PROJECT skill** if one shares the name: `claude -p "/doctor"` ran the project doctor skill for 18 min and overwrote `session_state_live.md`; `"/status"` ran the dashboard. Only `/context` and `/usage` are safe headless probes; the built-in `/doctor`, `/status`, `/mcp`, `/hooks`, `/model` are user-typed.
12. **Detached spawns hold the calling tool**: `pythonw x.py` from the Bash tool and `Start-Process ... -Wait` from PowerShell both block until the daemon child exits. Use `pwsh -File tools/daemon_restart.ps1`.

## Recovery paths

- Daemon: `curl -s http://127.0.0.1:19484/health`; restart with `pwsh -File tools/daemon_restart.ps1` (shutdown, detached spawn, health poll).
- Background subagent silent: parse `~/.claude/projects/<proj>/<session>/subagents/agent-*.jsonl` (`tool_use` named `SendMessage`, key `input.message`).

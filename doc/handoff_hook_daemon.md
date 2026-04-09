# Handoff: Hook Dispatcher Daemon

**From**: Main tab (session 233, optimization sweep)
**To**: New tab — build the hook daemon
**Date**: 2026-04-08
**Estimated effort**: 1-2 hours

---

## Problem

We have 20 Python hook scripts in `.claude/hooks/`. Each fires as a separate `python` subprocess. Python cold-start on Windows is ~80-150ms. On busy turns with 10+ tool calls, hooks fire 20-60 times = **2-6 seconds of pure Python startup latency per turn**.

`session-stats.py` alone fires on 6 different events. `edit-verifier.py` fires on every Edit. `large-file-guard.py` on every Read. It adds up.

We just added `PYTHONDONTWRITEBYTECODE=1` to user settings which shaves ~20ms each, but the root cause is N cold starts per turn.

## Solution: Hook Dispatcher Daemon

A single long-running Python process that receives hook events over localhost TCP and dispatches to handler functions in-process. Eliminates all Python cold-start overhead.

### Architecture

```
Claude Code                     Hook Daemon (always running)
    │                                │
    ├─ PreToolUse ───► dispatch.py ──┤──► sql_safety()
    ├─ PostToolUse ──► dispatch.py ──┤──► edit_verifier()
    ├─ UserPromptSubmit → dispatch.py┤──► timestamp_injector()
    │                                │    prompt_context_injector()
    └─ Stop ─────────► dispatch.py ──┤──► stop_verify()
                                     │    session_stats()
```

**Two files**:
1. **`hook_daemon.py`** — Long-running server. Loads all handler functions at startup. Listens on `localhost:19484`. Receives JSON event, routes to handler(s), returns JSON response.
2. **`hook_dispatch.py`** — Thin ~20-line script. Reads stdin JSON, sends to daemon via TCP, prints daemon response to stdout, propagates exit code. Falls back to direct Python invocation of the legacy script if daemon is unreachable.

### Communication Protocol

1. `dispatch.py` reads JSON from stdin (Claude Code hook protocol)
2. Opens TCP connection to `localhost:19484`
3. Sends: `{length}\n{json_payload}` (length-prefixed for framing)
4. Reads response: `{exit_code}\n{stdout_content}`
5. Prints `stdout_content` to stdout, exits with `exit_code`

The daemon must handle concurrent connections (multiple hooks fire in parallel when `async: true`). Use `asyncio` or `threading`.

### Handler Registry

The daemon maps `(event_type, matcher)` → `handler_function`. Each existing script becomes a function:

```python
HANDLERS = {
    ("PreToolUse", "Bash"): [sql_safety, release_gate_enforce],
    ("PreToolUse", "Edit|Write"): [sensitive_file_guard],
    ("PostToolUse", "Write|Edit"): [cpp_build_reminder, release_gate_revalidate],
    ("PostToolUse", "Edit"): [edit_verifier],
    ("PostToolUse", "Read"): [large_file_guard],
    ("PostToolUse", "Bash"): [sync_on_git],
    ("PostToolUse", ""): [session_stats],  # fires on ALL tools
    ("PostToolUseFailure", "Read"): [docx_auto_extract],
    ("PostToolUseFailure", ""): [session_stats],
    ("UserPromptSubmit", ""): [timestamp_injector, prompt_context_injector],
    ("PreCompact", ""): [precompact_snapshot],
    ("SessionStart", "compact"): [compact_reinject],
    ("SubagentStop", ""): [subagent_complete],
    ("SubagentStart", ""): [session_stats],
    ("ConfigChange", ""): [session_stats],
    ("Notification", ""): [notification_toast],
    ("Stop", ""): [stop_verify, session_stats],
    ("SessionEnd", ""): [cowork_sync],  # special: external script
}
```

### Existing Hooks — Current State

| Script | Lines | Event(s) | Sync? | Notes |
|--------|-------|----------|-------|-------|
| `sql-safety.py` | ~60 | PreToolUse(Bash) | SYNC | Blocks DROP/TRUNCATE/DELETE-no-WHERE. Exit 2 = block. |
| `release-gate-enforce.py` | ~80 | PreToolUse(Bash) | SYNC | Blocks git push --tags, gh release when gate != PASS. Exit 2 = block. |
| `sensitive-file-guard.py` | ~40 | PreToolUse(Edit\|Write) | SYNC | Blocks edits to .env, credentials, etc. |
| `cpp-build-reminder.py` | ~30 | PostToolUse(Write\|Edit) | SYNC | Prints reminder if .cpp/.h edited |
| `edit-verifier.py` | 172 | PostToolUse(Edit) | SYNC | Re-reads file, verifies edit applied. Stdout = advisory. |
| `release-gate-revalidate.py` | ~50 | PostToolUse(Write\|Edit) | ASYNC | Sets gate to STALE when publishable/ files change |
| `large-file-guard.py` | ~40 | PostToolUse(Read) | ASYNC | Warns when Read consumed >3000 lines |
| `sync-on-git.py` | ~30 | PostToolUse(Bash) | ASYNC | Triggers bridge sync after git ops |
| `session-stats.py` | 38 | 6 events (PostToolUse, Stop, SubagentStart/Stop, PostToolUseFailure, ConfigChange) | ASYNC | JSONL logger. Most frequent hook. |
| `docx-auto-extract.py` | ~50 | PostToolUseFailure(Read) | SYNC | Auto-extracts .docx when Read fails |
| `timestamp-injector.py` | 29 | UserPromptSubmit | SYNC | Injects timestamp into every prompt |
| `prompt-context-injector.py` | 128 | UserPromptSubmit | SYNC | Keyword-aware context injection |
| `precompact-snapshot.py` | ~80 | PreCompact | SYNC | Captures session state before compaction |
| `compact-reinject.py` | ~60 | SessionStart(compact) | SYNC | Restores context after compaction |
| `subagent-complete.py` | ~30 | SubagentStop | ASYNC | Toast + JSONL logging |
| `notification-toast.py` | ~60 | Notification | ASYNC | BurntToast with Forms fallback |
| `stop-verify.py` | 146 | Stop | SYNC | Workflow enforcement (<50ms, no API calls) |
| `file-changed-monitor.py` | ~30 | FileChanged? | ASYNC | Monitors file changes |
| `deadline-alert.py` | ~40 | SessionStart | SYNC | Surfaces critical deadlines from .claude/deadlines.json |

**CRITICAL**: sync hooks (no `"async": true` in settings) MUST return before Claude proceeds. The daemon must handle these with zero added latency beyond the TCP round-trip.

### Settings.local.json

All hooks are registered in `C:/Users/atayl/VoxCore/.claude/settings.local.json` under the `"hooks"` key. After building the daemon, you'll rewrite every hook entry to point at `dispatch.py` instead of the individual script.

Example — before:
```json
{
  "matcher": "Bash",
  "hooks": [{
    "type": "command",
    "command": "python \"$CLAUDE_PROJECT_DIR/.claude/hooks/sql-safety.py\"",
    "statusMessage": "SQL safety check..."
  }]
}
```

After:
```json
{
  "matcher": "Bash",
  "hooks": [{
    "type": "command",
    "command": "python \"$CLAUDE_PROJECT_DIR/.claude/hooks/hook_dispatch.py\" sql-safety",
    "statusMessage": "SQL safety check..."
  }]
}
```

The dispatch script receives the handler name as argv[1] so it can tell the daemon which handler to run. Alternatively, the daemon can infer the handler from the event JSON (it contains `hook_event_name` and `tool_name`).

### Fallback

If the daemon is unreachable (not started, crashed), `dispatch.py` MUST fall back to running the legacy script directly:
```python
# Pseudo:
try:
    response = send_to_daemon(event_json, handler_name)
except ConnectionRefusedError:
    # Fallback: run legacy script directly
    result = subprocess.run(["python", legacy_script_path], input=event_json, ...)
```

This ensures hooks never silently fail if the daemon isn't running.

### Daemon Lifecycle

- **Start**: `python .claude/hooks/hook_daemon.py` — runs in background. Could be started by `start_all.bat` or by a SessionStart hook itself (bootstrap).
- **Stop**: Graceful shutdown on SIGTERM/SIGINT. Or: the daemon auto-exits after 30 minutes of inactivity (no hook events received).
- **Health check**: `dispatch.py --health` → exits 0 if daemon responds, 1 if not.
- **PID file**: `.claude/hooks/hook_daemon.pid` for process management.

### Performance Target

- Legacy: ~100-150ms per hook invocation (Python startup)
- Daemon: <5ms per hook invocation (TCP round-trip + handler execution)
- Measured via: `session-stats.py` already logs timestamps — compare before/after

### Implementation Plan

1. **Phase 1: Daemon server** (~30 min)
   - `hook_daemon.py`: asyncio TCP server on localhost:19484
   - Health check endpoint
   - PID file management
   - Graceful shutdown

2. **Phase 2: Handler refactoring** (~30 min)
   - Create `hook_handlers/` directory
   - Move each hook's `main()` logic into a handler function
   - Each handler: `def handle(data: dict) -> tuple[int, str]` (exit_code, stdout)
   - Register all handlers in the daemon's routing table

3. **Phase 3: Dispatch script** (~15 min)
   - `hook_dispatch.py`: thin TCP client, fallback to subprocess
   - Test with one hook first (session-stats — safest, async)

4. **Phase 4: Settings migration** (~15 min)
   - Rewrite `settings.local.json` to point all hooks at dispatch.py
   - Verify each hook type works (PreToolUse blocking, PostToolUse async, UserPromptSubmit response)

5. **Phase 5: Startup integration** (~10 min)
   - Add daemon startup to `tools/shortcuts/start_all.bat`
   - SessionStart hook bootstraps daemon if not running
   - Test cold start → first hook latency

### Testing

Use the existing `test-hooks.py` harness:
```bash
python .claude/hooks/test-hooks.py
```

Also test manually:
```bash
# Start daemon
python .claude/hooks/hook_daemon.py &

# Test dispatch
echo '{"hook_event_name":"PostToolUse","tool_name":"Edit","tool_input":{"file_path":"test.cpp"}}' | python .claude/hooks/hook_dispatch.py

# Health check
python .claude/hooks/hook_dispatch.py --health
```

### Files You Own

- `.claude/hooks/hook_daemon.py` (NEW)
- `.claude/hooks/hook_dispatch.py` (NEW)
- `.claude/hooks/hook_handlers/` (NEW directory)
- `.claude/hooks/hook_handlers/__init__.py`
- `.claude/hooks/hook_handlers/*.py` (one per existing hook, refactored)
- `.claude/settings.local.json` (rewrite hooks entries)

### Files You Must NOT Touch

- `~/.claude/settings.json` (user settings — owned by main tab)
- `.claude/settings.json` (project settings — just cleaned up)
- Any file outside `.claude/hooks/` and `.claude/settings.local.json`
- Legacy hook scripts — keep them as fallback. Don't delete until daemon is proven.

### Special Cases

1. **`cowork sync_bridge.py`** (SessionEnd) — This calls an EXTERNAL script at `C:/Users/atayl/cowork/sync_bridge.py --full`. The daemon should shell out to it, not try to import it.

2. **`notification-toast.py`** — Uses BurntToast PowerShell module. The daemon handler should shell out to PowerShell for the toast, not try to do it in-process.

3. **`precompact-snapshot.py` and `compact-reinject.py`** — These are a two-stage pipeline. The daemon should ensure they share state (snapshot writes a file, reinject reads it).

4. **Exit code 2** — In PreToolUse hooks, exit code 2 means "BLOCK this action." The daemon MUST propagate this correctly through dispatch.py.

5. **UserPromptSubmit stdout** — These hooks return JSON to modify the prompt (`additionalContext` field). The daemon must return this JSON verbatim.

### Done Criteria

- [ ] Daemon starts and stays running
- [ ] All 20 hooks work through dispatch.py (test each)
- [ ] PreToolUse exit-code-2 blocking works (test sql-safety with `DROP TABLE`)
- [ ] UserPromptSubmit context injection works (test with "build error" prompt)
- [ ] Fallback works when daemon is stopped
- [ ] Latency measured: <10ms per dispatch vs old ~100ms baseline
- [ ] `test-hooks.py` passes
- [ ] No regressions: start a real Claude Code session and verify hooks fire

### Context References

- Hook protocol docs: Claude Code hooks use stdin JSON / stdout JSON / exit code. See existing scripts for protocol.
- Memory: `memory/claude-code-optimization.md` — has hook system overview
- Memory: `memory/claude-code-internals.md` — has hook lifecycle events
- Internals reports: `AI_Studio/Reports/ClaudeCodeInternals/` — deep architecture docs
- Published repos: 7 hook repos at github.com/VoxCore84 — reference implementations

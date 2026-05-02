---
name: MCP server fixes must be testable without restart
description: User has had to restart Claude Code 3+ times for docs-rag MCP fixes. Cache expensive init at module level, test via direct Python before claiming fixed.
type: feedback
originSessionId: 1beeeb4d-0ef0-4ba6-ab84-7011e3041e6d
---
MCP server code changes that crash the server force a full Claude Code tab restart — there's no way to reconnect a dead MCP server mid-session.

**Why:** User restarted the tab 3+ times for docs-rag fixes (sessions 247-248). Each restart loses conversation context and costs several minutes.

**How to apply:**
1. When writing MCP servers, cache expensive initialization (DB connections, large file opens) at module level — don't re-init on every tool call
2. Always test MCP logic changes via direct Python import (`sys.path.insert + import module`) BEFORE telling the user to restart
3. If a fix requires MCP restart, batch ALL fixes into one restart — don't ship partial fixes that need another restart
4. ChromaDB PersistentClient on 280MB+ databases takes 30-120s cold — always cache the client/collection object
5. **CRITICAL (Python 3.14):** Never `import chromadb` lazily inside a tool function. ChromaDB's import chain pulls in opentelemetry which touches `asyncio.iscoroutinefunction` — this deadlocks with anyio's event loop when the import runs in a thread pool. Always import chromadb at MODULE level (before the event loop starts). Same likely applies to any heavy package that touches asyncio internals.
6. **Use `from mcp.server.fastmcp import FastMCP`** (official SDK, mcp 1.26.0), NOT `from fastmcp import FastMCP` (standalone fastmcp 3.0.2). The standalone package has broken anyio integration on Python 3.14. The official SDK is what voxcore-db/voxcore-server use and it works.

## Event Loop Blocking — Investigated 2026-04-11

**Both** FastMCP variants (third-party `fastmcp` 3.0.2 and official `mcp.server.fastmcp`) auto-wrap sync tool functions in `anyio.to_thread.run_sync()`. So blocking calls (`subprocess.run`, `time.sleep`, heavy I/O) in tools do NOT block the event loop for FastMCP-based servers.

**The one exception:** `voxcore-server` uses raw `mcp.server.Server` + `stdio_server()`. Its `call_tool()` called sync `_dispatch()` directly on the event loop — `subprocess.run(build, timeout=600)` blocked the entire event loop for 10 minutes. **Fixed 2026-04-11** by wrapping `_dispatch` in `asyncio.to_thread()`.

**Hardening applied to all 9 Python MCP servers:**
- `line_buffering=True` on `sys.stderr.reconfigure()` — prevents 8KB block-buffered log output on Windows
- `PYTHONUTF8=1` in all `.claude.json` and `.mcp.json` registrations — prevents cp1252 encoding errors before Python runtime reconfigure runs

**Claude Code MCP timeout settings** (in `~/.claude/settings.json`):
- `MCP_TIMEOUT=60000` — server startup handshake
- `MCP_TOOL_TIMEOUT=120000` — per-tool-call execution deadline (no per-server override possible)
- `MCP_CONNECTION_NONBLOCKING=1` — sessions start even if slow servers are still connecting
- Claude Code does NOT auto-reconnect stdio servers after disconnect

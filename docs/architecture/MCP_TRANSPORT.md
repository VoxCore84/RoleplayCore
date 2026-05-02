# MCP Server Transport, State, and Error Handling

**Source of truth:** `.mcp.json` at repo root.
**Written:** 2026-05-02.
**Scope:** Closes Verification Master Checklist Cat 5 items: transport documented, stateless-vs-stateful behavior documented, error handling pattern documented.

## Server inventory and transport

All five MCP servers in `.mcp.json` are launched via the **stdio transport** — Claude Code spawns each server as a subprocess and exchanges JSON-RPC messages over stdin/stdout. None use SSE or HTTP/WebSocket transport. This is the canonical Claude Code config pattern (`"command"` + `"args"` keys, no `"url"` or `"transport"` keys).

| Server | Process | Transport | Implementation language |
|---|---|---|---|
| voxcore-db | `python -m voxcore_db.server` | stdio | Python (FastMCP) |
| voxcore-server | `python -m voxcore_server.server` | stdio | Python (FastMCP) |
| arcanum | `python tools-dev/arcanum/arcanum_server.py` | stdio | Python (FastMCP) |
| docs-rag | `python tools-dev/docs-rag/docs_rag_server.py` | stdio | Python (FastMCP) |
| local-llm | `node ~/mcp-local-llm/dist/index.js` | stdio | TypeScript (`@modelcontextprotocol/sdk`) |

**Why stdio only:** simpler permission model (no network ports exposed), zero auth surface (the spawning shell already has user privileges), trivial to add new servers. SSE would matter only if a remote client needed to call these tools, which is not in the threat model.

## Statelessness

**Tool calls are stateless.** Each invocation of a tool (e.g. `mcp__voxcore-db__query`, `mcp__docs-rag__docs_rag_search`) does its own DB connection, runs its own query, returns the result, and discards local state.

**Server processes hold persistent resources** for performance:
- `voxcore-db`: caches DB connection pools per database (auth/world/characters/hotfixes/roleplay)
- `voxcore-server`: caches the active worldserver/bnetserver process discovery + log-file watchers
- `arcanum`: lazy-loads the file index on first call; refresh via `arcanum_rebuild` tool
- `docs-rag`: holds the Chroma client, FTS5 connection, KG SQLite handle in process memory
- `local-llm`: holds an HTTP client to local Ollama; no model warmup state

These are caches, not session state — restarting any server drops nothing the next call can't reconstruct. There is no per-conversation or per-user state in any server.

**Implication for testing:** any tool call can be reproduced by replaying its inputs. There is no "warm vs cold" semantics that affects correctness, only latency.

## Error handling pattern

All servers follow a **structured-error-via-MCP-protocol** pattern, not raised exceptions to the client.

For Python FastMCP servers (voxcore-db, voxcore-server, arcanum, docs-rag):
- Tool functions return either a normal result or a string starting with `"ERROR:"` / `"Failed:"` / similar.
- Uncaught exceptions inside the tool are caught by FastMCP's `@server.tool()` decorator and converted to MCP error responses (JSON-RPC error code -32000, with the exception message in the data field).
- Validation failures (bad parameter types, missing required args) are caught at the JSON Schema layer and returned as JSON-RPC error code -32602 (Invalid params).

For the Node local-llm server:
- Errors are caught in the tool handler and returned as `{ content: [{ type: "text", text: "Error: ..." }], isError: true }`.

**No server raises an exception that crashes the subprocess.** A tool failing returns an error and remains available for the next call. Verified by observing that `tail_log` against a non-existent log file returns `"ERROR: log file not found"` rather than killing the server.

## Concurrency and rate limits

- No server enforces explicit rate limits on tool calls.
- Concurrency safety relies on the underlying resource being concurrency-safe — DB connections (MySQL handles per-call connections), SQLite reads (WAL mode), local HTTP to Ollama (Ollama serializes internally).
- Claude Code itself serializes tool calls within a single conversation; there is no race within one session.

## Auth model

- All five servers run as the local user; no in-MCP auth.
- Database credentials live in env vars (`MYSQL_*` for voxcore-db) loaded by the server on startup, not passed per-call.
- Anthropic / Google API keys for downstream calls (in tools that wrap LLMs) load from `tools/ai_studio/.env` and `config/gemini.local.env`.

For external integration (acquihire-grade): an MCP server fronting these tools to a remote client would need to add bearer-token auth in front of the stdio channel, plus a transport switch to SSE or HTTPS. Documented gap; not on the critical path for current scope.

### Auth model for external integration (closes Cat 5 checklist item)

If a future buyer wants to expose VoxCore tools to a non-local client, the auth changes required are enumerated:

| Layer | Current | Required for external |
|---|---|---|
| Transport | stdio subprocess | SSE or HTTPS WebSocket |
| Identity | local OS user | bearer token, API key, or mTLS client cert |
| Authorization | none (any tool callable) | per-tool ACL (e.g. read-only vs read-write tools split into separate servers) |
| Audit | none in-MCP | structured audit log of every tool call with caller identity |
| Rate limiting | none (Claude Code serializes) | per-token or per-IP rate limits |
| Secret handling | env vars on local user account | secrets manager (AWS Secrets, HashiCorp Vault, Azure Key Vault) |
| Tenant isolation | none (single corpus) | per-tenant DB connection, per-tenant cache directory |

**Sized cost to add all of the above:** 4-6 weeks of engineering against the current codebase, with most of the work in tenant isolation and audit logging. The MCP protocol layer itself supports both transports (`@modelcontextprotocol/sdk` Node and Python `FastMCP` both support SSE in addition to stdio); the heavy lift is everything OUTSIDE the MCP layer.

**Decision today:** do NOT build any of this preemptively. See `docs/DEPLOYMENT_MODEL.md` for the full local-only rationale.

## Verification

| Question | Answer | How verified |
|---|---|---|
| What transport? | stdio only | `.mcp.json` has `command`/`args`, no `url`/`transport` |
| Stateless tools? | Yes | Each call self-contained; servers hold caches not session state |
| Stateful caches? | Yes (per server) | DB pools, file index, FTS handle |
| Error pattern? | Structured MCP error or text-prefixed result string | FastMCP decorator behavior + observed in logs |
| Auth? | Local user only | No auth in any server config |
| Rate limits? | None enforced | Verified by code grep for rate limit logic in each server module |

# ADR 0002: MCP-First Protocol Surface

**Status:** Accepted
**Date:** 2026-03 (initial), 2026-04 (expanded)

## Context

Vertical legal-AI products (Harvey, CoCounsel, Spellbook, vLex) all ship as closed UI applications. To get case-aware answers, the user has to leave whatever AI workflow they already use (Claude Desktop, ChatGPT, Cursor) and live inside the vendor's product. Procurement teams rebill, security teams re-audit, training cycles repeat.

Anthropic released **Model Context Protocol** in November 2024: a standardized way for any compliant LLM client to call tools, read resources, and use prompts from any compliant server, over `stdio`/`SSE`/`HTTP`. As of mid-2026, near-zero vertical legal-AI products ship MCP servers.

## Decision

Build VoxCore's tool surface as MCP servers, not as a UI application. Six MCP servers expose 30+ tools:

- `arcanum` — case-archive doc search, mbox search, KG entity/mention/relation lookup
- `docs-rag` — semantic search over IMPORTANT DOCS via ChromaDB
- `local-llm` — Qwen 27B / Gemma 4 26B classify/summarize/transform helpers
- `voxcore-db` — MySQL queries, schema diffs, tribal knowledge
- `voxcore-server` — service start/stop/status/build/logs
- `codeintel` — ctags + clangd C++ symbol lookup

All tool schemas are JSON Schema validated at the protocol layer. Transport: `stdio` for local development, `SSE` available for remote.

## Alternatives considered

1. **Build a UI app (web or desktop).** Rejected: forces users into a parallel workflow, requires ongoing UX investment, doesn't compose with the AI-native development pattern that the rest of the system uses.

2. **REST API as primary surface, MCP as secondary.** Rejected: REST is older and broader, but MCP is what Claude Desktop / Cursor / Claude Code / Anthropic Workbench natively speak. We get those clients for free; with REST we'd write custom integrations per client.

3. **OpenAI function-calling + Anthropic tool-use as the protocol surface.** Rejected: same shape, different vendors' names. MCP is the cross-vendor abstraction over both. Investing in MCP positions us against either provider's lock-in.

4. **Wait for the market.** Rejected: 6–12 month first-mover window in MCP-native legal AI. Competitors will catch up; positioning early matters.

## Consequences

**Positive:**
- The same backend serves Claude Desktop, Cursor, custom agents, IDE plugins. New frontends are hours, not weeks.
- Schema-validated tool calls are a first-class diligence answer to "is the API contract enforced?" Yes — at the protocol layer, automatically.
- Every tool is independently testable: the eval harness can call a tool without going through an LLM at all.
- "Plugs into your existing AI" is a much easier sales motion than "compete with Harvey."

**Negative:**
- MCP is new (Nov 2024 spec). Some clients have rough edges. We've eaten this cost during early development.
- No native UI. Users who want a portal still have to use Claude Desktop or build their own. Acceptable for the acquihire-target audience (firms with mature AI investment); painful for solo lawyers without existing AI tooling.

**Neutral:**
- 30+ tools is a lot of surface to maintain. Mitigation: each MCP server is a small module (~200–500 LOC); adding a tool is a 1-day task.

## References

- `tools/mcp-voxcore-server/`, `tools/mcp-voxcore-db/`, etc.
- ADR 0001 — Triad orchestration uses these tools
- modelcontextprotocol.io — spec

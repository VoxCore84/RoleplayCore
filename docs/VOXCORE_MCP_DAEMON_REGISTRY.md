# VoxCore — MCP Server & Daemon Registry
**Last updated:** 2026-05-26
**Status:** DOCUMENTATION ONLY — no server started, restarted, or modified.

---

## WARNING: DO NOT DUPLICATE OR RESTART RUNNING SERVICES

**Before adding any new MCP server or daemon:**
1. Check this document for existing coverage.
2. Verify the target entrypoint is not already running.
3. The hook daemon serves ALL tabs AND CalmCore via symlink — an unplanned restart disrupts every active session.
4. If you think you need a new server, confirm it does not overlap with the 5 already configured.

---

## Part 1 — MCP Servers (5 configured, all LIVE)

Configuration source: `.mcp.json` (repo root). All servers have `alwaysLoad: true`.
Settings-level allows: `.claude/settings.json` line 28 (`mcp__local-llm__*`) and lines 22–27 (explicit allows for the other four).

### 1.1 voxcore-db

| Field | Value |
|-------|-------|
| **Entrypoint** | `python -m voxcore_db.server` |
| **Source dir** | `tools/mcp-voxcore-db/src/voxcore_db/` |
| **PYTHONPATH** | `tools/mcp-voxcore-db/src` |
| **Tools exposed** | 6: `query`, `describe`, `schema_diff`, `safe_apply`, `column_check`, `tribal_knowledge` |
| **Health check** | Connect via MCP; no separate HTTP endpoint. Verify via `mcp__voxcore-db__query` with `SELECT 1`. |
| **What uses it** | `/sql-pipeline`, `/cc-updates` skills; settings.json hook chains on `safe_apply` (PostToolUse: auto-tail dberrors) and `query`/`safe_apply` failure (PostToolUseFailure: tribal_knowledge + db-failure-chain). |
| **Known gaps** | No README in source dir. `tribal.py` holds knowledge inline (no JSON file). |
| **Duplicate risk** | LOW — only DB query/schema tool in the stack. |

### 1.2 voxcore-server

| Field | Value |
|-------|-------|
| **Entrypoint** | `python -m voxcore_server.server` |
| **Source dir** | `tools/mcp-voxcore-server/src/voxcore_server/` |
| **PYTHONPATH** | `tools/mcp-voxcore-server/src` |
| **Tools exposed** | 8: `status`, `start`, `stop`, `restart`, `soap`, `tail_log`, `watch_log`, `build` |
| **Health check** | `mcp__voxcore-server__status` (no separate HTTP endpoint). |
| **What uses it** | `/check-logs`, `/soap`, `/build-loop`, `/parse-errors` skills; settings.json hook chains on `restart`/`start` success (PostToolUse: auto-tail server log), build success (PostToolUse: tail dberrors), `start`/`restart` failure (PostToolUseFailure: tail + server-failure-chain), build failure (PostToolUseFailure: build-failure-chain). Hook daemon sets 600s timeout for `build` tool (`.claude/hooks/hook_daemon.py:997`). |
| **Known gaps** | No README. |
| **Duplicate risk** | LOW — only server control tool in the stack. |

### 1.3 arcanum

| Field | Value |
|-------|-------|
| **Entrypoint** | `python tools-dev/arcanum/arcanum_server.py` |
| **Source dir** | `tools-dev/arcanum/` |
| **Key env vars** | `CASE_DIR` (gitignored path), `IMPORTANT_DOCS_DIR` (gitignored path), `MBOX_DB_PATH` (gitignored path) — values set in `.mcp.json` but omitted here per no-personal-paths policy |
| **Tools exposed** | 9: `arcanum_search`, `arcanum_read`, `arcanum_index`, `arcanum_lookup`, `arcanum_rebuild`, `arcanum_reload`, `arcanum_mbox_search`, `arcanum_mbox_read` + hot-reload capability |
| **Health check** | Call `mcp__arcanum__arcanum_index` with empty folder arg — returns top-level tree if live. |
| **What uses it** | `/ex-ask`, `/ex-sme`, `/ex-status`, `/ex-posture`, `/search-docs`, `/sme-sweep` and 3 additional skills that reference `mcp__arcanum__*` (9 command files total). |
| **Retrieval layer** | FTS5 keyword search over wiki/memory/reports/case content + SQLite mbox FTS5. Does NOT do vector search. |
| **Known gaps** | No README. `arcanum_mbox_search` returns only headers (empty body) for deleted-then-archived messages — false confidence risk (see excluded-corpus.md gotcha #1). |
| **Duplicate risk** | NONE with docs-rag. arcanum = keyword/FTS5; docs-rag = vector/KG. `/ex-ask` intentionally fans out to both. |

### 1.4 docs-rag

| Field | Value |
|-------|-------|
| **Entrypoint** | `python tools-dev/docs-rag/docs_rag_server.py` |
| **Source dir** | `tools-dev/docs-rag/` |
| **Tools exposed** | 10: `docs_rag_search`, `docs_rag_read`, `docs_rag_list`, `docs_rag_status`, `docs_rag_rebuild`, `docs_rag_reload`, `kg_entity`, `kg_mentions`, `kg_relations`, `kg_stats` |
| **Health check** | Call `mcp__docs-rag__kg_stats` — returns entity/mention/relation counts if live. Current: ~24,640 entities / 175,793 mentions / 743,207 relations. |
| **What uses it** | Same `/ex-*` skills as arcanum + `/rag-search`, `/kg-query`. KG tools wire to `.cache/excluded_kg.db` via `tools.excluded_daemon.kg.query` (import at `docs_rag_logic.py:602–682`). |
| **Retrieval layer** | ChromaDB vector similarity (nomic-embed-text, 768-dim) + KG entity/relation traversal. Does NOT do FTS5 keyword search. |
| **Known gaps** | No README. The fused hybrid pipeline (`tools/excluded_hybrid_search.py` — FTS5 + vector + KG RRF) has NO MCP wrapper — it is CLI-only, subprocess-called from `/ex-ask`. This is a confirmed gap; the docs-rag server exposes vector-only, not the fused stack. |
| **Duplicate risk** | NONE with arcanum (complementary layers). Do not merge — would degrade retrieval. |

### 1.5 local-llm

| Field | Value |
|-------|-------|
| **Entrypoint** | `node C:/Users/atayl/mcp-local-llm/dist/index.js` |
| **Source repo** | External: `C:/Users/atayl/mcp-local-llm/` (not in VoxCore tree) |
| **Model config** | `qwen3.5:27b-q4_K_M` via Ollama at `http://localhost:11434/v1`; 4096 max tokens; temp 0.3 |
| **Tools exposed** | 6: `local_summarize`, `local_classify`, `local_extract`, `local_draft`, `local_transform`, `local_complete` |
| **Health check** | Call `mcp__local-llm__local_status` — returns model info if Ollama is running. |
| **What uses it** | `/ex-absorb`, `/ex-ask`, `/ex.md` skills; mandated by `excluded-corpus.md` for triage/classification tasks (local, $0 cost). |
| **Known gaps / config drift** | Absent from `enabledMcpjsonServers` in `.claude/settings.local.json` (lists only voxcore-db, voxcore-server, arcanum, docs-rag). Works anyway via `settings.json` line 28 wildcard allow (`mcp__local-llm__*`). Fix: add `"local-llm"` to `enabledMcpjsonServers` in `settings.local.json` — hygiene only, no functional impact. |
| **Duplicate risk** | LOW — only local-LLM inference tool. Do not spin up a second Ollama-backed server. |

### 1.6 Hybrid Retrieval MCP Gap

The production RRF-fused hybrid retrieval pipeline (`tools/excluded_hybrid_search.py`: FTS5 + ChromaDB + KG entity boost at k=60, 92.0% baseline) has **no MCP wrapper**. It is invoked via `Bash(python tools/excluded_hybrid_search.py "query")` inside the `/ex-ask` skill.

This is a confirmed gap. Future work: wrap as an additional tool in docs-rag or a dedicated server. See `docs/VOXCORE_GRAPH_RAG_READINESS.md` section 2 for why the existing tools do not cover this.

---

## Part 2 — Hook Daemon (v1.3.0)

### 2.1 Overview

| Field | Value |
|-------|-------|
| **File** | `.claude/hooks/hook_daemon.py` |
| **Version** | v1.3.0 |
| **At inventory (2026-05-26)** | PID 34224, ~21h uptime, `in_flight=0` |
| **Health check** | `curl -s http://127.0.0.1:19484/health` → `{"status": "ok", "version": "1.3.0", "routes": 25, "in_flight": N}` |
| **Route count** | 25 routes in `ROUTE_TABLE` |
| **Why it exists** | Replaced 38 individual subprocess hooks with a single persistent HTTP server (~127× latency improvement, per Stack Reference L2). Serves all VoxCore tabs and CalmCore via symlink. |
| **CalmCore symlinks** | 4 symlinks in `CalmCore/.claude/hooks/` point to VoxCore: `hook_daemon.py`, `daemon_shim.py`, `compact-reinject.py`, `deadline-alert.py`. Any change to these files affects both projects. |

### 2.2 Hook Events Wired in settings.json

The following hook matchers are wired to the daemon (source: `.claude/settings.json`):

| Event | Matcher | Daemon Route |
|-------|---------|-------------|
| UserPromptSubmit | (all) | `/hook/timestamp-injector`, `/hook/prompt-context-injector` |
| PreToolUse | `CronCreate` | `/hook/block-recurring-cron` |
| PreToolUse | `Bash` | `/hook/sql-safety`, `/hook/release-gate-enforce` |
| PreToolUse | `Edit\|Write` | `/hook/sensitive-file-guard` |
| PreToolUse | `Read` | `/hook/large-file-guard` |
| PreToolUse | `Edit\|Write` | `/hook/tab-ownership-check` |
| PostToolUse | `Edit` | `/hook/edit-verifier`, `/hook/cpp-build-reminder` |
| PostToolUse | `Write\|Edit` | `/hook/release-gate-revalidate` |
| PostToolUse | (all) | `/hook/session-stats` |
| PostToolUse | `Bash` | `/hook/sync-on-git` |
| PostToolUse | `Grep` | `/hook/grep-case-enricher` |
| PostToolUse | `mcp__voxcore-server__restart\|start` | (mcp_tool chain — tail_log, not daemon HTTP) |
| PostToolUse | `mcp__voxcore-db__safe_apply` | (mcp_tool chain — tail_log, not daemon HTTP) |
| PostToolUse | `mcp__voxcore-server__build` | (mcp_tool chain — tail_log, not daemon HTTP) |
| PostToolUseFailure | (all) | `/hook/session-stats` |
| PostToolUseFailure | `Read` | `/hook/docx-auto-extract` |
| PostToolUseFailure | `mcp__voxcore-db__query\|safe_apply` | tribal_knowledge chain + `/hook/db-failure-chain` |
| PostToolUseFailure | `mcp__voxcore-server__start\|restart` | tail_log chain + `/hook/server-failure-chain` |
| PostToolUseFailure | `mcp__voxcore-server__build` | `/hook/build-failure-chain` |
| SessionStart | (all) | `daemon_shim.py --ensure` (subprocess, not HTTP) |
| SessionStart | `compact` | `compact-reinject.py` (subprocess) |
| SessionEnd | (all) | `/hook/cowork-sync` |
| Stop | (all) | `/hook/stop-verify`, `/hook/cowork-sync`, `/hook/session-stats` |
| SubagentStart | (all) | `/hook/session-stats` |
| SubagentStop | (all) | `/hook/subagent-complete` |
| ConfigChange | (all) | `/hook/session-stats` |
| PreCompact | (all) | `/hook/precompact-snapshot` |
| Notification | (all) | `/hook/notification-toast` |
| FileChanged | `session_state.md\|Central_Brain.md\|todo.md` | UNKNOWN — settings.json read was truncated at this point; assumed wired to a daemon route |

Additionally, `PreToolUse → Write` wires `check_write_size.py` as a subprocess (not HTTP).
`PreToolUse → Write|Edit` with `*publishable*` pattern uses a `prompt`-type hook (not HTTP).

Total distinct HTTP route calls in settings.json: approximately 13 unique daemon routes wired.

### 2.3 Dormant Routes

| Route | Status | Notes |
|-------|--------|-------|
| `/hook/sql-write-monitor` | DORMANT — in ROUTE_TABLE, not wired in settings.json | Log-only when promoted. Promotion step documented at `AI_Studio/Reports/pictures1_ingest/HOOKS_PROMOTION_REPORT.md` § `.sql-write monitor`. Isolation-verified 2026-05-25. |
| CC-05 breadcrumb (`_subagent_complete_work`) | DORMANT in running process | Code added at commit `5e93222f62`; running pid 34224 predates commit. Activates automatically on next natural daemon reload via SubagentStop → `/hook/subagent-complete`. No settings change needed. |

### 2.4 Reload / Promotion Procedure

The daemon self-heals on each `SessionStart` via `daemon_shim.py` (`--ensure` flag). This means:

- **CC-05 breadcrumb** activates automatically the next time any Claude Code session starts in VoxCore or CalmCore. No manual action needed.
- **sql-write-monitor promotion:** Add a `PostToolUse` matcher block to `.claude/settings.json` (full block documented in `HOOKS_PROMOTION_REPORT.md` § `.sql`-write monitor). Do this only when no other tab is active and in_flight=0 at time of check.

**Deliberate reload (when needed):**
1. Verify `in_flight=0` at `http://127.0.0.1:19484/health`
2. Kill the running process: `taskkill /F /PID <pid>` (Windows) or note it self-heals on next SessionStart
3. Open a new Claude Code session — `daemon_shim.py` restarts it automatically
4. Verify new PID at `/health`
5. Run `/sync-infra` to confirm CalmCore parity

### 2.5 Rollback Procedure

- **CC-05 breadcrumb:** Delete the `# CC-05:` try/except block in `_subagent_complete_work` in `hook_daemon.py`. It is additive and exception-wrapped — worst case it is a no-op. Rollback is instant on next reload.
- **sql-write-monitor:** Remove the `PostToolUse` matcher block from `settings.json`. Takes effect immediately (no daemon restart needed for settings changes). Optionally delete the handler and route entry from `hook_daemon.py` as cleanup.
- **Any hook change:** Settings-level hook changes take effect on next prompt submit. Daemon code changes require daemon reload (next SessionStart). Keep both in sync via `/sync-infra`.

---

## Part 3 — Excluded-Corpus Daemon

| Field | Value |
|-------|-------|
| **Source dir** | `tools/excluded_daemon/` |
| **Architecture** | Asyncio job pipeline: index_worker, KG build (`kg/build.py`), router, ChromaDB embed, FTS5 index |
| **Status** | PARTIAL — 6 known reliability issues |
| **Backlog** | `SL_Vault/03b_Layer_Formalization_Closeouts/DAEMON_RELIABILITY_BACKLOG.md` (291 lines) |
| **Known issues (summary)** | Stale schema.sql fire; MySQL auto-start; noisy reminders; validate_schemas clobber; snapshot/run filename collision; no project healthcheck |
| **Relationship to hook daemon** | Separate process. The hook daemon is `.claude/hooks/hook_daemon.py` (HTTP, port 19484). The excluded-corpus daemon is `tools/excluded_daemon/` (asyncio, no HTTP port). They do not share code or ports. |
| **Action** | Leave alone. Consult backlog before any daemon work. Do not attempt to fix the 6 issues without reading the backlog first. |
| **CalmCore exposure** | None — this daemon has no CalmCore symlinks. |

---

## Part 4 — Consolidated Gap List

| Gap | Priority | Risk of touching |
|-----|----------|-----------------|
| `local-llm` missing from `enabledMcpjsonServers` in `settings.local.json` | LOW — hygiene, no functional impact | Negligible |
| Hybrid retrieval (`excluded_hybrid_search.py`) has no MCP wrapper | MEDIUM — new capability | Moderate (dep design needed) |
| No README for voxcore-db, voxcore-server, arcanum, docs-rag | LOW — docs only | None |
| Excluded-corpus daemon: 6 reliability issues | MEDIUM — operational risk | Consult backlog |
| sql-write-monitor route unwired | LOW — awaiting one clean pass | Low |

---

## References

- `.mcp.json` — server configuration (repo root)
- `.claude/settings.json` — hook wiring and MCP permissions
- `.claude/settings.local.json` — `enabledMcpjsonServers` list (4 of 5)
- `.claude/hooks/hook_daemon.py` — v1.3.0, 25 routes
- `.claude/hooks/daemon_shim.py` — self-heal shim (SessionStart)
- `AI_Studio/Reports/system_inventory_2026-05-26/cat_B_mcp.md` — full MCP inventory evidence
- `AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` — Category C daemon section
- `AI_Studio/Reports/pictures1_ingest/HOOKS_PROMOTION_REPORT.md` — dormant route promotion steps
- `tools/excluded_daemon/kg/build.py:411` — KG relation INSERT (only route into entity_relations)

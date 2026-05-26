# VoxCore Architecture Map

**Last updated:** 2026-05-26
**Source reports (gitignored):** `AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md`, `BUILD_VS_IMPROVE_DECISION.md`, `cat_A/B/D_*.md`
**Cross-references:** `docs/architecture/CHUNKING_STRATEGY.md`, `docs/architecture/MCP_TRANSPORT.md`, `docs/architecture/decisions/0001–0007`

---

## Do NOT Rediscover

Before proposing any new system, confirm you have checked this list. Every item below already exists — proposals to "add" any of these are duplicates.

**Already built and live:**
- RAG retrieval: ChromaDB vector store (477 MB, ~24,930 chunks, nomic-embed-text 768-dim)
- FTS5 keyword index (173 MB, ~20,807 chunks, SQLite BM25)
- Knowledge Graph (272 MB, 24,640 entities, 743,207 relations)
- Hybrid retrieval: FTS5 + vector + KG entity-match, RRF fused, 92% measured baseline (`tools/excluded_hybrid_search.py`)
- MCP servers: 5 live servers, 33 tools total (voxcore-db, voxcore-server, arcanum, docs-rag, local-llm)
- Daemon infrastructure: hook_daemon.py (25 routes) + excluded-corpus daemon (asyncio)
- Named agents: 28 in `.claude/agents/`
- Named skills: 79 in `.claude/commands/`
- Named rules: 16 in `.claude/rules/`
- Self-improvement loop: `tasks/lessons.md` (wired to session-start)
- Session memory persistence: local-only git + `last_verified` frontmatter + Task Scheduler

**Already built, dormant/unwired:**
- Model gateway: `tools/model_router.py` + `tools/anthropic_helpers.py` (zero importers)
- Backend decision matrix: `config/backend_selection.yaml` (390-line, inert + untracked)
- Memory Control Plane v0.1: `tools/memory_schema.py`, `tools/memory_context.py`, `tools/memory_fix_proposals.py`, `tools/agent_task_ledger.py` (committed on `feature/ai-harvest-quick-wins`, not merged)

**NOT yet built (do not claim these exist):**
- Production GraphRAG: `graphrag/PLAN.md` is a scaffold with zero production code
- Typed KG edges: all 743K relations are `predicate='mentioned_with'` (`kg/build.py:411`)
- Contradiction detection: `contradiction/PLAN.md` is a scaffold, blocked on typed edges
- MCP wrapper for the fused hybrid stack: CLI-only today
- Batch API on eval sweeps (real cost lever, not built)
- Live retrieval telemetry
- Off-machine case-archive backup

---

## 1. Main Layers

VoxCore maps onto the Ultrathink 13-layer + Anthropic "Building Effective Agents" framing documented in `AI_Studio/Reports/system_inventory_2026-05-26/DESKTOP_SOURCE_SUMMARY.md` (from `VoxCore_Stack_Reference.md`). The relevant layers for the current system are:

| Layer | Name | VoxCore status |
|-------|------|---------------|
| L3 | Data / Semantic | STRONG: FTS5 + ChromaDB + KG all live |
| L6 | Tools / MCP | LIVE: 5 servers, 33 tools. Gap: no hybrid-stack MCP wrapper |
| L8 | Model Gateway | GAP: router + helpers built but unbanked (zero importers) |
| L11 | Eval | STRONG (offline): 92% baseline, reproducible provenance |

The remaining Ultrathink layers (cloud infra, durable execution, multi-user ACL, autonomous loops) are intentional non-implementations per `VoxCore_Stack_Reference.md`.

---

## 2. What is Live Today

### Retrieval stack (triple-channel hybrid)

Three independent indexes feed one retrieval pipeline:

```
FTS5 index (.cache/excluded_fts.db, 173 MB)        ─┐
ChromaDB vector (.cache/rag/chroma/, 477 MB)         ├─► RRF fusion (k=60) ─► top-K results
KG entity-match (.cache/excluded_kg.db, 272 MB)     ─┘          │
                                                               2.0x entity-path boost
```

Each index is built with its own chunker (different sizes, tuned per consumer — see `docs/architecture/CHUNKING_STRATEGY.md`):

| Index | Chunk size | Overlap | Strategy |
|-------|-----------|---------|----------|
| FTS5 | 2400 chars | 400 chars | Fixed-size, whitespace boundary |
| Vector | 600 tokens | 100 tokens | Fixed-size, sentence boundary |
| KG NER | 2000 chars | 200 chars | Fixed-size, no boundary handling |

Decision record: `docs/architecture/decisions/0007-hybrid-retrieval-rrf.md`. Baseline: 92.0% (run_id `43b4e9ba4752a6fc`).

### MCP fleet (5 servers, stdio transport)

All servers use stdio transport (spawned subprocesses, JSON-RPC over stdin/stdout). No SSE, no HTTP. See `docs/architecture/MCP_TRANSPORT.md`.

| Server | Tools | Role |
|--------|-------|------|
| voxcore-db | 6 | MySQL queries, schema inspection, SQL apply |
| voxcore-server | 8 | worldserver management, logs, build |
| arcanum | 9 | FTS keyword search over wiki/memory/reports/case; mbox |
| docs-rag | 10 | Vector search (ChromaDB) + KG tools (kg_entity, kg_mentions, kg_relations, kg_stats) |
| local-llm | 6 | Qwen 27B via Ollama, $0 cost — classify/extract/summarize/draft |

arcanum and docs-rag are **complementary, not duplicate**: arcanum = keyword/mbox; docs-rag = vector + KG graph traversal. `/ex-ask` fans out to both. Decision: `docs/architecture/decisions/0002-mcp-first-protocol.md`.

### Hook / daemon layer

Two separate daemons — frequently confused:

| Daemon | Path | Role |
|--------|------|------|
| hook_daemon.py v1.3.0 | `.claude/hooks/hook_daemon.py` | HTTP event router for Claude Code hook events (25 routes, ~13 wired). Replaced 38 subprocess hooks. Serves ALL tabs + CalmCore (4 symlinks). |
| excluded-corpus daemon | `tools/excluded_daemon/` | asyncio daemon that builds/maintains FTS5 + ChromaDB + KG indexes from the corpus. Separate process, separate purpose. |

Hook wiring is in `.claude/settings.json` (~13 events). Changes affect all tabs and CalmCore immediately.

### Agent / skill / rule layer

| Component | Count | Location |
|-----------|-------|----------|
| Named agents | 28 | `.claude/agents/` |
| Named skills | 79 | `.claude/commands/` |
| Rules | 16 (13 tracked, 3 untracked) | `.claude/rules/` |

Agents are spawned by skills via the Agent tool. Skills are entry points; agents are implementation. 4 overlap clusters among agents (consolidation candidates — do not retire without reading both CLAUDE.md files first).

---

## 3. Dormant-but-Promising

These systems are committed, tested, and functional, but have zero production wiring:

**Model gateway (L8 gap):**
- `tools/model_router.py` — resolves 16 operation types to a backend; reads `config/backend_selection.yaml`.
- `tools/anthropic_helpers.py` — cost estimator, cache-block builder, batch dry-run. Self-test passes.
- `config/backend_selection.yaml` — 390-line decision matrix. UNTRACKED (missing from git → broken on fresh checkout).
- Zero importers across the entire codebase. The start of an L8 gateway; requires one real call site to activate.

**Memory Control Plane v0.1:**
- `tools/memory_schema.py`, `tools/memory_context.py`, `tools/memory_fix_proposals.py`, `tools/agent_task_ledger.py`
- On `feature/ai-harvest-quick-wins` branch (commit `73c6d4c771`), not merged to master.
- All 4 tools are read-only / propose-only — low risk to wire.
- Complements (does not replace) `memory/*.md` + `tools/memory_staleness.py`.

**CC-05 SubagentStop breadcrumb:**
- Added to `hook_daemon.py:_subagent_complete_work` (commit 5e93222f62).
- Running daemon predates this commit. Activates on next natural reload — no action needed.

**SQL-write-monitor route:**
- Route present in hook_daemon.py ROUTE_TABLE. NOT wired in settings.json. Log-only when activated.
- Promote to settings.json when desired — low risk.

---

## 4. Scaffold-Only (Zero Production Code)

Do not describe these as built systems. They are design documents only:

| Scaffold | File | What it would do | Blocker |
|----------|------|-----------------|---------|
| GraphRAG | `graphrag/PLAN.md` | Leiden community detection + global synthesis queries over the KG | Typed KG edges (none today) + igraph (not installed) + Adam GO |
| Contradiction detection | `contradiction/PLAN.md` | Cross-source contradiction detection via typed predicates | Typed KG edges (none today) |
| Cascade retrieval | `retrieval/CASCADE_PLAN.md` | Cheap-first channel ordering to reduce latency ~2181 ms → ~400 ms | Entangled files reconciled + Adam GO |
| v2 gold set | `eval/datasets/v2_scaffold/EXECUTION_PLAN.md` | 1000-query gold set (vs v1's 50) | Adam GO + LLM budget |

The single upstream unlock for both GraphRAG and contradiction is **typed KG edges**: replacing the 743,207 `mentioned_with` relations with typed predicates (extracted via per-chunk triple extraction). This is a real build requiring batch-API budget and an A/B vs the 92% baseline.

---

## 5. Systems That Overlap or Duplicate

### arcanum vs docs-rag (NOT a duplicate — complementary)

arcanum handles keyword/mbox search over wiki + memory + case files. docs-rag handles vector similarity and KG graph traversal over the same corpus. `/ex-ask` explicitly fans out to both in parallel. Merging them would degrade one retrieval layer. Source: `cat_B_mcp.md` overlap analysis.

### Agent overlap clusters (consolidation candidates, not retired)

Four clusters of partially-overlapping agents identified in the 2026-05-26 inventory:

| Cluster | Agents | Safe to retire? |
|---------|--------|-----------------|
| Legal drafting | case-drafter, filing-drafter | No — read both CLAUDE.md files first |
| Claim verification | contradiction-finder, fact-checker | No — structural vs factual scope differ |
| PII detection | redaction-scanner, security-hygiene-sweeper | No — doc-level vs filesystem-level differ |
| Structural audit (3-way) | doc-auditor, grep-auditor, memory-path-auditor | No — consolidation candidate, not blind retire |

`dormant-project-watchdog` is the one agent with zero skill references — a genuine retirement candidate.

### Two dormant control planes

Both exist committed but unwired; both are additive (not replacements):
1. **Cost gateway** (E1/E2/E3): model_router + anthropic_helpers + backend_selection.yaml — start of L8.
2. **Memory Control Plane v0.1** (D6): schema/context/ledger/fix-proposals — start of dynamic memory routing.

Neither duplicates the other. Neither duplicates the existing memory corpus or lessons loop. Both need one wired call site to activate.

---

## 6. Terminology Glossary: What Each Term Actually Means Here

**RAG / KG-enhanced retrieval (current production path):**
The live triple-channel hybrid in `tools/excluded_hybrid_search.py`. FTS5 + ChromaDB vector + KG entity co-mention boost, fused via RRF. The KG is used as a signal (entity-match boost), not as a graph traversal. This is the system with the 92% baseline. CLI-only.

**KG (Knowledge Graph):**
The SQLite database at `.cache/excluded_kg.db`. 24,640 entities, 743,207 relations. All relations are `predicate='mentioned_with'` (co-occurrence). Entity resolution and co-mention — not semantic triples. Exposed via docs-rag MCP (`kg_entity`, `kg_mentions`, `kg_relations`, `kg_stats`).

**KG-enhanced retrieval vs true GraphRAG:**
KG-enhanced = entity co-mention boost as one of three RRF signals. True GraphRAG = multi-hop graph traversal + Leiden community detection + global synthesis queries. The former is live. The latter is a scaffold with zero production code and a hard upstream dependency on typed edges.

**Typed KG edges:**
Semantic predicate triples (subject→predicate→object) where predicate is something like `filed_with`, `employed_by`, `contradicts`. Does not exist — build.py only inserts `mentioned_with`. This is the single upstream unlock for both GraphRAG and contradiction detection.

**MCP wrappers:**
Claude Code tool surfaces exposed by MCP servers (stdio JSON-RPC). The 5 live servers expose 33 tools. The fused hybrid retrieval stack (`excluded_hybrid_search.py`) has NO MCP wrapper — it is subprocess-called from skills only. This is the Stack Reference L6 gap.

**Daemons vs hooks:**
- Daemons: long-running processes that build/maintain indexes (excluded_daemon) or route Claude Code events (hook_daemon).
- Hooks: event triggers in settings.json that fire on Claude Code lifecycle events (UserPromptSubmit, PostToolUse, etc.) and call the hook_daemon HTTP routes.
These are two separate systems that interact but are not the same thing.

**Memory Control Plane vs memory corpus:**
- Memory corpus: `memory/*.md` — session-read topic files, manually curated.
- Memory Control Plane v0.1: 4 tools that validate schema, rank memories by keyword relevance, propose fixes, track tasks. Propose-only, never auto-applies. Dormant — not merged to master.

---

## 7. What Future Sessions Should Check Before Proposing New Systems

1. **Check this document** — if the system is listed as LIVE or DORMANT here, it exists. Do not rebuild.
2. **Check `docs/VOXCORE_SYSTEM_REGISTRY.md`** — the per-system row with path, status, evidence, and do-not-touch notes.
3. **Check the inventory reports** at `AI_Studio/Reports/system_inventory_2026-05-26/` — ground truth verified 2026-05-26.
4. **Check `docs/architecture/decisions/`** — ADRs 0001–0007 document what was considered and rejected.
5. **The most common false-discovery pattern:** "We should add [RAG/KG/MCP/agents/hooks/lessons loop/cost router/memory control plane]." All of these already exist in some form. The question is whether to wire a dormant system or improve an existing one — not whether to build.
6. **The real open build questions are:**
   - Typed KG edges (upstream unlock for two scaffolds)
   - MCP wrapper for the fused hybrid stack (genuine gap)
   - Batch API adoption on eval sweeps (real cost lever)
   - Entanglement resolution: `excluded_hybrid_search.py` (+105), `citation_scorer.py` (+93), `quality_probe.py` (+23)
   - Committing 3 untracked rules + `config/backend_selection.yaml`

---

## Cross-References

| Topic | Document |
|-------|----------|
| Chunking strategy (FTS5 / vector / KG sizes) | `docs/architecture/CHUNKING_STRATEGY.md` |
| MCP transport, statelessness, error handling, auth | `docs/architecture/MCP_TRANSPORT.md` |
| Hybrid retrieval decision (RRF, k=60, entity boost) | `docs/architecture/decisions/0007-hybrid-retrieval-rrf.md` |
| Triad orchestration (ChatGPT/Gemini/Claude Code pipeline) | `docs/architecture/decisions/0001-triad-orchestration.md` |
| MCP-first protocol (why MCP over direct API) | `docs/architecture/decisions/0002-mcp-first-protocol.md` |
| Local GPU offload (Ollama, which models run local) | `docs/architecture/decisions/0003-local-gpu-offload.md` |
| Governance gate (pre-ship, release-gate) | `docs/architecture/decisions/0004-governance-gate.md` |
| Citation precision pipeline | `docs/architecture/decisions/0005-citation-precision-pipeline.md` |
| PDF extraction choice (pdfplumber/pypdfium2) | `docs/architecture/decisions/0006-pdfplumber-pypdfium2-over-pymupdf.md` |
| Per-system status, paths, evidence | `docs/VOXCORE_SYSTEM_REGISTRY.md` |

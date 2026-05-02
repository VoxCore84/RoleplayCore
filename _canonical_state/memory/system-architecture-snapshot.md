---
description: "System architecture — LLM fleet (Claude, ChatGPT, Gemini, Grok models), orchestration scripts, MCP servers, hooks, agents, review cycle pipeline"
originSessionId: ab013a11-4f6d-4953-a8be-32a0f6ed330d
---
# System Architecture Snapshot — VoxCore AI Platform
Last updated: 2026-03-14 (session 174). Exported to `Desktop/Grok_Technical_Answers.md` for Grok handoff.

> Routinely update this file as models, tools, agents, or infrastructure change.

## LLM Fleet (exact models)

| Role | Model ID | Provider | Access | SDK |
|------|----------|----------|--------|-----|
| Primary Terminal / Implementer / Coordinator | `claude-opus-4-6` | Anthropic | Claude Code CLI (npm) | Built-in |
| Architect (spec gen, design review) | `gpt-5.4` | OpenAI | REST API | `openai` Python v2.26.0 |
| Auditor (correctness, security, final seal) | `gemini-3.1-pro` | Google AI / Vertex AI | REST API | `google-genai` Python v1.66.0 |
| Cold-reader (impl bias detection) | `claude-opus-4-7` | Anthropic | REST API | `anthropic` Python |
| Codex CLI (code-focused verification) | `gpt-5.4` | OpenAI (Codex CLI) | CLI subprocess | Codex CLI binary |
| Research / independent perspective | Grok 4 | xAI (SuperGrok $30/mo) | Browser (manual) | Not yet API-integrated |
| Subagents (parallel work) | `claude-opus-4-6` | Anthropic | Claude Code subagent spawn | Built-in |

**Local inference: Ollama v0.20.0** on RTX 5090 (32GB VRAM). Models: Qwen 3.5 27B (legal reasoning), Gemma 4 26B MoE (bulk/always-on), nomic-embed-text (embeddings). Open WebUI planned as frontend. MCP bridge planned for Claude Code delegation. See [local-ai-stack](local-ai-stack.md).

## Orchestration (no framework)

**No LangGraph/CrewAI/AutoGen.** Custom Python scripts + Claude Code native agent system.

### Claude Code Native
- **Subagents**: Parallel child agents (same model) for independent tasks
- **Agent Teams**: Experimental (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- **Skills**: 30+ slash commands (prompt templates triggering tool sequences)
- **Hooks**: 13 Python scripts on 11 lifecycle events

### Custom Python Scripts
| Script | Purpose |
|--------|---------|
| `tools/ai_studio/review_cycle.py` | Main multi-AI review pipeline (Phase 1 parallel → Phase 2 verify → Phase 3 seal) |
| `tools/api_architect/run_architect.py` | Design prompts → GPT-5.4 → spec `.md` files |
| `tools/ai_studio/chatgpt_bridge.py` | Spec review via ChatGPT |
| `tools/ai_studio/call_gemini.py` | Diff/artifact audit via Gemini |
| `tools/ai_studio/call_claude.py` | Cold-read review via Claude Opus 4.7 |
| `tools/ai_studio/call_codex_review.py` | Code-focused verify via Codex CLI |
| `tools/ai_studio/call_chatgpt_review.py` | ChatGPT API fallback for review cycle |
| `tools/ai_studio/orchestrator.py` | Full Triad loop: Gemini (Architect) → Claude (Executor) → Gemini (Auditor) |

### Slash Command: `/triad` (session 267)
Unified skill wrapping the entire pipeline. Subcommands: `test`, `review <file>`, `review-subagent <file>`, `spec <intake>`, `spec-dry <intake>`, `bridge [file]`, `orchestrate "<prompt>"`.

### Routing: Deterministic (not classifier-based)
| Trigger | Agent | Script |
|---------|-------|--------|
| New feature/architecture | GPT-5.4 | `run_architect.py` |
| Spec review | GPT-5.4 | `chatgpt_bridge.py` |
| Non-trivial implementation done | All 3 reviewers (parallel) | `review_cycle.py` |
| Localized bug fix, log parsing, cleanup | Claude Opus only | No API call |

## Memory & State (file-based, no vector DB, no embeddings)

### Persistent Memory
- `~/.claude/projects/<hash>/memory/MEMORY.md` — 200-line index, always in context
- 44 topic files — loaded on-demand by keyword or explicit read
- No embedding model, no semantic search — direct file reads

### Conversation State
- Full history until ~200K token context fills, then auto-compacts at 70%
- **Compaction resilience**: `precompact-snapshot.py` captures state → `compact-reinject.py` restores (novel)
- **Context injection**: `prompt-context-injector.py` detects keywords → injects topic files

### Cross-Session Coordination
- `AI_Studio/0_Central_Brain.md` — infrastructure state (read at session start)
- `doc/session_state.md` — multi-tab ownership (who edits what)
- `/wrap-up` commits + updates memory + syncs bridge

## Agents (5 primary + 7 on-demand + 1 scheduler)

### Primary (always available)
1. **Claude Code** — `claude-opus-4-6`, ~4,000 lines system prompt (CLAUDE.md + 8 rules + MEMORY.md)
2. **GPT-5.4 Architect** — spec gen, design review
3. **Gemini 2.5 Pro Auditor** — correctness, security, final seal
4. **Claude Sonnet Cold-reader** — impl bias detection (minimal context)
5. **Codex CLI Verifier** — code-focused verification

### On-Demand Subagents (spawned by skills)
6-8. **Pre-Ship Reviewers** (`/pre-ship`): Noob, Bully, Security
9-12. **Deep Investigation** (`/deep-investigate`): Code Trace, Data, Log, Context

### Scheduler
13. **Cowork** — Claude Desktop VM, 5 scheduled tasks (digest, inbox, git-hygiene, injection-sentinel, weekly-health)

## Tools (3 layers)

### Layer 1: Claude Code Native
Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch, LSP, Task*, Team*, Skill, NotebookEdit

### Layer 2: MCP Servers (6 active)
| Server | Tools | Purpose |
|--------|-------|---------|
| `mysql` | query, describe, show_tables | 5 databases (auth, characters, world, hotfixes, roleplay) |
| `wago-db2` | db2_lookup/query/search/describe/tables/validate_ids | 1,097 WoW DB2 tables (CSV-backed DuckDB) |
| `codeintel` | search_symbol, find_definition, find_references, hover_info, call/class_hierarchy | 416K C++ symbols (ctags + clangd) |
| `clangd-lsp` | LSP operations | C++ diagnostics, completions, go-to-def |
| `lua-lsp` | LSP operations | Lua (WoW addon dev) |
| `github` | 50+ GitHub ops | PRs, issues, commits, releases, code search |

### Layer 3: Custom Scripts (called via Bash)
- **AI Orchestration**: 8 scripts (review cycle, architect, bridges, reviewers)
- **Data Pipeline**: 30+ scripts (DB2 extraction, hotfix repair, coord conversion, cross-source mining)
- **Web Scrapers**: Tor Army (230K/hr, 400 instances), ATT parser, Wowhead enrichment
- **Audit Tools**: NPC (27 checks), GO (15), Quest (15), Spell, Placement
- **Server Ops**: start_all, stop_all, apply_pending_sql, SOAP, log parsing
- **Build**: configure.bat, build.bat (CMake + Ninja -j32)

## Prompt Structure

```
Claude Code system prompt (~500 lines, Anthropic-provided)
├── CLAUDE.md (~200 lines) — Triad rules, DB rules, work style, mandatory pipelines
├── .claude/rules/*.md (8 files, ~400 lines) — session-start, debugging, completion-integrity, etc.
├── MEMORY.md (200 lines) — project context, preferences, active systems
├── [Dynamic injection via hooks] — topic files injected by keyword detection
└── [Extended thinking] — always on, 32K token budget
```

Review agents get per-call system prompts (~200-500 lines) with role + artifact + prior feedback.

## Guardrails (13 hooks + 4 scoring systems)

### Hooks (Python, 1,131+ lines)
| Hook | Event | Action |
|------|-------|--------|
| sql-safety | PreToolUse | **BLOCKS** DROP/TRUNCATE/DELETE-without-WHERE |
| release-gate-enforce | PreToolUse | **BLOCKS** push --tags, gh release when gate != PASS |
| release-gate-revalidate | PostToolUse | Invalidates gate on publishable/ edits |
| edit-verifier | PostToolUse | Re-reads file to verify Edit applied |
| large-file-guard | PostToolUse | Warns on >3K line reads |
| cpp-build-reminder | PostToolUse | Reminds about build after C++ edits |
| stop-verify | Stop | Checks for unbuilt C++, unapplied SQL |
| prompt-context-injector | UserPromptSubmit | Keyword→topic file injection |
| precompact-snapshot | PreCompact | Captures session state |
| compact-reinject | SessionStart(compact) | Restores state after compaction |
| session-stats | PostToolUse/Stop/Failure | JSONL event logger |
| sync-on-git | PostToolUse(Bash) | Bridge sync after git ops |
| notification-toast | Notification | BurntToast + Forms fallback |
| subagent-complete | SubagentStop | Toast + JSONL logging |

### Scoring Systems
- **Release Gate** (`/pre-ship`): 9 mechanical checks + 3 adversarial agents → PASS/FAIL
- **Spawn Safety**: 0-100 confidence across 11 dimensions for 144K NPCs
- **Quest Integrity**: 0-100 from cross-source validation (MySQL + Wowhead + ATT + BtWQuests)
- **Spell Audit**: RED/YELLOW/GREEN classification for script coverage

### Anti-Theater Protocol (behavioral)
Built into system prompt — prevents false completion claims. Requires tool output evidence, falsifiable QA, mid-task verification gates.

## Hardware

| Component | Spec |
|-----------|------|
| CPU | AMD Ryzen 9 9950X3D — 16C/32T |
| RAM | 128 GB DDR5-5600 (2x64GB G.Skill) |
| GPU | NVIDIA RTX 5090 32GB |
| Storage | Samsung 980 PRO 2TB NVMe. Pending: 9100 PRO 4TB PCIe 5.0 Dev Drive |
| Mobo | ASUS ROG Crosshair X870E Extreme |
| OS | Windows 11 Pro 10.0.26200 |
| Monitors | LG 4K 240Hz G-SYNC + Dell secondary |
| Build | MSVC VS 2026, CMake + Ninja -j32, C++20 |
| DB | MySQL 8.0 (UniServerZ), root/admin |
| Python | 3.14.3, UV 0.10.9 |

System extensively tuned (VBS/HVCI off, Spectre off, Ultimate Performance, etc. — see MEMORY.md § Hardware).

## Cloud Resources
- Oracle Cloud VM (129.146.82.200) — DraconicBot hosting (pending deploy)
- GCP (voxcore-489923) — Gemini API billing, service account
- GitHub (VoxCore84) — 20+ repos, `gh` CLI authenticated

## Budget
~$680/mo (promo) / ~$800/mo (full) across 4 subscriptions + pay-as-you-go APIs.
See [ai-subscription-audit.md](ai-subscription-audit.md) for full breakdown.

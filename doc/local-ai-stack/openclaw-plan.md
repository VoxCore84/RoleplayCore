# OpenClaw — Always-On Agent Platform

> Local AI agent runtime for continuous background tasks. Zero API cost.

## Current State (Apr 16 2026)

**Version**: 2026.4.14 (323493f) — updated from 2026.4.2
**Status**: RUNNING, gateway healthy at `ws://127.0.0.1:18789`
**Canvas UI**: `http://127.0.0.1:18789/__openclaw__/canvas/`
**Config**: `~/.openclaw/openclaw.json`
**Daemon**: Windows Scheduled Task (auto-starts on boot)

### Models (via Ollama)
| Model | Purpose |
|-------|---------|
| `qwen3.5:27b-q4_K_M` | Primary agent model (legal reasoning) |
| `gemma4:26b` | Bulk processing, background indexing |
| `glm-4.7-flash` | Available as fallback |
| `nomic-embed-text:latest` | Embeddings for memory search |

### Active Plugins (63 loaded)
- **active-memory** — auto-injects relevant memory before replies
- **memory-wiki** — Obsidian-friendly knowledge vault
- **diffs** — read-only diff viewer for agents
- **llm-task** — structured JSON LLM tasks for workflows
- **lobster** — typed workflow tool with resumable approvals
- **thread-ownership** — multi-agent coordination
- **webhooks** — integration hooks
- **duckduckgo** — free web search for agents
- **browser** — browser tool plugin
- **ollama** — local model provider
- Plus 50+ provider plugins (Anthropic, Google, DeepSeek, etc.)

### Skills (14 eligible)
- **clawflow** — detached tasks with single owner context
- **clawflow-inbox-triage** — inbox message routing
- **coding-agent** — spawns Codex/Claude Code/Pi for coding tasks
- **gh-issues** — GitHub issue automation with PR creation
- **github** — GitHub CLI operations
- **healthcheck** — host security hardening
- **openai-whisper** — local speech-to-text
- **skill-creator** — create/audit AgentSkills
- **video-frames** — extract frames from video
- **weather** — weather queries
- **node-connect** — pairing diagnostics

### Known Issues
- **Discord plugin broken** — "missing register/activate export" in 2026.4.14; disabled
- **memory-lancedb** — needs embedding config but schema validation is strict; disabled
- **webhooks** — async registration warning (non-blocking)
- **Claude CLI auth** — needs interactive `openclaw models auth login --provider anthropic --method cli --set-default`

## NemoClaw / OpenShell — Guardrails Layer

**Status**: NOT INSTALLED — researched, not ready for our setup yet.

### What NemoClaw Is
NVIDIA's open-source security wrapper for OpenClaw. Provides kernel-level isolation:
- **Network**: blocks outbound except allowed hosts
- **Filesystem**: write only to `/sandbox` and `/tmp`
- **Process**: blocks privilege escalation via Landlock/seccomp
- **Inference**: all LLM calls route through OpenShell gateway

### Why We're Waiting
1. **Requires Linux/WSL2 + Docker** — NemoClaw runs agents inside containers
2. **Only supports NVIDIA Nemotron models** — no Qwen, Gemma, or other models
3. **Alpha quality** — "not production-ready, interfaces may change without notice"
4. **Our setup works differently** — we run Ollama natively on Windows with Qwen/Gemma

### Alternative Guardrails (what we CAN do now)
- OpenClaw's built-in `gateway.bind: loopback` — no external access
- Token-based auth on the gateway
- Tool profile set to `coding` (restrictive tool access)
- `agents.defaults.workspace` scoped to `~/.openclaw/workspace`
- Excluded/ corpus rules enforced by Claude Code tools (read-only, citations, etc.)

### When NemoClaw Makes Sense
- If we add WSL2 + Docker for other reasons
- If NVIDIA adds Ollama model support
- If we need true sandbox isolation for untrusted agent tasks

## Planned Agent Tasks (original vision, still valid)

### 1. Auto-Indexer
- Watch Case_Reference for new files
- Classify type, generate frontmatter, add to vector DB
- Update master index automatically

### 2. Contradiction Finder
- Nightly sweep for inconsistencies across documents
- "Command stated X in this MFR but stated Y in this email"

### 3. Cross-Reference Validator
- Check every claim in filings against source evidence
- Flag unsupported claims

### 4. Missing Evidence Detector
- Compare filing requirements against available evidence
- Proactive alerts before submission deadlines

### 5. Timeline Keeper
- Extract dates from all documents
- Maintain master chronological timeline

## Architecture

```
OpenClaw Gateway 2026.4.14 (Windows Scheduled Task)
    │
    ├── Ollama (localhost:11434) — 3 models + embeddings
    │     ├── qwen3.5:27b-q4_K_M (primary agent)
    │     ├── gemma4:26b (bulk/background)
    │     └── nomic-embed-text (memory search)
    │
    ├── Canvas UI (localhost:18789/__openclaw__/canvas/)
    │
    ├── 63 loaded plugins
    │     ├── active-memory (auto-recall)
    │     ├── memory-wiki (knowledge vault)
    │     ├── duckduckgo (web search)
    │     ├── lobster + clawflow (workflow engine)
    │     └── ...
    │
    ├── 14 eligible skills
    │     ├── coding-agent (spawn Claude Code/Codex)
    │     ├── gh-issues (GitHub automation)
    │     └── ...
    │
    └── [Future] NemoClaw/OpenShell sandbox (needs WSL2+Docker)
```

## Key Commands
```bash
openclaw gateway start        # Start via Scheduled Task
openclaw gateway stop         # Stop
openclaw gateway health       # Health check (use --timeout 20000 on Windows)
openclaw doctor               # Full diagnostic
openclaw skills list          # Show available skills
openclaw plugins list         # Show plugins
openclaw config set <path> <value>  # Change config
```

## Sources
- OpenClaw: https://github.com/openclaw
- NemoClaw: https://github.com/NVIDIA/NemoClaw
- NemoClaw docs: https://docs.nvidia.com/nemoclaw/latest/get-started/quickstart.html
- OpenClaw + Gemma guide: https://www.lushbinary.com/blog/openclaw-gemma-4-local-ai-agent-ollama-setup-guide-2026/

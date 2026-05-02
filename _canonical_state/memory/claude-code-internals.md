---
description: "Claude Code internals, source code architecture, tools, compaction, system prompt, context window, memory, hooks, permissions, MCP, plugins, skills, teams, swarm, agents, voice, API layer, messages pipeline, UI renderer"
originSessionId: 3cd2e95f-aa53-44de-bc7b-1f53d648e420
---
# Claude Code Internals — SME Reference

Source baseline: `C:\Users\atayl\Desktop\claude-code-source\claude-code-source\` (v2.1.88, source-map extracted from npm on 2026-03-31 leak)
2.1.97 refresh overlay: `C:/Users/atayl/Desktop/claude-code-source/extract-2.1.97/package/cli.js` (13.4 MB minified bundle — **no sourcemap**; Anthropic stopped shipping `cli.js.map` after the 2.1.88 leak, so 2.1.97 is grep-verified against the minified bundle rather than re-extracted)
Package: `@anthropic-ai/claude-code`, built with **Bun**, React/**Ink** (terminal UI), TypeScript. v2.1.88 had ~1,884 TS files.
Reports: `AI_Studio/Reports/ClaudeCodeInternals/` — start at `README.md`
**Status**: ALL 22 REPORTS COMPLETE (Tiers 1-4) + **2.1.97 delta refresh applied 2026-04-08** (Session 232)

## 2.1.97 Refresh — Top-Level Changes

**Methodology**: Section 5 of `doc/handoff_cc_297_source_refresh.md` priority list + `cli.js@2.1.97` grep verification + v2.1.88 source tree for old-behavior contrast. Every new claim has a `cli.js@2.1.97 symbol match` or `v2.1.88 src/path:NNN` anchor; changelog-only items are labeled. Delta summaries are at the top of each report. Full per-report findings in `AI_Studio/Reports/ClaudeCodeInternals/_2.1.97_refresh/`.

**Key invalidations** (report claims that were wrong before the refresh):

- **TaskOutput tool deprecated (2.1.83)** — `shouldDefer:!0`, runtime `description()` says `"[Deprecated] — prefer Read on the task output file path"`. Aliases `AgentOutputTool`/`BashOutputTool`. Report 06.
- **Agent `resume` parameter REMOVED (2.1.77)** — gone from `AgentInput` schema + runtime. `SendMessage` auto-resumes stopped agents. Reports 06, 08.
- **`getContextWindowForModel` simplified from 7 priorities to 4 (2.1.97)** — `CLAUDE_CODE_MAX_CONTEXT_TOKENS` env var REMOVED; `/models` capability cache + ant-model override paths gone. Remaining: `[1m]` suffix → beta header → Sonnet 1M experiment → 200K default. Reports 03, 1m_context.
- **1M context NOT default for Enterprise or plain Team** — the changelog overreached. Only Max and Team Premium (`E16()` = team with `default_claude_max_5x` billing) get `Opus 4.6[1m]` default via `QX()` check. Enterprise + Team Standard + Pro default to Sonnet. Reports 03, 1m_context.
- **Buddy system REMOVED in 2.1.97** (April Fools 2026 cleanup) — shipped in 2.1.x for the April 1-7, 2026 teaser, stripped from bundle 2026-04-08. Only vestigial `"companion_intro"` attachment denylist remains. Report 15 is now historical.
- **MCP HTTP/SSE connection leak ~50 MB/hour fixed (2.1.97)** — vendored `@modelcontextprotocol/sdk` upgrade. `close()` now calls `_abortController.abort()` and tears down the SSE pipeReader. Report 12.
- **Compaction wrote duplicate multi-MB subagent transcript files** (fixed 2.1.97). Report 01.
- **Subagents with `isolation: "worktree"` leaked parent CWD** (fixed 2.1.97). Report 07.
- **Nested CLAUDE.md re-injection fixed (2.1.89)** — four layered guards preserved; `loadedNestedMemoryPaths` Set on tool-use context (not LRU `readFileState`). Reports 02, 04, 20.
- **429 Retry-After cap (NEW 2.1.97)** — if `Retry-After > 60s` and NOT in unattended-retry, client throws immediately instead of burning attempt. `xs_=60000`, telemetry `tengu_api_retry_after_too_long`. Report 19.
- **Long-retry visibility fix (2.1.94)** — persistent-retry loop yields `system/api_error` every 30s so UI ticks down. Telemetry `tengu_api_persistent_retry_wait`. Report 19.

**Key gaps** (new surface area added):

- **`defer` permission decision** for `PreToolUse` hooks (2.1.89) — print-mode only, solo-only, emits `hook_deferred_tool` attachment + `tool_deferred` stop reason. Precedence: `deny > defer > ask > allow > passthrough`. Report 09.
- **Hook output >10K chars persisted to disk** (NEW 2.1.89) — `TR4=1e4`, telemetry `tengu_hook_output_persisted`, covers `stdout`/`systemMessage`/`additionalContext`/`initialUserMessage`. Report 09. (Changelog said "50K" but actual constant is 10K.)
- **`TaskCreated` + `TaskCompleted` hooks** (2.1.84) — coordinator lifecycle events. JSON: `{task_id, task_subject, task_description, teammate_name, team_name}`. Exit 2 blocks. Reports 08, 09.
- **`CLAUDE_CODE_NO_FLICKER=1` alt-screen compositor** — opt-in fullscreen mode, ~56 `T4()` call sites, auto-disabled under `tmux -CC`. Sticky footer, brief transcript, git-op summary, etc. all gate on it. `xj7` React wrapper, `setAltScreenActive`. Report 22 Section 3b.
- **NEW auto-compact window resolver** `getAutoCompactWindow(model, settingsWindow)` with 4 sources: env var (bounded `[100K, 1M]`) → settings.json → GrowthBook `tengu_amber_redwood` → model default. Returns `{window, configured, source}`. Reports 01, 03.
- **NEW rapid-refill autocompact breaker** — if context refills to threshold within `<3` turns 3 times in a row, throws `"Autocompact is thrashing"`. Telemetry `tengu_auto_compact_rapid_refill_breaker`. Report 01.
- **Dream: Memory Pruning** — second dream prompt `QGK()` fires in tiny-memory mode. `rm` allowed for `.md` files inside memory dir; Edit forbidden ("memories are immutable"). Two-directory variant (private + shared team). Report 05.
- **`/powerup` command** (2.1.90) — interactive animated lessons. `type:"local-jsx"`. Telemetry: `powerup_lesson_opened`/`_completed`. State: `powerupsUnlocked` Set. Report 18.
- **Commands removed in 2.1.9x**: `/tag` (2.1.92), `/vim` (2.1.92 → `/config`), `/pr-comments` (plugin migration), `/output-style`. Report 18.
- **Commands graduated internal→user-facing**: `/files`, `/btw`. Report 18.
- **Tool pool shrinkage**: v2.1.88's 18 anonymous stubs → 16 in 2.1.97. 16 of 18 named stubs removed entirely. 17 of ~25 internal-only commands removed. Report 18.
- **MCP per-tool `maxResultSizeChars` override** via `_meta["anthropic/maxResultSizeChars"]` (2.1.91) — clamped at `xF1=500000`. Also raises `persistenceThresholdCeiling`. Report 12.
- **MCP OAuth CIMD (SEP-991, 2.1.81)** — `client_id_metadata_document_supported` AS metadata flag. When CIMD + `clientMetadataUrl`, skips registration, sets `{client_id: <metadataUrl>}`. `MCP_OAUTH_CLIENT_METADATA_URL` env var. Report 12.
- **MCP OAuth RFC 9728** Protected Resource Metadata discovery (2.1.85) via `/.well-known/oauth-protected-resource`. Failure log: `"RFC 9728 discovery failed, falling back: ..."`. Report 12.
- **`MCP_CONNECTION_NONBLOCKING=true`** env var for `-p` mode (2.1.89) — default wait `J4=5000` ms. Report 12.
- **Slack MCP UI override** — `userFacingName(){return"Slacked"}`, clickable `https://slack.com/app_redirect?channel=...` link when terminal supports OSC 8. First MCP-specific UI override. Report 12.
- **PowerShell tool opt-in preview** (first-class in 2.1.97, `b9="PowerShell"`). NOT in public sdk-tools.d.ts union. Gated by Windows + sandbox + `!areUnsandboxedCommandsAllowed()`. Respects `settings.env` via `Ph6()` parser. Report 06.
- **`disableSkillShellExecution` setting** (2.1.91) — replaces inline skill shell blocks with placeholder. Reports 06, 10, 11.
- **Accept Edits mode auto-approves env-var prefixes** (2.1.97) — allowlist `s68=new Set(["GOEXPERIMENT", ...])` + regex `wi1=/^[A-Za-z_]\w*=/`. Report 10.
- **`forceRemoteSettingsRefresh`** policy setting (2.1.92) — blocks startup until remote managed settings freshly fetched. Report 10.
- **`managed-settings.d/` drop-in directory** (2.1.83) — base merge + alphabetical drop-ins. Report 10.
- **Voice mode Nova 3 unconditional** — `tengu_cobalt_frost` rollout gate removed; `use_conversation_engine=true` + `stt_provider=deepgram-nova3` hardcoded. `VoiceModeNotice` startup banner replaced by spinner tip. Report 14.
- **UltraPlan timeout 30min→90min default** via GrowthBook `tengu_ultraplan_timeout_seconds=5400`. Model flag removed; new `tengu_ultraplan_prompt_identifier` selects between prompt templates. Report 16.
- **6 provider paths** (was 4): firstParty, Bedrock, Vertex, Foundry, **Mantle** (`CLAUDE_CODE_USE_MANTLE`), **anthropicAws** (`CLAUDE_CODE_USE_ANTHROPIC_AWS`). Report 19.
- **Bridge session cards show local git repo info** — `git_repo_url` / `gitRepo*` serialized into bridge session metadata (claude.ai UI displays it). Report 17.

## Codename Table (updated)

- **Chicago** = Computer Use (macOS-only, `feature('CHICAGO_MCP')` + `tengu_malort_pedway`)
- **Fennec** = Opus 4.5 (pre-release)
- **Kairos** = unreleased scheduling/notification platform
- **Mantle** = Amazon Bedrock auth path (2.1.94) — 6th provider, `CLAUDE_CODE_USE_MANTLE=1`
- **NO_FLICKER** = alternate alt-screen fullscreen renderer mode (already in v2.1.88 as fullscreen toggle; publicly exposed around 2.1.89) — `CLAUDE_CODE_NO_FLICKER=1`
- **powerup** = interactive animated lessons feature (2.1.90) — `/powerup` slash command
- **Onyx Plover** = AutoDream feature gate (`tengu_onyx_plover`)

## Arcanum Wiki — Comprehensive Knowledge Base (Session 227)

**Location**: `doc/arcanum/` — 296 files, 2.6 MB across 25 directories
**Purpose**: NotebookLM-ready wiki of ALL Claude Code internals. Future: MCP server for persistent recall.
**Source preservation**: 130 .txt files (36,486 lines of TypeScript) in `doc/arcanum/source/`

### Key Discoveries (from 7-agent research swarm)
- CLAUDE.md is user message (NOT system prompt) — wrapped in `<system-reminder>` with "may or may not be relevant"
- Memory selector only sees filenames + `description` frontmatter (never content)
- Speculation system pre-runs tools during response streaming (copy-on-write overlay filesystem)
- 99 slash commands exist (18 stubbed). Hidden aliases: `/checkpoint`=rewind, `/continue`=resume, `/fork`=branch
- 170+ env vars. `CLAUDE_CODE_SIMPLE`=bare mode. `CLAUDE_CODE_ABLATION_BASELINE`=disable 7 features
- 700+ `tengu_` strings (~80 real feature gates, rest analytics). "Fennec" was codename for Opus 4.5
- Buddy pet: 18 species, 5 rarities, deterministic from userId hash. April Fools 2026 launch
- `scripts/external-stubs/` overlay system — Anthropic maintains internal-only implementations
- Default model: Max/Team Premium → Opus 4.6, everyone else → Sonnet 4.6
- Hook `allow` does NOT override `deny` — defense-in-depth, most restrictive wins

### Directory Map
core/ (14), tools/ (21), commands/ (12), hidden/ (11), services/ (14), guides/ (15),
hooks/ (8), agents/ (7), permissions/ (6), skills/ (5), mcp/ (7), ui/ (5), bridge/ (5),
config/ (3), api/ (3), source/ (130), plus 10 smaller dirs

## Architecture — Boot Sequence

```
cli.js (entry, bun binary)
  → src/entrypoints/ (arg parsing: REPL vs SDK vs bridge)
  → src/bootstrap/state.ts (global mutable state: session ID, cost, tokens)
  → src/setup.ts (worktree, hooks snapshot, UDS messaging, analytics, prefetch)
  → src/main.tsx (React/Ink render mount, 789KB)
    → src/screens/REPL.tsx (THE mega-component: UI, state, query orchestration)
      → src/query.ts (1,729 lines: main model conversation loop)
        → src/services/api/claude.ts (Anthropic SDK streaming, retries)
```

## Root Files — Backbone

| File | Lines | Role |
|------|-------|------|
| `Tool.ts` | 792 | `Tool<I,O,P>` interface, `buildTool()`, `ToolUseContext`, `ToolPermissionContext` |
| `query.ts` | 1,729 | Main loop: API call → stream → tool dispatch → compact check → loop |
| `QueryEngine.ts` | 1,295 | SDK/headless/print-mode engine (wraps query.ts) |
| `tools.ts` | 389 | Registry: `getAllBaseTools()`, `getTools()`, `assembleToolPool()` |
| `commands.ts` | 754 | 86+ slash commands, skill loading, dynamic discovery |
| `context.ts` | 189 | `getSystemContext()` = git status; `getUserContext()` = CLAUDE.md |
| `setup.ts` | 477 | Session init: node check, worktree, hooks, UDS, analytics |
| `Task.ts` | 125 | Task types: local_bash, local_agent, remote_agent, in_process_teammate, dream |
| `cost-tracker.ts` | 323 | Per-model token/cost tracking, session persistence |
| `history.ts` | 464 | JSONL prompt history, paste store, up-arrow |

## System Prompt Construction (`src/constants/prompts.ts`)

`getSystemPrompt()` builds array of strings:
1. **STATIC (cross-user cacheable)**:
   - Intro ("You are Claude Code, Anthropic's CLI…")
   - System section (tool permissions, system-reminders, hooks, compaction)
   - Doing Tasks (avoid over-engineering, no time estimates, security)
   - Executing Actions with Care (reversibility, blast radius)
   - Using Your Tools (prefer dedicated tools over Bash)
   - Tone and Style (no emojis, concise, file:line refs)
   - Output Efficiency (concise, inverted pyramid)
2. **`SYSTEM_PROMPT_DYNAMIC_BOUNDARY`** (cache partition)
3. **DYNAMIC (per-session)**:
   - Session-specific guidance (agent tool, skills, verify agent)
   - Memory (`loadMemoryPrompt()` — MEMORY.md + topic files)
   - Ant model overrides
   - Environment info (OS, cwd, git, shell, model)
   - Language preference
   - Output style
   - MCP instructions (from connected servers)
   - Scratchpad instructions
   - Function result clearing
   - Token budget (when specified)

Key constants: `FRONTIER_MODEL_NAME = 'Claude Opus 4.6'`
Model IDs: opus=`claude-opus-4-6`, sonnet=`claude-sonnet-4-6`, haiku=`claude-haiku-4-5-20251001`

**CLAUDE.md is NOT in API `system`** — injected as content in `<system-reminder>` tags in user message context.
Priority: Managed(lowest) → User → Project(root→CWD) → Local → AutoMem(highest)

## Context & Compaction

- Default 200K context. `[1m]` suffix = 1,000,000 tokens (beta header `context-1m-2025-08-07`)
- Auto-compact thresholds: 200K→167K, 1M→967K
- 4-tier compaction: API microcompact → microcompact → session memory → full LLM compact
- Honors `## Compaction Instructions` in CLAUDE.md
- Only 5 files restored post-compact (50K budget, 5K/file)
- MCP tool results NOT eligible for microcompact (accumulate faster)

## Memory System

- Dir: `~/.claude/projects/<hash>/memory/`
- MEMORY.md: always injected, 200 line / 25K byte cap
- Topic files: Sonnet selector picks ≤5/turn based on **filename + description frontmatter only**
- 200 topic file cap (oldest by mtime invisible beyond)
- `extractMemories` — auto-extraction after conversations
- `autoDream` — background consolidation (24h + 5 sessions, 4-phase)
- `SessionMemory` — feature-gated `tengu_session_memory`

## Tool System (`src/tools/`)

40+ tools. Each has: `call()`, `checkPermissions()`, `prompt()`, `isConcurrencySafe()`, `isReadOnly()`, `maxResultSizeChars`, `shouldDefer`.

### Always-loaded
AgentTool, BashTool, FileReadTool, FileEditTool, FileWriteTool, GlobTool, GrepTool, WebSearchTool, WebFetchTool, SkillTool, TaskCreate/Get/Update/List, SendMessageTool, TeamCreate/Delete, AskUserQuestionTool, EnterPlanMode, ExitPlanMode, EnterWorktree, ExitWorktree, TodoWriteTool, NotebookEditTool, TaskOutputTool, TaskStopTool, BriefTool, LSPTool, ListMcpResourcesTool, ReadMcpResourceTool, ToolSearchTool

### Feature-gated
REPLTool (ant), SleepTool (PROACTIVE/KAIROS), Cron tools (AGENT_TRIGGERS), RemoteTriggerTool, MonitorTool, PowerShellTool, TerminalCaptureTool, WebBrowserTool, SnipTool (HISTORY_SNIP), WorkflowTool (WORKFLOW_SCRIPTS), ConfigTool (ant), TungstenTool (ant)

### Agent Tool Filtering
- `ALL_AGENT_DISALLOWED_TOOLS`: TaskOutput, ExitPlanMode, EnterPlanMode, AskUserQuestion, TaskStop
- `ASYNC_AGENT_ALLOWED_TOOLS`: Read, Search, Grep, Glob, Bash, Edit, Write, Notebook, Skill, Worktree
- `IN_PROCESS_TEAMMATE_ALLOWED_TOOLS`: TaskCRUD, SendMessage, Cron
- `COORDINATOR_MODE_ALLOWED_TOOLS`: Agent, TaskStop, SendMessage, SyntheticOutput

## Hooks & Permissions

Hook types: PreToolUse, PostToolUse, SessionStart, SessionEnd, FileChanged
Permission modes: `default`, `plan`, `auto`, `bypassPermissions`, `acceptEdits`, `dontAsk`
Settings cascade: global → project → local
- `alwaysAllowRules`, `alwaysDenyRules`, `alwaysAskRules`
- Auto-mode classifier (yoloClassifier) for auto decisions
- Denial tracking → falls back to prompting after threshold
- Enterprise managed settings via remoteManagedSettings

## Teams/Swarm

- Team config: `~/.claude/teams/<name>/config.json`
- Task list: `~/.claude/tasks/<name>/`
- InProcessTeammateTask, LocalAgentTask, RemoteAgentTask
- Message passing: mailbox, UDS, leader permission bridge
- Permission sync between leader and workers

## Skills

- Bundled: `src/skills/bundled/`
- User: `.claude/skills/` directories
- Plugin/MCP skills
- Dynamic discovery during file ops
- Skill search: keyword matching for deferred tools

## MCP Client

- Discovery from `.mcp.json`
- Tools prefixed `mcp__server__tool`
- Resource handling, elicitation for auth
- Instructions injected into system prompt

## UI

- React + Ink (terminal), custom Yoga layout (`src/native-ts/yoga-layout/`)
- REPL.tsx = 789KB mega-component
- Vim mode (`src/vim/`), voice mode (`src/voice/`), buddy/companion (`src/buddy/`)
- Keybindings (`src/keybindings/`)

## Feature Flags (`bun:bundle` feature())

PROACTIVE, KAIROS, BRIDGE_MODE, VOICE_MODE, COORDINATOR_MODE, AGENT_TRIGGERS, CONTEXT_COLLAPSE, HISTORY_SNIP, FORK_SUBAGENT, UDS_INBOX, WORKFLOW_SCRIPTS, BUDDY, EXPERIMENTAL_SKILL_SEARCH, TOKEN_BUDGET, VERIFICATION_AGENT, CACHED_MICROCOMPACT, WEB_BROWSER_TOOL, TERMINAL_PANEL, TORCH, ULTRAPLAN, TEAMMEM, COMMIT_ATTRIBUTION, MCP_SKILLS, REACTIVE_COMPACT, BREAK_CACHE_COMMAND, MONITOR_TOOL, OVERFLOW_TEST_TOOL, KAIROS_BRIEF, KAIROS_PUSH_NOTIFICATION, KAIROS_GITHUB_WEBHOOKS, CCR_REMOTE_SETUP, DAEMON

## Key Patterns

1. **DCE via feature()** — `bun:bundle` eliminates code paths at build time
2. **ant vs external** — `USER_TYPE === 'ant'` gates internal-only features
3. **Prompt cache boundary** — static/dynamic split for cross-user cache hits
4. **System prompt sections** — memoized with cache-break option
5. **buildTool()** — factory with safe defaults (fail-closed)
6. **Tool deferred loading** — ToolSearch saves prompt tokens
7. **JSONL history** — lockfile-coordinated, paste store for large content
8. **Task ID prefixes** — b=bash, a=agent, r=remote, t=teammate, d=dream, w=workflow, m=monitor

## Applied Optimizations (Session 220+)

1. `opus[1m]` enabled (5.8x context)
2. 3 rules made conditional with `paths:` frontmatter
3. Git status capped at 2K chars
4. 54 memory files have keyword-rich `description` frontmatter
5. Settings: autoMemoryEnabled, enableAllProjectMcpServers, cleanupPeriodDays=90

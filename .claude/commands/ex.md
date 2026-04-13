---
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(python:*), Bash(ls:*), Bash(find:*), Bash(mkdir:*), Bash(wc:*), Bash(du:*), Agent, TaskCreate, TaskUpdate, mcp__docs-rag__*, mcp__arcanum__*, mcp__local-llm__*
description: Unified Excluded/ corpus command. Use for any legal/career/finance corpus operation — /ex <action> with action ∈ {status, posture, sme, ask, absorb, refresh, lint, persons, search}. Replaces the six separate /ex-* commands.
---

# /ex — Unified Excluded/ Corpus Command

One command, many actions. Replaces `/ex-status`, `/ex-posture`, `/ex-sme`, `/ex-ask`, `/ex-absorb`, `/ex-refresh`. Auto-match clarity: user types "ex" or "/ex" and picks an action rather than 6 commands racing on overlapping trigger descriptions.

## Invocation

```
/ex status                 # corpus health dashboard
/ex posture                # morning urgency brief
/ex sme [scope]            # prime as SME (case/career/finance/brand/fast/all)
/ex ask <question>         # swarm answer with citations
/ex absorb <path>          # one-shot ingestion
/ex refresh [folder]       # incremental maintenance (explicit only)
/ex lint                   # corpus integrity audit (orphan/stale/missing/dup/drift)
/ex persons <name>         # entity resolver via roster + hybrid search
/ex search <query>         # hybrid FTS5+vector retrieval
```

If `/ex` is invoked with no action, ask which action. If invoked with an unknown action, show this menu.

## P0 Constraints (apply to every action)

1. **NEVER use CronCreate.** Scheduled behavior → daemon asyncio loop, Task Scheduler, or watchdog events.
2. **NEVER run maintenance mid-query** (`refresh`/`absorb` inside `ask`/`search`/`posture`). If retrieval is thin, state it. User invokes maintenance explicitly.
3. **`Case_Reference/` is READ-ONLY.** Enforced by `tools/excluded_daemon/router.assert_writable()`.
4. **Every non-trivial claim needs a source citation.** See `.claude/rules/excluded-corpus.md`.
5. **Completion integrity.** No "successfully done" without counts and evidence.

## Action Dispatch

Each action is implemented by an existing sibling command file. `/ex <action>` acts as a router:

| Action | Implementation | Purpose |
|---|---|---|
| `status` | `.claude/commands/ex-status.md` | Freshness dashboard |
| `posture` | `.claude/commands/ex-posture.md` | Morning brief with urgency + deadlines |
| `sme` | `.claude/commands/ex-sme.md` | Prime Claude with structural map + memory |
| `ask` | `.claude/commands/ex-ask.md` | 4-agent swarm with Planning/Tool Use/Reflection |
| `absorb` | `.claude/commands/ex-absorb.md` | Ingest new file/folder with memory updates |
| `refresh` | `.claude/commands/ex-refresh.md` | Extract/OCR/transcribe/reindex |
| `lint` | `python tools/excluded_lint.py` (inline) | 6-check integrity audit |
| `persons` | `python tools/persons_resolve.py "<name>"` (inline) | Entity resolver |
| `search` | `python tools/excluded_hybrid_search.py "<query>"` (inline) | Hybrid retrieval |
| `thread` | `python tools/mbox_thread.py --id <n>` OR `--subject "<text>"` (inline) | Expand an email reply chain |
| `probe` | `python tools/quality_probe.py --engine all` (inline) | Retrieval scoreboard (FTS5 vs vector vs hybrid, 50-query suite) |
| `seed-persons` | `python tools/persons_ner_seed.py` (inline, long-running) | NER sweep to auto-populate persons candidate roster |

### Inline actions (no sibling command)

**`/ex lint`** — equivalent to:
```bash
python tools/excluded_lint.py
```
Surfaces orphans, stale extractions, missing files, duplicates, memory drift, citation breaks. Writes report to `AI_Studio/Reports/scheduled/excluded_lint_<timestamp>.json`.

**`/ex persons <name>`** — equivalent to:
```bash
python tools/persons_resolve.py "<name>"
```
Returns canonical name + role + org + FTS5 hits + mbox hits across all aliases.

**`/ex search <query>`** — equivalent to:
```bash
python tools/excluded_hybrid_search.py "<query>" --top-k 10
```
FTS5 + ChromaDB candidates fused via reciprocal rank fusion. Sub-second for FTS5, ~3s for vector side.

**`/ex thread <id_or_subject>`** — expands an email reply chain:
```bash
python tools/mbox_thread.py --id <n>              # by message id
python tools/mbox_thread.py --subject "<text>"    # by subject substring
```
Walks in_reply_to + References headers to find root, then emits every message in chronological order with headers + truncated bodies.

**`/ex probe`** — retrieval quality scoreboard:
```bash
python tools/quality_probe.py --engine all
```
Runs the 50-query test suite against FTS5, vector (ChromaDB), and hybrid (RRF). Exit code 2 if any engine below 80%. Reports land in `AI_Studio/Reports/scheduled/quality_probe_*.md`.

**`/ex seed-persons`** — NER sweep (long-running, ~50 min):
```bash
python tools/persons_ner_seed.py --min-mentions 2
```
Uses local Ollama qwen2.5 to extract person entities across all extracted texts. Writes candidates to `.cache/persons/persons_candidates.json` for user review/promotion into the canonical `persons.json` roster.

### Sibling-command actions

For `status`, `posture`, `sme`, `ask`, `absorb`, `refresh`: load the corresponding `.claude/commands/ex-<action>.md` and follow its instructions. Those files contain the full workflow for that action — `/ex` is a thin router.

## Disambiguation

If user types `/ex` with a string that doesn't match an action but could be a question or query:

- 5+ words with a question mark → assume `ask`
- Path-like (contains `/`, `\`, or exists on disk) → assume `absorb`
- Single word that matches a person name in `.cache/persons/persons.json` → assume `persons`
- Otherwise → show menu and ask

## Gotchas

1. **Typing `/ex` alone auto-matches nothing specific.** Must be `/ex <action>`. The six legacy `/ex-*` commands still work if you prefer them.
2. **The `/ex-*` sibling commands are NOT deprecated.** They're the implementations this routes to. Keeping them as first-class callables means skills that chain to them continue working.
3. **No `/ex` rename for `/case-status`, `/case-search`, etc.** Those remain because they have case-specific logic not covered by the generic corpus actions. Future work: consider absorbing them into `/ex case-status` / `/ex case-search`.

## Example Flows

**Morning startup:**
```
/ex posture
```
Shows deadlines, overnight evidence, stale items, recommended focus.

**Working on a filing:**
```
/ex sme case             # prime SME on case lane
/ex ask "what evidence do we have that McMaster contacted AFPC?"
/ex persons Corpening    # expand on a surfaced entity
/ex search "return without decision AFPC"   # cross-check
```

**After receiving new docs:**
```
/ex absorb "C:/Users/atayl/Desktop/Excluded/IMPORTANT DOCS/_Inbound/new_MFR.pdf"
/ex lint                 # confirm no duplicates or orphans introduced
```

**Weekly hygiene:**
```
/ex lint
/ex refresh IMPORTANT\ DOCS/Case_Reference
/ex status
```

## Why this exists

See `.claude/rules/excluded-corpus.md` Gotchas #7 (skill-trigger races). With 6 `/ex-*` commands plus `/case-*` commands plus `/rag-search` plus `/search-docs`, the Claude Code auto-match picked randomly when users typed generic phrases like "is the corpus current?" — sometimes routing to `/ex-status`, sometimes `/ex-posture`, sometimes `/memory-audit`. The unified `/ex <action>` forces intent to be explicit.

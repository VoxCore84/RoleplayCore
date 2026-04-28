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

## Pre-flight: KG entity context (for `ask`)

**Run BEFORE loading `ex-ask.md` whenever the action is `ask`.** Synchronous Knowledge Graph pre-fetch — pre-populates entity facts so each of the 4 fan-out agents starts KG-aware instead of having to rediscover persons, orgs, regulations, and case numbers via grep.

### Step A — Identify candidate entities in the question

Scan the question for:
- **Person names** — capitalized name tokens (e.g. "McMaster", "Amy Little", "Tolin"), military ranks ("Col Johnston", "Lt Col Earles")
- **Organizations / acronyms** — uppercase 2-6 letter tokens ("ET", "AFPC", "DCSA", "AFBCMR", "HAF/A1ZA"), org words ("USAF", "Cannon AFB")
- **Regulation citations** — patterns like "10 USC 1034", "DoDI 6495.02", "DAFI 36-3211", "45 CFR 60.21"
- **Case numbers** — "DSAID", "OSI", "AFBCMR" + alphanumeric IDs
- **Specific dates** — ISO or written ("2026-04-21", "Apr 13", "Aug 10 2026")

Cap at 8 entities to keep the pre-fetch fast (<2s). Skip generic words (the, what, did, etc.).

**Ambiguity caveat**: The KG uses fuzzy matching, so a 2-letter token like "ET" can resolve to a substring match (e.g. "DHA Market/Intermediate Headquarters" contains "et"). When an entity has fewer than ~50 mentions OR its canonical name barely overlaps the query token, mark it `[ambiguous]` in the context block. The fan-out agents can then search the corpus directly to correct the resolution rather than trusting a misleading KG hit.

### Step B — Resolve each entity via KG MCP

For each candidate, call `mcp__docs-rag__kg_entity(name=<token>, kind="")`. If the response has `count > 0`, take the top entity (highest mention_count). Skip entities with `count == 0` — they're not in the KG.

For the top 3 highest-mention-count entities, ALSO call `mcp__docs-rag__kg_relations(entity_id=<id>, depth=1)` to surface their direct connections. This is the "who else was involved" lookup.

For 1 entity (typically the central person/org of the question), call `mcp__docs-rag__kg_relations(entity_id=<id>, depth=2)` for multi-hop reach. Skip if the question is purely regulatory.

### Step C — Build the Entity Context Block

Format the KG findings as a compact markdown block (target <800 tokens):

```markdown
## Entity Context (KG pre-fetch)

| Entity | Kind | Canonical | Mentions | KG ID |
|--------|------|-----------|----------|-------|
| Amy Little | person | amy little | 102 | 7568 |
| McMaster | person | mcmaster | 374 | ... |

### Top connections (1-hop)
- **Amy Little** ↔ Tolin (715), Adam Taylor (5466), HAF/A1ZA, Earles (278)
- **McMaster** ↔ Adam Taylor, Johnston, AFPC, ...

### Multi-hop reach (from <central_entity>)
- Hop 1: <count> entities — top 5 by salience: ...
- Hop 2: <count> entities — top 5 by salience: ...

### Top doc paths surfaced
- `Case_Reference/04_LEGAL_CORRESPONDENCE/<file>.pdf`
- `Case_Reference/01_APPEALS_AND_QAI/<file>.pdf`
- ...
```

### Step D — Inject into the workflow

Once the Entity Context Block is built, **then** load `.claude/commands/ex-ask.md` and proceed with its phases. The block becomes part of working memory and MUST be:

1. **Included in the Phase 0 plan** as resolved entities (skip rediscovery)
2. **Prepended to each agent prompt** in Phase 1 — every agent (evidence, mbox, regulation, timeline) starts with "Given the Entity Context Block: <block>, your job is to..."
3. **Cited in the synthesis** — Phase 2's Key Evidence section can reference KG-resolved canonical names instead of raw mentions

### When to skip pre-flight

- Question has no resolvable entities (pure conceptual: "explain hostile work environment")
- KG MCP tools return `error: KG not built` — note this in the report header and proceed without
- User passed `--skip-prefetch` flag (escape hatch for debugging)

### Cost / latency

~5-8 MCP calls, each ~50-200ms (SQLite-backed). Total pre-flight overhead: 1-2 seconds. Negligible vs the 30-90s the 4-agent fan-out takes, and saves each agent from re-running the same entity grep.

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

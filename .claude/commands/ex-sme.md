---
allowed-tools: Read, Grep, Glob, Bash(python:*), Bash(python3:*), Bash(ls:*), Bash(find:*), mcp__docs-rag__*, mcp__arcanum__*, TaskCreate, TaskUpdate
description: Use at the start of a focused work session on the legal case/career/finance corpus, or before a multi-step task (filing draft, cross-folder synthesis, audit). Primes Claude with structural map, memory files, briefing docs, and runs anchor queries. No re-discovery needed downstream.
---

# /ex-sme — Become SME on the Excluded Corpus

Purpose: make Claude a subject-matter expert on the `Excluded/` tree in one command — ready to answer deep questions about the legal case, career package, finances, brand work, and supporting evidence without rediscovery.

This is different from `/ex-posture` (daily urgency brief) and `/ex-status` (corpus health). This is about **loading Claude with domain knowledge** so downstream tasks (`/ex-ask`, `/filing-prep`, `/one-pager`, drafting) hit the ground running.

## When to Run

- First command of a focused work session on the case/career/finances
- After a `/ex-refresh` that added significant new content
- Before a complex multi-step task (filing draft, cross-folder synthesis, audit)
- Explicitly by the user asking "become SME on Excluded"

## Invocation

`/ex-sme` — full prime (all domains)
`/ex-sme case` — narrow to legal/case material only
`/ex-sme career` — career package + resume lanes
`/ex-sme finance` — finances, VA, budgets
`/ex-sme brand` — brand/business/revenue
`/ex-sme fast` — minimal prime (structure + memory index only, no deep reads)

## P0 Constraints

- **NEVER use CronCreate** for any part of this command. No recurring scheduled calls. If the user wants this to auto-run, it goes through Windows Task Scheduler or a session-start hook — not cron.
- **Do not invent facts.** Every claim in the final summary must cite a specific file or query result.
- **Stay under 150 lines of output.** This is a prime, not a dump. Details go into context silently via the reads.

## Workflow

### Phase 0 — Self-check: is the corpus healthy?

Run in parallel:
```
Bash: python tools/excluded_fts_build.py --stats
MCP:  mcp__docs-rag__docs_rag_status()
Bash: python -c "from pathlib import Path; r=Path('C:/Users/atayl/Desktop/Excluded'); print(sum(1 for _ in r.rglob('*') if _.is_file()))"
```

If FTS5 is stale (last_build > 24h old) or docs-rag reports gaps, flag it in the output and suggest `/ex-refresh` before proceeding. Do not abort — proceed with whatever is current.

### Phase 1 — Structural map

Read in parallel:
- `UNIFIED_KNOWLEDGE_BASE/04_Architecture/Excluded_Knowledge_Base_Architecture.md` — what's in Excluded/, how indexes work
- `UNIFIED_KNOWLEDGE_BASE/04_Architecture/ExcludedDaemon_Agentic_RAG_Spec.md` — only if building daemon this session
- Output of `Glob: C:/Users/atayl/Desktop/Excluded/*` (top-level folders)

### Phase 2 — Memory prime (curated synthesis)

Read the MEMORY.md index + the topic files routed to the current scope:

**Default (no arg):** all of the following in parallel:
- `~/.claude/projects/C--Users-atayl-VoxCore/memory/MEMORY.md`
- `memory/case-status.md`
- `memory/case-filings-tracker.md`
- `memory/case-contacts.md`
- `memory/recent-work.md`
- `memory/user-profile.md`
- `memory/finances-overview.md`
- `memory/career-package.md`

**`case`:** case-status, filings-tracker, contacts, case-evidence-index-part1/2/3, case-emails-index, mh-records-extracted, ides-process, case-audio-recordings
**`career`:** user-profile, career-package, resume-package
**`finance`:** finances-overview, angel-va, ai-subscription-audit
**`brand`:** brand-and-business, brand-expansion-revenue
**`fast`:** MEMORY.md only

### Phase 3 — Living documents (if present)

Read in parallel (skip if not present — do not create):
- `C:/Users/atayl/Desktop/Excluded/IMPORTANT DOCS/Monday_HAF_Call_13Apr2026/00_CALL_BRIEF.md` (if current)
- `C:/Users/atayl/Desktop/Excluded/IMPORTANT DOCS/Case_Reference/__MASTER DOCUMENTS/MASTER_00_EXECUTIVE_SUMMARY.md` (if exists)
- `doc/session_state.md` (always)
- `todo.md` or `todo.md` from memory
- Latest `AI_Studio/Reports/sme_*/README.md` files (most recent 3)

### Phase 4 — Anchor queries (calibration)

Run 5 anchor queries across both indexes. These confirm retrieval works and provide concrete content as context:

```bash
# Structural — who/what/when anchors
python tools/excluded_fts_build.py --query '"ADSCD"'
python tools/excluded_fts_build.py --query '"Tolin"'
python tools/excluded_fts_build.py --query '"Constance Williams"'
python tools/excluded_fts_build.py --query '"NARSUM"'
python tools/excluded_fts_build.py --query '"DCSA SIR"'
```

And one semantic query to verify ChromaDB is healthy:
```
mcp__docs-rag__docs_rag_search(query="most urgent pending filings this week", top_k=5)
```

If any anchor returns zero hits, note it — likely means the corpus has drifted or a key synthesis file has been renamed.

### Phase 5 — Synthesis output

Produce a compact Ready Report:

```
## /ex-sme — [scope] — ready

### Corpus footprint
- Excluded/: X files, Y GB, Z folders
- FTS5 index: N chunks (last built: DATE)
- docs-rag: M chunks
- mbox: K messages (verified live)

### Loaded memory (N topic files)
[single-line list of topic files read, with 1-word domain tag each]

### Current posture (3 sentences max)
[synthesize from case-status.md + filings-tracker.md — what's blocking, what's urgent, what's recent]

### Top 5 live issues (pulled from loaded content)
1. [deadline or blocker] — [why it matters]
2. ...

### Anchor query health
- ADSCD query: N hits (expected ≥5)
- Tolin query: N hits (expected ≥20)
- Constance Williams: N hits
- NARSUM: N hits
- DCSA SIR: N hits
[Flag any that returned 0]

### What I did NOT load
- [list skipped topic files — e.g. "skipped brand/ since scope=case"]

### Ready for:
- Deep cross-folder questions via `/ex-ask`
- Filing drafts via `/filing-prep`
- Executive summaries via `/one-pager [audience]`
- Timeline construction via `/case-timeline`

Ask me anything about the corpus.
```

### Phase 6 — Session flag

Write a timestamp flag:
```bash
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) scope=<scope>" >> AI_Studio/Reports/ex_sme_primes.log
```

This lets `/ex-posture` know the session has been primed and skip redundant loads.

## Constraints

- **Parallel reads.** All memory files in one batch; all anchor queries in one batch.
- **Short output.** The value is in what Claude internalized, not what it prints.
- **No fabrication.** Every claim cites a loaded file or query result.
- **Fast mode exists for a reason** — if the user just wants a quick context load before a narrow task, `fast` scope takes <5 seconds.
- **No cron, ever.** If scheduled priming is desired, route through Task Scheduler or the daemon's asyncio loop — never `CronCreate`.

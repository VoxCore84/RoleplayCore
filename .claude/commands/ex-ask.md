---
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(python:*), Agent, TaskCreate, TaskUpdate, mcp__docs-rag__*, mcp__arcanum__*, mcp__local-llm__*
description: Use when you have a specific question about the legal case, career package, finances, brand, or anything in Excluded/ and need a cited, evidence-rated answer. Fans out 4 parallel agents (evidence + mbox + regulation + timeline), reranks, reflects, and returns with confidence tier.
---

# /ex-ask — Swarm Answer with Citations

The killer utilization command. Uses named agentic patterns from the UKB playbook to turn a question about `Excluded/` into a cited, evidence-rated answer.

**Patterns in use** (UKB Playbook 10 §18):
- **Planning** — Phase 0 decomposes the question
- **Multi-Agent Supervisor + Tool Use** — Phase 1 fans out 4 typed agents
- **Hybrid retrieval (RRF)** — each agent calls both FTS5 and ChromaDB through `tools/excluded_hybrid_search.py`
- **Reranking** — Phase 1.5 uses local-llm to classify each candidate as relevant/marginal/irrelevant
- **Reflection** — Phase 2.5 self-critiques the answer against its own citations
- **Completion Integrity** — Phase 3 enforces cited-claims-only discipline

## Invocation

`/ex-ask <question>` — examples:
- `/ex-ask what is the exact sequence of events that led to the ET obstruction?`
- `/ex-ask do we have proof that McMaster contacted AFPC, independent of Adam's own reporting?`
- `/ex-ask what is Amy Little's role and what is the Monday call about?`

If no argument, ask the user what they want to know.

## P0 Constraints

- **NEVER run maintenance mid-query.** No `/ex-refresh`, `/ex-absorb`, ChromaDB rebuild, extract_cache, or daemon trigger inside this command. If retrieval is thin, say so in the Gaps section. The user runs `/ex-refresh` explicitly. See Session Failure Retrospective for why this matters.
- **NEVER use CronCreate.** If a scheduled variant is wanted, it goes in the daemon's asyncio loop.
- **Every non-trivial claim requires a source citation** — file path + chunk/line. See `.claude/rules/excluded-corpus.md`.
- **Case_Reference/ is read-only.** Agents may read; may not write.

## Workflow

### Phase 0 — Plan (Planner pattern)

Before spawning agents, decompose the question:

1. **Classify** the question (one or more):
   - *Evidentiary* — "do we have proof that X?"
   - *Chronological* — "what happened between X and Y?"
   - *Person* — "everything about person X"
   - *Regulatory* — "what regulation requires X?"
   - *Strategic* — "should we do X given Y?"
   - *Status* — "where does X stand right now?"

2. **Identify entities** — people, orgs, dates, case numbers, filings referenced. Feed into later phases.

3. **Detect the gotcha** — one assumption in the question that, if wrong, changes the answer. State it.

4. **Select agents** — not every question needs all 4:
   - Evidentiary → Evidence + (Mbox if people involved) + Timeline
   - Regulatory → Regulation + Evidence
   - Person → Evidence + Mbox + Timeline
   - Status → Evidence + Timeline
   - Strategic → all 4

5. **Write the plan briefly to the user** so they can correct course before work begins.

### Phase 0.5 — SME sentinel check

Check if `/ex-sme` was run this session. If `AI_Studio/Reports/ex_sme_primes.log` has an entry newer than session start, skip the structural-map re-read steps (the SME context is already warm). Otherwise, do a lightweight one-shot read of `memory/case-status.md` to anchor.

### Phase 1 — Fan Out (Multi-Agent Supervisor)

Launch SELECTED agents from Phase 0 SIMULTANEOUSLY in a single message:

1. **Evidence agent** (subagent_type: `case-researcher`)
   - Tools: Read, Grep, Glob, `mcp__docs-rag__docs_rag_search`, `mcp__arcanum__arcanum_search`, `Bash(python tools/excluded_hybrid_search.py)`
   - Output: `AI_Studio/Reports/ex_ask_<timestamp>/evidence.md`
   - **Prefer hybrid search**: agent calls `python tools/excluded_hybrid_search.py "<focused query>" --top-k 15 --json` to get RRF-fused results across FTS5 + ChromaDB. Falls back to individual MCP calls if hybrid script unavailable.
   - Mandate: Every claim in output cites a file path. Rate each piece: *documentary* (primary) / *reported* (secondary) / *inferred* (derivative). Max 400 lines.

2. **Mbox agent** (subagent_type: `case-researcher`, mbox-focused)
   - Tools: `mcp__arcanum__arcanum_mbox_search`, `mcp__arcanum__arcanum_mbox_read`
   - Decomposed queries built from entities surfaced in Phase 0.
   - Output: `AI_Studio/Reports/ex_ask_<timestamp>/mbox.md`
   - Quotes headers (From/To/Date/Subject) verbatim for evidentiary use. Max 300 lines.

3. **Regulation agent** (subagent_type: `regulation-lookup`)
   - Tools: Read, Grep, `mcp__arcanum__arcanum_search` (scope=memory+arcanum)
   - Finds specific statute/DoDI/DAFI/case-law. Cites paragraph numbers verbatim.
   - Output: `AI_Studio/Reports/ex_ask_<timestamp>/regulation.md`. Max 200 lines.

4. **Timeline/context agent** (subagent_type: `timeline-builder`)
   - Tools: Read, Grep, `mcp__arcanum__arcanum_search`
   - Each entry: date | event | source file | quoted excerpt.
   - Output: `AI_Studio/Reports/ex_ask_<timestamp>/timeline.md`. Max 300 lines.

**Launch in parallel.** All selected agents in a single tool-use batch.

### Phase 1.5 — Rerank (local-llm classify)

For each agent output, run a quick relevance classification to drop noise before synthesis:

```
mcp__local-llm__local_classify(
    text=<agent output chunk>,
    categories=["directly relevant", "tangentially relevant", "irrelevant"],
    allow_multiple=false
)
```

Drop "irrelevant" chunks. Keep "tangentially relevant" only if the question is strategic or exploratory. This cuts Opus synthesis token cost ~80% on broad-corpus questions (Pattern B from UKB Playbook 01).

If local-llm is unavailable, skip this phase and note it in the report header.

### Phase 2 — Synthesize

Read the filtered agent outputs and produce the final answer.

**Answer structure:**

```
## /ex-ask — [question]

### The short answer
[2-4 sentences, direct, no hedging unless evidence is genuinely uncertain]

### Confidence
[PROVEN / WELL-SUPPORTED / PARTIALLY-SUPPORTED / UNCERTAIN / UNSUPPORTED]
Rationale: [what puts it at this level]

### Key evidence
1. **[Claim 1]** — [file_path:chunk/line] — verbatim quote
2. **[Claim 2]** — ...

### Regulation that applies
- [statute/paragraph] — verbatim — [why it applies]

### Timeline
| Date | Event | Source |
|------|-------|--------|
| ... | | |

### Gaps / what we DON'T have
- [what's missing that would strengthen the answer]

### Contradictions (if any)
[explicit list where sources disagree]

### Reports written
- AI_Studio/Reports/ex_ask_<timestamp>/evidence.md
- AI_Studio/Reports/ex_ask_<timestamp>/mbox.md
- AI_Studio/Reports/ex_ask_<timestamp>/regulation.md
- AI_Studio/Reports/ex_ask_<timestamp>/timeline.md
```

### Phase 2.5 — Reflect (Reflection pattern)

Before delivering, run a self-critique against the draft:

1. **Does every non-trivial claim have a source citation?** If any don't, either cite or drop the claim.
2. **Does each cited source actually contain the quoted text?** Spot-check 3 random citations by reading the source file. Flag if drift.
3. **Is the confidence level honest?** If evidence is thin, drop to UNCERTAIN/UNSUPPORTED. Inflated confidence is worse than honest gaps.
4. **Did I surface contradictions, or smooth them?** Re-read agent outputs for disagreements I missed.
5. **Am I answering what was asked, or drifting?** Re-read the original question.

If the reflection uncovers issues, patch and re-flect. If it still fails after 2 cycles, deliver with a `[SELF-AUDIT FAILED: <reason>]` tag prepended to the answer.

### Phase 3 — Persist + emit

Append to answer index (Pattern D from UKB):
```
AI_Studio/Reports/ex_ask_index.jsonl
```
One JSON line: `{ts, question, files_cited, confidence, scope_agents, self_audit_passed}`. Enables future /ex-posture to say "this question was answered N sessions ago with confidence X — want the cached answer?"

Also append to the episodic session log (Pattern J from UKB):
```bash
python tools/excluded_session_log.py --command ex-ask \
    --question "<original question>" \
    --summary "<2-sentence synthesis>" \
    --confidence "<PROVEN|WELL-SUPPORTED|...>" \
    --files <path1> <path2> ...
```

This adds one row to `memory/excluded-session-log.md` (human-readable) and one JSONL record to `memory/excluded-session-log.jsonl` (machine-readable). Legal audit-trail value: attorneys can grep "when did we first surface X" against this log.

## Gotchas (known failure modes)

1. **Mbox deleted-then-archived messages return headers only** — `body_text` is empty. False confidence risk. Always check non-empty body before citing. Use `has_body=1` filter where available.
2. **ChromaDB ranks emotional language high** — "I was devastated" may outscore a dry DoDI paragraph. Cross-check regulatory claims with FTS5 keyword hits. RRF fusion helps but doesn't eliminate this.
3. **OCR on scanned military records misreads AFSC codes and dates** — 2/Z, 0/O confusion, slash→dot. When AFSC or date matters, quote the raw image path so the user can verify visually.
4. **Duplicate chunks at `extracted/` and `Case_Reference/extracted/` source roots** for the same file — different rel_path bypasses dedup. Treat as one source; pick the shorter citation.
5. **Synthesis pulling from ChatGPT meta docs as if they were primary evidence** — `Chat GPT Meta for Case.docx` under `13_ANALYSIS_AND_BRIEFS/` is AI analysis, not primary documentation. Tag as *inferred*, not *documentary*.
6. **Timeline agent conflating date-of-email with date-of-event** — an email sent 2026-04-08 that references an event from 2024-11 should cite the 2024-11 date for the event, not 2026-04-08.

## Constraints

- Every non-trivial claim → file path citation. No exceptions.
- Confidence must be honest. UNSUPPORTED is a valid verdict.
- Agents write to files, not to conversation. Keeps context clean.
- Parallel, not sequential. Single tool-use batch for Phase 1.
- Case_Reference/ is read-only.
- Gaps section is mandatory — every answer states what's missing.
- Self-audit is mandatory — Phase 2.5 runs on every response.
- **No maintenance mid-query** — see P0 Constraints.

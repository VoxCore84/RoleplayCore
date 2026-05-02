# VoxCore Session Handoff — Apr 27-28 2026 (Session 273) — RECONSTRUCTED

> **[RECONSTRUCTED on 2026-05-02]** — This handoff was NOT written contemporaneously at the end of session 273.
> It is a deterministic template fill from the memory files listed in the Sources footer.
> A reader citing facts from this document should cross-verify against the primary sources.
> This is a back-fill so the `AI_Studio/Handoffs/voxcore/` folder has a complete audit trail; it is not a substitute for a real handoff.

**Session:** 273
**Date:** Apr 27-28 2026
**Title:** Knowledge Graph build + Triad model upgrade + filing prompts
**Commit (best-guess from `git log --grep`):** NOT FOUND
**Source provenance:** see footer

---

## What Happened (from recent-work.md)

- **Built daemon Phase D: Knowledge Graph** — 6 new files in `tools/excluded_daemon/kg/` and `workers/llm_worker.py` + `jobs/contradiction.py`. SQLite entity DB at `.cache/excluded_kg.db`. Full NER build across 1,484 extracted files using dual-backend (Ollama qwen3.5:27b + Anthropic Sonnet API round-robin with 15 parallel workers). Final: **24,854 entities, 177,703 mentions, 759,669 relations**. Entity kinds: 6,657 amounts, 6,430 orgs, 3,377 regulations, 3,289 persons, 2,581 case numbers, 2,520 dates. Zero-failure NER after defensive type-guard patches (LLM returns string-instead-of-dict + None values).
- **Updated Triad model architecture**: Gemini 2.5-pro → 3.1-pro, Claude cold-reader sonnet-4-6 → opus-4-7 across all 11 files (scripts, Central Brain, memory, /triad skill). ChatGPT/Codex already at gpt-5.4.
- **DD 7050 back under consideration**: Updated case-status.md and case-filings-tracker.md. Strategic rationale: complementary to DD 2910-2 (different legal lens on same adverse actions), evidence grown massively since Mar 16 draft, DoD IG SA retaliation team is different from exhausted standard IG channels.
- **Filing tab prompts**: Wrote comprehensive self-contained prompts to Desktop for DD 2910-2 (SAPR Retaliation) and DD 7050 (Whistleblower Reprisal) tabs.
- **Ran first contradiction scan**: 58 hits (mostly false-positive date co-occurrences — scanner v2 needs semantic comparison, not just date matching).
- **Verified Ollama + local LLMs healthy**: qwen3.5:27b, gemma4:26b, nomic-embed-text, snowflake-arctic-embed, bge-large all available.
- Commit: `e9d1419f9e`


---

## Automation Ledger Entry (from automation-ledger.md)

**Built**:
- `/kg-query` — slash command exposing KG entity API
- `tools/excluded_daemon/kg/` — entity/mention/relation SQLite database, NER worker, dedup utility, query layer
- `tools/excluded_daemon/workers/llm_worker.py` — daemon LLM dispatch with dual-backend round-robin
- `tools/excluded_daemon/jobs/contradiction.py` — synthesis-vs-source contradiction scanner v1

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | Ollama qwen3.5 stashes JSON in `thinking` field instead of `response` | NEW | `llm`, `kg` | Read from `thinking` field + type guards | LOW | DONE |
| 2 | LLM type variability (string vs dict, None vs "") crashed build twice | NEW | `llm`, `kg` | Defensive type-guard pattern library | LOW | DONE |
| 3 | KG build crashes lose work | NEW | `kg`, `daemon` | Crash-resume via `already_seen` content-addressed set | LOW | DONE |
| 4 | Cautious worker ramp-up wasted ~30 min | NEW | `daemon`, `kg` | Start parallel-heavy from session 1 | LOW | DEFERRED (mindset, not code) |
| 5 | Contradiction scanner v1 false positives (date co-occurrence ≠ contradiction) | NEW | `audit`, `kg` | Semantic comparison instead of date overlap | MED | QUEUED |
| 6 | No `/kg-query` skill — KG only reachable via Python CLI | NEW | `kg`, `skill` | Build slash command | LOW | DONE |
| 7 | UKB `06_Case_Intelligence/` not updated with KG pipeline doc | NEW | `legal`, `kg` | Write pipeline doc | LOW | QUEUED |

**Compounding**: 2/7 by tag-overlap, 3/7 with judgment
- Tag-matched: #3 (`daemon` ↔ s.269/272), #6 (`skill` ↔ s.263 combo skills, s.267 `/triad`)
- Judgment-additional: #1,#2 (`llm` defensive coding) ↔ session 244 config-API verification mismatch (same "verify before assuming" class)
- Note: KG/NER is a new domain in s.273, so most pains are NEW. Future KG-adjacent sessions should show much higher overlap.

---

---

## Resume Evidence (from resume-evidence.md)

**Quantifiable**: 24,854 entities, 177,703 cross-document mentions, 759,669 relations from 1,484 legal source documents. Dual-backend NER pipeline (Ollama qwen3.5:27b + Anthropic Sonnet API, 15 parallel workers) completed in 2.5 hours. Zero-failure after defensive type-guard patches. 6 entity kinds extracted: 6,657 amounts, 6,430 organizations, 3,377 regulations, 3,289 persons, 2,581 case numbers, 2,520 dates.
**Technical**: SQLite-backed Knowledge Graph (3 tables: entities, mentions, relations). GraphRAG architecture with triple-channel retrieval (FTS5 keyword + ChromaDB vector + entity-linked KG mentions) fused via Reciprocal Rank Fusion (k=60). Cross-encoder reranking via BGE-reranker-v2-m3. Crash-resume via content-addressed `already_seen` set.
**Outcome**: Sub-second entity resolution across 17 GB heterogeneous corpus; enables 100%-cited legal filings.
**STAR bullet**: Built a 25,000-entity Knowledge Graph from 1,484 legal documents using a dual-backend (local 27B + cloud API) NER pipeline with 15 parallel workers and crash-resume — completing in 2.5 hours what would have taken 10+ hours sequentially.
**Tags**: `kg`, `ner`, `rag`, `legal`, `daemon`, `llm`


---

## Sources

This reconstructed handoff was generated by `tools/backfill_handoffs.py` on 2026-05-02 from:

- `memory/recent-work.md` lines 54-63 — primary activity log
- `memory/automation-ledger.md` lines 161-187 — pain→fix entries + compounding score
- `memory/resume-evidence.md` lines 59-66 — STAR bullet + measurables
- git commit: NOT FOUND via `git log --all --grep "session 273"` — session may not have produced a single named commit

To verify any specific claim, open the cited file at the cited line range and read the primary entry.

---

*Reconstructed handoff — DO NOT cite externally without verification against the primary memory files. For going-forward sessions, `/wrap-up` Step 6.5 writes contemporaneous handoffs to this folder automatically.*

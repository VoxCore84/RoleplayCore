# VoxCore — GraphRAG Readiness Assessment
**Last updated:** 2026-05-26
**Status:** DOCUMENTATION ONLY — no implementation work performed.

---

## IMPORTANT: WHAT THIS DOCUMENT IS NOT

**WE ARE NOT BUILDING GRAPHRAG IN THIS SESSION.**

This document records the current state of retrieval and KG infrastructure, explains the gap between what exists and full GraphRAG, and captures a paste-ready implementation brief for a future session that has explicit Adam GO. Nothing in this file authorises any code change, daemon restart, or server modification.

---

## 1. What Retrieval / KG Capabilities Exist Today

### 1.1 The Three-Layer Index (all LIVE as of 2026-05-26)

| Index | Location | Size | What it covers |
|-------|----------|------|----------------|
| FTS5 keyword index | `.cache/excluded_fts.db` | 173 MB | Full-text search, 20,807 chunks |
| ChromaDB vector store | `.cache/rag/chroma/` | 477 MB | Semantic similarity, nomic-embed-text 768-dim, 24,930 chunks |
| Knowledge Graph | `.cache/excluded_kg.db` | 272 MB | Co-mention entity graph, 24,640 entities / 743,207 relations |

### 1.2 The Hybrid Retrieval Pipeline (LIVE)

**Entrypoint:** `tools/excluded_hybrid_search.py`

The production retrieval path fuses all three layers via Reciprocal Rank Fusion (RRF, k=60):

1. **FTS5 channel** — keyword hits against `.cache/excluded_fts.db`
2. **Vector channel** — ChromaDB nearest-neighbour over `nomic-embed-text` embeddings
3. **KG entity-match channel** — entity co-mention boost: if query terms resolve to known entities, chunks co-mentioning those entities get a score lift

All three scores are merged with RRF and the top-k results are returned. No multi-hop graph traversal. No community detection. No global synthesis.

### 1.3 MCP Exposure of KG (LIVE)

The `docs-rag` MCP server (`tools-dev/docs-rag/docs_rag_server.py`) exposes four KG tools that read directly from `.cache/excluded_kg.db`:

- `kg_entity` — fuzzy-match a name to canonical entities
- `kg_mentions` — all document chunks mentioning a given entity
- `kg_relations` — 1-hop or multi-hop BFS traversal between entities
- `kg_stats` — entity/mention/relation counts by kind

These tools are LIVE and callable in-session. They are wired to the same `excluded_kg.db` as the hybrid retrieval pipeline (config source: `tools-dev/docs-rag/docs_rag_logic.py`, `config.py:130`).

### 1.4 The Eval Baseline (LIVE + REPRODUCIBLE)

- **Headline:** 92.0% pass rate (46/50 gold-set queries)
- **Run ID:** `43b4e9ba4752a6fc` — artifact on disk at `.cache/runs/43b4e9ba4752_20260504T141540Z.json` (116 KB)
- **Corpus snapshot:** `23e51aac827e860a` — artifact at `.cache/corpus_snapshots/23e51aac827e_20260504T050519Z.json` (655 KB)
- **Gold set:** `.cache/gold_sets/retrieval_test_suite_v1.json` (50 queries, v1)
- **Pareto report:** `reporting/PARETO_2026-05-04.md` — cites both run IDs; production config is `fts_vec_kg_k60` (92.0% / 2181 ms mean latency)
- **Reproducibility caveat:** ChromaDB has tie-break non-determinism on rank ordering of non-passing queries; the headline pass rate (46/50 = 92.0%) is stable across re-runs (documented at `retrieval/HYDE_DECISION.md`)

---

## 2. Why Current KG-Enhanced Retrieval Is NOT Full GraphRAG

The current system is a **co-mention entity boost** grafted onto an RRF retrieval stack. This is meaningfully different from GraphRAG in four ways:

### 2.1 All Relations Are `mentioned_with` (Homogeneous)

Every one of the 743,207 relations in `excluded_kg.db` has `predicate = 'mentioned_with'`. This is a co-occurrence signal, not a semantic relationship. The schema (`tools/excluded_daemon/kg/schema.sql`) has a `predicate` column, but the build pipeline inserts only `'mentioned_with'` at every relation.

Source: `tools/excluded_daemon/kg/build.py:411` — the only INSERT into the relations table.

This means the graph carries no typed information: you cannot ask "who issued what order to whom" or "which regulation contradicts which claim." You can only ask "which entities appeared near which other entities."

### 2.2 No Graph Traversal in Retrieval

The retrieval pipeline (`tools/excluded_hybrid_search.py`) does not walk edges. The KG channel is an entity-ID lookup followed by a chunk-level score boost. The graph topology (who connects to whom, at what hop depth) is not used during retrieval.

In contrast, GraphRAG-style retrieval would traverse edges to find related entities, pull their associated chunks, and synthesise across them — producing answers that span documents that do not individually contain the query terms.

### 2.3 No Community Detection / Global Synthesis

Full GraphRAG (Microsoft MSFT-2024 formulation) builds hierarchical communities (Leiden algorithm) over the entity graph, generates community-level summaries, and answers global queries by aggregating across summaries. None of this exists. `graphrag/PLAN.md` contains the architecture for this but is a scaffold with zero production code. `igraph` (required for Leiden) is not installed.

### 2.4 No Contradiction / Multi-Predicate Inference

`contradiction/PLAN.md` describes a cross-source contradiction detection system using typed predicates. Its own documentation states: "Predicate typing is the precondition." That precondition is unmet. Until typed edges exist, contradiction detection cannot be built.

---

## 3. What Typed-Edge Schema Is Needed

The existing schema already has the column; the build pipeline needs to populate it with meaning.

### Required Schema Change (no DDL needed — column already exists)

```sql
-- Current state (all rows look like this):
-- INSERT INTO entity_relations (entity_a_id, entity_b_id, predicate, confidence, source_chunk_id)
-- VALUES (42, 99, 'mentioned_with', 1.0, 'chunk_abc');

-- Target state (varied predicates):
-- ('ISSUES_ORDER_TO', 'RETALIATES_AGAINST', 'REFERENCES_REGULATION',
--  'CONTRADICTS', 'SUPPORTS', 'EMPLOYS', 'SUPERVISES', 'AUTHORED_BY')
```

### Predicate vocabulary needed (minimum viable set)

| Predicate | Example | Source signal |
|-----------|---------|---------------|
| `ISSUES_ORDER_TO` | Commander → Subordinate | Action verbs in clinical/command text |
| `REFERENCES_REGULATION` | Document → DoDI/USC | Regex on regulatory citation patterns |
| `SUPPORTS` | Evidence chunk → Claim | LLM triple-extraction |
| `CONTRADICTS` | Finding A → Finding B | LLM comparison |
| `AUTHORED_BY` | Document → Person | Document metadata |
| `SUPERVISES` | Person A → Person B | Org chart signals |

Extraction approach: Sonnet 4.6 per-chunk triple extraction (planned in `contradiction/PLAN.md`) at an estimated ~$0.003/chunk × 20,807 chunks ≈ ~$60 extraction cost, one-time.

---

## 4. What Files Build KG Relations Today

The KG build pipeline lives entirely in `tools/excluded_daemon/kg/`:

| File | Role |
|------|------|
| `tools/excluded_daemon/kg/build.py` | Main pipeline: NER → entity resolution → co-mention relation INSERT. Line 411 is the only relation INSERT (predicate hardcoded to `'mentioned_with'`). |
| `tools/excluded_daemon/kg/schema.sql` | SQLite DDL: `entity_relations` table with `predicate TEXT` column (populated monotonically by build.py). |
| `tools/excluded_daemon/kg/query.py` | Read-only query helpers imported by `docs-rag` MCP tools (`kg_entity`, `kg_mentions`, `kg_relations`, `kg_stats`). |
| `tools/excluded_daemon/kg/ner.py` | Named-entity recognition: extracts persons, orgs, regulations, dates, amounts, case_numbers from chunk text. |
| `tools/excluded_daemon/kg/entities.py` | Entity resolution: deduplication + canonical-name assignment. |
| `tools-dev/docs-rag/docs_rag_logic.py` | MCP server logic; imports `tools.excluded_daemon.kg.query` at lines 602/625/649/667/682 to serve the four `kg_*` MCP tools. |

The excluded-corpus daemon orchestrates the full pipeline (extract → NER → KG build → ChromaDB embed → FTS5 index). The daemon is PARTIAL with 6 known reliability issues documented at the backlog pointer below.

---

## 5. What Eval Baseline Must Be Preserved

The 92.0% baseline is the ground truth for any future retrieval work. It must not be invalidated before a new baseline replaces it.

### Provenance (do not delete these files)

```
.cache/runs/43b4e9ba4752_20260504T141540Z.json          (116 KB — run record)
.cache/corpus_snapshots/23e51aac827e_20260504T050519Z.json  (655 KB — corpus snapshot)
.cache/gold_sets/retrieval_test_suite_v1.json           (50 queries — gold set v1)
reporting/PARETO_2026-05-04.md                          (21-config Pareto sweep results)
```

### What must not change before a new baseline is captured

- Do not rebuild the ChromaDB index (`tools-dev/docs-rag/docs_rag_logic.py` rebuild path) unless a new run is recorded first
- Do not rebuild `excluded_fts.db` without recording a pre-rebuild run
- Do not modify `tools/excluded_hybrid_search.py` without reconciling its 105 uncommitted insertions (Phase 4 HyDE refactor) first — the core RRF path is intact, but the diff must be committed or discarded before further edits
- Do not modify `tools/quality_probe.py` without reconciling its 23 uncommitted insertions
- The gold set v1 (`retrieval_test_suite_v1.json`) is the measurement instrument — do not edit it

---

## 6. What A/B Design to Use for GraphRAG Evaluation

When GraphRAG prototype work is authorised, use this A/B structure:

```
Control:  tools/excluded_hybrid_search.py (current FTS+vec+KG-boost RRF)
          run_id: 43b4e9ba4752a6fc  pass_rate: 92.0%  latency: 2181ms

Treatment: graphrag_retrieval.py (new — Leiden community + global synthesis layer)

Gold set: retrieval_test_suite_v1.json (50 queries) — IDENTICAL to control
Runner:   tools/quality_probe.py — same harness, same snapshot

Report dimensions:
  - pass_rate (primary)  — target: >= 92.0% (no regression acceptable)
  - MRR (secondary)      — must not regress below control MRR
  - mean_latency         — cost dimension; acceptable regression defined in advance
  - per-query drill-down — every regression listed individually (no-cherry-pick rule)

Tie-break rule (declare in advance): if pass_rate tied, prefer lower latency.
```

Run both variants against the same corpus snapshot (`23e51aac827e860a`). Record a new run_id for the treatment. Never mix run records from different snapshots.

---

## 7. What Counts as a Successful GraphRAG Prototype

A prototype is successful when ALL of the following are true:

1. **Typed edges exist in `excluded_kg.db`** with at least 3 distinct non-`mentioned_with` predicates populated for >= 1,000 entity pairs
2. **Pass rate >= 92.0%** on the v1 gold set (no regression on control baseline)
3. **At least one global query answered** that the control system returned UNSUPPORTED — demonstrating cross-document synthesis capability
4. **Community summaries generated** for at least the top-5 Leiden communities by entity count
5. **MRR not regressed** below control value
6. **Latency budget declared** and prototype measured against it (even if it exceeds — the number must exist)

---

## 8. What Counts as Failure / No-Go

Stop and do not proceed if:

- Pass rate drops below 92.0% on any run against v1 gold set
- MRR regresses by more than 0.05 below control without a documented explanation
- The typed-edge extraction LLM judge disagrees with ground-truth spot-checks on > 20% of sampled triples (inter-rater reliability gate)
- `igraph` / Leiden installation breaks any existing import in the retrieval stack
- Any of the four provenance artifacts (run record, snapshot, gold set, PARETO doc) are modified or deleted

If any no-go condition fires: stop, document in a `graphrag/ABORT_<date>.md` file, restore the system to the pre-experiment state, and get Adam GO before trying again.

---

## 9. What Must NOT Change Before the Baseline Is Captured

(Abbreviated — full detail in section 5 above)

- Do not touch `.cache/runs/`, `.cache/corpus_snapshots/`, or `.cache/gold_sets/`
- Do not rebuild the vector or FTS5 index
- Do not commit or amend `tools/excluded_hybrid_search.py` without recording a new run first
- Do not install new Python packages into the retrieval stack environment without verifying they do not conflict with ChromaDB or FTS5 deps

---

## FUTURE IMPLEMENTATION PROMPT — NOT FOR THIS SESSION

> **DO NOT EXECUTE.** Copy-paste this prompt into a new Claude Code session after Adam GO is given for GraphRAG work. Prerequisites: typed edges built, baseline re-verified, Adam GO documented.

```
=== GRAPHRAG IMPLEMENTATION BRIEF (paste into new session, Adam GO required) ===

Prerequisite checks (run before writing any code):
1. Verify .cache/excluded_kg.db exists and contains > 1,000 non-'mentioned_with' relations.
   SELECT predicate, COUNT(*) FROM entity_relations GROUP BY predicate;
   Expected: at least 3 predicate types besides 'mentioned_with'.

2. Verify baseline still holds:
   python tools/quality_probe.py --engine hybrid --output .cache/runs/pre_graphrag_baseline.json
   Expected pass_rate >= 92.0%. If not, STOP and investigate before proceeding.

3. Verify igraph installed without breaking imports:
   python -c "import igraph; from tools.excluded_daemon.kg.query import get_entity_relations; print('OK')"

Implementation steps (in order, do not skip):
Step 1 — Community detection
  File: graphrag/community_builder.py (new)
  Action: Load excluded_kg.db entity_relations (typed edges only, exclude 'mentioned_with').
          Run igraph Leiden over entity nodes. Write community assignments to
          excluded_kg.db table: entity_communities(entity_id, community_id, level INT).
          Log community count and top-5 by size.

Step 2 — Community summaries
  File: graphrag/summarizer.py (new)
  Action: For each community, fetch all chunk text for member entities via kg_mentions.
          Call local_summarize (local-llm MCP, Qwen, $0) with focus="key facts and relationships".
          Store summaries in excluded_kg.db: community_summaries(community_id, summary TEXT, chunk_count INT).

Step 3 — Global retrieval wrapper
  File: graphrag/retrieval.py (new)
  Action: Accept query string. Run existing hybrid pipeline (import excluded_hybrid_search).
          Additionally: resolve query entities → find their community_ids → pull community summaries
          for top-3 communities → prepend to context window.
          Return: {hybrid_results: [...], community_context: [...], synthesis_prompt: str}

Step 4 — A/B eval
  Run: python tools/quality_probe.py --engine graphrag --output .cache/runs/graphrag_v1.json
  Compare against run_id 43b4e9ba4752 (control).
  If pass_rate < 92.0% or MRR regresses > 0.05: STOP, file ABORT doc, restore.
  If successful: write graphrag/GRAPHRAG_BASELINE_<date>.md with full provenance.

Adam GO is required before Step 1. Do not start on scaffold or PLAN.md alone.
=== END OF FUTURE BRIEF ===
```

---

## References

- `tools/excluded_daemon/kg/build.py:411` — source of `mentioned_with` constraint
- `graphrag/PLAN.md` — architecture scaffold (0 production code)
- `contradiction/PLAN.md` — blocked on typed edges
- `retrieval/HYDE_DECISION.md` — HyDE killed (-10pp), methodology for A/B design
- `reporting/PARETO_2026-05-04.md` — 21-config sweep, 92.0% at `fts_vec_kg_k60`
- `tools-dev/docs-rag/docs_rag_logic.py` — MCP KG tools (lines 602–682)
- `AI_Studio/Reports/system_inventory_2026-05-26/cat_A_graph_rag_kg.md` — full inventory evidence

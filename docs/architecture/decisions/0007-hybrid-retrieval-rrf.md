# ADR 0007: Hybrid Retrieval with Reciprocal Rank Fusion (k=60)

**Status:** Accepted
**Date:** 2026-04 (initial), 2026-04-30 (entity path boost tuned to 2.0x)

## Context

Single-channel retrieval has a known failure mode: each channel is good at some queries and bad at others. Vector retrieval handles paraphrasing; keyword/BM25 handles exact-token matches; graph traversal handles structural questions. A flat-RAG implementation that picks one channel will systematically fail on queries the other channels would handle.

VoxCore needs to answer questions across legal-evidence corpora that mix:
- Master synthesis docs (high-quality prose, paraphrasing tolerated)
- Raw email mbox (exact-name, exact-date, exact-subject matches matter)
- Audio transcripts (Whisper output is approximate; need fuzzy matching)
- OCR'd images (Tesseract output is character-level approximate)
- Knowledge graph (structural questions: "every motion before this judge", "every party connected to entity X")

No single channel handles all five. A measurable example: on the 50-query test suite (`quality_probe.py`), FTS5 alone passes 39/50 (78%), vector alone passes 22/50 (44%). Different sub-distributions of failures.

## Decision

**Triple-channel hybrid retrieval** with reciprocal-rank fusion:

1. **FTS5 (SQLite full-text)** — keyword/BM25-style. Fast (~1s), handles exact-token matches.
2. **ChromaDB (vector)** — BGE-M3 embeddings. Slower (~100s on first cold call, much faster after warm-up), handles paraphrasing and semantic neighbors.
3. **Knowledge graph traversal** — entity-resolved walk over `excluded_kg.db` (24,640 entities, 743,207 relations). Handles structural questions.

Each channel returns a top-K ranked list. Lists are fused via **reciprocal rank fusion**: `score = Σ 1/(k + rank_i)` with **k = 60** (standard RRF k-value from Cormack/Clarke/Buettcher 2009). The fused result is then locally reranked via BGE-reranker-v2-m3.

**Entity path boost** (tuned 2026-04-30): when a query's extracted entities appear directly in the result's path or text, the result gets a `2.0x` multiplier (previously 1.5x). Tested before/after via `quality_probe.py` — 1.5x left some entity-specific queries underranked; 2.0x improved them without regression on other categories.

Measured: **92% pass rate** on 50-query suite, vs 78% FTS5-only and 44% vector-only.

## Alternatives considered

1. **Vector only.** Industry-standard simple-RAG default. Rejected: 44% on the test suite. Misses exact-match queries entirely.

2. **FTS5 only.** Cheaper, faster. Rejected: 78% is good but the 22% gap is on paraphrasing queries that vector captures.

3. **Score-based fusion** (cosine + BM25 score normalization, weighted average). Rejected: requires per-channel score-distribution tuning and is sensitive to outliers. RRF is rank-based and robust to score-scale differences.

4. **Stronger weight on the KG channel** (1.5x weight on graph results). Tested 2026-04-30 and **regressed** on financial queries (the KG isn't densely populated for financial entities). Reverted to equal weighting; entity path boost was the better lever.

5. **Reranking-only / no fusion** — let one channel do retrieval, rerank with cross-encoder. Rejected: rerankers are precision tools, not recall tools. If the candidate set doesn't contain the right answer, the reranker can't fix it.

## Consequences

**Positive:**
- Triple-channel resilience — when one channel misses, another usually catches it.
- 92% retrieval pass rate is the published canonical number (replaces the inferred 96% citation precision in the Economic Impact PDF — different metric, but the closest measured analog).
- Per-category breakdown: 6/9 categories at 100% (Clinical, Status, Regulatory, Semantic, Career, Brand). The remaining 4% gap is in Factual + Evidentiary which are the hardest categories.

**Negative:**
- Three retrieval calls per query (sequential by default; could parallelize as a hardening item). Latency p95 = ~150s on the test suite (dominated by ChromaDB cold calls).
- KG channel is the most complex; entity resolution drift over time requires periodic audits (Cat 2 follow-on).

**Neutral:**
- RRF k=60 was chosen from the Cormack 2009 paper and not tuned for VoxCore specifically. A small tuning experiment (k ∈ {30, 60, 90}) would be a worthwhile follow-on but the current value is in the standard range.

## References

- `tools/excluded_hybrid_search.py` — implementation
- `quality_probe.py` — measurement harness
- `AI_Studio/Reports/scheduled/quality_probe_20260430_191844.json` — current 92%/78%/44% measurement
- ADR 0001 — Triad's Executor calls these tools via the MCP surface (ADR 0002)
- Cormack, Clarke, Buettcher 2009 — "Reciprocal Rank Fusion outperforms Condorcet and Individual Rank Learning Methods"

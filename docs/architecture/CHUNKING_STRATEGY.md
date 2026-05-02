# Chunking Strategy

**Source of truth:** `tools/excluded_fts_build.py`, `tools/rag_build.py`, `tools/excluded_daemon/config.py`.
**Written:** 2026-05-02.
**Scope:** Closes Verification Master Checklist Cat 2 item: "Chunking strategy in tokens documented (size, overlap, semantic vs fixed)".

## Three chunkers, three uses

Three independent chunkers exist, each tuned for its consumer. They produce different chunks of the same source files because their consumers have different recall/precision tradeoffs.

| Chunker | File | Size | Overlap | Strategy | Consumer |
|---|---|---|---|---|---|
| FTS5 indexer | `excluded_fts_build.py:33-34` | **2400 chars (~600 tokens)** | **400 chars (~100 tokens)** | Fixed-size with trailing-whitespace boundary preference | SQLite FTS5 keyword search (BM25) |
| Vector RAG indexer | `rag_build.py:50-51` | **600 tokens (~2400 chars)** | **100 tokens (~400 chars)** | Fixed-size with sentence-boundary preference (period/newline) | ChromaDB nomic-embed-text vector index |
| KG NER chunker | `excluded_daemon/config.py:140-141` | **2000 chars (~500 tokens)** | **200 chars (~50 tokens)** | Fixed-size, no boundary handling | Per-chunk NER → entity/relation extraction → KG SQLite |

### Why three rather than one shared chunker

- **FTS5** needs slightly larger chunks (better term-density signal for BM25) and overlap on whitespace boundaries (token splits don't matter for keyword search).
- **Vector** needs sentence-boundary respect (mid-sentence cuts produce embeddings that don't match natural query phrasing).
- **NER** needs smaller chunks (the entity extractor's context window is the limiting factor; bigger chunks mean entity-level signal drowns in surrounding text).

Sharing one chunk size would degrade at least one consumer.

## Token-to-character conversion

Internal convention: **4 chars = 1 token**, used as a cheap proxy. Not exact for any specific tokenizer (Claude/OpenAI/sentence-piece all differ ~10–20%) but close enough for budget computations. Written as `CHARS_PER_TOKEN = 4` in `rag_build.py:60`.

For pure token-accurate counts (e.g. when constructing a prompt that must fit in 200K context), use the model's own tokenizer. The 4-char proxy is acceptable for chunking decisions because the embedder/indexer treats input as text not tokens.

## Boundary handling

`excluded_fts_build.py` chunker (`chunk_text` lines 103-130):
- Slides a window of `CHUNK_SIZE_CHARS` with `CHUNK_OVERLAP_CHARS` overlap.
- At each window end, looks back up to 200 chars for a whitespace character; cuts there if found, else cuts at the hard boundary.
- Preserves chunk start/end byte offsets in the FTS row for later citation lookup.

`rag_build.py` chunker (`chunk_text` lines 60-90):
- Same sliding window with overlap.
- Searches the second half of each chunk for `\n\n`, `\n`, `. `, `! `, `? ` (in priority order) to find a sentence boundary.
- Falls back to hard cut if no boundary found in the second half.

`excluded_daemon/kg/build.py` chunker (`_chunk_text` lines 242-260):
- Sliding window with overlap, no boundary preference.
- Pure character-position cuts. Acceptable because NER models are robust to mid-sentence input.

## Semantic chunking — explicit non-decision

We use **fixed-size chunking with boundary preferences**, not semantic/topic-based chunking (e.g. langchain's `SemanticChunker` or unstructured.io's element-based). Reasons:

1. **Determinism.** A fixed chunker produces the same chunks for the same input forever. A semantic chunker depends on a model whose behavior drifts; re-indexing with a new model version produces different chunks for the same file, breaking citation stability.
2. **Speed.** Fixed chunking is sub-millisecond. Semantic chunking adds ~10ms per chunk (model inference) which compounds to hours over a 24K-document corpus.
3. **Correctness.** For legal evidence, the chunk-level claim "this document says X" is more important than "the topic of this region is Y." Fixed boundaries preserve every sentence; topic-based chunkers can drop sentences that don't fit the dominant topic.

Trade-off: a long sentence that crosses a fixed boundary will be split between two chunks. The 400-char (FTS5) and 100-token (vector) overlaps are sized to recover such cases — any sentence ≤400 chars is fully present in at least one chunk.

## Inline citation alignment

Citations from `/ex-ask` and downstream consumers cite `path/to/file:chunk_idx`. The `chunk_idx` is the FTS5 chunker's index (since that's the index the citation_scorer's `verify_quote_in_file` uses for substring lookup). The vector chunker's indices are not surfaced to the user; they exist only for retrieval ranking.

## Verification

| Claim | Evidence |
|---|---|
| FTS5 chunks are 2400/400 chars | `excluded_fts_build.py:33-34` constants |
| Vector chunks are 600/100 tokens | `rag_build.py:50-51` constants |
| KG chunks are 2000/200 chars | `excluded_daemon/config.py:140-141` constants |
| Boundary preference exists | `excluded_fts_build.py:103-130`, `rag_build.py:60-90` |
| No semantic chunker used | grep for `SemanticChunker`, `semantic_chunker`, `topic_chunk` returns empty |
| 4-char/token proxy | `rag_build.py:60` `CHARS_PER_TOKEN = 4` |

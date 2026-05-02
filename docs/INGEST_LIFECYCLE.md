# Ingest Lifecycle

**Closes Verification Master Checklist items:**
- Cat 2: "Query rewriting (HyDE/FastT5) — confirm if actually used in production paths"
- Cat 2: "Staging period for freshly-ingested content documented"
- Cat 6: "No diarization metadata preserved in searchable form — gap noted"
- Cat 6: "Re-ingest mechanism if a model is upgraded"
- Cat 6: "Derived artifacts (transcripts, OCR text, embeddings) versioned with source models"

**Written:** 2026-05-02. Source-of-truth pointers to live code in every section.

---

## Query rewriting — what the production path actually does

**Audit answer:** **VoxCore production retrieval does NOT use HyDE or FastT5 query rewriting.** The verification checklist's gap question can be closed: those techniques were considered, neither was implemented.

What the production hybrid retrieval (`tools/excluded_hybrid_search.py`) DOES do:

| Technique | Where | What |
|---|---|---|
| Acronym expansion | `excluded_hybrid_search.py:63-90` `ACRONYM_MAP` | 20+ case-specific acronyms expanded for FTS5 (NPDB → "National Practitioner Data Bank" etc.) before retrieval |
| Entity detection | `excluded_hybrid_search.py` (entity-density logic) | Known persons from `.cache/persons/persons.json` are detected in the query and used to boost paths containing those entities (2.0× multiplier) |
| Adaptive FTS boost | RRF fusion in `excluded_hybrid_search.py` | When entity density is high, FTS5 weight is bumped (matches behave more like exact lookups) |
| Noise penalties | `excluded_hybrid_search.py:50-58` `NOISE_PENALTIES` | Paths matching `_Needs Sorted/_Archive`, `cr_pages/page_`, `paypal_statement` etc. get scores multiplied by 0.3-0.5 |
| Cross-channel RRF | k=60 across FTS5 + ChromaDB + KG | Reciprocal Rank Fusion of three independent retrievers |
| Optional reranker | `--rerank` flag, BGE-reranker-v2-m3 via Ollama | Off by default; on opt-in for top-precision queries |

**Why not HyDE:** HyDE generates a hypothetical answer with an LLM, then embeds and searches. Adds ~3s + cost per query for marginal recall gain over the existing acronym + entity expansion. Considered and not adopted; documented here so it doesn't keep showing up as an open question.

**Why not FastT5:** FastT5 query rewriting is a transformer query-rewriter trained on labeled query-rewrite pairs. We don't have labeled training data and the marginal gain over acronym expansion is small for this corpus.

**If a future need to add HyDE arises:** the integration point is `excluded_hybrid_search.py` immediately after acronym expansion and before FTS5/vector search. The prompt template should mirror the acronym-expanded query format so RRF fusion still works.

---

## Staging period for freshly-ingested content

**Question the checklist asks:** "Once a new file lands in the corpus, when is it searchable?"

**Operational answer:** **There is no staging period — extraction and indexing are eventually-consistent and depend on which path the daemon is on.**

Two ingest paths exist, with different freshness guarantees:

### Path A — daemon-driven (default)

`tools/excluded_daemon/` runs as a background asyncio loop. The relevant jobs:

| Job | File | Cadence | What it does |
|---|---|---|---|
| Index worker | `excluded_daemon/workers/index_worker.py` | event-driven (folder watch) | When a new file lands in `Excluded/IMPORTANT DOCS/`, extract text → write to `.cache/extracted/` |
| Freshness sweep | `excluded_daemon/jobs/freshness.py` | every ~3600s (1 hr) | Scan extraction manifest mtimes vs source file mtimes; flag stale extractions |
| KG NER | `excluded_daemon/kg/build.py` | manual + nightly | Extract entities/mentions/relations into `.cache/excluded_kg.db` |

**End-to-end staging:**
1. File appears in `Excluded/IMPORTANT DOCS/`: ~immediate detection (folder watch)
2. Extraction to `.cache/extracted/`: seconds to minutes (depending on PDF size + OCR need)
3. FTS5 index update: requires `python tools/excluded_fts_build.py` re-run (NOT automatic)
4. ChromaDB vector index update: requires `python tools/rag_build.py` re-run (NOT automatic)
5. KG entities update: requires `python tools/excluded_daemon/kg/build.py` (NOT automatic)

**Gap:** steps 3-5 are manual. A new file is extracted automatically but not searchable until indices rebuild. **Searchable latency = next manual rebuild.**

### Path B — manual ingest

User runs `python tools/bulk_extract.py <dir>` then `excluded_fts_build.py` + `rag_build.py` + KG build. Same eventual-consistency model; user controls the cadence.

### Operational implications for measurement

- A measurement run that depends on freshly-ingested content must rebuild the indices first. If `excluded_fts_build.py` hasn't been re-run since a new file landed, that file is not in the FTS index and will not appear in any retrieval until rebuilt.
- For acquihire-grade measurement runs, the safe practice is: rebuild all three indices the day before any benchmark run, snapshot timestamps in the run report.

### Future improvement (documented, not built)

Auto-rebuild of FTS5 + Chroma + KG on a 24-hr cron via Windows Task Scheduler. Per `no-recurring-cron.md` rule: NOT via `CronCreate`.

---

## Diarization metadata — explicit gap

**Question the checklist asks:** "Audio is transcribed but is speaker-diarization information preserved in a searchable form?"

**Audit answer:** **No.** Whisper-large-v3 transcripts are stored as plain text without speaker labels. There is no `speaker_id` column in the FTS index, no diarization JSON sidecar, no per-segment speaker attribution.

**What this means in practice:**
- A query like "what did Adam say about X?" cannot retrieve only Adam's spoken segments — it retrieves any transcript chunk where "Adam" and "X" are nearby.
- For evidentiary use the operator must listen to the audio to confirm which speaker said the cited text.

**Why this gap exists:**
- Whisper-large-v3 alone does not produce diarization. Adding it requires pyannote-audio (LGPL, separate model + pipeline) or a hosted diarization API.
- For the current corpus (45 audio files, mostly recordings the operator made themselves), the operator already knows the speakers.

**Cost to close (documented, not built):**
- Add pyannote-audio to the Whisper pipeline: ~1-2 day build + GPU model download.
- Re-transcribe all 45 audio with diarization: ~2-3 hr GPU time.
- Add `speaker_id` column to FTS5 chunks + per-segment metadata: ~3-4 hr.
- Rerun all retrieval benchmarks: ~$15.

**Decision:** documented gap, not in critical path for acquihire diligence. Will be closed if/when the corpus grows past the operator's personal-knowledge scale.

---

## Re-ingest mechanism if a model is upgraded

**Question the checklist asks:** "If Whisper or the embedding model is upgraded, how do existing transcripts/embeddings get refreshed?"

**Audit answer:** **Re-ingest is fully manual. No automated migration exists.**

What the operator does today:
1. Identify the affected modality (audio = Whisper; vector index = nomic-embed-text; OCR = Tesseract or pdf_lib).
2. Delete or rename the affected cache subdirectory under `.cache/extracted/` or `.cache/rag/`.
3. Re-run the appropriate build script (`excluded_fts_build.py`, `rag_build.py`, audio transcribe pipeline).
4. Manually verify a sample of refreshed artifacts before the new index is treated as canonical.

**Versioning:** there is **no model-version field in the cache file format.** Cache filenames don't encode the model that produced them; the operator must remember (or check git history) what was active when a given cache was built.

**Operational implication:** if Whisper-large-v3 is replaced by Whisper-v4 mid-corpus, the operator cannot tell from the cache alone which transcripts came from which model unless they re-run from scratch.

**Future improvement (documented, not built):** add a `provenance.json` sidecar per cached artifact recording {model_id, model_version, build_timestamp, source_file_mtime}. Buildable in ~3-4 hr; not blocking for current corpus scale.

---

## Derived-artifact versioning with source models

**Question the checklist asks:** "Are transcripts, OCR text, and embeddings versioned with the source models that produced them?"

**Audit answer:** **No, see the previous section.** This is the same gap.

**Current state:** every derived artifact (transcript, extracted text, vector embedding) is stored without a model-version tag. The operator can find the model in use at the time only by checking git history of the build script that produced the artifact.

**Mitigation today:** the operator runs all builds on the same machine with one active model per modality at a time. If a model is upgraded, the convention is to re-run the affected build from scratch and discard the old cache.

**Future improvement:** see Re-Ingest section above. One `provenance.json` sidecar covers both gaps.

---

## Summary of staging / re-ingest / versioning posture

| Concern | Status | Why this is OK for current scope |
|---|---|---|
| Staging period | Eventually-consistent, manual rebuild | Single operator manages cadence; new files don't appear until rebuild, no false-stale claim risk |
| Diarization | Not preserved | Operator knows speakers in the 45-file audio corpus |
| Re-ingest on model upgrade | Fully manual, no migration tool | One operator, one model per modality at a time, full re-run when models change |
| Derived-artifact versioning | No version tag in cache | Same — git history of build scripts is the de-facto version log |

These are documented gaps, not bugs. They become real engineering work if/when the corpus scales to multi-operator or hosted deployment (see `docs/DEPLOYMENT_MODEL.md`).

# Handoff — Session 258: Excluded/ Knowledge Base Stack

**Generated**: 2026-04-12 23:15
**Branch**: master
**Last commit**: f179eadec9 handoffs(index): append ai-audit-and-handoff-infra row
**Uncommitted**: 29 new files + 8 modified (all Excluded/ tooling — no CalmCore code touched)
**Session duration**: ~6 hours
**Retrieval baseline**: 64% hybrid on 50-query probe (nomic-embed-text, 15,680 ChromaDB + 19,699 FTS5 chunks)

---

## What This Session Built

A complete document intelligence stack for `C:\Users\atayl\Desktop\Excluded\` — the legal case, career, finance, and brand corpus that dictates Adam's life right now. Six-layer architecture: source files → extraction/OCR/transcription → FTS5 + ChromaDB indexes → hybrid retrieval → agent swarm → cited answers.

**Key artifacts**: 7 `/ex-*` slash commands (unified under `/ex`), daemon scaffold, hybrid search with RRF, 50-query quality probe, semantic chunker, persons roster + NER seeder, email thread viewer, corpus lint, security v2 filter, architecture docs, UKB research reports.

**Key metrics**: 64% hybrid retrieval baseline, 96.4% RAG anchor-grep verification, 0 missing extractions (was 1,302), 0 credentials in indexes (3 purged + security filter hardened).
## 13 Open Items — Detailed

### Item 1: Run `persons_ner_seed.py` (~50 min Ollama)
**What**: `python tools/persons_ner_seed.py --min-mentions 2` scans all 2,275 extracted texts via Ollama qwen3.5:27b NER, produces candidate person roster at `.cache/persons/persons_candidates.json`.
**Why**: Current 25-person `persons.json` was hand-curated. NER auto-populates 200+ candidates; user promotes real ones.
**Blocked by**: Nothing. Needs Ollama idle (not embedding).
**Run**: `cd C:\Users\atayl\VoxCore && python tools/persons_ner_seed.py --min-mentions 2`
**Output**: `.cache/persons/persons_candidates.json` — review, promote good entries into `.cache/persons/persons.json`.

### Item 2: Run `excluded_tiers_build.py` (~30-60 min Ollama)
**What**: Generates Tier 2 (one-line micro-digest per document, max 120 chars) and Tier 3 (per-folder paragraph summary) via Ollama.
**Why**: Powers `/ex sme` session-start priming. Currently `/ex sme` reads raw files; tiers give compressed navigable context.
**Blocked by**: Nothing. Same Ollama dependency as #1.
**Run**: `python tools/excluded_tiers_build.py --tier 2` then `--tier 3`
**Output**: `.cache/tiers/tier2_excluded.md` + `tier3_excluded.md` + `tier_meta.json`

### Item 3: Reranker implementation (2h)
**What**: After hybrid retrieval returns 50 candidates, a cross-encoder re-scores each `(query, chunk)` pair to promote relevant results into top-K. Biggest lever for retrieval quality.
**Why**: Quality probe shows 64% hybrid. Many failures have the right doc in top-50 but ranked below the cutoff. Reranker pushes it up.
**Options**: (a) `sentence-transformers` BGE-reranker (Python, offline), (b) Ollama `local_classify` with a relevance prompt (slower, simpler), (c) Qwen-based rerank via `/api/generate`.
**Where**: Add to `tools/excluded_hybrid_search.py` as an optional `--rerank` flag. Update `quality_probe.py` to test with/without.
**Measure**: Re-run `python tools/quality_probe.py --engine hybrid` before and after.

### Item 4: Query expansion (1h)
**What**: Before FTS5 search, expand abbreviations and document-type terms. "DD214" → "DD Form 214 Certificate of Release". "ET" → "Expedited Transfer". "NARSUM" → "Narrative Summary".
**Why**: FTS5 implicit-AND fails when the document uses the full form but the query uses the abbreviation. Expansion bridges the gap.
**Where**: Add an expansion dict to `tools/excluded_hybrid_search.py` `_prep_fts_query()`. Small, testable.
**Measure**: Same probe before/after.

### Item 5: sentence-transformers for Snowflake embeddings (1h setup + 2 min rebuild)
**What**: Bypass Ollama (which can't batch snowflake/bge-large — returns 400 on batch>1) and use `sentence-transformers` directly for GPU-batched embedding. `pip install sentence-transformers`, update `rag_build.py` to call `SentenceTransformer.encode()` when `EMBED_BACKEND=st` env var set.
**Why**: Snowflake-arctic-embed-l beats nomic on MTEB retrieval benchmarks. Ollama limitation (no batch support for non-nomic models) made this seem infeasible. sentence-transformers bypasses the limitation entirely.
**Blocked by**: `pip install sentence-transformers` (~500 MB with PyTorch). May conflict with existing torch install.
**Measure**: Rebuild ChromaDB with Snowflake, re-run probe, compare to nomic 64% baseline.

### Item 6: Audio transcription (38 remaining files) — IN PROGRESS (OTHER TAB)
**What**: 45 M4A recordings in `Excluded/Recordings/`, 7 already transcribed (session 248 via CPU Whisper). 38 remain.
**Status**: **Tab T-32 is actively implementing WhisperX and working on the audio.** Do NOT start transcription from this tab — it will conflict.
**Action for this tab**: None. T-32 owns audio. Once complete, run `/ex refresh` to pick up new transcripts into FTS5 + ChromaDB.

### Item 7: Remaining _Needs Sorted (4 items)
**What's left**: `_Archive/` subfolder only. All real files were moved this session. The `_Archive/` inside `_Needs Sorted/` contains items from prior sorts.
**Action**: `rm -rf "C:/Users/atayl/Desktop/Excluded/_Needs Sorted/_Archive"` if empty, or check contents first.
**Status**: Low priority. _Needs Sorted is functionally clean.

### Item 8: LoreWalkerTDB decision (1.2 GB)
**What**: SQL dumps at `Excluded/LoreWalkerTDB/` (README.txt, hotfixes.sql, world.sql). CalmCore already has newer TDB at `CalmCore/sql/base/TDB_full_*.sql` (Feb 2026).
**Options**: (a) Move to `CalmCore/sql/base/LoreWalkerTDB_OLD/` for reference. (b) Delete (CalmCore has newer). (c) Leave (already in SKIP_FOLDERS, costs only 1.2 GB disk).
**Risk**: Zero — it's excluded from all indexing via `config.SKIP_FOLDERS`.
**Recommendation**: Option (c) until you need the disk space.

### Item 9: takeout-20260411 extraction (135 MB)
**What**: Google Takeout at `Excluded/takeout-20260411T200559Z-3-001/Takeout/Mail/` — likely a Gmail mbox subset.
**Action**: Check if it duplicates the main `mbox/` exports. If new content, run `python tools/mbox/index.py` on it. If duplicate, move to `_Archive/`.
**Run**: `ls "C:/Users/atayl/Desktop/Excluded/takeout-20260411T200559Z-3-001/Takeout/"` to inspect structure first.

### Item 10: Tray UI for daemon (3h)
**What**: pystray desktop tray icon for ExcludedDaemon — status colors, right-click menu (Status/Lint/Refresh/Pause/Exit), Desktop shortcut.
**Why**: Current daemon is CLI-only (`python -m tools.excluded_daemon`). Tray would 10x actual usage.
**Blocked by**: Daemon Phase B stability proven (smoke-tested once, not stress-tested).
**Spec**: Full spec at `UNIFIED_KNOWLEDGE_BASE/04_Architecture/ExcludedDaemon_Agentic_RAG_Spec.md` § "Shortcut Launcher Pattern".

### Item 11: ChromaDB remaining failures (64 chunks)
**What**: `rag_build.py` added pre-truncation at 7000 chars, dropping failures from 256 → 64. Remaining 64 are likely chunks that fail even after truncation (encoding issues, empty after truncation, or Ollama timeout).
**Action**: Run `python tools/rag_build.py --stats` to identify failing chunks by doc_type/path. Fix or accept the ~0.4% loss.

### Item 12: Memory citation audit (379 breaks from lint)
**What**: `excluded_lint.py` flagged 379 broken citations in memory files — paths like `case-status.md:42` that don't resolve to files in Excluded/.
**Why most are false positives**: The citation regex matches memory-internal cross-references (e.g. `memory/case-status.md` cited in `memory/MEMORY.md`) as well as actual Excluded/ paths. The regex doesn't distinguish.
**Fix**: Refine `_check_citation_breaks()` in `excluded_lint.py` to skip paths that start with `memory/` or `~/.claude/` (internal references, not Excluded/ citations).
**Effort**: 30 min.

### Item 13: Deferred items from `deferred_items.md`
**What**: Document graph (adjacency table), ingest_config.yaml, DMAIC mapping for filing-prep, Conway daemon escalation, auto-populated memory edits, retrieval A/B framework.
**Where**: Full list at `AI_Studio/Reports/deferred_items.md`.
**Priority**: All are post-retrieval-plateau work. Don't touch until items #3-5 above have been measured.
## Second Tab: Monday HAF Call Prep (`/ex sme case`)

**Open a new Claude Code tab in VoxCore and paste this:**

```
/ex sme case
```

This primes Claude as an SME on the legal case lane. After it loads, use these follow-up commands:

### Call prep workflow

1. **After `/ex sme case` completes**, read the call brief:
```
Read C:\Users\atayl\Desktop\Excluded\IMPORTANT DOCS\Monday_HAF_Call_13Apr2026\00_CALL_BRIEF.md
```

2. **Check if anything changed since the brief was written (Apr 11)**:
```
/ex search "Amy Little April 2026"
```

3. **Review the post-call checklist so you know what to capture DURING the call**:
```
Read C:\Users\atayl\Desktop\Excluded\IMPORTANT DOCS\Monday_HAF_Call_13Apr2026\07_POST_CALL_CHECKLIST.md
```

4. **Verify the DCSA SIR deadline status (due ~Apr 15, 2 days after call)**:
```
/ex ask "What is the current status of the DCSA SIR response package and is it submitted?"
```

5. **Check Constance Williams response status (ball in your court 19 days)**:
```
/ex search "Constance Williams privacy release"
/ex thread --subject "HAF-250411"
```

6. **Generate a one-pager for Amy Little if needed**:
```
/one-pager "Amy Little"
```

### Key documents to have open during the call

| Document | Purpose |
|----------|---------|
| `Monday_HAF_Call_13Apr2026/00_CALL_BRIEF.md` | Quick reference — who, when, platform |
| `Monday_HAF_Call_13Apr2026/02_TALKING_POINTS.md` | 9 topics with legal authority citations |
| `Monday_HAF_Call_13Apr2026/01_CONTACTS_AND_REFERENCES.md` | Names, numbers, case IDs |
| `Monday_HAF_Call_13Apr2026/06_RECORDS_TO_REQUEST.md` | Checklist of what to ask for |
| `Monday_HAF_Call_13Apr2026/11_CLINICAL_SUMMARY_FOR_TOLIN.md` | 66-session MH synthesis if clinical questions arise |
| `Monday_HAF_Call_13Apr2026/09_EVIDENCE_GAP_MATRIX_CHATGPT.md` | What's proven vs what needs softening |

### The single most important ask for Monday

From ChatGPT strategic input (08_CHATGPT_STRATEGIC_INPUT.md):

> **"Can your office help identify, in writing, whether the case is open or closed, whether DD Form 2701 was ever issued, who my current victim-notification point of contact is, and what the path is for VLC and SARC continuity?"**

This one answer unlocks all downstream issues. It works whether the case is active or closed.

### After the call

Run this in the same tab:
```
/ex absorb "C:\Users\atayl\Desktop\Excluded\IMPORTANT DOCS\Case_Reference\04_LEGAL_CORRESPONDENCE\HAF_Call_Notes_13Apr2026.md"
```
(After you write up your notes from the call.)

Then:
```
/draft-email "Amy Little thank-you recap"
/draft-email "Constance Williams follow-up with HAF update"
```

### Light findings from SME sweep (this session)

1. **Ko's VLC termination memo signature fields are blank** in the PDF extraction — may be unsigned copy. Verify you have the signed version.
2. **`AFPC_refuses_ET_screenshot.png` is a ChatGPT conversation**, not AFPC evidence. Already flagged in talking points. Do NOT present as AFPC communication.
3. **`Jackie_text_McMaster_ET_obstruction.png` OCR only captured Jackie's reply**, not Adam's outgoing text. The obstruction claim may be truncated by screenshot framing.
4. **PEBLO day count: 93 days in call brief (Apr 13) vs 88 days in MASTER_05 (Apr 8)**. Both correct for their dates. Use 93 on the call.
## Key Files Created This Session

### Commands (`.claude/commands/`)
| File | Purpose |
|------|---------|
| `ex.md` | Unified `/ex <action>` router |
| `ex-status.md` | Corpus health dashboard |
| `ex-absorb.md` | One-shot ingestion |
| `ex-ask.md` | 4-agent swarm with named patterns |
| `ex-posture.md` | Morning urgency brief |
| `ex-refresh.md` | Incremental maintenance |
| `ex-sme.md` | SME priming |

### Rules (`.claude/rules/`)
| File | Purpose |
|------|---------|
| `excluded-corpus.md` | 5-rule constitution for the legal corpus |

### Tools (`tools/`)
| File | Purpose |
|------|---------|
| `semantic_chunk.py` | Header-aware .md chunker |
| `excluded_hybrid_search.py` | RRF fusion of FTS5 + ChromaDB |
| `excluded_fts_build.py` | FTS5 trigram index builder |
| `excluded_tiers_build.py` | Tier 2/3 digest pyramid via Ollama |
| `excluded_lint.py` | 6-check corpus integrity audit |
| `excluded_session_log.py` | Episodic session log (md + jsonl) |
| `quality_probe.py` | 50-query retrieval scoreboard |
| `retrieval_test_suite.jsonl` | The 50 anchor queries |
| `persons_resolve.py` | Entity resolver with alias expansion |
| `persons_ner_seed.py` | NER auto-population of persons roster |
| `mbox_thread.py` | Email reply-chain viewer |

### Daemon (`tools/excluded_daemon/`)
| File | Purpose |
|------|---------|
| `config.py` | Paths, routing, security, HIGH_PRIORITY_FOLDERS |
| `router.py` | Two-stage security + extension routing + READ-ONLY guard |
| `watcher.py` | watchdog + debounce + dirty flag |
| `daemon.py` | asyncio main loop + worker dispatch |
| `workers/extract_worker.py` | Wraps extract_cache.py |
| `workers/ocr_worker.py` | Wraps ocr_images.py |
| `workers/index_worker.py` | FTS5 rebuild + priority-folder notifications |
| `jobs/freshness.py` | Hourly staleness sweep |
| `jobs/verify_rag.py` | Nightly anchor-grep RAG verification |

### Architecture docs (`UNIFIED_KNOWLEDGE_BASE/04_Architecture/`)
| File | Purpose |
|------|---------|
| `Excluded_Knowledge_Base_Architecture.md` | Complete as-built reference |
| `ExcludedDaemon_Agentic_RAG_Spec.md` | Daemon design (Phases A-G) |

### Reports (`AI_Studio/Reports/`)
| File | Purpose |
|------|---------|
| `ukb_pass2_frameworks.md` | 16 patterns from 8 UKB Playbook files |
| `ukb_pass2_vocabulary.md` | 30+ terms from 7 UKB Vocabulary files |
| `excluded_phase_ab_complete.md` | Phase A+B shipping report |
| `deferred_items.md` | What was knowingly not built + rationale |
| `sme_monday_haf_call_13apr2026/README.md` | HAF call SME sweep notes |
| `scheduled/quality_probe_*.md` | Retrieval scoreboard runs |
| `scheduled/excluded_lint_*.json` | Corpus integrity reports |
| `scheduled/freshness_*.md` | Staleness sweep |
| `scheduled/rag_verify_*.md` | RAG anchor verification (96.4%) |

### Caches
| Path | What |
|------|------|
| `.cache/excluded_fts.db` | 19,699 chunks, 165 MB, FTS5 trigram |
| `.cache/rag/chroma/` | 15,680 chunks, ChromaDB nomic-embed-text |
| `.cache/extracted/` | 3 clean buckets (IMPORTANT_DOCS + Monday_HAF + _Needs_Sorted + For_TAP + memory) |
| `.cache/ocr/` | 5 buckets |
| `.cache/persons/persons.json` | 25 hand-curated entities |
| `.cache/excluded_daemon/` | PID file, queue, state |

## Don't Touch (Other Tab Owns)
- CalmCore source code (`C:\Users\atayl\CalmCore\src\`)
- CalmCore `.cache/codebase.db`
- `Case_Reference/` contents (READ-ONLY policy — see `excluded-corpus.md` Rule 1)
- **Audio transcription / WhisperX** — Tab T-32 owns `Excluded/Recordings/`, `tools/audio_transcribe*.py`, and any Whisper/WhisperX venv setup. Do not run transcription or modify audio tooling from other tabs.

## Warnings
- **29 untracked + 8 modified files not committed.** User should `/wrap-up` when ready to persist.
- **MCP servers disconnected mid-session** (docs-rag, arcanum, etc.). They reconnect on next session start. Commands that reference MCP tools will work once reconnected.
- **ChromaDB has 64 Ollama-failed chunks** (~0.4% loss). Not blocking but worth investigating.
- **Ollama can't batch embed snowflake/bge-large models** — only nomic-embed-text supports batch. To test other models, install `sentence-transformers` for direct GPU embedding.

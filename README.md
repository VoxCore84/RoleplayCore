# VoxCore

**Local-only retrieval, citation-precision, and synthesis software for high-stakes evidence work.**

VoxCore is single-machine software that ingests heterogeneous evidence (email archives, PDFs, audio, scanned images, office docs), indexes it across keyword + vector + knowledge-graph channels, and answers questions with verbatim-quoted citations that are deterministically verifiable against the source. It was built solo on personally-owned hardware to address the working set of one operator's privileged legal case; the architecture is general.

The differentiated capability is **forensically-defensible citation**: every quote in an answer is paired with its source path, and a substring verifier confirms the quote exists verbatim in that source. Quotes the model invents are deterministically flagged FABRICATED at scoring time AND prevented from shipping by a verify-retry loop. The pipeline also runs an in-pipeline CONTRADICTS Auditor (Sonnet 4.6) that holds answers when the model's quote opposes its own claim. As of 2026-05-02 the system delivers an answer with 16.7% hallucination on shipped (n=35 held-out, v4 with auditor) OR refuses to deliver and flags for human review — 80% delivery rate, 0 silent CONTRADICTS, 0 fabricated quotes shipped.

## What this is

A single-machine appliance with three layers stacked on top of each other:

- **Ingest.** `tools/extract_cache.py`, `tools/bulk_extract.py`, `tools/excluded_daemon/` watch a folder tree, extract text from PDFs / DOCX / EML / MSG / images / audio (Whisper-large-v3) / mbox archives, run a governance gate (PII + classification-marker + sealing-order detection), and write to a CAS-style cache.
- **Index.** `tools/excluded_fts_build.py` (SQLite FTS5), `tools/rag_build.py` (ChromaDB + nomic-embed-text), and `tools/excluded_daemon/kg/` (knowledge graph, 24K entities / 175K mentions / 743K relations) build three independent retrievers over the cached text. `tools/excluded_hybrid_search.py` fuses them via Reciprocal Rank Fusion with adaptive boosts.
- **Answer.** `.claude/commands/ex-ask.md` is a multi-agent skill that fans out to typed retrieval agents, synthesizes an answer under one-quote-per-claim discipline, and emits citations. `tools/citation_scorer.py` measures hallucination rate by extracting claims, verifying citation paths exist in the corpus, substring-verifying inline quotes, and (optionally) running a Claude-Opus-4.7 LLM-as-judge over each (claim, quote) pair to score span correctness.

The MCP fleet (`.mcp.json` — voxcore-db, voxcore-server, arcanum, docs-rag, local-llm) exposes corpus + database + LLM access to Claude Code over stdio. See `docs/architecture/MCP_TRANSPORT.md`.

## Who this is for

The intended user is the operator who owns the corpus. There is no multi-tenant story, no remote API, no hosted deployment. Production = development = operator's workstation by design — see `docs/DEPLOYMENT_MODEL.md` for the full rationale and the cost of going hosted.

If you are evaluating this for an acquihire or technical diligence: read `docs/architecture/decisions/` (7 ADRs), `docs/COST_AND_LATENCY_BENCHMARKS.md`, and the Desktop verification artifacts (`VoxCore_Verification_Master_Checklist.md`, `VoxCore_Decisions_Log.md`, `VoxCore_Benchmark_Results.md`).

## Measured numbers (current, as of 2026-05-02 evening)

| Metric | Value | Test set | Judge | Evidence |
|---|---|---|---|---|
| Hybrid retrieval pass rate | 92% (46/50) | 50-query suite | n/a (deterministic) | `quality_probe_20260430_191844.json` |
| Citation precision (path-level) | 100% (302/302) | n=30 batch | n/a (deterministic FTS lookup) | `citation_score_n30_20260502.json` |
| **Hallucination rate, v4 shipped-only** | **16.7%** | n=35 held-out (28 shipped, 7 held) | claude-opus-4-7 | `citation_score_holdout_n35_v4_claudejudge_20260502_142347.json` |
| Hallucination rate, v2 all-shipped | 24.7% | n=35 held-out (35 shipped) | claude-opus-4-7 | `citation_score_holdout_n35_v2_claudejudge_20260502_113446.json` |
| **FABRICATED quotes shipped (with verify-retry)** | **0** | n=35 held-out | substring verifier | same |
| **Silent CONTRADICTS shipped (with v4 auditor)** | **0** | n=35 held-out | substring + Sonnet 4.6 auditor | same |
| Coverage (deliverable, v4) | 80% (28/35) | n=35 held-out | auditor 0.70 threshold | same |
| FABRICATED detection rate (catch at scoring) | 100% | n=35 held-out (pre-v2 measurement) | substring verifier | `citation_score_holdout_n35_claudejudge_20260502_074107.json` |
| Multi-hop coverage | 33% (4/12) | n=12 held-out, mixed hop types | n/a | `citation_score_multihop_n12_claudejudge_20260502_140536.json` |
| Multi-hop on-coverage hallucination | 39.6% | same | claude-opus-4-7 | same |
| Audio cross-instance WER | 0.59% | 26 audio files | n/a | `wer_cross-instance_20260502_031916.json` |
| OCR character accuracy (avg CER) | 24.26% | 10 random PDFs | n/a | `ocr_accuracy_20260502_032335.json` |
| **LegalBench overall (PROVEN tier)** | **66.4%** (166/250) | n=50/task, 5 tasks | claude-opus-4-7 (free-text), string-match (binary) | `legalbench_n50_claudejudge_20260502_135847.json` |
| Throughput, PDF (cold-cache) | 12,033 files/hour | 10 random PDFs | n/a | `throughput_pdf_image_20260502_115747.json` |
| Cost per fully-judged query (v4) | ~$0.24 | n=35 (synthesis + auditor + judging) | claude-opus-4-7 | `docs/COST_AND_LATENCY_BENCHMARKS.md` |
| Latency, synthesis only (v4) | p50=6.1s, p95=12.3s | n=35 sequential | n/a | same |

**Methodology discipline (encoded in `~/.claude/projects/C--Users-atayl-VoxCore/memory/feedback_calibration_overfit.md`):**
1. Test sets must be held out from pipeline development. A 0% hallucination rate on the calibration batch was 30% on a held-out batch of fresh queries.
2. Every published quality number must specify the judge model. Same answers, Gemma judge → 45.5%; Claude Opus judge → 30.3%.
3. Roadmap predictions calibrated against an inflated baseline are themselves inflated.

## Tech stack

| Component | Choice | ADR |
|---|---|---|
| Orchestration | Triad (Gemini 3.1 Pro Architect → Claude Opus 4.7 Executor → Gemini 3.1 Pro Auditor, fail-closed, 3-retry) | `docs/architecture/decisions/0001-triad-orchestration.md` |
| Tool integration | MCP (Model Context Protocol), stdio transport | `docs/architecture/decisions/0002-mcp-first-protocol.md`, `docs/architecture/MCP_TRANSPORT.md` |
| Local compute | Ollama (gemma4:26b, qwen3.5:27b, nomic-embed-text), Whisper-large-v3 (audio), Tesseract 5.4 (OCR) | `docs/architecture/decisions/0003-local-gpu-offload.md` |
| Governance | Pre-ingest filename gate + post-extraction content scan (PII/credentials/classification markers/sealing orders) | `docs/architecture/decisions/0004-governance-gate.md` |
| Citation precision | Inline-grounded verbatim quotes + substring verifier + LLM-as-judge for span correctness | `docs/architecture/decisions/0005-citation-precision-pipeline.md` |
| PDF extraction | pdfplumber (MIT) + pypdfium2 (Apache 2.0) — chosen over PyMuPDF (AGPL) | `docs/architecture/decisions/0006-pdfplumber-pypdfium2-over-pymupdf.md` |
| Retrieval fusion | Reciprocal Rank Fusion across FTS5 + ChromaDB + KG, k=60, adaptive boosts | `docs/architecture/decisions/0007-hybrid-retrieval-rrf.md` |
| Chunking | Three independent fixed-size chunkers, NOT semantic — for determinism and citation stability | `docs/architecture/CHUNKING_STRATEGY.md` |

## Hardware (the production runtime)

Documented in `docs/ENVIRONMENT.md`. Ryzen 9 9950X3D / RTX 5090 32GB / 128GB DDR5 / NVMe. Windows 11 Pro, Python 3.14.3. All personally-owned. No government-furnished equipment, no .mil network, no employer-paid subscriptions — see `docs/acquihire/03_IP_Chain_of_Title/02_Subscriptions/subscription_summary.md`.

## License

VoxCore-specific code is MIT-equivalent (single author, no employer claims, no government code). The TrinityCore subtree under `src/server/` is GPL-2.0 inherited (legacy WoW-server work that lives in the same repo for historical reasons; not part of the AI/retrieval product). Third-party Python deps were audited 2026-05-02 — all AGPL/GPL dependencies replaced; see `docs/acquihire/03_IP_Chain_of_Title/04_Open_Source_Inventory/license_remediation.md`.

## Diligence-grade documentation map

If you read these in order you'll have the full picture in under an hour:

1. `README.md` (this file) — what it is, who it's for, what's measured
2. `docs/ENVIRONMENT.md` — hardware, OS, Python, GPU, models, databases
3. `docs/DEPLOYMENT_MODEL.md` — explicit local-only decision, cost-of-reversal
4. `docs/architecture/decisions/README.md` — index of 7 ADRs covering the non-obvious choices
5. `docs/architecture/MCP_TRANSPORT.md` — MCP server fleet, transport, statefulness, error handling
6. `docs/architecture/CHUNKING_STRATEGY.md` — three chunkers, why fixed not semantic
7. `docs/COST_AND_LATENCY_BENCHMARKS.md` — measured per-query cost and latency by role
8. `docs/architecture/TRIAD_ENTRY_POINT.md` — orchestrator entry, fail-closed enforcement, model selection
9. Desktop: `Do NOT Delete These/VoxCore_Verification_Summary_3page.md` — diligence-grade 3-page leave-behind (PROVEN-tier numbers + methodology + IP/license posture)
10. Desktop: `Do NOT Delete These/VoxCore_Economic_Impact_Analysis_v3.1.md` — full Economic Impact analysis with measured numbers replacing the v2 PDF
11. Desktop: `VoxCore_Verification_Master_Checklist.md` — 106/171 verified, with evidence per item
12. Desktop: `VoxCore_Benchmark_Results.md` — measured-numbers ledger
13. Desktop: `VoxCore_Decisions_Log.md` — append-only decision audit trail

## Building / running

The retrieval and citation pipeline is pure Python — no compiled component to build. Pinned dependencies live alongside each subproject (`tools/ai_studio/requirements.pinned.txt`, `tools/voxcore-daemon/requirements.pinned.txt`, etc. — there is no top-level `tools/requirements.pinned.txt` because each subproject has its own dependency surface).

```
# Install per-subproject (the subprojects you actually use):
pip install -r tools/ai_studio/requirements.pinned.txt        # for Triad orchestration
pip install -r tools/voxcore-daemon/requirements.pinned.txt   # for the ingest daemon
pip install -r tools/mcp-voxcore-db/requirements.pinned.txt   # for the MCP DB server

# Most retrieval/citation tooling has no separate requirements file — the imports
# resolve from any of the above (anthropic, requests, sqlite3 stdlib, etc.).

# MySQL is required for the legacy server subtree but not for the AI/retrieval product.
# For retrieval-only use, the SQLite + ChromaDB indices in .cache/ are self-contained.

# Build the FTS index (one-shot, ~30 min for 24K-doc corpus)
python tools/excluded_fts_build.py

# Build the vector index (one-shot, ~2 hr for 24K-doc corpus)
python tools/rag_build.py

# Build the KG (one-shot, ~6 hr for 24K-doc corpus — runs locally via Ollama)
python tools/excluded_daemon/kg/build.py
```

Day-to-day usage is via Claude Code with the `.claude/commands/ex-ask.md` skill. The MCP fleet (`.mcp.json`) loads automatically.

## Status

- **v4 shipped-only hallucination rate: 16.7%** (28 of 35 held-out queries delivered; 7 held with `[AUDITOR_FAILED]` for human review).
- 0 silent CONTRADICTS, 0 fabricated quotes shipped, 100% fabrication detection rate.
- LegalBench n=50 + Claude judge: 66.4% overall (PROVEN tier, externally publishable).
- Multi-hop coverage 33% on n=12 held-out (current bottleneck — the next major engineering target via per-claim re-retrieval).
- Documented path to 8-12% held-out shipped hallucination via two queued Tier 2 fixes (per-claim re-retrieval; CONTRADICTS Auditor full implementation per spec).
- The Tier 3 fine-tuned reranker for sub-2% is months out and requires a labeled training corpus.
- Acquihire diligence: 106/171 master-checklist items verified with evidence (62%); 17 of the remainder are Adam's strategic / ethics / financial decisions (`VoxCore_Open_Questions.md`).

## Credits

- [TrinityCore](https://github.com/TrinityCore/TrinityCore) — legacy WoW-server subtree under `src/server/` (separate from the AI/retrieval product)
- [Anthropic](https://www.anthropic.com) — Claude API used as Triad Executor and citation judge
- [Google](https://ai.google.dev) — Gemini 3.1 Pro used as Triad Architect and Auditor
- [Ollama](https://ollama.com) — local model runtime for embeddings, NER, and free-tier LLM-as-judge

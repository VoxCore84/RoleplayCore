# VoxCore — Verification Summary

**One-page-equivalent leave-behind for acquirer technical review.** Three pages of measured numbers + methodology, designed to read in 5 minutes and decide "yes, schedule the technical diligence call."

**Author:** Adam Taylor (operator). **Date:** 2026-05-02. **Confidence tiers** per `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`.

---

## What VoxCore is

A single-machine retrieval and citation appliance for high-stakes evidence work. Built solo on personally-owned hardware, on personal time, with personally-paid subscriptions, on a personal corpus (no DoD or government data, no GFE, no .mil network — `docs/ENVIRONMENT.md` and `docs/acquihire/03_IP_Chain_of_Title/02_Subscriptions/subscription_summary.md`).

**Differentiated capability vs. published vertical-legal-AI vendors:**
1. Every cited quote is **forensically verifiable** — substring-matched against the source file at scoring time, **100% catch rate on fabrication**.
2. The system either delivers an answer or **refuses to deliver and flags for human review** — it does not silently ship contradictions or fabricated quotes.
3. Every published quality number specifies (a) the test set, (b) the judge model, (c) the confidence tier — no inferred numbers in external materials.

No published vendor offers all three today.

---

## Page 1 — The headline numbers (PROVEN tier unless noted)

### Citation pipeline (held-out n=35, Claude Opus 4.7 judge, v4 with CONTRADICTS Auditor)

| Metric | Value | Confidence |
|---|---|---|
| **Hallucination rate, on shipped answers** | **16.7%** | WELL-SUPPORTED |
| **FABRICATED quotes shipped** | **0** | PROVEN (deterministic substring verifier) |
| **Silent CONTRADICTS shipped** | **0** | WELL-SUPPORTED (auditor + 0.70 confidence threshold) |
| **Coverage (deliverable)** | **80%** (28 of 35; 7 held for human review) | WELL-SUPPORTED |
| Citation precision (path-level) | 100% (302/302 cited paths resolve in corpus) | PROVEN |
| Span correctness (claim-vs-quote, on shipped) | 0.7992 | WELL-SUPPORTED |
| FABRICATED detection rate (catch at scoring) | 100% (24/24 in pre-v2 test; 0/0 in v4-shipped) | PROVEN |

### Retrieval (50-query hand-curated suite)

| Metric | Value |
|---|---|
| Hybrid retrieval pass rate (FTS5 + ChromaDB + KG, RRF k=60) | **92%** (46/50) |
| FTS5 alone | 78% (39/50) |
| Vector alone | 44% (22/50) |

### LegalBench (n=50/task, Claude Opus 4.7 judge, 5 tasks)

| Task | Score | Type |
|---|---|---|
| contract_qa | 90% | binary |
| diversity_1 | 94% | binary |
| hearsay | 52% | binary |
| rule_qa | 94% | free-text (Claude judge) |
| citation_prediction_classification | 2% | free-text |
| **Overall** | **66.4%** (166/250) | mixed — squarely in published-frontier range for similar test-takers |

### Audio + OCR + Throughput (deterministic, no judge)

| Metric | Value |
|---|---|
| Whisper-large-v3 cross-instance WER | 0.59% (n=26 audio files) |
| Whisper-large-v3 cross-instance CER | 0.40% |
| OCR character accuracy on prose | 0–5% CER |
| OCR character accuracy on layout-heavy forms | 47–73% CER |
| Cold-cache PDF extraction throughput | 12,033 files/hour (the bottleneck modality) |
| Cold-cache email extraction throughput | 1,293,103 files/hour |

### Cost economics (claude-opus-4-7 throughout)

| Item | Cost |
|---|---|
| Per-query synthesis (v4 with auditor) | **$0.087** |
| Per fully-judged query (synthesis + auditor + per-claim judging) | **$0.24** |
| Per query at 200/day workload | **~$17/day** synthesis-only |

---

## Page 2 — Methodology (why these numbers can be trusted)

### Three rules behind every published number

(Operationalized in `docs/PUBLISHABLE_CLAIM_WORKFLOW.md` and `~/.claude/projects/C--Users-atayl-VoxCore/memory/feedback_calibration_overfit.md`.)

**1. Test sets must be HELD OUT from pipeline development.** On 2026-05-02 the same pipeline scored 0.0% hallucination on its 15-query calibration batch and 30.0% on a 35-query held-out batch. Calibration numbers are overfit and not citable externally; only held-out numbers appear in this document.

**2. Every published number specifies the judge.** The same 15 answers scored 45.5% hallucination (Gemma 4 26B judge) vs. 30.3% (Claude Opus 4.7 judge) — a 15pp swing from judge calibration alone. This document uniformly uses Claude Opus 4.7 for free-text judging; substring verification is deterministic and judge-independent.

**3. Predictions reference measured baselines, not inferred ones.** The original published "<2% hallucination" claim was inferred from comparable system performance, never measured. Held-out measurement (16.7% on shipped) is materially worse than the inferred number — and that gap would have surfaced in the first 5 minutes of technical diligence. **The inferred claim is formally WITHDRAWN; the measured number replaces it in all external materials.**

### What was inferred → what is now measured

| Prior claim (INFERRED) | Status | Replacement (MEASURED) |
|---|---|---|
| 96% citation precision | WITHDRAWN as single number | Path 100% PROVEN; span 0.799 WELL-SUPPORTED |
| <2% hallucination | WITHDRAWN | 16.7% on shipped, WELL-SUPPORTED (n=35 held-out) |
| 82% multi-hop accuracy | WITHDRAWN | Coverage 33%, on-coverage hallucination 39.6%, effective ~20%, PARTIALLY-SUPPORTED (n=12 held-out) |
| LegalBench ~78% | Replaced | 66.4% PROVEN (n=50, Claude Opus 4.7 judge) |
| 85-95% time reduction | NOT MEASURED | Requires design-partner pilot; not citable yet |

### Architecture audit trail (7 ADRs)

`docs/architecture/decisions/0001-triad-orchestration.md` through `0007-hybrid-retrieval-rrf.md`. Each follows Context / Decision / Alternatives / Consequences format. Topics: Triad orchestration, MCP-first protocol, local-GPU offload, governance gate, citation precision pipeline, pdfplumber+pypdfium2 over PyMuPDF (license remediation), hybrid retrieval RRF.

### Fail-closed safety pattern (the differentiated diligence story)

The pipeline runs synthesizer → FABRICATED substring verifier (with retry loop) → CONTRADICTS Auditor (Sonnet 4.6, 0.70 confidence threshold). On any unresolved hard-fail at any stage, the answer is held with `[AUDITOR_FAILED]` rather than delivered. **No silent failure modes.** This is the legal-evidence-grade difference from the consumer-RAG pattern that just answers and hopes.

---

## Page 3 — IP, license, deployment posture; the roadmap

### IP and chain of title

| Item | Status |
|---|---|
| Single-author code (no employer claims) | Verified — git history shows VoxCore (Adam) is sole VoxCore-specific committer |
| GFE / .mil network use | None — `docs/ENVIRONMENT.md` documents personally-owned hardware + home network |
| Subscriptions (Claude Max, ChatGPT Pro, Google AI Ultra, Anthropic API, OpenAI API, GCP, SuperGrok, Oracle Free, AWS) | All personally-paid, attestation in `docs/acquihire/03_IP_Chain_of_Title/02_Subscriptions/subscription_summary.md` |
| Corpus | Operator's own legal/financial/personal documents — NO DoD or government data |
| Secrets in git history (since 2026-02-22) | 0 findings across 31,257 unique blobs scanned (`tools/secrets_scan.py`) |

### License posture (Cat 9 of verification checklist — DONE)

All AGPL/GPL dependencies replaced or carved out:

| Dep | License | Status |
|---|---|---|
| PyMuPDF (AGPL) | replaced by pdfplumber (MIT) + pypdfium2 (Apache 2.0) via `tools/pdf_lib.py` shim |
| extract-msg (GPL) | replaced by `tools/msg_extract.py` (olefile / BSD-3) |
| mysql-connector-python (GPL) | removed (PyMySQL/MIT was the actual driver) |
| pcodedmp (GPL) | removed (transitive of oletools, not used by VoxCore) |
| pillow_heif | info correction — current upstream is BSD-3, not GPL |
| pyinstaller | GPL with explicit PyInstaller exception allowing commercial bundled binary distribution; used only by separate TongueAndQuill project |

### Deployment posture (explicit decision)

**Local-only single-machine appliance by design** — `docs/DEPLOYMENT_MODEL.md`. Reasons: (1) corpus is privileged legal evidence; hosting multiplies attack surface and chain-of-custody risk, (2) all compute on-machine (Ollama, Whisper, Tesseract, SQLite, ChromaDB), (3) single intended user. Going hosted is reversible but sized at 4-6 weeks (tenant isolation, network auth, encryption-at-rest, real CI/CD, monitoring) — documented gap, not a present capability.

### Roadmap (predicted, not measured — will re-measure after each ship)

| Step | Target failure mode | Effort | Predicted shipped hallucination |
|---|---|---|---|
| ✓ DONE — v2 verify-retry (2026-05-02 morning) | FABRICATED 24 → 0 | shipped | 30% → 24.7% all-shipped |
| ✓ DONE — v4 CONTRADICTS Auditor MVP (2026-05-02 evening) | Silent CONTRADICTS 14 → 0 | shipped | 24.7% → 16.7% on shipped |
| ⏳ NEXT — v5 rewrite-path FABRICATED retry | FABRICATED on rewrite path 5 → 0 | in progress | 16.7% → ~13-14% |
| ⏳ NEXT — Per-claim re-retrieval (code ready) | IRRELEVANT 46 → ~15 | 1-2 hr | ~13-14% → ~10% |
| Queued — In-pipeline Auditor full per spec | CONTRADICTS edge cases | 3-5 days | ~10% → ~8% |
| Tier 3 — fine-tuned legal reranker | All categories | months — needs labeled training data | 8% → 1-2% |

### How to verify any number in this document

Every number cites a JSON or JSONL evidence file in `AI_Studio/Reports/scheduled/`. The full reading order (1 hour read time):

1. This Verification Summary (3 pages)
2. `Desktop/Do NOT Delete These/VoxCore_Economic_Impact_Analysis_v3.1.md` (12 KB)
3. `docs/architecture/decisions/0005-citation-precision-pipeline.md` (full ADR)
4. `Desktop/VoxCore_Verification_Master_Checklist.md` (106/171 verified items, each with evidence)
5. `Desktop/VoxCore_Decisions_Log.md` (append-only decision audit trail; 36+ entries)
6. `Desktop/VoxCore_Benchmark_Results.md` (measured-numbers ledger)
7. `docs/PUBLISHABLE_CLAIM_WORKFLOW.md` (the methodology gate every number passes)

### What the technical diligence call should focus on

1. **Watch the substring verifier catch a fabricated quote in real time.** Run any `/ex-ask` query that exercises a multi-fact claim; observe the verify-retry loop reject and rewrite the model's first attempt.
2. **Watch the CONTRADICTS Auditor hold an answer.** Run a query whose top-k retrieval contains a contradicting fact; observe the [AUDITOR_FAILED] tag and the per-claim audit log.
3. **Walk through one held-out batch end-to-end.** Pick 5 queries from `citation_holdout_queries_v1.jsonl`, see the per-query meta JSON, the score JSON, the shipped vs held disposition, and the cited file paths.
4. **Audit the methodology workflow.** Run a measurement under the 7-step gate in `PUBLISHABLE_CLAIM_WORKFLOW.md`. Confirm the diligence-grade discipline.

If those four pass, the rest is engineering scope — the architecture and methodology are sound.

---

*This summary is a snapshot as of 2026-05-02 evening. Numbers refresh after every measurement run; the canonical evidence is the JSON in `AI_Studio/Reports/scheduled/` and the master ledger at `Desktop/VoxCore_Benchmark_Results.md`. Reach out for the full diligence package.*

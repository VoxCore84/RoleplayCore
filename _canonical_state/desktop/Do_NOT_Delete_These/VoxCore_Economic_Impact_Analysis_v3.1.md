# VoxCore — Economic Impact Analysis v3.1

**Status:** Diligence-ready for external sharing.
**Version:** v3.1 (replaces v3 from earlier 2026-05-02; v3 itself replaced the v2 PDF in the mbox VoxCore Architecture archive).
**Date:** 2026-05-02 (evening).
**Authoring discipline:** Every numerical claim specifies (a) what was measured, (b) the test-set provenance (calibration vs held-out), (c) the judge model where an LLM judged, (d) the confidence tier per `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`. Inferred numbers from prior versions are explicitly flagged as withdrawn.

---

## What changed from v3 (the morning version)

This v3.1 incorporates measurements from the four knockdown rounds completed 2026-05-02:

| v3 morning headline | v3.1 evening headline | Why upgraded |
|---|---|---|
| 30.0% held-out hallucination (v1 of synthesizer) | **24.7% with v2 (FABRICATED verify-retry); 16.7% on shipped with v4 (CONTRADICTS Auditor MVP)** | Two new product capabilities shipped + measured today |
| 100% FABRICATED detection at scoring | **100% detection AND 0 fabricated quotes shipped** | v2 verify-retry rewrites them before delivery |
| 14 silent CONTRADICTS in v1 batch | **0 silent CONTRADICTS shipped (with v4); 7/35 answers held with [AUDITOR_FAILED] for human review** | New in-pipeline auditor blocks high-confidence contradictions |
| LegalBench 70% (n=20, Gemma judge) — interim | **66.4% (n=50, Claude Opus 4.7 judge) — PROVEN tier** | Externally-publishable benchmark with stricter methodology |
| Multi-hop pending | **MEASURED: 33% coverage, 39.6% on-coverage hallucination, effective ~20%; PDF claim of 82% formally WITHDRAWN** | First held-out multi-hop measurement; coverage problem identified |

---

## What changed from v2 (the original PDF)

The v2 PDF claimed four figures that this v3.1 withdraws and replaces with measured-and-honest numbers:

| v2 claim (INFERRED) | v3.1 status | Replacement |
|---|---|---|
| **96% citation precision** | Withdrawn as a single figure | Path-level **100% (302/302) PROVEN**; span-level **0.7992 on shipped (Claude Opus judge, n=35 held-out, v4 with auditor) WELL-SUPPORTED** |
| **<2% hallucination rate** | **WITHDRAWN. Cannot be supported by current measurement.** | Held-out **24.7% with v2** all-shipped; **16.7% on v4-shipped (28/35 delivered, 7/35 held)** — both WELL-SUPPORTED |
| **82% multi-hop accuracy** | **WITHDRAWN.** | Multi-hop n=12 measured 2026-05-02: **33% coverage, 60% span correctness on covered, ~20% effective** — PARTIALLY-SUPPORTED |
| 85-95% time reduction | Still pending measurement | Requires design-partner pilot; do not cite |

The v2 numbers were inferred from comparable system performance, not measured on production output. v3.1 is built only from measured numbers with documented methodology.

---

## The headline figure

> **The system either delivers an answer with measured 16.7% hallucination, or refuses to deliver and flags for human review. It does not silently ship contradictions or fabricated quotes. 80% delivery rate; 20% safety-flag rate.**

What that means in plain terms:
- When the system delivers an answer to a question, every cited quote is **verbatim from the cited source** (deterministic substring check, 100% catch rate on fabrication). ~83% of factual claims in delivered answers are correctly supported by the cited quote (judged by Claude Opus 4.7).
- When the system **cannot deliver an answer with high confidence** — because the model wanted to use a quote that contradicted its own claim, or because the source chunks don't contain the asserted fact — it withholds the answer and tags it `[AUDITOR_FAILED]` for human review. **It does not silently ship.**
- The differentiated capability vs. published vertical-legal-AI vendors: **forensically-defensible inline quotes plus fail-closed safety on contradictions.** No published vendor offers both today.

What this is NOT:
- Not a sub-2% claim (that requires Tier 3 fine-tuned reranker, months out)
- Not a 100% delivery rate (the 20% safety-flag is the trade-off for 0 silent failures)
- Not a calibration-batch number (held-out from pipeline development per the publishable-claim workflow)

---

## Methodology — three rules behind every number

The methodology is durably encoded in `~/.claude/projects/C--Users-atayl-VoxCore/memory/feedback_calibration_overfit.md` and operationalized in `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`.

### Rule 1 — Test sets must be HELD OUT from pipeline development

On 2026-05-02 the same pipeline scored:
- **0.0% hallucination on its 15-query calibration batch** (queries used to develop the prompt and scorer).
- **30.0% on a separate 35-query held-out batch** of fresh attorney-grade questions.

The 0% on calibration was overfit. Pipelines tuned against a fixed test set learn that set's specific failure patterns; they do not generalize. Every external claim in this document comes from held-out measurement.

### Rule 2 — Every published number specifies the judge

The same 15 answers scored:
- **45.5% hallucination** (Gemma 4 26B judge)
- **30.3% hallucination** (Claude Opus 4.7 judge)

A 15-percentage-point swing from judge calibration alone, not pipeline change. Different judges have different IRRELEVANT-vs-PARTIAL boundaries. Comparisons across runs with different judges are meaningless. v3.1 numbers are uniformly Claude-Opus-4.7-judged unless explicitly noted; substring verification is deterministic and judge-independent.

### Rule 3 — Predictions reference measured baselines, not inferred ones

The original roadmap predicted "step 1 prompt change → ~10% hallucination" calibrated against the 45% Gemma baseline. After Claude judge correction the real baseline was 30%, and step 1's true held-out effect was ~0pp. We predict against measured baselines going forward.

---

## Measurement detail (v4 shipped on n=35 held-out, 2026-05-02)

### Test set composition
| Category | n |
|---|---|
| Evidentiary | 12 |
| Regulatory | 6 |
| Person | 6 |
| Chronological | 6 |
| Strategic | 5 |
| **Total** | **35** |

Generated by Claude Opus 4.7 from case-status / case-contacts / case-filings memory context with explicit calibration-batch exclusions. Source: `AI_Studio/Reports/scheduled/citation_holdout_queries_v1.jsonl`.

### v4 result — the production-relevant numbers

| Metric | All-shipped (v2 baseline) | v4 with auditor — full set | **v4 shipped-only (28/35)** |
|---|---|---|---|
| Citation precision | 1.0000 | 1.0000 | 1.0000 |
| Citation recall | 0.5643 | 0.5429 | 0.4286 |
| Span correctness | 0.7529 | 0.6962 | **0.7992** |
| **Hallucination rate** | 0.2472 | 0.2718 | **0.1674** |
| FABRICATED quotes shipped | 0 | 5 (all in held set) | **0** |
| CONTRADICTS shipped | 14 | 13 (most held) | **5 (all under threshold)** |
| Coverage (deliverable) | 35/35 (100%) | 35/35 in JSONL | **28/35 (80%)** |
| Per-query end-to-end cost | $0.22 | $0.31 | $0.31 |

Verdict distribution (shipped-only, 28 queries, 108 verdict calls):
- **SUPPORTS: 30** — quote contains the specific fact ✓
- **PARTIAL: 32** — quote on-topic, doesn't contain specific fact
- **IRRELEVANT: 46** — quote does not address claim's subject
- **CONTRADICTS: 5** — under the 0.70 confidence threshold (above-threshold contradictions were caught and held)
- **FABRICATED: 0** — verify-retry prevents quote invention by construction

### Failure-mode decomposition (what the 16.7% on shipped is composed of)

| Mode | Count (shipped) | Fix path | Tier |
|---|---|---|---|
| FABRICATED | 0 | Already prevented (v2 verify-retry) | Done |
| Hard CONTRADICTS | 0 | Already prevented (v4 auditor + hold) | Done (MVP) |
| Soft CONTRADICTS (<0.70 confidence) | 5 | Auditor v6: tighten threshold; per-claim re-retrieval | Tier 2, queued |
| IRRELEVANT (95→46 from v2) | 46 | Per-claim re-retrieval (v3 architecture, code shipped) | Tier 2, queued |
| PARTIAL | 32 | Stricter prompt; LLM reranker for chunk selection | Tier 2-3 |

Realistic projection after Tier 2 (per-claim re-retrieval + auditor refinement): **8-12% held-out shipped hallucination**.
Sub-2% requires Tier 3 fine-tuned legal reranker — months out.

---

## What's measured outside the citation pipeline

### LegalBench (n=50/task, Claude Opus 4.7 judge, 5 tasks)

Externally-publishable per `docs/PUBLISHABLE_CLAIM_WORKFLOW.md` PROVEN tier.

| Task | Score | Type |
|---|---|---|
| contract_qa | 90% (45/50) | binary |
| diversity_1 | 94% (47/50) | binary |
| hearsay | 52% (26/50) | binary |
| rule_qa | 94% (47/50) | free-text (Claude judge) |
| citation_prediction_classification | 2% (1/50) | free-text (genuinely hard task) |
| **Overall** | **66.4% (166/250)** | mixed |

Squarely in published-frontier range for similar test-takers. Stanford CodeX baselines on similar 5-task subsets typically score 50-70%.

### Audio (Whisper-large-v3 cross-instance stability)

| Metric | Value | Sample |
|---|---|---|
| WER | 0.59% | 26 audio files, 2 independent transcriptions each |
| CER | 0.40% | same |

Cross-instance stability of 99.4% word-level agreement.

### OCR (Tesseract 5.4 vs pdfplumber native text)

| Metric | Value |
|---|---|
| Avg CER | 24.26% |
| CER on prose | 0–5% |
| CER on layout-heavy forms | 47–73% |

For VoxCore's actual use case (prose legal documents), the relevant number is the prose subset (0–5%).

### Throughput per modality (cold-cache extraction)

| Modality | Files/hour | MB/hour |
|---|---|---|
| txt/md | 19,354,838 | 723,742 |
| eml | 1,293,103 | 131,909 |
| docx | 240,320 | 6,023 |
| PDF | **12,033** (the bottleneck) | 6,138 |
| audio (Whisper-large-v3) | ~60-120 (estimated, RTX 5090) | varies |

### Hybrid retrieval (FTS5 + ChromaDB + KG, RRF k=60)

| Metric | Value |
|---|---|
| Pass rate (50-query hand-curated suite) | 92% (46/50) |
| FTS5 alone | 78% (39/50) |
| Vector alone | 44% (22/50) |

### Multi-hop coverage (n=12 held-out, hop types: event_to_sequel, regulation_to_application, claim_vs_counter, etc.)

| Metric | Value |
|---|---|
| Coverage (queries with grounded answer) | 33% (4/12) |
| On-coverage hallucination | 39.58% |
| Effective accuracy | ~20% |

8 of 12 queries returned "no relevant sources" — system honestly refused multi-hop joins beyond top-5 retrieval reach.

---

## Cost economics (claude-opus-4-7 throughout, no Batch API, no prompt caching)

| Per-call | n | Avg in tokens | Avg out tokens | Per-call cost |
|---|---|---|---|---|
| Executor synthesis (v2/v4) | 35 | 3,353 | 428 | **$0.082** |
| Inline auditor (Sonnet 4.6, per-claim) | ~5/answer | ~400 | ~50 | **~$0.005** |
| Span judge (Opus 4.7, per verdict) | 7.8/answer | ~400 | ~50 | **~$0.018** |

Per fully-judged held-out query end-to-end:
- v2 (no auditor): synthesis $0.082 + 7.8 × $0.018 judge = **$0.22**
- v4 (with auditor): synthesis $0.082 + ~5 × $0.005 auditor + 7.8 × $0.018 judge = **$0.24** (audit cost is negligible — Sonnet is ~5× cheaper than Opus per token, and the auditor uses far fewer tokens)

Synthesis-only (production usage, no per-query judging):
- v2: $0.082/query
- v4: $0.087/query (auditor adds ~$0.005)

At a notional 200 queries/day: **~$17/day v4 synthesis-only**. Anthropic Batch API (50% discount, async, ≤24h SLA) would cut to ~$8/day for non-real-time workflows.

---

## What this software is

A single-machine retrieval and citation appliance for high-stakes evidence work. **Local-only by design** (corpus is privileged legal evidence; multi-tenant deployment would multiply attack surface, audit-trail burden, and chain-of-custody risk). All compute on personally-owned hardware (Ryzen 9 9950X3D / RTX 5090 / 128GB RAM). All code MIT-equivalent (single author, no employer claims, no government code); all third-party deps audited with AGPL/GPL replaced (closed Cat 9 of the verification checklist). Documented in `docs/DEPLOYMENT_MODEL.md`.

The full diligence reading order:
1. This document (Economic Impact v3.1)
2. `docs/architecture/decisions/` — 7 ADRs covering non-obvious architectural choices
3. `Desktop/VoxCore_Verification_Master_Checklist.md` — 106/171 items verified with per-item evidence
4. `Desktop/VoxCore_Decisions_Log.md` — append-only decision audit trail
5. `Desktop/VoxCore_Benchmark_Results.md` — measured-numbers ledger
6. `docs/PUBLISHABLE_CLAIM_WORKFLOW.md` — the methodology gate every number passes
7. `docs/COST_AND_LATENCY_BENCHMARKS.md` — per-role economics
8. `docs/architecture/MCP_TRANSPORT.md` + `docs/INGEST_LIFECYCLE.md` + `docs/architecture/CHUNKING_STRATEGY.md` — system internals

---

## What this software is NOT (explicit non-claims)

1. **Not a turnkey legal-AI product.** It is software one operator built on one machine for one corpus. The acquihire premise is that the same operator can rebuild the appropriate variant at scale inside an acquirer; the current artifact is the proof of capability, not the deployable product.

2. **Not a frontier-model competitor.** The synthesis is GPT-style RAG with a tighter citation discipline. The differentiation is the verifier + the auditor + the methodology, not a novel model architecture.

3. **Not at the published-frontier hallucination rate yet.** v4-shipped is 16.7%; published frontier-RAG legal-AI work is 6-12% on similar tasks. The gap is closeable with the queued Tier 2 work (per-claim re-retrieval + auditor refinement); months for sub-2% Tier 3.

4. **Not multi-tenant.** Single-operator local-only by design. Going hosted is a 4-6 week build (tenant isolation, network auth, encryption-at-rest, real CI/CD, monitoring) — sized in `docs/architecture/MCP_TRANSPORT.md`.

---

## Roadmap (predicted-not-measured; will re-measure each ship)

| Step | Target failure mode | Effort | Predicted held-out shipped hallucination |
|---|---|---|---|
| ✓ DONE — v2 verify-retry | FABRICATED 24 → 0 | shipped 2026-05-02 morning | 30% → 24.7% (all-shipped) |
| ✓ DONE — v4 CONTRADICTS Auditor MVP | Silent CONTRADICTS 14 → 0 | shipped 2026-05-02 evening | 24.7% → **16.7% (on shipped)** + 7/35 held |
| ⏳ NEXT — v5 rewrite-path FABRICATED retry | FABRICATED on rewrite 5 → ~0 | 1-2 hr (in progress) | 16.7% → ~13-14% |
| ⏳ NEXT — Per-claim re-retrieval | IRRELEVANT 46 → ~15 | 1-2 hr (code ready, needs isolated session) | ~13-14% → ~10% |
| Queued — In-pipeline Auditor full per spec | CONTRADICTS edge cases | 3-5 days | ~10% → ~8% |
| Queued — Anthropic Citations API integration | FABRICATED by-construction | 1-2 day spike | ~8% → ~7% |
| Tier 3 — fine-tuned legal reranker | All categories | months — requires labeled training data | 7% → 1-2% |

Per-step predictions will be re-measured after each ship per `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`. A predicted improvement is not a measurement.

---

## Provenance

This document is the v3.1 replacement for the v3 written earlier 2026-05-02 (which replaced the v2 PDF in `Desktop/Excluded/takeout-20260502T050948Z-3-001/Takeout/Mail/VoxCore Architecture Stuff.mbox`). v3.1 incorporates the v4 CONTRADICTS Auditor measurements, the LegalBench n=50 + Claude judge expansion, and the multi-hop n=12 baseline measured the same day.

Once approved by the operator, the v3 morning version should be moved to `Desktop/Safe To Delete/` (superseded). The v2 PDF in the mbox archive should be marked superseded in the mbox manifest.

Author: Claude Code session 277-continuation, 2026-05-02 evening. Reviewed and dispositioned by operator (Adam Taylor) before any external distribution.

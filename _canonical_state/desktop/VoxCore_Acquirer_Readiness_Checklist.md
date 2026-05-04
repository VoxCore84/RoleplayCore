# VoxCore — Acquirer-Readiness Checklist

**Purpose:** Diligence-survivable readiness inventory. What an acquirer's technology, IP, business, and people-diligence teams will check; what we have ready; what is gated; what is gap.

**Document type:** Internal preparation reference. Not for external circulation. Companion to (not replacement for) `VoxCore_Verification_Master_Checklist.md`, which remains the engineering-discipline document.

**Date prepared:** 2026-05-02 (incorporates session 277b state)
**Owner:** Adam Taylor
**Sequencing:** All "external use" items remain gated by JAG ethics opinion per Standing Directive #6.

**Evidence-tier conventions** (per `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`):
- **PROVEN** — measured with reproducible methodology, hostile-audit survivable
- **WELL-SUPPORTED** — measured but with known caveats or smaller N
- **PARTIALLY-SUPPORTED** — measured at small N or with methodology questions
- **INFERRED** — claimed without measurement; cannot be cited externally

---

## How to use this document

This is not the engineering checklist. The engineering checklist (`VoxCore_Verification_Master_Checklist.md`) is for hygiene; this document is for readiness.

Each row is phrased in the language an acquirer's diligence team uses. "Ready" means the item would survive a hostile audit by that team. "Gap" means the item would not survive, and the gap is explicitly named. "Gated" means the work is done but the item cannot be presented externally until a specific gate clears (almost always the JAG opinion).

Each section maps to one of the four diligence categories acquirers run in parallel. Within each section, items are ordered roughly by what the diligence team checks first.

When an item is marked **GAP**, the next column states what closing it requires. Gaps are not a problem; unacknowledged gaps are. The discipline this document enforces is: every gap surfaces explicitly, with a defined close path.

---

## Section 1 — Technology Diligence

Acquirer's technical due-diligence team. Engineering leadership plus a senior architect plus (often) a hands-on engineer who will pull the repo and read code. They evaluate: does it work, is it maintainable, can our team extend it, and what are the architectural risks.

### 1.1 Repo state and code quality

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 1.1.1 | Repo cleanly committed; no large uncommitted change sets | **READY** | Resolved 2026-05-02: commit `46a57adedb` removed 3,766 files (cmake/, contrib/, dep/, src/, sql/, scripts/). 18 untracked new-work files remain (normal). |
| 1.1.2 | Recent commit cadence visible and consistent | **READY** | Git log shows sustained engineering activity; session 277b alone produced 14 files / +3584 / -46 in commit `c3f40e6394`. |
| 1.1.3 | Build reproducible from clean clone in <30 minutes | **GAP** | README walkthrough: 43/45 paths resolve; 1 real bug fixed. Has not been walked through on a true clean shell. Close: clean-shell walkthrough by Code, document any remaining friction. |
| 1.1.4 | Dependency inventory current and license-clean | **GAP** | License remediation pending: PyMuPDF → pdfplumber, extract-msg → msg_parser, mysql-connector → PyMySQL. Pcodedmp audit pending. Close: items 1-3 + #4 of Top 50. |
| 1.1.5 | All dependencies pinned to exact versions | **GAP** | `requirements.txt` mixes `~=`, `>=`, exact pins. Close: item 13 of Top 50 (sequence after the swaps land). |
| 1.1.6 | No checked-in secrets, credentials, or API keys (current OR historical) | **GAP** | Single gitleaks scan against current tree only; full-history scan not yet run. Close: item 5 of Top 50. |
| 1.1.7 | No hardcoded paths, machine-specific configs, or local-only behavior | **PARTIALLY-SUPPORTED** | Most paths abstracted; `C:\Users\atayl\` references remain in some scripts. Close: targeted sweep before external review. |
| 1.1.8 | Linting and formatting consistent across codebase | **PARTIALLY-SUPPORTED** | No formal CI lint gate; ad-hoc consistency. Close: lower priority; document as roadmap. |

### 1.2 Architecture documentation

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 1.2.1 | High-level architecture documented with sequence diagrams | **READY** | `docs/INGEST_LIFECYCLE.md`, `docs/architecture/MCP_TRANSPORT.md`, plus 4 architecture docs shipped in session 277b round 3. |
| 1.2.2 | Triad orchestration model (Architect / Executor / Auditor) documented | **READY** | Documented in architecture docs and `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`. |
| 1.2.3 | Hybrid retrieval architecture documented (FTS5 + vector + KG, RRF, reranker) | **READY** | Knowledge graph build documented (session 273), retrieval pipeline documented across multiple sessions. |
| 1.2.4 | CONTRADICTS Auditor architecture documented | **READY** | `AI_Studio/2_Active_Specs/contradicts_auditor_v1_20260502_115918.md` (spec). MVP shipped + measured (session 277b round 4). |
| 1.2.5 | Governance gate (classification / sealing / privilege / scope) documented | **PARTIALLY-SUPPORTED** | Architecture exists; structural enforcement not yet implemented (currently cost optimization). Close: pending strategic decision per Decisions Log. |
| 1.2.6 | MCP tool surface documented (30+ tools across 6 servers) | **PARTIALLY-SUPPORTED** | MCP transport documented; per-tool schema validation not yet run. Close: item 12 of Top 50. |
| 1.2.7 | Five canonical task workflows documented end-to-end | **GAP** | Task brief for benchmark suite shipped today (`VoxCore_Task_Completion_Benchmark_Suite.pdf`); execution pending. |
| 1.2.8 | Single canonical query trace artifact (Architect → Executor → Auditor with logs) | **GAP** | Item 25 of Top 50; not yet built. |

### 1.3 Measured benchmarks (per session 277b state)

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 1.3.1 | Hybrid retrieval pass rate measured against held-out test suite | **PROVEN** | 92% (46/50). Evidence: `quality_probe_20260430_191844.json`. |
| 1.3.2 | LegalBench overall score measured with LLM-as-judge | **PROVEN** | 66.4% overall, n=50, Claude Opus 4.7 judge. Evidence: `legalbench_n50_claudejudge_20260502_135847.json`. |
| 1.3.3 | LegalBench binary task average reported separately | **PROVEN** | 80% binary average; reported alongside the overall number, not in place of it, per honest framing. |
| 1.3.4 | Citation precision (path-level) measured at production scale | **PROVEN** | 100% (302/302). Evidence: `citation_score_n30_20260502.json`. |
| 1.3.5 | Citation span correctness measured | **GAP** | LLM-as-judge wrapper for span correctness deferred per Decisions Log. Close: build wrapper (8-16 hrs); re-run; replace "span correctness pending" caveat. |
| 1.3.6 | Hallucination rate measured on held-out queries | **WELL-SUPPORTED** | 16.7% on shipped (v4 production); 24.7% baseline before CONTRADICTS Auditor. Evidence: `citation_score_holdout_n35_v4_claudejudge_20260502_142347.json`. |
| 1.3.7 | Zero silent CONTRADICTS shipped | **WELL-SUPPORTED** | 0/0 measured; Sonnet 4.6 inline auditor at 0.70 threshold. |
| 1.3.8 | Zero fabricated quotes shipped | **PROVEN** | Deterministic substring verifier; 0 fabricated on 28 delivered. |
| 1.3.9 | Multi-hop accuracy measured | **PARTIALLY-SUPPORTED** | n=12 small; 33% coverage / 39.6% on-coverage hallucination. Previously-claimed 82% multi-hop **WITHDRAWN**. Close: expand to n=50+. |
| 1.3.10 | Audio cross-instance WER measured | **WELL-SUPPORTED** | 0.59% on n=26. Evidence: `wer_cross-instance_20260502_031916.json`. |
| 1.3.11 | OCR character accuracy measured per document type | **WELL-SUPPORTED** | 24.26% avg CER; 0-5% on prose, 47-73% on layout-heavy forms. Reported with the per-document granularity. |
| 1.3.12 | Throughput per modality measured | **WELL-SUPPORTED** | PDF cold-cache 12,033 files/hour; identified as modality bottleneck. |
| 1.3.13 | Cost per query instrumented | **WELL-SUPPORTED** | ~$0.24 per query (v4 fully-judged). Evidence: `docs/COST_AND_LATENCY_BENCHMARKS.md`. |
| 1.3.14 | Latency p50 / p95 / p99 instrumented at role boundaries | **GAP** | Item 10 of Top 50; not yet executed end-to-end. |

### 1.4 Pause points (acknowledged roadmap items)

These are not "GAP" in the diligence sense — they are explicitly documented roadmap items, and acknowledging them honestly is the discipline. An acquirer's diligence team expects to see roadmap items; what they will not accept is finding pause points that were not disclosed.

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1.4.1 | Span correctness via LLM-as-judge wrapper | Roadmap | Deferred per Decisions Log. ~8-16 hr build. |
| 1.4.2 | Multi-hop coverage push (33% → target ~80%) | Roadmap | Spec via ChatGPT first per Triad rule. |
| 1.4.3 | CONTRADICTS Auditor v6: extend to PARTIAL/IRRELEVANT verdicts | Roadmap | 3-4 hr build + ~$10 to validate. Predicted held-out shipped halluc 16.7% → ~10%. |
| 1.4.4 | Forensic provenance with signed manifests | Roadmap | 2-4 weeks. Self-contained module. |
| 1.4.5 | Privilege-boundary structural enforcement | Roadmap | Currently cost optimization; pending strategic decision. |
| 1.4.6 | Classification marking detector | Roadmap | Item 32 of Top 50. ~4 hrs. |

### 1.5 Reproducibility

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 1.5.1 | LegalBench benchmark reproducible from fresh checkout | **WELL-SUPPORTED** | Harness exists (`tools/legalbench_harness.py`); setup guide partial. Close: item 16 of Top 50. |
| 1.5.2 | Citation precision pipeline reproducible | **PROVEN** | `tools/citation_scorer.py` self-test passes; runs against any corpus. |
| 1.5.3 | Retrieval probe reproducible | **PROVEN** | `tools/quality_probe.py` against `retrieval_test_suite.jsonl`. |
| 1.5.4 | Hallucination measurement reproducible | **WELL-SUPPORTED** | `tools/citation_holdout_synthesizer_v4.py` + `tools/inline_auditor.py`. Held-out queries at `citation_holdout_queries_v1.jsonl` (canonical n=35). |
| 1.5.5 | Knowledge graph build reproducible | **WELL-SUPPORTED** | NER pipeline documented in session 273 handoff. Defensive type guards in place. |

---

## Section 2 — IP & Chain-of-Title Diligence

Acquirer's IP diligence team — typically led by acquirer's outside M&A counsel. They evaluate: does the seller actually own this, is the chain unbroken, are there third-party claims, and are the open-source licenses clean.

### 2.1 Authorship and ownership

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 2.1.1 | Sole authorship of VoxCore documented | **GAP** | Affidavit not yet drafted. Close: `00_Summary/IP_Chain_of_Title_Affidavit_DRAFT.md` per checklist; sections 1, 2, 9. |
| 2.1.2 | No prior contractor, employer, or third-party claim | **GAP** | Negative documented in checklist; affidavit pending. |
| 2.1.3 | Personal hardware purchase receipts gathered | **GAP** | Folder 01 of chain-of-title checklist; not yet built. |
| 2.1.4 | Personal subscription billing records gathered | **GAP** | Folder 02 of chain-of-title checklist; not yet built. |
| 2.1.5 | Personal home network / ISP confirmed | **GAP** | Folder 01; one-page statement. |
| 2.1.6 | Git commit history extracted with timestamps | **GAP** | Folder 03; export trivial via `git log --all --pretty=format`. |
| 2.1.7 | Commit timestamp histogram (off-duty pattern documented honestly) | **GAP** | Folder 03; analysis from Git extract. Honest treatment of any duty-hours commits. |
| 2.1.8 | Domain registrations (voxcore84.github.io, etc.) WHOIS-personal | **GAP** | Folder 03; one-line check. |

### 2.2 Federal-employee separation

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 2.2.1 | No government equipment used | **GAP** | Folder 07; signed statement. |
| 2.2.2 | No government network used | **GAP** | Folder 07; signed statement. |
| 2.2.3 | No government data used | **GAP** | Folder 07; signed statement. |
| 2.2.4 | No duty time used | **GAP** | Folder 07; signed statement; supported by Git timeline analysis. |
| 2.2.5 | No government-funded research touched the work | **GAP** | Folder 07; signed statement. |
| 2.2.6 | Duty-position-no-nexus statement (clinical → legal AI, no overlap) | **GAP** | Folder 06. |
| 2.2.7 | LCSW credential-no-nexus statement (not clinical software) | **GAP** | Folder 06. |
| 2.2.8 | JAG ethics opinion in writing (any government-side disclaimer step) | **GATED** | Email to Tolin sent 2026-05-01 requesting non-Cannon ethics counselor referral. Awaiting response. |

### 2.3 Open-source license compliance

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 2.3.1 | Full dependency inventory exported | **GAP** | Folder 04 of chain-of-title; pip freeze + npm list. Trivial. |
| 2.3.2 | License per dependency documented | **GAP** | Folder 04; tooling exists. |
| 2.3.3 | No AGPL dependencies remaining | **GAP** | PyMuPDF swap pending (item 1 of Top 50); pdfplumber decided per Decisions Log. |
| 2.3.4 | GPL/LGPL dependencies isolated or removed | **GAP** | extract-msg → msg_parser pending (item 2). pcodedmp audit pending (item 4). |
| 2.3.5 | Permissive-license inventory clean (MIT, Apache 2.0, BSD) | **PARTIALLY-SUPPORTED** | Most dependencies are permissive; full inventory pending. |

### 2.4 Personal-corpus separation

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 2.4.1 | Personal case archive held strictly local | **READY** | Architecture enforces this; never used in commercial demos. |
| 2.4.2 | Commercial demos run against public corpora only | **READY** | Enron specified for benchmark suite; LibriSpeech + COCO for multimodal. |
| 2.4.3 | Personal photo archive held strictly local | **READY** | Per discussion 2026-05-01; not part of any transferable artifact. |
| 2.4.4 | Personal-corpus separation statement drafted | **GAP** | Folder 05; one-paragraph statement. |
| 2.4.5 | Governance design rationale (general-purpose, not informed by privileged case knowledge) | **GAP** | Folder 05; one-paragraph statement. |

---

## Section 3 — Builder Diligence

Acquirer's people-leadership and product team. They evaluate: who is this person, what will they produce inside our company, what is their domain understanding, and are there any background issues that affect retention.

### 3.1 Builder background documentation

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 3.1.1 | Three-pillar framing document complete | **READY** | `VoxCore_Builder_Background_Framing.pdf` shipped 2026-05-01. |
| 3.1.2 | Comprehensive accomplishment record | **READY** | `Adam_Taylor_Comprehensive_Accomplishment_Record.md` shipped 2026-05-01. |
| 3.1.3 | Defensible language inventory in place | **READY** | Page 19 of buyer-framing PDF. Phrase-pairs for systems-engineering, credential-vs-judgment, four-month claim, production-readiness. |
| 3.1.4 | Acceleration-curve timeline verified from Git history | **GAP** | Currently "approximately four months — to be confirmed from earliest VoxCore commit timestamp." Close: 10-min Git history extraction. |
| 3.1.5 | TrinityCore body-of-work narrative ready | **READY** | Section 4.1 of accomplishment record; specific achievements (transmog system, hotfix audit, TACTSharp pipeline, NPC pipeline, build diff audit, companion squads, Stormwind QA, LoreWalker import) documented with dates and outcomes. |
| 3.1.6 | Domain understanding (clinical → product judgment) framed correctly | **READY** | Pillar 2 of buyer-framing; aligned with chain-of-title separation. |
| 3.1.7 | Boundary statements consistent across documents | **READY** | Buyer-framing page 12 + chain-of-title folder 06 say the same thing in different language. |

### 3.2 Velocity and productivity signals

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 3.2.1 | Development velocity metrics extracted (commits/week, modality-add timeline) | **GAP** | One-page artifact; 1-2 hr work; recommended Top 50 entry per 2026-05-01 discussion. |
| 3.2.2 | Sustained engineering output during conditions of load documented | **PARTIALLY-SUPPORTED** | Resume evidence file in `~/.claude/projects/.../memory/resume-evidence.md` captures this per session. Cleaner external version not yet built. |
| 3.2.3 | Documentation discipline evidence | **READY** | Decisions Log, Benchmark Results ledger, master checklist, session handoffs (15+) all serve as evidence. |
| 3.2.4 | AI-native development workflow demonstrable | **READY** | Triad orchestration, MCP-native architecture, multi-LLM coordination all visible in the codebase. |

### 3.3 Retention-pricing inputs

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 3.3.1 | Geographic preference post-separation | **GAP** | Open Questions document; user decision pending. |
| 3.3.2 | Acceptable retention length | **GAP** | Open Questions; user decision. |
| 3.3.3 | Cash vs equity preference | **GAP** | Open Questions; user decision. |
| 3.3.4 | Walk-away number | **GAP** | Open Questions; user decision. |
| 3.3.5 | Open-source carve-out preference (MCP server layer) | **GAP** | Open Questions; user decision. |
| 3.3.6 | Plan B if no deal by EOY 2026 | **GAP** | Open Questions; user decision. |

These are not deliverables; they are user-side decisions that need to be made before negotiation, not before outreach. Surfaced here because an acquirer who senses indecision on these will use it.

---

## Section 4 — Business & Posture Diligence

Acquirer's deal team. They evaluate: is the seller representable, are there compliance issues, is there outreach posture that conflicts with the acquihire frame, and are the asks reasonable.

### 4.1 Compliance and posture

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 4.1.1 | JAG ethics opinion in writing | **GATED** | Tolin email sent 2026-05-01. Awaiting referral routing. |
| 4.1.2 | Civilian counsel engaged | **READY** | Joshua Tolin (Veritas Military Law) — multi-lane representation including SVC. |
| 4.1.3 | Active-duty constraints documented and being followed | **READY** | Standing Directive #6 enforces; no commercial activity ahead of opinion. |
| 4.1.4 | Decisions Log captures every commercial-adjacent decision contemporaneously | **READY** | Confirmed via session 277b uploads; entries for Boots to Business, TAP investor offer declined, Tolin email, Volare partnership awareness. |
| 4.1.5 | TAP class disclosures handled appropriately (declined investor offer) | **READY** | Decisions Log 2026-05-01. |
| 4.1.6 | No public marketing of VoxCore | **READY** | Website frozen per directive; no LinkedIn presence; no public pitches. |
| 4.1.7 | No premature commercial outreach | **READY** | All outreach gated by JAG opinion. |

### 4.2 Outreach materials staged

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 4.2.1 | 60-second pitch (general-audience) | **READY** | Delivered 2026-05-01 in TAP class; landed cleanly. |
| 4.2.2 | Acquirer-tuned pitch (60s) | **GAP** | Adapt from general-audience version when outreach authorized. |
| 4.2.3 | Pitch deck (full, 15-20 slides) | **GAP** | Build from buyer-framing + benchmark suite output + Economic Impact v3.1. |
| 4.2.4 | One-page leave-behind | **GAP** | Verification Summary 3-page exists per session 277b; one-page version pending. |
| 4.2.5 | Verification Summary (3-page external-facing) | **READY** | Shipped session 277b round 5. `Desktop/Do NOT Delete These/VoxCore_Verification_Summary_3page.md`. |
| 4.2.6 | Economic Impact PDF v3.1 (replaces withdrawn v2) | **READY** | Shipped session 277b round 5. v2 formally withdrawn per honest-framing discipline. |
| 4.2.7 | Outreach message templates (cold and warm) | **GAP** | Build when outreach authorized; reference deal-side counsel for review. |

### 4.3 Acquirer target list

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 4.3.1 | Primary candidates identified (Harvey, CoCounsel/Thomson Reuters, vLex, Casetext, Everlaw) | **READY** | Per acquihire playbook. |
| 4.3.2 | Secondary candidates (Anthropic, OpenAI for talent acquihire) | **READY** | Per playbook. |
| 4.3.3 | Federal-sponsor parallel candidates (AFWERX, DIU) | **READY** | Per playbook; specific program research pending if path activates. |
| 4.3.4 | Warm-introduction inventory | **GAP** | Begin building post-JAG; do not solicit before. |

### 4.4 Term-sheet readiness

| # | Item | Status | Evidence / close path |
|---|------|--------|----------------------|
| 4.4.1 | Active-duty deal-terms one-pager (handed to M&A counsel as starting position) | **GAP** | Cat 10 priority 7-8 of master checklist. Build before any term-sheet conversation. |
| 4.4.2 | Term-sheet redline checklist | **GAP** | Build when offer arrives, not before. |
| 4.4.3 | Valuation defense memo | **GAP** | Build when offer arrives. |
| 4.4.4 | M&A attorney engaged | **GAP** | Tolin handles current scope; M&A is separate engagement. Decision: scope-expand Tolin OR retain separate counsel. Pending Tolin call per 2026-05-01 email. |

---

## Section 5 — Standing Directives (preserved)

These are constants. They do not move. They are restated here so that any future Claude chat or any future reader of this document inherits the same constraints.

| # | Directive | Source |
|---|-----------|--------|
| 5.1 | **JAG ethics meeting gates external outreach.** No acquirer contact, no investor contact, no public marketing until written ethics opinion in hand. | Acquihire Playbook constraint #4; reinforced 2026-05-01 |
| 5.2 | **Website is FROZEN.** No updates until explicitly unfrozen. Thaw trigger needs to be documented or it sits frozen indefinitely. | Decisions Log 2026-05-01 |
| 5.3 | **Personal-corpus separation is absolute.** Personal case archive, personal photo archive, personal medical records all held strictly local. Never used in commercial demos, transferable artifacts, or training data. | Buyer-framing boundary statement; chain-of-title checklist |
| 5.4 | **Numbers are measured, not asserted.** If a number is not in `VoxCore_Benchmark_Results.md`, it is not measured. Withdrawn-claim discipline applies (Economic Impact v2 → v3.1). | `docs/PUBLISHABLE_CLAIM_WORKFLOW.md` |
| 5.5 | **Decisions Log is append-only.** Never edit prior entries. | Standing convention. |
| 5.6 | **Case_Reference is READ-ONLY.** New files allowed; existing files untouched. | Standing convention. |
| 5.7 | **No parallel Opus jobs.** API rate-limit contention costs $$ and wall time. Sequential or use serializer. | Session 277b operational warning |
| 5.8 | **Sub-agents inherit parent context billing.** Top 50 fan-out plan works only if Code uses standard context for spawned agents. Discussed 2026-05-01. | Decisions Log 2026-05-01 |

---

## Section 6 — Closing-checklist gates

Items that must be in hand before specific closing moments. Each is its own gate.

### 6.1 Before any acquirer outreach

- [ ] JAG ethics opinion in writing (5.1)
- [ ] License remediation complete (1.1.4, 2.3.3, 2.3.4)
- [ ] Repo clean (1.1.1)
- [ ] Pitch deck v1 ready (4.2.3)
- [ ] One-page leave-behind (4.2.4)
- [ ] Acceleration-curve timeline verified (3.1.4)

### 6.2 Before any term-sheet conversation

All of 6.1, plus:

- [ ] Active-duty deal-terms one-pager (4.4.1)
- [ ] M&A counsel engagement decision (4.4.4)
- [ ] User decisions on retention/cash-equity/walk-away (3.3)
- [ ] Chain-of-title affidavit and supporting folder complete (Section 2)
- [ ] Span correctness measured (1.3.5)
- [ ] Multi-hop expanded (1.3.9)

### 6.3 Before signing definitive agreement

All of 6.1 and 6.2, plus:

- [ ] Term-sheet redline checklist used (4.4.2)
- [ ] Valuation defense memo used (4.4.3)
- [ ] Definitive-agreement counsel review complete
- [ ] All Standing Directives still observed
- [ ] No drift from honest framing throughout deal-side conversations

---

## Section 7 — Revision policy

This document gets updated when any of the following occur:

- Status change on any line item (GAP → READY, READY → GAP if regression, etc.)
- New measured benchmark added to Benchmark Results ledger
- New Decisions Log entry that affects readiness state
- Standing Directive change (rare; logged separately)
- JAG opinion received (resets all GATED items to evaluable)
- Each major handoff session that produces measurable change to readiness state

Each update bumps the date at the top. Prior versions are preserved (not overwritten).

---

## Section 8 — Closing note

This checklist is not a to-do list. It is a readiness inventory.

The fact that many items show GAP does not mean the project is not ready. Most GAPs are mechanical, well-scoped, and fast to close (chain-of-title is gathering files; license remediation is three swaps; acceleration-curve verification is a Git query). The GATED items are the only ones with external dependencies, and the primary one (JAG opinion) is in motion.

What this document protects is honest accounting. An acquirer's diligence team finds gaps regardless. The discipline of surfacing them yourself, with named close paths, is what separates a clean acquihire from a contested one.

The work is real. The benchmarks are measured. The architecture holds. The framing is consistent across documents. What remains is mechanical completion and the JAG gate.

When this checklist shows zero GAPs in Sections 1, 2, and 3, and the GATED items in Section 4 have cleared, the launch decision is yours.

*End of Acquirer-Readiness Checklist. Internal reference. Not for external circulation.*

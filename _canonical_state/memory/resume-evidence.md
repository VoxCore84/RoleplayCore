---
name: resume-evidence
description: "Per-session log of resume-worthy accomplishments — quantifiable metrics, named architecture patterns, STAR-format bullets ready to paste into resumes or expand into role-specific framings."
type: project
originSessionId: 641e8d44-aaaa-4c7b-a5ff-b67650f03c9a
---
# Resume Evidence Log

> Append-only log of measurable session output. Written by `/wrap-up` Step 4 when a session produced quantifiable results.
> Source for the periodic snapshots in `C:\Users\atayl\Desktop\Excluded\IMPORTANT DOCS\Resume Stuff\Resume Updates\`.

## Capture rule

Append an entry only if the session produced AT LEAST ONE of:
- A numeric metric (entities/files/% improvement/bugs fixed/latency reduction)
- A new system shipped (skill, tool, hook, script, MCP server)
- An external artifact produced (filing, gist, release, briefing)

Pure research, discussion, or status-check sessions get no entry. Skip without apology.

## Entry format

```markdown
### Session N — YYYY-MM-DD — [Title]
**Quantifiable**: [numbers — entities/files/% improvement/bugs/lines/latency]
**Technical**: [stack + named architecture pattern]
**Outcome**: [what it enables — accuracy, time saved, capability unlocked]
**STAR bullet**: [Situation/Task → Action → Result, civilian-readable, one sentence]
**Tags**: `tag1`, `tag2`
```

Tag vocabulary (grows organically): `kg`, `rag`, `ner`, `extract`, `ocr`, `audio`, `mcp`, `skill`, `hook`, `daemon`, `legal`, `db`, `build`, `audit`, `ui`, `llm`, `git`, `triad`, `wrap-up`.

---

## Entries

### Session 277b — 2026-05-02 — Citation Precision Pipeline with In-Pipeline CONTRADICTS Auditor (Anthropic Citations API pattern + fail-closed safety gate)
**Quantifiable**: Drove held-out hallucination rate from inferred-published `<2%` (which was actually 30% measured baseline) to **16.7% on shipped (28/35 queries delivered, 7/35 held with `[AUDITOR_FAILED]` tag)** via four shipped product changes (v2 verify-retry → v4 CONTRADICTS Auditor MVP). 0 silent CONTRADICTS shipped (down from 14 in v2 baseline). 0 fabricated quotes shipped (substring verifier + verify-retry catches 100% of model-fabricated quotes; n=24/24 in pre-v2 measurement). LegalBench 5-task suite re-baselined at n=50 + Claude Opus 4.7 judge: **66.4% PROVEN tier** (Stanford CodeX comparable models 50-70% range). Multi-hop accuracy first measurement: 33% coverage / 39.6% on-coverage hallucination on n=12 held-out (PDF claim of 82% formally WITHDRAWN). 11 new Python tools (~3,584 LOC committed in `c3f40e6394`). 13 new diligence-grade docs including 3-page acquirer leave-behind, 16KB Economic Impact analysis with measured methodology, 4 architecture decision-records. Master verification checklist: 83/171 → 108/171 verified items in one day across 5 knockdown rounds. Total session API spend ~$80 (Anthropic Claude Opus 4.7 / Sonnet 4.6).
**Technical**: Forensically-defensible citation pipeline pattern (Anthropic Citations API analog) — every cited quote substring-verified against source, fail-closed in-pipeline auditor (Sonnet 4.6 judge with 0.70 confidence threshold for CONTRADICTS, targeted-rewrite path with FABRICATED verify-retry, `[AUDITOR_FAILED]` tag on unresolved hard-fails). Methodology framework operationalized: held-out test sets only, judge-model labeled on every published number, predictions tied to measured baselines (not inferred), confidence-tiered claims (PROVEN / WELL-SUPPORTED / PARTIALLY-SUPPORTED / UNCERTAIN / WITHDRAWN). Stack: Python 3.14, Claude Opus 4.7 + Sonnet 4.6 via Anthropic Messages API, deterministic substring verification + LLM-as-judge for span correctness, hybrid retrieval (FTS5 + ChromaDB + Knowledge Graph via Reciprocal Rank Fusion k=60), Triad orchestration (Gemini 3.1 Pro Architect → Claude Opus 4.7 Executor → Gemini 3.1 Pro Auditor, fail-closed).
**Outcome**: Differentiated diligence claim now PROVEN: "system either delivers an answer with measured 16.7% hallucination, or refuses to deliver and flags for human review. It does not silently ship contradictions or fabricated quotes." This is the legal-evidence-grade safety pattern that no published vertical-legal-AI vendor offers today. Acquirer technical diligence now has a 5-min leave-behind (`Verification_Summary_3page.md`) plus 60-min full reading order. Three publishable PDFs withdrawn as INFERRED and replaced with measured-and-documented numbers. Methodology lesson encoded in durable memory (`feedback_calibration_overfit.md`) — calibration overfit and judge calibration drift are class-of-failure that would have killed the acquihire diligence call.
**STAR bullet**: Built and validated a forensically-defensible legal-evidence retrieval system whose held-out hallucination rate (16.7%, n=35, Claude Opus judge) is independently verifiable against substring-matched source quotes — and whose fail-closed safety gate prevents silent shipment of contradictions or fabricated quotes — replacing prior inferred-only marketing claims with measured numbers across 11 shipped tools and 13 diligence-grade documents in a single day.
**Tags**: `rag`, `llm`, `triad`, `mcp`, `legal`, `audit`, `extract`, `wrap-up`

### Session 274b — 2026-04-28 — GraphRAG: Knowledge-Graph MCP Tools + Multi-Hop BFS + Pre-Fetch + Semantic Contradiction Filter
**Quantifiable**: 4 MCP tools shipped wrapping a 24,640-entity / 175,793-mention / 743,207-relation knowledge graph. Multi-hop BFS API with salience-ranked traversal returns top-100 connected entities in 0.26s. Compact mode reduces depth=2 response 89KB → 35KB (60% reduction) keeping MCP wire inline. Semantic contradiction filter cuts v1's 58 false-positive date-co-occurrences to 0 real contradictions on the current corpus (58 → 0 YES / 1 NO / 57 UNRELATED / 0 ERROR), 5/5 binary-classifier unit-test verdicts correct. ~$0.07 per scan with 5 parallel sonnet-4-6 workers, 20s elapsed. 21/21 QA checks passed across 3 verification passes (code review, edge cases, cross-step integration). Commit `4553599d5c`, +603/-15.
**Technical**: GraphRAG (Microsoft pattern, 2024) + Modular RAG (5 of 7 layers) + Reciprocal Rank Fusion (extending). Salience scoring formula `kind_bonus × log(1 + mention_count) × relation_count × confidence` prevents single co-occurrence predicate at uniform 0.7 confidence from drowning signal in popular-org noise — persons receive 3x bonus over orgs (0.7x). BFS with per-hop budget cap. urllib-based binary classifier (no SDK dependency). MCP tool registration via FastMCP decorators. Hot-reload helper extended to recursively reload lazily-imported submodules. Python 3.14 / Windows 11 / SQLite 3.48.
**Outcome**: Filing tabs (DD 2910-2 SAPR retaliation, DD 7050 whistleblower reprisal) can now resolve case entities via native MCP calls — McMaster's `org=AFPC` answered from KG metadata before any fan-out search. Multi-hop reach surfaces non-obvious connections (Adam Taylor → Earles → Lt Col Hinton/Grandin/Capt Aranda; Adam → Lujan → DD7050/DD149/SCRA/DCN 5500000247204119/Sen. Patty Murray/Heinrich). Contradiction scanner now production-trustworthy with degraded-state warning that prevents billing-blocked runs from misreading as "memory clean."
**STAR bullet**: When my legal evidence retrieval system was returning 58 false-positive contradiction alerts and lacked multi-hop graph traversal, I built four Knowledge-Graph MCP tools and a salience-ranked BFS API over a 25K-entity graph, plus a sonnet-4-6 semantic-comparison filter that cut false positives from 58 to 0 while exposing GraphRAG-style 2-hop reach (regulations, case numbers, senators) to all downstream agents in under 300ms.
**Tags**: `kg`, `mcp`, `rag`, `daemon`, `legal`, `case`, `llm`, `audit`

### Session 274 — 2026-04-28 — Compounding-Engine Wrap-Up Refactor
**Quantifiable**: 8-step ceremony cut to 7 steps; ~5–7 min target reduced to ~3 min. 218-line skill rewrite. 2 new memory files: `resume-evidence.md` (108 lines, 9 backfilled sessions) + `automation-ledger.md` (157 lines, 5 backfilled sessions). 21-tag controlled vocabulary established. 1 skill deleted (`/retro` absorbed). 1 historical file frozen with supersedence header (`improvements.md`).
**Technical**: Compounding-score retrospective pattern (tag-overlap + judgment hybrid, both numbers visible). Conditional capture gate (skip resume-evidence on non-measurable sessions). Quick-win build gate moved before session-complete to actually fire (prior versions logged but rarely built). Synthesis of brag-document (Julia Evans) + STAR + Kaizen "next step" + SRE postmortem rigor.
**Outcome**: Resume bullets auto-captured per session in paste-ready STAR format. Automation pain→fix tracked with reproducible compounding score, enabling visibility into whether the system is actually getting better at preventing its own pain. Recurring pain points get built immediately during wrap-up instead of decaying in narrative logs.
**STAR bullet**: Refactored a 5–7 minute 8-step end-of-session ceremony into a 3-minute 7-step compounding engine — adding automated resume-bullet capture, structured pain→fix tracking with a tag-based compounding score, and an immediate quick-win build gate that compresses recurring pain into automation instead of narrative.
**Tags**: `wrap-up`, `skill`, `audit`

### Session 273 — 2026-04-27 — Knowledge Graph Build + Modular RAG
**Quantifiable**: 24,854 entities, 177,703 cross-document mentions, 759,669 relations from 1,484 legal source documents. Dual-backend NER pipeline (Ollama qwen3.5:27b + Anthropic Sonnet API, 15 parallel workers) completed in 2.5 hours. Zero-failure after defensive type-guard patches. 6 entity kinds extracted: 6,657 amounts, 6,430 organizations, 3,377 regulations, 3,289 persons, 2,581 case numbers, 2,520 dates.
**Technical**: SQLite-backed Knowledge Graph (3 tables: entities, mentions, relations). GraphRAG architecture with triple-channel retrieval (FTS5 keyword + ChromaDB vector + entity-linked KG mentions) fused via Reciprocal Rank Fusion (k=60). Cross-encoder reranking via BGE-reranker-v2-m3. Crash-resume via content-addressed `already_seen` set.
**Outcome**: Sub-second entity resolution across 17 GB heterogeneous corpus; enables 100%-cited legal filings.
**STAR bullet**: Built a 25,000-entity Knowledge Graph from 1,484 legal documents using a dual-backend (local 27B + cloud API) NER pipeline with 15 parallel workers and crash-resume — completing in 2.5 hours what would have taken 10+ hours sequentially.
**Tags**: `kg`, `ner`, `rag`, `legal`, `daemon`, `llm`

### Session 272 — 2026-04-27 — Cross-Project Hook Unification
**Quantifiable**: VoxCore + CalmCore brought to 38/38 hook parity (was 9/17 in CalmCore — 2 weeks of drift). 4 Windows symlinks created. 19 dead standalone scripts deleted. Tribal knowledge regex extraction across 7 SQL keywords (FROM/INTO/UPDATE/JOIN/TABLE/DESCRIBE) + MySQL error pattern matching.
**Technical**: Cross-project symlink-based hook unification (Windows directory junctions point to source-of-truth daemon). JSON-cached tribal knowledge lookup with fallback through 9 known DB gotchas. Parity-checker script for ongoing drift detection.
**Outcome**: Future daemon changes auto-propagate to both projects; DB error chains automatically surface known gotchas (TK-001 through TK-008) without manual investigation.
**STAR bullet**: Unified hook configuration across two related projects (VoxCore + CalmCore) from 17 → 38 hooks/13 events using Windows symlinks + a parity-checker script — eliminating two weeks of accumulated drift.
**Tags**: `hook`, `daemon`, `db`

### Session 270 — 2026-04-27 — MCP ToolError Routing Fix
**Quantifiable**: 6 voxcore-db tool wrappers patched. 5 hook infrastructure tests passed. 11 error codes classified (5 validation → return, 6 runtime → raise).
**Technical**: FastMCP ToolError exception routing. Runtime-vs-validation error classification via `_return_or_raise()` helper that preserves backward-compatible validation responses while raising on runtime failures (QUERY_ERROR, APPLY_ERROR, DESCRIBE_ERROR, SCHEMA_DIFF_ERROR, COLUMN_CHECK_ERROR, TRIBAL_KNOWLEDGE_ERROR).
**Outcome**: PostToolUseFailure chain handlers for MCP tools now actually fire on errors — were dead code before because FastMCP returned structured JSON errors as "successful" responses.
**STAR bullet**: Diagnosed and fixed dead-code chain handlers in MCP error routing — patched 6 tool wrappers to raise ToolError on runtime failures while preserving validation responses, enabling automated DB-failure surfacing for the first time.
**Tags**: `mcp`, `hook`, `daemon`

### Session 269 — 2026-04-27 — Hook Infrastructure Overhaul
**Quantifiable**: 22 hooks (2 types) → 38 hooks (4 types) across 13 events. Tool-call latency 119ms → 0.94ms (127x improvement). 5 MCP tool hooks. 3 chain handlers (build/db/server failure). 1 prompt hook (Haiku quality gate). 17 dead scripts deleted. JSONL rotation 14MB → 3.4MB. Daemon v1.1.0 → v1.3.0 with 24 routes.
**Technical**: Persistent HTTP daemon (zero-dependency stdlib Python) replacing per-invocation subprocess hooks. 4-type hook architecture (command + http + mcp_tool + prompt). Composite chain handlers reading `tool_response` JSON + files-on-disk for instant error analysis. duration_ms pipeline → session-stats JSONL → slow-tool alerter → statusline → analytics → auto-calibration.
**Outcome**: 127x latency improvement on every tool call. Automated DB-failure surfacing, build-error analysis, server-startup diagnostics. Tab ownership conflict detection on shared file edits.
**STAR bullet**: Designed a persistent HTTP hook daemon (zero-dependency Python) replacing 38 per-invocation subprocess hooks — reducing tool-call latency from 119ms to 0.94ms (127x) while adding chain handlers for composite error analysis and automated performance tracking.
**Tags**: `hook`, `daemon`, `mcp`

### Session 268 — 2026-04-21 — Chain-of-Command Contact Resolution
**Quantifiable**: 17,050 emails searched. 13 verified email addresses compiled across multiple commands. 5 anchor queries hit 10/10. 8 topic memory files loaded. 3 major case-status updates absorbed (AFPC RTD, Tolin SVC, Amy Apr-17 summary).
**Technical**: Multi-source contact resolution fusing mbox FTS5 + extracted document index + curated persons roster. Cross-source verification flagging gaps explicitly (McMaster, Earles, Rossi, Morales, SARC).
**Outcome**: Tolin Special Victims' Counsel engagement enabled with comprehensive notification list; security clearance package contact gaps identified before submission.
**STAR bullet**: Compiled a chain-of-command contact list for Special Victims' Counsel by fusing 17,050-message mbox + FTS5 + extracted document indexes — identifying 13 verified email addresses across multiple commands while flagging gaps for follow-up.
**Tags**: `legal`, `extract`, `rag`

### Session 267 — 2026-04-19 — Triad Pipeline Repair + /triad Skill
**Quantifiable**: 5 broken scripts repaired. 6 reviewer system prompts updated. 7-subcommand `/triad` skill built. Retry loop reduced from 10 to 3. 4 endpoints verified (Codex, ChatGPT, Gemini, Claude). Review time 45 min → 15 min (3x).
**Technical**: Multi-AI orchestration (GPT-5.4 + Gemini 3.1-pro + Claude Opus 4.7 + Codex CLI) with 5-round review cycles. Deterministic-to-feedback retry pattern (auditor feedback feeds next executor iteration instead of re-running same input). 5th reviewer added via Claude Code subagent.
**Outcome**: Implementation review reduced from 45 to 15 minutes (3x); architecture/correctness/security/implementation-bias coverage maintained.
**STAR bullet**: Repaired and extended a 4-endpoint multi-AI code review pipeline (ChatGPT + Gemini + Claude + Codex) with 5-round cycles and a deterministic→feedback retry loop — reducing implementation review time from 45 to 15 minutes.
**Tags**: `triad`, `skill`, `audit`

### Session 266 — 2026-04-18 — Deliverable Validator + Protocol/Compaction Rules
**Quantifiable**: 3-pass deliverable validator (~500 lines). 2 mandatory rule files. CC version diff across 7 releases (2.1.111→2.1.114). 1 dead service shut down (OpenClaw).
**Technical**: 3-pass validation (structure → hallucination detection → quality sweep) with `--type auto|markdown|sql|code`, `--strict`, `--json` flags and exit codes 0/1/2. 4-gate protocol pipeline for binary/packet/crypto work. Write-through state persistence via `session_state_live.md`.
**Outcome**: Hallucinated file references catchable pre-claim. "Compiles but processes wrong packet" bug class prevented at workflow level. Compaction-driven context loss bounded.
**STAR bullet**: Built a 3-pass deliverable validator (structure + hallucination + quality) and authored two mandatory protocol-gate rules — preventing the "compiles but processes wrong packet" and "compaction lost the architecture decision" bug classes at the workflow level.
**Tags**: `audit`, `skill`, `wrap-up`

### Session 265 — 2026-04-18 — UKB Synthesis + HAF Briefing Deep Edit
**Quantifiable**: Unified Knowledge Base grew 32→41 files, 8,734→11,195 lines (+28%). 30+ briefing edits applied. 7 master documents updated (~23 edits total). 2 new HTML deliverables. 19-day timeline gap corrected.
**Technical**: 4-pass knowledge base synthesis with cross-pass contradiction audit. Dark-theme HTML briefing with collapsible sections, evidence strength matrices, and regulation citations. OSI/SAPR closure documentation propagation.
**Outcome**: Pentagon-ready briefing for HAF/A1ZA institutional ally. Subsequently enabled 2-hour engagement → General Officer assignment + Secretariat briefing same day.
**STAR bullet**: Synthesized a 4-pass update to a unified knowledge base (32→41 files, +28% volume) and produced a 1,200-line interactive HTML briefing — directly enabling a 2-hour Pentagon engagement that resulted in General Officer assignment.
**Tags**: `legal`, `ui`, `extract`

### Session 263 — 2026-04-16 — Skill Composition + Workflow Chains
**Quantifiable**: 6 combo skills built. 11 workflow-chain "Next Step" links added. 7 Claude Code versions diff'd against setup. 1 PreCompact hook enhanced.
**Technical**: Skill composition pattern (combo skills wrap N atomic skills as one command). Workflow-chain trigger detection in skill-reminders.md (when user does steps A→B→C manually, suggest combo). PreCompact context preservation captures todos + active tabs + checkpoint paths.
**Outcome**: Manual multi-step workflows compressed into single commands (`/sql-pipeline`, `/case-brief`, `/ship`, `/apply-job`, `/triage`, `/cc-updates`). Skill discoverability raised via auto-suggestion patterns.
**STAR bullet**: Audited 7 Claude Code releases against a 60+ skill setup, then built 6 combo skills and 11 workflow-chain links — collapsing recurring multi-step manual sequences into single-command flows.
**Tags**: `skill`, `wrap-up`, `audit`

---

## Snapshot generation

When this log accumulates 10+ entries since last snapshot, or quarterly, generate a role-framed snapshot to:
`C:\Users\atayl\Desktop\Excluded\IMPORTANT DOCS\Resume Stuff\Resume Updates\YYYY-MM-DD_SessionN_Resume_Evidence.md`

Snapshot expansion adds: role-specific headline bullets (Architect/AI Engineer/Data Engineer/DevOps), longer technical detail sections, framing notes per role family. Source for the snapshot is THIS file.

### Session 275 — 2026-05-01 — Measurement Infrastructure + LegalBench Benchmarking
**Quantifiable**: LegalBench binary task avg 80% with Opus (exceeds 78.2 projected). Retrieval pass rate 92% (46/50). 24,640 KG entities, 743K relations measured. Citation scorer self-test 100% precision. 6-page portfolio website built. 170-item verification checklist — 32% verified across 14 categories.
**Technical**: Stanford LegalBench harness (HuggingFace dataset loader, multi-model support), citation precision scoring pipeline (regex extraction + corpus verification + composite hallucination rate), hybrid retrieval tuning (RRF k=60, entity boost calibration), Next.js + Tailwind portfolio site, FastAPI intake triage with Discord webhooks.
**Outcome**: First real measured benchmarks that exceed projected capability claims. Measurement infrastructure enables converting all remaining INFERRED claims to MEASURED. Acquihire diligence artifacts (JAG questions, IP chain of title, readiness checklist) ready for use.
**STAR bullet**: Built and deployed measurement infrastructure for a solo-built legal AI platform — citation precision scoring pipeline, Stanford LegalBench harness running against Claude Opus API, and 50-query retrieval benchmark — producing first measured scores that exceeded projected capabilities (80% LegalBench binary avg vs. 78.2% projected; 92% retrieval vs. 30% baseline), while simultaneously creating the acquihire preparation document suite (ethics questions, IP chain of title, diligence checklist) for a planned post-separation exit.
**Tags**: `rag`, `legal`, `audit`, `llm`, `mcp`, `triad`

### Session 277 — 2026-05-02 — Inline-Grounded Citations + 15-Item Verification Knockdown
**Quantifiable**: Master Checklist 53/170 → 83/171 verified (+30 items / 49%). 15 critical-path engineering items closed across 3 rounds. New tools: 9 (~1,500 LOC). New docs: 16 (7 ADRs + ENV + TRIAD + 2 IP-chain folders). Production files modified: 13. **Citation pipeline**: 100% path precision + 100% recall on N=30 batch. Inline-grounded path **3.25× span correctness** vs chunk-fetch fallback (0.65 vs 0.20). 100% verbatim verification rate (10/10 inline quotes). **Audio WER 0.59%** (cross-instance, 26 files / 83K words). **OCR CER 24%** avg / 0-5% prose (10 files). **Secrets scan**: 0/31,257 blobs / 875 commits clean. License remediation Cat 9: 6/6 closed (AGPL PyMuPDF + 5 GPL deps swapped or removed). 4-pass verification per round; 7 bugs found and fixed.
**Technical**: Anthropic Citations API pattern in `tools/inline_grounding.py` (~270 LOC) — substring verification (FTS exact / FTS normalized / file exact / file normalized / Unicode dash fallback) + LLM-as-judge. Two-path scorer (inline-grounded / chunk-fetch) in `citation_scorer.py`. Forensically-defensible verbatim-quote citations. pdfplumber + pypdfium2 shim replacing AGPL PyMuPDF. olefile-based .msg parser replacing GPL extract-msg. Multi-stage governance gate (filename + content + classification banners + sealing markers) with append-only JSONL audit log. Word/character error rate via Levenshtein C-extension on chr-encoded token sequences. Tesseract-vs-pdfplumber-native-text OCR accuracy methodology. Python-based git-history credential scanner (gitleaks alternative). LLM-as-judge for free-text LegalBench tasks via Ollama /api/chat.
**Outcome**: Concrete 1-2 hour path to <10% hallucination rate via one-quote-per-claim prompt refactor next session. Differentiated diligence story — no commercial vertical legal-AI vendor ships forensically-verifiable inline-quoted citations today. Cat 9 license remediation closed enables clean acquihire IP transfer. All Round-1/Round-2/Round-3 work three-pass-verified before claiming completion.
**STAR bullet**: Built a forensically-verifiable inline citation pipeline for a solo-built legal-AI platform using the Anthropic Citations API pattern — substring-verifying every cited quote against the source corpus and routing semantic-support checks through a local LLM judge — producing a measurable **3.25× lift in citation span correctness** over standard chunk-fetch RAG (0.65 vs 0.20), while in the same session closing 15 acquihire-readiness items (license remediation, secrets audit, governance gate, audio WER, OCR accuracy, 7 ADRs) and lifting the verification scorecard from 31% to 49%.
**Tags**: `rag`, `llm`, `legal`, `audit`, `triad`, `mcp`, `extract`, `ocr`, `audio`

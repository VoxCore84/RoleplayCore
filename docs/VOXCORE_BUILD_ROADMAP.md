# VoxCore Build Roadmap

**Status:** Engineering sequencing document — WHAT to build and in what order.
**Last updated:** 2026-05-26
**Source:** `AI_Studio/Reports/system_inventory_2026-05-26/` (BUILD_VS_IMPROVE_DECISION.md Q10,
COST_BANKING_READINESS.md, NEXT_IMPLEMENTATION_PROMPT.md, EXISTING_SYSTEMS_MAP.md)

**Companion docs:**
- Granular architecture choices → `docs/architecture/decisions/` (ADR 0001–0007)
- Engineering/strategy decisions → `docs/VOXCORE_DECISION_LOG.md`
- Commercial decisions → `_canonical_state/desktop/VoxCore_Decisions_Log.md`

---

## Guiding principle

VoxCore already has the hard parts: hybrid FTS5+vector+KG retrieval at 92.0% baseline,
5 MCP servers (33 tools), 2 daemons, 28 agents, 79 skills, a 272 MB live KG, and a
reproducible eval harness. Almost every advanced-feature recommendation is an **improvement
to or duplicate of an existing system**, not a new one. The blockers are consolidation and
entanglement, not missing infrastructure.

Priority order: unblock first; improve existing second; add net-new capabilities only when
the existing foundation is solid.

---

## Item 0: Consolidation and repo hygiene (CURRENT ARC)

### What
Clear uncommitted entanglement and untracked infrastructure that blocks downstream items.
This is the output of the 2026-05-26 inventory session. No new systems built.

### Preconditions
None — this IS the precondition for everything else.

### Exact files involved
- `tools/citation_scorer.py` — +93 uncommitted lines (Phase 3.9 judge-package hook)
- `tools/quality_probe.py` — +23 uncommitted lines (Phase 4 HyDE eval channel)
- `tools/excluded_hybrid_search.py` — +105 uncommitted lines (Phase 4 HyDE refactor)
- `config/backend_selection.yaml` — untracked (model_router.py depends on it; broken on fresh checkout without it)
- `.claude/rules/documentation-discipline.md` — untracked sibling of tracked rules
- `.claude/rules/measurement-discipline.md` — untracked sibling of tracked rules
- `.claude/rules/session-handoff.md` — untracked sibling of tracked rules

### Decision required per entangled file
For each of the three entangled tools (citation_scorer, quality_probe,
excluded_hybrid_search), owner must choose: (a) commit as its own commit, (b) defer to
the authoring session, or (c) discard. Do NOT mix a new edit with the prior-session work.

### Risks
- Overwriting prior-session uncommitted work (mitigated: explicit per-file decisions, stage
  by explicit filename only, never `git add -A`)
- Committing unreviewed rules that reference personal paths (mitigated: grep for Excluded/
  IMPORTANT DOCS/Case_Reference/Desktop before committing)
- Entangled files carrying Phase 3.9 + Phase 4 work not yet ready for the main branch

### Tests/evals required
- `python tools/model_router.py --print` resolves all 16 ops after yaml is committed
- `python tools/anthropic_helpers.py` self-test passes after commit
- `python tools/quality_probe.py --engine fts` still reports 92.0% (unchanged by hygiene commit)
- Rules committed: verify no personal paths via grep

### Definition of done
- `config/backend_selection.yaml` committed; the 3 untracked rules committed
- A recorded decision for each of the 3 entangled files (committed / deferred / discarded)
- A recorded disposition for each of the 2 dormant control planes (see Item 1 below)
- No new system built; no daemon restarted; no API spend; no prior-session work overwritten

### What NOT to do
- Do NOT restart `hook_daemon.py` — 2-project blast radius (VoxCore + CalmCore via symlink)
- Do NOT `git add -A` or commit anything matching Excluded/IMPORTANT DOCS/Case_Reference
- Do NOT start GraphRAG, MCP wrappers, or any new feature build
- Do NOT add prompt caching anywhere — verified $0 no-op (169-tok judge prompt < 1024 cache floor)

---

## Item 1: Cost banking — Batch API on eval sweeps

### What
Wire `tools/anthropic_helpers.py`'s batch dry-run into the eval sweep, reducing eval cost
by approximately 50% on each 50-query gold-set run. Build in a NEW file (`tools/batch_eval.py`)
to avoid touching the entangled tools.

### Preconditions
- **Item 0 complete** — entangled files (citation_scorer.py, quality_probe.py) must be
  reconciled/committed before any new edit to those paths
- `config/backend_selection.yaml` committed so model_router works on fresh checkout
- Adam GO on which entangled-file disposition was chosen

### Exact files involved
- `tools/batch_eval.py` — NEW file; collects judge requests as `[{custom_id, params}]`,
  calls `anthropic_helpers.submit_batch(requests, dry_run=True)` by default, `--submit`
  for live runs
- `tools/anthropic_helpers.py` — READ-ONLY in this item (infra already exists)
- `tools/quality_probe.py` — READ-ONLY or touched only AFTER reconciliation
- `tools/citation_scorer.py` — READ-ONLY or touched only AFTER reconciliation

For model_router adoption: pick ONE highest-volume hardcoded-model call site and swap in
`select_backend()`. Candidate: the `JUDGE_MODEL` default in `citation_scorer.py` (after
reconciliation). Do NOT adopt across all call sites in one pass.

### Risks
- Async batch turnaround (Anthropic Batch API SLA is up to 24h) — synchronous path must
  remain default; batch is an opt-in `--batch` mode for offline eval sweeps only
- Mixing batch cost tracking with the synchronous path adds complexity; keep them separate
- Caching is a verified $0 no-op at VoxCore's call sizes — do not add it

### Tests/evals required
- Dry-run outputs a valid `requests.jsonl` (inspectable, no spend)
- Live-run produces the same pass rate as synchronous eval (92.0% ± 0pp on same gold set
  and snapshot, per measurement-discipline: cite gold-set name, snapshot id, run id)
- Cost delta measured: before (sync cost) vs after (batch cost), same N queries
- Regression check: synchronous path still works after batch file addition

### Definition of done
- `tools/batch_eval.py` committed; `--batch` flag documented in tool docstring
- One dry-run succeeded (no spend); one live-run (or N-query subset) measured vs baseline
- Synchronous eval path unchanged and still reproducible at 92.0%
- Cost delta documented with provenance (run_id, gold_set_version, snapshot_id)

### What NOT to do
- Do NOT add caching — verified no-op
- Do NOT refactor quality_probe.py or citation_scorer.py in the same commit as batch_eval.py
- Do NOT adopt model_router at more than one call site in this item
- Do NOT submit a live batch run without first inspecting the dry-run output

---

## Item 2: Hook promotion — sql-write-monitor and SubagentStop

### What
Promote two dormant hook routes that are already implemented but not wired:
- **CC-05 SubagentStop breadcrumb** (C3): `hook_daemon.py:_subagent_complete_work` — activates
  automatically on next natural daemon reload; no settings change needed
- **sql-write-monitor** (C4): route exists in `hook_daemon.py`; needs one entry in
  `.claude/settings.json` to become active (log-only mode)

### Preconditions
- Item 0 complete (clean repo state)
- A natural daemon reload event (server restart, etc.) — do NOT force-reload for this

### Exact files involved
- `.claude/hooks/hook_daemon.py` — READ-ONLY (route already implemented as C4)
- `.claude/settings.json` — ADD one hook event for sql-write-monitor (log-only)
- Test: simulate a SQL write event after wiring and verify log output

### Risks
- Forced daemon reload: HIGH blast radius — disrupts all open tabs and CalmCore (via 4
  symlinks). Never force-reload for hook promotion; let it happen naturally
- Settings change to `.claude/settings.json` takes effect immediately across all tabs
- sql-write-monitor must be log-only initially; never auto-reject or auto-rollback

### Tests/evals required
- After natural reload: verify SubagentStop fires on next subagent completion (check daemon
  log for `_subagent_complete_work` event)
- sql-write-monitor: run a SQL-writing tool call and verify the route logs it (no action)
- Regression: run `python tools/quality_probe.py --engine fts` and confirm 92.0% unaffected

### Definition of done
- SubagentStop breadcrumb active (confirmed via daemon log after natural reload)
- sql-write-monitor logging SQL write events (confirmed via log inspection)
- No forced daemon restart; no regression on retrieval baseline
- Rollback documented: remove the settings.json entry to disable sql-write-monitor

### What NOT to do
- Do NOT force-restart the daemon for this item
- Do NOT promote sql-write-monitor to auto-reject mode without a separate Adam GO
- Do NOT wire any other dormant hooks in the same settings.json edit

---

## Item 3: Typed KG edges

### What
Replace the universal `predicate='mentioned_with'` relation (all 743,207 relations today)
with extracted typed (subject, predicate, object) triples. This is the upstream unlock for
both GraphRAG (Item 4) and the Contradiction Engine (Item 5).

### Preconditions
- **Item 0 complete** (clean repo, no entangled files)
- **Item 1 complete or confirmed unnecessary** — typed-edge extraction uses the same eval
  harness; don't run a paid extraction pass without cost controls in place
- Adam GO: this is a real build with per-chunk LLM extraction cost
- Design review: propose the relation schema to Adam before extracting (what predicates?
  what granularity? what entity types?)

### Exact files involved
- `tools/excluded_daemon/kg/build.py:411` — the co-mention predicate assignment; this is
  where typed predicates replace `mentioned_with`
- NEW: `tools/kg_triple_extractor.py` — per-chunk triple extraction (LLM call per chunk);
  reads the existing 24,640-entity graph as context for entity resolution
- `.cache/excluded_kg.db` — 272 MB live KG; migrated in-place or rebuilt from scratch
  (rebuilding is safer; document the choice)
- `tools/quality_probe.py` — A/B eval before and after migration; 92.0% must be preserved

### Risks
- Paid API cost: per-chunk extraction over the full corpus is significant. Estimate tokens
  per chunk × chunk count × model price before submitting. Use Batch API (Item 1) to
  reduce cost
- KG rebuild loses the existing co-mention graph during migration window; document rollback
  (backup `.cache/excluded_kg.db` before any migration)
- Entity resolution drift: new typed predicates may resolve entities differently than the
  co-mention graph; validate with a subset before full rebuild
- The 92.0% baseline must survive; run `quality_probe.py` A/B before and after

### Tests/evals required
- Design: proposed relation schema reviewed and approved before any extraction
- Subset test: extract typed triples from 100 chunks; manually inspect for predicate quality
- A/B eval: `quality_probe.py` on same gold set before and after migration; delta reported
  with provenance (run_id, snapshot_id, gold_set_version)
- Regression: docs-rag MCP `kg_entity/kg_mentions/kg_relations` tools still return correct
  results after migration
- Spot-check: sample 20 (subject, predicate, object) triples and verify against source docs

### Definition of done
- `build.py:411` updated; no chunk produces `predicate='mentioned_with'`
- At least 5 meaningful predicate types extracted and documented
- A/B eval shows 92.0% preserved (or improvement noted with provenance)
- KG backup exists at `_vault_only/reconciliation_backups/excluded_kg_pre_typed_<date>/`
- docs-rag MCP tools functional against the migrated KG

### What NOT to do
- Do NOT start GraphRAG or Contradiction Engine until this item is done and A/B'd
- Do NOT delete the co-mention backup before confirming the typed-edge KG passes eval
- Do NOT build typed edges without first getting Adam GO on the relation schema
- Do NOT run full-corpus extraction without first estimating and approving the API cost

---

## Item 4: GraphRAG — multi-hop traversal

### What
Add multi-hop graph traversal to the retrieval pipeline, leveraging the typed KG edges
from Item 3. The `graphrag/PLAN.md` scaffold exists and is intentionally untouched until
now. This enables structural questions: "every filing before this judge," "every party
co-mentioned with entity X in clinical context."

### Preconditions
- **Item 3 complete and A/B'd** — typed edges must exist and be proven stable
- The 92.0% baseline must be the A/B reference; GraphRAG is evaluated against it
- Adam GO on the specific multi-hop traversal design before building

### Exact files involved
- `graphrag/PLAN.md` — scaffold; read before implementing, do not blindly execute
- `tools/excluded_hybrid_search.py` — hybrid retrieval pipeline; GraphRAG is added as a
  FOURTH channel to the existing FTS5+vector+KG-entity RRF stack (not a replacement)
- `tools/quality_probe.py` — A/B eval; GraphRAG channel tested as additive, with a
  channel-ablation study (all 4 channels vs 3 vs 2) to confirm it adds net lift

### Risks
- Multi-hop traversal on 743K+ typed relations can be expensive without traversal limits;
  document max-hop depth and timeout before shipping
- Adding a fourth RRF channel shifts the fusion weights; re-tune entity_path_boost if
  needed, per measurement-discipline (document the tuning experiment)
- GraphRAG may regress on financial/brand queries (same pattern as KG-channel regresssion
  in ADR 0007); test per-category, not just headline pass rate

### Tests/evals required
- A/B: 4-channel (FTS5+vector+KG-entity+GraphRAG) vs 3-channel (current) on same gold set
- Per-category breakdown: report both regressions and lifts (no cherry-picking)
- Traversal-limit stress test: verify max-hop depth prevents runaway queries
- Latency: report p50/p95 wall-clock before and after; document acceptable latency delta

### Definition of done
- GraphRAG adds measurable net lift on at least one query category without regression on others
- A/B results documented with provenance and per-category breakdown
- Max-hop depth and traversal timeout documented and enforced
- 92.0% baseline preserved or exceeded

### What NOT to do
- Do NOT build GraphRAG before typed edges (Item 3) — it requires them structurally
- Do NOT wholesale replace the existing RRF stack; add GraphRAG as a fourth channel
- Do NOT report only the positive categories; report all per-category deltas

---

## Item 5: Contradiction engine

### What
Surface contradictions between documents in the corpus: conflicting factual claims,
date inconsistencies, regulation mismatches. The `contradiction/PLAN.md` scaffold
exists but is blocked on typed edges (required for reliable entity and predicate lookup).

### Preconditions
- **Item 3 complete** (typed edges required for contradiction lookups)
- The contradiction scaffold (`contradiction/PLAN.md`) reviewed before implementation;
  do not treat the scaffold as a ticket — it requires Adam GO to execute

### Exact files involved
- `contradiction/PLAN.md` — scaffold; read before building, requires Adam GO
- `tools/excluded_hybrid_search.py` — retrieval; contradiction engine queries it
- `tools/ai_studio/review_cycle.py` — Triad auditor role is the natural home for
  contradiction flagging in the final review pass

### Risks
- False-positive contradictions on clinical records are high-stakes: a "contradiction"
  between two clinical notes may be a legitimate change-over-time, not an error
- Contradiction detection is only as good as the relation schema from Item 3; run the
  contradiction engine only after the A/B from Item 3 confirms relation quality
- High computational cost if run across the full corpus naively; scope to query-driven
  (contradiction check on a specific claim, not a full-corpus scan)

### Tests/evals required
- Design: contradiction schema and detection strategy reviewed before building
- Test set: at least 20 manually labeled (contradiction / not-contradiction) pairs from
  the corpus; precision/recall reported with conservative judge calibration
- False-positive rate on clinical records: specifically audit the clinical category
- Integration test: contradiction flag surfaces in Triad Auditor output

### Definition of done
- Contradiction engine returns meaningful results on at least 10 real cross-document pairs
- False-positive rate on clinical records measured and documented
- Integration with Triad Auditor confirmed
- The scaffold disposition (PLAN.md) updated to reflect what was built vs deferred

### What NOT to do
- Do NOT build before typed edges are proven (Item 3)
- Do NOT run full-corpus contradiction scan in the first pass; scope to query-driven first
- Do NOT auto-flag contradictions in clinical records without human review gate

---

## Item 6: MCP wrapper improvements — fill proven gaps only

### What
The genuine gap in the MCP fleet is that `tools/excluded_hybrid_search.py` (the fused
FTS5+vector+KG hybrid pipeline) is CLI-only. Wrapping it as an MCP tool gives agent skills
and Claude Desktop sessions direct access to the full hybrid stack, not just the
vector-only (docs-rag) or keyword-only (arcanum) channels. This is the only confirmed
missing tool in the fleet (B6 in EXISTING_SYSTEMS_MAP.md).

### Preconditions
- Item 0 complete (excluded_hybrid_search.py entanglement resolved)
- The fused hybrid pipeline stable and A/B'd at 92.0%

### Exact files involved
- `tools-dev/docs-rag/` — most natural home for a hybrid-search tool alongside the
  existing vector+KG tools in that server
- `tools/excluded_hybrid_search.py` — the CLI tool being wrapped (READ-ONLY; add a thin
  adapter, do not refactor the core)
- `tools-dev/docs-rag/docs_rag_server.py` — add one new tool definition

### Risks
- Entanglement: do not wrap excluded_hybrid_search.py while it still carries uncommitted
  Phase 4 HyDE lines (those must be resolved in Item 0 first)
- Do not duplicate the existing vector-search or KG tools in docs-rag; the wrapper adds
  the FUSED hybrid surface only

### Tests/evals required
- MCP tool schema validation (JSON Schema via protocol layer)
- End-to-end: call the new MCP tool from a Claude Code session; verify it returns the same
  top-5 results as the CLI for a known query
- Regression: existing docs-rag tools unaffected

### Definition of done
- New `docs_rag_hybrid_search` MCP tool committed; schema validated
- End-to-end test passing
- No duplication of existing vector/KG tools

### What NOT to do
- Do NOT build a sixth standalone MCP server for this; add to the existing docs-rag server
- Do NOT duplicate arcanum (keyword) or docs-rag (vector+KG) tools
- Do NOT wrap the HyDE path; it was killed as net-negative (ADR candidate)

---

## Item 7: AutoReason / Borda advanced agent review

### What
Advanced multi-agent review patterns (Borda voting, AutoReason deliberation) that go
beyond the current 5-round Triad review cycle. Relevant only after the eval harness
(quality_probe.py) and cost controls (Items 0–1) are stable.

### Preconditions
- **Items 0–1 complete** — eval harness must be clean and cost-controlled before adding
  more LLM-intensive review passes
- The 5-round Triad review cycle (`tools/ai_studio/review_cycle.py`) must be measured
  for baseline quality before adding a layer on top

### Exact files involved
- `tools/ai_studio/review_cycle.py` — existing 5-round cycle; measure before extending
- `tools/model_router.py` — use to route reviewer model selection
- NEW: `tools/ai_studio/borda_reviewer.py` (tentative) — Borda-count aggregation over
  parallel reviewer outputs

### Risks
- Cost multiplier: each additional reviewer adds LLM spend. Measure before committing
  to a multi-reviewer pattern
- Latency: sequential multi-round reviews already add 30–60s per query (ADR 0001);
  adding more rounds compounds this
- Quality ceiling: if the 5-round Triad already catches all real issues, adding Borda
  may add cost without adding quality. Measure first

### Tests/evals required
- Baseline: measure 5-round Triad quality on a held-out test set before adding Borda
- A/B: Borda vs 5-round Triad on same test set; report both regressions and lifts
- Cost delta: document per-query cost increase

### Definition of done
- A/B confirms net quality lift (not just a different distribution of the same errors)
- Cost delta documented and approved by Adam
- No regression on the 92.0% retrieval baseline (these are independent but the same
  eval infrastructure is used)

### What NOT to do
- Do NOT build before Items 0–1 are complete and the eval harness is stable
- Do NOT add Borda as a default-on pass; make it opt-in (`--borda` flag)

---

## Item 8: OCR / research verification improvements

### What
Two targeted improvements to the ingest and verification pipeline:
1. **Verify-before-recommend gate**: any screenshot or image-harvest recommendation
   must be verified against source documents before being implemented. Gate implemented
   as a rule in `completion-integrity.md` and `operational-discipline.md` (already added
   in session 285). This item is about harness integration, not rule-writing.
2. **OCR fidelity harness**: add a spot-check pass to `tools/extract_cache.py` that
   compares OCR'd AFSC codes and dates against known-good values, flagging misreads
   (2→Z, 0→O, date slashes→dots are known failure modes per excluded-corpus.md).

### Preconditions
- Item 0 complete (clean repo)
- A gold set of at least 20 OCR'd documents with known-good AFSC/date values (UNKNOWN:
  whether this gold set currently exists; must be confirmed before building the harness)

### Exact files involved
- `tools/extract_cache.py` — add OCR fidelity spot-check pass
- `.claude/rules/completion-integrity.md` — verify-before-recommend gate (already added)
- `.claude/rules/operational-discipline.md` — verify-before-recommend gate (already added)
- NEW: `tools/ocr_fidelity_check.py` — OCR spot-check harness (if gold set exists)

### Risks
- UNKNOWN: whether a labeled OCR gold set exists. Do not build the harness if no gold set;
  building a harness without ground truth produces an unvalidated verification step
- OCR fidelity check adds latency to the ingest pipeline; scope to post-ingest spot-check,
  not a blocking gate

### Tests/evals required
- If gold set exists: precision/recall of fidelity check on the gold set, with conservative
  judge calibration stated explicitly
- If gold set does not exist: document the gap and defer the harness build until labeled data
  is available
- Regression: existing `tools/extract_cache.py` behavior unchanged for non-OCR paths

### Definition of done
- Verify-before-recommend gate integrated into eval harness (not just documented in rules)
- OCR fidelity spot-check implemented IF gold set exists
- UNKNOWN flag resolved (gold set confirmed or gap documented)

### What NOT to do
- Do NOT build the OCR fidelity harness without a gold set
- Do NOT block the ingest pipeline with the spot-check; run it asynchronously
- Do NOT claim OCR quality improved without measuring before/after on labeled data

---

## Summary table

| Item | Name | Preconditions | Risk | Rough cost |
|------|------|---------------|------|------------|
| 0 | Consolidation / repo hygiene | None | Low | $0 |
| 1 | Cost banking (Batch API) | Item 0 done | Low-medium | $0 (dry-run) |
| 2 | Hook promotion | Item 0 done | Low (no forced reload) | $0 |
| 3 | Typed KG edges | Item 0+1 done, Adam GO | High (paid extraction) | UNKNOWN — estimate first |
| 4 | GraphRAG | Item 3 proven | Medium | UNKNOWN — estimate first |
| 5 | Contradiction engine | Item 3 proven | Medium | Scoped to query-driven |
| 6 | MCP hybrid wrapper | Item 0 done | Low | $0 |
| 7 | AutoReason / Borda | Items 0+1, baseline measured | Medium | Per-query cost delta |
| 8 | OCR/research verification | Item 0 done; gold set UNKNOWN | Low-medium | $0 if no gold set |

---

## UNKNOWN flags

- **Item 8**: whether a labeled OCR gold set exists is UNKNOWN. Confirm before building
  the OCR fidelity harness.
- **Item 3 cost**: per-chunk triple extraction cost over the full 24,640-entity / 743K-relation
  corpus is UNKNOWN until token-count estimation is done. Estimate before submitting.

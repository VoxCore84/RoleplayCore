## Goal

Add a fail-closed, cost-bounded **in-pipeline CONTRADICTS Auditor** to the citation synthesis path so that every `[grounded]` sentence is checked before delivery for whether its inline verbatim quote actually supports the claim it is attached to. The purpose is to eliminate the highest-risk legal failure mode—claims paired with verbatim quotes that directly contradict them—without regressing the existing FABRICATED:0 protection from substring verification, and without blowing the synthesis hot-path cost/latency budget.

## Context (read first)

Implementer must read these files before editing code:

1. `tools/citation_holdout_synthesizer_v2.py`
   - Read the full synthesis flow, especially:
     - answer generation
     - inline quote verification / retry loop
     - final answer return path
   - This is the primary integration point; extend it rather than rewriting.
   - Line numbers not provided; inspect the functions that:
     - call the model for synthesis
     - invoke `tools/inline_grounding.py`
     - perform verify-retry after FABRICATED-like failures

2. `tools/inline_grounding.py`
   - Read quote extraction and substring verification logic.
   - Understand current source span matching and how grounded sentences are identified.
   - The new auditor composes after this verifier, not instead of it.

3. `tools/citation_scorer.py`
   - Read:
     - `judge_span_*` functions
     - `score_span_correctness`
   - Reuse prompt structure / verdict schema where possible so offline scoring and in-pipeline auditing stay aligned.
   - This file is the reference implementation for SUPPORTS / PARTIAL / IRRELEVANT / CONTRADICTS semantics.

4. `tools/ai_studio/orchestrator.py`
   - Read lines 124–200 for the Triad Auditor pattern.
   - Read lines 160–166 specifically for fail-closed Auditor enforcement and retry behavior.
   - The new inline auditor is **not** the same orchestration layer, but should mirror its fail-closed philosophy and result handling.

5. `docs/architecture/decisions/0005-citation-precision-pipeline.md`
   - Read the v3 ADR for the citation precision pipeline.
   - Ensure the new tier fits the existing architecture and terminology.

6. `AI_Studio/Reports/citation_holdout_n35_results_20260502.md`
   - Read the failure-mode decomposition, especially the 14 CONTRADICTS examples and any notes on common patterns.

7. `.claude/commands/ex-ask.md`
   - Read Phase 2 guidance on one-quote-per-claim discipline.
   - The new auditor assumes this discipline and should reinforce it.

8. `AI_Studio/Reports/scheduled/citation_holdout_queries_v1.jsonl`
   - Held-out evaluation input set for end-to-end measurement.

9. Baseline score artifact:
   - `citation_score_holdout_n35_v2_claudejudge_20260502_113446.json`
   - Use as the measured baseline for comparison.
   - Baseline to cite in outputs: held-out n=35, judge model `claude-opus-4-7`, CONTRADICTS=14, FABRICATED=0.

## Architecture

### Decision summary

- **Triad role mapping:** This is a **specialized in-pipeline auditor**, distinct from the AI Studio Triad Auditor in `tools/ai_studio/orchestrator.py`, but modeled after its fail-closed behavior. It is not part of the Architect/Executor/Auditor workflow; it is a runtime citation safety gate inside synthesis.
- **Granularity:** **Per-claim / per-grounded-sentence**, not per-answer. This is required to localize rewrites and keep cost bounded by only auditing grounded claims.
- **Source of truth:** Auditor sees the **claim + inline quote + source chunk containing the quote**. This is the best tradeoff:
  - cheaper than full answer-wide judging over all chunks
  - more reliable than claim+quote only, because it can disambiguate quote meaning and local context
- **Model choice:** Default to **Claude Sonnet 4.6** for the in-pipeline auditor.
  - Rationale: better semantic contradiction detection than Haiku for date/negation/temporal mismatches, while still materially cheaper/faster than Opus 4.7.
  - Haiku may be exposed as an opt-in lower-cost mode, but not the default for legal-risk gating.
- **Retry strategy:** On high-confidence CONTRADICTS, request an **Executor rewrite of the specific sentence**:
  1. first preference: rewrite the claim to match the quote if supported by source
  2. second preference: replace the quote with a different supporting quote from source
  3. if neither is possible: downgrade sentence to `[synthesis]` or drop it entirely
  - Do **not** silently ship a contradicted grounded sentence.
- **Confidence threshold:** Auditor returns a confidence score. Force rewrite only for:
  - `verdict == CONTRADICTS` and `confidence >= 0.70`
  - For lower-confidence CONTRADICTS, treat as soft-fail requiring one rewrite pass; if still unresolved, hold answer with tag rather than shipping silently.
- **Fail-closed:** Any auditor execution error, malformed output, or unresolved hard contradiction causes the answer to be held and tagged `[AUDITOR_FAILED]`.

### Tier placement

Current v2 path:
1. synthesize answer
2. extract grounded claims / quotes
3. verify quote substrings in source
4. retry on fabricated / unverifiable quote
5. return answer

New v3 path:
1. synthesize answer
2. extract grounded claims / quotes
3. verify quote substrings in source
4. retry on fabricated / unverifiable quote
5. **inline contradiction audit on each grounded sentence**
6. targeted rewrite if needed
7. re-run verification on rewritten grounded sentences
8. re-run contradiction audit on rewritten grounded sentences
9. return answer only if no hard contradiction and no auditor failure

### Data flow

```text
User Query
   |
   v
[Synthesizer v2]
   |
   v
Draft answer with [grounded] sentences + inline quotes
   |
   v
[inline_grounding.py]
  - extract grounded spans
  - verify quote is verbatim in source
   |
   +--> if fabricated/unverifiable -> existing verify-retry loop
   |
   v
[Inline CONTRADICTS Auditor]
  - per grounded sentence:
    claim text
    quote text
    local source chunk
  - returns verdict/confidence/rationale
   |
   +--> if SUPPORTS -> keep
   +--> if PARTIAL/IRRELEVANT -> soft flag, keep unless strict mode
   +--> if CONTRADICTS -> targeted rewrite request
   |
   v
[Targeted rewrite pass]
   |
   v
Re-verify quote substring
   |
   v
Re-audit rewritten grounded sentence
   |
   +--> pass -> deliver
   +--> unresolved contradiction / auditor error -> hold with [AUDITOR_FAILED]
```

### Components

1. **Inline auditor module**: new reusable module for per-claim contradiction checking.
2. **Synthesizer integration layer**: extends v2 flow to call the auditor after quote verification.
3. **Targeted rewrite prompt path**: asks the synthesis model to repair only flagged grounded sentences.
4. **Result metadata emitter**: records auditor model, verdict counts, and hold reasons in output JSON/sidecar.
5. **CLI controls**: enable/disable auditor, choose model, set thresholds, strictness, and retry count.

## Interface

### Public API

Create a new module:

#### `tools/inline_auditor.py`

```python
from dataclasses import dataclass
from typing import Literal, Optional, Sequence

Verdict = Literal["SUPPORTS", "PARTIAL", "IRRELEVANT", "CONTRADICTS"]
Disposition = Literal["keep", "soft_flag", "rewrite", "hold"]

@dataclass
class GroundedSentence:
    sentence_id: str
    sentence_text: str
    claim_text: str
    quote_text: str
    source_doc_id: str
    source_chunk_id: str
    source_chunk_text: str
    quote_start: Optional[int]
    quote_end: Optional[int]

@dataclass
class AuditResult:
    sentence_id: str
    verdict: Verdict
    confidence: float
    rationale: str
    disposition: Disposition
    auditor_model: str
    auditor_prompt_version: str

@dataclass
class AuditBatchResult:
    results: list[AuditResult]
    hard_fail: bool
    hard_fail_reason: Optional[str]
    supports_count: int
    partial_count: int
    irrelevant_count: int
    contradicts_count: int
    auditor_model: str
    auditor_prompt_version: str
```

Required functions:

```python
def audit_grounded_sentence(
    grounded: GroundedSentence,
    *,
    model: str = "claude-sonnet-4-6",
    temperature: float = 0.0,
    contradiction_threshold: float = 0.70,
) -> AuditResult:
    ...
```

```python
def audit_grounded_sentences(
    grounded_sentences: Sequence[GroundedSentence],
    *,
    model: str = "claude-sonnet-4-6",
    temperature: float = 0.0,
    contradiction_threshold: float = 0.70,
) -> AuditBatchResult:
    ...
```

```python
def decide_disposition(
    verdict: Verdict,
    confidence: float,
    *,
    contradiction_threshold: float = 0.70,
    strict_partial: bool = False,
) -> Disposition:
    ...
```

```python
def build_grounded_sentence_records(
    answer_text: str,
    verification_result: object,
    source_chunks_by_id: dict[str, str],
) -> list[GroundedSentence]:
    ...
```

```python
def format_auditor_hold_tag(
    reason: str,
    *,
    auditor_model: str,
) -> str:
    ...
```

### Synthesizer integration API

Extend `tools/citation_holdout_synthesizer_v2.py` with functions like:

```python
def run_inline_auditor(
    answer_text: str,
    verification_result: object,
    source_chunks_by_id: dict[str, str],
    *,
    auditor_enabled: bool,
    auditor_model: str,
    contradiction_threshold: float,
    strict_partial: bool,
) -> AuditBatchResult | None:
    ...
```

```python
def rewrite_flagged_grounded_sentences(
    answer_text: str,
    audit_result: AuditBatchResult,
    source_chunks_by_id: dict[str, str],
    *,
    max_rewrites: int = 1,
) -> str:
    ...
```

```python
def finalize_answer_with_auditor(
    answer_text: str,
    audit_result: AuditBatchResult | None,
    *,
    fail_closed: bool = True,
) -> str:
    ...
```

Exact names may vary, but the above responsibilities must exist.

### CLI surface

Extend the synthesizer CLI, preferably in-place in `tools/citation_holdout_synthesizer_v2.py`. If a wrapper `v3` file is created, it should delegate to v2 internals and not fork logic.

Required flags:

```text
--inline-auditor
    Enable in-pipeline contradiction auditing. Default: off for backward compatibility.

--inline-auditor-model {claude-sonnet-4-6,claude-haiku-4-5}
    Default: claude-sonnet-4-6

--inline-auditor-threshold FLOAT
    Confidence threshold for hard CONTRADICTS rewrite/hold. Default: 0.70

--inline-auditor-max-rewrites INT
    Max targeted rewrite passes after contradiction audit. Default: 1

--inline-auditor-strict-partial
    If set, PARTIAL and IRRELEVANT also force rewrite. Default: false

--inline-auditor-fail-closed / --no-inline-auditor-fail-closed
    Default: fail-closed true

--emit-auditor-metadata
    Include auditor metadata in output JSON / sidecar. Default: true when inline auditor enabled.
```

Optional but recommended:

```text
--inline-auditor-batch
    Audit all grounded sentences in one model call per answer when possible. Default: true

--inline-auditor-max-sentences INT
    Safety cap on grounded sentences audited per answer. Default: 12
```

### Output / metadata format

When auditor is enabled, output must include metadata specifying the auditor model used, to satisfy methodology requirements.

If the synthesizer already emits JSON, add:

```json
{
  "inline_auditor": {
    "enabled": true,
    "model": "claude-sonnet-4-6",
    "prompt_version": "inline_auditor_v1",
    "threshold": 0.7,
    "supports": 2,
    "partial": 1,
    "irrelevant": 0,
    "contradicts": 0,
    "hard_fail": false,
    "results": [
      {
        "sentence_id": "s1",
        "verdict": "SUPPORTS",
        "confidence": 0.94,
        "disposition": "keep"
      }
    ]
  }
}
```

If the answer is held due to auditor failure, prepend or append a visible tag:

```text
[AUDITOR_FAILED model=claude-sonnet-4-6 reason="inline auditor error"]
```

or

```text
[AUDITOR_FAILED model=claude-sonnet-4-6 reason="unresolved CONTRADICTS after rewrite"]
```

Do not return an untagged answer in these cases.

## Implementation plan

1. **Create `tools/inline_auditor.py`**
   - Add dataclasses for grounded sentence records and audit results.
   - Add verdict/disposition logic.
   - Add prompt builder and response parser.
   - Add single-item and batch audit functions.
   - Add fail-closed parsing behavior for malformed model output.

2. **Port / align verdict semantics from `tools/citation_scorer.py`**
   - Reuse the same four verdict labels: SUPPORTS, PARTIAL, IRRELEVANT, CONTRADICTS.
   - Mirror scorer definitions as closely as possible.
   - Add a prompt version constant, e.g. `inline_auditor_v1`.

3. **Add deterministic non-LLM helper logic in `tools/inline_auditor.py`**
   - Implement pure functions for:
     - disposition decision
     - confidence threshold handling
     - hold-tag formatting
     - grounded sentence record construction from verifier output
   - These functions support offline deterministic tests without API spend.

4. **Extend `tools/citation_holdout_synthesizer_v2.py` CLI**
   - Add the new `--inline-auditor*` flags.
   - Keep default behavior unchanged when `--inline-auditor` is absent.

5. **Integrate auditor after existing quote verification**
   - In the current verify-retry flow, insert the auditor only after quote substring verification succeeds.
   - Do not duplicate fabricated checking.
   - Build `GroundedSentence` records from the verified grounded spans and source chunk context.

6. **Implement targeted rewrite path in `tools/citation_holdout_synthesizer_v2.py`**
   - For each sentence with disposition `rewrite`, ask the synthesis model to repair only those sentences.
   - Prompt requirements:
     - preserve answer structure where possible
     - for each flagged sentence, either:
       - rewrite claim to match quote and source
       - replace quote with a supporting quote from source
       - or convert to `[synthesis]` / remove if unsupported
     - never keep a `[grounded]` sentence whose quote contradicts the claim
   - Limit to `--inline-auditor-max-rewrites` passes, default 1.

7. **Re-run verification and auditor on rewritten grounded sentences**
   - After rewrite, run existing `inline_grounding` verification again.
   - Then re-run inline auditor on the rewritten grounded sentences.
   - If any high-confidence CONTRADICTS remains, hold answer with `[AUDITOR_FAILED]`.

8. **Add metadata emission**
   - Include auditor model, prompt version, verdict counts, and hard-fail status in output artifacts.
   - Ensure every measured output clearly states the auditor model used.

9. **Add deterministic tests**
   - Create `tests/test_inline_auditor_logic.py`
   - Cover:
     - disposition threshold behavior
     - malformed parser output -> hard fail
     - hold-tag formatting
     - grounded sentence record construction from a fixed verifier fixture

10. **Add LLM integration tests with fixtures**
    - Create `tests/test_inline_auditor_integration.py`
    - Use mocked model responses to simulate:
      - SUPPORTS
      - high-confidence CONTRADICTS -> rewrite
      - auditor malformed output -> fail-closed hold

11. **Add end-to-end measurement script support**
    - If needed, add a thin wrapper `tools/citation_holdout_synthesizer_v3.py` that calls v2 with `--inline-auditor` defaults.
    - Preferred: keep v2 as the implementation and make v3 a compatibility entrypoint only.

12. **Update ADR / docs**
    - Add a short addendum to `docs/architecture/decisions/0005-citation-precision-pipeline.md` documenting Tier 2 inline contradiction auditing, model default, fail-closed behavior, and measurement expectations.

## Error handling

### Auditor model call fails
- Cause: network/API error, timeout, auth issue, rate limit.
- Handling:
  - If `--inline-auditor-fail-closed` true: hold answer and tag `[AUDITOR_FAILED ...]`.
  - Do not ship silently.
  - Record `hard_fail=true` and reason.
- No automatic fallback to “ship anyway”.

### Auditor returns malformed JSON / unparsable schema
- Cause: model drift, prompt noncompliance.
- Handling:
  - Treat as auditor failure.
  - Hold answer with `[AUDITOR_FAILED model=... reason="malformed auditor output"]`.

### Grounded sentence missing quote/source mapping after verification
- Cause: parser mismatch between synthesizer and verifier outputs.
- Handling:
  - Treat that sentence as hard-fail for auditing if it is still marked `[grounded]`.
  - Hold answer with `[AUDITOR_FAILED ... reason="grounded sentence missing source mapping"]`.

### CONTRADICTS with confidence >= threshold
- Handling:
  - Force targeted rewrite.
  - Re-run verifier and auditor.
  - If still CONTRADICTS after max rewrites: hold answer with `[AUDITOR_FAILED ... reason="unresolved CONTRADICTS after rewrite"]`.

### CONTRADICTS with confidence < threshold
- Handling:
  - Still perform one rewrite attempt by default, because legal risk is high.
  - If unresolved after rewrite:
    - if fail-closed true: hold
    - otherwise soft-flag in metadata only
- Recommended default remains fail-closed true.

### PARTIAL / IRRELEVANT
- Handling:
  - Default disposition `soft_flag`.
  - Keep answer unless `--inline-auditor-strict-partial` is set.
  - Include counts in metadata for later measurement.

### Rewrite introduces FABRICATED quote
- Handling:
  - Existing `inline_grounding` verifier catches it.
  - Use existing verify-retry logic first.
  - If unresolved after allowed retries, hold answer; do not bypass verifier because rewrite came from contradiction repair.

### No grounded sentences in answer
- Handling:
  - Auditor is a no-op.
  - Emit metadata with zero counts if enabled.

### Too many grounded sentences
- Cause: pathological answer size.
- Handling:
  - Audit up to `--inline-auditor-max-sentences` and then:
    - either hard-fail hold, or
    - require synthesis to shorten answer
  - Recommended default: hard-fail hold with reason `"grounded sentence count exceeds auditor cap"` to avoid partial unchecked delivery.

## Test plan

### 1. Deterministic offline test required before any API spend

Create `tests/test_inline_auditor_logic.py` with no model calls.

Minimum cases:

1. **Disposition threshold**
   - Input: `verdict="CONTRADICTS", confidence=0.85, threshold=0.70`
   - Expect: `rewrite`
   - Input: `verdict="SUPPORTS", confidence=0.90`
   - Expect: `keep`
   - Input: `verdict="PARTIAL", confidence=0.80, strict_partial=False`
   - Expect: `soft_flag`

2. **Malformed output handling**
   - Feed parser invalid JSON / missing fields.
   - Expect batch result `hard_fail=True`.

3. **Hold tag formatting**
   - Input reason/model.
   - Expect exact `[AUDITOR_FAILED model=... reason="..."]` format.

4. **Grounded sentence record construction**
   - Use a fixed verifier fixture representing one grounded sentence with quote offsets and source chunk.
   - Assert deterministic extraction of `claim_text`, `quote_text`, `source_chunk_id`.

This test suite must run fully offline and deterministically.

### 2. Mocked integration test

Create `tests/test_inline_auditor_integration.py`.

Use monkeypatch/mocks for model responses.

Cases:

1. **SUPPORTS path**
   - Verified grounded sentence audited as SUPPORTS.
   - Expect no rewrite, answer delivered.

2. **High-confidence CONTRADICTS path**
   - First audit returns CONTRADICTS 0.92.
   - Rewrite function returns repaired answer.
   - Re-verify + re-audit returns SUPPORTS.
   - Expect final answer delivered, metadata shows one contradiction resolved.

3. **Auditor failure path**
   - Auditor raises exception.
   - Expect final answer tagged `[AUDITOR_FAILED ...]`.

4. **Unresolved contradiction path**
   - Audit returns CONTRADICTS before and after rewrite.
   - Expect hold with `[AUDITOR_FAILED ... reason="unresolved CONTRADICTS after rewrite"]`.

### 3. Focused live test on known contradiction example

Before full held-out run, execute a single known failure case from Q9:

- Claim: `"The NPDB Subject Statement was filed on March 15."`
- Quote: `"added to report 03/16/2026, forwarded to DHA. Now visible on all queries."`

Expected:
- Auditor verdict: `CONTRADICTS`
- Confidence: >= 0.70
- Disposition: `rewrite`

This can be a manual smoke test if no fixture harness exists.

### 4. End-to-end held-out measurement

Run:

```bash
python tools/citation_holdout_synthesizer_v3.py \
  --input AI_Studio/Reports/scheduled/citation_holdout_queries_v1.jsonl \
  --inline-auditor \
  --inline-auditor-model claude-sonnet-4-6
```

Then score with:

```bash
python tools/citation_scorer.py \
  --judge claude \
  --judge-model claude-opus-4-7 \
  ...
```

Compare against measured baseline artifact:

- `citation_score_holdout_n35_v2_claudejudge_20260502_113446.json`

Expected measured outcome target:
- Held-out set: `n=35`
- Judge model for measurement: `claude-opus-4-7`
- CONTRADICTS: **14 → <= 2**
- FABRICATED: remains **0**
- Any reported quality numbers must explicitly name the judge model `claude-opus-4-7`

Secondary metrics to inspect:
- SUPPORTS should not collapse materially due to over-dropping grounded claims
- PARTIAL / IRRELEVANT may shift modestly
- Count of `[AUDITOR_FAILED]` holds should be reported separately

### 5. Cost / latency validation

On a representative subset and then full n=35:
- Compare synthesis-only cost/latency against v2 baseline:
  - baseline synthesis-only cost: `$0.153/query`
  - baseline p50: `6.1s`
  - baseline p95: `12.3s`

Expected addition from inline auditor:
- cost: `<= +$0.10/query`
- p50 latency: `<= +5s`

If exceeded, trigger fallback plan in Rollout.

## Cost / latency budget

### Default operating assumption

- Average grounded sentences per answer: likely low single digits under one-quote-per-claim discipline.
- One batch audit call per answer is preferred over one call per sentence when possible.
- One targeted rewrite pass max by default.

### Model choice justification

**Default: Claude Sonnet 4.6**
- Better contradiction detection reliability than Haiku for legal/date/negation mismatches.
- Lower cost and latency than Opus 4.7.
- Appropriate for hot-path semantic auditing.

**Not default: Claude Haiku 4.5**
- Acceptable as an opt-in budget mode, but too risky as default for the highest-severity failure mode.

**Forbidden: Claude Opus 4.7**
- Violates cost ceiling for per-claim hot-path judging.

### Budget target

Relative to v2 synthesis-only baseline:
- baseline: `$0.153/query`, p50 `6.1s`, p95 `12.3s`

Target with inline auditor enabled:
- added cost: `+$0.04` to `+$0.10/query`
- added p50 latency: `+1.5s` to `+5s`
- added p95 latency: ideally `< +7s`

Implementation tactics to stay within budget:
1. Audit only `[grounded]` sentences.
2. Batch all grounded sentences for an answer into one auditor call when possible.
3. Use local source chunk only, not all source chunks.
4. Limit rewrite passes to 1 by default.
5. Skip auditor entirely when no grounded sentences exist.

## Triad notes

### What the Auditor (Gemini) should specifically verify before approving

1. **Fail-closed is explicit**
   - Any auditor error, malformed output, or unresolved contradiction must hold the answer with `[AUDITOR_FAILED]`.
   - No silent fail-open path exists.

2. **Opus is not mandated for in-pipeline judging**
   - Default model must be Sonnet 4.6 or cheaper/faster equivalent.
   - Opus reserved for synthesis/offline scoring, not hot-path auditing.

3. **Integration composes with v2 verify-retry**
   - Auditor runs after existing substring verification.
   - Rewrite path reuses verifier on rewritten output.
   - No duplicate or conflicting fabricated-check logic.

4. **Deterministic offline test exists**
   - At least one no-API deterministic test is specified and implementable.

5. **Methodology rule is respected**
   - Every reported quality number names the judge model.
   - Held-out n=35 is used for evaluation, not tuning-only examples.
   - Baseline comparisons are against measured artifacts, not inferred numbers.

6. **Acceptance target is measurable**
   - CONTRADICTS reduction target is explicit: 14 → <=2 on held-out n=35, judged by `claude-opus-4-7`.
   - FABRICATED remains 0.

### What the Auditor should refuse to approve

1. Any design that requires **Opus 4.7** as the in-pipeline contradiction judge.
2. Any design that **fails open** or allows contradicted grounded sentences to ship untagged.
3. Any design that does not specify **where the auditor sits relative to the existing v2 verify-retry loop**.
4. Any design that lacks a **deterministic offline test**.
5. Any design that audits only the whole answer without sentence-level localization, unless it still specifies exact rewrite localization and cost bounds.
6. Any design that omits **auditor model metadata** from outputs.

## Rollout

### Phase 1: dark-launch / measurement mode
- Ship code behind `--inline-auditor`.
- Default off to preserve current measurements and workflows.
- When enabled, emit metadata and hold tags.
- Run on held-out n=35 and compare to baseline artifact.

### Phase 2: guarded opt-in
- Enable for internal legal-evidence runs only.
- Monitor:
  - CONTRADICTS count
  - FABRICATED count
  - hold rate
  - added cost/query
  - added latency

### Phase 3: default-on if targets met
Make default-on only if all are true on held-out measurement:
- CONTRADICTS <= 2
- FABRICATED remains 0
- added synthesis cost <= +$0.10/query
- added p50 latency <= +5s
- hold rate acceptable for operator workflow

### Fallback path

If any of the following occur:
- CONTRADICTS does not materially drop
- FABRICATED regresses above 0
- cost exceeds +$0.10/query
- p50 latency exceeds +5s
- hold rate is operationally too high

Then:
1. Keep the module, but disable hot-path enforcement by default.
2. Move the auditor into an **offline scoring / pre-delivery review mode** only.
3. Preserve metadata emission and measurement hooks.
4. Optionally switch default auditor model from Sonnet to Haiku only for experimentation, but do not silently change legal-risk defaults without re-measurement.

## Open questions

1. **Exact verifier output schema**
   - The spec assumes `inline_grounding.py` exposes enough structure to map each grounded sentence to quote text and source chunk.
   - If not, implementer must add a minimal structured return type there.

2. **Whether v2 already has sentence IDs**
   - If not, implementer should generate stable per-answer IDs like `s1`, `s2`, etc.

3. **Batch vs single-call auditor prompt**
   - Preferred is one batch call per answer for cost efficiency.
   - If prompt reliability is poor in batch mode, implementer may switch to per-sentence calls with a cap, but must re-check budget.

4. **Low-confidence CONTRADICTS policy**
   - Spec recommends one rewrite attempt even below threshold due to legal risk.
   - Implementer may simplify to “all CONTRADICTS force rewrite” if this is easier and still within budget.

5. **Whether rewrite should downgrade to `[synthesis]` or delete**
   - Preferred order is:
     1. repair grounded claim
     2. replace quote
     3. downgrade to `[synthesis]`
     4. drop sentence
   - Implementer can choose exact fallback wording.

6. **Whether to create `citation_holdout_synthesizer_v3.py`**
   - Preferred only as a thin wrapper / alias to preserve v2 internals.
   - Avoid code fork.

7. **Prompt wording reuse from scorer**
   - Best effort should be made to align with `citation_scorer.py`, but exact prompt text may need adaptation for runtime brevity and JSON reliability.
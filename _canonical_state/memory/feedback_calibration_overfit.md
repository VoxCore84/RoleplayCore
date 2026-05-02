---
name: Calibration overfit and judge calibration in AI quality measurement
description: Always use held-out test sets and always state the judge model when reporting AI quality numbers. Calibration-batch numbers can be 30+ percentage points more optimistic than held-out.
type: feedback
originSessionId: 72dee022-30ea-464f-b3c8-c821121ea838
---
When measuring AI system quality (hallucination rate, span correctness, citation precision, retrieval quality, etc.):

**Rule 1: The test set must be HELD OUT from pipeline development.**
Measuring on the same N queries you developed against produces overfit numbers. On 2026-05-02, the citation_scorer pipeline scored **0.0% hallucination on its 15-query calibration batch but 30.0% on 35 fresh held-out queries — a 30pp gap that hid in plain sight**. Calibration numbers prove the pipeline *can* hit a level on its training data; they don't predict production behavior.

**Rule 2: Every published quality number MUST specify the judge model.**
Same answers, Gemma 4 26B judge → 45.5% hallucination. Claude Opus 4.7 judge → 30.3%. The Gemma → Claude swap alone explained 15pp of the original published number's "improvement." Different judges have different calibration; comparisons across runs with different judges are meaningless.

**Rule 3: Roadmap predictions calibrated against an inflated baseline are themselves inflated.**
The original "step 1 → ~10% hallucination" prediction was based on the 45% Gemma-baseline. After Claude judge correction the baseline was already 30%, and step 1's true held-out effect was ~0pp. Predict against measured baselines, not assumed ones.

**Why:** A 30pp methodology error in production rate measurement isn't theoretical risk — it changes the public/diligence claim from "industry-leading <2% hallucination" to "30% hallucination" overnight. For acquihire/diligence-grade work this is the difference between a defensible pitch and a fraud claim.

**How to apply:**
- When writing or reviewing any AI-quality measurement: ask "is this test set held-out from pipeline development?"
- When publishing any rate: state the judge model and the test-set provenance.
- When predicting an improvement: cite the measured-not-assumed baseline.
- When the calibration result looks suspiciously good (e.g. 0%): immediately suspect overfit; demand a held-out replication before celebrating.

**Source:** Session 2026-05-02 citation precision pipeline work. Reports: `AI_Studio/Reports/citation_step1_results_20260502.md`, `AI_Studio/Reports/citation_holdout_n35_results_20260502.md`. ADR: `docs/architecture/decisions/0005-citation-precision-pipeline.md`.

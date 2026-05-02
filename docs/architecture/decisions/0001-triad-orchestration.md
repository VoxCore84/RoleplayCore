# ADR 0001: Triad Orchestration with Epistemic Isolation

**Status:** Accepted
**Date:** 2026-04-30
**Deciders:** Adam Taylor

## Context

Single-model RAG systems share a known failure mode: the model that drafts an answer is the same model that's asked to verify it. Self-confirmation is structural — the verifier inherits whatever bias the drafter brought, and the only signals it has access to are the ones the drafter selected. The audit pass rubber-stamps the draft.

VoxCore needs an answer-grade architecture for legal evidence: every claim cited, every citation verified, every output reproducible. Single-model RAG can't deliver that.

## Decision

Three-role orchestration with cross-provider isolation:

- **Architect** (Gemini, `gemini-3.1-pro`) — plan decomposition, sub-question generation, budget setting. Produces a structured plan but never calls tools.
- **Executor** (Claude, `claude-opus-4-7`) — runs the plan, calls tools (MCP), drafts the answer with inline citations.
- **Auditor** (Gemini, separate invocation with different system prompt) — sees the draft + retrieved evidence but **does NOT see the Architect's plan**. Verifies citations, flags unsupported claims, can force a rerun.
- **Local GPU tier** (RTX 5090 via Ollama) — embeddings (BGE-M3), reranking (BGE-reranker-v2-m3), OCR (Tesseract), ASR (Whisper-large-v3). Runs anything that touches privilege-sensitive content or that scales to electricity-cost regimes.

Routing entry point: `tools/ai_studio/orchestrator.py:168` `TriadOrchestrator.orchestrate()`. Up to 3 retry iterations on Auditor reject. Fail-closed by default — ambiguous Auditor output blocks ship.

A larger 5-Round Review Cycle (`tools/ai_studio/review_cycle.py`) runs for non-trivial reviews: Phase 1 parallel (Codex + Gemini + Claude), Phase 2 Codex verifies fixes, Phase 3 Gemini final-seals.

## Alternatives considered

1. **Single-model orchestration (Claude or GPT or Gemini alone).** Cheapest, simplest. Rejected: the self-confirmation failure mode is the central reason flat-RAG hallucination rates stay at 15–18%. The whole point of the Triad is to break that loop.

2. **Two-role orchestration (drafter + verifier, both Claude).** Rejected: same provider, same training distribution, same blind spots. Cross-provider independence is what makes the Auditor credible; using a different Claude model isn't enough.

3. **Voting ensemble (3 drafters, majority wins).** Rejected: doesn't address the audit problem, just averages out random errors. Systematic biases compound rather than cancel.

4. **Constitutional AI / self-critique (drafter critiques itself).** Rejected: research-tier today (Anthropic published the technique) but doesn't survive the "does the model that drafted the bad answer recognize the bad answer" test in legal-AI conditions.

## Consequences

**Positive:**
- The Auditor can refuse to ship outputs the Executor drafted. Loop only emits when Auditor passes.
- Cost predictable: 3 LLM invocations per query (~$0.05–0.15 per complex query at current pricing).
- Privilege boundary structurally simpler — local-GPU tier handles any retrieval/embedding/OCR that touches sensitive content; cloud tier only sees the Architect's plan and the abstracted query.

**Negative:**
- Latency: 3 sequential LLM calls add up. Median complex query is ~30–60s vs 5–10s for single-model.
- Cost: 3x higher than single-model on a per-query basis.
- Coordination complexity: prompt-version drift across roles is a real risk. Mitigated by version-controlling prompts in git (Cat 1 follow-on item).

**Neutral:**
- Architect and Auditor sharing a provider (Gemini) in `orchestrator.py` is a simplification — the 5-round cycle uses true cross-provider for non-trivial work.
- Model identifiers: Architect/Auditor via `ORCHESTRATOR_GEMINI_MODEL` env var; Executor hardcoded to `claude-opus-4-7` (hardening: lift to env var for parity).

## References

- `docs/architecture/TRIAD_ENTRY_POINT.md` — function-by-function map
- `tools/ai_studio/orchestrator.py:168` `orchestrate()`
- `tools/ai_studio/review_cycle.py` — 5-round version

# ADR 0003: Local-GPU Offload for Privilege-Sensitive Operations

**Status:** Accepted
**Date:** 2026-04 (formalized; pattern was implicit from project start)

## Context

Most legal-AI products are fully cloud (raw documents go to Anthropic/OpenAI/Google) or fully on-prem (capability and cost penalty). Neither is a clean fit for the legal-AI workload.

Two pressures:

1. **Privilege.** Sending raw privileged content to commodity cloud LLM endpoints is hard to justify to a firm's GC. Even with vendor BAAs and "no training" guarantees, the privilege analysis is murky — and most firms' answer is "send less."
2. **Cost.** Embedding 100K chunks and reranking on every query at cloud-API rates ($0.02–$0.13 per 1K tokens) makes the per-query cost prohibitive at scale. Heavy throughput operations need to be off the metered cloud path.

VoxCore's primary dev machine has a 32GB RTX 5090 — substantial VRAM headroom for embedding models, rerankers, OCR, and ASR.

## Decision

Route all the operations below to local GPU via Ollama:

- **Embeddings**: BGE-M3 (1024 dim) — text chunk vectors for the ChromaDB index
- **Reranking**: BGE-reranker-v2-m3 — second-stage cross-encoder
- **OCR**: Tesseract 5.4 on pypdfium2-rendered images — scanned PDFs
- **ASR**: Whisper-large-v3 via faster-whisper (CUDA backend) — audio depositions
- **Light classification / triage**: Gemma 4 26B and Qwen 3.5 27B — judge wrapper for citation_scorer + legalbench harness

Cloud APIs (Anthropic / OpenAI / Google) remain for:
- Triad role calls (Architect/Executor/Auditor)
- High-stakes synthesis where frontier reasoning quality justifies the cost

## Alternatives considered

1. **Fully cloud.** Cheapest for the developer (no GPU spend), but the privilege story doesn't hold up and per-query cost compounds.

2. **Fully on-prem.** Requires either local frontier-tier models (Llama 3.3 70B+ for the Triad roles) or accepting much weaker results. Frontier-tier local inference at acceptable latency requires multi-GPU setups VoxCore doesn't have.

3. **Cloud-only with redaction layer.** Strip PII / PHI / privileged markers before sending to cloud; cloud sees only abstracted content. Rejected because (a) the redaction layer is itself a model we'd have to trust and validate, and (b) the abstracted content loses the signals that make retrieval work.

4. **Confidential computing (Azure Confidential VMs, AWS Nitro Enclaves).** Strong privilege story but ~3x cost and limited model availability. Acceptable as a future deployment option; not the primary path.

## Consequences

**Positive:**
- Heavy-throughput operations cost electricity, not API spend. Embedding the full corpus is ~$0; doing it on cloud APIs would be hundreds of dollars per refresh.
- Privilege boundary defensible: when the user runs a privilege-sensitive query, all retrieval and reranking happen locally; only the abstracted query and pre-redacted excerpts go to the cloud Triad.
- Per-query latency: local rerank ~200ms vs Cohere/Jina API ~500–1000ms.

**Negative:**
- Privilege boundary is currently a **cost optimization**, not **structural enforcement**. Cloud APIs *can* see raw content if a developer wires them that way. Documented honestly: structural enforcement is a roadmap item.
- Local model quality lags frontier by ~6–12 months. We use local for triage / embedding / OCR / ASR (where quality is acceptable) but route reasoning to cloud frontier models.
- Hardware dependency: any developer running VoxCore needs ≥24GB VRAM. Documented in `docs/ENVIRONMENT.md`.

## References

- `docs/ENVIRONMENT.md` — current Ollama model inventory
- ADR 0004 — governance gate routes documents based partly on local-GPU availability
- ADR 0005 — citation scorer's LLM-as-judge defaults to local Ollama

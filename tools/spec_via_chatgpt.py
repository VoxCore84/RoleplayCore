#!/usr/bin/env python3
"""Generate an architecture spec via ChatGPT (Triad Architect role).

Reuses the OpenAI key + model env config that chatgpt_bridge.py uses.
Writes the spec to AI_Studio/2_Active_Specs/<slug>_<ts>.md.

Usage:
    python tools/spec_via_chatgpt.py --slug contradicts_auditor --prompt-file SPEC_REQUEST.md
    python tools/spec_via_chatgpt.py --slug X --prompt "Inline prompt text"
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ACTIVE_SPECS = REPO_ROOT / "AI_Studio" / "2_Active_Specs"

SYSTEM = """You are the Lead Architect in the VoxCore Triad workflow.

The user (Adam, solo developer) is building a citation-precision pipeline for high-stakes legal evidence work. The system is single-machine local-only software. Your job is to produce a markdown SPEC for the requested feature: enough detail that the Executor (Claude Opus 4.7) can implement it correctly without re-asking design questions, but no actual code.

Required spec structure:

## Goal
One-paragraph what + why.

## Context (read first)
File paths the implementer must read before writing code. Cite line numbers if known.

## Architecture
Components, data flow, ASCII diagram if helpful, decision points.

## Interface
- Public API: function signatures, CLI flags, file/JSON formats
- Inputs / outputs

## Implementation plan
Numbered steps the Executor follows. Each step is a discrete file edit or new file.

## Error handling
Specific failure modes and how each is handled.

## Test plan
How the Executor verifies the implementation works. Include at least one offline deterministic test and one end-to-end test against the held-out batch.

## Cost / latency budget
Estimated per-query cost and latency impact.

## Triad notes
What the Auditor (Gemini) should specifically verify before approving. What the Auditor should refuse to approve.

## Rollout
How to ship without breaking existing measurements. Include a fallback path.

## Open questions
Anything you're NOT certain about. The implementer can pick a default but flag here.

VoxCore-specific facts:
- Triad: Architect=Gemini, Executor=Claude Opus 4.7, Auditor=Gemini. Fail-closed Auditor enforced in `tools/ai_studio/orchestrator.py:160-166`. Up to 3 retries on Auditor reject.
- Citation pipeline: `tools/citation_scorer.py` (scoring + LLM-as-judge), `tools/inline_grounding.py` (verbatim-quote substring verifier), `.claude/commands/ex-ask.md` Phase 2 (one-quote-per-claim discipline). v3 ADR `docs/architecture/decisions/0005-citation-precision-pipeline.md`.
- Held-out hallucination measurement (n=35, claude-opus-4-7 judge): 30.0% v1 → 24.7% v2 (verify-retry shipped 2026-05-02). Verdict distribution: SUPPORTS 75 / PARTIAL 121 / IRRELEVANT 147 / CONTRADICTS 14 / FABRICATED 0.
- Methodology rule (encoded in memory `feedback_calibration_overfit.md`): all quality numbers must specify the judge model; test sets must be held out from pipeline development; predict against measured baselines not inferred ones.

Output the spec markdown ONLY. No preamble, no explanation outside the spec."""


def get_openai_client():
    sys.path.insert(0, str(REPO_ROOT / "tools" / "ai_studio"))
    # Reuse chatgpt_bridge's env loading
    from dotenv import load_dotenv
    load_dotenv(REPO_ROOT / "tools" / "ai_studio" / ".env")
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key or api_key == "YOUR_KEY_HERE":
        print("ERROR: OPENAI_API_KEY missing", file=sys.stderr)
        sys.exit(1)
    from openai import OpenAI
    return OpenAI(api_key=api_key)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--prompt", default=None)
    p.add_argument("--prompt-file", default=None)
    p.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-5.4"))
    p.add_argument("--out-dir", default=str(ACTIVE_SPECS))
    args = p.parse_args()

    if args.prompt is None and args.prompt_file is None:
        print("ERROR: --prompt or --prompt-file required", file=sys.stderr)
        sys.exit(1)
    user_prompt = args.prompt
    if args.prompt_file:
        user_prompt = Path(args.prompt_file).read_text(encoding="utf-8")

    client = get_openai_client()
    print(f"Calling ChatGPT ({args.model}) for spec '{args.slug}'...")
    t0 = time.time()
    try:
        resp = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )
    except Exception as e:
        print(f"ERROR: API call failed: {e}", file=sys.stderr)
        sys.exit(1)
    dt = time.time() - t0

    spec_text = resp.choices[0].message.content or ""
    usage = resp.usage
    in_tok = getattr(usage, "prompt_tokens", 0)
    out_tok = getattr(usage, "completion_tokens", 0)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    out_path = out_dir / f"{args.slug}_{ts}.md"
    out_path.write_text(spec_text, encoding="utf-8")

    print(f"  {dt:.1f}s in={in_tok} out={out_tok}")
    print(f"  Wrote {out_path} ({len(spec_text)} chars)")


if __name__ == "__main__":
    main()

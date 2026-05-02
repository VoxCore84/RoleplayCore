#!/usr/bin/env python3
"""In-pipeline CONTRADICTS Auditor (MVP per spec contradicts_auditor_v1).

Runs after the v2/v3 synthesizer's FABRICATED verify-retry loop, judging each
[grounded] sentence's (claim, inline quote) pair against the source-chunk
context the quote came from. Returns SUPPORTS / PARTIAL / IRRELEVANT /
CONTRADICTS with a confidence score (0.0-1.0) and a one-line rationale.

The synthesizer integrates this by:
  1. Running v2 verify-retry first (FABRICATED -> 0)
  2. Calling audit_answer(answer, original_chunks, model="claude-sonnet-4-6")
  3. For each CONTRADICTS verdict with confidence >= threshold: triggering a
     targeted rewrite of just that sentence
  4. Re-verifying the rewritten sentence (substring) and re-auditing it
  5. If unresolved after one rewrite: HOLD the answer with [AUDITOR_FAILED] tag

Default judge: claude-sonnet-4-6. Per the spec, Sonnet has materially better
date/negation/temporal contradiction detection than Haiku at materially less
cost than Opus 4.7. The Auditor is on the synthesis hot path; cost matters.

Public API:
    audit_answer(answer, chunks, model=...) -> dict with per-claim verdicts
    targeted_rewrite_request(claim, quote, source, verdict, ...) -> str

CLI:
    python tools/inline_auditor.py --answer-file answer.txt --chunks-file chunks.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))
from inline_grounding import extract_inline_quotes  # noqa: E402

DEFAULT_AUDITOR_MODEL = "claude-sonnet-4-6"
AUDITOR_PROMPT_VERSION = "v1.0-2026-05-02"


def load_env_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if key:
        return key
    env_path = REPO_ROOT / "tools" / "ai_studio" / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY"):
                return line.partition("=")[2].strip().strip('"').strip("'")
    return ""


AUDITOR_SYSTEM = """You are an in-pipeline CONTRADICTS Auditor for a legal-evidence citation system. You read a CLAIM (a single factual sentence from an answer), the INLINE QUOTE the answer paired with that claim, and the SOURCE CHUNK the quote came from. You return a verdict on whether the quote actually supports the claim.

VERDICTS:
- SUPPORTS: the quote's text directly contains and confirms the specific fact the claim asserts (date, name, amount, status, finding).
- PARTIAL: the quote is on-topic and partially supports the claim, but does not contain the specific fact.
- IRRELEVANT: the quote is in the source but does not address the subject of the claim.
- CONTRADICTS: the quote actively contradicts the claim (different date, different name, different status, opposite finding).

CRITICAL: distinguish PARTIAL (under-specifies) from CONTRADICTS (over-specifies in the wrong direction). Examples:
- Claim "filed on March 15", Quote "added 03/16/2026" -> CONTRADICTS (different date)
- Claim "filed on March 15", Quote "filing was timely" -> PARTIAL (on-topic, doesn't pin date)
- Claim "filed on March 15", Quote "the meeting was on the third floor" -> IRRELEVANT (off-topic)
- Claim "filed on March 15", Quote "filed on March 15, 2026" -> SUPPORTS

Output FORMAT (exactly 3 lines):
Line 1: one of SUPPORTS / PARTIAL / IRRELEVANT / CONTRADICTS
Line 2: a confidence score 0.0-1.0 with two decimals (e.g. 0.85)
Line 3: a one-sentence rationale (<= 25 words)

Do not output anything else. No preamble, no thinking tags."""


AUDITOR_USER_TMPL = """CLAIM: {claim}

INLINE QUOTE: "{quote}"

SOURCE CHUNK (the quote was extracted from this):
{source_chunk}

Verdict on line 1, confidence on line 2, one-sentence rationale on line 3."""


def call_claude_audit(claim: str, quote: str, source_chunk: str,
                      model: str, api_key: str) -> dict:
    """Single audit call — returns parsed verdict + confidence + rationale."""
    body = json.dumps({
        "model": model,
        "max_tokens": 200,
        "system": AUDITOR_SYSTEM,
        "messages": [
            {"role": "user", "content": AUDITOR_USER_TMPL.format(
                claim=claim, quote=quote, source_chunk=source_chunk[:3000],
            )},
        ],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read())
    except Exception as e:
        return {
            "verdict": "AUDITOR_ERROR",
            "confidence": 0.0,
            "rationale": f"api error: {e}",
            "raw": "",
        }
    text = ""
    for block in payload.get("content", []):
        if block.get("type") == "text":
            text += block.get("text", "")
    return _parse_audit_output(text.strip())


_VERDICT_TOKENS = {"SUPPORTS", "PARTIAL", "IRRELEVANT", "CONTRADICTS"}
_CONF_RE = re.compile(r"\b(0?\.\d{1,3}|1\.0+|0|1)\b")


def _parse_audit_output(raw: str) -> dict:
    """Parse the 3-line audit output into structured fields."""
    if not raw:
        return {"verdict": "AUDITOR_ERROR", "confidence": 0.0, "rationale": "empty output", "raw": ""}
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    verdict = "AUDITOR_ERROR"
    confidence = 0.0
    rationale = ""
    if lines:
        for tok in _VERDICT_TOKENS:
            if tok in lines[0].upper():
                verdict = tok
                break
    if len(lines) >= 2:
        m = _CONF_RE.search(lines[1])
        if m:
            try:
                confidence = float(m.group(1))
            except ValueError:
                confidence = 0.0
    if len(lines) >= 3:
        rationale = lines[2][:200]
    elif len(lines) == 2:
        # Some models put rationale on line 2 with the confidence
        rationale = lines[1][:200]
    return {
        "verdict": verdict,
        "confidence": round(confidence, 2),
        "rationale": rationale,
        "raw": raw[:400],
        "auditor_model": None,  # filled by caller
        "auditor_prompt_version": AUDITOR_PROMPT_VERSION,
    }


def find_source_chunk_for_quote(quote: str, chunks: list[dict]) -> str:
    """Find the chunk whose content contains the verbatim quote. Falls back to
    the first chunk with the same path if no substring match."""
    quote_clean = quote.replace('\\"', '"').replace("\\'", "'")
    for c in chunks:
        if quote_clean in c.get("content", ""):
            return c["content"]
    # Whitespace-normalized fallback
    qnorm = re.sub(r"\s+", " ", quote_clean).lower()
    for c in chunks:
        if qnorm in re.sub(r"\s+", " ", c.get("content", "")).lower():
            return c["content"]
    # Path-prefix fallback (use first chunk with same rel_path)
    return chunks[0]["content"] if chunks else ""


def determine_disposition(verdict: str, confidence: float,
                           contradicts_threshold: float = 0.70) -> str:
    """Map (verdict, confidence) to disposition per the spec."""
    if verdict == "SUPPORTS":
        return "keep"
    if verdict == "PARTIAL":
        return "soft_flag"
    if verdict == "IRRELEVANT":
        return "soft_flag"
    if verdict == "CONTRADICTS":
        if confidence >= contradicts_threshold:
            return "rewrite"
        return "soft_flag"
    if verdict == "AUDITOR_ERROR":
        return "hold"
    return "hold"


def audit_answer(answer: str, chunks: list[dict],
                  model: str = DEFAULT_AUDITOR_MODEL,
                  api_key: str | None = None,
                  contradicts_threshold: float = 0.70) -> dict:
    """Audit every [grounded] sentence in answer. Returns {audits: [...], summary: {...}}.

    Caller decides what to do with rewrite/hold dispositions.
    """
    if api_key is None:
        api_key = load_env_key()
    if not api_key:
        return {"error": "ANTHROPIC_API_KEY not set", "audits": [], "summary": {}}

    quotes = extract_inline_quotes(answer)
    audits = []
    for q in quotes:
        # Walk back from cite position to find the claim sentence
        cite_start = q["span_in_text"][0]
        preceding = answer[:cite_start]
        sents = re.split(r"(?<=[.!?])\s+", preceding)
        claim = ""
        for s in reversed(sents):
            s = s.strip()
            s_clean = re.sub(r"(?:^\s*\[grounded\]\s*|\s*\[grounded\]\s*$)", "", s, flags=re.I).strip()
            if not s_clean:
                continue
            if re.search(r"`[^`\n]+`\s*:\s*[\"“]", s_clean):
                continue  # skip citation lines
            if len(s_clean) >= 15:
                claim = s_clean.rstrip(".:")
                break
        if not claim:
            continue
        # Find the source chunk for this quote
        source = find_source_chunk_for_quote(q["quote"], chunks)
        if not source:
            audits.append({
                "claim": claim[:200], "quote": q["quote"][:200], "path": q["path"],
                "verdict": "AUDITOR_ERROR", "confidence": 0.0,
                "rationale": "no source chunk found for quote", "disposition": "hold",
                "auditor_model": model, "auditor_prompt_version": AUDITOR_PROMPT_VERSION,
            })
            continue
        # Audit
        result = call_claude_audit(claim, q["quote"], source, model, api_key)
        result["claim"] = claim[:200]
        result["quote"] = q["quote"][:200]
        result["path"] = q["path"]
        result["auditor_model"] = model
        result["disposition"] = determine_disposition(
            result["verdict"], result["confidence"], contradicts_threshold,
        )
        audits.append(result)

    # Summary
    counts = {"SUPPORTS": 0, "PARTIAL": 0, "IRRELEVANT": 0, "CONTRADICTS": 0,
              "AUDITOR_ERROR": 0}
    dispositions = {"keep": 0, "soft_flag": 0, "rewrite": 0, "hold": 0}
    for a in audits:
        counts[a.get("verdict", "AUDITOR_ERROR")] = counts.get(a.get("verdict"), 0) + 1
        dispositions[a.get("disposition", "hold")] = dispositions.get(a.get("disposition"), 0) + 1
    summary = {
        "n_audits": len(audits),
        "verdicts": counts,
        "dispositions": dispositions,
        "auditor_model": model,
        "auditor_prompt_version": AUDITOR_PROMPT_VERSION,
        "contradicts_threshold": contradicts_threshold,
        "needs_rewrite": dispositions["rewrite"] > 0,
        "needs_hold": dispositions["hold"] > 0,
    }
    return {"audits": audits, "summary": summary}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--answer-file", required=True)
    p.add_argument("--chunks-file", required=True,
                   help="JSON file with [{rel_path, content}, ...]")
    p.add_argument("--model", default=DEFAULT_AUDITOR_MODEL)
    p.add_argument("--threshold", type=float, default=0.70,
                   help="Confidence threshold for CONTRADICTS to force rewrite")
    p.add_argument("--out", default=None)
    args = p.parse_args()

    answer = Path(args.answer_file).read_text(encoding="utf-8")
    chunks = json.loads(Path(args.chunks_file).read_text(encoding="utf-8"))
    if isinstance(chunks, dict):
        chunks = chunks.get("chunks") or chunks.get("hits") or []

    result = audit_answer(answer, chunks, model=args.model,
                           contradicts_threshold=args.threshold)
    out_text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(out_text, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(out_text)
    print(f"\nSummary: {result.get('summary', {})}", file=sys.stderr)


if __name__ == "__main__":
    main()

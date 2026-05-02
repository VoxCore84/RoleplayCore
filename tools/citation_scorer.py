#!/usr/bin/env python3
"""Citation precision scorer — measures whether cited sources actually exist and support claims.

This is the pipeline that converts "we claim 96% citation precision" into
"we measured X% citation precision across N outputs."

Methodology (from VoxCore Benchmarking Methodology PDF):
  Citation precision = of all citations an answer makes, what fraction point
  to real source spans that exist in the corpus?

  Citation recall = of all factual claims an answer makes, what fraction
  carry at least one citation?

  Hallucination rate = 1 - (precision * recall * span_correctness)

Pipeline:
  1. Take a query + corpus answer (from /ex-ask or docs_rag_search output)
  2. Extract all citations (file paths, chunk references)
  3. Verify each citation exists in the corpus index
  4. Score: citations_verified / citations_total = precision
  5. Extract factual claims from the answer
  6. Check each claim has at least one citation = recall
  7. Log everything for calibration dashboard

Usage:
    python tools/citation_scorer.py --query "Who is Amy Little?" --answer-file answer.txt
    python tools/citation_scorer.py --batch results.jsonl --output scores.json
    python tools/citation_scorer.py --self-test  # run built-in test queries
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"
KG_DB = REPO_ROOT / ".cache" / "excluded_kg.db"
REPORT_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"
OLLAMA_URL = "http://localhost:11434"
SCORER_MODEL = "gemma4:26b"  # gemma4 is reliable on /api/chat; qwen3.5:27b also works

# Regex patterns for citation extraction
CITATION_PATTERNS = [
    re.compile(r"(?:file[_\s]*path|source|cited?|ref):\s*[`\"']?([^\s`\"']+\.[a-z]{2,5})", re.I),
    re.compile(r"`([^`]+\.(txt|md|pdf|docx|eml|msg)[^`]*)`"),
    re.compile(r"(\S+(?:/|\\)\S+\.\w{2,5})"),
    re.compile(r"\[([^\]]+\.\w{2,5})\]"),
]


def extract_citations(text: str) -> list[str]:
    """Extract file path citations from an answer text."""
    citations = set()
    for pattern in CITATION_PATTERNS:
        for match in pattern.finditer(text):
            path = match.group(1) if match.lastindex else match.group(0)
            path = path.strip("`,\"'()[]")
            if len(path) > 5 and "." in path and not path.startswith("http"):
                citations.add(path)
    return sorted(citations)


def verify_citation_exists(citation: str, fts_conn: sqlite3.Connection) -> bool:
    """Check if a cited path exists in the FTS corpus index."""
    c = fts_conn.cursor()
    citation_lower = citation.lower().replace("\\", "/")
    parts = citation_lower.rsplit("/", 1)
    search_term = parts[-1] if parts else citation_lower

    rows = c.execute(
        "SELECT COUNT(*) FROM chunks WHERE LOWER(rel_path) LIKE ?",
        (f"%{search_term}%",),
    ).fetchone()
    return rows[0] > 0


_CLAIM_TAG_RE = re.compile(r"^\s*\[(grounded|synthesis)\]\s*", re.IGNORECASE)


def claim_kind(claim_text: str) -> tuple[str, str]:
    """Detect the answer-level tag on a claim sentence.

    Returns (kind, clean_claim) where kind is:
      * "grounded"  — sentence asserts a single fact requiring verbatim support
      * "synthesis" — sentence is a derivation/summary; not span-scored
      * "untagged"  — legacy claim with no tag (default behavior — span-scored)

    The clean_claim has the leading [tag] stripped so the judge sees the actual
    sentence, not the tag noise.
    """
    m = _CLAIM_TAG_RE.match(claim_text)
    if not m:
        return ("untagged", claim_text.strip())
    kind = m.group(1).lower()
    return (kind, _CLAIM_TAG_RE.sub("", claim_text, count=1).strip())


def _split_sentences(text: str) -> list[str]:
    """Split answer text into sentences. Splits on:
      - Standard sentence terminators followed by whitespace ([.!?]\\s+)
      - Paragraph breaks (\\n\\n)
      - Start of a [grounded] or [synthesis] tag at line start (forces a new
        sentence even when the previous one ended without a period — e.g. when a
        [grounded] sentence ends with a closing quote and no terminal punctuation).

    The split-on-tag rule keeps tagged claim boundaries faithful so the judge
    sees exactly the claim its author wrote, not a glue of two adjacent claims.
    """
    # First normalize: paragraph breaks become a sentinel terminator
    text = re.sub(r"\n{2,}", "\n\n", text)
    # Insert a synthetic split point before any line that begins with [tag]
    text = re.sub(r"\n(\s*\[(?:grounded|synthesis)\])", r"\n\n\1", text, flags=re.IGNORECASE)
    # Now split on (a) standard terminators OR (b) paragraph breaks
    parts = re.split(r"(?<=[.!?])\s+|\n\n+", text)
    return [p for p in parts if p and p.strip()]


def extract_claims(text: str) -> list[str]:
    """Extract factual claims from answer text using sentence splitting."""
    sentences = _split_sentences(text)
    claims = []
    for s in sentences:
        s = s.strip()
        if len(s) < 20:
            continue
        if s.lower().startswith(("note:", "disclaimer:", "caveat:", "however,")):
            continue
        # Tagged sentences ([grounded] / [synthesis]) are always claims regardless
        # of marker words — the answer author explicitly tagged them.
        if _CLAIM_TAG_RE.match(s):
            claims.append(s)
            continue
        if any(
            marker in s.lower()
            for marker in [
                "according to", "states that", "shows that", "indicates",
                "confirms", "documents", "filed", "dated", "signed",
                "reported", "found", "determined", "concluded",
            ]
        ):
            claims.append(s)
        elif re.search(r"\d{4}|\d+%|\$[\d,]+", s):
            claims.append(s)
    return claims


def claim_has_citation(claim: str, citations: list[str], full_text: str) -> bool:
    """Check if a claim is supported by at least one citation in the answer."""
    claim_lower = claim.lower()
    for cite in citations:
        cite_parts = cite.lower().replace("\\", "/").rsplit("/", 1)
        cite_name = cite_parts[-1] if cite_parts else cite.lower()
        cite_stem = cite_name.rsplit(".", 1)[0]
        paragraph_window = full_text[
            max(0, full_text.lower().find(claim_lower[:30]) - 500) :
            full_text.lower().find(claim_lower[:30]) + len(claim) + 500
        ]
        if cite_stem in paragraph_window.lower() or cite_name in paragraph_window.lower():
            return True
    return False


# =========================================================================
# LLM-as-judge — span correctness scoring
#
# Span correctness asks: of the citations that point to real files, do those
# files' contents actually support the claim being made? This requires reading
# the cited chunk and asking a judge model whether the support is real.
#
# Two backends:
#   * local Qwen 27B via Ollama (default, free)
#   * Claude API (--judge claude-opus / claude-sonnet, more accurate, costs $)
# =========================================================================

JUDGE_PROMPT = """You are a citation-faithfulness judge. Given a CLAIM and a CITED SOURCE EXCERPT, decide whether the source excerpt supports the claim.

CLAIM: {claim}

CITED SOURCE: {citation_path}

SOURCE EXCERPT:
\"\"\"
{excerpt}
\"\"\"

Answer with ONE of:
  SUPPORTS    - The excerpt clearly supports the specific claim being made.
  PARTIAL     - The excerpt is on-topic but does not specifically support the claim.
  CONTRADICTS - The excerpt contradicts the claim.
  IRRELEVANT  - The excerpt does not address the subject of the claim.
  UNREADABLE  - The excerpt is empty or unintelligible.

Then on a new line, give one short sentence (max 25 words) explaining your verdict.

VERDICT:"""


def fetch_excerpt_for_citation(citation: str, claim: str, fts_conn: sqlite3.Connection,
                                window: int = 1500) -> str:
    """Pull the relevant chunk text for a citation from the FTS corpus.

    Strategy: find the chunk whose ``rel_path`` matches the citation basename,
    then return the ``window``-char excerpt nearest to keywords from the claim.
    """
    cite_path = citation.lower().replace("\\", "/")
    parts = cite_path.rsplit("/", 1)
    basename = parts[-1] if parts else cite_path
    c = fts_conn.cursor()

    # Get any chunks whose rel_path contains the citation basename
    rows = c.execute(
        "SELECT content, rel_path FROM chunks WHERE LOWER(rel_path) LIKE ? LIMIT 5",
        (f"%{basename}%",),
    ).fetchall()
    if not rows:
        return ""

    # Score chunks by overlap with claim keywords (simple word match)
    claim_words = {w for w in re.findall(r"[A-Za-z][A-Za-z0-9]{3,}", claim.lower())}
    if not claim_words:
        return (rows[0][0] or "")[:window]

    best_text = ""
    best_score = -1
    for text, _path in rows:
        text = text or ""
        text_lower = text.lower()
        score = sum(1 for w in claim_words if w in text_lower)
        if score > best_score:
            best_score = score
            best_text = text

    if not best_text:
        return ""

    # Find the densest claim-keyword window
    text_lower = best_text.lower()
    best_pos = 0
    best_density = 0
    step = max(100, window // 4)
    for pos in range(0, max(1, len(best_text) - window + 1), step):
        chunk = text_lower[pos:pos + window]
        density = sum(1 for w in claim_words if w in chunk)
        if density > best_density:
            best_density = density
            best_pos = pos
    return best_text[best_pos:best_pos + window]


JUDGE_SYSTEM = (
    "You are a citation-faithfulness judge. Read the CLAIM and the SOURCE EXCERPT, "
    "then on the FIRST line output exactly one of these tokens (no punctuation, no other words): "
    "SUPPORTS, PARTIAL, CONTRADICTS, IRRELEVANT, UNREADABLE. "
    "On the SECOND line write one short sentence (max 25 words) explaining the verdict. "
    "Do not output anything else. Do not output thinking tags."
)

JUDGE_USER = (
    "CLAIM: {claim}\n\n"
    "CITED SOURCE: {citation_path}\n\n"
    "SOURCE EXCERPT:\n\"\"\"\n{excerpt}\n\"\"\"\n\n"
    "Verdict on line 1, reason on line 2."
)


def judge_span_ollama(claim: str, citation: str, excerpt: str,
                      model: str = SCORER_MODEL) -> dict:
    """Ask a local Ollama model for a span verdict.

    Uses /api/chat with a strict system message. Reasoning models (Qwen 3.5)
    handle thinking internally before the chat response, which avoids the
    num_predict-truncation problem the /api/generate endpoint has.
    """
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": JUDGE_SYSTEM},
            {"role": "user", "content": JUDGE_USER.format(
                claim=claim, citation_path=citation, excerpt=excerpt or "(empty)",
            )},
        ],
        "stream": False,
        "options": {"temperature": 0.0},
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/chat",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            payload = json.loads(resp.read())
    except Exception as e:
        return {"verdict": "ERROR", "reason": f"ollama: {e}", "raw": ""}
    text = payload.get("message", {}).get("content", "") or ""
    return _parse_verdict(text)


def judge_span_claude(claim: str, citation: str, excerpt: str,
                      model: str = "claude-opus-4-7") -> dict:
    """Ask Claude API for a span verdict. Requires ANTHROPIC_API_KEY env var."""
    import os
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return {"verdict": "ERROR", "reason": "ANTHROPIC_API_KEY not set", "raw": ""}
    prompt = JUDGE_PROMPT.format(claim=claim, citation_path=citation, excerpt=excerpt or "(empty)")
    body = json.dumps({
        "model": model,
        "max_tokens": 200,
        "messages": [{"role": "user", "content": prompt}],
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
        return {"verdict": "ERROR", "reason": f"claude: {e}", "raw": ""}
    text = ""
    for block in payload.get("content", []):
        if block.get("type") == "text":
            text += block.get("text", "")
    return _parse_verdict(text)


_VERDICT_RE = re.compile(r"\b(SUPPORTS|PARTIAL|CONTRADICTS|IRRELEVANT|UNREADABLE)\b", re.I)


def _parse_verdict(raw: str) -> dict:
    """Pull the verdict token + first sentence of reasoning."""
    raw = (raw or "").strip()
    m = _VERDICT_RE.search(raw)
    verdict = m.group(1).upper() if m else "UNPARSEABLE"
    # Reason = text after the verdict, first sentence
    reason = ""
    if m:
        tail = raw[m.end():].strip(": \n")
        # First sentence
        first = re.split(r"(?<=[.!?])\s", tail, maxsplit=1)
        reason = (first[0] if first else tail).strip()
    return {"verdict": verdict, "reason": reason[:200], "raw": raw[:400]}


def score_span_correctness(claim: str, citations: list[str],
                            fts_conn: sqlite3.Connection,
                            judge: str = "ollama",
                            judge_model: str | None = None) -> list[dict]:
    """For each citation supporting a claim, return the judge's verdict."""
    judge_fn = judge_span_ollama if judge == "ollama" else judge_span_claude
    if judge_model is None:
        judge_model = SCORER_MODEL if judge == "ollama" else "claude-opus-4-7"
    verdicts = []
    for cite in citations:
        excerpt = fetch_excerpt_for_citation(cite, claim, fts_conn)
        v = judge_fn(claim, cite, excerpt, model=judge_model)
        v["citation"] = cite
        v["excerpt_chars"] = len(excerpt)
        verdicts.append(v)
    return verdicts


def aggregate_span_verdicts(verdicts: list[dict]) -> dict:
    """Aggregate per-citation verdicts into a span-correctness score for the claim.

    A claim is span-correct if AT LEAST ONE of its citations is SUPPORTS.
    PARTIAL counts as 0.5. CONTRADICTS / IRRELEVANT / UNREADABLE / ERROR / UNPARSEABLE = 0.
    """
    if not verdicts:
        return {"score": 0.0, "best_verdict": "NONE", "n": 0}
    best = max(verdicts, key=lambda v: _verdict_weight(v.get("verdict", "")))
    score = _verdict_weight(best.get("verdict", ""))
    return {"score": score, "best_verdict": best.get("verdict"), "n": len(verdicts)}


def _verdict_weight(v: str) -> float:
    return {
        "SUPPORTS": 1.0,
        "PARTIAL": 0.5,
        "CONTRADICTS": 0.0,
        "IRRELEVANT": 0.0,
        "UNREADABLE": 0.0,
        "ERROR": 0.0,
        "UNPARSEABLE": 0.0,
    }.get((v or "").upper(), 0.0)


def score_answer(query: str, answer: str, fts_conn: sqlite3.Connection,
                 judge: str | None = None, judge_model: str | None = None) -> dict:
    """Score a single answer for citation precision, recall, and (optionally) span correctness.

    If ``judge`` is "ollama" or "claude", run the LLM-as-judge wrapper to score
    span correctness — i.e. whether each cited file actually supports its claim.
    Without a judge, span_correctness stays None and hallucination_rate is the
    P × R component only.
    """
    citations = extract_citations(answer)
    claims = extract_claims(answer)

    verified = 0
    unverified = []
    for cite in citations:
        if verify_citation_exists(cite, fts_conn):
            verified += 1
        else:
            unverified.append(cite)

    precision = verified / len(citations) if citations else None

    cited_claims = 0
    uncited_claims = []
    claim_records = []
    for claim in claims:
        kind, clean_claim = claim_kind(claim)
        cited = claim_has_citation(claim, citations, answer)
        record = {"claim": claim[:200], "cited": cited, "kind": kind, "clean_claim": clean_claim[:200]}
        if cited:
            cited_claims += 1
            # Find which citations sit near this claim — those are the ones we judge
            claim_lower = claim.lower()
            window_start = max(0, answer.lower().find(claim_lower[:30]) - 500)
            window_end = answer.lower().find(claim_lower[:30]) + len(claim) + 500
            window = answer[window_start:window_end].lower()
            nearby = [c for c in citations
                      if c.lower().rsplit("/", 1)[-1].rsplit(".", 1)[0] in window]
            record["nearby_citations"] = nearby
        else:
            uncited_claims.append(claim[:80])
            record["nearby_citations"] = []
        claim_records.append(record)

    recall = cited_claims / len(claims) if claims else None

    # ---- Inline-grounded citation extraction + verification ----
    # When the answer includes verbatim quoted spans tied to citations, we can
    # bypass the chunk-fetch artifact entirely — the model told us exactly which
    # span supports each claim. We verify the quote exists verbatim in the cited
    # file (fast substring), then judge the claim-vs-quote semantically.
    #
    # Two import paths so this works whether citation_scorer is run as
    # ``python tools/citation_scorer.py`` (sys.path[0] = tools/) or imported
    # from repo root.
    try:
        from tools.inline_grounding import extract_inline_quotes, verify_quote_in_file
    except ImportError:
        try:
            from inline_grounding import extract_inline_quotes, verify_quote_in_file
        except ImportError:
            extract_inline_quotes = None
            verify_quote_in_file = None

    inline_grounding = None
    if extract_inline_quotes is not None:
        ig_quotes = extract_inline_quotes(answer)
        ig_verifications = []
        for ig in ig_quotes:
            v = verify_quote_in_file(ig["quote"], ig["path"], fts_conn=fts_conn)
            ig_verifications.append({
                "path": ig["path"],
                "quote": ig["quote"][:200],
                "format": ig["format"],
                "verified": v["verified"],
                "method": v["method"],
                "span_in_text": ig["span_in_text"],
            })
        n_quotes = len(ig_quotes)
        n_verified = sum(1 for v in ig_verifications if v["verified"])
        inline_grounding = {
            "n_quotes": n_quotes,
            "verified_count": n_verified,
            "fabricated_count": n_quotes - n_verified,
            "verification_rate": round(n_verified / n_quotes, 4) if n_quotes else None,
            "verifications": ig_verifications,
        }

    # ---- LLM-as-judge for span correctness (optional) ----
    # Inline-grounded path: when a claim has a nearby inline-quoted citation,
    # judge the claim-vs-quote directly (much higher signal than chunk-fetch).
    # Fall back to chunk-fetch for claims with no inline quote.
    span_score = None
    span_per_claim = []
    if judge in ("ollama", "claude") and claim_records:
        # Build a (claim_text -> nearby inline quotes) index for O(1) lookup
        inline_by_claim_pos: list[dict] = []
        if inline_grounding and inline_grounding["verifications"]:
            inline_by_claim_pos = [
                {"path": v["path"], "quote": v["quote"], "verified": v["verified"],
                 "span_start": v["span_in_text"][0], "span_end": v["span_in_text"][1]}
                for v in inline_grounding["verifications"]
            ]

        weighted = 0.0
        n_with_cite = 0
        for record in claim_records:
            # [synthesis]-tagged claims are derivations/summaries — they carry source
            # citations for traceability but are NOT required to have verbatim quote
            # support. Excluded from span scoring entirely. Recorded for transparency.
            if record.get("kind") == "synthesis":
                span_per_claim.append({
                    "claim": record["claim"], "verdicts": [], "score": None,
                    "kind": "synthesis", "scoring_path": "skipped_synthesis",
                })
                continue

            if not record["nearby_citations"]:
                span_per_claim.append({"claim": record["claim"], "verdicts": [], "score": None,
                                       "kind": record.get("kind")})
                continue

            # Use the [tag]-stripped sentence so the judge sees only the assertion.
            judged_claim = record.get("clean_claim") or record["claim"]

            # Find inline quotes whose span_in_text is within ±400 chars of the claim
            claim_pos = answer.lower().find(record["claim"][:40].lower())
            inline_for_claim = []
            if claim_pos >= 0:
                for iq in inline_by_claim_pos:
                    midpoint = (iq["span_start"] + iq["span_end"]) // 2
                    if abs(midpoint - claim_pos) <= 600:
                        inline_for_claim.append(iq)

            if inline_for_claim:
                # Inline-grounded path: judge claim vs each verified quote directly
                verdicts = []
                for iq in inline_for_claim:
                    if not iq["verified"]:
                        verdicts.append({
                            "verdict": "FABRICATED",
                            "reason": "quote not found verbatim in cited file",
                            "citation": iq["path"],
                            "quote": iq["quote"][:200],
                        })
                        continue
                    judge_fn = judge_span_ollama if judge == "ollama" else judge_span_claude
                    if judge_model is None:
                        judge_model_use = SCORER_MODEL if judge == "ollama" else "claude-opus-4-7"
                    else:
                        judge_model_use = judge_model
                    v = judge_fn(judged_claim, iq["path"], iq["quote"], model=judge_model_use)
                    v["citation"] = iq["path"]
                    v["quote"] = iq["quote"][:200]
                    v["scoring_path"] = "inline_grounded"
                    verdicts.append(v)
                agg = aggregate_span_verdicts(verdicts)
                # FABRICATED is a hard 0
                if any(v.get("verdict") == "FABRICATED" for v in verdicts):
                    agg["score"] = min(agg["score"], 0.0) if agg["score"] is not None else 0.0
            else:
                # Chunk-fetch fallback (original behavior)
                verdicts = score_span_correctness(
                    judged_claim, record["nearby_citations"],
                    fts_conn, judge=judge, judge_model=judge_model,
                )
                for v in verdicts:
                    v["scoring_path"] = "chunk_fetch"
                agg = aggregate_span_verdicts(verdicts)

            weighted += agg["score"]
            n_with_cite += 1
            span_per_claim.append({
                "claim": record["claim"],
                "kind": record.get("kind"),
                "score": agg["score"],
                "best_verdict": agg["best_verdict"],
                "scoring_path": "inline_grounded" if inline_for_claim else "chunk_fetch",
                "verdicts": verdicts,
            })
        span_score = round(weighted / n_with_cite, 4) if n_with_cite else None

    hallucination_rate = None
    if precision is not None and recall is not None:
        component = precision * recall
        if span_score is not None:
            component *= span_score
        hallucination_rate = round(1.0 - component, 4)

    return {
        "query": query,
        "total_citations": len(citations),
        "verified_citations": verified,
        "unverified_citations": unverified,
        "citation_precision": round(precision, 4) if precision is not None else None,
        "total_claims": len(claims),
        "cited_claims": cited_claims,
        "uncited_claims": uncited_claims[:5],
        "citation_recall": round(recall, 4) if recall is not None else None,
        "span_correctness": span_score,
        "span_per_claim": span_per_claim if span_score is not None else None,
        "hallucination_rate": hallucination_rate,
        "judge": judge,
        "judge_model": judge_model,
        "inline_grounding": inline_grounding,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


def run_self_test(fts_conn: sqlite3.Connection, judge: str | None = None,
                   judge_model: str | None = None) -> dict:
    """Run built-in test queries through the scoring pipeline."""
    test_cases = [
        {
            "query": "Who is Amy Little?",
            "answer": (
                "Amy Little is a Senior SAPR Policy Analyst at HAF/A1ZA with D-SAACP certification. "
                "She was engaged in April 2026 following a 2-hour call. "
                "Source: `01_CONTACTS_AND_REFERENCES.md` and `00_CALL_BRIEF.md`."
            ),
        },
        {
            "query": "What is the ADSCD?",
            "answer": (
                "The Active Duty Service Commitment Date (ADSCD) is 10 August 2026, "
                "marking Captain Taylor's separation from the Air Force. "
                "This is documented in `MASTER_05_STATUS_DEADLINES_EXECUTION.md`."
            ),
        },
        {
            "query": "What happened at Rio Vista?",
            "answer": (
                "On October 23, 2024, Captain Taylor was transferred to Rio Vista, "
                "a maximum security psychiatric facility. This forced transfer is documented "
                "in the timeline at `10. October 2024 Timeline.docx` and referenced in "
                "`Executive Summary by Taylor - 24 Jan 2025.docx`."
            ),
        },
        {
            "query": "Made up claim with no citations",
            "answer": (
                "The defendant clearly violated 14 separate federal statutes on March 5, 2024. "
                "This resulted in $5.2 million in damages and a formal censure by the Senate "
                "Committee on Armed Services."
            ),
        },
    ]

    results = []
    for tc in test_cases:
        score = score_answer(tc["query"], tc["answer"], fts_conn, judge=judge, judge_model=judge_model)
        results.append(score)
        status = "PASS" if (score["citation_precision"] or 0) > 0.5 else "WATCH"
        if score["total_citations"] == 0 and score["total_claims"] > 0:
            status = "FAIL (no citations)"
        span = score.get("span_correctness")
        span_str = f" span={span}" if span is not None else ""
        print(
            f"  [{status}] {tc['query'][:40]}: "
            f"precision={score['citation_precision']} "
            f"recall={score['citation_recall']} "
            f"cites={score['total_citations']} "
            f"claims={score['total_claims']}{span_str}"
        )

    precisions = [r["citation_precision"] for r in results if r["citation_precision"] is not None]
    recalls = [r["citation_recall"] for r in results if r["citation_recall"] is not None]

    summary = {
        "test_count": len(results),
        "avg_precision": round(sum(precisions) / len(precisions), 4) if precisions else None,
        "avg_recall": round(sum(recalls) / len(recalls), 4) if recalls else None,
        "results": results,
    }
    return summary


def main():
    parser = argparse.ArgumentParser(description="Citation precision scorer")
    parser.add_argument("--self-test", action="store_true", help="Run built-in test queries")
    parser.add_argument("--query", help="Single query to score")
    parser.add_argument("--answer", help="Answer text to score")
    parser.add_argument("--answer-file", help="File containing the answer")
    parser.add_argument("--batch", help="JSONL file with {query, answer} pairs")
    parser.add_argument("--output", help="Output JSON file for results")
    parser.add_argument(
        "--judge",
        choices=["ollama", "claude"],
        default=None,
        help="Run LLM-as-judge for span correctness (default: skip)",
    )
    parser.add_argument(
        "--judge-model",
        default=None,
        help="Model id for the judge (default: qwen3.5:27b-q4_K_M for ollama, claude-opus-4-7 for claude)",
    )
    args = parser.parse_args()

    if not FTS_DB.exists():
        print(f"ERROR: FTS database not found at {FTS_DB}", file=sys.stderr)
        sys.exit(1)

    fts_conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True)

    if args.self_test:
        print("=== Citation Scorer Self-Test ===\n")
        summary = run_self_test(fts_conn, judge=args.judge, judge_model=args.judge_model)
        print(f"\n=== Summary ===")
        print(f"  Tests: {summary['test_count']}")
        print(f"  Avg precision: {summary['avg_precision']}")
        print(f"  Avg recall: {summary['avg_recall']}")

        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        ts = time.strftime("%Y%m%d_%H%M%S")
        report_path = REPORT_DIR / f"citation_score_{ts}.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"\n  Report: {report_path}")

    elif args.query and (args.answer or args.answer_file):
        answer = args.answer
        if args.answer_file:
            answer = Path(args.answer_file).read_text(encoding="utf-8")
        score = score_answer(args.query, answer, fts_conn, judge=args.judge, judge_model=args.judge_model)
        print(json.dumps(score, indent=2, ensure_ascii=False))

    elif args.batch:
        results = []
        with open(args.batch, encoding="utf-8") as f:
            for line in f:
                item = json.loads(line.strip())
                score = score_answer(
                    item["query"], item["answer"], fts_conn,
                    judge=args.judge, judge_model=args.judge_model,
                )
                results.append(score)

        precisions = [r["citation_precision"] for r in results if r["citation_precision"] is not None]
        recalls = [r["citation_recall"] for r in results if r["citation_recall"] is not None]

        output = {
            "batch_count": len(results),
            "avg_precision": round(sum(precisions) / len(precisions), 4) if precisions else None,
            "avg_recall": round(sum(recalls) / len(recalls), 4) if recalls else None,
            "results": results,
        }

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            print(f"Results written to {args.output}")
        else:
            print(json.dumps(output, indent=2, ensure_ascii=False))

    else:
        parser.print_help()

    fts_conn.close()


if __name__ == "__main__":
    main()

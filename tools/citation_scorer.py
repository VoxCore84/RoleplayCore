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
SCORER_MODEL = "qwen3.5:27b-q4_K_M"

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


def extract_claims(text: str) -> list[str]:
    """Extract factual claims from answer text using sentence splitting."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    claims = []
    for s in sentences:
        s = s.strip()
        if len(s) < 20:
            continue
        if s.lower().startswith(("note:", "disclaimer:", "caveat:", "however,")):
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


def score_answer(query: str, answer: str, fts_conn: sqlite3.Connection) -> dict:
    """Score a single answer for citation precision and recall."""
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
    for claim in claims:
        if claim_has_citation(claim, citations, answer):
            cited_claims += 1
        else:
            uncited_claims.append(claim[:80])

    recall = cited_claims / len(claims) if claims else None

    span_correctness = None  # requires LLM-as-judge, deferred

    hallucination_rate = None
    if precision is not None and recall is not None:
        hallucination_rate = round(1.0 - (precision * recall), 4)

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
        "span_correctness": span_correctness,
        "hallucination_rate": hallucination_rate,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


def run_self_test(fts_conn: sqlite3.Connection) -> dict:
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
        score = score_answer(tc["query"], tc["answer"], fts_conn)
        results.append(score)
        status = "PASS" if (score["citation_precision"] or 0) > 0.5 else "WATCH"
        if score["total_citations"] == 0 and score["total_claims"] > 0:
            status = "FAIL (no citations)"
        print(
            f"  [{status}] {tc['query'][:40]}: "
            f"precision={score['citation_precision']} "
            f"recall={score['citation_recall']} "
            f"cites={score['total_citations']} "
            f"claims={score['total_claims']}"
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
    args = parser.parse_args()

    if not FTS_DB.exists():
        print(f"ERROR: FTS database not found at {FTS_DB}", file=sys.stderr)
        sys.exit(1)

    fts_conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True)

    if args.self_test:
        print("=== Citation Scorer Self-Test ===\n")
        summary = run_self_test(fts_conn)
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
        score = score_answer(args.query, answer, fts_conn)
        print(json.dumps(score, indent=2, ensure_ascii=False))

    elif args.batch:
        results = []
        with open(args.batch, encoding="utf-8") as f:
            for line in f:
                item = json.loads(line.strip())
                score = score_answer(item["query"], item["answer"], fts_conn)
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

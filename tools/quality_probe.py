#!/usr/bin/env python3
"""Retrieval quality probe — runs the test suite and reports precision/recall.

Hand-curated 20 anchor queries with expected top-N matches. The discipline I
should have had from day 1. Without this, any chunking/embedding/rerank change
silently regresses retrieval.

Runs against:
  1. FTS5 alone (baseline)
  2. ChromaDB alone (semantic baseline)
  3. Hybrid RRF (current production)

Emits per-engine pass rates + per-query drill-down. Writes markdown +
JSON reports to AI_Studio/Reports/scheduled/quality_probe_<date>.*.

Usage:
    python tools/quality_probe.py                   # run all 3 engines
    python tools/quality_probe.py --engine hybrid
    python tools/quality_probe.py --suite path/to/custom.jsonl
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SUITE_FILE = REPO_ROOT / "tools" / "retrieval_test_suite.jsonl"
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"
CHROMA_DIR = REPO_ROOT / ".cache" / "rag" / "chroma"
CHROMA_COLLECTION = "important_docs"
OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
REPORT_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"


def load_suite(path: Path) -> list[dict]:
    suite = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            suite.append(json.loads(line))
    return suite


def embed(q: str) -> list[float] | None:
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/embed",
        data=json.dumps({"model": EMBED_MODEL, "input": q}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8")).get("embeddings", [None])[0]
    except Exception:
        return None


_STOPWORDS = {
    "the","a","an","is","are","was","were","be","been","being","of","to","in",
    "on","at","for","by","with","from","about","and","or","but","if","then",
    "else","when","where","why","how","what","which","who","whom","whose",
    "that","this","these","those","i","me","my","mine","you","your","yours",
    "he","him","his","she","her","hers","it","its","they","them","their","theirs",
    "we","us","our","ours","do","does","did","have","has","had","can","could",
    "would","should","will","shall","may","might","must","not","no","yes","as",
    "so","than","too","very","just","only","any","all","some","each","every",
    "other","another",
}


def _prep_fts_and(q: str) -> str:
    """AND-mode FTS5 query — all terms must co-occur."""
    if '"' in q:
        return q
    toks = []
    for t in q.split():
        s = t.strip(".,;:!?()[]{}")
        if not s:
            continue
        if s[0].isupper() or s.lower() not in _STOPWORDS:
            toks.append(f'"{s}"' if "-" in s else s)
    return " ".join(toks) if toks else q


def _prep_fts_or(q: str) -> str:
    """OR-mode FTS5 query — partial matches ranked by BM25 coverage."""
    if '"' in q:
        return q
    toks = []
    for t in q.split():
        s = t.strip(".,;:!?()[]{}")
        if not s:
            continue
        if s[0].isupper() or s.lower() not in _STOPWORDS:
            toks.append(f'"{s}"' if "-" in s else s)
    if not toks:
        return q
    return " OR ".join(toks)


def fts_query(q: str, limit: int = 20) -> list[str]:
    """AND-preferred with OR fallback, document-level dedup."""
    if not FTS_DB.exists():
        return []
    conn = sqlite3.connect(str(FTS_DB))

    # AND first
    and_query = _prep_fts_and(q)
    and_rows = []
    try:
        and_rows = conn.execute(
            """SELECT c.rel_path FROM chunks_fts
               JOIN chunks c ON c.rowid = chunks_fts.rowid
               WHERE chunks_fts MATCH ? ORDER BY rank LIMIT ?""",
            (and_query, limit),
        ).fetchall()
    except sqlite3.OperationalError:
        pass

    # OR fallback if AND is thin
    or_rows = []
    if len(and_rows) < 10:
        or_query = _prep_fts_or(q)
        try:
            or_rows = conn.execute(
                """SELECT c.rel_path FROM chunks_fts
                   JOIN chunks c ON c.rowid = chunks_fts.rowid
                   WHERE chunks_fts MATCH ? ORDER BY rank LIMIT ?""",
                (or_query, limit),
            ).fetchall()
        except sqlite3.OperationalError:
            pass

    conn.close()

    # Merge: AND first, then OR, dedup by path
    seen = set()
    result = []
    for r in and_rows:
        p = r[0]
        if p not in seen:
            seen.add(p)
            result.append(p)
    for r in or_rows:
        p = r[0]
        if p not in seen:
            seen.add(p)
            result.append(p)
    return result[:limit]


def vector_query(q: str, limit: int = 20) -> list[str]:
    if not CHROMA_DIR.exists():
        return []
    try:
        import chromadb
    except ImportError:
        return []
    vec = embed(q)
    if vec is None:
        return []
    try:
        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        col = client.get_collection(CHROMA_COLLECTION)
        res = col.query(query_embeddings=[vec], n_results=min(limit, col.count()),
                        include=["metadatas"])
        return [m.get("rel_path", "") for m in res["metadatas"][0]]
    except Exception as e:
        print(f"  vector error: {e}", file=sys.stderr)
        return []


def hybrid_query(q: str, limit: int = 20) -> list[str]:
    """Delegate to excluded_hybrid_search.py for canonical RRF + rerank."""
    try:
        r = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools" / "excluded_hybrid_search.py"),
             q, "--top-k", str(limit), "--json"],
            capture_output=True, text=True, timeout=120,
        )
        if r.returncode != 0:
            return []
        data = json.loads(r.stdout)
        return [h["rel_path"] for h in data.get("hits", [])]
    except Exception as e:
        print(f"  hybrid error: {e}", file=sys.stderr)
        return []


def evaluate_query(q_spec: dict, results: list[str]) -> dict:
    """Check if ANY expected substring appears in top `min_rank` results.

    Accepts either `expected_path_substring` (legacy, single) or
    `expected_paths` (list — pass if any substring matches).
    """
    if "expected_paths" in q_spec:
        expected_list = [e.lower() for e in q_spec["expected_paths"]]
    else:
        expected_list = [q_spec["expected_path_substring"].lower()]
    min_rank = q_spec.get("min_rank", 5)
    rank_found = None
    matched_expected = None
    for i, path in enumerate(results[:min_rank], 1):
        pl = path.lower()
        for exp in expected_list:
            if exp in pl:
                rank_found = i
                matched_expected = exp
                break
        if rank_found:
            break
    return {
        "id": q_spec["id"],
        "query": q_spec["query"],
        "expected": expected_list,
        "matched": matched_expected,
        "min_rank": min_rank,
        "kind": q_spec.get("kind", ""),
        "passed": rank_found is not None,
        "rank_found": rank_found,
        "top_results": results[:5],
    }


def run_engine(name: str, qfn, suite: list[dict]) -> dict:
    print(f"\n=== {name} ===", file=sys.stderr)
    t0 = time.perf_counter()
    results = []
    for q_spec in suite:
        hits = qfn(q_spec["query"], max(q_spec.get("min_rank", 5), 20))
        evaluation = evaluate_query(q_spec, hits)
        results.append(evaluation)
        status = "PASS" if evaluation["passed"] else "FAIL"
        rank = evaluation["rank_found"] or "-"
        print(f"  [{evaluation['id']:2}] {status} rank={rank} — {q_spec['query'][:60]}", file=sys.stderr)
    elapsed = time.perf_counter() - t0
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    by_kind: dict[str, dict] = {}
    for r in results:
        k = r.get("kind", "")
        by_kind.setdefault(k, {"pass": 0, "total": 0})
        by_kind[k]["total"] += 1
        if r["passed"]:
            by_kind[k]["pass"] += 1
    return {
        "engine": name,
        "elapsed_sec": round(elapsed, 1),
        "passed": passed,
        "total": total,
        "pass_rate": round(passed / total, 3) if total else 0,
        "by_kind": by_kind,
        "results": results,
    }


def format_report(runs: list[dict]) -> str:
    lines = [
        f"# Retrieval Quality Probe — {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Summary",
        "",
        "| Engine | Passed | Total | Rate | Elapsed |",
        "|--------|--------|-------|------|---------|",
    ]
    for r in runs:
        lines.append(f"| {r['engine']} | {r['passed']} | {r['total']} | {r['pass_rate']*100:.1f}% | {r['elapsed_sec']}s |")

    lines += ["", "## By Query Kind", "", "| Engine | " + " | ".join(sorted({k for r in runs for k in r["by_kind"]})) + " |", "|--------|" + "|".join(["--------"] * len({k for r in runs for k in r["by_kind"]})) + "|"]
    kinds = sorted({k for r in runs for k in r["by_kind"]})
    for r in runs:
        row = [r["engine"]]
        for k in kinds:
            bk = r["by_kind"].get(k, {"pass": 0, "total": 0})
            if bk["total"]:
                row.append(f"{bk['pass']}/{bk['total']}")
            else:
                row.append("-")
        lines.append("| " + " | ".join(row) + " |")

    lines += ["", "## Per-Query (hybrid engine)", ""]
    hybrid_run = next((r for r in runs if r["engine"] == "hybrid"), None)
    if hybrid_run:
        lines.append("| # | Status | Rank | Kind | Query | Top hit |")
        lines.append("|---|--------|------|------|-------|---------|")
        for r in hybrid_run["results"]:
            status = "✓" if r["passed"] else "✗"
            rank = r["rank_found"] or "-"
            top = r["top_results"][0] if r["top_results"] else "-"
            lines.append(f"| {r['id']} | {status} | {rank} | {r['kind']} | {r['query'][:50]} | `{top[:50]}` |")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--engine", choices=["fts", "vector", "hybrid", "all"], default="all")
    ap.add_argument("--suite", default=str(SUITE_FILE))
    args = ap.parse_args()

    suite_path = Path(args.suite)
    if not suite_path.exists():
        print(f"ERROR: test suite not found at {suite_path}", file=sys.stderr)
        return 1
    suite = load_suite(suite_path)
    print(f"Loaded {len(suite)} queries from {suite_path}", file=sys.stderr)

    runs = []
    if args.engine in ("fts", "all"):
        runs.append(run_engine("fts", fts_query, suite))
    if args.engine in ("vector", "all"):
        runs.append(run_engine("vector", vector_query, suite))
    if args.engine in ("hybrid", "all"):
        runs.append(run_engine("hybrid", hybrid_query, suite))

    # Reports
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    md_path = REPORT_DIR / f"quality_probe_{stamp}.md"
    json_path = REPORT_DIR / f"quality_probe_{stamp}.json"
    md_path.write_text(format_report(runs), encoding="utf-8")
    json_path.write_text(json.dumps({"date": time.strftime("%Y-%m-%d %H:%M:%S"),
                                      "runs": runs}, indent=2, default=str),
                         encoding="utf-8")
    print(f"\nReports:\n  {md_path}\n  {json_path}", file=sys.stderr)

    # Print summary to stdout
    print()
    print("## Summary")
    for r in runs:
        print(f"  {r['engine']:8} {r['passed']:2}/{r['total']} ({r['pass_rate']*100:.1f}%) in {r['elapsed_sec']}s")

    # Exit non-zero on regression (pass rate < 80%)
    any_weak = any(r["pass_rate"] < 0.80 for r in runs)
    return 0 if not any_weak else 2


if __name__ == "__main__":
    sys.exit(main())

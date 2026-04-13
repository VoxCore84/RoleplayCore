#!/usr/bin/env python3
"""Excluded/ corpus lint — Karpathy KB Phase 4 equivalent.

Checks the document corpus for integrity issues comparable to what CalmCore's
codebase_freshness() / codebase_stale_ids() do for the codebase:

1. ORPHAN — extracted .txt sidecars whose source file no longer exists
2. STALE — source file newer than its extracted .txt cache
3. MISSING — files in Excluded/ that are extractable but have no cache entry
4. DUPLICATE — same content sha256 extracted to two different cache paths
5. MEMORY DRIFT — memory/*.md files older than N days when their corresponding
   source folder has newer content
6. CITATION BREAK — memory files citing `file_path:line` where the file doesn't exist

Output:
    - Console table summary
    - JSON report to AI_Studio/Reports/scheduled/excluded_lint_<timestamp>.json
    - Fix suggestions (no auto-repairs; user runs /ex-refresh if needed)

Usage:
    python tools/excluded_lint.py                   # full scan
    python tools/excluded_lint.py --json            # machine-readable
    python tools/excluded_lint.py --check orphan    # only orphan check
    python tools/excluded_lint.py --quiet           # just the summary line
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_ROOT = Path("C:/Users/atayl/Desktop/Excluded")
CACHE_EXTRACT = REPO_ROOT / ".cache" / "extracted"
MEMORY_DIR = Path.home() / ".claude/projects/C--Users-atayl-VoxCore/memory"
REPORT_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"

MEMORY_STALE_DAYS = 14
EXTRACTABLE_EXTS = {".pdf", ".docx", ".doc", ".eml", ".msg", ".md", ".txt", ".rtf"}

# Memory files that legitimately cite paths in Excluded/
MEMORY_CITATION_PATTERN = re.compile(r"`([A-Za-z_0-9][A-Za-z_0-9/\\. -]+?\.(?:md|pdf|docx|eml|txt|json))(?::\d+)?`")


def check_orphans() -> list[dict]:
    """Cache .txt files whose source no longer exists."""
    orphans = []
    if not CACHE_EXTRACT.exists():
        return orphans
    for bucket in CACHE_EXTRACT.iterdir():
        files_dir = bucket / "files"
        manifest_path = bucket / "manifest.json"
        if not (files_dir.exists() and manifest_path.exists()):
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        source_root = Path(manifest.get("source", ""))
        if not source_root.exists():
            # Entire bucket is orphaned
            orphans.append({
                "severity": "bucket-orphan",
                "bucket": bucket.name,
                "missing_source": str(source_root),
            })
            continue
        for entries_rel in manifest.get("entries", {}).keys():
            src = source_root / entries_rel
            if not src.exists():
                cache_sidecar = files_dir / (entries_rel + ".txt")
                orphans.append({
                    "severity": "file-orphan",
                    "bucket": bucket.name,
                    "source": str(src),
                    "cache": str(cache_sidecar) if cache_sidecar.exists() else None,
                })
    return orphans


def check_stale() -> list[dict]:
    """Source file mtime > extraction mtime."""
    stale = []
    if not CACHE_EXTRACT.exists():
        return stale
    for bucket in CACHE_EXTRACT.iterdir():
        manifest_path = bucket / "manifest.json"
        if not manifest_path.exists():
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        source_root = Path(manifest.get("source", ""))
        if not source_root.exists():
            continue
        for rel, entry in manifest.get("entries", {}).items():
            src = source_root / rel
            if not src.exists():
                continue
            try:
                src_mtime = src.stat().st_mtime
            except OSError:
                continue
            cached_mtime = entry.get("mtime", 0)
            if src_mtime > cached_mtime + 1:   # 1s tolerance
                stale.append({
                    "bucket": bucket.name,
                    "source": str(src),
                    "src_mtime": src_mtime,
                    "cached_mtime": cached_mtime,
                    "drift_sec": int(src_mtime - cached_mtime),
                })
    return stale


def check_missing() -> list[dict]:
    """Source files extractable-by-type but never extracted."""
    missing = []
    if not EXCLUDED_ROOT.exists():
        return missing
    # Walk IMPORTANT DOCS only — other top-level folders have different policies
    important = EXCLUDED_ROOT / "IMPORTANT DOCS"
    if not important.exists():
        return missing
    # Build set of source paths that ARE in a manifest
    indexed = set()
    for bucket in CACHE_EXTRACT.iterdir() if CACHE_EXTRACT.exists() else []:
        manifest_path = bucket / "manifest.json"
        if not manifest_path.exists():
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        source_root = Path(manifest.get("source", ""))
        for rel in manifest.get("entries", {}).keys():
            indexed.add(str((source_root / rel).resolve()).lower())

    for src in important.rglob("*"):
        if not src.is_file():
            continue
        if src.suffix.lower() not in EXTRACTABLE_EXTS:
            continue
        if str(src.resolve()).lower() not in indexed:
            missing.append({
                "source": str(src),
                "size": src.stat().st_size,
                "ext": src.suffix.lower(),
            })
    return missing


def check_duplicates() -> list[dict]:
    """Same content hash → multiple cache entries. Uses a cheap first-1MB sha256."""
    by_hash: dict[str, list[str]] = defaultdict(list)
    if not CACHE_EXTRACT.exists():
        return []
    for bucket in CACHE_EXTRACT.iterdir():
        files_dir = bucket / "files"
        if not files_dir.exists():
            continue
        for p in files_dir.rglob("*.txt"):
            if not p.is_file():
                continue
            try:
                with p.open("rb") as f:
                    content = f.read(1_048_576)   # first 1MB is enough
                h = hashlib.sha256(content).hexdigest()[:16]
            except Exception:
                continue
            by_hash[h].append(str(p))
    dups = []
    for h, paths in by_hash.items():
        if len(paths) > 1:
            dups.append({"sha": h, "paths": sorted(paths), "count": len(paths)})
    return dups


def check_memory_drift() -> list[dict]:
    """Memory topic files older than source-folder contents they summarize."""
    drifts = []
    if not MEMORY_DIR.exists():
        return drifts
    # Heuristic: any memory/*.md older than MEMORY_STALE_DAYS is flagged
    now = time.time()
    threshold = now - MEMORY_STALE_DAYS * 86400
    for m in MEMORY_DIR.rglob("*.md"):
        if not m.is_file():
            continue
        try:
            mtime = m.stat().st_mtime
        except OSError:
            continue
        if mtime < threshold:
            drifts.append({
                "memory_file": str(m),
                "age_days": round((now - mtime) / 86400, 1),
            })
    return drifts


def check_citation_breaks() -> list[dict]:
    """Memory files citing source paths that no longer exist."""
    breaks = []
    if not MEMORY_DIR.exists():
        return breaks
    for m in MEMORY_DIR.rglob("*.md"):
        try:
            text = m.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for match in MEMORY_CITATION_PATTERN.finditer(text):
            cited = match.group(1)
            # Try to resolve: maybe absolute, maybe relative to Excluded
            candidates = [
                Path(cited),
                EXCLUDED_ROOT / cited,
                EXCLUDED_ROOT / "IMPORTANT DOCS" / cited,
                EXCLUDED_ROOT / "IMPORTANT DOCS" / "Case_Reference" / cited,
            ]
            if not any(c.exists() for c in candidates):
                breaks.append({
                    "memory_file": str(m),
                    "broken_citation": cited,
                })
    return breaks


CHECKS = {
    "orphan": check_orphans,
    "stale": check_stale,
    "missing": check_missing,
    "duplicate": check_duplicates,
    "memory_drift": check_memory_drift,
    "citation_break": check_citation_breaks,
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="Emit JSON to stdout")
    ap.add_argument("--check", choices=sorted(CHECKS.keys()), help="Run only one check")
    ap.add_argument("--quiet", action="store_true", help="Only one-line summary")
    args = ap.parse_args()

    selected = {args.check: CHECKS[args.check]} if args.check else CHECKS

    results: dict[str, list] = {}
    for name, fn in selected.items():
        t0 = time.perf_counter()
        results[name] = fn()
        print(f"  check '{name}': {len(results[name])} issues ({time.perf_counter() - t0:.1f}s)", file=sys.stderr)

    # Write report
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    report_path = REPORT_DIR / f"excluded_lint_{ts}.json"
    report = {
        "timestamp": int(time.time()),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "checks_run": list(selected.keys()),
        "results": results,
        "counts": {k: len(v) for k, v in results.items()},
    }
    report_path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    elif args.quiet:
        totals = sum(len(v) for v in results.values())
        print(f"{totals} total issues. Report: {report_path}")
    else:
        print()
        print(f"## Excluded Lint — {report['date']}")
        print()
        print("| Check | Issues |")
        print("|-------|--------|")
        for name, items in results.items():
            print(f"| {name} | {len(items)} |")
        print()
        print(f"Full report: {report_path}")
        print()
        # Top examples per category (max 3 each)
        for name, items in results.items():
            if not items:
                continue
            print(f"### {name} (top 3)")
            for item in items[:3]:
                print(f"  {item}")
            if len(items) > 3:
                print(f"  ... and {len(items) - 3} more")
            print()

    total = sum(len(v) for v in results.values())
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

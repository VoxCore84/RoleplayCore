#!/usr/bin/env python3
"""Memory Control Plane v0.1 -- task -> memory context packet.

Given a task string, returns the most relevant memories with FRESHNESS,
SENSITIVITY, and CONFIDENCE flags + the source-of-truth hierarchy. Retrieval
NEVER asserts a memory is true -- it labels how much to trust it and whether to
verify first. v0.1 uses keyword / term-frequency scoring (arcanum MCP semantic
retrieval is a Later item); no external deps, degrades gracefully.

Usage:
  python tools/memory_context.py "task or question text" [--top 5] [--json]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from memory_schema import (  # noqa: E402
    parse_frontmatter, classify_sensitivity, memory_files, MEMORY_DIR,
)

_WORD = re.compile(r"[a-z0-9][a-z0-9_-]{2,}")
STOP = {"the", "and", "for", "with", "that", "this", "what", "how", "memory", "are", "was"}
STALE_DAYS = 90

HIERARCHY = [
    "1. Current user instruction",
    "2. Current repo/filesystem state",
    "3. Fresh source-of-truth check",
    "4. Verified memory (last_verified real + within TTL)",
    "5. Provisional / stale memory (last_touched only, or aged)",
    "6. Archived / historical memory",
]


def _age(datestr: str, today: dt.date):
    try:
        return (today - dt.date.fromisoformat(datestr)).days
    except (ValueError, TypeError):
        return None


def freshness(fm: dict | None, today: dt.date) -> tuple[str, int]:
    """(verdict, source-of-truth tier). Honest: a real last_verified is tier 4;
    mtime-seeded last_touched is tier 5 (provisional); no frontmatter is tier 6."""
    if not fm:
        return "unknown provenance (no frontmatter)", 6
    lv, vm, lt = fm.get("last_verified", ""), fm.get("verification_method", ""), fm.get("last_touched", "")
    if lv and vm and vm != "unverified_backfill":
        a = _age(lv, today)
        return (f"VERIFIED {a}d ago", 4) if a is not None else ("verified (undated)", 4)
    a = _age(lt, today)
    if a is None:
        return "provisional, unverified (undated)", 5
    if a > STALE_DAYS:
        return f"STALE + unverified ({a}d since touch)", 5
    return f"provisional, unverified ({a}d since touch)", 5


def _score(tokens, path: Path, fm: dict | None) -> int:
    text = path.read_text(encoding="utf-8", errors="replace").lower()
    name = path.name.lower()
    desc = (fm.get("description", "") if fm else "").lower()
    s = 0
    for t in tokens:
        s += text.count(t) + 5 * name.count(t) + 3 * desc.count(t)
    return s


def build_packet(task: str, top: int) -> list[dict]:
    today = dt.date.today()
    tokens = {t for t in _WORD.findall(task.lower()) if t not in STOP}
    out = []
    for p in memory_files():
        fm = parse_frontmatter(p)
        sc = _score(tokens, p, fm)
        if sc <= 0:
            continue
        sens = classify_sensitivity(p, fm)
        verdict, tier = freshness(fm, today)
        out.append({
            "file": p.relative_to(MEMORY_DIR).as_posix(),
            "score": sc, "sensitivity": sens,
            "confidence": (fm.get("confidence") if fm else None) or "(none)",
            "freshness": verdict, "sot_tier": tier,
            "verify_before_use": sens == "restricted" or (fm or {}).get("verify_before_use") == "true",
        })
    out.sort(key=lambda r: -r["score"])
    return out[:top]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("task", help="task or question text")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    packet = build_packet(args.task, args.top)
    if args.json:
        print(json.dumps({"task": args.task, "packet": packet}, indent=2))
        return 0

    print(f"[memory-context] task: {args.task!r}")
    print("source-of-truth hierarchy (trust order; memory is tiers 4-6, NEVER assume true):")
    for h in HIERARCHY:
        print(f"  {h}")
    if not packet:
        print("\n  no relevant memories matched -- fall back to tiers 1-3 (ask / read files / verify).")
        return 0
    print(f"\n  top {len(packet)} relevant memories (apply the per-item flags before relying on them):")
    for r in packet:
        vbu = "  [VERIFY BEFORE USE]" if r["verify_before_use"] else ""
        print(f"  - {r['file']}  (score {r['score']}, tier {r['sot_tier']}, {r['sensitivity']}, conf={r['confidence']})")
        print(f"      freshness: {r['freshness']}{vbu}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

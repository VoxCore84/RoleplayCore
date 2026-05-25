#!/usr/bin/env python3
"""Memory Control Plane v0.1 -- closed-loop fix PROPOSALS (dry-run, never applies).

Detects issues (schema gaps via memory_schema + drift via memory_staleness) and
emits risk-classified patch PROPOSALS with evidence + an approval requirement.
It NEVER mutates files in v0.1 (propose-only). Safety gate: a LOW-class change to
a `restricted` (legal/medical/financial/identity) file is ESCALATED to require
human approval; HIGH-risk files never auto-apply.

Closed loop: detect -> propose (evidence + risk) -> [human approves] -> apply.
Only the first two steps run in v0.1.

Usage:
  python tools/memory_fix_proposals.py            # dry-run report
  python tools/memory_fix_proposals.py --json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import memory_schema as ms          # noqa: E402
import memory_staleness as mstale   # noqa: E402


def _effective_risk(change_class: str, file_sensitivity: str) -> tuple[str, bool]:
    """Escalate by file sensitivity. Returns (effective_risk, approval_required).
    A LOW change to a restricted file becomes HIGH + approval-required."""
    if file_sensitivity == "restricted":
        return "HIGH", True
    if change_class == "LOW":
        return "LOW", False
    return "MEDIUM", True


def _add(out, file, sens, issue, change, evidence, change_class="LOW"):
    er, appr = _effective_risk(change_class, sens)
    out.append({
        "file": file, "issue": issue, "proposed_change": change, "evidence": evidence,
        "change_class": change_class, "file_sensitivity": sens,
        "effective_risk": er, "approval_required": appr, "auto_applicable": not appr,
    })


def build_proposals() -> list[dict]:
    out: list[dict] = []
    # 1. Schema-gap proposals (additive frontmatter)
    for p in ms.memory_files():
        v = ms.validate_file(p)
        if not v.get("frontmatter"):
            continue
        sens = v["sensitivity"]
        if "schema_version" in v["missing_required"]:
            _add(out, v["file"], sens, "missing schema_version",
                 f"add `schema_version: {ms.SCHEMA_VERSION}` to frontmatter",
                 "memory_schema: required field absent")
        if "sensitivity" in v["missing_required"]:
            _add(out, v["file"], sens, "missing sensitivity",
                 f"add `sensitivity: {sens}` (inferred from filename; CONFIRM before applying)",
                 f"memory_schema: inferred = {sens}")
    # 2. Drift proposals (broken references) from the staleness sweep
    for r in mstale.collect(mstale.DEFAULT_STALE_DAYS):
        for ref in r.get("broken_refs", []):
            p = ms.MEMORY_DIR / r["file"]
            sens = ms.classify_sensitivity(p, ms.parse_frontmatter(p))
            _add(out, r["file"], sens, f"broken reference `{ref}`",
                 f"verify, then repair or remove dead reference `{ref}`",
                 "memory_staleness: target does not exist")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--apply-low", action="store_true",
                    help="(DISABLED in v0.1 -- propose-only) would apply LOW non-restricted proposals")
    args = ap.parse_args()

    props = build_proposals()
    if args.json:
        print(json.dumps(props, indent=2))
        return 0

    by_risk = Counter(p["effective_risk"] for p in props)
    auto = [p for p in props if p["auto_applicable"]]
    appr = [p for p in props if p["approval_required"]]
    print(f"[memory-fix-proposals] {len(props)} proposals (DRY-RUN -- nothing applied)")
    print(f"  by effective risk: {dict(by_risk)}")
    print(f"  auto-applicable (LOW, non-restricted): {len(auto)} | approval-required: {len(appr)}")

    print("\n  sample auto-applicable (LOW, non-restricted -- safe to apply behind an explicit flag):")
    for p in auto[:3]:
        print(f"    - {p['file']}: {p['issue']} -> {p['proposed_change']}")
    print("\n  sample approval-required (HIGH / restricted -- human + evidence, NEVER auto):")
    for p in [x for x in appr if x["effective_risk"] == "HIGH"][:3]:
        print(f"    - {p['file']} [{p['file_sensitivity']}]: {p['issue']}")

    if args.apply_low:
        print("\n  --apply-low is DISABLED in v0.1 (propose-only). No changes made.")
    print("\n  closed loop: detect -> propose -> [human approves] -> apply (apply step deferred past v0.1)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

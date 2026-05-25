#!/usr/bin/env python3
"""Memory Control Plane v0.1 -- schema definition + dry-run validator.

Defines the progressive frontmatter schema for the memory corpus and reports
which files satisfy it. NEVER edits files -- it reports gaps; mutations are
proposed by memory_fix_proposals.py (dry-run, human-approved). Shared helpers
(parse_frontmatter, classify_sensitivity, risk_for) are imported by
memory_context.py and memory_fix_proposals.py.

Usage:
  python tools/memory_schema.py            # dry-run validation report
  python tools/memory_schema.py --json     # machine-readable
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MEMORY_DIR = Path(r"C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory")
SCHEMA_VERSION = 1

REQUIRED_NOW = ["schema_version", "name", "description", "type", "sensitivity",
                "confidence", "last_touched", "verification_method"]
OPTIONAL = ["last_verified", "verify_before_use", "source_of_truth", "ttl_days",
            "owner", "subsystem", "supersedes", "superseded_by", "allowed_export",
            "risk_level", "related_tasks"]

# Filename-based sensitivity inference (SUGGESTION only -- never auto-applied).
_RESTRICTED = re.compile(r"^(case-|mh-records|dossier_|angel-va|finances|resume|ides|va-)", re.I)
# Files with no frontmatter by design -- not schema-validated.
SKIP_NAMES = {"MEMORY.md"}

_KEY_RE = re.compile(r"^\s*([A-Za-z_][\w]*):\s*(.*)$")


def parse_frontmatter(path: Path) -> dict | None:
    """Return {key: raw_value} for the frontmatter block (captures both top-level
    keys AND keys nested under `metadata:`, flattened), or None if no frontmatter."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fm: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = _KEY_RE.match(line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def classify_sensitivity(path: Path, fm: dict | None) -> str:
    """restricted / internal / public. Explicit frontmatter wins; else inferred
    from filename. Suggestion only -- never written without approval."""
    if fm and fm.get("sensitivity"):
        return fm["sensitivity"]
    if _RESTRICTED.search(path.name):
        return "restricted"
    return "internal"


def risk_for(path: Path, fm: dict | None) -> str:
    """Mutation-risk gate for a file. restricted sensitivity -> HIGH (legal/
    medical/financial/identity; human approval + evidence, never auto-apply).
    Everything else -> MEDIUM (review) by default."""
    return "HIGH" if classify_sensitivity(path, fm) == "restricted" else "MEDIUM"


def memory_files() -> list[Path]:
    return sorted(p for p in MEMORY_DIR.rglob("*.md")
                  if "archive" not in p.relative_to(MEMORY_DIR).parts
                  and p.name not in SKIP_NAMES)


def validate_file(path: Path) -> dict:
    fm = parse_frontmatter(path)
    rel = path.relative_to(MEMORY_DIR).as_posix()
    if fm is None:
        return {"file": rel, "frontmatter": False, "missing_required": ["(no frontmatter)"],
                "sensitivity": classify_sensitivity(path, None), "schema_clean": False}
    present = set(fm)
    if "memory_type" in present:
        present.add("type")
    missing = [f for f in REQUIRED_NOW if f not in present]
    return {
        "file": rel,
        "frontmatter": True,
        "missing_required": missing,
        "has_optional": [f for f in OPTIONAL if f in present],
        "sensitivity": classify_sensitivity(path, fm),
        "confidence": fm.get("confidence", "(none)"),
        "schema_clean": not missing,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    results = [validate_file(p) for p in memory_files()]
    if args.json:
        print(json.dumps(results, indent=2))
        return 0

    clean = [r for r in results if r.get("schema_clean")]
    print(f"[memory-schema v{SCHEMA_VERSION}] {len(results)} files scanned, "
          f"{len(clean)} schema-clean, {len(results) - len(clean)} with gaps")
    print(f"  required-now: {', '.join(REQUIRED_NOW)}")
    # Most-common missing fields (the corpus-wide gap)
    from collections import Counter
    miss = Counter(f for r in results for f in r.get("missing_required", []))
    if miss:
        print("  missing-field frequency:")
        for field, n in miss.most_common():
            print(f"    {field}: {n}")
    # Restricted files (sensitivity gate) -- these need verify_before_use + HIGH-risk mutation gate
    restricted = [r for r in results if r["sensitivity"] == "restricted"]
    print(f"\n  restricted-sensitivity files ({len(restricted)}) -- mutations are HIGH-risk (approval+evidence):")
    for r in restricted[:15]:
        print(f"    - {r['file']}")
    if len(restricted) > 15:
        print(f"    ... +{len(restricted) - 15} more")
    print("\n  (dry-run report only -- no files edited. Use memory_fix_proposals.py to propose patches.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

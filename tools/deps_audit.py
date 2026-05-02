"""Audit requirements.txt files for unpinned versions.

A pinned version is one of:
  pkg==1.2.3                 (exact)
  pkg==1.2.3 ; python<"3.11" (exact + marker)

NOT pinned:
  pkg                        (any version)
  pkg>=1.0.0                 (range)
  pkg~=1.2                   (compatible-release)
  pkg<2.0                    (upper-bound only)

Reproducibility blocker: any non-pinned line means a re-install on a clean
machine could pull a different version. For acquihire diligence, pin all.

Usage:
    python tools/deps_audit.py
    python tools/deps_audit.py --fix       # write a pinned variant alongside each file
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


PIN_RE = re.compile(r"^([A-Za-z0-9_.\-]+)\s*([<>=!~]+)?\s*([A-Za-z0-9_.\-+]+)?")


def parse_requirement(line: str) -> tuple[str | None, str | None, str | None]:
    """Return (name, op, version) or (None, None, None) if not a requirement."""
    line = line.split("#", 1)[0].strip()
    if not line or line.startswith("-"):
        return (None, None, None)
    spec = line.split(";", 1)[0].strip()  # strip env marker
    m = PIN_RE.match(spec)
    if not m:
        return (None, None, None)
    return (m.group(1), m.group(2) or "", m.group(3) or "")


def is_pinned(op: str) -> bool:
    return op == "=="


def installed_version(pkg: str) -> str | None:
    try:
        out = subprocess.check_output(
            [sys.executable, "-m", "pip", "show", pkg],
            encoding="utf-8", errors="replace", stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None
    for line in out.splitlines():
        if line.lower().startswith("version:"):
            return line.split(":", 1)[1].strip()
    return None


def audit_file(path: Path) -> dict:
    findings: list[dict] = []
    pinned: list[dict] = []
    for i, raw_line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        name, op, ver = parse_requirement(line)
        if not name:
            continue
        record = {"line": i, "raw": raw_line, "package": name, "op": op, "spec_version": ver}
        if is_pinned(op):
            pinned.append(record)
        else:
            record["installed_version"] = installed_version(name)
            findings.append(record)
    return {"file": str(path.relative_to(REPO_ROOT)), "pinned": pinned, "unpinned": findings}


def write_pinned_variant(audit: dict) -> Path | None:
    """Write a {file}.pinned.txt with == versions where we know them."""
    p = REPO_ROOT / audit["file"]
    out = p.with_suffix(".pinned.txt")
    lines = [f"# Auto-pinned variant generated {time.strftime('%Y-%m-%d %H:%M:%S')}",
             f"# Source: {audit['file']}",
             ""]
    skipped = []
    for rec in audit["pinned"]:
        lines.append(rec["raw"])
    for rec in audit["unpinned"]:
        installed = rec.get("installed_version")
        if installed:
            lines.append(f"{rec['package']}=={installed}")
        else:
            lines.append(f"# UNRESOLVED: {rec['raw']}")
            skipped.append(rec["package"])
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fix", action="store_true", help="Write .pinned.txt alongside each requirements file")
    p.add_argument("--output", help="Write JSON summary to this path")
    args = p.parse_args()

    files = sorted(REPO_ROOT.glob("**/requirements.txt"))
    files = [f for f in files if not any(part in f.parts for part in (".venv", "venv", "node_modules", ".cache", ".git", "out", "dist"))]

    results = [audit_file(f) for f in files]
    total_pinned = sum(len(r["pinned"]) for r in results)
    total_unpinned = sum(len(r["unpinned"]) for r in results)

    print(f"Audited {len(results)} requirements files: {total_pinned} pinned, {total_unpinned} unpinned")
    print()
    for r in results:
        if not r["unpinned"]:
            print(f"  PASS  {r['file']}  ({len(r['pinned'])} pinned)")
            continue
        print(f"  FAIL  {r['file']}  ({len(r['pinned'])} pinned, {len(r['unpinned'])} unpinned)")
        for rec in r["unpinned"]:
            inst = rec.get("installed_version") or "NOT INSTALLED"
            print(f"          line {rec['line']}: {rec['package']}{rec['op'] or ''}{rec['spec_version'] or ''}  (installed: {inst})")

    if args.fix:
        print("\n[--fix] writing .pinned.txt variants...")
        for r in results:
            out = write_pinned_variant(r)
            print(f"  -> {out.relative_to(REPO_ROOT)}")

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps({
            "elapsed": 0,
            "files": results,
            "totals": {"pinned": total_pinned, "unpinned": total_unpinned},
        }, indent=2), encoding="utf-8")
        print(f"\n[output] {args.output}")

    return 1 if total_unpinned > 0 else 0


if __name__ == "__main__":
    sys.exit(main())

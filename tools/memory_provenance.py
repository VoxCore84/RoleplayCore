#!/usr/bin/env python3
"""Memory provenance -- HONEST last_touched / verification frontmatter.

Ensures each memory file carries truthful provenance:
  - last_touched:        <date>   filesystem mtime -- a real, factual signal
  - verification_method: <how>    `unverified_backfill` until a real check runs
  - confidence:          <level>  `provisional` until verified

It deliberately does NOT set `last_verified`. A modification time is not a
verification event; conflating them manufactures false confidence -- the exact
failure this corpus exists to avoid. Only a real check (repo-path validation,
source re-read, manual review) may set `last_verified`, and that is the
staleness sweep's job, not this backfill's.

Per file, idempotent (one of):
  - has `last_touched`             -> already honest, skip
  - has legacy `last_verified`     -> MIGRATE: rename to last_touched + annotate
  - has frontmatter, no provenance -> BACKFILL: add last_touched (mtime) + annotate
  - no frontmatter (MEMORY.md ...) -> skip, never fabricate

Usage:
  python tools/memory_provenance.py --dry-run     # show what would change
  python tools/memory_provenance.py               # apply
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

MEMORY_DIR = Path(r"C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory")

_LV_RE = re.compile(r"^(?P<indent>[ \t]*)last_verified:\s*(?P<date>\d{4}-\d{2}-\d{2})")
_LT_RE = re.compile(r"^[ \t]*last_touched:")
_VM_RE = re.compile(r"^[ \t]*verification_method:")
_CONF_RE = re.compile(r"^[ \t]*confidence:")


def mtime_date(p: Path) -> str:
    return dt.date.fromtimestamp(p.stat().st_mtime).isoformat()


def _close_fence(lines: list[str]) -> int | None:
    """Index of the closing '---' frontmatter fence, or None if no frontmatter."""
    if not lines or lines[0].rstrip("\r\n") != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            return i
    return None


def process(path: Path, apply: bool) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    close = _close_fence(lines)
    if close is None:
        return "no_frontmatter"

    head, fm, body = lines[:1], lines[1:close], lines[close:]
    if any(_LT_RE.match(l) for l in fm):
        return "already"

    nl = "\r\n" if (lines[0].endswith("\r\n")) else "\n"

    # Locate a legacy last_verified line (top-level or nested).
    lv_idx, indent, date = None, "", None
    for i, l in enumerate(fm):
        m = _LV_RE.match(l)
        if m:
            lv_idx, indent, date = i, m.group("indent"), m.group("date")
            break

    if lv_idx is not None:
        status = "migrated"
    else:
        status = "backfilled"
        indent, date = "", mtime_date(path)

    if not apply:
        return status

    if lv_idx is not None:
        fm[lv_idx] = f"{indent}last_touched: {date}{nl}"
        anchor = lv_idx
    else:
        fm.append(f"{indent}last_touched: {date}{nl}")
        anchor = len(fm) - 1

    additions = []
    if not any(_VM_RE.match(l) for l in fm):
        additions.append(f"{indent}verification_method: unverified_backfill{nl}")
    if not any(_CONF_RE.match(l) for l in fm):
        additions.append(f"{indent}confidence: provisional{nl}")
    fm[anchor + 1:anchor + 1] = additions

    path.write_text("".join(head + fm + body), encoding="utf-8")
    return status


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="show changes without writing")
    ap.add_argument("--dir", default=str(MEMORY_DIR))
    args = ap.parse_args()

    root = Path(args.dir)
    apply = not args.dry_run
    counts: dict[str, list[str]] = {
        "migrated": [], "backfilled": [], "already": [], "no_frontmatter": [],
    }
    for p in sorted(root.rglob("*.md")):
        counts[process(p, apply)].append(p.relative_to(root).as_posix())

    verb = "APPLIED" if apply else "DRY-RUN"
    print(f"[{verb}] honest memory provenance in {root}")
    print(f"  migrated (last_verified -> last_touched + annotate): {len(counts['migrated'])}")
    print(f"  backfilled (added last_touched from mtime):          {len(counts['backfilled'])}")
    print(f"  already honest (has last_touched):                   {len(counts['already'])}")
    print(f"  skipped (no frontmatter):                            {len(counts['no_frontmatter'])}")
    if counts["no_frontmatter"]:
        print("  no-frontmatter files (left untouched):")
        for f in counts["no_frontmatter"]:
            print(f"    - {f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Memory provenance backfill -- adds `last_verified` frontmatter to memory files.

Seeds `last_verified` from each file's filesystem mtime. This is the best signal
available at backfill time: we treat last-modification as the last point the
content was known-good. The future staleness sweep updates this with real
verification dates as it re-checks each memory against current sources.

Idempotent: only inserts the key when a frontmatter block already exists and the
key is absent. Files without frontmatter (e.g. MEMORY.md, which must stay
frontmatter-free) are skipped, never fabricated.

Usage:
  python tools/memory_provenance.py --dry-run     # show what would change
  python tools/memory_provenance.py               # apply
"""
from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

MEMORY_DIR = Path(r"C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory")
KEY = "last_verified"


def mtime_date(p: Path) -> str:
    return dt.date.fromtimestamp(p.stat().st_mtime).isoformat()


def process(path: Path, apply: bool) -> str:
    """Return one of: updated / has_key / no_frontmatter."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return "no_frontmatter"

    lines = text.splitlines(keepends=True)
    close_idx = None
    for i in range(1, len(lines)):
        if lines[i].rstrip("\r\n") == "---":
            close_idx = i
            break
    if close_idx is None:
        return "no_frontmatter"

    block = lines[1:close_idx]
    if any(l.split(":", 1)[0].strip() == KEY for l in block):
        return "has_key"

    if apply:
        newline = "\r\n" if lines[0].endswith("\r\n") else "\n"
        lines.insert(close_idx, f"{KEY}: {mtime_date(path)}{newline}")
        path.write_text("".join(lines), encoding="utf-8")
    return "updated"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="show changes without writing")
    ap.add_argument("--dir", default=str(MEMORY_DIR), help="memory directory")
    args = ap.parse_args()

    root = Path(args.dir)
    apply = not args.dry_run
    counts: dict[str, list[str]] = {"updated": [], "has_key": [], "no_frontmatter": []}

    for p in sorted(root.rglob("*.md")):
        status = process(p, apply)
        counts[status].append(p.relative_to(root).as_posix())

    verb = "APPLIED" if apply else "DRY-RUN"
    print(f"[{verb}] memory provenance backfill in {root}")
    print(f"  updated (last_verified added): {len(counts['updated'])}")
    print(f"  already had key:               {len(counts['has_key'])}")
    print(f"  skipped (no frontmatter):      {len(counts['no_frontmatter'])}")
    if counts["no_frontmatter"]:
        print("  no-frontmatter files (left untouched):")
        for f in counts["no_frontmatter"]:
            print(f"    - {f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

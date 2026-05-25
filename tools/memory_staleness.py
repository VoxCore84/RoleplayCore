#!/usr/bin/env python3
"""Mechanical memory staleness + drift detector. No LLM. Fast. Silent on clean.

Scans the Claude Code memory corpus and flags, per file:
  - BROKEN REF (hard): a markdown .md link or a repo-relative path
    (`tools/`, `.claude/`, `src/`, ...) that no longer exists on disk.
  - STALE (soft): days since `last_verified` (or mtime if absent) >= threshold.
  - UNRESOLVED [[wikilink]] (soft): may be an intentional forward-reference.

It deliberately does NOT judge whether prose claims still hold -- that semantic
call is deferred to in-session Claude (Opus, already loaded) reading the flagged
file. This keeps the sweep instant, free, and deterministic, so it can run at
every session start like deadline-alert.py.

Output: compact report to stdout, ONLY if there are findings. Silent (exit 0)
when the corpus is healthy. Path checks are conservative -- a false "missing"
that cries wolf is worse than a miss, so only high-confidence path shapes are
checked (repo-relative roots + sibling .md links; template/glob/abs/personal
paths are skipped).

Usage:
  python tools/memory_staleness.py                 # report (silent if clean)
  python tools/memory_staleness.py --all           # include healthy summary
  python tools/memory_staleness.py --stale-days 60 # override age threshold (default 90)
  python tools/memory_staleness.py --json          # machine-readable
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

MEMORY_DIR = Path(r"C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory")
VOXCORE_ROOT = Path(r"C:\Users\atayl\VoxCore")
DEFAULT_STALE_DAYS = 90

# VoxCore-owned, current, stable roots only. Deliberately EXCLUDES migrated roots
# (src/, sql/, doc/ -> CalmCore after the repo split) and high-churn roots
# (AI_Studio/ reports get archived/deleted constantly). Checking those produced
# 300+ false "missing" hits on historical references -- worse than useless.
REPO_ROOTS = ("tools/", "tools-dev/", ".claude/")
# Tokens containing any of these are templates/globs/non-paths -> never checked.
SKIP_MARKERS = ("<", ">", "*", "$", "..", "://", "YYYY", " ", "\t", "{", "}")

_LINK_RE = re.compile(r"\]\(([^)]+)\)")          # markdown link target
_BACKTICK_RE = re.compile(r"`([^`]+)`")           # `code`/`path`
_WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")    # [[name]]
# Match last_verified whether top-level or nested under a `metadata:` block --
# the Claude Code memory canonicalizer rewrites new files into the nested form.
_VERIFIED_RE = re.compile(r"^\s*last_verified:\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)


def age_days(path: Path, text: str, today: dt.date) -> tuple[int, str]:
    """Return (age_in_days, basis) where basis is 'last_verified' or 'mtime'."""
    head = text[:600]
    m = _VERIFIED_RE.search(head)
    if m:
        try:
            base = dt.date.fromisoformat(m.group(1))
            return (today - base).days, "last_verified"
        except ValueError:
            pass
    base = dt.date.fromtimestamp(path.stat().st_mtime)
    return (today - base).days, "mtime"


def _repo_path(token: str) -> Path | None:
    """Resolve a token to a VoxCore-owned repo path worth existence-checking,
    or None. High precision: only tools/, tools-dev/, .claude/ roots."""
    t = token.strip().strip("`").replace("\\", "/")
    if not t or any(mark in t for mark in SKIP_MARKERS):
        return None
    t = re.sub(r":\d+(?:-\d+)?$", "", t)  # strip line-citation suffix (foo.py:998)
    for pre in ("c:/users/atayl/voxcore/", "voxcore/"):
        if t.lower().startswith(pre):
            t = t[len(pre):]
            break
    if t.startswith(REPO_ROOTS):
        return VOXCORE_ROOT / t
    return None


def _sibling_md(token: str, current_file: Path) -> Path | None:
    """Resolve a bare `X.md` to a sibling memory file, or None. Only meaningful
    for markdown LINK targets (intentional cross-refs) -- not backtick prose
    mentions, which are usually external document filenames, not memory links."""
    t = re.sub(r":\d+(?:-\d+)?$", "", token.strip())
    if not t.endswith(".md") or "/" in t or "\\" in t or len(t) <= 3:
        return None
    if any(mark in t for mark in SKIP_MARKERS):
        return None
    return current_file.parent / t


def scan_file(path: Path, today: dt.date, memory_names: set[str]) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(MEMORY_DIR).as_posix()
    age, basis = age_days(path, text, today)

    broken: list[str] = []
    seen: set[str] = set()
    # Markdown links: intentional cross-refs -> check repo paths AND sibling .md.
    for tok in _LINK_RE.findall(text):
        if tok in seen:
            continue
        seen.add(tok)
        resolved = _repo_path(tok) or _sibling_md(tok, path)
        if resolved is not None and not resolved.exists():
            broken.append(tok.strip().strip("`"))
    # Backtick mentions: repo paths only (prose filenames are not memory links).
    for tok in _BACKTICK_RE.findall(text):
        if tok in seen:
            continue
        seen.add(tok)
        resolved = _repo_path(tok)
        if resolved is not None and not resolved.exists():
            broken.append(tok.strip().strip("`"))

    unresolved: list[str] = []
    for tok in _WIKILINK_RE.findall(text):
        name = tok.split("|")[0].split("#")[0].strip()
        if name and name.lower() not in memory_names:
            unresolved.append(name)

    return {
        "file": rel,
        "age_days": age,
        "age_basis": basis,
        "broken_refs": sorted(set(broken)),
        "unresolved_links": sorted(set(unresolved)),
    }


def collect(stale_days: int) -> list[dict]:
    today = dt.date.today()
    # Skip archive/ (deprecated snapshots) and append-only historical LOGS. Both
    # reference CalmCore-migrated code and long-gone tools by design -- they are
    # records, not live guidance, so a broken ref in them is expected, not drift.
    skip_files = {"recent-work.md", "improvements.md", "improvements-archive.md"}
    files = sorted(f for f in MEMORY_DIR.rglob("*.md")
                   if "archive" not in f.relative_to(MEMORY_DIR).parts
                   and f.name not in skip_files)
    # Build the set of resolvable memory names: filename stems + frontmatter name: slugs.
    memory_names: set[str] = set()
    for f in files:
        memory_names.add(f.stem.lower())
        head = f.read_text(encoding="utf-8", errors="replace")[:600]
        nm = re.search(r"^name:\s*(.+)$", head, re.MULTILINE)
        if nm:
            memory_names.add(nm.group(1).strip().lower())
    return [scan_file(f, today, memory_names) for f in files]


def render(results: list[dict], stale_days: int, show_all: bool) -> str:
    broken = [r for r in results if r["broken_refs"]]
    stale = sorted([r for r in results if r["age_days"] >= stale_days],
                   key=lambda r: -r["age_days"])
    unresolved = [r for r in results if r["unresolved_links"]]

    if not broken and not stale and not show_all:
        return ""  # silent: healthy

    lines = ["[memory-health] mechanical sweep -- judge prose drift when you open a flagged file"]

    if broken:
        total = sum(len(r["broken_refs"]) for r in broken)
        lines.append(f"\nBROKEN REFERENCES ({total} in {len(broken)} file(s)):")
        for r in broken[:12]:
            for ref in r["broken_refs"][:6]:
                lines.append(f"  - {r['file']} -> `{ref}` (missing)")
        if len(broken) > 12:
            lines.append(f"  ... +{len(broken) - 12} more file(s)")

    if stale:
        oldest = ", ".join(f"{r['file']} ({r['age_days']}d)" for r in stale[:5])
        lines.append(f"\nSTALE (>={stale_days}d unverified): {len(stale)} file(s)")
        lines.append(f"  oldest: {oldest}")

    if unresolved:
        total = sum(len(r["unresolved_links"]) for r in unresolved)
        names = sorted({n for r in unresolved for n in r["unresolved_links"]})
        lines.append(f"\nUNRESOLVED [[links]] ({total}, may be intentional forward-refs): "
                     + ", ".join(names[:10]))

    if show_all:
        healthy = len(results) - len(broken) - len({r["file"] for r in stale})
        lines.append(f"\nScanned {len(results)} files. ~{max(healthy, 0)} clean.")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--all", action="store_true", help="include healthy summary")
    ap.add_argument("--stale-days", type=int, default=DEFAULT_STALE_DAYS)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if not MEMORY_DIR.exists():
        return 0

    results = collect(args.stale_days)

    if args.json:
        print(json.dumps(results, indent=2))
        return 0

    report = render(results, args.stale_days, args.all)
    if report:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

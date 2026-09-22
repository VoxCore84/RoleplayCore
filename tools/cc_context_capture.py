#!/usr/bin/env python3
"""cc_context_capture.py — measure Claude Code's per-turn context from a fresh headless session.

Runs `claude -p "/context"` through PowerShell (Git Bash rewrites the leading slash into a
path — see tasks/lessons.md 2026-09-22), saves the full output under
AI_Studio/Reports/context_captures/<timestamp>_<label>.md, prints the category table, and
optionally diffs the totals against an earlier capture. This is the only trustworthy way to
claim "saves N tokens": compare the TOTAL of two captures of the shipped state.

Usage:
    python tools/cc_context_capture.py --label before
    python tools/cc_context_capture.py --label after --diff AI_Studio/Reports/context_captures/<before>.md
    python tools/cc_context_capture.py --file <existing_capture>.md --diff <other>.md   # parse only, no new session
"""
from __future__ import annotations

import argparse
import datetime
import os
import pathlib
import re
import shutil
import subprocess
import sys

DEFAULT_DIR = pathlib.Path("AI_Studio/Reports/context_captures")


def run_capture(timeout: int = 300) -> str:
    env = dict(os.environ)
    env.pop("CLAUDECODE", None)               # allow a nested session
    env.pop("CLAUDE_CODE_CHILD_SESSION", None)
    shell = shutil.which("pwsh") or shutil.which("powershell")
    if not shell:
        sys.exit("PowerShell not found; run claude -p \"/context\" from a PowerShell window instead")
    cmd = [shell, "-NoProfile", "-Command", 'claude -p "/context" --output-format text']
    r = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=timeout,
                       encoding="utf-8", errors="replace")
    return (r.stdout or "") + (r.stderr or "")


def parse(text: str) -> tuple[str, dict[str, str]]:
    m = re.search(r"\*\*Tokens:\*\*\s*([\d.]+k?)", text)
    total = m.group(1) if m else "?"
    cats: dict[str, str] = {}
    in_table = False
    for line in text.splitlines():
        if line.startswith("### Estimated usage by category"):
            in_table = True
            continue
        if in_table and line.startswith("### "):
            break
        mm = re.match(r"\|\s*([^|]+?)\s*\|\s*([\d.]+k?|\d+)\s*\|\s*[\d.]+%\s*\|", line)
        if in_table and mm:
            cats[mm.group(1)] = mm.group(2)
    return total, cats


def tok(s: str) -> float:
    s = s.strip().lower()
    return float(s[:-1]) * 1000 if s.endswith("k") else float(s)


def fmt(n: float, signed: bool = False) -> str:
    sign = ("+" if n > 0 else "") if signed else ""
    return f"{sign}{n/1000:.1f}k" if abs(n) >= 1000 else f"{sign}{n:.0f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="capture")
    ap.add_argument("--diff", help="earlier capture file to compare against")
    ap.add_argument("--out", default=str(DEFAULT_DIR))
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--file", help="parse an existing capture instead of running a new one")
    args = ap.parse_args()

    text = pathlib.Path(args.file).read_text(encoding="utf-8") if args.file else run_capture(args.timeout)
    total, cats = parse(text)
    if total == "?":
        print(text[:1500])
        sys.exit("could not find the /context table in the output above")

    if args.file:
        print(f"parsed {args.file}")
    else:
        out_dir = pathlib.Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        out = out_dir / f"{stamp}_{args.label}.md"
        out.write_text(text, encoding="utf-8")
        print(f"saved {out}")
    print(f"TOTAL live: {total}")
    prev_total, prev = ("", {})
    if args.diff:
        prev_total, prev = parse(pathlib.Path(args.diff).read_text(encoding="utf-8"))
        print(f"vs {args.diff}: {prev_total} -> {total} ({fmt(tok(total) - tok(prev_total), signed=True)})")
    print(f"{'Category':34s} {'now':>8s} {'prev':>8s} {'delta':>8s}")
    for k, v in cats.items():
        d = f"{fmt(tok(v) - tok(prev[k]), signed=True):>8}" if k in prev else ""
        print(f"{k:34s} {v:>8s} {prev.get(k, ''):>8s} {d}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

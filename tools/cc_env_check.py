#!/usr/bin/env python3
"""cc_env_check.py — prove each settings key is one the installed Claude Code binary can read.

For every `env` key and every top-level key in ~/.claude/settings.json (plus any --also names),
count occurrences of the exact string inside claude.exe. A count of 0 is decisive: the code
cannot read that name, so the setting is dead or misspelled (this is how the
CLAUDE_CODE_AUTOCOMPACT_PCT_OVERRIDE no-op was caught on 2026-09-22 after a truncated docs page
had misled two earlier passes). A positive count only proves the string exists, not that the
setting is honoured on your model or plan — treat "undocumented" as "unverified", not "dead".

Usage:
    python tools/cc_env_check.py
    python tools/cc_env_check.py --also CLAUDE_AUTOCOMPACT_PCT_OVERRIDE CLAUDE_CODE_FORK_SUBAGENT
    python tools/cc_env_check.py --settings path/to/settings.json --binary path/to/claude.exe
Exit code 1 if any checked name has 0 hits.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shutil
import sys

SKIP_TOPLEVEL = {"env", "permissions", "hooks", "statusLine", "enabledPlugins", "skillOverrides"}


def find_binary() -> pathlib.Path | None:
    p = os.environ.get("CLAUDE_CODE_EXECPATH")
    if p and pathlib.Path(p).exists():
        return pathlib.Path(p)
    shim = shutil.which("claude")
    if shim:
        cand = pathlib.Path(shim).resolve().parent / "node_modules" / "@anthropic-ai" / "claude-code" / "bin" / "claude.exe"
        if cand.exists():
            return cand
    npm = pathlib.Path(os.environ.get("APPDATA", "")) / "npm" / "node_modules" / "@anthropic-ai" / "claude-code" / "bin" / "claude.exe"
    return npm if npm.exists() else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--settings", default=str(pathlib.Path.home() / ".claude" / "settings.json"))
    ap.add_argument("--binary", default=None)
    ap.add_argument("--also", nargs="*", default=[], help="extra names to check")
    args = ap.parse_args()

    binary = pathlib.Path(args.binary) if args.binary else find_binary()
    if not binary or not binary.exists():
        sys.exit("claude.exe not found; pass --binary")
    blob = binary.read_bytes()
    settings = json.loads(pathlib.Path(args.settings).read_text(encoding="utf-8"))

    names: list[tuple[str, str]] = []
    names += [("env", k) for k in settings.get("env", {})]
    names += [("top", k) for k in settings if k not in SKIP_TOPLEVEL]
    names += [("also", k) for k in args.also]

    print(f"binary: {binary} ({len(blob)/1e6:.0f} MB)")
    print(f"{'kind':5s} {'hits':>5s}  name")
    dead = []
    for kind, k in names:
        n = blob.count(k.encode("utf-8"))
        flag = "  <-- 0 hits: the binary cannot read this name" if n == 0 else ""
        print(f"{kind:5s} {n:5d}  {k}{flag}")
        if n == 0:
            dead.append(k)
    print()
    print("DEAD/MISNAMED:" if dead else "all names present in the binary", ", ".join(dead))
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""skill_audit.py — DIY stand-in for the built-in `/skill-doctor` report.

`/skill-doctor` is feature-flag-gated and unavailable while
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 is set. This script measures the
same two things from disk:

  1. Context cost: estimated tokens each skill's listing entry (name +
     description) adds to EVERY turn's system prompt.
  2. Usage: how often each skill was invoked — user-typed `/name` from
     ~/.claude/history.jsonl (all sessions since the log began) plus Skill-tool
     and <command-name> invocations found in surviving session transcripts.

Token counts are a chars/4 estimate (labelled as such). Bundled skills
(dataviz, update-config, loop, ...) are not on disk here and are excluded,
matching /skill-doctor's own scope.

Usage:
    python tools/skill_audit.py [--project PATH] [--days N] [--out REPORT.md]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

HOME = Path.home()
CLAUDE_DIR = HOME / ".claude"


def est_tokens(s: str) -> int:
    return max(1, round(len(s) / 4))


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return {}, text
    fm_block = parts[0][3:]
    body = parts[1].lstrip("\n")
    fm: dict = {}
    cur_key = None
    for line in fm_block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            cur_key, val = m.group(1), m.group(2).strip()
            if val in (">", "|", ">-", "|-"):
                fm[cur_key] = ""
            else:
                fm[cur_key] = val.strip('"').strip("'")
        elif cur_key and line.startswith((" ", "\t")):
            fm[cur_key] = (fm.get(cur_key, "") + " " + line.strip()).strip()
    return fm, body


def skill_files(project: Path) -> list[tuple[str, str, Path]]:
    """Return (source, name, path) for every skill/command file on disk."""
    out: list[tuple[str, str, Path]] = []
    for src, base in (("user", CLAUDE_DIR), ("project", project / ".claude")):
        for p in sorted((base / "commands").glob("*.md")):
            out.append((src, p.stem, p))
        for p in sorted((base / "skills").glob("*/SKILL.md")):
            out.append((src, p.parent.name, p))
    plug_root = CLAUDE_DIR / "plugins" / "cache"
    if plug_root.exists():
        for p in sorted(plug_root.rglob("SKILL.md")):
            out.append(("plugin", f"{p.parents[2].name}:{p.parent.name}", p))
        for p in sorted(plug_root.rglob("commands/*.md")):
            out.append(("plugin", f"{p.parents[1].name}:{p.stem}", p))
    return out


def listing_entry(name: str, path: Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    desc = fm.get("description", "").strip()
    if not desc:
        for line in body.splitlines():
            line = line.strip().lstrip("#").strip()
            if line:
                desc = line
                break
    entry = f"- {name}: {desc}"
    return desc, est_tokens(entry)


def history_usage(since: datetime | None) -> tuple[Counter, dict, Counter]:
    """User-typed /commands from history.jsonl → (count_all, last_used, count_window)."""
    hist = CLAUDE_DIR / "history.jsonl"
    count_all: Counter = Counter()
    count_window: Counter = Counter()
    last_used: dict[str, datetime] = {}
    if not hist.exists():
        return count_all, last_used, count_window
    with hist.open(encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            disp = (rec.get("display") or "").strip()
            if not disp.startswith("/"):
                continue
            name = disp.split()[0][1:]
            if not name:
                continue
            ts = datetime.fromtimestamp(rec.get("timestamp", 0) / 1000, tz=timezone.utc)
            count_all[name] += 1
            if since is None or ts >= since:
                count_window[name] += 1
            if name not in last_used or ts > last_used[name]:
                last_used[name] = ts
    return count_all, last_used, count_window


SKILL_TOOL_RE = re.compile(r'"name":"Skill","input":\{[^}]*?"skill":"([^"]+)"')
CMD_NAME_RE = re.compile(r"<command-name>/([\w:.-]+)</command-name>")


def transcript_usage() -> tuple[Counter, Counter, int]:
    """Skill-tool + <command-name> hits across surviving transcripts."""
    by_tool: Counter = Counter()
    by_cmd: Counter = Counter()
    n_files = 0
    for p in (CLAUDE_DIR / "projects").glob("*/*.jsonl"):
        n_files += 1
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in SKILL_TOOL_RE.finditer(text):
            by_tool[m.group(1)] += 1
        for m in CMD_NAME_RE.finditer(text):
            by_cmd[m.group(1)] += 1
    return by_tool, by_cmd, n_files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=os.getcwd())
    ap.add_argument("--days", type=int, default=90, help="recent-usage window")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    project = Path(args.project).resolve()
    since = datetime.now(timezone.utc) - timedelta(days=args.days)

    files = skill_files(project)
    hist_all, hist_last, hist_win = history_usage(since)
    tool_hits, cmd_hits, n_tx = transcript_usage()

    rows = []
    for src, name, path in files:
        desc, toks = listing_entry(name, path)
        short = name.split(":")[-1]
        typed = hist_all.get(short, 0) + (hist_all.get(name, 0) if ":" in name else 0)
        typed_win = hist_win.get(short, 0)
        by_claude = tool_hits.get(short, 0) + tool_hits.get(name, 0)
        last = hist_last.get(short)
        rows.append(dict(src=src, name=name, tokens=toks, desc_len=len(desc),
                         typed=typed, typed_win=typed_win, by_claude=by_claude,
                         last=last.date().isoformat() if last else "never",
                         path=str(path)))

    total_tokens = sum(r["tokens"] for r in rows)
    never = [r for r in rows if r["typed"] == 0 and r["by_claude"] == 0]
    stale = [r for r in rows if r["typed"] > 0 and r["typed_win"] == 0 and r["by_claude"] == 0]
    never_tokens = sum(r["tokens"] for r in never)
    stale_tokens = sum(r["tokens"] for r in stale)

    hist_path = CLAUDE_DIR / "history.jsonl"
    first_ts = None
    if hist_path.exists():
        with hist_path.open(encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    first_ts = datetime.fromtimestamp(json.loads(line)["timestamp"] / 1000, tz=timezone.utc)
                    break
                except Exception:
                    continue

    L: list[str] = []
    L.append(f"# Skill audit — {datetime.now().date().isoformat()} (DIY /skill-doctor)\n")
    L.append(f"Project: `{project}`  ")
    L.append(f"Skill files on disk: **{len(rows)}** (user/project/plugin; bundled skills excluded, as /skill-doctor does)  ")
    L.append(f"Listing cost, all {len(rows)} entries: **~{total_tokens:,} tokens/turn** (chars/4 estimate)  ")
    L.append(f"Usage sources: `history.jsonl` user-typed commands since {first_ts.date() if first_ts else '?'} "
             f"(all projects), plus Skill-tool / `<command-name>` hits across {n_tx} surviving transcripts  ")
    L.append(f"Recent window: last {args.days} days\n")
    L.append(f"- **Never invoked** (0 typed ever, 0 Claude Skill-tool hits): **{len(never)}** skills, ~{never_tokens:,} tokens/turn")
    L.append(f"- **Stale** (typed before, not in last {args.days} d, no tool hits): **{len(stale)}** skills, ~{stale_tokens:,} tokens/turn")
    L.append(f"- Active: {len(rows) - len(never) - len(stale)} skills\n")

    def table(title: str, subset: list[dict]) -> None:
        L.append(f"## {title} ({len(subset)})\n")
        L.append("| skill | src | ~tok | typed (all) | typed (window) | by Claude | last typed |")
        L.append("|---|---|---:|---:|---:|---:|---|")
        for r in sorted(subset, key=lambda r: -r["tokens"]):
            L.append(f"| {r['name']} | {r['src']} | {r['tokens']} | {r['typed']} | {r['typed_win']} | {r['by_claude']} | {r['last']} |")
        L.append("")

    table("Never invoked — sorted by context cost (turn these off first)", never)
    table(f"Stale (>{args.days} d)", stale)
    table("Active", [r for r in rows if r not in never and r not in stale])

    L.append("## Caveats\n")
    L.append("- Token numbers are chars/4 estimates of the `- name: description` listing line, not tokenizer-exact.")
    L.append("- `by Claude` only sees the transcripts still on disk; older sessions' Skill-tool calls are gone. `typed` is complete back to the history start date.")
    L.append("- Commands invoked from other projects (CalmCore) with the same name count toward `typed`.")
    L.append("- Turning a skill off: `/skills` → highlight → Space to cycle → Esc saves to `.claude/settings.local.json` (skillOverrides).")

    report = "\n".join(L)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"wrote {args.out}")
    print("\n".join(L[:12]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

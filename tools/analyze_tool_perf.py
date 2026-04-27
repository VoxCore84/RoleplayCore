#!/usr/bin/env python3
"""Analyze tool performance from session-stats.jsonl (duration_ms field).

Usage:
    python tools/analyze_tool_perf.py              # last 24h summary
    python tools/analyze_tool_perf.py --hours 4    # last 4 hours
    python tools/analyze_tool_perf.py --slow        # only show slow tools
    python tools/analyze_tool_perf.py --tool Agent  # filter by tool name
"""
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from statistics import mean, median

STATS_FILE = Path.home() / ".claude" / "session-stats.jsonl"


def load_entries(hours: int) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    entries = []
    try:
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ts_str = entry.get("timestamp", "")
                try:
                    ts = datetime.fromisoformat(ts_str)
                    if ts < cutoff:
                        continue
                except (ValueError, TypeError):
                    continue
                if entry.get("duration_ms") is not None:
                    entries.append(entry)
    except FileNotFoundError:
        pass
    return entries


def percentile(sorted_vals: list[float], pct: float) -> float:
    if not sorted_vals:
        return 0.0
    idx = int(len(sorted_vals) * pct / 100)
    return sorted_vals[min(idx, len(sorted_vals) - 1)]


def main() -> int:
    hours = 24
    slow_only = False
    tool_filter = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--hours" and i + 1 < len(args):
            hours = int(args[i + 1])
            i += 2
        elif args[i] == "--slow":
            slow_only = True
            i += 1
        elif args[i] == "--tool" and i + 1 < len(args):
            tool_filter = args[i + 1]
            i += 2
        else:
            i += 1

    entries = load_entries(hours)
    if not entries:
        print(f"No duration data found in the last {hours}h.")
        print("Duration tracking was just enabled -- data will accumulate from this session onward.")
        return 0

    by_tool: dict[str, list[float]] = defaultdict(list)
    for e in entries:
        tool = e.get("tool", "")
        if tool_filter and tool_filter.lower() not in tool.lower():
            continue
        by_tool[tool].append(float(e["duration_ms"]))

    if not by_tool:
        print(f"No matching entries for filter '{tool_filter}'.")
        return 0

    print(f"Tool Performance Report ({hours}h window, {len(entries)} calls with duration data)")
    print(f"{'='*80}")
    print(f"{'Tool':<45} {'Count':>5} {'Med':>8} {'P95':>8} {'Max':>8} {'Avg':>8}")
    print(f"{'-'*45} {'-'*5} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")

    rows = []
    for tool, durations in sorted(by_tool.items()):
        s = sorted(durations)
        med = median(s)
        p95 = percentile(s, 95)
        mx = max(s)
        avg = mean(s)
        rows.append((tool, len(s), med, p95, mx, avg))

    rows.sort(key=lambda r: r[3], reverse=True)

    for tool, count, med, p95, mx, avg in rows:
        if slow_only and p95 < 5000:
            continue
        def fmt(ms: float) -> str:
            if ms >= 60000:
                return f"{ms/60000:.1f}m"
            if ms >= 1000:
                return f"{ms/1000:.1f}s"
            return f"{ms:.0f}ms"
        print(f"{tool:<45} {count:>5} {fmt(med):>8} {fmt(p95):>8} {fmt(mx):>8} {fmt(avg):>8}")

    total_ms = sum(d for durs in by_tool.values() for d in durs)
    print(f"\nTotal tool time: {total_ms/1000:.1f}s across {sum(len(d) for d in by_tool.values())} calls")

    slowest = max(entries, key=lambda e: e.get("duration_ms", 0))
    print(f"Slowest single call: {slowest.get('tool', '?')} at {slowest['duration_ms']/1000:.1f}s")
    if slowest.get("file_path") or slowest.get("path"):
        print(f"  Target: {slowest.get('file_path') or slowest.get('path')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

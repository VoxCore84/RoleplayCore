#!/usr/bin/env python3
"""Auto-calibrate slow-tool thresholds from session-stats.jsonl duration data.

Reads accumulated duration_ms data, calculates P95 per tool, and writes
thresholds to ~/.claude/tool-thresholds.json. The hook daemon loads these
on startup and merges with hardcoded defaults.

Usage:
    python tools/calibrate_thresholds.py           # calibrate from all data
    python tools/calibrate_thresholds.py --hours 72  # last 72 hours only
    python tools/calibrate_thresholds.py --dry-run   # show what would be written
"""
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

STATS_FILE = Path.home() / ".claude" / "session-stats.jsonl"
THRESHOLDS_FILE = Path.home() / ".claude" / "tool-thresholds.json"

MIN_SAMPLES = 20
MULTIPLIER = 2.0


def percentile(sorted_vals: list[float], pct: float) -> float:
    if not sorted_vals:
        return 0.0
    idx = int(len(sorted_vals) * pct / 100)
    return sorted_vals[min(idx, len(sorted_vals) - 1)]


def main() -> int:
    hours = 0
    dry_run = False

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--hours" and i + 1 < len(args):
            hours = int(args[i + 1])
            i += 2
        elif args[i] == "--dry-run":
            dry_run = True
            i += 1
        else:
            i += 1

    cutoff = None
    if hours > 0:
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)

    durations: dict[str, list[float]] = defaultdict(list)
    total = 0

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
                ms = entry.get("duration_ms")
                tool = entry.get("tool")
                if ms is None or not tool:
                    continue
                if cutoff:
                    ts_str = entry.get("timestamp", "")
                    try:
                        ts = datetime.fromisoformat(ts_str)
                        if ts < cutoff:
                            continue
                    except (ValueError, TypeError):
                        continue
                durations[tool].append(float(ms))
                total += 1
    except FileNotFoundError:
        print("No session-stats.jsonl found. Duration data accumulates from sessions with v1.2.0+ daemon.")
        return 1

    if total == 0:
        print("No duration_ms data found yet. Run some tool calls first.")
        return 1

    thresholds: dict[str, dict] = {}
    for tool, vals in sorted(durations.items()):
        if len(vals) < MIN_SAMPLES:
            continue
        s = sorted(vals)
        p50 = s[len(s) // 2]
        p95 = percentile(s, 95)
        threshold = max(5000, round(p95 * MULTIPLIER))
        thresholds[tool] = {
            "threshold_ms": threshold,
            "p95_ms": round(p95),
            "p50_ms": round(p50),
            "max_ms": round(max(s)),
            "samples": len(s),
            "calibrated_at": datetime.now(timezone.utc).isoformat(),
        }

    window = f"last {hours}h" if hours else "all data"
    print(f"Calibrated thresholds for {len(thresholds)} tools ({total} samples, {window})")
    print(f"{'Tool':<45} {'P50':>8} {'P95':>8} {'Thresh':>8} {'Samples':>8}")
    print(f"{'-'*45} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")

    for tool, data in sorted(thresholds.items(), key=lambda x: x[1]["p95_ms"], reverse=True):
        def fmt(ms: float) -> str:
            if ms >= 60000:
                return f"{ms/60000:.1f}m"
            if ms >= 1000:
                return f"{ms/1000:.1f}s"
            return f"{ms:.0f}ms"
        print(f"{tool:<45} {fmt(data['p50_ms']):>8} {fmt(data['p95_ms']):>8} {fmt(data['threshold_ms']):>8} {data['samples']:>8}")

    skipped = [t for t, v in durations.items() if len(v) < MIN_SAMPLES]
    if skipped:
        print(f"\nSkipped {len(skipped)} tools with <{MIN_SAMPLES} samples: {', '.join(skipped[:5])}")

    if dry_run:
        print(f"\n[dry-run] Would write to {THRESHOLDS_FILE}")
    else:
        THRESHOLDS_FILE.write_text(json.dumps(thresholds, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nWrote to {THRESHOLDS_FILE}")
        print("Restart the hook daemon to load new thresholds.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

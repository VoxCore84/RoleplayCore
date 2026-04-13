"""Freshness sweep — asyncio job that runs every ~60 min inside the daemon.

Karpathy Phase 4 (lint) for the document corpus. Compares:
  - Extraction manifest mtimes vs. source file mtimes (stale extractions)
  - Folder mtimes vs. memory file mtimes (memory drift)

Emits a report to AI_Studio/Reports/scheduled/freshness_<date>.md that
session-start reads and surfaces RED items.

This runs as an asyncio task, NOT a CronCreate. Recurring cron is banned.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from pathlib import Path

from .. import config

log = logging.getLogger(__name__)

CACHE_EXTRACT = config.REPO_ROOT / ".cache" / "extracted"
MEMORY_DIR = Path.home() / ".claude/projects/C--Users-atayl-VoxCore/memory"
REPORT_DIR = config.REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"

DEFAULT_INTERVAL_SECONDS = 3600


async def run_once() -> dict:
    """Single freshness-check pass. Returns summary dict."""
    findings: dict = {
        "timestamp": int(time.time()),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "stale_extractions": [],
        "stale_memory": [],
    }

    # Stale extractions
    if CACHE_EXTRACT.exists():
        for bucket in CACHE_EXTRACT.iterdir():
            manifest_path = bucket / "manifest.json"
            if not manifest_path.exists():
                continue
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            except Exception:
                continue
            source_root = Path(manifest.get("source", ""))
            if not source_root.exists():
                continue
            for rel, entry in manifest.get("entries", {}).items():
                src = source_root / rel
                if not src.exists():
                    continue
                try:
                    src_mtime = src.stat().st_mtime
                except OSError:
                    continue
                if src_mtime > entry.get("mtime", 0) + 1:
                    findings["stale_extractions"].append({
                        "source": str(src),
                        "drift_sec": int(src_mtime - entry.get("mtime", 0)),
                    })

    # Stale memory (older than 14 days)
    now = time.time()
    threshold = now - 14 * 86400
    if MEMORY_DIR.exists():
        for m in MEMORY_DIR.rglob("*.md"):
            if not m.is_file():
                continue
            try:
                if m.stat().st_mtime < threshold:
                    findings["stale_memory"].append({
                        "file": str(m),
                        "age_days": round((now - m.stat().st_mtime) / 86400, 1),
                    })
            except OSError:
                continue

    return findings


def write_report(findings: dict) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d")
    path = REPORT_DIR / f"freshness_{stamp}.md"
    stale_ext = findings.get("stale_extractions", [])
    stale_mem = findings.get("stale_memory", [])
    lines = [
        f"# Freshness sweep — {findings['date']}",
        "",
        f"- Stale extractions: {len(stale_ext)}",
        f"- Stale memory files: {len(stale_mem)}",
        "",
    ]
    if stale_ext:
        lines.append("## Stale extractions (top 20)")
        for item in stale_ext[:20]:
            lines.append(f"- `{item['source']}` (drift {item['drift_sec']}s)")
        lines.append("")
    if stale_mem:
        lines.append("## Stale memory (top 20)")
        for item in stale_mem[:20]:
            lines.append(f"- `{item['file']}` ({item['age_days']}d old)")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


async def run_forever(interval_seconds: int = DEFAULT_INTERVAL_SECONDS, stop_event: asyncio.Event | None = None) -> None:
    """Run freshness sweeps on a loop. Call from daemon.py main().

    Respects stop_event for graceful shutdown. Never uses cron.
    """
    while stop_event is None or not stop_event.is_set():
        try:
            findings = await run_once()
            path = write_report(findings)
            log.info(f"freshness sweep: {len(findings['stale_extractions'])} stale extractions, {len(findings['stale_memory'])} stale memory — {path}")
        except Exception as e:
            log.exception(f"freshness sweep error: {e}")
        try:
            await asyncio.wait_for(
                stop_event.wait() if stop_event else asyncio.sleep(interval_seconds),
                timeout=interval_seconds if stop_event else None,
            )
            break  # stop_event fired
        except asyncio.TimeoutError:
            continue


if __name__ == "__main__":
    # CLI: run once
    import sys
    findings = asyncio.run(run_once())
    path = write_report(findings)
    print(f"Report: {path}")
    print(f"Stale extractions: {len(findings['stale_extractions'])}")
    print(f"Stale memory: {len(findings['stale_memory'])}")
    sys.exit(0)

"""RAG verification sweep — samples N chunks per Case_Reference subfolder and confirms the chunk text appears in the source file.

Anchor-grep pattern adapted from CalmCore's verify_digest.py. Catches extraction
drift, truncation, and OCR artifacts before they reach a filing.

Runs as asyncio task inside the daemon, nightly. Or standalone:
    python -m tools.excluded_daemon.jobs.verify_rag
"""
from __future__ import annotations

import asyncio
import json
import logging
import random
import sqlite3
import time
from collections import defaultdict
from pathlib import Path

from .. import config

log = logging.getLogger(__name__)

FTS_DB = config.REPO_ROOT / ".cache" / "excluded_fts.db"
CACHE_EXTRACT = config.REPO_ROOT / ".cache" / "extracted"
REPORT_DIR = config.REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"

SAMPLES_PER_BUCKET = 5


def _sample_chunks() -> list[dict]:
    """Pull SAMPLES_PER_BUCKET random chunks from each extraction bucket."""
    if not FTS_DB.exists():
        return []
    conn = sqlite3.connect(str(FTS_DB))
    conn.row_factory = sqlite3.Row
    buckets: dict[str, list[dict]] = defaultdict(list)
    rows = conn.execute(
        """SELECT source_root, rel_path, chunk_idx, content
           FROM chunks ORDER BY RANDOM() LIMIT 2000"""
    ).fetchall()
    for r in rows:
        bucket_key = Path(r["source_root"]).parent.name  # cache bucket name
        if len(buckets[bucket_key]) < SAMPLES_PER_BUCKET:
            buckets[bucket_key].append(dict(r))
    conn.close()
    return [c for bucket_rows in buckets.values() for c in bucket_rows]


def _verify(chunk: dict) -> dict:
    """Confirm chunk['content'] substring appears in the source extraction file."""
    src_path = Path(chunk["source_root"]) / chunk["rel_path"]
    if not src_path.exists():
        return {"ok": False, "reason": "source .txt missing", "chunk": chunk}
    try:
        text = src_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"ok": False, "reason": f"read error: {e}", "chunk": chunk}

    # Use a stable 60-char anchor from middle of the chunk
    needle = chunk["content"][60:120] if len(chunk["content"]) > 120 else chunk["content"][:60]
    needle = needle.strip()
    if not needle:
        return {"ok": True, "reason": "empty chunk"}
    if needle in text:
        return {"ok": True}
    # Fallback: first 60 chars
    alt = chunk["content"][:60].strip()
    if alt and alt in text:
        return {"ok": True, "reason": "matched alt anchor"}
    return {"ok": False, "reason": "anchor not found in source", "chunk": {"rel_path": chunk["rel_path"], "chunk_idx": chunk["chunk_idx"]}}


async def run_once() -> dict:
    samples = _sample_chunks()
    results = [_verify(s) for s in samples]
    passed = sum(1 for r in results if r["ok"])
    failed = [r for r in results if not r["ok"]]
    return {
        "timestamp": int(time.time()),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "samples": len(samples),
        "passed": passed,
        "failed_count": len(failed),
        "pass_rate": round(passed / len(samples), 3) if samples else 1.0,
        "failures": failed[:20],
    }


def write_report(findings: dict) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d")
    path = REPORT_DIR / f"rag_verify_{stamp}.md"
    lines = [
        f"# RAG verification — {findings['date']}",
        "",
        f"- Samples: {findings['samples']}",
        f"- Passed: {findings['passed']}",
        f"- Failed: {findings['failed_count']}",
        f"- Pass rate: {findings['pass_rate']*100:.1f}%",
        "",
    ]
    if findings["failures"]:
        lines.append("## Failures (top 20)")
        for f in findings["failures"]:
            lines.append(f"- {f.get('reason')} — `{f.get('chunk', {}).get('rel_path', '?')}` chunk {f.get('chunk', {}).get('chunk_idx', '?')}")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


async def run_forever(interval_seconds: int = 86400, stop_event: asyncio.Event | None = None) -> None:
    """Nightly verification. Asyncio task — never cron."""
    while stop_event is None or not stop_event.is_set():
        try:
            findings = await run_once()
            path = write_report(findings)
            log.info(f"rag verify: {findings['passed']}/{findings['samples']} pass ({findings['pass_rate']*100:.1f}%) — {path}")
        except Exception as e:
            log.exception(f"rag verify error: {e}")
        try:
            if stop_event:
                await asyncio.wait_for(stop_event.wait(), timeout=interval_seconds)
                break
            await asyncio.sleep(interval_seconds)
        except asyncio.TimeoutError:
            continue


if __name__ == "__main__":
    import sys
    findings = asyncio.run(run_once())
    path = write_report(findings)
    print(f"Report: {path}")
    print(f"Pass rate: {findings['pass_rate']*100:.1f}%  ({findings['passed']}/{findings['samples']})")
    if findings["failures"]:
        print(f"Failures: {findings['failed_count']}")
        for f in findings["failures"][:3]:
            print(f"  {f}")
    sys.exit(0)

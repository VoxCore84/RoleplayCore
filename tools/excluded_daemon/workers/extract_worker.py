"""Extract worker — invokes extract_cache.py on the parent folder of a changed file.

Simplification for v1: we re-run extract_cache.py over the source folder, which is
already incremental (sha-keyed), so re-running on a folder with one changed file
only extracts that one file. Lower-complexity than maintaining a per-file cache
routine here.
"""
from __future__ import annotations

import asyncio
import logging
import subprocess
import sys
from pathlib import Path

from .. import config

log = logging.getLogger(__name__)


async def extract(path: Path) -> dict:
    """Run extract_cache.py on path's parent folder. Returns a status dict."""
    # Determine the source folder to run extract_cache.py against. Use the
    # path's immediate parent under EXCLUDED_ROOT so the cache bucket is stable.
    try:
        rel = path.relative_to(config.EXCLUDED_ROOT)
    except ValueError:
        return {"ok": False, "error": f"path not under EXCLUDED_ROOT: {path}"}

    # Run against the top-level subfolder (e.g. IMPORTANT DOCS/Monday_HAF_Call_13Apr2026)
    # so the cache bucket matches the existing ones. Walk upward until we're at root level.
    if len(rel.parts) == 0:
        return {"ok": False, "error": "path is the root"}
    # Use the top-level subfolder under EXCLUDED_ROOT so cache buckets stay stable.
    # For IMPORTANT DOCS we go one level deeper so each category gets its own bucket.
    if rel.parts[0] == "IMPORTANT DOCS" and len(rel.parts) >= 2:
        source_folder = config.EXCLUDED_ROOT / rel.parts[0] / rel.parts[1]
    else:
        source_folder = config.EXCLUDED_ROOT / rel.parts[0]
    if not source_folder.is_dir():
        return {"ok": False, "error": f"source_folder not a dir: {source_folder}"}

    cmd = [
        sys.executable,
        str(config.EXTRACT_CACHE_PY),
        str(source_folder),
    ]
    log.info(f"extract: {source_folder} (trigger: {path.name})")

    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=600)
        return {
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout_tail": stdout.decode("utf-8", errors="replace")[-500:],
            "stderr_tail": stderr.decode("utf-8", errors="replace")[-500:],
        }
    except asyncio.TimeoutError:
        return {"ok": False, "error": "extract timed out after 600s"}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}

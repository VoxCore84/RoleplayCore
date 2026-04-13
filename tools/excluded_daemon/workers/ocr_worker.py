"""OCR worker — invokes ocr_images.py on the parent folder of a new image."""
from __future__ import annotations

import asyncio
import logging
import sys
from pathlib import Path

from .. import config

log = logging.getLogger(__name__)


async def ocr(path: Path) -> dict:
    try:
        rel = path.relative_to(config.EXCLUDED_ROOT)
    except ValueError:
        return {"ok": False, "error": f"path not under EXCLUDED_ROOT: {path}"}

    if len(rel.parts) == 0:
        return {"ok": False, "error": "path is the root"}
    if rel.parts[0] == "IMPORTANT DOCS" and len(rel.parts) >= 2:
        source_folder = config.EXCLUDED_ROOT / rel.parts[0] / rel.parts[1]
    else:
        source_folder = config.EXCLUDED_ROOT / rel.parts[0]
    if not source_folder.is_dir():
        return {"ok": False, "error": f"source_folder not a dir: {source_folder}"}

    cmd = [sys.executable, str(config.OCR_IMAGES_PY), str(source_folder), "--workers", "4"]
    log.info(f"ocr: {source_folder} (trigger: {path.name})")
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
        return {"ok": False, "error": "ocr timed out after 600s"}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}

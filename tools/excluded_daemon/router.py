"""Route filesystem events to the right pipeline.

Enforces security gate FIRST — credentials/secrets never enter any pipeline.
Then classifies by extension and returns the appropriate worker kind.

Two-stage security (UKB Playbook Pattern A):
  Stage 1 — filename/folder blocklist (fast, always applied)
  Stage 2 — content pattern scan (first 4KB, regex for SSN/keys/PEM/etc.)
  Both stages must pass before the file can enter any pipeline.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from . import config

log = logging.getLogger(__name__)

# Compile content patterns once
_CONTENT_RE = [re.compile(p) for p in getattr(config, "SECURITY_CONTENT_PATTERNS", [])]

# Text-extractable extensions whose first 4KB we scan
_CONTENT_SCAN_EXTS = {".txt", ".md", ".rtf", ".eml", ".msg", ".csv", ".json", ".env"}


class Pipeline(Enum):
    EXTRACT = "extract"
    OCR = "ocr"
    AUDIO = "audio"
    MBOX = "mbox"
    LLM = "llm"             # NER post-processing → Knowledge Graph
    SKIP = "skip"
    SECURITY = "security"   # log + refuse


@dataclass
class RoutingDecision:
    path: Path
    pipeline: Pipeline
    reason: str
    priority: int   # 0=high, 1=medium, 2=low


def _hits_security_filter(path: Path) -> str | None:
    """Stage 1: filename + folder blocklist. Fast substring matching."""
    name_lower = path.name.lower()
    for pattern in config.SECURITY_FILENAMES:
        if pattern in name_lower:
            return f"filename matches security pattern '{pattern}'"

    for part in path.parts:
        if part in config.SECURITY_FOLDERS:
            return f"under security folder '{part}'"

    return None


def _hits_content_filter(path: Path) -> str | None:
    """Stage 2: scan first 4KB for credential/SSN/key patterns.

    Only applied to small text-extractable files where the patterns would be
    meaningful. Binary PDFs and images are not scanned at this level (OCR
    output is caught at the content-filter in extract_cache.py post-extract).
    """
    if not _CONTENT_RE:
        return None
    ext = path.suffix.lower()
    if ext not in _CONTENT_SCAN_EXTS:
        return None
    try:
        size = path.stat().st_size
    except OSError:
        return None
    # Skip large files — if it's a 50MB .txt it's almost certainly not a secret
    if size > 1_048_576:
        return None
    try:
        with path.open("rb") as f:
            head = f.read(4096)
        text = head.decode("utf-8", errors="replace")
    except Exception:
        return None
    for pat in _CONTENT_RE:
        m = pat.search(text)
        if m:
            # Log the pattern name, NOT the matched text (which may be the secret)
            return f"content matches sensitive pattern {pat.pattern!r}"
    return None


def _in_skip_folder(path: Path, root: Path) -> str | None:
    """Check if path is under a top-level skip folder."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        return None
    if len(rel.parts) == 0:
        return None
    top = rel.parts[0]
    if top in config.SKIP_FOLDERS:
        return f"under skip folder '{top}'"
    return None


def is_readonly_path(path: Path, root: Path = config.EXCLUDED_ROOT) -> bool:
    """Return True if `path` lies under any configured read-only sub-path.

    Used by any daemon worker before attempting a write. Reads are always allowed;
    writes raise PermissionError at the worker level if this returns True.
    """
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    rel_str = str(rel).replace("\\", "/")
    for readonly in config.READONLY_PATHS:
        normalized = readonly.replace("\\", "/")
        if rel_str == normalized or rel_str.startswith(normalized + "/"):
            return True
    return False


def assert_writable(path: Path, root: Path = config.EXCLUDED_ROOT) -> None:
    """Raise PermissionError if `path` is under a READONLY_PATHS root.

    Every worker that produces output destined INSIDE the corpus must call this
    first. (Workers that write to .cache/ don't need to — .cache is outside
    EXCLUDED_ROOT by construction.)
    """
    if is_readonly_path(path, root):
        raise PermissionError(
            f"Write blocked: {path} is under a read-only root (Case_Reference chain-of-custody). "
            f"See .claude/rules/excluded-corpus.md Rule 1."
        )


def in_high_priority_folder(path: Path, root: Path = config.EXCLUDED_ROOT) -> bool:
    """True if `path` lies under one of the HIGH_PRIORITY_FOLDERS from config."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    rel_str = str(rel).replace("\\", "/")
    for folder in getattr(config, "HIGH_PRIORITY_FOLDERS", set()):
        normalized = folder.replace("\\", "/")
        if rel_str.startswith(normalized + "/") or rel_str == normalized:
            return True
    return False


def route(path: Path, root: Path = config.EXCLUDED_ROOT) -> RoutingDecision:
    """Classify a file path into a pipeline decision.

    Order matters:
    1. Security stage 1 (filename/folder blocklist)
    2. Skip-folder policy (LoreWalkerTDB, etc.)
    3. Extension match
    4. Security stage 2 (content pattern scan on small text files)
       — runs after extension match so we don't scan binary PDFs at this layer
    """
    # 1. Security stage 1 — filename/folder
    reason = _hits_security_filter(path)
    if reason:
        log.warning(f"SECURITY refuse (stage 1): {path}: {reason}")
        return RoutingDecision(path, Pipeline.SECURITY, reason, priority=0)

    # 2. Policy skips
    reason = _in_skip_folder(path, root)
    if reason:
        return RoutingDecision(path, Pipeline.SKIP, reason, priority=2)

    ext = path.suffix.lower()

    # 3. Extension routing
    pipeline = Pipeline.SKIP
    rr = f"unknown ext={ext}"
    if ext in config.EXTRACTABLE_EXTS:
        pipeline, rr = Pipeline.EXTRACT, f"ext={ext}"
    elif ext in config.OCR_EXTS:
        pipeline, rr = Pipeline.OCR, f"ext={ext}"
    elif ext in config.AUDIO_EXTS:
        pipeline, rr = Pipeline.AUDIO, f"ext={ext}"
    elif ext in config.MBOX_EXTS:
        pipeline, rr = Pipeline.MBOX, f"ext={ext}"
    elif ext in config.SKIP_EXTS:
        pipeline, rr = Pipeline.SKIP, f"explicit-skip ext={ext}"

    if pipeline == Pipeline.SKIP:
        return RoutingDecision(path, pipeline, rr, priority=2)

    # 4. Security stage 2 — content scan (only for text-extractable small files)
    reason = _hits_content_filter(path)
    if reason:
        log.warning(f"SECURITY refuse (stage 2): {path}: {reason}")
        return RoutingDecision(path, Pipeline.SECURITY, reason, priority=0)

    # Priority bump if in HIGH_PRIORITY_FOLDERS — same pipeline, but priority=0 always
    priority = 0 if in_high_priority_folder(path, root) else (0 if pipeline in (Pipeline.EXTRACT, Pipeline.OCR, Pipeline.MBOX) else 1)
    return RoutingDecision(path, pipeline, rr, priority=priority)

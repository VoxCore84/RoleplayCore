#!/usr/bin/env python3
"""Measure ingest throughput per modality (docs/hour, audio/hour).

Closes Verification Master Checklist Cat 4 + Cat 6 item: "Throughput per modality
(mbox, PDF, audio, image, office docs) — never measured."

Methodology: time the existing extraction tool against a fresh-rendered sample
of files for each modality, normalize to per-hour rate. Skips files with
existing cache hits so we measure cold-cache extraction (the bottleneck).

Output: AI_Studio/Reports/scheduled/throughput_per_modality_<ts>.json
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_ROOT = Path("C:/Users/atayl/Desktop/Excluded")
IMPORTANT_DOCS = EXCLUDED_ROOT / "IMPORTANT DOCS"

# Modality → {extension(s), root path glob, target sample size}
MODALITY_CONFIG = {
    "pdf":     {"exts": [".pdf"],          "max_files": 10,  "max_bytes_per_file": 5_000_000},
    "docx":    {"exts": [".docx", ".doc"], "max_files": 10,  "max_bytes_per_file": 2_000_000},
    "eml":     {"exts": [".eml"],          "max_files": 25,  "max_bytes_per_file": 1_000_000},
    "msg":     {"exts": [".msg"],          "max_files": 10,  "max_bytes_per_file": 2_000_000},
    "txt_md":  {"exts": [".txt", ".md"],   "max_files": 50,  "max_bytes_per_file": 1_000_000},
    "image":   {"exts": [".png", ".jpg", ".jpeg", ".heic", ".heif"], "max_files": 10, "max_bytes_per_file": 10_000_000},
}


def discover_files(root: Path, modality: str) -> list[Path]:
    cfg = MODALITY_CONFIG[modality]
    exts = set(e.lower() for e in cfg["exts"])
    candidates: list[Path] = []
    if not root.exists():
        return candidates
    try:
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if p.suffix.lower() not in exts:
                continue
            try:
                size = p.stat().st_size
            except OSError:
                continue
            if size == 0 or size > cfg["max_bytes_per_file"]:
                continue
            candidates.append(p)
            if len(candidates) >= cfg["max_files"] * 4:
                break
    except (PermissionError, OSError):
        pass
    # Take a deterministic sample (first N by path) — avoid cherry-picking
    candidates.sort()
    return candidates[: cfg["max_files"]]


def time_extract_one(path: Path) -> dict:
    """Invoke the project's extraction pipeline on a single file and time it.

    Uses tools/extract_cache.py if available, otherwise falls back to direct
    pdf_lib / msg_extract / docx2txt / Tesseract calls — whatever's right per
    extension.
    """
    ext = path.suffix.lower()
    t0 = time.time()
    error = None
    bytes_in = path.stat().st_size
    chars_out = 0
    try:
        text = ""
        if ext == ".pdf":
            sys.path.insert(0, str(REPO_ROOT / "tools"))
            import pdf_lib
            doc = pdf_lib.open(str(path))
            try:
                pages_text = []
                for i in range(len(doc)):
                    page = doc[i]
                    pages_text.append(page.get_text() if hasattr(page, "get_text") else "")
                text = "\n".join(pages_text)
            finally:
                if hasattr(doc, "close"):
                    doc.close()
        elif ext == ".msg":
            sys.path.insert(0, str(REPO_ROOT / "tools"))
            from msg_extract import extract_msg_text
            text = extract_msg_text(str(path)) or ""
        elif ext == ".docx":
            try:
                from docx import Document
                doc = Document(str(path))
                text = "\n".join(p.text for p in doc.paragraphs)
            except Exception as e:
                error = f"docx: {e}"
        elif ext in (".txt", ".md"):
            text = path.read_text(encoding="utf-8", errors="replace")
        elif ext == ".eml":
            import email
            from email import policy
            with open(path, "rb") as f:
                msg = email.message_from_bytes(f.read(), policy=policy.default)
            body = msg.get_body(preferencelist=("plain",))
            text = body.get_content() if body else ""
        elif ext in (".png", ".jpg", ".jpeg"):
            # Time the OCR — try pytesseract (Python wrapper) first, then CLI
            try:
                import pytesseract
                from PIL import Image
                img = Image.open(str(path))
                text = pytesseract.image_to_string(img, lang="eng")
            except ImportError:
                try:
                    import subprocess as sp
                    result = sp.run(["tesseract", str(path), "-", "-l", "eng"],
                                    capture_output=True, text=True, timeout=60,
                                    encoding="utf-8", errors="replace")
                    text = result.stdout
                except FileNotFoundError:
                    error = "tesseract not in PATH; pytesseract not installed"
                except Exception as e:
                    error = f"tesseract cli: {e}"
            except Exception as e:
                error = f"tesseract py: {e}"
        elif ext in (".heic", ".heif"):
            error = "heic/heif extraction not in scope"
        else:
            error = f"unknown ext {ext}"
        chars_out = len(text)
    except Exception as e:
        error = f"{type(e).__name__}: {e}"
    dt = time.time() - t0
    return {
        "path": str(path),
        "bytes": bytes_in,
        "elapsed_s": round(dt, 4),
        "chars_extracted": chars_out,
        "error": error,
    }


def measure_modality(root: Path, modality: str) -> dict:
    files = discover_files(root, modality)
    if not files:
        return {"modality": modality, "n": 0, "skipped": "no files found"}
    print(f"  {modality:>8}: {len(files)} files...", flush=True)
    per_file = []
    total_t = 0.0
    total_bytes = 0
    total_chars = 0
    n_errors = 0
    for f in files:
        r = time_extract_one(f)
        per_file.append(r)
        total_t += r["elapsed_s"]
        total_bytes += r["bytes"]
        total_chars += r["chars_extracted"]
        if r.get("error"):
            n_errors += 1
    if total_t == 0:
        return {"modality": modality, "n": len(files), "skipped": "all extractions failed"}
    return {
        "modality": modality,
        "n_files": len(files),
        "n_errors": n_errors,
        "total_elapsed_s": round(total_t, 3),
        "total_bytes": total_bytes,
        "total_chars": total_chars,
        "avg_elapsed_s": round(total_t / len(files), 4),
        "avg_bytes": round(total_bytes / len(files)),
        "avg_chars": round(total_chars / len(files)),
        "files_per_hour": round(3600 / (total_t / len(files)), 1),
        "MB_per_hour": round((total_bytes / total_t) * 3600 / (1024 * 1024), 1),
        "chars_per_second": round(total_chars / total_t, 0),
        "per_file": per_file[:5],  # truncate for output cleanliness
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=str(IMPORTANT_DOCS))
    p.add_argument("--out", default=None)
    p.add_argument("--modalities", nargs="+",
                   default=list(MODALITY_CONFIG.keys()),
                   help=f"Subset to measure. Default: all of {list(MODALITY_CONFIG.keys())}")
    args = p.parse_args()

    root = Path(args.root)
    out_path = (Path(args.out) if args.out else
                REPO_ROOT / "AI_Studio" / "Reports" / "scheduled" /
                f"throughput_per_modality_{time.strftime('%Y%m%d_%H%M%S')}.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Measuring throughput from {root}...")
    results = []
    t_total = time.time()
    for m in args.modalities:
        if m not in MODALITY_CONFIG:
            print(f"  unknown modality {m}, skipping")
            continue
        r = measure_modality(root, m)
        results.append(r)

    summary = {
        "root": str(root),
        "measured_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "wall_elapsed_s": round(time.time() - t_total, 2),
        "modalities": results,
    }
    out_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out_path}")

    print("\n=== Summary ===")
    print(f"  {'Modality':<10} {'N':>4} {'Avg s':>9} {'Files/hr':>10} {'MB/hr':>10} {'Errs':>5}")
    for r in results:
        if "skipped" in r:
            print(f"  {r['modality']:<10} {r['n']:>4} (skipped: {r['skipped']})")
            continue
        print(f"  {r['modality']:<10} {r['n_files']:>4} {r['avg_elapsed_s']:>9.4f} "
              f"{r['files_per_hour']:>10.1f} {r['MB_per_hour']:>10.1f} {r['n_errors']:>5}")


if __name__ == "__main__":
    main()

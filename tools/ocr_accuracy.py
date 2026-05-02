"""OCR character/word accuracy measurement.

Methodology:
  1. Pick PDFs that have a native text layer (pdfplumber can extract).
  2. Render each PDF's first page to PNG via pypdfium2.
  3. Run Tesseract on the PNG.
  4. Compare Tesseract output (hypothesis) to native text (ground truth).
  5. Report CER + WER per file and aggregate.

This is a true OCR-accuracy measurement: native text = ground truth.
Common methodology in OCR-quality benchmarks.

Usage:
    python tools/ocr_accuracy.py                         # default sample of 10
    python tools/ocr_accuracy.py --sample 20
    python tools/ocr_accuracy.py --output report.json
"""
from __future__ import annotations

import argparse
import io
import json
import os
import random
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"
TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Make ``tools.pdf_lib`` importable when this script is run directly from
# the repo (``python tools/ocr_accuracy.py``).
sys.path.insert(0, str(REPO_ROOT))


def configure_tesseract():
    if Path(TESSERACT).exists():
        os.environ.setdefault("TESSERACT_PATH", TESSERACT)
        try:
            import pytesseract
            pytesseract.pytesseract.tesseract_cmd = TESSERACT
        except ImportError:
            pass


def find_candidate_pdfs(roots: list[Path], limit: int) -> list[Path]:
    """Find PDFs likely to have native text (small-ish, not scanned-only)."""
    candidates: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for p in root.rglob("*.pdf"):
            try:
                size = p.stat().st_size
                if 50_000 < size < 5_000_000:  # >50KB to avoid trivial; <5MB to keep fast
                    candidates.append(p)
            except OSError:
                continue
    random.shuffle(candidates)
    return candidates[: limit * 3]  # over-sample so we can drop scan-only ones


def normalize(text: str) -> str:
    import re
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def chars(s: str) -> list[str]:
    return list(s.replace(" ", ""))


def words(s: str) -> list[str]:
    return s.split()


def levenshtein(a: list, b: list) -> int:
    """Token-level edit distance via Levenshtein C extension on chr-encoded strings."""
    try:
        import Levenshtein as Lev
    except ImportError:
        # Pure-Python fallback
        if not a:
            return len(b)
        if not b:
            return len(a)
        prev = list(range(len(b) + 1))
        for i, ca in enumerate(a, 1):
            cur = [i] + [0] * len(b)
            for j, cb in enumerate(b, 1):
                cost = 0 if ca == cb else 1
                cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
            prev = cur
        return prev[-1]
    if not a:
        return len(b)
    if not b:
        return len(a)
    vocab: dict = {}
    def encode(seq):
        return "".join(chr(0x4e00 + vocab.setdefault(t, len(vocab))) for t in seq)
    return Lev.distance(encode(a), encode(b))


def measure_one(pdf_path: Path) -> dict | None:
    """Return CER/WER metrics for one PDF, or None if unsuitable."""
    import pdfplumber
    from tools import pdf_lib

    # 1. Native text from page 1
    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            if not pdf.pages:
                return None
            native = pdf.pages[0].extract_text() or ""
    except Exception as e:
        return {"file": str(pdf_path.name), "error": f"pdfplumber: {e}"}

    if len(native.strip()) < 200:
        return None  # Page lacks meaningful text — likely scan-only

    # 2. Render page 1 to PNG via pypdfium2 (300 dpi)
    try:
        with pdf_lib.open(str(pdf_path)) as doc:
            pix = doc[0].get_pixmap(dpi=300)
            png = pix.tobytes("png")
    except Exception as e:
        return {"file": str(pdf_path.name), "error": f"render: {e}"}

    # 3. Tesseract OCR
    try:
        from PIL import Image
        import pytesseract
        img = Image.open(io.BytesIO(png))
        ocr_text = pytesseract.image_to_string(img, lang="eng") or ""
    except Exception as e:
        return {"file": str(pdf_path.name), "error": f"tesseract: {e}"}

    if len(ocr_text.strip()) < 50:
        return {"file": str(pdf_path.name), "error": "OCR returned empty"}

    # 4. Score
    ref = normalize(native)
    hyp = normalize(ocr_text)
    r_chars = chars(ref)
    h_chars = chars(hyp)
    r_words = words(ref)
    h_words = words(hyp)
    char_edits = levenshtein(h_chars, r_chars)
    word_edits = levenshtein(h_words, r_words)
    return {
        "file": pdf_path.name,
        "path": str(pdf_path),
        "ref_chars": len(r_chars),
        "hyp_chars": len(h_chars),
        "ref_words": len(r_words),
        "hyp_words": len(h_words),
        "char_edits": char_edits,
        "word_edits": word_edits,
        "cer": round(char_edits / max(len(r_chars), 1), 4),
        "wer": round(word_edits / max(len(r_words), 1), 4),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sample", type=int, default=10)
    p.add_argument("--output")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    random.seed(args.seed)
    configure_tesseract()

    roots = [
        Path("C:/Users/atayl/Desktop/Excluded/IMPORTANT DOCS"),
        Path("C:/Users/atayl/Desktop/Excluded"),
    ]
    candidates = find_candidate_pdfs(roots, args.sample)
    print(f"[ocr-accuracy] candidate pool: {len(candidates)}")

    results = []
    for cand in candidates:
        if len(results) >= args.sample:
            break
        m = measure_one(cand)
        if m is None:
            continue
        if "error" in m:
            print(f"  skip {cand.name}: {m['error']}")
            continue
        results.append(m)
        print(f"  {cand.name}: CER={m['cer']} WER={m['wer']}  ({m['char_edits']}/{m['ref_chars']} char edits)")

    if not results:
        print("[ocr-accuracy] no measurable samples", file=sys.stderr)
        return 1

    summary = {
        "n": len(results),
        "avg_cer": round(sum(r["cer"] for r in results) / len(results), 4),
        "avg_wer": round(sum(r["wer"] for r in results) / len(results), 4),
        "median_cer": round(sorted(r["cer"] for r in results)[len(results) // 2], 4),
        "p95_cer": round(sorted(r["cer"] for r in results)[max(0, int(len(results) * 0.95) - 1)], 4),
        "max_cer": round(max(r["cer"] for r in results), 4),
        "min_cer": round(min(r["cer"] for r in results), 4),
        "total_ref_chars": sum(r["ref_chars"] for r in results),
        "total_char_edits": sum(r["char_edits"] for r in results),
    }

    print()
    print("=== OCR Accuracy ===")
    print(f"  files: {summary['n']}")
    print(f"  avg CER: {summary['avg_cer']}  avg WER: {summary['avg_wer']}")
    print(f"  median CER: {summary['median_cer']}  p95: {summary['p95_cer']}")
    print(f"  aggregate: {summary['total_char_edits']}/{summary['total_ref_chars']} char edits")

    out = {"results": results, "summary": summary, "methodology": {
        "ground_truth": "pdfplumber native-text extract of PDF page 1",
        "hypothesis": "Tesseract 5.4 OCR on pypdfium2-rendered 300dpi PNG of same page",
        "normalization": "lowercase + strip punctuation + collapse whitespace",
    }}
    out_path = Path(args.output) if args.output else REPORT_DIR / f"ocr_accuracy_{time.strftime('%Y%m%d_%H%M%S')}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\n[output] {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

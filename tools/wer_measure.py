"""Word/Character Error Rate measurement.

Two modes:

  --mode cross-instance      Compare two independent transcripts of the SAME
                              audio file (transcription stability — measures
                              run-to-run disagreement, not absolute accuracy).
  --mode against-reference    Compare transcripts to a reference transcript
                              (true WER — absolute accuracy vs. ground truth).

Output: per-file and aggregate WER + CER, dumped to JSON for the calibration
ledger. Uses Levenshtein distance via pure-Python implementation (no jiwer
dependency).

Usage:
    # Stability check across the 26 duplicate-transcribed audio files
    python tools/wer_measure.py --mode cross-instance --output AI_Studio/Reports/scheduled/wer_xinstance.json

    # True WER vs reference (when references exist)
    python tools/wer_measure.py --mode against-reference \
        --hyps .cache/transcribed/...txt \
        --refs ref/...txt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
TRANSCRIBED_DIR = REPO_ROOT / ".cache" / "transcribed"
REPORT_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"


try:
    import Levenshtein as _Lev  # C extension; fast on long sequences
    _HAVE_LEV = True
except ImportError:
    _HAVE_LEV = False


def levenshtein(a: list[str], b: list[str]) -> int:
    """Token-sequence edit distance.

    Uses the C-extension ``Levenshtein`` library when available (orders of
    magnitude faster on multi-thousand-word transcripts); falls back to
    pure-Python DP otherwise.
    """
    if _HAVE_LEV:
        # Map tokens to single chars to use the C string-distance fast path.
        # python-Levenshtein supports list inputs natively via .editops, but
        # we want just the count — easiest via a synthetic char mapping.
        if not a:
            return len(b)
        if not b:
            return len(a)
        vocab: dict[str, int] = {}
        def encode(seq):
            return "".join(chr(0x4e00 + vocab.setdefault(t, len(vocab))) for t in seq)
        return _Lev.distance(encode(a), encode(b))
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


def normalize_transcript(text: str) -> str:
    """Strip our standard transcript header and normalize for WER comparison.

    Removes the 'Source:', 'Language:', 'Duration-sec:', etc. metadata header
    that faster-whisper writes before the actual transcript text.
    """
    lines = text.splitlines()
    # Find first blank line — content starts after that
    start = 0
    for i, line in enumerate(lines):
        if not line.strip():
            start = i + 1
            break
    body = "\n".join(lines[start:])
    # Lowercase, drop punctuation, collapse whitespace
    body = body.lower()
    body = re.sub(r"[^\w\s']", " ", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body


def words(text: str) -> list[str]:
    return text.split()


def chars(text: str) -> list[str]:
    return list(text.replace(" ", ""))


def compute_wer_cer(hyp_text: str, ref_text: str) -> dict:
    hyp_norm = normalize_transcript(hyp_text)
    ref_norm = normalize_transcript(ref_text)
    h_words = words(hyp_norm)
    r_words = words(ref_norm)
    h_chars = chars(hyp_norm)
    r_chars = chars(ref_norm)
    word_edits = levenshtein(h_words, r_words)
    char_edits = levenshtein(h_chars, r_chars)
    wer = word_edits / max(len(r_words), 1)
    cer = char_edits / max(len(r_chars), 1)
    return {
        "ref_words": len(r_words),
        "hyp_words": len(h_words),
        "ref_chars": len(r_chars),
        "hyp_chars": len(h_chars),
        "word_edits": word_edits,
        "char_edits": char_edits,
        "wer": round(wer, 4),
        "cer": round(cer, 4),
    }


def find_duplicate_transcript_pairs() -> list[tuple[str, list[Path]]]:
    """Return [(audio_basename, [path1, path2, ...])] for each audio file
    with 2+ independent transcripts under .cache/transcribed/."""
    by_name: dict[str, list[Path]] = defaultdict(list)
    for t in TRANSCRIBED_DIR.rglob("*.txt"):
        by_name[t.name].append(t)
    return [(name, paths) for name, paths in by_name.items() if len(paths) > 1]


def cross_instance_run(max_files: int | None = None) -> dict:
    """For each audio file with 2+ transcripts, compute pairwise WER between
    the first two distinct transcripts."""
    pairs = find_duplicate_transcript_pairs()
    if max_files:
        pairs = pairs[:max_files]
    results = []
    for name, paths in pairs:
        # Pick the two paths (deterministic order)
        a, b = sorted(paths)[:2]
        a_text = a.read_text(encoding="utf-8", errors="replace")
        b_text = b.read_text(encoding="utf-8", errors="replace")
        if hashlib.md5(a_text.encode()).hexdigest() == hashlib.md5(b_text.encode()).hexdigest():
            continue  # identical, skip
        metrics = compute_wer_cer(a_text, b_text)
        metrics["file"] = name
        metrics["a_path"] = str(a.relative_to(REPO_ROOT))
        metrics["b_path"] = str(b.relative_to(REPO_ROOT))
        results.append(metrics)
    if not results:
        return {"results": [], "summary": {"n": 0}}
    summary = {
        "n": len(results),
        "avg_wer": round(sum(r["wer"] for r in results) / len(results), 4),
        "avg_cer": round(sum(r["cer"] for r in results) / len(results), 4),
        "median_wer": round(sorted(r["wer"] for r in results)[len(results) // 2], 4),
        "p95_wer": round(sorted(r["wer"] for r in results)[int(len(results) * 0.95)], 4),
        "max_wer": round(max(r["wer"] for r in results), 4),
        "min_wer": round(min(r["wer"] for r in results), 4),
        "total_ref_words": sum(r["ref_words"] for r in results),
        "total_word_edits": sum(r["word_edits"] for r in results),
    }
    return {"results": results, "summary": summary}


def reference_run(hyp_paths: Iterable[Path], ref_paths: Iterable[Path]) -> dict:
    hyp_paths = list(hyp_paths)
    ref_paths = list(ref_paths)
    if len(hyp_paths) != len(ref_paths):
        raise SystemExit(f"hyp count ({len(hyp_paths)}) != ref count ({len(ref_paths)})")
    results = []
    for hp, rp in zip(hyp_paths, ref_paths):
        h = Path(hp).read_text(encoding="utf-8", errors="replace")
        r = Path(rp).read_text(encoding="utf-8", errors="replace")
        m = compute_wer_cer(h, r)
        m["hyp"] = str(hp)
        m["ref"] = str(rp)
        results.append(m)
    summary = {
        "n": len(results),
        "avg_wer": round(sum(r["wer"] for r in results) / len(results), 4) if results else None,
        "avg_cer": round(sum(r["cer"] for r in results) / len(results), 4) if results else None,
    }
    return {"results": results, "summary": summary}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=("cross-instance", "against-reference"), default="cross-instance")
    p.add_argument("--max-files", type=int, default=None)
    p.add_argument("--hyps", nargs="*")
    p.add_argument("--refs", nargs="*")
    p.add_argument("--output")
    args = p.parse_args()

    if args.mode == "cross-instance":
        out = cross_instance_run(max_files=args.max_files)
    else:
        if not args.hyps or not args.refs:
            print("--mode against-reference requires --hyps and --refs", file=sys.stderr)
            return 2
        out = reference_run(args.hyps, args.refs)

    s = out["summary"]
    print(f"=== WER {args.mode} ===")
    print(f"  files: {s['n']}")
    if s["n"]:
        print(f"  avg WER: {s.get('avg_wer')}  avg CER: {s.get('avg_cer')}")
        if "median_wer" in s:
            print(f"  median: {s['median_wer']}  p95: {s['p95_wer']}  max: {s['max_wer']}  min: {s['min_wer']}")
        if "total_ref_words" in s:
            print(f"  aggregate (across all files): {s['total_word_edits']}/{s['total_ref_words']} word edits")

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"\n[output] {args.output}")
    elif s["n"]:
        ts = time.strftime("%Y%m%d_%H%M%S")
        out_path = REPORT_DIR / f"wer_{args.mode}_{ts}.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"\n[output] {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

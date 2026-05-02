"""Inline-grounded citation extraction + substring verification.

Forensically-defensible citation pattern: every cited file path is paired with
a verbatim quoted span from that file. The scorer can then verify the quote
exists in the source via a deterministic substring match — no LLM needed for
the existence check. The semantic-support check (does the quote actually back
the claim?) is what the LLM judge handles.

This bypasses the single-chunk-fetch artifact that drives ~half the IRRELEVANT
verdicts in the standard span-correctness pipeline. The model tells us which
span it relied on; we don't have to guess.

Supported formats (we extract from answer text):

  Format A — colon-quote:        `path.md`: "quoted span"
  Format B — colon-states:       `path.md` states: "quoted span"
  Format C — quote-em-dash-path: "quoted span" — `path.md`
  Format D — quote-from-path:    "quoted span" (from `path.md`)
  Format E — markdown blockquote with cite line below:
                                 > quoted span
                                 > — path.md

Quotes use straight ASCII (") OR curly (“ ”) OR single ('). Any of these.

Public API:
    extract_inline_quotes(text) -> list[dict]
    verify_quote_in_file(quote, cite_path, fts_conn=None) -> dict
    score_inline_grounded(query, answer, fts_conn) -> dict   (no judge layer; that's in citation_scorer)

The verification check uses three fallbacks, in order:
    1. FTS index substring match (fast — ~1ms per check)
    2. Raw file substring match (handles content not in the index, e.g. attachments)
    3. Whitespace-normalized substring match (handles re-flowed line breaks in the answer)
"""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"
EXCLUDED_ROOT = Path("C:/Users/atayl/Desktop/Excluded")


# ---- Quote extraction ----

# Path-then-quote patterns. Three flavors so the inner character class only
# excludes the SAME quote type that opened — apostrophes inside double-quoted
# spans (e.g. "Adam's ADSCD") work correctly.
#
# The double-quote inner class is `(?:[^"\\\n]|\\.){8,400}` — matches any non-quote
# non-newline char, OR a backslash followed by any char (so \" inside a quoted
# span is captured as part of the span, not treated as the closing quote).
_PATTERN_PATH_THEN_DQUOTE = re.compile(
    r"`([^`\n]+\.[a-z]{1,5})`[\s\w:,'’]{0,120}?\"((?:[^\"\\\n]|\\.){8,400})\"",
    re.IGNORECASE,
)
_PATTERN_PATH_THEN_CURLY = re.compile(
    r"`([^`\n]+\.[a-z]{1,5})`[\s\w:,'’]{0,120}?[“]([^”\n]{8,400})[”]",
    re.IGNORECASE,
)
_PATTERN_PATH_THEN_SQUOTE = re.compile(
    r"`([^`\n]+\.[a-z]{1,5})`[\s\w:,'’]{0,120}?'((?:[^'\\\n]|\\.){8,400})'",
    re.IGNORECASE,
)

# Quote-then-path patterns (same three flavors).
_PATTERN_DQUOTE_THEN_PATH = re.compile(
    r"\"((?:[^\"\\\n]|\\.){8,400})\"[\s\w(,'’\-—–]{0,120}?`([^`\n]+\.[a-z]{1,5})`",
    re.IGNORECASE,
)
_PATTERN_CURLY_THEN_PATH = re.compile(
    r"[“]([^”\n]{8,400})[”][\s\w(,'’\-—–]{0,120}?`([^`\n]+\.[a-z]{1,5})`",
    re.IGNORECASE,
)
_PATTERN_SQUOTE_THEN_PATH = re.compile(
    r"'((?:[^'\\\n]|\\.){8,400})'[\s\w(,'’\-—–]{0,120}?`([^`\n]+\.[a-z]{1,5})`",
    re.IGNORECASE,
)


def _unescape_inner(quote: str) -> str:
    """Convert backslash-escaped inner quotes back to literal quotes for verification.

    Models commonly emit `\"` and `\'` inside quoted spans because they were
    trained on JSON or escaped contexts. The source file has the unescaped form,
    so we strip the escapes before substring-matching.
    """
    return (quote.replace('\\"', '"')
                 .replace("\\'", "'")
                 .replace("\\\\", "\\"))


_FORMATS_PATH_FIRST = [
    ("path-dquote", _PATTERN_PATH_THEN_DQUOTE),
    ("path-curly", _PATTERN_PATH_THEN_CURLY),
    ("path-squote", _PATTERN_PATH_THEN_SQUOTE),
]
_FORMATS_QUOTE_FIRST = [
    ("dquote-path", _PATTERN_DQUOTE_THEN_PATH),
    ("curly-path", _PATTERN_CURLY_THEN_PATH),
    ("squote-path", _PATTERN_SQUOTE_THEN_PATH),
]


def extract_inline_quotes(text: str) -> list[dict]:
    """Return [{"path", "quote", "span_in_text": (start, end), "format"}] for every
    inline-grounded citation found in ``text``.

    De-duplicates exact (path, quote) pairs.
    """
    found: list[dict] = []
    seen: set[tuple[str, str]] = set()

    for fmt_name, pattern in _FORMATS_PATH_FIRST:
        for m in pattern.finditer(text):
            path = m.group(1).strip()
            quote = m.group(2).strip()
            key = (path.lower(), quote.lower())
            if key in seen:
                continue
            seen.add(key)
            found.append({
                "path": path,
                "quote": quote,
                "span_in_text": (m.start(), m.end()),
                "format": fmt_name,
            })

    for fmt_name, pattern in _FORMATS_QUOTE_FIRST:
        for m in pattern.finditer(text):
            quote = m.group(1).strip()
            path = m.group(2).strip()
            key = (path.lower(), quote.lower())
            if key in seen:
                continue
            seen.add(key)
            found.append({
                "path": path,
                "quote": quote,
                "span_in_text": (m.start(), m.end()),
                "format": fmt_name,
            })

    return sorted(found, key=lambda r: r["span_in_text"][0])


# ---- Quote verification ----


def _normalize_for_match(s: str) -> str:
    """Collapse whitespace + lowercase + dash variants for fallback substring matching.

    Real-world docs have inconsistent dash characters (em-dash, en-dash, hyphen,
    Unicode replacement char from bad encoding reads). All collapse to a single
    plain hyphen for matching purposes.
    """
    s = s.lower()
    # Normalize all dash-like chars (em-dash, en-dash, minus, replacement) to "-"
    for ch in ("—", "–", "−", "�", "—", "–"):
        s = s.replace(ch, "-")
    return re.sub(r"[\s\-]+", " ", s).strip()


def _curly_to_straight(s: str) -> str:
    return s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")


def verify_quote_in_file(quote: str, cite_path: str,
                          fts_conn: sqlite3.Connection | None = None) -> dict:
    """Verify ``quote`` is verbatim present in ``cite_path``.

    Strategy:
      1. FTS index substring match against ``content`` column (fastest)
      2. Raw file substring match (if file resolvable on disk)
      3. Whitespace-normalized fallback (handles answer-side re-flow)

    Returns ``{"verified": bool, "method": str, "excerpt": str, "reason": str|None}``.
    """
    # Strip backslash-escapes the model added to inner quotes — source files
    # have the unescaped form. Then convert curly to straight for normalization.
    quote_clean = _curly_to_straight(_unescape_inner(quote)).strip()
    quote_norm = _normalize_for_match(quote_clean)

    # ---- Strategy 1: FTS index ----
    if fts_conn is not None:
        try:
            basename = cite_path.lower().replace("\\", "/").rsplit("/", 1)[-1]
            rows = fts_conn.execute(
                "SELECT content FROM chunks WHERE LOWER(rel_path) LIKE ? LIMIT 25",
                (f"%{basename}%",),
            ).fetchall()
            for (content,) in rows:
                content = content or ""
                if quote_clean in content:
                    idx = content.find(quote_clean)
                    return {
                        "verified": True,
                        "method": "fts_exact",
                        "excerpt": content[max(0, idx - 60): idx + len(quote_clean) + 60],
                        "reason": None,
                    }
                if quote_norm and quote_norm in _normalize_for_match(content):
                    return {
                        "verified": True,
                        "method": "fts_normalized",
                        "excerpt": _normalize_for_match(content)[
                            : 0 if not quote_norm else _normalize_for_match(content).find(quote_norm) + len(quote_norm) + 60
                        ][-200:],
                        "reason": None,
                    }
        except sqlite3.Error as e:
            return {"verified": False, "method": "fts_error", "excerpt": "", "reason": str(e)}

    # ---- Strategy 2: raw file on disk ----
    cand_paths = _resolve_cite_path(cite_path)
    for p in cand_paths:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except (OSError, UnicodeDecodeError):
            continue
        if quote_clean in text:
            idx = text.find(quote_clean)
            return {
                "verified": True,
                "method": "file_exact",
                "excerpt": text[max(0, idx - 60): idx + len(quote_clean) + 60],
                "reason": None,
            }
        if quote_norm and quote_norm in _normalize_for_match(text):
            text_norm = _normalize_for_match(text)
            idx = text_norm.find(quote_norm)
            return {
                "verified": True,
                "method": "file_normalized",
                "excerpt": text_norm[max(0, idx - 60): idx + len(quote_norm) + 60],
                "reason": None,
            }

    return {
        "verified": False,
        "method": "no_match",
        "excerpt": "",
        "reason": f"quote not found in any of {len(cand_paths)} candidate paths or FTS",
    }


def _resolve_cite_path(cite_path: str) -> list[Path]:
    """Return candidate absolute paths the citation could point to.

    Citations are usually relative ('Case_Reference/...md'), so we search:
    - EXCLUDED_ROOT joined with the cite as-is
    - EXCLUDED_ROOT/IMPORTANT DOCS/<cite>
    - REPO_ROOT joined with cite
    - .cache/extracted/**/<basename>.txt (for extracted-text fallback)
    """
    cite_path = cite_path.replace("\\", "/").lstrip("/")
    candidates: list[Path] = []
    bases = [
        EXCLUDED_ROOT,
        EXCLUDED_ROOT / "IMPORTANT DOCS",
        REPO_ROOT,
    ]
    for b in bases:
        candidates.append(b / cite_path)
    # Also try basename-glob in .cache/extracted as a last resort
    basename = cite_path.rsplit("/", 1)[-1]
    cache = REPO_ROOT / ".cache" / "extracted"
    if cache.exists():
        for p in cache.rglob(basename + ".txt"):
            candidates.append(p)
            if len(candidates) > 20:
                break
    return [p for p in candidates if p.exists()]


# ---- Per-answer scoring (path + existence; semantic-support is in citation_scorer.py) ----


def score_inline_grounded(query: str, answer: str,
                           fts_conn: sqlite3.Connection | None = None) -> dict:
    """Score the *path-existence* component of inline-grounded citations.

    Doesn't run the LLM judge — that lives in citation_scorer.score_answer with
    the right plumbing. This returns the substring-verification step that
    citation_scorer can use as the basis for the second-layer judge call.

    Returns:
        {
            "query": ...,
            "inline_quotes": [...],            # all extracted (path, quote) pairs
            "verified_count": int,             # how many had verbatim substring match
            "fabricated_count": int,           # how many failed verification (caught fabrication)
            "verification_rate": float,        # verified / total
            "verifications": [...]             # per-quote detail
        }
    """
    quotes = extract_inline_quotes(answer)
    verifications = []
    verified = 0
    fabricated = 0
    for q in quotes:
        v = verify_quote_in_file(q["quote"], q["path"], fts_conn=fts_conn)
        verifications.append({
            "path": q["path"],
            "quote": q["quote"][:200],
            "format": q["format"],
            **v,
        })
        if v["verified"]:
            verified += 1
        else:
            fabricated += 1
    n = len(quotes)
    return {
        "query": query,
        "inline_quotes": quotes,
        "verifications": verifications,
        "n_quotes": n,
        "verified_count": verified,
        "fabricated_count": fabricated,
        "verification_rate": round(verified / n, 4) if n else None,
    }


# CLI for quick checks
def _main():
    import argparse, json, sys
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    extract = sub.add_parser("extract", help="Extract inline quotes from --answer or --answer-file")
    extract.add_argument("--answer")
    extract.add_argument("--answer-file")
    verify = sub.add_parser("verify", help="Verify a single quote against a path")
    verify.add_argument("--quote", required=True)
    verify.add_argument("--path", required=True)
    score = sub.add_parser("score", help="Score an answer's inline grounding")
    score.add_argument("--query", required=True)
    score.add_argument("--answer-file", required=True)
    args = p.parse_args()

    if args.cmd == "extract":
        text = args.answer or Path(args.answer_file).read_text(encoding="utf-8")
        for q in extract_inline_quotes(text):
            print(json.dumps(q, ensure_ascii=False))
    elif args.cmd == "verify":
        conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True) if FTS_DB.exists() else None
        v = verify_quote_in_file(args.quote, args.path, fts_conn=conn)
        print(json.dumps(v, indent=2, ensure_ascii=False))
    elif args.cmd == "score":
        text = Path(args.answer_file).read_text(encoding="utf-8")
        conn = sqlite3.connect(f"file:{FTS_DB.as_posix()}?mode=ro", uri=True) if FTS_DB.exists() else None
        s = score_inline_grounded(args.query, text, fts_conn=conn)
        print(json.dumps(s, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    _main()

#!/usr/bin/env python3
"""Persistent extraction cache wrapper.

Extracts text from PDF/DOCX/EML/MSG files into a cache directory, keyed by
(path, mtime, size). Only re-extracts files that have changed since the last
run. Dramatically faster for repeated sweeps of the same source tree.

Shares extraction functions with tools/bulk_extract.py — any extractor added
there is automatically picked up here.

Usage:
    # Extract into default cache location
    python tools/extract_cache.py "C:/Users/atayl/Desktop/IMPORTANT DOCS"

    # Custom output dir
    python tools/extract_cache.py <src> --out .cache/my_cache/

    # Only show stats, don't extract
    python tools/extract_cache.py <src> --stats

    # Force full re-extraction (ignore cache)
    python tools/extract_cache.py <src> --force

    # Clean stale entries (files deleted from source)
    python tools/extract_cache.py <src> --clean

Cache layout:
    <cache_dir>/
        manifest.json              # {rel_path: {mtime, size, out_file, status}}
        files/                     # mirror of source tree, one .txt per file
            subdir1/
                file1.pdf.txt
            subdir2/
                file2.docx.txt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Reuse extractors from bulk_extract.py — add tools/ to sys.path so it imports
TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))
from bulk_extract import EXTRACTORS  # noqa: E402


DEFAULT_CACHE_ROOT = Path(__file__).resolve().parents[1] / ".cache" / "extracted"


def cache_dir_for(src: Path, custom: Path | None = None) -> Path:
    """Return a stable cache dir for a source tree."""
    if custom:
        return custom
    # Hash the absolute source path so different sources don't collide
    src_abs = str(src.resolve()).replace("\\", "/")
    h = hashlib.sha1(src_abs.encode("utf-8")).hexdigest()[:10]
    slug = src.name.replace(" ", "_") or "root"
    return DEFAULT_CACHE_ROOT / f"{slug}_{h}"


def load_manifest(cache_dir: Path) -> dict:
    mf = cache_dir / "manifest.json"
    if not mf.exists():
        return {"source": "", "entries": {}}
    try:
        return json.loads(mf.read_text(encoding="utf-8"))
    except Exception:
        return {"source": "", "entries": {}}


def save_manifest(cache_dir: Path, manifest: dict) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    mf = cache_dir / "manifest.json"
    mf.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


# Security filter — these filenames / folders are never extracted.
# Keeps credentials and recovery codes out of the RAG pipeline even if they
# end up somewhere under the source tree. Match is substring, case-insensitive.
_SECURITY_FILENAME_PATTERNS = (
    "pword", "password", "passwd",
    "recovery-codes", "recovery_codes",
    "backup-codes", "backup_codes",
    "credentials", "creds",
    ".env",
    "id_rsa", "id_ed25519", "id_ecdsa",
    "apikey", "api-key", "api_key",
    "private-key", "privatekey",
    "access-token", "access_token",
)
_SECURITY_FOLDER_NAMES = {"Credentials", "Secrets", ".ssh", ".gnupg"}


def _is_security_sensitive(rel_path: str) -> str | None:
    """Return reason string if this path should be skipped for security, else None."""
    name_lower = rel_path.rsplit("/", 1)[-1].lower()
    # Allow document-format discussion of credentials (PDFs, docx, md narratives)
    # but never extract raw text/env files with credential-like names.
    ext = os.path.splitext(name_lower)[1]
    if ext in {".pdf", ".docx", ".doc", ".md"}:
        return None
    for pat in _SECURITY_FILENAME_PATTERNS:
        if pat in name_lower:
            return f"credential pattern '{pat}'"
    for part in rel_path.split("/"):
        if part in _SECURITY_FOLDER_NAMES:
            return f"under security folder '{part}'"
    return None


# ---------------------------------------------------------------------------
# Security v2 — scan extracted text for embedded credentials
# Caught 'The Master.txt' class of leaks where a password appeared in a research
# note without the literal word 'password' preceding it.
# ---------------------------------------------------------------------------

import math as _math
import re as _re

_SECURITY_TEXT_PATTERNS = [
    _re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),                      # SSN
    _re.compile(r"(?i)\bpassword\s*[:=]\s*\S+"),                # password= / password:
    _re.compile(r"(?i)\bapi[_-]?key\s*[:=]\s*\S+"),
    _re.compile(r"(?i)\bsecret[_-]?key\s*[:=]\s*\S+"),
    _re.compile(r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    _re.compile(r"\bAKIA[0-9A-Z]{16}\b"),                       # AWS access key
    _re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._-]{20,}\b"),
    _re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),                    # GitHub PAT
    _re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),                    # OpenAI-style
]

# Tokens that mix letters/digits/special, 18+ chars, high entropy — password-shaped
_HIGH_ENTROPY_RE = _re.compile(r"[A-Za-z0-9!@#$%^&*()_+\-={}\[\]|\\:;\"'<>,.?/~`]{18,}")


def _shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    freq: dict[str, int] = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    total = len(s)
    return -sum((c / total) * _math.log2(c / total) for c in freq.values())


def scan_extracted_text(text: str, rel_path: str = "") -> str | None:
    """Post-extraction content scan. Returns reason if sensitive content detected."""
    # Only scan first 8KB to bound cost
    sample = text[:8192]
    for pat in _SECURITY_TEXT_PATTERNS:
        if pat.search(sample):
            return f"content pattern matched: {pat.pattern!r}"
    # Entropy fallback — flag any single token with 18+ chars and entropy >= 4.0
    for match in _HIGH_ENTROPY_RE.finditer(sample):
        tok = match.group(0)
        # Skip URLs
        if tok.startswith(("http://", "https://", "ftp://")):
            continue
        # Skip file paths (contain / or \) — paths are never credentials
        if "/" in tok or "\\" in tok:
            continue
        # Skip code snippets (contain parens, brackets, or common code tokens)
        if "(" in tok or ")" in tok or "=>" in tok or "::" in tok:
            continue
        # Skip markdown formatting (backticks, pipes)
        if "`" in tok or "||" in tok:
            continue
        # Skip filenames (tokens ending with a file extension are never credentials)
        if _re.search(r"\.(md|pdf|txt|docx|doc|eml|msg|sql|json|html|csv|py|cpp|h|log|conf|yaml|xml|jpg|png|bak|rtf|ini|bat|ps1|sh|toml|cfg)$", tok, _re.IGNORECASE):
            continue
        # Skip build configuration names (x64-Debug, x64-RelWithDebInfo, etc.)
        if tok.startswith(("x64-", "x86-", "arm64-")):
            continue
        if _shannon_entropy(tok) >= 4.0:
            # Must have ALL 4 character classes (upper + lower + digit + special)
            # to distinguish real passwords from sha256 hashes, model IDs,
            # file paths with underscores, and UUID-like strings.
            # Tuned after false-positive flood on memory/*.md files (session 258).
            has_upper = any(c.isupper() for c in tok)
            has_lower = any(c.islower() for c in tok)
            has_digit = any(c.isdigit() for c in tok)
            has_special = any(not c.isalnum() for c in tok)
            classes = sum([has_upper, has_lower, has_digit, has_special])
            if classes >= 4:
                return f"high-entropy token {classes}-class detected (18+ chars, entropy>=4.0)"
    return None


def scan_source(src: Path, include_exts: set[str]) -> dict[str, dict]:
    """Walk the source tree, return {rel_path: {mtime, size}} for matching files.

    Applies the security filter — credential/secret files are silently skipped
    and never enter the cache manifest.
    """
    out = {}
    security_skipped = 0
    for dirpath, _dirs, filenames in os.walk(src):
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext not in include_exts:
                continue
            abs_path = os.path.join(dirpath, fn)
            try:
                st = os.stat(abs_path)
            except OSError:
                continue
            rel = os.path.relpath(abs_path, src).replace("\\", "/")
            reason = _is_security_sensitive(rel)
            if reason:
                security_skipped += 1
                print(f"  SECURITY skip: {rel} ({reason})", file=sys.stderr)
                continue
            out[rel] = {
                "mtime": int(st.st_mtime),
                "size": st.st_size,
            }
    if security_skipped:
        print(f"  SECURITY: {security_skipped} file(s) refused", file=sys.stderr)
    return out


def extract_one(src: Path, rel_path: str, cache_files_dir: Path) -> tuple[str, bool, str]:
    """Extract a single file, write to cache. Returns (rel_path, ok, message).

    Applies post-extraction content scan (security v2) — if the extracted text
    contains SSN/credential/high-entropy patterns, refuses to write the cache
    file and logs a SECURITY event. This catches the 'The Master.txt' class
    where a filename-safe file has a password embedded on line 2.
    """
    abs_src = src / rel_path
    ext = abs_src.suffix.lower()
    extractor = EXTRACTORS.get(ext)
    if not extractor:
        return rel_path, False, f"no extractor for {ext}"
    try:
        text = extractor(str(abs_src))
    except Exception as e:
        return rel_path, False, f"extraction error: {e}"

    # Post-extraction security scan — catches embedded credentials
    security_reason = scan_extracted_text(text, rel_path)
    if security_reason:
        return rel_path, False, f"SECURITY-content: {security_reason}"

    out_file = cache_files_dir / (rel_path + ".txt")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    header = f"Source: {rel_path}\n\n"
    out_file.write_text(header + text, encoding="utf-8", newline="\n")
    return rel_path, True, "ok"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", help="Source directory to extract")
    parser.add_argument("--out", help="Cache directory (default: .cache/extracted/<slug>_<hash>/)")
    parser.add_argument("--types", default=".pdf,.docx,.eml,.msg,.doc,.md,.txt,.rtf",
                        help="Comma-separated extensions (default: all bulk_extract types including native-text passthrough)")
    parser.add_argument("--workers", type=int, default=8, help="Parallel workers (default: 8)")
    parser.add_argument("--stats", action="store_true", help="Show cache stats, no extraction")
    parser.add_argument("--force", action="store_true", help="Ignore cache, re-extract everything")
    parser.add_argument("--clean", action="store_true", help="Remove stale cache entries (files deleted from source)")
    args = parser.parse_args()

    src = Path(args.source).resolve()
    if not src.is_dir():
        print(f"ERROR: {src} is not a directory", file=sys.stderr)
        return 1

    cache_dir = cache_dir_for(src, Path(args.out).resolve() if args.out else None)
    files_dir = cache_dir / "files"
    files_dir.mkdir(parents=True, exist_ok=True)

    # Overlap detection — refuse to extract if src is a parent of an existing bucket
    # or a child of one. Overlapping source paths create duplicate chunks at index time.
    overlap_detected = []
    cache_root = DEFAULT_CACHE_ROOT
    if cache_root.exists():
        src_norm = str(src.resolve()).replace("\\", "/")
        for other in cache_root.iterdir():
            if other.resolve() == cache_dir.resolve():
                continue
            other_manifest = other / "manifest.json"
            if not other_manifest.exists():
                continue
            try:
                other_data = json.loads(other_manifest.read_text(encoding="utf-8"))
                other_src = str(Path(other_data.get("source", "")).resolve()).replace("\\", "/")
            except Exception:
                continue
            if not other_src:
                continue
            # Check: is src a parent of other_src, or other_src a parent of src?
            src_is_parent = other_src.startswith(src_norm + "/")
            src_is_child = src_norm.startswith(other_src + "/")
            if src_is_parent or src_is_child:
                overlap_detected.append({
                    "existing_bucket": other.name,
                    "existing_source": other_src,
                    "relation": "contains" if src_is_parent else "is contained by",
                })
    if overlap_detected:
        print("\nWARN: overlap with existing extraction bucket(s):", file=sys.stderr)
        for ov in overlap_detected:
            print(f"  {src} {ov['relation']} {ov['existing_source']}", file=sys.stderr)
            print(f"    (bucket: {ov['existing_bucket']})", file=sys.stderr)
        if not args.force:
            print("\nRun with --force to proceed anyway, or purge the overlapping bucket first.", file=sys.stderr)
            print("This refusal prevents the 462-duplicate incident from session 258.", file=sys.stderr)
            return 2

    include_exts = {e.strip().lower() for e in args.types.split(",") if e.strip()}
    missing_exts = include_exts - set(EXTRACTORS)
    if missing_exts:
        print(f"WARN: no extractor registered for: {sorted(missing_exts)}", file=sys.stderr)

    print(f"Source: {src}", file=sys.stderr)
    print(f"Cache:  {cache_dir}", file=sys.stderr)

    manifest = load_manifest(cache_dir)
    manifest["source"] = str(src)
    entries = manifest.get("entries", {})

    t0 = time.perf_counter()
    current = scan_source(src, include_exts)
    scan_elapsed = time.perf_counter() - t0

    # Classify
    new_files = []
    changed = []
    unchanged = []
    for rel, meta in current.items():
        prev = entries.get(rel)
        if args.force or prev is None:
            new_files.append(rel)
        elif prev.get("mtime") != meta["mtime"] or prev.get("size") != meta["size"]:
            changed.append(rel)
        else:
            unchanged.append(rel)

    deleted = [rel for rel in entries.keys() if rel not in current]

    print(f"Scan:      {len(current):>6} files ({scan_elapsed:.2f}s)", file=sys.stderr)
    print(f"  new:     {len(new_files):>6}", file=sys.stderr)
    print(f"  changed: {len(changed):>6}", file=sys.stderr)
    print(f"  cached:  {len(unchanged):>6}", file=sys.stderr)
    print(f"  deleted: {len(deleted):>6}", file=sys.stderr)

    if args.stats:
        return 0

    # Clean stale
    if args.clean or deleted:
        for rel in deleted:
            out_file = files_dir / (rel + ".txt")
            try:
                if out_file.exists():
                    out_file.unlink()
            except OSError:
                pass
            entries.pop(rel, None)
        if deleted:
            print(f"Cleaned {len(deleted)} stale entries", file=sys.stderr)

    # Extract new + changed
    to_extract = new_files + changed
    if not to_extract:
        print("Nothing to extract - cache is current.", file=sys.stderr)
        manifest["entries"] = entries
        manifest["last_run"] = int(time.time())
        save_manifest(cache_dir, manifest)
        return 0

    t0 = time.perf_counter()
    ok = 0
    failed = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(extract_one, src, rel, files_dir): rel for rel in to_extract}
        for fut in as_completed(futs):
            rel, success, msg = fut.result()
            meta = current[rel]
            entries[rel] = {
                "mtime": meta["mtime"],
                "size": meta["size"],
                "ok": success,
                "msg": msg if not success else "ok",
            }
            if success:
                ok += 1
            else:
                failed += 1
    elapsed = time.perf_counter() - t0
    rate = (ok + failed) / elapsed if elapsed else 0
    print(f"Extracted: {ok} ok, {failed} failed in {elapsed:.1f}s ({rate:.1f} files/s)", file=sys.stderr)

    manifest["entries"] = entries
    manifest["last_run"] = int(time.time())
    save_manifest(cache_dir, manifest)
    print(f"Cache ready: {files_dir}", file=sys.stderr)
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    sys.exit(main())

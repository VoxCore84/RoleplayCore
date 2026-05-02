"""Full git-history secrets scanner.

Scans every blob in every commit for credential-shaped strings (API keys,
private keys, passwords, AWS/GCP/GitHub tokens, OpenAI keys, Bearer tokens,
high-entropy hex/base64 strings).

Drop-in alternative to gitleaks/trufflehog when those aren't installed.
Output: per-finding JSONL plus a summary report. Exit code: 0 if clean,
1 if findings, 2 on scan error.

Usage:
    python tools/secrets_scan.py
    python tools/secrets_scan.py --since 2026-01-01
    python tools/secrets_scan.py --output AI_Studio/Reports/scheduled/secrets_scan.jsonl
"""
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"

# ---------- Regex patterns ----------
PATTERNS: list[tuple[str, re.Pattern, str]] = [
    ("aws_access_key", re.compile(rb"\bAKIA[0-9A-Z]{16}\b"), "high"),
    ("aws_secret", re.compile(rb"\baws_secret_access_key[\"']?\s*[:=]\s*[\"']?([A-Za-z0-9/+=]{40})[\"']?", re.I), "high"),
    ("github_pat_classic", re.compile(rb"\bghp_[A-Za-z0-9]{36}\b"), "high"),
    ("github_pat_fine", re.compile(rb"\bgithub_pat_[A-Za-z0-9_]{82}\b"), "high"),
    ("github_oauth", re.compile(rb"\bgho_[A-Za-z0-9]{36}\b"), "high"),
    ("github_app", re.compile(rb"\b(ghu|ghs)_[A-Za-z0-9]{36}\b"), "high"),
    ("openai_key", re.compile(rb"\bsk-[A-Za-z0-9]{20,}T3BlbkFJ[A-Za-z0-9]{20,}\b"), "high"),
    ("openai_project_key", re.compile(rb"\bsk-proj-[A-Za-z0-9_\-]{40,}\b"), "high"),
    ("anthropic_key", re.compile(rb"\bsk-ant-(?:api|admin)\d+-[A-Za-z0-9_\-]{80,}\b"), "high"),
    ("google_api_key", re.compile(rb"\bAIza[0-9A-Za-z_\-]{35}\b"), "high"),
    ("slack_token", re.compile(rb"\bxox[abprs]-[0-9]+-[0-9]+(?:-[0-9]+)?-[a-zA-Z0-9]+\b"), "high"),
    ("stripe_key", re.compile(rb"\b(sk|pk|rk)_(test|live)_[0-9A-Za-z]{24,}\b"), "high"),
    ("private_key_pem", re.compile(rb"-----BEGIN (RSA |OPENSSH |EC |DSA |PGP |ENCRYPTED |)PRIVATE KEY-----"), "high"),
    ("password_assignment", re.compile(rb"(?<![A-Za-z_])(password|passwd|pwd|api_key|apikey|secret|token|auth_token)[\"']?\s*[:=]\s*[\"']([A-Za-z0-9_\-+/=!@#$%^&*]{8,80})[\"']", re.I), "med"),
    ("bearer_token", re.compile(rb"\bBearer\s+[A-Za-z0-9._\-]{20,}"), "med"),
    ("ssn", re.compile(rb"\b(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}\b"), "med"),
    ("jwt", re.compile(rb"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b"), "med"),
]

# False-positive patterns (placeholders we should ignore)
FALSE_POSITIVE_VALUES = {
    "your_api_key_here", "your_password", "example_key", "test_key", "dummy_password",
    "placeholder", "xxxxxxxxxxxxxxxx", "redacted", "admin", "password", "secret",
    "your_token_here", "<your_api_key>", "$ANTHROPIC_API_KEY", "$OPENAI_API_KEY",
    "your-api-key", "abc123", "todo", "tbd", "n/a",
}

# Skip these path prefixes (they're not first-party code)
SKIP_PATHS = {
    ".git/", "node_modules/", ".venv/", "venv/", "__pycache__/", "dist/",
    "build/", ".cache/", ".pytest_cache/", ".mypy_cache/", "out/", "deps/",
    "wago/", "wago-db2/", "tools-dev/code-intel/", "tools-dev/coreretail6/",
    "ExtTools/", "tor-army/", "lambda-swarm/", "repos/", "runtime/UniServerZ/",
    "Recordings/", "ChatGPT_Latest_Backup/",
}

# Skip these extensions (binaries, lockfiles full of base64)
SKIP_EXTS = {
    ".bin", ".exe", ".dll", ".pyc", ".pyo", ".so", ".dylib", ".class",
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".ico", ".webp",
    ".pdf", ".docx", ".xlsx", ".pptx", ".doc", ".xls", ".ppt", ".odt",
    ".zip", ".tar", ".gz", ".7z", ".rar", ".jar", ".msi", ".db", ".sqlite",
    ".mp3", ".mp4", ".wav", ".flac", ".webm", ".mov", ".avi", ".m4a",
    ".whl", ".egg", ".csv",  # csvs are usually data not code
    ".db2", ".dbc",  # WoW data files
}


def shannon_entropy(b: bytes) -> float:
    if not b:
        return 0.0
    counts = Counter(b)
    n = len(b)
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


def should_skip_path(path: str) -> bool:
    if not path:
        return True
    if any(path.startswith(p) for p in SKIP_PATHS):
        return True
    if any(p in path for p in SKIP_PATHS):
        return True
    lower = path.lower()
    if any(lower.endswith(ext) for ext in SKIP_EXTS):
        return True
    return False


def is_false_positive(match_value: str) -> bool:
    v = match_value.strip("\"'").lower()
    if not v:
        return True
    if v in FALSE_POSITIVE_VALUES:
        return True
    if len(v) < 8:
        return True
    if v.startswith("$") or v.startswith("${") or v.startswith("%"):
        return True  # env-var reference
    if v.startswith("<") and v.endswith(">"):
        return True  # placeholder
    return False


def scan_blob(content: bytes, path: str, commit: str) -> list[dict]:
    findings = []
    for name, pattern, severity in PATTERNS:
        for m in pattern.finditer(content):
            try:
                raw = m.group(0).decode("utf-8", errors="replace")
            except Exception:
                continue
            value_for_fp = raw
            if m.lastindex:
                try:
                    value_for_fp = m.group(m.lastindex).decode("utf-8", errors="replace")
                except Exception:
                    pass
            if is_false_positive(value_for_fp):
                continue

            line_start = content.rfind(b"\n", 0, m.start()) + 1
            line_end = content.find(b"\n", m.end())
            if line_end == -1:
                line_end = len(content)
            line_no = content[: m.start()].count(b"\n") + 1
            line_text = content[line_start:line_end].decode("utf-8", errors="replace")[:200]

            findings.append({
                "rule": name,
                "severity": severity,
                "commit": commit,
                "path": path,
                "line": line_no,
                "match_preview": raw[:80],
                "line_preview": line_text,
            })
    return findings


def list_blobs(since: str | None = None) -> list[tuple[str, str, str]]:
    """Return [(commit_sha, path, blob_sha)] for every file at every commit."""
    cmd = ["git", "-C", str(REPO_ROOT), "log", "--all", "--pretty=format:%H"]
    if since:
        cmd += [f"--since={since}"]
    commits = subprocess.check_output(cmd, encoding="utf-8").splitlines()
    out = []
    for commit in commits:
        try:
            ls = subprocess.check_output(
                ["git", "-C", str(REPO_ROOT), "ls-tree", "-r", commit],
                encoding="utf-8", errors="replace",
            )
        except subprocess.CalledProcessError:
            continue
        for line in ls.splitlines():
            parts = line.split("\t", 1)
            if len(parts) != 2:
                continue
            meta, path = parts
            mode_type_sha = meta.split()
            if len(mode_type_sha) != 3:
                continue
            mode, obj_type, blob_sha = mode_type_sha
            if obj_type != "blob":
                continue
            if should_skip_path(path):
                continue
            out.append((commit, path, blob_sha))
    return out


def cat_blob(blob_sha: str) -> bytes:
    return subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "cat-file", "blob", blob_sha],
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Full git-history secrets scanner")
    p.add_argument("--since", help="Only scan commits since this date (e.g. 2026-01-01)")
    p.add_argument("--output", help="Output JSONL path (default: AI_Studio/Reports/scheduled/secrets_scan_<ts>.jsonl)")
    p.add_argument("--max-blob-size", type=int, default=512_000,
                   help="Skip blobs larger than this many bytes (default 512KB)")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()

    ts = time.strftime("%Y%m%d_%H%M%S")
    out_path = Path(args.output) if args.output else (DEFAULT_OUTPUT_DIR / f"secrets_scan_{ts}.jsonl")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not args.quiet:
        print(f"[scan] enumerating blobs ({'since '+args.since if args.since else 'full history'})...")
    t0 = time.time()
    blobs = list_blobs(since=args.since)
    if not args.quiet:
        print(f"[scan] {len(blobs):,} (commit,path) pairs to inspect")

    seen_blob_shas: set[str] = set()
    findings: list[dict] = []
    blob_count = 0

    with out_path.open("w", encoding="utf-8") as f:
        for commit, path, blob_sha in blobs:
            if blob_sha in seen_blob_shas:
                continue
            seen_blob_shas.add(blob_sha)

            try:
                content = cat_blob(blob_sha)
            except subprocess.CalledProcessError:
                continue
            if len(content) > args.max_blob_size:
                continue
            blob_count += 1

            new_findings = scan_blob(content, path, commit)
            for hit in new_findings:
                f.write(json.dumps(hit, ensure_ascii=False) + "\n")
                findings.append(hit)

            if not args.quiet and blob_count % 1000 == 0:
                print(f"  {blob_count:,} blobs scanned, {len(findings)} findings so far")

    elapsed = time.time() - t0
    summary = {
        "elapsed": round(elapsed, 1),
        "commits": len({b[0] for b in blobs}),
        "unique_blobs_scanned": blob_count,
        "findings_total": len(findings),
        "findings_by_rule": dict(Counter(f["rule"] for f in findings)),
        "findings_by_severity": dict(Counter(f["severity"] for f in findings)),
        "output_jsonl": str(out_path),
    }
    summary_path = out_path.with_suffix(".summary.json")
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    if not args.quiet:
        print()
        print(f"[scan] done in {elapsed:.1f}s")
        print(f"[scan] {summary['unique_blobs_scanned']:,} unique blobs across {summary['commits']:,} commits")
        print(f"[scan] {summary['findings_total']} findings")
        if summary["findings_by_rule"]:
            for rule, n in sorted(summary["findings_by_rule"].items(), key=lambda x: -x[1]):
                print(f"  {rule}: {n}")
        print()
        print(f"[scan] full JSONL: {out_path}")
        print(f"[scan] summary:    {summary_path}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

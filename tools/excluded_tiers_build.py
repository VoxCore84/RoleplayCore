#!/usr/bin/env python3
"""Build the Excluded/ digest pyramid — Tier 2 (per-document micro-digests) and Tier 3 (per-folder summaries).

Tier 2: one line per extracted document, max 90 chars, structured as
    <category> | <entities> | <one-sentence purpose>
Generated via Ollama local-llm (qwen2.5:7b or 27b), $0 per query.

Tier 3: one paragraph per top-level folder, merging Tier 2 lines for that folder
into a coherent summary. Also local-llm.

Tier 4 (optional): whole-corpus one-pager. Hand-curated or final local-llm pass.

Output locations:
    .cache/tiers/tier2_excluded.md        — one line per file, sorted by path
    .cache/tiers/tier3_excluded.md        — per-folder paragraphs
    .cache/tiers/tier_meta.json           — freshness tracking (sha256 per file)

Usage:
    python tools/excluded_tiers_build.py                   # incremental
    python tools/excluded_tiers_build.py --drop            # full rebuild
    python tools/excluded_tiers_build.py --stats
    python tools/excluded_tiers_build.py --tier 2          # only Tier 2
    python tools/excluded_tiers_build.py --tier 3          # only Tier 3
    python tools/excluded_tiers_build.py --limit 50        # only first 50 new files (testing)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXTRACT_ROOT = REPO_ROOT / ".cache" / "extracted"
TIERS_DIR = REPO_ROOT / ".cache" / "tiers"
TIER2_FILE = TIERS_DIR / "tier2_excluded.md"
TIER3_FILE = TIERS_DIR / "tier3_excluded.md"
META_FILE = TIERS_DIR / "tier_meta.json"

OLLAMA_URL = "http://localhost:11434"
TIER2_MODEL = os.environ.get("TIER2_MODEL", "qwen2.5:7b-instruct-q5_K_M")
TIER3_MODEL = os.environ.get("TIER3_MODEL", "qwen2.5:7b-instruct-q5_K_M")

MICRO_MAX_CHARS = 120
TIER2_PROMPT = """You will receive a legal/career/finance document. Write ONE line, max 120 characters, capturing:
- Document type (memo, email, regulation, clinical note, filing, form, letter, etc.)
- Key people/orgs mentioned (2-4 max)
- What the document is about, factually, in one phrase

Format: <type> | <people/orgs> | <factual subject>

Examples of correct output:
- email | Amy Little, Adam Taylor | HAF/A1ZA scheduling Teams call 13 Apr 2026
- memo | Capt Daniel Ko, Adam Taylor | VLC termination citing "case disposition completed" 30 Jan 2026
- clinical note | Dr Zander | PTSD therapy session #9, PCL-5 score 72, triggered by Referral OPB

Do NOT include adjectives, speculation, or filler. Just: type | people | subject.
Output ONLY the line — no preamble, no quotes, no explanation.

Document:
"""

TIER3_PROMPT = """You will receive a set of one-line micro-digests, one per document in a folder.
Write ONE paragraph (3-5 sentences, max 600 chars) that summarizes:
- What kind of material this folder contains
- Who the main actors are
- What the main threads/topics are
- What's most recent or most important

Write in past tense, third person, no hype. Factual briefing style.

Output ONLY the paragraph — no preamble, no headings.

Folder name: {folder}
Micro-digests:
"""


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()[:16]


def ollama_chat(prompt: str, model: str, timeout: int = 120) -> str | None:
    """Call Ollama /api/generate. Returns response text or None on error."""
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=json.dumps({
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 200},
        }).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("response", "").strip()
    except Exception as e:
        print(f"WARN: ollama call failed: {e}", file=sys.stderr)
        return None


def load_meta() -> dict:
    if META_FILE.exists():
        try:
            return json.loads(META_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"tier2": {}, "tier3": {}, "last_build": None}


def save_meta(meta: dict) -> None:
    TIERS_DIR.mkdir(parents=True, exist_ok=True)
    META_FILE.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def iter_cached_text_files():
    """Yield (bucket_name, rel_path, abs_path, source_tag)."""
    if not EXTRACT_ROOT.exists():
        return
    for bucket in sorted(EXTRACT_ROOT.iterdir()):
        files_dir = bucket / "files"
        if not files_dir.exists():
            continue
        # Read manifest to recover original source folder
        mf = bucket / "manifest.json"
        source = ""
        if mf.exists():
            try:
                source = json.loads(mf.read_text(encoding="utf-8")).get("source", "")
            except Exception:
                pass
        bucket_name = bucket.name
        for root, _dirs, filenames in os.walk(files_dir):
            for fn in filenames:
                if not fn.endswith(".txt"):
                    continue
                abs_path = Path(root) / fn
                rel_path = str(abs_path.relative_to(files_dir)).replace("\\", "/")
                yield bucket_name, rel_path, abs_path, source


def build_tier2(limit: int | None = None, drop: bool = False) -> int:
    TIERS_DIR.mkdir(parents=True, exist_ok=True)
    meta = {} if drop else load_meta()
    if drop:
        meta = {"tier2": {}, "tier3": {}, "last_build": None}

    files_processed = 0
    files_cached = 0
    files_failed = 0
    tier2_entries = dict(meta.get("tier2", {}))   # key → {line, sha, generated_at}

    t0 = time.perf_counter()
    for bucket_name, rel_path, abs_path, source in iter_cached_text_files():
        key = f"{bucket_name}::{rel_path}"
        try:
            sha = sha256_of(abs_path)
        except Exception:
            continue

        if key in tier2_entries and tier2_entries[key].get("sha") == sha:
            files_cached += 1
            continue

        try:
            text = abs_path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            files_failed += 1
            continue

        if len(text.strip()) < 60:
            # Too short to meaningfully summarize — use the text itself truncated
            line = text.strip().replace("\n", " ")[:MICRO_MAX_CHARS]
            tier2_entries[key] = {"line": line, "sha": sha, "source": source, "bucket": bucket_name, "rel_path": rel_path, "generated_at": int(time.time()), "model": "raw"}
            files_processed += 1
        else:
            # Truncate to first 6000 chars for the LLM prompt (enough context, bounded cost)
            snippet = text[:6000]
            prompt = TIER2_PROMPT + snippet
            response = ollama_chat(prompt, TIER2_MODEL, timeout=90)
            if response is None or not response.strip():
                files_failed += 1
                continue
            # Single-line, bounded length
            line = response.strip().split("\n")[0][:MICRO_MAX_CHARS]
            tier2_entries[key] = {
                "line": line,
                "sha": sha,
                "source": source,
                "bucket": bucket_name,
                "rel_path": rel_path,
                "generated_at": int(time.time()),
                "model": TIER2_MODEL,
            }
            files_processed += 1

        if files_processed % 25 == 0:
            elapsed = time.perf_counter() - t0
            print(f"  tier2 [{files_processed}+{files_cached}] {elapsed:.0f}s", file=sys.stderr)

        if limit and files_processed >= limit:
            break

    meta["tier2"] = tier2_entries
    meta["last_build"] = int(time.time())
    save_meta(meta)

    # Write tier2 markdown file
    lines = ["# Tier 2 — Micro-digests per document",
             f"_Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}, {len(tier2_entries)} entries_", ""]
    by_bucket: dict[str, list[tuple[str, str]]] = {}
    for key, entry in tier2_entries.items():
        by_bucket.setdefault(entry.get("bucket", "unknown"), []).append((entry.get("rel_path", ""), entry.get("line", "")))

    for bucket in sorted(by_bucket):
        lines.append(f"## {bucket}")
        for rel_path, line in sorted(by_bucket[bucket]):
            lines.append(f"- `{rel_path}` — {line}")
        lines.append("")
    TIER2_FILE.write_text("\n".join(lines), encoding="utf-8")

    elapsed = time.perf_counter() - t0
    print(f"Tier 2: {files_processed} generated, {files_cached} cached, {files_failed} failed in {elapsed:.1f}s", file=sys.stderr)
    print(f"Tier 2 file: {TIER2_FILE} ({TIER2_FILE.stat().st_size} bytes)", file=sys.stderr)
    return 0


def build_tier3() -> int:
    meta = load_meta()
    tier2 = meta.get("tier2", {})
    if not tier2:
        print("No Tier 2 data yet; run with --tier 2 first", file=sys.stderr)
        return 1

    TIERS_DIR.mkdir(parents=True, exist_ok=True)

    # Group by bucket
    by_bucket: dict[str, list[str]] = {}
    for entry in tier2.values():
        b = entry.get("bucket", "unknown")
        line = entry.get("line", "")
        if line:
            by_bucket.setdefault(b, []).append(line)

    # One Ollama call per bucket
    tier3_entries: dict[str, dict] = {}
    for bucket, lines in sorted(by_bucket.items()):
        # Truncate to first 80 lines per bucket to bound the prompt
        bucket_body = "\n".join(lines[:80])
        prompt = TIER3_PROMPT.format(folder=bucket) + bucket_body
        response = ollama_chat(prompt, TIER3_MODEL, timeout=120)
        if response is None:
            continue
        paragraph = response.strip().replace("\n\n", "\n")[:800]
        tier3_entries[bucket] = {
            "paragraph": paragraph,
            "line_count": len(lines),
            "generated_at": int(time.time()),
            "model": TIER3_MODEL,
        }
        print(f"  tier3 {bucket}: {len(paragraph)} chars from {len(lines)} lines", file=sys.stderr)

    meta["tier3"] = tier3_entries
    save_meta(meta)

    # Write tier3 markdown
    lines = ["# Tier 3 — Per-folder summaries",
             f"_Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}, {len(tier3_entries)} folders_", ""]
    for bucket, entry in sorted(tier3_entries.items()):
        lines.append(f"## {bucket}")
        lines.append(f"_{entry['line_count']} documents_")
        lines.append("")
        lines.append(entry["paragraph"])
        lines.append("")
    TIER3_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Tier 3: {len(tier3_entries)} folders summarized. File: {TIER3_FILE}", file=sys.stderr)
    return 0


def stats() -> int:
    meta = load_meta()
    tier2 = meta.get("tier2", {})
    tier3 = meta.get("tier3", {})
    print(f"Meta file: {META_FILE}")
    print(f"Last build: {meta.get('last_build')}")
    print(f"Tier 2 entries: {len(tier2)}")
    print(f"Tier 3 entries: {len(tier3)}")
    if TIER2_FILE.exists():
        print(f"Tier 2 md: {TIER2_FILE} ({TIER2_FILE.stat().st_size} bytes)")
    if TIER3_FILE.exists():
        print(f"Tier 3 md: {TIER3_FILE} ({TIER3_FILE.stat().st_size} bytes)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drop", action="store_true", help="Nuke meta and rebuild from scratch")
    ap.add_argument("--stats", action="store_true", help="Show current tier state and exit")
    ap.add_argument("--tier", type=int, choices=[2, 3], help="Only build specified tier")
    ap.add_argument("--limit", type=int, help="Cap files processed this run (testing)")
    args = ap.parse_args()

    if args.stats:
        return stats()

    if args.tier in (None, 2):
        rc = build_tier2(limit=args.limit, drop=args.drop)
        if rc != 0:
            return rc
    if args.tier in (None, 3):
        rc = build_tier3()
        if rc != 0:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())

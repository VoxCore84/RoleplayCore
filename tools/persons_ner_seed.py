#!/usr/bin/env python3
"""Auto-seed the persons roster from the extracted corpus via local NER.

Addresses critique item #4: hand-curating persons.json was the wrong first step.
This script uses local-llm (Ollama qwen2.5:7b or 27b) to extract person entities
from every extracted document, aggregates mentions, and produces a candidate
roster at .cache/persons/persons_candidates.json for user review.

User then promotes good entries into persons.json (merging with existing 25 hand-curated
canonical entries — aliases are appended, not replaced).

Run:
    python tools/persons_ner_seed.py               # scan all cached extractions
    python tools/persons_ner_seed.py --limit 100   # sample mode (testing)
    python tools/persons_ner_seed.py --min-mentions 3  # threshold for candidate inclusion
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXTRACT_ROOT = REPO_ROOT / ".cache" / "extracted"
ROSTER_DIR = REPO_ROOT / ".cache" / "persons"
CANDIDATES_OUT = ROSTER_DIR / "persons_candidates.json"
EXISTING_ROSTER = ROSTER_DIR / "persons.json"

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
# Default to whatever qwen is locally installed; user has qwen3.5:27b-q4_K_M
NER_MODEL = os.environ.get("NER_MODEL", "qwen3.5:27b-q4_K_M")

NER_PROMPT = """Extract all PERSON names mentioned in this legal/military document.
Rules:
- Include full names (first + last) with titles/ranks if present: "Capt Daniel Ko", "Col Johnston", "Dr Zander"
- Skip organizations, acronyms, places, dates, regulations
- Skip generic references like "the commander" or "a provider"
- One name per line. No extra text, no numbering, no commentary.
- Cap at 15 names. Most important first.

Document:
"""

# Heuristic filter — even the LLM occasionally emits non-person strings
_NON_PERSON_PATTERNS = re.compile(
    r"^(Department|Office|Agency|Staff|Board|Committee|Court|Command|Wing|Squadron|"
    r"Group|Division|Service|Air Force|Army|Navy|Marine|USAF|USAR|VA|DHA|DoD|IG|"
    r"OSC|AFOSI|SAPR|VLC|SARC|AFPC|HAF|NARSUM|MEB|PEBLO|ODC|ADC|ATS|TBI|PTSD)$",
    re.IGNORECASE,
)
_NAME_LIKE = re.compile(r"^[A-Z][a-zA-Z'-]+(?:\s+[A-Z][a-zA-Z'-]+)+$|^(?:Capt|Col|Maj|Lt|Gen|Sgt|Dr|Mr|Ms|Mrs|MSgt|SrA|VADM|SA)\b")


def ollama_generate(prompt: str, model: str, timeout: int = 90) -> str | None:
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=json.dumps({
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1, "num_predict": 400},
        }).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8")).get("response", "").strip()
    except Exception as e:
        print(f"  WARN: ollama call failed: {e}", file=sys.stderr)
        return None


def parse_names(response: str) -> list[str]:
    names = []
    for line in response.splitlines():
        line = line.strip().lstrip("-*•0123456789. )").strip()
        if not line or len(line) > 80:
            continue
        if _NON_PERSON_PATTERNS.match(line):
            continue
        if not _NAME_LIKE.match(line):
            continue
        names.append(line)
    return names


def canonical_key(name: str) -> str:
    """Collapse common variants: 'Capt Ko' and 'Capt Daniel Ko' share the 'ko' key."""
    tokens = re.findall(r"[A-Za-z]+", name)
    if not tokens:
        return name.lower()
    # Use last token (surname) as key; collapse common titles
    last = tokens[-1].lower()
    return last


def load_existing_roster() -> set[str]:
    """Return set of canonical surnames already in persons.json (lowercase)."""
    if not EXISTING_ROSTER.exists():
        return set()
    try:
        data = json.loads(EXISTING_ROSTER.read_text(encoding="utf-8"))
    except Exception:
        return set()
    known: set[str] = set()
    for p in data.get("persons", []):
        known.add(canonical_key(p["canonical"]))
        for alias in p.get("aliases", []):
            known.add(canonical_key(alias))
    return known


def iter_txt_files():
    if not EXTRACT_ROOT.exists():
        return
    for bucket in sorted(EXTRACT_ROOT.iterdir()):
        files_dir = bucket / "files"
        if not files_dir.exists():
            continue
        for dirpath, _dirs, filenames in os.walk(files_dir):
            for fn in filenames:
                if fn.endswith(".txt"):
                    yield Path(dirpath) / fn


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, help="Max files to scan (testing)")
    ap.add_argument("--min-mentions", type=int, default=2,
                    help="Minimum mention count to include as candidate (default 2)")
    ap.add_argument("--include-known", action="store_true",
                    help="Include names already in persons.json (useful for mention-count audit)")
    args = ap.parse_args()

    ROSTER_DIR.mkdir(parents=True, exist_ok=True)
    known = load_existing_roster() if not args.include_known else set()
    if known:
        print(f"Loaded {len(known)} known surnames from existing roster", file=sys.stderr)

    mentions: dict[str, int] = defaultdict(int)
    variants: dict[str, set[str]] = defaultdict(set)
    sources: dict[str, set[str]] = defaultdict(set)

    files = list(iter_txt_files())
    if args.limit:
        files = files[: args.limit]
    print(f"Scanning {len(files)} extracted text files", file=sys.stderr)

    t0 = time.perf_counter()
    for i, path in enumerate(files, 1):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if len(text.strip()) < 120:
            continue
        # Truncate to first 6000 chars for the LLM prompt (cost bound)
        response = ollama_generate(NER_PROMPT + text[:6000], NER_MODEL, timeout=60)
        if not response:
            continue
        for name in parse_names(response):
            key = canonical_key(name)
            if key in known:
                continue
            mentions[key] += 1
            variants[key].add(name)
            sources[key].add(str(path.relative_to(EXTRACT_ROOT)))
        if i % 25 == 0:
            elapsed = time.perf_counter() - t0
            print(f"  [{i}/{len(files)}] {elapsed:.0f}s — {len(mentions)} unique candidates", file=sys.stderr)

    # Rank + filter
    candidates = []
    for key, count in sorted(mentions.items(), key=lambda kv: -kv[1]):
        if count < args.min_mentions:
            continue
        candidates.append({
            "surname_key": key,
            "mention_count": count,
            "variants_seen": sorted(variants[key]),
            "sample_sources": sorted(sources[key])[:5],
        })

    CANDIDATES_OUT.write_text(json.dumps({
        "generated_at": int(time.time()),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "files_scanned": len(files),
        "total_candidates": len(candidates),
        "min_mentions_threshold": args.min_mentions,
        "candidates": candidates,
    }, indent=2, default=str), encoding="utf-8")

    elapsed = time.perf_counter() - t0
    print(f"\nDone in {elapsed:.1f}s — {len(candidates)} candidates with ≥{args.min_mentions} mentions", file=sys.stderr)
    print(f"Output: {CANDIDATES_OUT}", file=sys.stderr)
    print("\nTop 10 candidates:", file=sys.stderr)
    for c in candidates[:10]:
        print(f"  {c['mention_count']:3}x  {c['surname_key']:20}  variants={c['variants_seen'][:3]}", file=sys.stderr)
    print("\nReview candidates and promote into .cache/persons/persons.json with aliases + role + org.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

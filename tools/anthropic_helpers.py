"""Reusable Anthropic API cost-reduction helpers — prompt caching, batch, cost math.

OPT-IN. Importing tools adopt these to cut cost without changing default behavior.
Nothing here makes a live API call unless you pass a client AND dry_run=False.

The standalone tools (citation_scorer, quality_probe, review_cycle) make their own
`anthropic.Anthropic()` calls, so the global `ENABLE_PROMPT_CACHING_1H` set for the
Claude Code session does NOT apply to them — they must add cache_control explicitly.
That's what `cached_system()` is for.

Self-test:  python tools/anthropic_helpers.py --selftest
"""
from __future__ import annotations

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Pricing (USD per Mtok) — mirror of config/backend_selection.yaml backends.
# Kept inline so this helper has no hard YAML dependency; refresh if prices move.
PRICING = {
    "claude-opus-4-7": {"in": 15.0, "out": 75.0},
    "claude-sonnet-4-6": {"in": 3.0, "out": 15.0},
    "claude-haiku-4-5-20251001": {"in": 1.0, "out": 5.0},
}
# Anthropic cache economics: cache WRITE costs 1.25x base input; cache READ costs 0.1x.
CACHE_WRITE_MULT = 1.25
CACHE_READ_MULT = 0.10


def cache_control_block(text: str, ttl: str = "5m") -> dict:
    """A single system/content block tagged for prompt caching.

    ttl: "5m" (default ephemeral) or "1h" (extended; requires the 1h cache beta).
    Pass the returned block inside a list as `system=[block, ...]`.
    """
    block = {"type": "text", "text": text, "cache_control": {"type": "ephemeral"}}
    if ttl and ttl != "5m":
        block["cache_control"]["ttl"] = ttl
    return block


def cached_system(text: str, ttl: str = "5m") -> list[dict]:
    """Wrap a system prompt as a cache-eligible block list.

    Use for the LARGE, STABLE prefix that repeats across many calls (a judge
    rubric, a reviewer persona, a fixed instruction set). Put per-call variation
    in the user message, never in the cached system block.
    """
    return [cache_control_block(text, ttl=ttl)]


def estimate_cache_savings(system_tokens: int, n_calls: int, model: str,
                           cache_hit_rate: float = 0.9) -> dict:
    """Estimate $ for repeating a fixed system prompt across n_calls, cached vs not.

    Only models the SYSTEM-prefix input cost (the part caching helps). Per-call
    user-input and output costs are unaffected by caching and excluded here.
    """
    price = PRICING.get(model)
    if not price:
        raise KeyError(f"no pricing for model '{model}'. Known: {sorted(PRICING)}")
    in_rate = price["in"] / 1_000_000  # per token

    uncached = system_tokens * in_rate * n_calls

    # Cached: first call writes (1.25x); subsequent hits read (0.1x).
    hits = max(0, round(n_calls * cache_hit_rate) - 1)
    misses = n_calls - hits
    cached = (system_tokens * in_rate * CACHE_WRITE_MULT * misses
              + system_tokens * in_rate * CACHE_READ_MULT * hits)

    saved = uncached - cached
    return {
        "model": model,
        "system_tokens": system_tokens,
        "n_calls": n_calls,
        "cache_hit_rate": cache_hit_rate,
        "uncached_usd": round(uncached, 4),
        "cached_usd": round(cached, 4),
        "saved_usd": round(saved, 4),
        "saved_pct": round(100 * saved / uncached, 1) if uncached else 0.0,
    }


def build_batch(requests: list[dict]) -> list[dict]:
    """Shape a list of {custom_id, params} into Message Batches request items.

    `params` is the normal messages.create(...) kwargs dict (model, max_tokens,
    system, messages, ...). Returns the list ready for messages.batches.create.
    """
    items = []
    for i, r in enumerate(requests):
        cid = r.get("custom_id") or f"req-{i}"
        if "params" not in r:
            raise ValueError(f"request {cid} missing 'params'")
        items.append({"custom_id": cid, "params": r["params"]})
    return items


def submit_batch(requests: list[dict], *, client=None, dry_run: bool = True,
                 out_path: str | None = None) -> dict:
    """Submit a Message Batch, or (default) DRY-RUN: save the request and return.

    Batch API is ~50% cheaper than synchronous calls and is ideal for the
    quality_probe 50-query sweep and citation_scorer --batch. By DEFAULT this
    does NOT submit — it serializes the batch so you can inspect it first.
    """
    items = build_batch(requests)
    if dry_run or client is None:
        path = Path(out_path) if out_path else PROJECT_ROOT / "AI_Studio" / "Reports" / "batch_dryrun.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(items, indent=2, default=str), encoding="utf-8")
        return {"submitted": False, "n_requests": len(items), "dry_run_file": str(path)}
    batch = client.messages.batches.create(requests=items)
    return {"submitted": True, "n_requests": len(items), "batch_id": batch.id}


def _selftest() -> None:
    blk = cached_system("RUBRIC PREFIX", ttl="1h")
    assert blk[0]["cache_control"]["type"] == "ephemeral"
    assert blk[0]["cache_control"]["ttl"] == "1h"
    assert blk[0]["text"] == "RUBRIC PREFIX"

    est = estimate_cache_savings(system_tokens=2000, n_calls=50, model="claude-sonnet-4-6")
    assert est["uncached_usd"] > est["cached_usd"] > 0
    assert 0 < est["saved_pct"] < 100

    items = build_batch([{"custom_id": "q1", "params": {"model": "x", "messages": []}}])
    assert items[0]["custom_id"] == "q1"

    res = submit_batch([{"params": {"model": "x", "messages": []}}], dry_run=True,
                       out_path=str(PROJECT_ROOT / "AI_Studio" / "Reports" / "batch_dryrun_selftest.json"))
    assert res["submitted"] is False and res["n_requests"] == 1

    print("anthropic_helpers self-test: PASS")
    print("  example cache savings (2000-tok system, 50 calls, Sonnet):")
    print("   ", json.dumps(est))


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Anthropic cost-reduction helpers")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--estimate", nargs=3, metavar=("SYS_TOKENS", "N_CALLS", "MODEL"),
                    help="print cache-savings estimate")
    args = ap.parse_args()
    if args.estimate:
        print(json.dumps(estimate_cache_savings(int(args.estimate[0]), int(args.estimate[1]),
                                                 args.estimate[2]), indent=2))
    else:
        _selftest()

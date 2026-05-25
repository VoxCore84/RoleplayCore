"""Model router — wires the (previously inert) config/backend_selection.yaml.

Reads the per-operation backend assignments and resolves each operation to a
concrete backend, honoring availability (local Ollama reachable? cloud key
present?), primary/fallback, and the `local_required` refuse-to-run rule.

This is OPT-IN: importing tools call `select_backend("operation_name")` to get
the configured backend instead of hardcoding a model. Nothing changes until a
tool adopts it. The CLI `--print` is a dry-run that shows the full routing table
with cost estimates — no API calls, no side effects.

Usage:
    python tools/model_router.py --print            # full routing table (dry-run)
    python tools/model_router.py --operation judge_citation
    python tools/model_router.py --print --assume-local-down   # what falls back

Programmatic:
    from tools.model_router import select_backend
    be = select_backend("synthesis_personal_corpus")
    # -> {"operation":..., "backend":"sonnet_4_6", "model":"claude-sonnet-4-6",
    #     "kind":"cloud_anthropic", "available":True, "reason":..., "cost":{...}}
"""
from __future__ import annotations

import argparse
import os
import socket
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "config" / "backend_selection.yaml"

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise SystemExit("PyYAML required: pip install pyyaml") from e


def load_config(path: Path = CONFIG_PATH) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"backend config not found: {path}")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def probe_local(host: str = "127.0.0.1", port: int = 11434, timeout: float = 2.0) -> bool:
    """True if a local Ollama (or compatible) endpoint accepts a TCP connection."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def probe_cloud() -> bool:
    """True if an Anthropic API key is reachable (env or the project .env)."""
    if os.environ.get("ANTHROPIC_API_KEY"):
        return True
    for env_path in (PROJECT_ROOT / "tools" / "ai_studio" / ".env", PROJECT_ROOT / "config" / ".env"):
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                if line.strip().startswith("ANTHROPIC_API_KEY=") and line.split("=", 1)[1].strip():
                    return True
    return False


def _backend_cost(be: dict) -> dict:
    """Normalize a backend's cost fields into a small dict for display."""
    if be.get("kind") == "local":
        return {"per_call_usd": be.get("cost_per_call_usd", 0.0)}
    return {
        "in_per_mtok_usd": be.get("cost_input_per_mtok_usd"),
        "out_per_mtok_usd": be.get("cost_output_per_mtok_usd"),
    }


def select_backend(operation: str, *, force: str | None = None, config: dict | None = None,
                   local_up: bool | None = None, cloud_up: bool | None = None) -> dict:
    """Resolve an operation to a concrete backend, honoring availability + fallback.

    `force` overrides the choice with a named backend. `local_up`/`cloud_up` let
    callers (and the CLI) inject availability instead of probing live.
    """
    cfg = config or load_config()
    ops = cfg.get("operations", {})
    backends = cfg.get("backends", {})
    if operation not in ops:
        raise KeyError(f"unknown operation '{operation}'. Known: {sorted(ops)}")

    if local_up is None:
        local_up = probe_local()
    if cloud_up is None:
        cloud_up = probe_cloud()

    op = ops[operation]
    primary = force or op.get("primary")
    fallback = op.get("fallback")
    local_required = operation in cfg.get("availability", {}).get("local_required_operations", [])

    def _is_up(name: str) -> bool:
        b = backends.get(name, {})
        return local_up if b.get("kind") == "local" else cloud_up

    chosen, reason = primary, "primary"
    if not force and primary in backends and not _is_up(primary):
        if local_required:
            return {
                "operation": operation, "backend": None, "available": False,
                "reason": f"local-required op but primary '{primary}' unavailable "
                          f"(refuse-to-run by policy)",
                "model": None, "kind": None, "cost": {},
            }
        if fallback and _is_up(fallback):
            chosen, reason = fallback, f"fallback (primary '{primary}' unavailable)"
        else:
            chosen, reason = primary, f"primary '{primary}' UNAVAILABLE and no usable fallback"

    be = backends.get(chosen, {})
    return {
        "operation": operation,
        "backend": chosen,
        "model": be.get("model", chosen),
        "kind": be.get("kind"),
        "available": _is_up(chosen) if chosen in backends else False,
        "reason": reason,
        "privacy": op.get("privacy"),
        "prompt": op.get("prompt"),
        "override_env": op.get("override_env"),
        "cost": _backend_cost(be),
    }


def routing_table(config: dict | None = None, local_up: bool | None = None,
                  cloud_up: bool | None = None) -> list[dict]:
    cfg = config or load_config()
    if local_up is None:
        local_up = probe_local()
    if cloud_up is None:
        cloud_up = probe_cloud()
    rows = []
    for op in cfg.get("operations", {}):
        rows.append(select_backend(op, config=cfg, local_up=local_up, cloud_up=cloud_up))
    return rows


def _fmt_cost(cost: dict) -> str:
    if "per_call_usd" in cost:
        return f"${cost['per_call_usd']:.3f}/call (local)"
    i, o = cost.get("in_per_mtok_usd"), cost.get("out_per_mtok_usd")
    return f"${i}/${o} per Mtok in/out" if i is not None else "n/a"


def main() -> None:
    ap = argparse.ArgumentParser(description="Model router (reads backend_selection.yaml)")
    ap.add_argument("--print", action="store_true", help="print full routing table (dry-run)")
    ap.add_argument("--operation", help="resolve a single operation")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--assume-local-down", action="store_true", help="simulate Ollama unreachable")
    ap.add_argument("--assume-cloud-down", action="store_true", help="simulate no API key")
    args = ap.parse_args()

    cfg = load_config()
    local_up = False if args.assume_local_down else probe_local()
    cloud_up = False if args.assume_cloud_down else probe_cloud()

    if args.operation:
        res = select_backend(args.operation, config=cfg, local_up=local_up, cloud_up=cloud_up)
        if args.json:
            import json
            print(json.dumps(res, indent=2))
        else:
            print(f"{res['operation']}: -> {res['backend']} ({res['model']}) "
                  f"[{res['kind']}, available={res['available']}] {res['reason']}")
        return

    rows = routing_table(cfg, local_up=local_up, cloud_up=cloud_up)
    if args.json:
        import json
        print(json.dumps(rows, indent=2))
        return

    print(f"Backend routing  (local_up={local_up}, cloud_up={cloud_up})")
    print(f"config: {CONFIG_PATH}")
    print(f"{'OPERATION':28} {'-> BACKEND':18} {'AVAIL':6} {'PRIVACY':8} COST")
    print("-" * 96)
    for r in rows:
        avail = "yes" if r["available"] else "NO"
        print(f"{r['operation']:28} {str(r['backend']):18} {avail:6} "
              f"{str(r['privacy']):8} {_fmt_cost(r['cost'])}")
    unavailable = [r["operation"] for r in rows if not r["available"]]
    if unavailable:
        print(f"\nUNAVAILABLE ({len(unavailable)}): {', '.join(unavailable)}")
    print("\nDry-run only -- no API calls, no config changes. Tools opt in via "
          "`from tools.model_router import select_backend`.")


if __name__ == "__main__":
    main()

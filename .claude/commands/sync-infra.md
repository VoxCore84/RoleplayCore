# /sync-infra — Cross-project infrastructure drift audit + sync

## Arguments
- `--apply` — actually sync (default is dry-run audit)
- `--only <category>` — rules | hooks | commands | agents | tools
- `--audit` — full bidirectional drift report (no changes)

## What it does

Compares `.claude/` infrastructure between CalmCore and VoxCore:
- **rules/** — shared behavioral rules
- **hooks/** — shared automation hooks
- **commands/** — shared slash commands (respects CalmCore=WoW, VoxCore=non-WoW)
- **agents/** — agent definitions
- **tools/*.py** — shared Python utilities

## Instructions

### Step 1: Run the sync script in audit mode

```bash
python tools/sync_claude_config.py 2>&1
```

This runs a dry-run by default showing what WOULD be synced from VoxCore → CalmCore.

### Step 1b: Hook configuration sync check

```bash
python ~/.claude/hooks/check_hook_sync.py
```

Compares the `hooks` sections of VoxCore and CalmCore `settings.json` — reports missing events, missing hook entries, and count mismatches. Ignores expected differences (FileChanged matchers). Exit code 0 = in sync, 1 = drift detected.

### Step 2: Bidirectional audit (what the script doesn't cover)

Also check reverse direction — CalmCore-only items that VoxCore might need:

```bash
# Commands only in CalmCore but not VoxCore (WoW-specific = expected, generic = drift)
comm -23 <(ls C:/Users/atayl/CalmCore/.claude/commands/ | sort) <(ls C:/Users/atayl/VoxCore/.claude/commands/ | sort)

# Commands only in VoxCore but not CalmCore (non-WoW = expected, generic = drift)
comm -13 <(ls C:/Users/atayl/CalmCore/.claude/commands/ | sort) <(ls C:/Users/atayl/VoxCore/.claude/commands/ | sort)

# Hooks that differ
for f in C:/Users/atayl/CalmCore/.claude/hooks/*.py; do
  b=$(basename "$f")
  vc="C:/Users/atayl/VoxCore/.claude/hooks/$b"
  if [ -f "$vc" ]; then
    if ! diff -q "$f" "$vc" > /dev/null 2>&1; then
      echo "DIVERGED: hooks/$b"
    fi
  else
    echo "CC-ONLY: hooks/$b"
  fi
done

# Tools that differ
for f in C:/Users/atayl/CalmCore/tools/*.py; do
  b=$(basename "$f")
  vc="C:/Users/atayl/VoxCore/tools/$b"
  if [ -f "$vc" ]; then
    if ! diff -q "$f" "$vc" > /dev/null 2>&1; then
      echo "DIVERGED: tools/$b ($(wc -c < "$f") vs $(wc -c < "$vc") bytes)"
    fi
  fi
done
```

### Step 3: Present findings

Report in this format:

```
## Infrastructure Drift Report

### Identical (no action)
- N rules, N hooks, N commands, N agents

### Diverged (need reconciliation)
| File | CC size | VC size | Newer |

### CC-only (expected if WoW-specific)
| File | Category | WoW? |

### VC-only (expected if non-WoW)
| File | Category | Non-WoW? |

### Recommendation
- [list of copies/syncs needed]
```

### Step 4: Apply (if user says --apply)

If the user passed `--apply`, run:
```bash
python tools/sync_claude_config.py --apply 2>&1
```

Then for any reverse-direction items the user approved, copy them manually.

## Architectural principle

- **CalmCore = WoW only** (server code, ExtTools, wago, addons, WoW skills)
- **VoxCore = non-WoW** (legal, career, finances, brand, case work)
- **Shared infrastructure** lives in both: hooks, generic rules, generic commands (checkpoint, verify, wrap-up, status, retro, etc.)
- **Source of truth for shared infra**: VoxCore (it's the older, more developed project)

## When to run

- After any session that adds new commands, hooks, agents, or tools
- After `sync_claude_config.py` is updated with new shared file lists
- Monthly as part of infrastructure hygiene

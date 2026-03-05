# Hotfix Redundancy Audit Tools

Identifies and removes **redundant rows** from TrinityCore's hotfix database by comparing every hotfix table against authoritative DBC/DB2 baselines extracted from the WoW client.

In the March 2026 audit against build 66220, this pipeline reduced the hotfix DB from **10.8M rows to ~240K rows** (97.8% reduction), dramatically improving login time and server memory usage.

## How It Works

The audit classifies every hotfix row into one of four categories:

| Category | Meaning | Action |
|----------|---------|--------|
| **Redundant** | Identical to DBC baseline | DELETE — the client already has this data |
| **Override** | Differs from DBC baseline | KEEP — this is a genuine server-side correction |
| **New** | Not in DBC at all | KEEP — custom content or community data (e.g., broadcast_text) |
| **Negative Build** | VerifiedBuild < 0 | KEEP — TC uses negative builds as deletion markers |

## Prerequisites

1. **wow.tools.local (WTL)** — Local WoW client CASC browser for extracting DB2 files
2. **DBC2CSV** — Converts extracted DB2 binary files to CSV format
3. **MySQL** — Access to the hotfix database (pymysql)
4. **Python 3.10+** with `pymysql` installed
5. **Wago tooling** — `table_hashes.py` from the wago scripts directory (for hotfix_data cleanup)

## 3-Step Process

### Step 1: Build Column Mappings (Discover)

```bash
python build_table_info_r3.py
```

Generates `table_info_r3.json` — maps every hotfix DB column to its corresponding DBC CSV column. Handles:
- Array index mapping (DB `Foo1` -> CSV `Foo[0]`, 1-indexed to 0-indexed)
- Coordinate mapping (DB `PosX/Y/Z` -> CSV `Pos[0]/[1]/[2]`)
- Column renames between TC schema and Blizzard DB2 names (28 global + 23 table-specific aliases)
- Custom logical primary keys (e.g., `broadcast_text_duration` uses `(BroadcastTextID, Locale)` not `ID`)
- MySQL column type extraction for type-aware comparison

**Input**: `table_info.json` (R1 discovery), `tables_r2.json` (R2 table list), `col_types.json` (MySQL types)
**Output**: `table_info_r3.json`

### Step 2: Diff Against Baseline (Diff)

```bash
python hotfix_differ_r3.py --config table_info_r3.json --tables spell_name,item_sparse,...
```

Compares every row in each hotfix table against the DBC CSV baseline. Type-aware comparison:
- **Float32**: IEEE 754 bit-level comparison via `struct.pack('f')` — handles MySQL FLOAT precision loss
- **Integer**: Exact comparison with unsigned/signed int32 equivalence (same 32-bit pattern)
- **Text**: Exact string comparison with `_lang` suffix NULL/empty normalization

**Input**: `table_info_r3.json`, WTL CSV files, MySQL hotfix DB
**Output**: Per-table JSON results in `results_r3/` with classification of every row

### Step 3: Generate Cleanup SQL (Cleanup)

```bash
python gen_practical_sql_r3.py
```

Reads all results and generates cleanup SQL:
- **TRUNCATE** for 100% redundant tables (most efficient)
- **Batched DELETE** with IN clauses for partially redundant tables (500 IDs per batch)
- **hotfix_data cleanup** for truncated tables (removes corresponding registry entries)
- Full PK (ID + VerifiedBuild) used when same ID has both redundant and override rows

**Input**: `results_r3/*.json`
**Output**: `hotfix_cleanup_round3.sql`

### Merge Results (Optional)

```bash
python merge_results.py
```

Aggregates per-table JSON results into a summary report and generates the initial one-DELETE-per-row cleanup SQL. Primarily used in R1; the `gen_practical_sql_r3.py` generator produces more efficient SQL for later rounds.

## Running a Full Audit Against a New Build

1. Extract DB2 files from the WoW client using wow.tools.local
2. Convert to CSV using DBC2CSV
3. Update `CSV_DIR` in `hotfix_differ_r3.py` and `WTL_DIR` in `build_table_info_r3.py`
4. Run `build_table_info_r3.py` to generate new column mappings
5. Run `hotfix_differ_r3.py` in batches (use `groups_r3.json` or similar grouping)
6. Run `gen_practical_sql_r3.py` to generate cleanup SQL
7. Take a snapshot: `python db_snapshot.py snapshot --db hotfixes --label pre-cleanup`
8. Apply the cleanup SQL
9. Verify with spot checks

## File Overview

| File | Purpose |
|------|---------|
| `hotfix_differ_r3.py` | Type-aware row differ (final version) |
| `gen_practical_sql_r3.py` | Efficient cleanup SQL generator (TRUNCATE + batched DELETE) |
| `build_table_info_r3.py` | Column mapping builder with array index + coordinate fixes |
| `merge_results.py` | Result aggregator and report generator |
| `build_hash_map.py` | Table name to hotfix_data TableHash mapping |
| `build_mapping_bidirectional.py` | Bidirectional column mapping discovery |
| `extract_and_hash.py` | Hash-based table matching utility |
| `final_mapping.py` | Final column mapping consolidation |
| `optimized_mapping.py` | Optimized column mapping with caching |
| `reverse_hash.py` | Reverse lookup from TableHash to table name |
| `gen_inventory_report.py` | Detailed inventory report generator |
| `prep_r3_groups.py` | Batch grouping for R3 processing |

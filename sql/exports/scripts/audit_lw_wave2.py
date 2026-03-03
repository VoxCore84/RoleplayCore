"""
audit_lw_wave2.py — Compare LoreWalkerTDB world.sql against our world DB
for wave-2 tables. Parses the mysqldump line by line, counting INSERT rows
and sampling data for quality checks.

Usage: python audit_lw_wave2.py
"""

import re
import sys
import random
import subprocess
import json
from collections import defaultdict

LW_PATH = r"C:\Users\atayl\OneDrive\Desktop\Excluded\LoreWalkerTDB\LoreWalkerTDB\world.sql"
MYSQL = r"C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe"

TABLES = [
    "creature_queststarter",
    "creature_questender",
    "gameobject_queststarter",
    "gameobject_questender",
    "trainer",
    "trainer_spell",
    "npc_spellclick_spells",
    "vehicle_template_accessory",
    "creature_onkill_reputation",
    "creature_template_movement",
    "spell_area",
    "disables",
    "spawn_group",
    "conversation_actors",
    "conversation_line_template",
    "conversation_template",
    "reference_loot_template",
    "skinning_loot_template",
    "pickpocketing_loot_template",
    "npc_vendor",
    "gossip_menu",
    "gossip_menu_option",
    "quest_offer_reward",
    "quest_request_items",
    "areatrigger_template",
    "gameobject_addon",
    "creature_template_addon",
    "creature_addon",
]

OUR_COUNTS = {
    "creature_queststarter": 26386,
    "creature_questender": 33122,
    "gameobject_queststarter": 1463,
    "gameobject_questender": 1448,
    "trainer": 1014,
    "trainer_spell": 33402,
    "npc_spellclick_spells": 831,
    "vehicle_template_accessory": 492,
    "creature_onkill_reputation": 2020,
    "creature_template_movement": 9930,
    "spell_area": 964,
    "disables": 5300,
    "spawn_group": 91484,
    "conversation_actors": 117,
    "conversation_line_template": 585,
    "conversation_template": 178,
    "reference_loot_template": 13812,
    "skinning_loot_template": 2755,
    "pickpocketing_loot_template": 9556,
    "npc_vendor": 165859,
    "gossip_menu": 17086,
    "gossip_menu_option": 13987,
    "quest_offer_reward": 17513,
    "quest_request_items": 11675,
    "areatrigger_template": 4454,
    "gameobject_addon": 26424,
    "creature_template_addon": 27925,
    "creature_addon": 83311,
}

# We'll track: row counts, sampled raw row strings (up to 1000 per table)
lw_counts = defaultdict(int)
lw_samples = defaultdict(list)  # table -> list of raw value tuples as strings

# Also capture CREATE TABLE columns for quality analysis
lw_columns = {}  # table -> list of column names


def parse_values_count(line):
    """Count the number of value tuples in an INSERT line.
    Each tuple starts with '(' after VALUES or after '),'.
    This is much faster than full regex parsing."""
    # Count occurrences of '),(' plus 1 for the first tuple
    # This works because mysqldump escapes literal '),' inside strings
    count = line.count("),(") + 1
    return count


def sample_values(line, table, max_samples=1000):
    """Extract a sample of value tuples from an INSERT line using reservoir sampling."""
    current = lw_samples[table]
    current_count = lw_counts[table]  # count BEFORE this line

    # Find the start of VALUES
    vals_idx = line.find("VALUES (")
    if vals_idx == -1:
        return

    start = vals_idx + 7  # position of first '('

    # Parse tuples — we need to handle quoted strings with escaped chars
    tuples = []
    depth = 0
    tuple_start = -1
    i = start
    in_string = False

    while i < len(line):
        ch = line[i]
        if ch == '\\' and in_string:
            i += 2  # skip escaped char
            continue
        if ch == "'":
            in_string = not in_string
        elif not in_string:
            if ch == '(':
                if depth == 0:
                    tuple_start = i
                depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0 and tuple_start >= 0:
                    tuples.append(line[tuple_start:i+1])
                    tuple_start = -1
                    # Reservoir sampling: keep up to max_samples
                    if len(current) < max_samples:
                        current.append(tuples[-1])
                    else:
                        # Replace with decreasing probability
                        idx = current_count + len(tuples)
                        j = random.randint(0, idx - 1)
                        if j < max_samples:
                            current[j] = tuples[-1]
                    # For very large tables, stop parsing after collecting enough candidates
                    if len(tuples) > max_samples * 3:
                        break
        i += 1


def parse_create_columns(lines_buffer, table):
    """Extract column names from a CREATE TABLE statement."""
    cols = []
    for line in lines_buffer:
        line = line.strip()
        if line.startswith('`'):
            col_name = line.split('`')[1]
            cols.append(col_name)
    lw_columns[table] = cols


def main():
    print(f"Parsing LoreWalkerTDB world.sql ({LW_PATH})...")
    print(f"Target tables: {len(TABLES)}")
    print()

    table_set = set(TABLES)
    current_create_table = None
    create_buffer = []

    # Regex for INSERT INTO `table_name`
    insert_re = re.compile(r"^INSERT INTO `(\w+)`")
    create_re = re.compile(r"^CREATE TABLE `(\w+)`")

    line_num = 0
    tables_found = set()

    with open(LW_PATH, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line_num += 1
            if line_num % 500000 == 0:
                print(f"  ...line {line_num:,} (found {len(tables_found)}/{len(TABLES)} tables so far)")

            # Track CREATE TABLE for column info
            m = create_re.match(line)
            if m:
                tbl = m.group(1)
                if tbl in table_set:
                    current_create_table = tbl
                    create_buffer = []
                else:
                    current_create_table = None
                continue

            if current_create_table:
                if line.strip().startswith(')'):
                    parse_create_columns(create_buffer, current_create_table)
                    current_create_table = None
                else:
                    create_buffer.append(line)
                continue

            # Check for INSERT lines
            if not line.startswith('INSERT'):
                continue

            m = insert_re.match(line)
            if not m:
                continue

            tbl = m.group(1)
            if tbl not in table_set:
                continue

            tables_found.add(tbl)

            # Count rows
            count = parse_values_count(line)

            # Sample values for quality check (only for tables where we need it)
            if len(lw_samples[tbl]) < 1000:
                sample_values(line, tbl)

            lw_counts[tbl] += count

    print(f"\nParsing complete. {line_num:,} lines processed.")
    print(f"Found {len(tables_found)}/{len(TABLES)} tables.\n")

    missing_tables = table_set - tables_found
    if missing_tables:
        print(f"Tables NOT found in LW dump: {sorted(missing_tables)}\n")

    # Quality checks for tables with >100 extra rows
    quality_notes = {}

    for tbl in TABLES:
        lw = lw_counts.get(tbl, 0)
        ours = OUR_COUNTS.get(tbl, 0)
        diff = lw - ours

        if diff > 100 and lw_samples.get(tbl):
            samples = lw_samples[tbl]
            cols = lw_columns.get(tbl, [])
            notes = []

            # Check for non-zero primary keys (first field in tuple)
            zero_pk_count = 0
            empty_count = 0
            for s in samples:
                # Extract first value
                inner = s[1:-1]  # strip parens
                # Get first field
                if inner.startswith("'"):
                    # string field
                    end = inner.find("'", 1)
                    while end > 0 and inner[end-1] == '\\':
                        end = inner.find("'", end+1)
                    first_val = inner[1:end] if end > 0 else inner
                else:
                    comma = inner.find(',')
                    first_val = inner[:comma] if comma > 0 else inner

                if first_val in ('0', 'NULL', "''", ''):
                    zero_pk_count += 1

                # Check if mostly zeros/empty
                fields = []
                # Simple field split (imperfect but good enough for spot check)
                in_str = False
                field_start = 0
                for ci in range(len(inner)):
                    c = inner[ci]
                    if c == '\\' and in_str:
                        continue
                    if c == "'":
                        in_str = not in_str
                    elif c == ',' and not in_str:
                        fields.append(inner[field_start:ci])
                        field_start = ci + 1
                fields.append(inner[field_start:])

                zero_fields = sum(1 for fv in fields if fv.strip() in ('0', 'NULL', "''", "' '", ''))
                if len(fields) > 0 and zero_fields / len(fields) > 0.8:
                    empty_count += 1

            n_samples = len(samples)
            if zero_pk_count > n_samples * 0.5:
                notes.append(f"{zero_pk_count}/{n_samples} samples have zero/NULL PK")
            if empty_count > n_samples * 0.3:
                notes.append(f"{empty_count}/{n_samples} samples mostly empty")

            if not notes:
                notes.append(f"OK — {n_samples} samples checked, data looks meaningful")

            quality_notes[tbl] = "; ".join(notes)

    # Special check: conversation_actors — check if actor entries reference existing creature_templates
    if "conversation_actors" in lw_samples and lw_counts.get("conversation_actors", 0) > 0:
        samples = lw_samples["conversation_actors"]
        cols = lw_columns.get("conversation_actors", [])
        print("--- conversation_actors deep check ---")
        print(f"  Columns: {cols}")
        print(f"  Sample rows: {len(samples)}")

        # Extract CreatureId values from samples
        # conversation_actors columns: ConversationId, ConversationActorId, ActivePlayerObject,
        #   NoActorObject, CreatureId, CreatureDisplayInfoId, ConversationActorGuid, ...
        creature_ids = set()
        if cols:
            # Find CreatureId column index
            cid_idx = None
            for ci, cn in enumerate(cols):
                if cn.lower() in ('creatureid', 'creature_id'):
                    cid_idx = ci
                    break

            if cid_idx is not None:
                for s in samples:
                    inner = s[1:-1]
                    fields = []
                    in_str = False
                    field_start = 0
                    for i in range(len(inner)):
                        c = inner[i]
                        if c == '\\' and in_str:
                            continue
                        if c == "'":
                            in_str = not in_str
                        elif c == ',' and not in_str:
                            fields.append(inner[field_start:i].strip())
                            field_start = i + 1
                    fields.append(inner[field_start:].strip())

                    if cid_idx < len(fields):
                        val = fields[cid_idx]
                        if val not in ('0', 'NULL'):
                            creature_ids.add(val)

                print(f"  Unique non-zero CreatureIds in samples: {len(creature_ids)}")

                if creature_ids:
                    # Check against our world DB
                    id_list = ",".join(sorted(creature_ids))
                    query = f"SELECT id FROM creature_template WHERE entry IN ({id_list})"
                    # Actually, creature_template PK is 'entry'
                    query = f"SELECT COUNT(*) as found FROM creature_template WHERE entry IN ({id_list})"
                    try:
                        result = subprocess.run(
                            [MYSQL, "-u", "root", "-padmin", "world", "-N", "-e", query],
                            capture_output=True, text=True, timeout=30
                        )
                        found = result.stdout.strip()
                        print(f"  Of {len(creature_ids)} creature IDs, {found} exist in our creature_template")

                        # Also check which ones are missing
                        query2 = f"SELECT entry FROM creature_template WHERE entry IN ({id_list})"
                        result2 = subprocess.run(
                            [MYSQL, "-u", "root", "-padmin", "world", "-N", "-e", query2],
                            capture_output=True, text=True, timeout=30
                        )
                        existing = set(result2.stdout.strip().split('\n')) if result2.stdout.strip() else set()
                        missing = creature_ids - existing
                        if missing:
                            print(f"  Missing creature IDs: {sorted(missing)[:20]}{'...' if len(missing) > 20 else ''}")

                        quality_notes["conversation_actors"] = (
                            quality_notes.get("conversation_actors", "") +
                            f"; CreatureId check: {found}/{len(creature_ids)} exist in our DB"
                        )
                    except Exception as e:
                        print(f"  MySQL check failed: {e}")
            else:
                print(f"  Could not find CreatureId column (cols: {cols})")

        # Print some sample rows
        print(f"  First 5 sample rows:")
        for s in samples[:5]:
            print(f"    {s[:200]}")
        print()

    # Print comparison table
    print()
    print("=" * 120)
    print(f"{'Table':<35} {'Ours':>10} {'LW':>10} {'Diff':>10} {'%':>8}  Quality Notes")
    print("-" * 120)

    significant = []

    for tbl in TABLES:
        lw = lw_counts.get(tbl, 0)
        ours = OUR_COUNTS.get(tbl, 0)
        diff = lw - ours
        pct = f"{(diff/ours*100):+.1f}%" if ours > 0 else "N/A"

        note = quality_notes.get(tbl, "")
        if lw == 0:
            note = "NOT IN LW DUMP"
        elif diff <= 100:
            note = "~same" if abs(diff) <= 100 else ""

        marker = " ***" if diff > 100 else ""
        print(f"{tbl:<35} {ours:>10,} {lw:>10,} {diff:>+10,} {pct:>8}  {note}{marker}")

        if diff > 100:
            significant.append((tbl, ours, lw, diff, note))

    print("-" * 120)

    # Summary
    print(f"\nTables with >100 new rows in LW: {len(significant)}")
    if significant:
        print()
        for tbl, ours, lw, diff, note in sorted(significant, key=lambda x: -x[3]):
            print(f"  {tbl}: +{diff:,} rows ({ours:,} -> {lw:,})  {note}")

    print("\nDone.")


if __name__ == "__main__":
    main()

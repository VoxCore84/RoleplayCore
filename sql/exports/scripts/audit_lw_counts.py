"""
Audit LoreWalkerTDB world.sql row counts.

Scans the mysqldump file for INSERT statements and counts rows per table.
Handles extended INSERT format (one INSERT with millions of rows separated by ),(
"""
import re
import sys
import time

LW_DUMP = r"C:\Users\atayl\OneDrive\Desktop\Excluded\LoreWalkerTDB\LoreWalkerTDB\world.sql"

# We parse line-by-line for memory efficiency on an 897MB file.
# mysqldump format:
#   LOCK TABLES `table_name` WRITE;
#   INSERT INTO `table_name` VALUES (...),(...),(...);
#   (possibly multiple INSERT statements per table)
#   UNLOCK TABLES;
#
# Row counting strategy: for each INSERT line, count occurrences of "),("
# plus 1 (since N rows have N-1 separators). But we must be careful about
# values containing "),(" as string literals.
#
# A more robust approach: count the number of top-level value tuples by
# tracking parentheses depth outside of string literals.

def count_rows_in_insert_line(line):
    """
    Count rows in an INSERT INTO ... VALUES (...),(...),(...),...; line.

    We find the VALUES keyword, then count top-level tuples by tracking
    parenthesis depth and string quoting.
    """
    # Find "VALUES " (case-insensitive)
    values_idx = line.upper().find("VALUES ")
    if values_idx == -1:
        # Try VALUES( without space
        values_idx = line.upper().find("VALUES(")
        if values_idx == -1:
            return 0
        pos = values_idx + 6  # skip "VALUES"
    else:
        pos = values_idx + 7  # skip "VALUES "

    row_count = 0
    length = len(line)

    while pos < length:
        c = line[pos]
        if c == '(':
            # Start of a tuple — count it
            row_count += 1
            # Now skip to the matching close paren, respecting strings
            depth = 1
            pos += 1
            while pos < length and depth > 0:
                c = line[pos]
                if c == '(':
                    depth += 1
                elif c == ')':
                    depth -= 1
                elif c == "'":
                    # Skip string literal
                    pos += 1
                    while pos < length:
                        c2 = line[pos]
                        if c2 == '\\':
                            pos += 2  # skip escaped char
                            continue
                        if c2 == "'":
                            break
                        pos += 1
                pos += 1
        elif c == ';':
            break
        else:
            pos += 1

    return row_count


def main():
    start = time.time()

    table_counts = {}
    current_table = None
    lines_processed = 0
    insert_lines_found = 0

    print(f"Reading {LW_DUMP} ...")
    print(f"File size: scanning...", flush=True)

    with open(LW_DUMP, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            lines_processed += 1

            if lines_processed % 500000 == 0:
                elapsed = time.time() - start
                print(f"  ... {lines_processed:,} lines processed ({elapsed:.1f}s)", flush=True)

            # Detect table context
            if line.startswith("LOCK TABLES "):
                m = re.match(r"LOCK TABLES `(\w+)` WRITE;", line)
                if m:
                    current_table = m.group(1)
                    if current_table not in table_counts:
                        table_counts[current_table] = 0
                continue

            if line.startswith("INSERT INTO ") or line.startswith("INSERT IGNORE INTO "):
                insert_lines_found += 1
                # Extract table name from INSERT
                m = re.match(r"INSERT (?:IGNORE )?INTO `(\w+)`", line)
                if m:
                    tbl = m.group(1)
                    if tbl not in table_counts:
                        table_counts[tbl] = 0
                    rows = count_rows_in_insert_line(line)
                    table_counts[tbl] += rows
                continue

    elapsed = time.time() - start
    print(f"\nDone. {lines_processed:,} lines, {insert_lines_found} INSERT statements, {elapsed:.1f}s\n")

    # Print all tables sorted
    print(f"{'Table':<50} {'LW Rows':>12}")
    print("-" * 64)
    for tbl in sorted(table_counts.keys()):
        print(f"{tbl:<50} {table_counts[tbl]:>12,}")

    print(f"\nTotal tables found: {len(table_counts)}")
    print(f"Total rows: {sum(table_counts.values()):,}")

    # Now print the focused comparison table
    our_counts = {
        "creature_template": 225657,
        "creature_template_difficulty": 502651,
        "creature_template_spell": 9450,
        "creature_template_model": 355834,
        "creature_equip_template": 39178,
        "creature_template_addon": 27925,
        "creature_addon": 83311,
        "creature": 661901,
        "creature_text": 52641,
        "gameobject_template": 85405,
        "gameobject": 188567,
        "gameobject_template_addon": 44124,
        "gameobject_addon": 26424,
        "smart_scripts": 292732,
        "waypoint_path": 9038,
        "waypoint_path_node": 160784,
        "conditions": 26540,
        "spell_script_names": 3519,
        "creature_formations": 2764,
        "gossip_menu": 17086,
        "gossip_menu_option": 13987,
        "npc_vendor": 165859,
        "quest_template": 47164,
        "quest_template_addon": 46997,
        "quest_offer_reward": 17513,
        "quest_request_items": 11675,
        "game_event": 89,
        "game_event_creature": 2761,
        "game_event_gameobject": 33750,
        "pool_template": 2139,
        "pool_members": 11782,
        "spawn_group_template": 556,
        "spawn_group": 91484,
        "phase_area": 6974,
        "scene_template": 844,
        "conversation_template": 178,
        "conversation_actors": 117,
        "conversation_line_template": 585,
        "creature_loot_template": 2948661,
        "gameobject_loot_template": 63894,
        "reference_loot_template": 13812,
        "skinning_loot_template": 2755,
        "pickpocketing_loot_template": 9556,
        "areatrigger_template": 4454,
    }

    print(f"\n{'='*80}")
    print(f"COMPARISON: Our DB vs LoreWalkerTDB")
    print(f"{'='*80}")
    print(f"{'Table':<40} {'Ours':>12} {'LW':>12} {'Diff':>12} {'%':>8}")
    print("-" * 86)

    for tbl in sorted(our_counts.keys()):
        ours = our_counts[tbl]
        lw = table_counts.get(tbl, 0)
        diff = lw - ours
        if ours > 0:
            pct = (diff / ours) * 100
            pct_str = f"{pct:+.1f}%"
        else:
            pct_str = "N/A"

        marker = ""
        if diff > 0:
            marker = " <-- LW has more"
        elif diff < 0:
            marker = " <-- We have more"

        print(f"{tbl:<40} {ours:>12,} {lw:>12,} {diff:>+12,} {pct_str:>8}{marker}")

    # Also list tables in LW that we didn't compare
    lw_only = set(table_counts.keys()) - set(our_counts.keys())
    if lw_only:
        print(f"\n{'='*80}")
        print(f"Additional tables in LW dump (not in comparison list):")
        print(f"{'='*80}")
        print(f"{'Table':<50} {'LW Rows':>12}")
        print("-" * 64)
        for tbl in sorted(lw_only):
            if table_counts[tbl] > 0:
                print(f"{tbl:<50} {table_counts[tbl]:>12,}")


if __name__ == "__main__":
    main()

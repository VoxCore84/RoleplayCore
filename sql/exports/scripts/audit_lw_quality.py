#!/usr/bin/env python3
"""
audit_lw_quality.py — Audit LoreWalkerTDB data quality before importing.

Parses the 897MB world.sql mysqldump and evaluates data quality for 6 key tables:
1. creature_template_difficulty — placeholder/empty row detection
2. creature_loot_template — item existence, reference vs direct, drop chance sanity
3. gameobject_loot_template — same checks
4. quest_template_addon — meaningful data vs empty rows
5. creature (spawns) — template existence, coordinate sanity
6. smart_scripts — source_type breakdown, action diversity

Compares primary keys against our live world DB to find what's NEW (not duplicate).

Usage: python audit_lw_quality.py
"""

import subprocess
import sys
import time
import os
from collections import Counter, defaultdict

# ── Config ──────────────────────────────────────────────────────────────────
LW_DUMP = r"C:\Users\atayl\OneDrive\Desktop\Excluded\LoreWalkerTDB\LoreWalkerTDB\world.sql"
MYSQL_BIN = r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe"
MYSQL_USER = "root"
MYSQL_PASS = "admin"
MYSQL_DB = "world"
SAMPLE_LIMIT = 10_000  # max rows to parse per table for quality checks
FULL_COUNT_LIMIT = 0   # 0 = count all rows (just count, don't parse)


def mysql_query(sql):
    """Run a MySQL query and return rows as list of tuples."""
    cmd = [MYSQL_BIN, "-u", MYSQL_USER, f"-p{MYSQL_PASS}", MYSQL_DB,
           "--batch", "--skip-column-names", "-e", sql]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        stderr = result.stderr.strip()
        if "Warning" not in stderr or result.returncode != 0:
            # Filter out password warning
            lines = [l for l in stderr.split('\n') if 'password' not in l.lower()]
            if lines and result.returncode != 0:
                print(f"  [MySQL ERROR] {' '.join(lines)}")
                return []
    rows = []
    for line in result.stdout.strip().split('\n'):
        if line:
            rows.append(tuple(line.split('\t')))
    return rows


def mysql_query_set(sql):
    """Run a MySQL query and return a set of first-column values."""
    rows = mysql_query(sql)
    return {r[0] for r in rows if r}


# ── String-aware mysqldump row parser ───────────────────────────────────────
def parse_mysqldump_rows(line, max_rows=0):
    """
    Parse a mysqldump extended INSERT line into rows of string values.
    Handles quoted strings with escaped characters, NULL, and numeric values.

    line: "INSERT INTO `table` VALUES (v1,v2,...),(v1,v2,...),...;\n"
    Returns list of tuples of string values.
    """
    # Find start of VALUES
    idx = line.find("VALUES ")
    if idx == -1:
        return []
    idx += 7  # skip "VALUES "

    rows = []
    row_count = 0
    length = len(line)

    while idx < length:
        # Skip whitespace
        while idx < length and line[idx] in ' \t\r\n':
            idx += 1
        if idx >= length:
            break

        # Expect '('
        if line[idx] != '(':
            break
        idx += 1  # skip '('

        # Parse values within this row
        values = []
        while idx < length:
            # Skip whitespace
            while idx < length and line[idx] in ' \t':
                idx += 1
            if idx >= length:
                break

            ch = line[idx]

            if ch == ')':
                # End of row
                idx += 1
                break
            elif ch == ',':
                # Separator between values
                idx += 1
                continue
            elif ch == "'":
                # Quoted string
                idx += 1  # skip opening quote
                val_parts = []
                while idx < length:
                    c = line[idx]
                    if c == '\\':
                        # Escaped character
                        idx += 1
                        if idx < length:
                            val_parts.append(line[idx])
                        idx += 1
                    elif c == "'":
                        idx += 1
                        # Check for '' escape
                        if idx < length and line[idx] == "'":
                            val_parts.append("'")
                            idx += 1
                        else:
                            break
                    else:
                        val_parts.append(c)
                        idx += 1
                values.append(''.join(val_parts))
            elif ch == 'N' and line[idx:idx+4] == 'NULL':
                values.append(None)
                idx += 4
            else:
                # Numeric or unquoted value
                start = idx
                while idx < length and line[idx] not in ',)':
                    idx += 1
                values.append(line[start:idx])

        rows.append(tuple(values))
        row_count += 1
        if max_rows and row_count >= max_rows:
            break

        # After ')', expect ',' or ';' or end
        while idx < length and line[idx] in ' \t\r\n':
            idx += 1
        if idx < length and line[idx] == ',':
            idx += 1
        elif idx < length and line[idx] == ';':
            break
        else:
            break

    return rows


def count_rows_in_line(line):
    """Fast count of rows in a mysqldump INSERT line without full parsing."""
    # Count occurrences of '),(' plus 1 for the first/last row
    idx = line.find("VALUES ")
    if idx == -1:
        return 0
    substr = line[idx:]
    count = substr.count('),(') + 1
    return count


# ── Table-specific parsers ──────────────────────────────────────────────────

def scan_table(table_name, sample_limit=SAMPLE_LIMIT):
    """
    Scan the LW dump for a specific table, returning:
    - total_rows: total row count across all INSERT statements
    - sampled_rows: list of parsed row tuples (up to sample_limit)
    """
    marker = f"INSERT INTO `{table_name}`"
    total_rows = 0
    sampled_rows = []
    remaining_sample = sample_limit

    with open(LW_DUMP, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            if not line.startswith(marker):
                continue

            # Count all rows in this INSERT
            line_count = count_rows_in_line(line)
            total_rows += line_count

            # Parse rows if we still need samples
            if remaining_sample > 0:
                parsed = parse_mysqldump_rows(line, max_rows=remaining_sample)
                sampled_rows.extend(parsed)
                remaining_sample -= len(parsed)

    return total_rows, sampled_rows


# ── Audit functions ─────────────────────────────────────────────────────────

def audit_creature_template_difficulty():
    """
    Columns (from LW CREATE TABLE):
    0: Entry, 1: DifficultyID, 2: LevelScalingDeltaMin, 3: LevelScalingDeltaMax,
    4: ContentTuningID, 5: HealthScalingExpansion, 6: HealthModifier, 7: ManaModifier,
    8: ArmorModifier, 9: DamageModifier, 10: CreatureDifficultyID, 11: TypeFlags,
    12: TypeFlags2, 13: TypeFlags3, 14: LootID, 15: PickPocketLootID, 16: SkinLootID,
    17: GoldMin, 18: GoldMax, 19-25: StaticFlags1-7, 26: StaticFlags8, 27: VerifiedBuild
    """
    print("\n" + "="*80)
    print("1. CREATURE_TEMPLATE_DIFFICULTY")
    print("="*80)

    t0 = time.time()
    total, rows = scan_table('creature_template_difficulty')
    print(f"  Parsed in {time.time()-t0:.1f}s")
    print(f"  Total rows in LW dump: {total:,}")
    print(f"  Sampled rows: {len(rows):,}")

    if not rows:
        print("  [WARN] No data found!")
        return

    # Quality metrics
    nonzero_health_mod = 0
    nonzero_dmg_mod = 0
    nonzero_content_tuning = 0
    has_loot = 0
    has_gold = 0
    has_type_flags = 0
    placeholder_rows = 0  # All key fields are defaults
    health_mod_1 = 0
    dmg_mod_1 = 0
    difficulty_ids = Counter()

    for r in rows:
        try:
            health_mod = float(r[6])
            dmg_mod = float(r[9])
            content_tuning = int(r[4])
            loot_id = int(r[14])
            gold_min = int(r[17])
            gold_max = int(r[18])
            type_flags = int(r[11])
            diff_id = int(r[1])
        except (ValueError, IndexError):
            continue

        difficulty_ids[diff_id] += 1

        if health_mod != 0 and health_mod != 1:
            nonzero_health_mod += 1
        if health_mod == 1:
            health_mod_1 += 1
        if dmg_mod != 0 and dmg_mod != 1:
            nonzero_dmg_mod += 1
        if dmg_mod == 1:
            dmg_mod_1 += 1
        if content_tuning != 0:
            nonzero_content_tuning += 1
        if loot_id != 0:
            has_loot += 1
        if gold_min > 0 or gold_max > 0:
            has_gold += 1
        if type_flags != 0:
            has_type_flags += 1

        # Placeholder: HealthMod=1, DmgMod=1, ContentTuning=0, no loot, no gold, no typeflags
        is_placeholder = (
            health_mod in (0, 1) and
            dmg_mod in (0, 1) and
            content_tuning == 0 and
            loot_id == 0 and
            gold_min == 0 and gold_max == 0 and
            type_flags == 0
        )
        if is_placeholder:
            placeholder_rows += 1

    n = len(rows)
    print(f"\n  Quality Metrics (from {n:,} sampled rows):")
    print(f"    Non-default HealthModifier (not 0 or 1): {nonzero_health_mod:,} ({100*nonzero_health_mod/n:.1f}%)")
    print(f"    HealthModifier = 1 (default): {health_mod_1:,} ({100*health_mod_1/n:.1f}%)")
    print(f"    Non-default DamageModifier: {nonzero_dmg_mod:,} ({100*nonzero_dmg_mod/n:.1f}%)")
    print(f"    DamageModifier = 1 (default): {dmg_mod_1:,} ({100*dmg_mod_1/n:.1f}%)")
    print(f"    Non-zero ContentTuningID: {nonzero_content_tuning:,} ({100*nonzero_content_tuning/n:.1f}%)")
    print(f"    Has LootID: {has_loot:,} ({100*has_loot/n:.1f}%)")
    print(f"    Has Gold range: {has_gold:,} ({100*has_gold/n:.1f}%)")
    print(f"    Has TypeFlags: {has_type_flags:,} ({100*has_type_flags/n:.1f}%)")
    print(f"    PLACEHOLDER rows (all defaults/zeros): {placeholder_rows:,} ({100*placeholder_rows/n:.1f}%)")

    print(f"\n  DifficultyID distribution (top 10):")
    for did, cnt in difficulty_ids.most_common(10):
        print(f"    DifficultyID={did}: {cnt:,} ({100*cnt/n:.1f}%)")

    # Compare against our DB
    print(f"\n  Comparing against our DB...")
    our_keys = mysql_query_set(
        "SELECT CONCAT(Entry, ':', DifficultyID) FROM creature_template_difficulty"
    )
    print(f"    Our DB has {len(our_keys):,} rows")

    lw_keys_sample = set()
    for r in rows:
        try:
            lw_keys_sample.add(f"{r[0]}:{r[1]}")
        except IndexError:
            pass

    new_keys = lw_keys_sample - our_keys
    existing_keys = lw_keys_sample & our_keys
    print(f"    In sample: {len(new_keys):,} NEW, {len(existing_keys):,} already exist")
    est_new = int(total * len(new_keys) / max(len(lw_keys_sample), 1))
    print(f"    Estimated NEW in full dump: ~{est_new:,}")


def audit_loot_template(table_name, table_index):
    """
    Audit creature_loot_template or gameobject_loot_template.
    creature_loot_template columns:
      0: Entry, 1: ItemType, 2: Item, 3: Chance, 4: QuestRequired, 5: LootMode,
      6: GroupId, 7: MinCount, 8: MaxCount, 9: Comment, 10: Reference (creature only)
    gameobject_loot_template: same but no Reference column (only 10 cols)
    """
    has_reference = (table_name == 'creature_loot_template')

    print("\n" + "="*80)
    print(f"{table_index}. {table_name.upper()}")
    print("="*80)

    t0 = time.time()
    total, rows = scan_table(table_name)
    print(f"  Parsed in {time.time()-t0:.1f}s")
    print(f"  Total rows in LW dump: {total:,}")
    print(f"  Sampled rows: {len(rows):,}")

    if not rows:
        print("  [WARN] No data found!")
        return

    # Quality metrics
    item_type_counts = Counter()  # 0=direct, 1=reference
    chance_zero = 0
    chance_100 = 0
    chance_ranges = Counter()  # buckets
    quest_required = 0
    min_count_zero = 0
    unique_entries = set()
    unique_items = set()
    direct_items = set()

    for r in rows:
        try:
            item_type = int(r[1])
            item_id = int(r[2])
            chance = float(r[3])
            quest_req = int(r[4])
            min_count = int(r[7])
        except (ValueError, IndexError):
            continue

        item_type_counts[item_type] += 1
        unique_entries.add(r[0])
        unique_items.add(item_id)

        if item_type == 0:
            direct_items.add(item_id)

        if chance == 0:
            chance_zero += 1
        elif chance == 100:
            chance_100 += 1

        if chance <= 1:
            chance_ranges['0-1%'] += 1
        elif chance <= 10:
            chance_ranges['1-10%'] += 1
        elif chance <= 50:
            chance_ranges['10-50%'] += 1
        elif chance <= 99:
            chance_ranges['50-99%'] += 1
        else:
            chance_ranges['100%'] += 1

        if quest_req:
            quest_required += 1
        if min_count == 0:
            min_count_zero += 1

    n = len(rows)
    print(f"\n  Quality Metrics (from {n:,} sampled rows):")
    print(f"    Unique loot entries: {len(unique_entries):,}")
    print(f"    Unique item/reference IDs: {len(unique_items):,}")
    print(f"    Direct items (ItemType=0): {item_type_counts.get(0, 0):,} ({100*item_type_counts.get(0,0)/n:.1f}%)")
    print(f"    References (ItemType=1): {item_type_counts.get(1, 0):,} ({100*item_type_counts.get(1,0)/n:.1f}%)")
    if has_reference:
        ref_col_set = 0
        for r in rows:
            try:
                if len(r) > 10 and r[10] is not None and r[10] != '' and int(r[10]) != 0:
                    ref_col_set += 1
            except (ValueError, IndexError):
                pass
        print(f"    Reference column non-zero: {ref_col_set:,}")

    print(f"    Quest-required items: {quest_required:,} ({100*quest_required/n:.1f}%)")
    print(f"    MinCount = 0: {min_count_zero:,} ({100*min_count_zero/n:.1f}%)")

    print(f"\n  Drop Chance Distribution:")
    for bucket in ['0-1%', '1-10%', '10-50%', '50-99%', '100%']:
        cnt = chance_ranges.get(bucket, 0)
        print(f"    {bucket}: {cnt:,} ({100*cnt/n:.1f}%)")
    print(f"    Chance exactly 0: {chance_zero:,} ({100*chance_zero/n:.1f}%)")

    # Check direct items against hotfixes.item
    if direct_items:
        print(f"\n  Checking {len(direct_items):,} unique direct item IDs against hotfixes.item...")
        # Sample up to 5000 for the check
        check_items = list(direct_items)[:5000]
        batch_size = 500
        found_items = set()
        for i in range(0, len(check_items), batch_size):
            batch = check_items[i:i+batch_size]
            ids_str = ','.join(str(x) for x in batch)
            result = mysql_query_set(f"SELECT ID FROM hotfixes.item WHERE ID IN ({ids_str})")
            found_items.update(result)

        checked = len(check_items)
        found = len(found_items)
        missing = checked - found
        print(f"    Checked {checked:,} items: {found:,} exist ({100*found/max(checked,1):.1f}%), {missing:,} missing ({100*missing/max(checked,1):.1f}%)")

        # Show some missing item IDs
        missing_ids = set(str(x) for x in check_items) - found_items
        if missing_ids:
            sample_missing = sorted(int(x) for x in list(missing_ids)[:20])
            print(f"    Sample missing item IDs: {sample_missing}")

    # Compare keys against our DB
    print(f"\n  Comparing against our DB...")
    if has_reference:
        our_keys = mysql_query_set(
            f"SELECT CONCAT(Entry, ':', ItemType, ':', Item) FROM {table_name}"
        )
    else:
        our_keys = mysql_query_set(
            f"SELECT CONCAT(Entry, ':', ItemType, ':', Item) FROM {table_name}"
        )
    print(f"    Our DB has {len(our_keys):,} rows")

    lw_keys_sample = set()
    for r in rows:
        try:
            lw_keys_sample.add(f"{r[0]}:{r[1]}:{r[2]}")
        except IndexError:
            pass

    new_keys = lw_keys_sample - our_keys
    existing_keys = lw_keys_sample & our_keys
    print(f"    In sample: {len(new_keys):,} NEW, {len(existing_keys):,} already exist")
    est_new = int(total * len(new_keys) / max(len(lw_keys_sample), 1))
    print(f"    Estimated NEW in full dump: ~{est_new:,}")


def audit_quest_template_addon():
    """
    Columns:
    0: ID, 1: MaxLevel, 2: AllowableClasses, 3: SourceSpellID, 4: PrevQuestID,
    5: NextQuestID, 6: ExclusiveGroup, 7: BreadcrumbForQuestId, 8: RewardMailTemplateID,
    9: RewardMailDelay, 10: RequiredSkillID, 11: RequiredSkillPoints,
    12: RequiredMinRepFaction, 13: RequiredMaxRepFaction, 14: RequiredMinRepValue,
    15: RequiredMaxRepValue, 16: ProvidedItemCount, 17: SpecialFlags, 18: ScriptName
    """
    print("\n" + "="*80)
    print("4. QUEST_TEMPLATE_ADDON")
    print("="*80)

    t0 = time.time()
    total, rows = scan_table('quest_template_addon')
    print(f"  Parsed in {time.time()-t0:.1f}s")
    print(f"  Total rows in LW dump: {total:,}")
    print(f"  Sampled rows: {len(rows):,}")

    if not rows:
        print("  [WARN] No data found!")
        return

    # Quality metrics
    has_prev_quest = 0
    has_next_quest = 0
    has_exclusive_group = 0
    has_special_flags = 0
    has_breadcrumb = 0
    has_allowable_classes = 0
    has_source_spell = 0
    has_reward_mail = 0
    has_skill_req = 0
    has_rep_req = 0
    has_script_name = 0
    smart_quest_script = 0
    empty_rows = 0  # all fields zero/default/empty except ID and possibly ScriptName

    script_names = Counter()
    special_flags_dist = Counter()

    for r in rows:
        try:
            max_level = int(r[1])
            allow_classes = int(r[2])
            source_spell = int(r[3])
            prev_quest = int(r[4])
            next_quest = int(r[5])
            exclusive_group = int(r[6])
            breadcrumb = int(r[7])
            reward_mail = int(r[8])
            skill_id = int(r[10])
            rep_min_faction = int(r[12])
            rep_max_faction = int(r[13])
            special_flags = int(r[17])
            script_name = r[18] if len(r) > 18 else ''
        except (ValueError, IndexError):
            continue

        if prev_quest != 0: has_prev_quest += 1
        if next_quest != 0: has_next_quest += 1
        if exclusive_group != 0: has_exclusive_group += 1
        if special_flags != 0:
            has_special_flags += 1
            special_flags_dist[special_flags] += 1
        if breadcrumb != 0: has_breadcrumb += 1
        if allow_classes != 0: has_allowable_classes += 1
        if source_spell != 0: has_source_spell += 1
        if reward_mail != 0: has_reward_mail += 1
        if skill_id != 0: has_skill_req += 1
        if rep_min_faction != 0 or rep_max_faction != 0: has_rep_req += 1
        if script_name and script_name not in ('', 'NULL'):
            has_script_name += 1
            script_names[script_name] += 1
            if script_name == 'SmartQuest':
                smart_quest_script += 1

        # "Empty" = only has ScriptName='SmartQuest' but all other fields default
        meaningful = (
            prev_quest != 0 or next_quest != 0 or exclusive_group != 0 or
            special_flags != 0 or breadcrumb != 0 or allow_classes != 0 or
            source_spell != 0 or reward_mail != 0 or skill_id != 0 or
            rep_min_faction != 0 or rep_max_faction != 0 or max_level != 0
        )
        if not meaningful:
            empty_rows += 1

    n = len(rows)
    print(f"\n  Quality Metrics (from {n:,} sampled rows):")
    print(f"    Has PrevQuestID: {has_prev_quest:,} ({100*has_prev_quest/n:.1f}%)")
    print(f"    Has NextQuestID: {has_next_quest:,} ({100*has_next_quest/n:.1f}%)")
    print(f"    Has ExclusiveGroup: {has_exclusive_group:,} ({100*has_exclusive_group/n:.1f}%)")
    print(f"    Has SpecialFlags: {has_special_flags:,} ({100*has_special_flags/n:.1f}%)")
    print(f"    Has BreadcrumbForQuestId: {has_breadcrumb:,} ({100*has_breadcrumb/n:.1f}%)")
    print(f"    Has AllowableClasses: {has_allowable_classes:,} ({100*has_allowable_classes/n:.1f}%)")
    print(f"    Has SourceSpellID: {has_source_spell:,} ({100*has_source_spell/n:.1f}%)")
    print(f"    Has RewardMailTemplateID: {has_reward_mail:,} ({100*has_reward_mail/n:.1f}%)")
    print(f"    Has RequiredSkillID: {has_skill_req:,} ({100*has_skill_req/n:.1f}%)")
    print(f"    Has RepFaction req: {has_rep_req:,} ({100*has_rep_req/n:.1f}%)")
    print(f"    Has ScriptName: {has_script_name:,} ({100*has_script_name/n:.1f}%)")
    print(f"    ScriptName='SmartQuest': {smart_quest_script:,} ({100*smart_quest_script/n:.1f}%)")
    print(f"    EMPTY rows (only ScriptName, all else default): {empty_rows:,} ({100*empty_rows/n:.1f}%)")

    print(f"\n  ScriptName distribution:")
    for name, cnt in script_names.most_common(10):
        print(f"    '{name}': {cnt:,}")

    if special_flags_dist:
        print(f"\n  SpecialFlags distribution (top 10):")
        for sf, cnt in special_flags_dist.most_common(10):
            print(f"    SpecialFlags={sf}: {cnt:,}")

    # Compare against our DB
    print(f"\n  Comparing against our DB...")
    our_ids = mysql_query_set("SELECT ID FROM quest_template_addon")
    print(f"    Our DB has {len(our_ids):,} rows")

    lw_ids = {r[0] for r in rows}
    new_ids = lw_ids - our_ids
    existing_ids = lw_ids & our_ids
    print(f"    In sample: {len(new_ids):,} NEW, {len(existing_ids):,} already exist")

    # Of the empty rows, how many are new?
    empty_new = 0
    for r in rows:
        try:
            meaningful = (
                int(r[4]) != 0 or int(r[5]) != 0 or int(r[6]) != 0 or
                int(r[17]) != 0 or int(r[7]) != 0 or int(r[2]) != 0 or
                int(r[3]) != 0 or int(r[8]) != 0 or int(r[10]) != 0 or
                int(r[12]) != 0 or int(r[13]) != 0 or int(r[1]) != 0
            )
            if not meaningful and r[0] in new_ids:
                empty_new += 1
        except (ValueError, IndexError):
            pass
    print(f"    Of NEW rows, {empty_new:,} are EMPTY (just SmartQuest script)")


def audit_creature_spawns():
    """
    Columns (from dump):
    0: guid, 1: id(entry), 2: map, 3: zoneId, 4: areaId, 5: spawnDifficulties,
    6: phaseUseFlags, 7: PhaseId (or modelid?), 8: PhaseGroup (or equipment_id?),
    ... let me re-check from the actual data.

    Actually from the sample: (5,12160,1,6450,188,'0',0,0,0,-1,0,1,10348.9,751.136,...)
    0: guid=5, 1: id=12160, 2: map=1, 3: zoneId=6450, 4: areaId=188,
    5: spawnDifficulties='0', 6: phaseUseFlags=0, 7: PhaseId=0, 8: PhaseGroup=0,
    9: terrainSwapMap=-1, 10: modelid=0, 11: equipment_id=1,
    12: position_x, 13: position_y, 14: position_z, 15: orientation,
    16: spawntimesecs, 17: wander_distance, 18: currentwaypoint, 19: curHealthPct,
    20: MovementType, 21: npcflag, 22: unit_flags, 23: unit_flags2, 24: unit_flags3,
    25: ScriptName, 26: StringId, 27: VerifiedBuild

    Wait, our schema has 'size' at the end too. Let me check LW's CREATE TABLE.
    Actually our DB has 29 cols. LW might have fewer. Let me count from sample:
    (5,12160,1,6450,188,'0',0,0,0,-1,0,1,10348.9,751.136,1325.35,5.05727,120,10,0,100,2,NULL,NULL,NULL,NULL,'',NULL,0)
    = 28 values. Our DB has size as col 28 (0-indexed). LW has 28 cols (0-27).
    """
    print("\n" + "="*80)
    print("5. CREATURE (SPAWNS)")
    print("="*80)

    t0 = time.time()
    total, rows = scan_table('creature')
    print(f"  Parsed in {time.time()-t0:.1f}s")
    print(f"  Total rows in LW dump: {total:,}")
    print(f"  Sampled rows: {len(rows):,}")

    if not rows:
        print("  [WARN] No data found!")
        return

    # Quality metrics
    zero_coords = 0
    zero_entry = 0
    map_ids = Counter()
    unique_entries = set()
    unique_guids = set()
    spawn_time_zero = 0

    for r in rows:
        try:
            guid = r[0]
            entry = int(r[1])
            map_id = int(r[2])
            pos_x = float(r[12])
            pos_y = float(r[13])
            pos_z = float(r[14])
            spawn_time = int(r[16])
        except (ValueError, IndexError) as e:
            continue

        unique_guids.add(guid)
        unique_entries.add(str(entry))
        map_ids[map_id] += 1

        if entry == 0:
            zero_entry += 1
        if pos_x == 0 and pos_y == 0 and pos_z == 0:
            zero_coords += 1
        if spawn_time == 0:
            spawn_time_zero += 1

    n = len(rows)
    print(f"\n  Quality Metrics (from {n:,} sampled rows):")
    print(f"    Unique GUIDs: {len(unique_guids):,}")
    print(f"    Unique creature entries: {len(unique_entries):,}")
    print(f"    Zero entry (id=0): {zero_entry:,} ({100*zero_entry/n:.1f}%)")
    print(f"    Zero coordinates (0,0,0): {zero_coords:,} ({100*zero_coords/n:.1f}%)")
    print(f"    SpawnTimeSecs = 0: {spawn_time_zero:,} ({100*spawn_time_zero/n:.1f}%)")

    print(f"\n  Map distribution (top 15):")
    for mid, cnt in map_ids.most_common(15):
        print(f"    Map {mid}: {cnt:,} spawns ({100*cnt/n:.1f}%)")

    # Check creature entries against our creature_template
    print(f"\n  Checking creature entries against our creature_template...")
    our_templates = mysql_query_set("SELECT entry FROM creature_template")
    print(f"    Our DB has {len(our_templates):,} creature templates")

    entries_found = unique_entries & our_templates
    entries_missing = unique_entries - our_templates
    print(f"    Of {len(unique_entries):,} unique entries in sample:")
    print(f"      {len(entries_found):,} have templates in our DB ({100*len(entries_found)/max(len(unique_entries),1):.1f}%)")
    print(f"      {len(entries_missing):,} MISSING templates ({100*len(entries_missing)/max(len(unique_entries),1):.1f}%)")

    if entries_missing:
        sample_missing = sorted(int(x) for x in list(entries_missing)[:20])
        print(f"      Sample missing entries: {sample_missing}")

    # Check GUIDs against our DB
    print(f"\n  Checking GUIDs against our creature table...")
    our_guids = mysql_query_set("SELECT guid FROM creature")
    print(f"    Our DB has {len(our_guids):,} creature spawns")

    new_guids = unique_guids - our_guids
    existing_guids = unique_guids & our_guids
    print(f"    In sample: {len(new_guids):,} NEW GUIDs, {len(existing_guids):,} already exist")
    est_new = int(total * len(new_guids) / max(len(unique_guids), 1))
    print(f"    Estimated NEW spawns in full dump: ~{est_new:,}")

    # Of the new GUIDs, how many reference missing templates?
    new_with_missing_template = 0
    for r in rows:
        try:
            if r[0] in new_guids and str(int(r[1])) in entries_missing:
                new_with_missing_template += 1
        except (ValueError, IndexError):
            pass
    print(f"    NEW spawns referencing MISSING templates: {new_with_missing_template:,}")


def audit_smart_scripts():
    """
    Columns:
    0: entryorguid, 1: source_type, 2: id, 3: link, 4: Difficulties,
    5: event_type, 6: event_phase_mask, 7: event_chance, 8: event_flags,
    9: event_param1, 10: event_param2, 11: event_param3, 12: event_param4,
    13: event_param5, 14: event_param_string, 15: action_type,
    16: action_param1, 17: action_param2, 18: action_param3, 19: action_param4,
    20: action_param5, 21: action_param7, 22: action_param_string, 23: action_param6,
    24: target_type, 25: target_param1, 26: target_param2, 27: target_param3,
    28: target_param4, 29: target_param_string, 30: target_x, 31: target_y,
    32: target_z, 33: target_o, 34: comment
    """
    print("\n" + "="*80)
    print("6. SMART_SCRIPTS")
    print("="*80)

    t0 = time.time()
    total, rows = scan_table('smart_scripts')
    print(f"  Parsed in {time.time()-t0:.1f}s")
    print(f"  Total rows in LW dump: {total:,}")
    print(f"  Sampled rows: {len(rows):,}")

    if not rows:
        print("  [WARN] No data found!")
        return

    # Quality metrics
    source_types = Counter()
    action_types = Counter()
    event_types = Counter()

    # Quest script specifics (source_type=5)
    quest_action_types = Counter()
    quest_spell_82238 = 0
    quest_rows = 0
    unique_quest_entries = set()

    # Creature script specifics (source_type=0)
    creature_rows = 0
    creature_action_types = Counter()

    for r in rows:
        try:
            source_type = int(r[1])
            action_type = int(r[15])
            event_type = int(r[5])
        except (ValueError, IndexError):
            continue

        source_types[source_type] += 1
        action_types[action_type] += 1
        event_types[event_type] += 1

        if source_type == 5:
            quest_rows += 1
            quest_action_types[action_type] += 1
            unique_quest_entries.add(r[0])
            # Check if it's casting spell 82238
            if action_type == 11:  # SMART_ACTION_CAST = 11
                try:
                    spell_id = int(r[16])
                    if spell_id == 82238:
                        quest_spell_82238 += 1
                except (ValueError, IndexError):
                    pass
        elif source_type == 0:
            creature_rows += 1
            creature_action_types[action_type] += 1

    n = len(rows)
    print(f"\n  Source Type Distribution:")
    type_names = {
        0: 'Creature', 1: 'GameObject', 2: 'AreaTrigger',
        5: 'Quest', 9: 'TimedActionList', 10: 'Scene', 12: 'AreaTriggerEntity',
        13: 'Conversation'
    }
    for st, cnt in sorted(source_types.items(), key=lambda x: -x[1]):
        name = type_names.get(st, f'Unknown({st})')
        print(f"    Type {st} ({name}): {cnt:,} ({100*cnt/n:.1f}%)")

    print(f"\n  Action Type Distribution (top 15):")
    action_names = {
        0: 'NONE', 1: 'TALK', 2: 'SET_FACTION', 5: 'EMOTE',
        11: 'CAST', 12: 'SUMMON_CREATURE', 17: 'SET_REACT_STATE',
        18: 'ACTIVATE_GOBJECT', 20: 'FOLLOW', 24: 'SET_VISIBILITY',
        28: 'SET_ORIENTATION', 37: 'REMOVE_AURA', 41: 'SET_IN_COMBAT_WITH_ZONE',
        44: 'SET_DATA', 45: 'MOVE_TO_POS', 53: 'DIE', 62: 'SET_COUNTER',
        80: 'RANDOM_EMOTE', 86: 'SET_MOVEMENT_SPEED', 97: 'SEND_GOSSIP_MENU',
        144: 'UPDATE_TEMPLATE', 146: 'TRIGGER_GAME_EVENT', 201: 'FLEE_FOR_ASSIST',
    }
    for at, cnt in action_types.most_common(15):
        name = action_names.get(at, f'action_{at}')
        print(f"    {at} ({name}): {cnt:,} ({100*cnt/n:.1f}%)")

    print(f"\n  Quest Scripts (source_type=5) Analysis:")
    print(f"    Total quest rows: {quest_rows:,}")
    print(f"    Unique quest entries: {len(unique_quest_entries):,}")
    if quest_rows:
        print(f"    Cast spell 82238 rows: {quest_spell_82238:,} ({100*quest_spell_82238/quest_rows:.1f}% of quest rows)")
        print(f"    Quest action type breakdown:")
        for at, cnt in quest_action_types.most_common(10):
            name = action_names.get(at, f'action_{at}')
            print(f"      {at} ({name}): {cnt:,} ({100*cnt/quest_rows:.1f}%)")

    print(f"\n  Creature Scripts (source_type=0) Analysis:")
    print(f"    Total creature rows: {creature_rows:,}")
    if creature_rows:
        print(f"    Creature action type breakdown (top 10):")
        for at, cnt in creature_action_types.most_common(10):
            name = action_names.get(at, f'action_{at}')
            print(f"      {at} ({name}): {cnt:,} ({100*cnt/creature_rows:.1f}%)")

    # Compare against our DB
    print(f"\n  Comparing against our DB...")
    our_keys = mysql_query_set(
        "SELECT CONCAT(entryorguid, ':', source_type, ':', id, ':', link) FROM smart_scripts"
    )
    print(f"    Our DB has {len(our_keys):,} rows")

    lw_keys_sample = set()
    for r in rows:
        try:
            lw_keys_sample.add(f"{r[0]}:{r[1]}:{r[2]}:{r[3]}")
        except IndexError:
            pass

    new_keys = lw_keys_sample - our_keys
    existing_keys = lw_keys_sample & our_keys
    print(f"    In sample: {len(new_keys):,} NEW, {len(existing_keys):,} already exist")
    est_new = int(total * len(new_keys) / max(len(lw_keys_sample), 1))
    print(f"    Estimated NEW in full dump: ~{est_new:,}")

    # Source type breakdown of NEW rows
    new_source_types = Counter()
    for r in rows:
        try:
            key = f"{r[0]}:{r[1]}:{r[2]}:{r[3]}"
            if key in new_keys:
                new_source_types[int(r[1])] += 1
        except (ValueError, IndexError):
            pass
    if new_source_types:
        print(f"\n    NEW rows by source_type:")
        for st, cnt in sorted(new_source_types.items(), key=lambda x: -x[1]):
            name = type_names.get(st, f'Unknown({st})')
            print(f"      Type {st} ({name}): {cnt:,}")


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("LoreWalkerTDB Data Quality Audit")
    print(f"Dump: {LW_DUMP}")
    print(f"Sample limit: {SAMPLE_LIMIT:,} rows per table")
    print("=" * 80)

    if not os.path.exists(LW_DUMP):
        print(f"ERROR: Dump file not found: {LW_DUMP}")
        sys.exit(1)

    total_start = time.time()

    audit_creature_template_difficulty()
    audit_loot_template('creature_loot_template', 2)
    audit_loot_template('gameobject_loot_template', 3)
    audit_quest_template_addon()
    audit_creature_spawns()
    audit_smart_scripts()

    print("\n" + "=" * 80)
    print(f"Audit complete in {time.time()-total_start:.1f}s")
    print("=" * 80)


if __name__ == '__main__':
    main()

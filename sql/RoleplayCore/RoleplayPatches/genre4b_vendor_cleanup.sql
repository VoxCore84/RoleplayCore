/* ================================================================== */
/* GENRE 4B v2 — Vendor table cleanup (Midnight 12.x / TWW 11.1.7)   */
/*                                                                    */
/* Targets:                                                           */
/*   1) creature_template — add vendor npcflag (bit 128) where       */
/*      NPC has vendor items but flag is missing                      */
/*   2) npc_vendor / game_event_npc_vendor — fix MaxCount/IncrTime   */
/*      mismatch (one set, other zero)                                */
/*   3) npc_vendor / game_event_npc_vendor — zero invalid             */
/*      PlayerConditionID refs                                        */
/*   4) npc_vendor / game_event_npc_vendor — delete rows pointing    */
/*      to items that don't exist (WITH COVERAGE GUARD)               */
/*                                                                    */
/* v2 fixes:                                                          */
/*   - Removed embedded GitHub review comment (syntax error)          */
/*   - game_event_npc_vendor column detection now includes 'guid'     */
/*   - Item delete has a COVERAGE GUARD: if <80% of vendor items      */
/*     are found in the item source table, deletion is SKIPPED to     */
/*     prevent mass-deletion when item_template is incomplete         */
/*   - COALESCE on session save/restore (NULL-proof)                  */
/*   - Self-contained — safe to run standalone in HeidiSQL            */
/*                                                                    */
/* IMPORTANT: Run the COMPLETE file. Do not paste fragments.          */
/* ================================================================== */

USE `world`;
SELECT DATABASE() AS active_database;

/* ── Session snapshot ────────────────────────────────────────────── */
SET @OLD_SQL_SAFE_UPDATES   := COALESCE(@@SQL_SAFE_UPDATES, 1);
SET @OLD_FOREIGN_KEY_CHECKS := COALESCE(@@FOREIGN_KEY_CHECKS, 1);
SET @OLD_UNIQUE_CHECKS      := COALESCE(@@UNIQUE_CHECKS, 1);
SET @OLD_AUTOCOMMIT         := COALESCE(@@AUTOCOMMIT, 1);

SET SQL_SAFE_UPDATES  = 0;
SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS      = 0;
SET AUTOCOMMIT         = 0;

START TRANSACTION;

/* ── Summary table ───────────────────────────────────────────────── */
DROP TEMPORARY TABLE IF EXISTS `_summary_4b`;
CREATE TEMPORARY TABLE `_summary_4b` (
  `action`     VARCHAR(80) NOT NULL,
  `tbl`        VARCHAR(80) NOT NULL,
  `rows_hit`   BIGINT NOT NULL DEFAULT 0
);

/* ================================================================== */
/* SCHEMA DETECTION                                                   */
/* ================================================================== */

/* ── Table existence ─────────────────────────────────────────────── */
SET @has_npc_vendor := (
  SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = DATABASE() AND table_name = 'npc_vendor'
);
SET @has_ge_vendor := (
  SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = DATABASE() AND table_name = 'game_event_npc_vendor'
);
SET @has_ct := (
  SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = DATABASE() AND table_name = 'creature_template'
);

/* ── npc_vendor columns ──────────────────────────────────────────── */
SET @nv_creature_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'npc_vendor'
    AND column_name IN ('entry','Entry','CreatureID','creature','id')
  ORDER BY FIELD(column_name,'entry','Entry','CreatureID','creature','id') LIMIT 1
);
SET @nv_item_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'npc_vendor'
    AND column_name IN ('item','Item','itemid','ItemID')
  ORDER BY FIELD(column_name,'item','Item','itemid','ItemID') LIMIT 1
);
SET @nv_max_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'npc_vendor'
    AND column_name IN ('maxcount','MaxCount','max_count')
  ORDER BY FIELD(column_name,'maxcount','MaxCount','max_count') LIMIT 1
);
SET @nv_incr_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'npc_vendor'
    AND column_name IN ('incrtime','IncrTime','incr_time')
  ORDER BY FIELD(column_name,'incrtime','IncrTime','incr_time') LIMIT 1
);
SET @nv_pc_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'npc_vendor'
    AND column_name IN ('PlayerConditionID','playerConditionId','player_condition_id','condition_id','ConditionID')
  ORDER BY FIELD(column_name,'PlayerConditionID','playerConditionId','player_condition_id','condition_id','ConditionID') LIMIT 1
);

/* ── game_event_npc_vendor columns (FIX: added 'guid','Guid') ───── */
SET @ge_creature_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'game_event_npc_vendor'
    AND column_name IN ('guid','Guid','entry','Entry','CreatureID','creature','id')
  ORDER BY FIELD(column_name,'guid','Guid','entry','Entry','CreatureID','creature','id') LIMIT 1
);
SET @ge_item_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'game_event_npc_vendor'
    AND column_name IN ('item','Item','itemid','ItemID')
  ORDER BY FIELD(column_name,'item','Item','itemid','ItemID') LIMIT 1
);
SET @ge_max_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'game_event_npc_vendor'
    AND column_name IN ('maxcount','MaxCount','max_count')
  ORDER BY FIELD(column_name,'maxcount','MaxCount','max_count') LIMIT 1
);
SET @ge_incr_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'game_event_npc_vendor'
    AND column_name IN ('incrtime','IncrTime','incr_time')
  ORDER BY FIELD(column_name,'incrtime','IncrTime','incr_time') LIMIT 1
);
SET @ge_pc_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'game_event_npc_vendor'
    AND column_name IN ('PlayerConditionID','playerConditionId','player_condition_id','condition_id','ConditionID')
  ORDER BY FIELD(column_name,'PlayerConditionID','playerConditionId','player_condition_id','condition_id','ConditionID') LIMIT 1
);

/* ── creature_template columns ───────────────────────────────────── */
SET @ct_pk_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'creature_template'
    AND column_name IN ('entry','Entry','ID','Id')
  ORDER BY FIELD(column_name,'entry','Entry','ID','Id') LIMIT 1
);
SET @ct_npcflag_col := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'creature_template'
    AND column_name IN ('npcflag','npcFlag','npc_flag')
  ORDER BY FIELD(column_name,'npcflag','npcFlag','npc_flag') LIMIT 1
);

/* ── player_condition lookup ─────────────────────────────────────── */
SET @pc_schema := (
  SELECT table_schema FROM information_schema.tables
  WHERE table_name IN ('player_condition','player_conditions')
  ORDER BY (table_schema = DATABASE()) DESC, (table_schema = 'hotfixes') DESC,
           FIELD(table_name,'player_condition','player_conditions'), table_schema
  LIMIT 1
);
SET @pc_table := (
  SELECT table_name FROM information_schema.tables
  WHERE table_schema = @pc_schema AND table_name IN ('player_condition','player_conditions')
  ORDER BY FIELD(table_name,'player_condition','player_conditions') LIMIT 1
);
SET @pc_pk := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = @pc_schema AND table_name = @pc_table
    AND LOWER(column_name) = 'id' LIMIT 1
);
SET @has_pc := IF(@pc_schema IS NOT NULL AND @pc_table IS NOT NULL AND @pc_pk IS NOT NULL, 1, 0);
SET @pc_ref := IF(@has_pc = 1, CONCAT('`', @pc_schema, '`.`', @pc_table, '`'), NULL);

/* ── Item source detection (cascading priority) ──────────────────── */
/*    Priority: item_template(world) > item_sparse(world) > item_sparse(hotfixes) */
SET @item_schema := NULL;
SET @item_table  := NULL;
SET @item_pk     := NULL;

/* Try item_template in world */
SET @_pk := (
  SELECT column_name FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'item_template'
    AND column_name IN ('entry','ID')
  ORDER BY FIELD(column_name,'entry','ID') LIMIT 1
);
SET @item_schema := IF(@_pk IS NOT NULL, DATABASE(), @item_schema);
SET @item_table  := IF(@_pk IS NOT NULL, 'item_template', @item_table);
SET @item_pk     := IF(@_pk IS NOT NULL, @_pk, @item_pk);

/* Try item_sparse in world (only if item_template not found) */
SET @_has := (
  SELECT COUNT(*) FROM information_schema.columns
  WHERE table_schema = DATABASE() AND table_name = 'item_sparse' AND column_name = 'ID'
);
SET @item_schema := IF(@item_table IS NULL AND @_has > 0, DATABASE(), @item_schema);
SET @item_table  := IF(@item_table IS NULL AND @_has > 0, 'item_sparse', @item_table);
SET @item_pk     := IF(@item_table = 'item_sparse' AND @item_schema = DATABASE(), 'ID', @item_pk);

/* Try item_sparse in hotfixes (only if still not found) */
SET @_has := (
  SELECT COUNT(*) FROM information_schema.columns
  WHERE table_schema = 'hotfixes' AND table_name = 'item_sparse' AND column_name = 'ID'
);
SET @item_schema := IF(@item_table IS NULL AND @_has > 0, 'hotfixes', @item_schema);
SET @item_table  := IF(@item_table IS NULL AND @_has > 0, 'item_sparse', @item_table);
SET @item_pk     := IF(@item_table = 'item_sparse' AND @item_schema = 'hotfixes', 'ID', @item_pk);

SET @has_item_source := IF(@item_table IS NOT NULL AND @item_pk IS NOT NULL, 1, 0);
SET @item_ref := IF(@has_item_source = 1, CONCAT('`', @item_schema, '`.`', @item_table, '`'), NULL);

/* ── Diagnostic: show detected schema ────────────────────────────── */
SELECT
  IFNULL(@nv_creature_col, 'NULL')  AS nv_creature_col,
  IFNULL(@ge_creature_col, 'NULL')  AS ge_creature_col,
  IFNULL(@ct_pk_col, 'NULL')        AS ct_pk_col,
  IFNULL(@item_ref, 'none')         AS item_source,
  IFNULL(@pc_ref, 'none')           AS player_condition_source;

/* ================================================================== */
/* BACKUP TABLES                                                      */
/* ================================================================== */

SET @sql := IF(@has_npc_vendor > 0,
  'CREATE TABLE IF NOT EXISTS `npc_vendor_backup_genre4b` LIKE `npc_vendor`',
  'SELECT ''SKIP: npc_vendor missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_ge_vendor > 0,
  'CREATE TABLE IF NOT EXISTS `game_event_npc_vendor_backup_genre4b` LIKE `game_event_npc_vendor`',
  'SELECT ''SKIP: game_event_npc_vendor missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_ct > 0,
  'CREATE TABLE IF NOT EXISTS `creature_template_backup_vendorflag_genre4b` LIKE `creature_template`',
  'SELECT ''SKIP: creature_template missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* VENDOR CREATURE SET                                                */
/* ================================================================== */

DROP TEMPORARY TABLE IF EXISTS `_vendor_creatures`;
CREATE TEMPORARY TABLE `_vendor_creatures` (
  `creature_entry` BIGINT NOT NULL,
  PRIMARY KEY (`creature_entry`)
);

SET @sql := IF(@has_npc_vendor > 0 AND @nv_creature_col IS NOT NULL,
  CONCAT('INSERT IGNORE INTO `_vendor_creatures` SELECT DISTINCT `',
         @nv_creature_col, '` FROM `npc_vendor`'),
  'SELECT ''SKIP: npc_vendor creature col missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_ge_vendor > 0 AND @ge_creature_col IS NOT NULL,
  CONCAT('INSERT IGNORE INTO `_vendor_creatures` SELECT DISTINCT `',
         @ge_creature_col, '` FROM `game_event_npc_vendor`'),
  'SELECT ''SKIP: game_event_npc_vendor creature col missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* 1) FIX MISSING VENDOR NPCFLAG (bit 128)                            */
/* ================================================================== */
SELECT 'STEP 1: vendor npcflag fix' AS section;

SET @sql := IF(@has_ct > 0 AND @ct_pk_col IS NOT NULL AND @ct_npcflag_col IS NOT NULL,
  CONCAT(
    'INSERT IGNORE INTO `creature_template_backup_vendorflag_genre4b` ',
    'SELECT ct.* FROM `creature_template` ct ',
    'INNER JOIN `_vendor_creatures` vc ON vc.`creature_entry` = ct.`', @ct_pk_col, '` ',
    'WHERE (ct.`', @ct_npcflag_col, '` & 128) = 0'
  ),
  'SELECT ''SKIP: creature_template PK or npcflag missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_ct > 0 AND @ct_pk_col IS NOT NULL AND @ct_npcflag_col IS NOT NULL,
  CONCAT(
    'UPDATE `creature_template` ct ',
    'INNER JOIN `_vendor_creatures` vc ON vc.`creature_entry` = ct.`', @ct_pk_col, '` ',
    'SET ct.`', @ct_npcflag_col, '` = ct.`', @ct_npcflag_col, '` | 128 ',
    'WHERE (ct.`', @ct_npcflag_col, '` & 128) = 0'
  ),
  'SELECT ''SKIP: vendor flag update skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
INSERT INTO `_summary_4b` VALUES ('vendor_flag_fix','creature_template', ROW_COUNT());
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* 2) FIX MAXCOUNT / INCRTIME MISMATCH                                */
/* ================================================================== */
SELECT 'STEP 2: MaxCount/IncrTime mismatch' AS section;

/* ── npc_vendor ──────────────────────────────────────────────────── */
SET @sql := IF(@has_npc_vendor > 0 AND @nv_max_col IS NOT NULL AND @nv_incr_col IS NOT NULL,
  CONCAT(
    'INSERT IGNORE INTO `npc_vendor_backup_genre4b` SELECT v.* FROM `npc_vendor` v ',
    'WHERE (v.`', @nv_max_col, '` = 0 AND v.`', @nv_incr_col, '` > 0) ',
    'OR (v.`', @nv_max_col, '` > 0 AND v.`', @nv_incr_col, '` = 0)'
  ),
  'SELECT ''SKIP: npc_vendor max/incr backup skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_npc_vendor > 0 AND @nv_max_col IS NOT NULL AND @nv_incr_col IS NOT NULL,
  CONCAT(
    'UPDATE `npc_vendor` v SET ',
    'v.`', @nv_incr_col, '` = IF(v.`', @nv_max_col, '` = 0 AND v.`', @nv_incr_col, '` > 0, 0, v.`', @nv_incr_col, '`), ',
    'v.`', @nv_max_col, '` = IF(v.`', @nv_max_col, '` > 0 AND v.`', @nv_incr_col, '` = 0, 0, v.`', @nv_max_col, '`) ',
    'WHERE (v.`', @nv_max_col, '` = 0 AND v.`', @nv_incr_col, '` > 0) ',
    'OR (v.`', @nv_max_col, '` > 0 AND v.`', @nv_incr_col, '` = 0)'
  ),
  'SELECT ''SKIP: npc_vendor max/incr update skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
INSERT INTO `_summary_4b` VALUES ('maxincr_fix','npc_vendor', ROW_COUNT());
DEALLOCATE PREPARE stmt;

/* ── game_event_npc_vendor ───────────────────────────────────────── */
SET @sql := IF(@has_ge_vendor > 0 AND @ge_max_col IS NOT NULL AND @ge_incr_col IS NOT NULL,
  CONCAT(
    'INSERT IGNORE INTO `game_event_npc_vendor_backup_genre4b` SELECT v.* FROM `game_event_npc_vendor` v ',
    'WHERE (v.`', @ge_max_col, '` = 0 AND v.`', @ge_incr_col, '` > 0) ',
    'OR (v.`', @ge_max_col, '` > 0 AND v.`', @ge_incr_col, '` = 0)'
  ),
  'SELECT ''SKIP: ge_vendor max/incr backup skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_ge_vendor > 0 AND @ge_max_col IS NOT NULL AND @ge_incr_col IS NOT NULL,
  CONCAT(
    'UPDATE `game_event_npc_vendor` v SET ',
    'v.`', @ge_incr_col, '` = IF(v.`', @ge_max_col, '` = 0 AND v.`', @ge_incr_col, '` > 0, 0, v.`', @ge_incr_col, '`), ',
    'v.`', @ge_max_col, '` = IF(v.`', @ge_max_col, '` > 0 AND v.`', @ge_incr_col, '` = 0, 0, v.`', @ge_max_col, '`) ',
    'WHERE (v.`', @ge_max_col, '` = 0 AND v.`', @ge_incr_col, '` > 0) ',
    'OR (v.`', @ge_max_col, '` > 0 AND v.`', @ge_incr_col, '` = 0)'
  ),
  'SELECT ''SKIP: ge_vendor max/incr update skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
INSERT INTO `_summary_4b` VALUES ('maxincr_fix','game_event_npc_vendor', ROW_COUNT());
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* 3) FIX INVALID PLAYERCONDITIONID                                   */
/* ================================================================== */
SELECT 'STEP 3: invalid PlayerConditionID' AS section;

/* ── npc_vendor ──────────────────────────────────────────────────── */
SET @sql := IF(@has_npc_vendor > 0 AND @nv_pc_col IS NOT NULL AND @has_pc > 0,
  CONCAT(
    'INSERT IGNORE INTO `npc_vendor_backup_genre4b` SELECT v.* FROM `npc_vendor` v ',
    'WHERE v.`', @nv_pc_col, '` <> 0 ',
    'AND NOT EXISTS (SELECT 1 FROM ', @pc_ref, ' pc WHERE pc.`', @pc_pk, '` = v.`', @nv_pc_col, '`)'
  ),
  'SELECT ''SKIP: npc_vendor PC backup skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_npc_vendor > 0 AND @nv_pc_col IS NOT NULL AND @has_pc > 0,
  CONCAT(
    'UPDATE `npc_vendor` v SET v.`', @nv_pc_col, '` = 0 ',
    'WHERE v.`', @nv_pc_col, '` <> 0 ',
    'AND NOT EXISTS (SELECT 1 FROM ', @pc_ref, ' pc WHERE pc.`', @pc_pk, '` = v.`', @nv_pc_col, '`)'
  ),
  'SELECT ''SKIP: npc_vendor PC update skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
INSERT INTO `_summary_4b` VALUES ('playercond_fix','npc_vendor', ROW_COUNT());
DEALLOCATE PREPARE stmt;

/* ── game_event_npc_vendor ───────────────────────────────────────── */
SET @sql := IF(@has_ge_vendor > 0 AND @ge_pc_col IS NOT NULL AND @has_pc > 0,
  CONCAT(
    'INSERT IGNORE INTO `game_event_npc_vendor_backup_genre4b` SELECT v.* FROM `game_event_npc_vendor` v ',
    'WHERE v.`', @ge_pc_col, '` <> 0 ',
    'AND NOT EXISTS (SELECT 1 FROM ', @pc_ref, ' pc WHERE pc.`', @pc_pk, '` = v.`', @ge_pc_col, '`)'
  ),
  'SELECT ''SKIP: ge_vendor PC backup skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_ge_vendor > 0 AND @ge_pc_col IS NOT NULL AND @has_pc > 0,
  CONCAT(
    'UPDATE `game_event_npc_vendor` v SET v.`', @ge_pc_col, '` = 0 ',
    'WHERE v.`', @ge_pc_col, '` <> 0 ',
    'AND NOT EXISTS (SELECT 1 FROM ', @pc_ref, ' pc WHERE pc.`', @pc_pk, '` = v.`', @ge_pc_col, '`)'
  ),
  'SELECT ''SKIP: ge_vendor PC update skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
INSERT INTO `_summary_4b` VALUES ('playercond_fix','game_event_npc_vendor', ROW_COUNT());
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* 4) DELETE MISSING ITEM REFERENCES  *** WITH COVERAGE GUARD ***     */
/*                                                                    */
/*    This is what killed npc_vendor last time. If the item source    */
/*    table only covers a small fraction of the items referenced by   */
/*    vendors, we REFUSE to delete — the item table is incomplete,    */
/*    not the vendor table.                                           */
/*                                                                    */
/*    Guard: at least 80% of distinct vendor items must exist in the  */
/*    item source, otherwise step 4 is skipped entirely.              */
/* ================================================================== */
SELECT 'STEP 4: missing item references (coverage-guarded)' AS section;

SET @nv_total_items   := 0;
SET @nv_matched_items := 0;
SET @nv_coverage_pct  := 0;
SET @nv_delete_allowed := 0;

/* Count total distinct items in npc_vendor */
SET @sql := IF(@has_npc_vendor > 0 AND @nv_item_col IS NOT NULL,
  CONCAT('SELECT COUNT(DISTINCT `', @nv_item_col, '`) INTO @nv_total_items FROM `npc_vendor`'),
  'SELECT 0 INTO @nv_total_items');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Count how many of those exist in the item source */
SET @sql := IF(@has_npc_vendor > 0 AND @nv_item_col IS NOT NULL AND @has_item_source > 0,
  CONCAT(
    'SELECT COUNT(DISTINCT v.`', @nv_item_col, '`) INTO @nv_matched_items ',
    'FROM `npc_vendor` v ',
    'WHERE EXISTS (SELECT 1 FROM ', @item_ref, ' i WHERE i.`', @item_pk, '` = v.`', @nv_item_col, '`)'
  ),
  'SELECT 0 INTO @nv_matched_items');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @nv_coverage_pct := IF(@nv_total_items > 0,
  ROUND(100.0 * @nv_matched_items / @nv_total_items, 1), 0);
SET @nv_delete_allowed := IF(@nv_coverage_pct >= 80, 1, 0);

SELECT
  @nv_total_items    AS nv_distinct_items,
  @nv_matched_items  AS nv_items_in_source,
  @nv_coverage_pct   AS nv_coverage_pct,
  IF(@nv_delete_allowed = 1, 'DELETE ENABLED', 'DELETE BLOCKED — item source coverage too low') AS nv_delete_status;

/* ── npc_vendor: backup + delete (only if coverage OK) ───────────── */
SET @sql := IF(@nv_delete_allowed = 1 AND @has_npc_vendor > 0 AND @nv_item_col IS NOT NULL AND @has_item_source > 0,
  CONCAT(
    'INSERT IGNORE INTO `npc_vendor_backup_genre4b` SELECT v.* FROM `npc_vendor` v ',
    'WHERE NOT EXISTS (SELECT 1 FROM ', @item_ref, ' i WHERE i.`', @item_pk, '` = v.`', @nv_item_col, '`)'
  ),
  'SELECT ''SKIP: npc_vendor item-delete backup skipped (coverage guard or missing deps)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@nv_delete_allowed = 1 AND @has_npc_vendor > 0 AND @nv_item_col IS NOT NULL AND @has_item_source > 0,
  CONCAT(
    'DELETE v FROM `npc_vendor` v ',
    'WHERE NOT EXISTS (SELECT 1 FROM ', @item_ref, ' i WHERE i.`', @item_pk, '` = v.`', @nv_item_col, '`)'
  ),
  'SELECT ''SKIP: npc_vendor item-delete skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
INSERT INTO `_summary_4b` VALUES ('item_delete', 'npc_vendor',
  IF(@nv_delete_allowed = 1, ROW_COUNT(), 0));
DEALLOCATE PREPARE stmt;

/* ── game_event_npc_vendor: same coverage guard ──────────────────── */
SET @ge_total_items   := 0;
SET @ge_matched_items := 0;
SET @ge_coverage_pct  := 0;
SET @ge_delete_allowed := 0;

SET @sql := IF(@has_ge_vendor > 0 AND @ge_item_col IS NOT NULL,
  CONCAT('SELECT COUNT(DISTINCT `', @ge_item_col, '`) INTO @ge_total_items FROM `game_event_npc_vendor`'),
  'SELECT 0 INTO @ge_total_items');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_ge_vendor > 0 AND @ge_item_col IS NOT NULL AND @has_item_source > 0,
  CONCAT(
    'SELECT COUNT(DISTINCT v.`', @ge_item_col, '`) INTO @ge_matched_items ',
    'FROM `game_event_npc_vendor` v ',
    'WHERE EXISTS (SELECT 1 FROM ', @item_ref, ' i WHERE i.`', @item_pk, '` = v.`', @ge_item_col, '`)'
  ),
  'SELECT 0 INTO @ge_matched_items');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @ge_coverage_pct := IF(@ge_total_items > 0,
  ROUND(100.0 * @ge_matched_items / @ge_total_items, 1), 0);
SET @ge_delete_allowed := IF(@ge_coverage_pct >= 80, 1, 0);

SELECT
  @ge_total_items    AS ge_distinct_items,
  @ge_matched_items  AS ge_items_in_source,
  @ge_coverage_pct   AS ge_coverage_pct,
  IF(@ge_delete_allowed = 1, 'DELETE ENABLED', 'DELETE BLOCKED — coverage too low') AS ge_delete_status;

SET @sql := IF(@ge_delete_allowed = 1 AND @has_ge_vendor > 0 AND @ge_item_col IS NOT NULL AND @has_item_source > 0,
  CONCAT(
    'INSERT IGNORE INTO `game_event_npc_vendor_backup_genre4b` SELECT v.* FROM `game_event_npc_vendor` v ',
    'WHERE NOT EXISTS (SELECT 1 FROM ', @item_ref, ' i WHERE i.`', @item_pk, '` = v.`', @ge_item_col, '`)'
  ),
  'SELECT ''SKIP: ge_vendor item-delete backup skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@ge_delete_allowed = 1 AND @has_ge_vendor > 0 AND @ge_item_col IS NOT NULL AND @has_item_source > 0,
  CONCAT(
    'DELETE v FROM `game_event_npc_vendor` v ',
    'WHERE NOT EXISTS (SELECT 1 FROM ', @item_ref, ' i WHERE i.`', @item_pk, '` = v.`', @ge_item_col, '`)'
  ),
  'SELECT ''SKIP: ge_vendor item-delete skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
INSERT INTO `_summary_4b` VALUES ('item_delete', 'game_event_npc_vendor',
  IF(@ge_delete_allowed = 1, ROW_COUNT(), 0));
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* VERIFICATION                                                       */
/* ================================================================== */
SELECT 'VERIFICATION' AS section;

SET @sql := IF(@has_ct > 0 AND @ct_pk_col IS NOT NULL AND @ct_npcflag_col IS NOT NULL,
  CONCAT(
    'SELECT ''missing_vendor_flag'' AS chk, COUNT(*) AS remaining ',
    'FROM `creature_template` ct ',
    'INNER JOIN `_vendor_creatures` vc ON vc.`creature_entry` = ct.`', @ct_pk_col, '` ',
    'WHERE (ct.`', @ct_npcflag_col, '` & 128) = 0'
  ),
  'SELECT ''missing_vendor_flag'' AS chk, NULL AS remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_npc_vendor > 0 AND @nv_max_col IS NOT NULL AND @nv_incr_col IS NOT NULL,
  CONCAT(
    'SELECT ''nv_maxincr_mismatch'' AS chk, COUNT(*) AS remaining FROM `npc_vendor` v ',
    'WHERE (v.`', @nv_max_col, '` = 0 AND v.`', @nv_incr_col, '` > 0) ',
    'OR (v.`', @nv_max_col, '` > 0 AND v.`', @nv_incr_col, '` = 0)'
  ),
  'SELECT ''nv_maxincr_mismatch'' AS chk, NULL AS remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_npc_vendor > 0 AND @nv_pc_col IS NOT NULL AND @has_pc > 0,
  CONCAT(
    'SELECT ''nv_invalid_playercond'' AS chk, COUNT(*) AS remaining FROM `npc_vendor` v ',
    'WHERE v.`', @nv_pc_col, '` <> 0 ',
    'AND NOT EXISTS (SELECT 1 FROM ', @pc_ref, ' pc WHERE pc.`', @pc_pk, '` = v.`', @nv_pc_col, '`)'
  ),
  'SELECT ''nv_invalid_playercond'' AS chk, NULL AS remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_item_source > 0 AND @has_npc_vendor > 0 AND @nv_item_col IS NOT NULL,
  CONCAT(
    'SELECT ''nv_missing_items'' AS chk, COUNT(*) AS remaining FROM `npc_vendor` v ',
    'WHERE NOT EXISTS (SELECT 1 FROM ', @item_ref, ' i WHERE i.`', @item_pk, '` = v.`', @nv_item_col, '`)'
  ),
  'SELECT ''nv_missing_items'' AS chk, NULL AS remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── Summary ─────────────────────────────────────────────────────── */
SELECT `action`, `tbl`, SUM(`rows_hit`) AS affected_rows
FROM `_summary_4b`
GROUP BY `action`, `tbl`
ORDER BY `tbl`, `action`;

DROP TEMPORARY TABLE IF EXISTS `_vendor_creatures`;
DROP TEMPORARY TABLE IF EXISTS `_summary_4b`;

COMMIT;

/* ── Restore session ─────────────────────────────────────────────── */
SET SQL_SAFE_UPDATES  = COALESCE(@OLD_SQL_SAFE_UPDATES, 1);
SET FOREIGN_KEY_CHECKS = COALESCE(@OLD_FOREIGN_KEY_CHECKS, 1);
SET UNIQUE_CHECKS      = COALESCE(@OLD_UNIQUE_CHECKS, 1);
SET AUTOCOMMIT         = COALESCE(@OLD_AUTOCOMMIT, 1);

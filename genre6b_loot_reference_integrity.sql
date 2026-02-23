/* Genre 6B: Loot reference integrity + group rules + MinCount repairs */
USE world;
SELECT DATABASE() AS active_database;

SET @APPLY_FIX := 0;
SET @MAX_DELETE_PER_TABLE := 5000;
SET @MAX_UPDATE_PER_TABLE := 20000;
SET @MAX_TOUCH_TOTAL := 40000;
SET @FORCE_TOUCH := 0;

SET @OLD_SQL_SAFE_UPDATES := @@SQL_SAFE_UPDATES;
SET @OLD_FOREIGN_KEY_CHECKS := @@FOREIGN_KEY_CHECKS;
SET @OLD_UNIQUE_CHECKS := @@UNIQUE_CHECKS;
SET @OLD_AUTOCOMMIT := @@AUTOCOMMIT;
SET @OLD_GROUP_CONCAT_MAX_LEN := @@SESSION.group_concat_max_len;

SET SESSION group_concat_max_len = 1024 * 1024 * 16;
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;
SET AUTOCOMMIT = 0;
START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_target_tables;
CREATE TEMPORARY TABLE tmp_target_tables (
  table_name VARCHAR(128) PRIMARY KEY
) ENGINE=InnoDB;

INSERT INTO tmp_target_tables (table_name)
SELECT x.table_name
FROM (
  SELECT 'creature_loot_template' AS table_name
  UNION ALL SELECT 'gameobject_loot_template'
  UNION ALL SELECT 'item_loot_template'
  UNION ALL SELECT 'fishing_loot_template'
  UNION ALL SELECT 'skinning_loot_template'
  UNION ALL SELECT 'pickpocketing_loot_template'
  UNION ALL SELECT 'prospecting_loot_template'
  UNION ALL SELECT 'milling_loot_template'
  UNION ALL SELECT 'disenchant_loot_template'
  UNION ALL SELECT 'spell_loot_template'
  UNION ALL SELECT 'mail_loot_template'
  UNION ALL SELECT 'reference_loot_template'
) x
WHERE EXISTS (
  SELECT 1
  FROM information_schema.tables t
  WHERE t.table_schema = DATABASE()
    AND t.table_name = x.table_name
);

DROP TEMPORARY TABLE IF EXISTS tmp_loot_tables;
CREATE TEMPORARY TABLE tmp_loot_tables (
  table_name VARCHAR(128) PRIMARY KEY,
  entry_col VARCHAR(128) NULL,
  item_col VARCHAR(128) NULL,
  reference_col VARCHAR(128) NULL,
  group_col VARCHAR(128) NULL,
  chance_col VARCHAR(128) NULL,
  mincount_col VARCHAR(128) NULL
) ENGINE=InnoDB;

INSERT INTO tmp_loot_tables (table_name, entry_col, item_col, reference_col, group_col, chance_col, mincount_col)
SELECT
  tt.table_name,
  (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = tt.table_name
      AND c.column_name IN ('Entry','entry')
    ORDER BY FIELD(c.column_name,'Entry','entry')
    LIMIT 1
  ) AS entry_col,
  (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = tt.table_name
      AND c.column_name IN ('Item','item','itemid','ItemID')
    ORDER BY FIELD(c.column_name,'Item','item','itemid','ItemID')
    LIMIT 1
  ) AS item_col,
  (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = tt.table_name
      AND c.column_name IN ('Reference','reference','Ref','ref')
    ORDER BY FIELD(c.column_name,'Reference','reference','Ref','ref')
    LIMIT 1
  ) AS reference_col,
  (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = tt.table_name
      AND c.column_name IN ('GroupId','groupid','group','GroupID')
    ORDER BY FIELD(c.column_name,'GroupId','groupid','group','GroupID')
    LIMIT 1
  ) AS group_col,
  (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = tt.table_name
      AND c.column_name IN ('ChanceOrQuestChance','chance','Chance','ChanceOrQuestChance')
    ORDER BY FIELD(c.column_name,'ChanceOrQuestChance','chance','Chance')
    LIMIT 1
  ) AS chance_col,
  (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = tt.table_name
      AND c.column_name IN ('MinCount','mincount','MinCountOrRef','mincountOrRef')
    ORDER BY FIELD(c.column_name,'MinCount','mincount','MinCountOrRef','mincountOrRef')
    LIMIT 1
  ) AS mincount_col
FROM tmp_target_tables tt;

SET @HAS_REF_TABLE := EXISTS(
  SELECT 1 FROM information_schema.tables
  WHERE table_schema = DATABASE() AND table_name = 'reference_loot_template'
);

SET @REF_ENTRY_COL := (
  SELECT c.column_name
  FROM information_schema.columns c
  WHERE c.table_schema = DATABASE() AND c.table_name = 'reference_loot_template'
    AND c.column_name IN ('Entry','entry','ID','Id')
  ORDER BY FIELD(c.column_name,'Entry','entry','ID','Id')
  LIMIT 1
);

DROP TEMPORARY TABLE IF EXISTS tmp_loot_ref_summary;
CREATE TEMPORARY TABLE tmp_loot_ref_summary (
  table_name VARCHAR(128) PRIMARY KEY,
  missing_ref_before BIGINT NOT NULL DEFAULT 0,
  group_fix_before BIGINT NOT NULL DEFAULT 0,
  mincount_fix_before BIGINT NOT NULL DEFAULT 0,
  missing_ref_after BIGINT NULL,
  group_fix_after BIGINT NULL,
  mincount_fix_after BIGINT NULL,
  deleted_missing_ref BIGINT NOT NULL DEFAULT 0,
  updated_group BIGINT NOT NULL DEFAULT 0,
  updated_mincount BIGINT NOT NULL DEFAULT 0,
  note TEXT NULL
) ENGINE=InnoDB;

SET @sql_diag := (
  SELECT GROUP_CONCAT(s.q ORDER BY s.table_name SEPARATOR ' UNION ALL ')
  FROM (
    SELECT
      lt.table_name,
      CONCAT(
        'SELECT ', QUOTE(lt.table_name), ' AS table_name, ',
        IF(@HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND lt.reference_col IS NOT NULL,
          CONCAT('SUM(CASE WHEN t.`', lt.reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL THEN 1 ELSE 0 END)'),
          '0'
        ),
        ' AS missing_ref_before, ',
        IF(lt.chance_col IS NOT NULL AND lt.group_col IS NOT NULL AND lt.item_col IS NOT NULL,
          CONCAT('SUM(CASE WHEN t.`', lt.chance_col, '` = 0 AND (t.`', lt.group_col, '` IS NULL OR t.`', lt.group_col, '` = 0) AND t.`', lt.item_col, '` > 0 THEN 1 ELSE 0 END)'),
          '0'
        ),
        ' AS group_fix_before, ',
        IF(lt.mincount_col IS NOT NULL AND lt.item_col IS NOT NULL,
          CONCAT('SUM(CASE WHEN t.`', lt.item_col, '` > 0 AND t.`', lt.mincount_col, '` = 0 THEN 1 ELSE 0 END)'),
          '0'
        ),
        ' AS mincount_fix_before, ',
        QUOTE(
          CONCAT(
            IF(lt.reference_col IS NULL, 'SKIP A: missing Reference column. ', ''),
            IF(NOT (@HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL), 'SKIP A: reference_loot_template missing or entry column not found. ', ''),
            IF(lt.chance_col IS NULL OR lt.group_col IS NULL OR lt.item_col IS NULL, 'SKIP B: required columns missing. ', ''),
            IF(lt.mincount_col IS NULL OR lt.item_col IS NULL, 'SKIP C: required columns missing. ', '')
          )
        ),
        ' AS note FROM `', lt.table_name, '` t ',
        IF(@HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND lt.reference_col IS NOT NULL,
          CONCAT('LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', lt.reference_col, '` '),
          ''
        )
      ) AS q
    FROM tmp_loot_tables lt
  ) s
);

SET @sql_diag_ins := CONCAT(
  'INSERT INTO tmp_loot_ref_summary (table_name, missing_ref_before, group_fix_before, mincount_fix_before, note) ',
  @sql_diag
);
PREPARE stmt_diag FROM @sql_diag_ins;
EXECUTE stmt_diag;
DEALLOCATE PREPARE stmt_diag;

SET @sql_sample_a := (
  SELECT GROUP_CONCAT(q SEPARATOR ' UNION ALL ')
  FROM (
    SELECT CONCAT(
      'SELECT * FROM (SELECT ', QUOTE(lt.table_name), ' AS table_name, ',
      IF(lt.entry_col IS NOT NULL, CONCAT('t.`', lt.entry_col, '`'), 'NULL'), ' AS entry_val, ',
      IF(lt.item_col IS NOT NULL, CONCAT('t.`', lt.item_col, '`'), 'NULL'), ' AS item_val, ',
      IF(lt.reference_col IS NOT NULL, CONCAT('t.`', lt.reference_col, '`'), 'NULL'), ' AS reference_val, ',
      IF(lt.group_col IS NOT NULL, CONCAT('t.`', lt.group_col, '`'), 'NULL'), ' AS groupid_val, ',
      IF(lt.chance_col IS NOT NULL, CONCAT('t.`', lt.chance_col, '`'), 'NULL'), ' AS chance_val, ',
      IF(lt.mincount_col IS NOT NULL, CONCAT('t.`', lt.mincount_col, '`'), 'NULL'), ' AS mincount_val ',
      'FROM `', lt.table_name, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', lt.reference_col, '` ',
      'WHERE t.`', lt.reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL LIMIT 25) z'
    ) AS q
    FROM tmp_loot_tables lt
    WHERE @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND lt.reference_col IS NOT NULL
  ) u
);
SET @sql_sample_a_exec := IF(@sql_sample_a IS NULL, 'SELECT ''SKIP: no table eligible for missing reference sampling'' AS note', @sql_sample_a);
PREPARE stmt_sample_a FROM @sql_sample_a_exec;
EXECUTE stmt_sample_a;
DEALLOCATE PREPARE stmt_sample_a;

SET @sql_sample_b := (
  SELECT GROUP_CONCAT(q SEPARATOR ' UNION ALL ')
  FROM (
    SELECT CONCAT(
      'SELECT * FROM (SELECT ', QUOTE(lt.table_name), ' AS table_name, ',
      IF(lt.entry_col IS NOT NULL, CONCAT('t.`', lt.entry_col, '`'), 'NULL'), ' AS entry_val, ',
      IF(lt.item_col IS NOT NULL, CONCAT('t.`', lt.item_col, '`'), 'NULL'), ' AS item_val, ',
      IF(lt.reference_col IS NOT NULL, CONCAT('t.`', lt.reference_col, '`'), 'NULL'), ' AS reference_val, ',
      IF(lt.group_col IS NOT NULL, CONCAT('t.`', lt.group_col, '`'), 'NULL'), ' AS groupid_val, ',
      IF(lt.chance_col IS NOT NULL, CONCAT('t.`', lt.chance_col, '`'), 'NULL'), ' AS chance_val, ',
      IF(lt.mincount_col IS NOT NULL, CONCAT('t.`', lt.mincount_col, '`'), 'NULL'), ' AS mincount_val ',
      'FROM `', lt.table_name, '` t ',
      'WHERE t.`', lt.chance_col, '` = 0 AND (t.`', lt.group_col, '` IS NULL OR t.`', lt.group_col, '` = 0) AND t.`', lt.item_col, '` > 0 LIMIT 25) z'
    ) AS q
    FROM tmp_loot_tables lt
    WHERE lt.chance_col IS NOT NULL AND lt.group_col IS NOT NULL AND lt.item_col IS NOT NULL
  ) u
);
SET @sql_sample_b_exec := IF(@sql_sample_b IS NULL, 'SELECT ''SKIP: no table eligible for group fix sampling'' AS note', @sql_sample_b);
PREPARE stmt_sample_b FROM @sql_sample_b_exec;
EXECUTE stmt_sample_b;
DEALLOCATE PREPARE stmt_sample_b;

SET @sql_sample_c := (
  SELECT GROUP_CONCAT(q SEPARATOR ' UNION ALL ')
  FROM (
    SELECT CONCAT(
      'SELECT * FROM (SELECT ', QUOTE(lt.table_name), ' AS table_name, ',
      IF(lt.entry_col IS NOT NULL, CONCAT('t.`', lt.entry_col, '`'), 'NULL'), ' AS entry_val, ',
      IF(lt.item_col IS NOT NULL, CONCAT('t.`', lt.item_col, '`'), 'NULL'), ' AS item_val, ',
      IF(lt.reference_col IS NOT NULL, CONCAT('t.`', lt.reference_col, '`'), 'NULL'), ' AS reference_val, ',
      IF(lt.group_col IS NOT NULL, CONCAT('t.`', lt.group_col, '`'), 'NULL'), ' AS groupid_val, ',
      IF(lt.chance_col IS NOT NULL, CONCAT('t.`', lt.chance_col, '`'), 'NULL'), ' AS chance_val, ',
      IF(lt.mincount_col IS NOT NULL, CONCAT('t.`', lt.mincount_col, '`'), 'NULL'), ' AS mincount_val ',
      'FROM `', lt.table_name, '` t ',
      'WHERE t.`', lt.item_col, '` > 0 AND t.`', lt.mincount_col, '` = 0 LIMIT 25) z'
    ) AS q
    FROM tmp_loot_tables lt
    WHERE lt.mincount_col IS NOT NULL AND lt.item_col IS NOT NULL
  ) u
);
SET @sql_sample_c_exec := IF(@sql_sample_c IS NULL, 'SELECT ''SKIP: no table eligible for mincount sampling'' AS note', @sql_sample_c);
PREPARE stmt_sample_c FROM @sql_sample_c_exec;
EXECUTE stmt_sample_c;
DEALLOCATE PREPARE stmt_sample_c;

SET @TOTAL_DELETE_CANDIDATES := (SELECT COALESCE(SUM(missing_ref_before),0) FROM tmp_loot_ref_summary);
SET @TOTAL_UPDATE_CANDIDATES := (SELECT COALESCE(SUM(group_fix_before + mincount_fix_before),0) FROM tmp_loot_ref_summary);
SET @TOTAL_TOUCH := @TOTAL_DELETE_CANDIDATES + @TOTAL_UPDATE_CANDIDATES;

SELECT @TOTAL_DELETE_CANDIDATES AS TOTAL_DELETE_CANDIDATES, @TOTAL_UPDATE_CANDIDATES AS TOTAL_UPDATE_CANDIDATES, @TOTAL_TOUCH AS TOTAL_TOUCH;

SET @OVER_DELETE_CAP_TABLES := (SELECT COUNT(*) FROM tmp_loot_ref_summary WHERE missing_ref_before > @MAX_DELETE_PER_TABLE);
SET @OVER_GROUP_CAP_TABLES := (SELECT COUNT(*) FROM tmp_loot_ref_summary WHERE group_fix_before > @MAX_UPDATE_PER_TABLE);
SET @OVER_MINCOUNT_CAP_TABLES := (SELECT COUNT(*) FROM tmp_loot_ref_summary WHERE mincount_fix_before > @MAX_UPDATE_PER_TABLE);

SET @CAPS_EXCEEDED := IF(
  @TOTAL_TOUCH > @MAX_TOUCH_TOTAL
  OR @OVER_DELETE_CAP_TABLES > 0
  OR @OVER_GROUP_CAP_TABLES > 0
  OR @OVER_MINCOUNT_CAP_TABLES > 0,
  1,
  0
);

SET @APPLY_ALLOWED := IF(@APPLY_FIX = 1 AND (@CAPS_EXCEEDED = 0 OR @FORCE_TOUCH = 1), 1, 0);

UPDATE tmp_loot_ref_summary
SET note = CONCAT(COALESCE(note,''), IF(@APPLY_FIX = 1 AND @APPLY_ALLOWED = 0, 'CAPS_EXCEEDED: apply disabled by cap controls. ', ''))
WHERE table_name IS NOT NULL;

SELECT IF(@APPLY_ALLOWED = 1, 'APPLY: enabled', 'APPLY: report-only or blocked by caps') AS apply_mode;


SET @tbl := 'creature_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table creature_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup creature_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete creature_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table creature_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup creature_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update creature_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table creature_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup creature_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update creature_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'gameobject_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table gameobject_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup gameobject_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete gameobject_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table gameobject_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup gameobject_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update gameobject_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table gameobject_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup gameobject_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update gameobject_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'item_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table item_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup item_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete item_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table item_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup item_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update item_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table item_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup item_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update item_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'fishing_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table fishing_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup fishing_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete fishing_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table fishing_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup fishing_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update fishing_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table fishing_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup fishing_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update fishing_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'skinning_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table skinning_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup skinning_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete skinning_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table skinning_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup skinning_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update skinning_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table skinning_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup skinning_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update skinning_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'pickpocketing_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table pickpocketing_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup pickpocketing_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete pickpocketing_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table pickpocketing_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup pickpocketing_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update pickpocketing_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table pickpocketing_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup pickpocketing_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update pickpocketing_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'prospecting_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table prospecting_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup prospecting_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete prospecting_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table prospecting_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup prospecting_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update prospecting_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table prospecting_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup prospecting_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update prospecting_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'milling_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table milling_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup milling_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete milling_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table milling_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup milling_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update milling_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table milling_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup milling_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update milling_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'disenchant_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table disenchant_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup disenchant_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete disenchant_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table disenchant_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup disenchant_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update disenchant_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table disenchant_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup disenchant_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update disenchant_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'spell_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table spell_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup spell_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete spell_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table spell_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup spell_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update spell_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table spell_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup spell_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update spell_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'mail_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table mail_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup mail_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete mail_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table mail_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup mail_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update mail_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table mail_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup mail_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update mail_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;


SET @tbl := 'reference_loot_template';
SET @entry_col := (SELECT entry_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @item_col := (SELECT item_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @reference_col := (SELECT reference_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @group_col := (SELECT group_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @chance_col := (SELECT chance_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @mincount_col := (SELECT mincount_col FROM tmp_loot_tables WHERE table_name = @tbl);
SET @missing_before := COALESCE((SELECT missing_ref_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @group_before := COALESCE((SELECT group_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @mincount_before := COALESCE((SELECT mincount_fix_before FROM tmp_loot_ref_summary WHERE table_name = @tbl),0);
SET @can_delete := IF(@APPLY_ALLOWED = 1 AND @missing_before > 0 AND (@missing_before <= @MAX_DELETE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_group := IF(@APPLY_ALLOWED = 1 AND @group_before > 0 AND (@group_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @can_mincount := IF(@APPLY_ALLOWED = 1 AND @mincount_before > 0 AND (@mincount_before <= @MAX_UPDATE_PER_TABLE OR @FORCE_TOUCH = 1), 1, 0);
SET @backup_a := CONCAT(@tbl, '_backup_genre6b_missing_ref');
SET @backup_b := CONCAT(@tbl, '_backup_genre6b_group_fix');
SET @backup_c := CONCAT(@tbl, '_backup_genre6b_mincount_fix');
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_a, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP A table reference_loot_template'' AS note');
PREPARE st1 FROM @sql; EXECUTE st1; DEALLOCATE PREPARE st1;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_a, '` SELECT t.* FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A backup reference_loot_template'' AS note');
PREPARE st2 FROM @sql; EXECUTE st2; DEALLOCATE PREPARE st2;
SET @sql := IF(@can_delete = 1 AND @HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND @reference_col IS NOT NULL, CONCAT('DELETE t FROM `', @tbl, '` t LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', @reference_col, '` WHERE t.`', @reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL'), 'SELECT ''SKIP A delete reference_loot_template'' AS note');
PREPARE st3 FROM @sql; EXECUTE st3; DEALLOCATE PREPARE st3;
SET @rows_a := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET deleted_missing_ref = IF(@can_delete = 1, @rows_a, 0), note = CONCAT(COALESCE(note, ''), IF(@can_delete = 0 AND @missing_before > 0, 'SKIP A: per-table delete cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_b, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP B table reference_loot_template'' AS note');
PREPARE st4 FROM @sql; EXECUTE st4; DEALLOCATE PREPARE st4;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_b, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B backup reference_loot_template'' AS note');
PREPARE st5 FROM @sql; EXECUTE st5; DEALLOCATE PREPARE st5;
SET @sql := IF(@can_group = 1 AND @entry_col IS NOT NULL AND @item_col IS NOT NULL AND @group_col IS NOT NULL AND @chance_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t JOIN (SELECT `', @entry_col, '` AS e, COALESCE(MAX(`', @group_col, '`),0)+1 AS next_groupid FROM `', @tbl, '` GROUP BY `', @entry_col, '`) g ON g.e = t.`', @entry_col, '` SET t.`', @group_col, '` = g.next_groupid WHERE t.`', @chance_col, '` = 0 AND (t.`', @group_col, '` IS NULL OR t.`', @group_col, '` = 0) AND t.`', @item_col, '` > 0'), 'SELECT ''SKIP B update reference_loot_template'' AS note');
PREPARE st6 FROM @sql; EXECUTE st6; DEALLOCATE PREPARE st6;
SET @rows_b := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_group = IF(@can_group = 1, @rows_b, 0), note = CONCAT(COALESCE(note, ''), IF(@can_group = 0 AND @group_before > 0, 'SKIP B: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('CREATE TABLE IF NOT EXISTS `', @backup_c, '` LIKE `', @tbl, '`'), 'SELECT ''SKIP C table reference_loot_template'' AS note');
PREPARE st7 FROM @sql; EXECUTE st7; DEALLOCATE PREPARE st7;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('INSERT IGNORE INTO `', @backup_c, '` SELECT t.* FROM `', @tbl, '` t WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C backup reference_loot_template'' AS note');
PREPARE st8 FROM @sql; EXECUTE st8; DEALLOCATE PREPARE st8;
SET @sql := IF(@can_mincount = 1 AND @item_col IS NOT NULL AND @mincount_col IS NOT NULL, CONCAT('UPDATE `', @tbl, '` t SET t.`', @mincount_col, '` = 1 WHERE t.`', @item_col, '` > 0 AND t.`', @mincount_col, '` = 0'), 'SELECT ''SKIP C update reference_loot_template'' AS note');
PREPARE st9 FROM @sql; EXECUTE st9; DEALLOCATE PREPARE st9;
SET @rows_c := ROW_COUNT();
UPDATE tmp_loot_ref_summary SET updated_mincount = IF(@can_mincount = 1, @rows_c, 0), note = CONCAT(COALESCE(note, ''), IF(@can_mincount = 0 AND @mincount_before > 0, 'SKIP C: per-table update cap exceeded or apply disabled. ', '')) WHERE table_name = @tbl;

SET @sql_after := (
  SELECT GROUP_CONCAT(s.q ORDER BY s.table_name SEPARATOR ' UNION ALL ')
  FROM (
    SELECT
      lt.table_name,
      CONCAT(
        'SELECT ', QUOTE(lt.table_name), ' AS table_name, ',
        IF(@HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND lt.reference_col IS NOT NULL,
          CONCAT('SUM(CASE WHEN t.`', lt.reference_col, '` > 0 AND r.`', @REF_ENTRY_COL, '` IS NULL THEN 1 ELSE 0 END)'),
          '0'
        ),
        ' AS missing_ref_after, ',
        IF(lt.chance_col IS NOT NULL AND lt.group_col IS NOT NULL AND lt.item_col IS NOT NULL,
          CONCAT('SUM(CASE WHEN t.`', lt.chance_col, '` = 0 AND (t.`', lt.group_col, '` IS NULL OR t.`', lt.group_col, '` = 0) AND t.`', lt.item_col, '` > 0 THEN 1 ELSE 0 END)'),
          '0'
        ),
        ' AS group_fix_after, ',
        IF(lt.mincount_col IS NOT NULL AND lt.item_col IS NOT NULL,
          CONCAT('SUM(CASE WHEN t.`', lt.item_col, '` > 0 AND t.`', lt.mincount_col, '` = 0 THEN 1 ELSE 0 END)'),
          '0'
        ),
        ' AS mincount_fix_after FROM `', lt.table_name, '` t ',
        IF(@HAS_REF_TABLE = 1 AND @REF_ENTRY_COL IS NOT NULL AND lt.reference_col IS NOT NULL,
          CONCAT('LEFT JOIN `reference_loot_template` r ON r.`', @REF_ENTRY_COL, '` = t.`', lt.reference_col, '` '),
          ''
        )
      ) AS q
    FROM tmp_loot_tables lt
  ) s
);

DROP TEMPORARY TABLE IF EXISTS tmp_after_counts;
CREATE TEMPORARY TABLE tmp_after_counts (
  table_name VARCHAR(128) PRIMARY KEY,
  missing_ref_after BIGINT NOT NULL,
  group_fix_after BIGINT NOT NULL,
  mincount_fix_after BIGINT NOT NULL
) ENGINE=InnoDB;

SET @sql_after_ins := CONCAT('INSERT INTO tmp_after_counts (table_name, missing_ref_after, group_fix_after, mincount_fix_after) ', @sql_after);
PREPARE stmt_after FROM @sql_after_ins;
EXECUTE stmt_after;
DEALLOCATE PREPARE stmt_after;

UPDATE tmp_loot_ref_summary s
JOIN tmp_after_counts a ON a.table_name = s.table_name
SET s.missing_ref_after = a.missing_ref_after,
    s.group_fix_after = a.group_fix_after,
    s.mincount_fix_after = a.mincount_fix_after
WHERE s.table_name IS NOT NULL;

SELECT
  table_name,
  missing_ref_before,
  missing_ref_after,
  deleted_missing_ref,
  group_fix_before,
  group_fix_after,
  updated_group,
  mincount_fix_before,
  mincount_fix_after,
  updated_mincount,
  note
FROM tmp_loot_ref_summary
ORDER BY table_name;

COMMIT;

SET SQL_SAFE_UPDATES = @OLD_SQL_SAFE_UPDATES;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS;
SET AUTOCOMMIT = @OLD_AUTOCOMMIT;
SET SESSION group_concat_max_len = @OLD_GROUP_CONCAT_MAX_LEN;

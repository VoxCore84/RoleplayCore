/* ================================================================== */
/* GENRE 7A v2 — AreaTrigger orphan spawn cleanup                     */
/* TrinityCore Midnight 12.x (TWW 11.1.7)                            */
/*                                                                    */
/* Deletes areatrigger rows whose CreatePropertiesId doesn't exist    */
/* in any known source table (world/hotfixes variants).               */
/*                                                                    */
/* v2 fixes over v1:                                                  */
/*   - Removed embedded GitHub review comment (syntax error)          */
/*   - Added AreaTriggerCreatePropertiesId to column detection        */
/*     (canonical column name in TC Midnight schema)                  */
/*   - DDL (backup table) BEFORE START TRANSACTION                    */
/*   - ROW_COUNT() captured BEFORE DEALLOCATE PREPARE                 */
/*   - COALESCE on session variable restores                          */
/*   - Conditional COMMIT/ROLLBACK via @APPLY_FIX                    */
/*                                                                    */
/* SET @APPLY_FIX := 0 for dry-run diagnostics only.                  */
/* SET @APPLY_FIX := 1 to apply mutations.                            */
/*                                                                    */
/* IMPORTANT: Run the COMPLETE file. Do not paste fragments.          */
/* ================================================================== */

SET @APPLY_FIX    := 1;
SET @MAX_DELETE   := 5000;
SET @FORCE_DELETE := 0;

USE `world`;
SELECT DATABASE() AS active_database;

/* ── Session snapshot ────────────────────────────────────────────── */
SET @OLD_SQL_SAFE_UPDATES   := COALESCE(@@sql_safe_updates, 1);
SET @OLD_FOREIGN_KEY_CHECKS := COALESCE(@@foreign_key_checks, 1);
SET @OLD_UNIQUE_CHECKS      := COALESCE(@@unique_checks, 1);
SET @OLD_AUTOCOMMIT         := COALESCE(@@autocommit, 1);

SET sql_safe_updates  = 0;
SET foreign_key_checks = 1;
SET unique_checks      = 1;
SET autocommit         = 0;

/* ================================================================== */
/* SCHEMA INTROSPECTION                                               */
/* ================================================================== */
SELECT 'SCHEMA INTROSPECTION' AS section;

SELECT COUNT(*) INTO @has_areatrigger
FROM information_schema.tables
WHERE table_schema = 'world'
  AND table_name = 'areatrigger';

SELECT COLUMN_NAME INTO @spawn_pk_col
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger'
  AND column_name IN ('SpawnId', 'spawnId', 'guid', 'GUID', 'id', 'ID')
ORDER BY FIELD(column_name, 'SpawnId', 'spawnId', 'guid', 'GUID', 'id', 'ID')
LIMIT 1;

/* v2: Added AreaTriggerCreatePropertiesId — canonical column name
   in TrinityCore Midnight schema (sql/base/dev/world_database.sql) */
SELECT COLUMN_NAME INTO @spawn_cp_col
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger'
  AND column_name IN (
    'AreaTriggerCreatePropertiesId',
    'CreatePropertiesId',
    'createPropertiesId',
    'CreatePropertiesID',
    'create_properties_id'
  )
ORDER BY FIELD(column_name,
  'AreaTriggerCreatePropertiesId',
  'CreatePropertiesId',
  'createPropertiesId',
  'CreatePropertiesID',
  'create_properties_id'
)
LIMIT 1;

SELECT COLUMN_NAME INTO @spawn_map_col
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger'
  AND column_name IN ('map', 'Map', 'mapId', 'MapId', 'MapID')
ORDER BY FIELD(column_name, 'map', 'Map', 'mapId', 'MapId', 'MapID')
LIMIT 1;

SELECT
  IF(@has_areatrigger = 1, 'OK', 'MISSING') AS areatrigger_table,
  COALESCE(@spawn_pk_col, 'NOT FOUND')      AS pk_column,
  COALESCE(@spawn_cp_col, 'NOT FOUND')      AS create_properties_column,
  COALESCE(@spawn_map_col, 'NOT FOUND')     AS map_column;

/* ── Reference source tables ─────────────────────────────────────── */
SELECT COUNT(*) INTO @src_world_acp_exists
FROM information_schema.tables
WHERE table_schema = 'world' AND table_name = 'areatrigger_create_properties';

SELECT COLUMN_NAME INTO @src_world_acp_pk
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger_create_properties'
  AND column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
ORDER BY FIELD(column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
LIMIT 1;

SELECT COUNT(*) INTO @src_hotfixes_acp_exists
FROM information_schema.tables
WHERE table_schema = 'hotfixes' AND table_name = 'areatrigger_create_properties';

SELECT COLUMN_NAME INTO @src_hotfixes_acp_pk
FROM information_schema.columns
WHERE table_schema = 'hotfixes'
  AND table_name = 'areatrigger_create_properties'
  AND column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
ORDER BY FIELD(column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
LIMIT 1;

SELECT COUNT(*) INTO @src_world_acpt_exists
FROM information_schema.tables
WHERE table_schema = 'world' AND table_name = 'areatrigger_create_properties_template';

SELECT COLUMN_NAME INTO @src_world_acpt_pk
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger_create_properties_template'
  AND column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
ORDER BY FIELD(column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
LIMIT 1;

SELECT COUNT(*) INTO @src_hotfixes_acpt_exists
FROM information_schema.tables
WHERE table_schema = 'hotfixes' AND table_name = 'areatrigger_create_properties_template';

SELECT COLUMN_NAME INTO @src_hotfixes_acpt_pk
FROM information_schema.columns
WHERE table_schema = 'hotfixes'
  AND table_name = 'areatrigger_create_properties_template'
  AND column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
ORDER BY FIELD(column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
LIMIT 1;

SET @has_any_cp_source :=
  (CASE WHEN @src_world_acp_exists = 1 AND @src_world_acp_pk IS NOT NULL THEN 1 ELSE 0 END) +
  (CASE WHEN @src_hotfixes_acp_exists = 1 AND @src_hotfixes_acp_pk IS NOT NULL THEN 1 ELSE 0 END) +
  (CASE WHEN @src_world_acpt_exists = 1 AND @src_world_acpt_pk IS NOT NULL THEN 1 ELSE 0 END) +
  (CASE WHEN @src_hotfixes_acpt_exists = 1 AND @src_hotfixes_acpt_pk IS NOT NULL THEN 1 ELSE 0 END);

SELECT
  IF(@src_world_acp_exists = 1 AND @src_world_acp_pk IS NOT NULL,
     CONCAT('OK (', @src_world_acp_pk, ')'), 'SKIP') AS world_acp,
  IF(@src_hotfixes_acp_exists = 1 AND @src_hotfixes_acp_pk IS NOT NULL,
     CONCAT('OK (', @src_hotfixes_acp_pk, ')'), 'SKIP') AS hotfixes_acp,
  IF(@src_world_acpt_exists = 1 AND @src_world_acpt_pk IS NOT NULL,
     CONCAT('OK (', @src_world_acpt_pk, ')'), 'SKIP') AS world_acpt,
  IF(@src_hotfixes_acpt_exists = 1 AND @src_hotfixes_acpt_pk IS NOT NULL,
     CONCAT('OK (', @src_hotfixes_acpt_pk, ')'), 'SKIP') AS hotfixes_acpt,
  @has_any_cp_source AS total_sources;

/* ================================================================== */
/* DDL PHASE — backup table (before transaction)                      */
/* ================================================================== */
SELECT 'BACKUP TABLE CREATION (DDL)' AS section;

/* Pre-check: can we potentially apply? */
SET @prereqs_ok := IF(
  @has_areatrigger = 1
  AND @spawn_pk_col IS NOT NULL
  AND @spawn_cp_col IS NOT NULL
  AND @has_any_cp_source > 0,
  1, 0
);

SET @sql := IF(@APPLY_FIX = 1 AND @prereqs_ok = 1,
  'CREATE TABLE IF NOT EXISTS `world`.`areatrigger_backup_genre7a` LIKE `world`.`areatrigger`',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* DML PHASE                                                          */
/* ================================================================== */
START TRANSACTION;

/* ── Build reference ID lookup ───────────────────────────────────── */
SELECT 'LOADING REFERENCE IDs' AS section;

DROP TEMPORARY TABLE IF EXISTS tmp_create_property_ids;
DROP TEMPORARY TABLE IF EXISTS tmp_invalid_spawns;

CREATE TEMPORARY TABLE tmp_create_property_ids (
  id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TEMPORARY TABLE tmp_invalid_spawns (
  spawn_pk BIGINT UNSIGNED NOT NULL,
  create_properties_id BIGINT UNSIGNED NOT NULL,
  map_id BIGINT NULL,
  PRIMARY KEY (spawn_pk)
) ENGINE=InnoDB;

/* Load from each available source */
SET @sql := IF(@src_world_acp_exists = 1 AND @src_world_acp_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_world_acp_pk, '` AS UNSIGNED) FROM `world`.`areatrigger_create_properties` WHERE `', @src_world_acp_pk, '` IS NOT NULL'),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@src_hotfixes_acp_exists = 1 AND @src_hotfixes_acp_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_hotfixes_acp_pk, '` AS UNSIGNED) FROM `hotfixes`.`areatrigger_create_properties` WHERE `', @src_hotfixes_acp_pk, '` IS NOT NULL'),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@src_world_acpt_exists = 1 AND @src_world_acpt_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_world_acpt_pk, '` AS UNSIGNED) FROM `world`.`areatrigger_create_properties_template` WHERE `', @src_world_acpt_pk, '` IS NOT NULL'),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@src_hotfixes_acpt_exists = 1 AND @src_hotfixes_acpt_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_hotfixes_acpt_pk, '` AS UNSIGNED) FROM `hotfixes`.`areatrigger_create_properties_template` WHERE `', @src_hotfixes_acpt_pk, '` IS NOT NULL'),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SELECT COUNT(*) INTO @cp_reference_count FROM tmp_create_property_ids;
SELECT @cp_reference_count AS reference_ids_loaded, @has_any_cp_source AS source_tables_used;

/* ── Scan for invalid spawns ─────────────────────────────────────── */
SELECT 'SCANNING FOR INVALID SPAWNS' AS section;

SET @map_expr := IF(@spawn_map_col IS NULL, 'NULL', CONCAT('CAST(a.`', @spawn_map_col, '` AS SIGNED)'));

SET @sql := IF(@prereqs_ok = 1,
  CONCAT(
    'INSERT INTO tmp_invalid_spawns (spawn_pk, create_properties_id, map_id) ',
    'SELECT CAST(a.`', @spawn_pk_col, '` AS UNSIGNED), CAST(a.`', @spawn_cp_col, '` AS UNSIGNED), ', @map_expr, ' ',
    'FROM `world`.`areatrigger` a ',
    'LEFT JOIN tmp_create_property_ids cp ON cp.id = CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) ',
    'WHERE CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) > 0 AND cp.id IS NULL'
  ),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SELECT COUNT(*) INTO @invalid_before FROM tmp_invalid_spawns;

/* ── Sample + map breakdown ──────────────────────────────────────── */
SET @sql := IF(@prereqs_ok = 1 AND @invalid_before > 0,
  'SELECT spawn_pk AS spawnPK, create_properties_id AS CreatePropertiesId, map_id AS map FROM tmp_invalid_spawns ORDER BY spawn_pk LIMIT 50',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@prereqs_ok = 1 AND @invalid_before > 0 AND @spawn_map_col IS NOT NULL,
  'SELECT map_id AS map, COUNT(*) AS invalid_count FROM tmp_invalid_spawns GROUP BY map_id ORDER BY invalid_count DESC, map_id ASC LIMIT 25',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── Apply decision ──────────────────────────────────────────────── */
SET @deleted_rows := 0;

SET @can_apply := IF(
  @APPLY_FIX = 1
  AND @prereqs_ok = 1
  AND @invalid_before > 0
  AND (@invalid_before <= @MAX_DELETE OR @FORCE_DELETE = 1),
  1, 0
);

SET @cap_note :=
  CASE
    WHEN @APPLY_FIX <> 1 THEN 'DRY RUN: report-only mode (@APPLY_FIX=0).'
    WHEN @prereqs_ok = 0 THEN 'Apply skipped: prerequisites missing.'
    WHEN @invalid_before = 0 THEN 'Apply mode: no invalid rows found.'
    WHEN @invalid_before > @MAX_DELETE AND @FORCE_DELETE = 0
      THEN CONCAT('Delete BLOCKED by cap: ', @invalid_before, ' rows exceeds @MAX_DELETE=', @MAX_DELETE, '. Set @FORCE_DELETE=1 to override.')
    ELSE CONCAT('Apply mode: deleting ', @invalid_before, ' rows.')
  END;

SELECT @cap_note AS apply_decision;

/* ── Backup + delete ─────────────────────────────────────────────── */
SET @sql := IF(@can_apply = 1,
  CONCAT(
    'INSERT IGNORE INTO `world`.`areatrigger_backup_genre7a` ',
    'SELECT a.* FROM `world`.`areatrigger` a ',
    'INNER JOIN tmp_invalid_spawns x ON x.spawn_pk = CAST(a.`', @spawn_pk_col, '` AS UNSIGNED)'
  ),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@can_apply = 1,
  CONCAT(
    'DELETE a FROM `world`.`areatrigger` a ',
    'INNER JOIN tmp_invalid_spawns x ON x.spawn_pk = CAST(a.`', @spawn_pk_col, '` AS UNSIGNED)'
  ),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @deleted_rows := IF(@can_apply = 1, ROW_COUNT(), 0);
DEALLOCATE PREPARE stmt;

/* ── Verification ────────────────────────────────────────────────── */
SELECT 'VERIFICATION' AS section;

SET @invalid_after := 0;
SET @sql := IF(@prereqs_ok = 1,
  CONCAT(
    'SELECT COUNT(*) INTO @invalid_after ',
    'FROM `world`.`areatrigger` a ',
    'LEFT JOIN tmp_create_property_ids cp ON cp.id = CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) ',
    'WHERE CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) > 0 AND cp.id IS NULL'
  ),
  'SET @invalid_after := 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* SUMMARY                                                            */
/* ================================================================== */
SELECT 'SUMMARY' AS section;

SELECT
  @invalid_before AS invalid_before,
  @deleted_rows   AS deleted_rows,
  @invalid_after  AS invalid_after,
  @cap_note       AS notes;

SELECT IF(@can_apply = 1, 'APPLIED — committing changes',
  IF(@APPLY_FIX = 0, 'DRY RUN — rolling back', 'BLOCKED — rolling back')) AS mode;

/* ── Commit or rollback ──────────────────────────────────────────── */
SET @sql := IF(@can_apply = 1, 'COMMIT', 'ROLLBACK');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── Cleanup ─────────────────────────────────────────────────────── */
DROP TEMPORARY TABLE IF EXISTS tmp_create_property_ids;
DROP TEMPORARY TABLE IF EXISTS tmp_invalid_spawns;

/* ── Restore session ─────────────────────────────────────────────── */
SET sql_safe_updates   = COALESCE(@OLD_SQL_SAFE_UPDATES, 1);
SET foreign_key_checks = COALESCE(@OLD_FOREIGN_KEY_CHECKS, 1);
SET unique_checks      = COALESCE(@OLD_UNIQUE_CHECKS, 1);
SET autocommit         = COALESCE(@OLD_AUTOCOMMIT, 1);

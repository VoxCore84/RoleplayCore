SET @APPLY_FIX := 0;
SET @MAX_DELETE := 5000;
SET @FORCE_DELETE := 0;

USE world;
SELECT DATABASE() AS active_database;

SET @OLD_SQL_SAFE_UPDATES := @@sql_safe_updates;
SET @OLD_FOREIGN_KEY_CHECKS := @@foreign_key_checks;
SET @OLD_UNIQUE_CHECKS := @@unique_checks;
SET @OLD_AUTOCOMMIT := @@autocommit;

SET sql_safe_updates = 0;
SET foreign_key_checks = 1;
SET unique_checks = 1;
SET autocommit = 0;

START TRANSACTION;

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

SELECT COLUMN_NAME INTO @spawn_cp_col
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger'
  AND column_name IN ('CreatePropertiesId', 'createPropertiesId', 'CreatePropertiesID', 'create_properties_id')
ORDER BY FIELD(column_name, 'CreatePropertiesId', 'createPropertiesId', 'CreatePropertiesID', 'create_properties_id')
LIMIT 1;

SELECT COLUMN_NAME INTO @spawn_map_col
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger'
  AND column_name IN ('map', 'Map', 'mapId', 'MapId')
ORDER BY FIELD(column_name, 'map', 'Map', 'mapId', 'MapId')
LIMIT 1;

SET @sql_guard := IF(
  @has_areatrigger = 1,
  'SELECT ''OK: world.areatrigger found'' AS note',
  'SELECT ''SKIP: world.areatrigger missing; diagnostics and apply steps skipped'' AS note'
);
PREPARE stmt FROM @sql_guard;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_guard := IF(
  @has_areatrigger = 1 AND @spawn_pk_col IS NOT NULL,
  CONCAT('SELECT ''OK: spawn PK column detected: ', @spawn_pk_col, ''' AS note'),
  'SELECT ''SKIP: spawn PK column missing; diagnostics and apply steps skipped'' AS note'
);
PREPARE stmt FROM @sql_guard;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_guard := IF(
  @has_areatrigger = 1 AND @spawn_cp_col IS NOT NULL,
  CONCAT('SELECT ''OK: CreatePropertiesId column detected: ', @spawn_cp_col, ''' AS note'),
  'SELECT ''SKIP: CreatePropertiesId column missing; diagnostics and apply steps skipped'' AS note'
);
PREPARE stmt FROM @sql_guard;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SELECT COUNT(*) INTO @src_world_acp_exists
FROM information_schema.tables
WHERE table_schema = 'world'
  AND table_name = 'areatrigger_create_properties';

SELECT COLUMN_NAME INTO @src_world_acp_pk
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger_create_properties'
  AND column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
ORDER BY FIELD(column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
LIMIT 1;

SELECT COUNT(*) INTO @src_hotfixes_acp_exists
FROM information_schema.tables
WHERE table_schema = 'hotfixes'
  AND table_name = 'areatrigger_create_properties';

SELECT COLUMN_NAME INTO @src_hotfixes_acp_pk
FROM information_schema.columns
WHERE table_schema = 'hotfixes'
  AND table_name = 'areatrigger_create_properties'
  AND column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
ORDER BY FIELD(column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
LIMIT 1;

SELECT COUNT(*) INTO @src_world_acpt_exists
FROM information_schema.tables
WHERE table_schema = 'world'
  AND table_name = 'areatrigger_create_properties_template';

SELECT COLUMN_NAME INTO @src_world_acpt_pk
FROM information_schema.columns
WHERE table_schema = 'world'
  AND table_name = 'areatrigger_create_properties_template'
  AND column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
ORDER BY FIELD(column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
LIMIT 1;

SELECT COUNT(*) INTO @src_hotfixes_acpt_exists
FROM information_schema.tables
WHERE table_schema = 'hotfixes'
  AND table_name = 'areatrigger_create_properties_template';

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

SET @sql_insert_cp := IF(
  @src_world_acp_exists = 1 AND @src_world_acp_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_world_acp_pk, '` AS UNSIGNED) FROM `world`.`areatrigger_create_properties` WHERE `', @src_world_acp_pk, '` IS NOT NULL'),
  'SELECT ''SKIP: source world.areatrigger_create_properties unavailable'' AS note'
);
PREPARE stmt FROM @sql_insert_cp;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_insert_cp := IF(
  @src_hotfixes_acp_exists = 1 AND @src_hotfixes_acp_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_hotfixes_acp_pk, '` AS UNSIGNED) FROM `hotfixes`.`areatrigger_create_properties` WHERE `', @src_hotfixes_acp_pk, '` IS NOT NULL'),
  'SELECT ''SKIP: source hotfixes.areatrigger_create_properties unavailable'' AS note'
);
PREPARE stmt FROM @sql_insert_cp;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_insert_cp := IF(
  @src_world_acpt_exists = 1 AND @src_world_acpt_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_world_acpt_pk, '` AS UNSIGNED) FROM `world`.`areatrigger_create_properties_template` WHERE `', @src_world_acpt_pk, '` IS NOT NULL'),
  'SELECT ''SKIP: source world.areatrigger_create_properties_template unavailable'' AS note'
);
PREPARE stmt FROM @sql_insert_cp;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_insert_cp := IF(
  @src_hotfixes_acpt_exists = 1 AND @src_hotfixes_acpt_pk IS NOT NULL,
  CONCAT('INSERT IGNORE INTO tmp_create_property_ids (id) SELECT DISTINCT CAST(`', @src_hotfixes_acpt_pk, '` AS UNSIGNED) FROM `hotfixes`.`areatrigger_create_properties_template` WHERE `', @src_hotfixes_acpt_pk, '` IS NOT NULL'),
  'SELECT ''SKIP: source hotfixes.areatrigger_create_properties_template unavailable'' AS note'
);
PREPARE stmt FROM @sql_insert_cp;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SELECT COUNT(*) INTO @cp_reference_count FROM tmp_create_property_ids;

SET @sql_cp_status := IF(
  @has_any_cp_source > 0,
  CONCAT('SELECT ''OK: reference create-properties IDs loaded: ', @cp_reference_count, ''' AS note'),
  'SELECT ''SKIP: no create-properties source table detected; diagnostics and apply steps skipped'' AS note'
);
PREPARE stmt FROM @sql_cp_status;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @map_expr := IF(@spawn_map_col IS NULL, 'NULL', CONCAT('CAST(a.`', @spawn_map_col, '` AS SIGNED)'));

SET @sql_collect_invalid := IF(
  @has_areatrigger = 1 AND @spawn_pk_col IS NOT NULL AND @spawn_cp_col IS NOT NULL AND @has_any_cp_source > 0,
  CONCAT(
    'INSERT INTO tmp_invalid_spawns (spawn_pk, create_properties_id, map_id) ',
    'SELECT CAST(a.`', @spawn_pk_col, '` AS UNSIGNED), CAST(a.`', @spawn_cp_col, '` AS UNSIGNED), ', @map_expr, ' ',
    'FROM `world`.`areatrigger` a ',
    'LEFT JOIN tmp_create_property_ids cp ON cp.id = CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) ',
    'WHERE CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) > 0 AND cp.id IS NULL'
  ),
  'SELECT ''SKIP: prerequisites not met for invalid-spawn scan'' AS note'
);
PREPARE stmt FROM @sql_collect_invalid;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SELECT COUNT(*) INTO @invalid_before FROM tmp_invalid_spawns;

SET @sql_sample := IF(
  @has_areatrigger = 1 AND @spawn_pk_col IS NOT NULL AND @spawn_cp_col IS NOT NULL AND @has_any_cp_source > 0,
  'SELECT spawn_pk AS spawnPK, create_properties_id AS CreatePropertiesId, map_id AS map FROM tmp_invalid_spawns ORDER BY spawn_pk LIMIT 50',
  'SELECT ''SKIP: invalid sample unavailable because prerequisites are missing'' AS note'
);
PREPARE stmt FROM @sql_sample;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_map_top := IF(
  @has_areatrigger = 1 AND @spawn_pk_col IS NOT NULL AND @spawn_cp_col IS NOT NULL AND @has_any_cp_source > 0 AND @spawn_map_col IS NOT NULL,
  'SELECT map_id AS map, COUNT(*) AS invalid_count FROM tmp_invalid_spawns GROUP BY map_id ORDER BY invalid_count DESC, map_id ASC LIMIT 25',
  'SELECT ''SKIP: map breakdown unavailable (map column missing or prerequisites missing)'' AS note'
);
PREPARE stmt FROM @sql_map_top;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @deleted_rows := 0;
SET @cap_note := 'Report-only mode (@APPLY_FIX=0).';

SET @can_apply :=
  CASE
    WHEN @APPLY_FIX <> 1 THEN 0
    WHEN NOT (@has_areatrigger = 1 AND @spawn_pk_col IS NOT NULL AND @spawn_cp_col IS NOT NULL AND @has_any_cp_source > 0) THEN 0
    WHEN @invalid_before = 0 THEN 0
    WHEN @invalid_before > @MAX_DELETE AND @FORCE_DELETE = 0 THEN 0
    ELSE 1
  END;

SET @cap_note :=
  CASE
    WHEN @APPLY_FIX <> 1 THEN 'Report-only mode (@APPLY_FIX=0).'
    WHEN NOT (@has_areatrigger = 1 AND @spawn_pk_col IS NOT NULL AND @spawn_cp_col IS NOT NULL AND @has_any_cp_source > 0) THEN 'Apply skipped: prerequisites missing.'
    WHEN @invalid_before = 0 THEN 'Apply mode: no invalid rows found.'
    WHEN @invalid_before > @MAX_DELETE AND @FORCE_DELETE = 0 THEN CONCAT('Delete blocked by cap: invalid rows ', @invalid_before, ' exceeds @MAX_DELETE ', @MAX_DELETE, ' and @FORCE_DELETE=0.')
    WHEN @invalid_before > @MAX_DELETE AND @FORCE_DELETE = 1 THEN CONCAT('Force delete enabled: invalid rows ', @invalid_before, ' exceeds @MAX_DELETE ', @MAX_DELETE, '.')
    ELSE CONCAT('Apply mode: delete allowed for ', @invalid_before, ' rows.')
  END;

SET @sql_cap_note := CONCAT('SELECT ', QUOTE(@cap_note), ' AS note');
PREPARE stmt FROM @sql_cap_note;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_backup_table := IF(
  @can_apply = 1,
  'CREATE TABLE IF NOT EXISTS `world`.`areatrigger_backup_genre7a` LIKE `world`.`areatrigger`',
  'SELECT ''SKIP: backup table creation not required'' AS note'
);
PREPARE stmt FROM @sql_backup_table;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_backup_rows := IF(
  @can_apply = 1,
  CONCAT(
    'INSERT IGNORE INTO `world`.`areatrigger_backup_genre7a` ',
    'SELECT a.* FROM `world`.`areatrigger` a ',
    'INNER JOIN tmp_invalid_spawns x ON x.spawn_pk = CAST(a.`', @spawn_pk_col, '` AS UNSIGNED)'
  ),
  'SELECT ''SKIP: backup rows not written'' AS note'
);
PREPARE stmt FROM @sql_backup_rows;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql_delete_rows := IF(
  @can_apply = 1,
  CONCAT(
    'DELETE a FROM `world`.`areatrigger` a ',
    'INNER JOIN tmp_invalid_spawns x ON x.spawn_pk = CAST(a.`', @spawn_pk_col, '` AS UNSIGNED)'
  ),
  'SELECT ''SKIP: delete not executed'' AS note'
);
PREPARE stmt FROM @sql_delete_rows;
EXECUTE stmt;
SELECT IF(@can_apply = 1, ROW_COUNT(), 0) INTO @deleted_rows;
DEALLOCATE PREPARE stmt;

SET @sql_invalid_after := IF(
  @has_areatrigger = 1 AND @spawn_pk_col IS NOT NULL AND @spawn_cp_col IS NOT NULL AND @has_any_cp_source > 0,
  CONCAT(
    'SELECT COUNT(*) INTO @invalid_after ',
    'FROM `world`.`areatrigger` a ',
    'LEFT JOIN tmp_create_property_ids cp ON cp.id = CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) ',
    'WHERE CAST(a.`', @spawn_cp_col, '` AS UNSIGNED) > 0 AND cp.id IS NULL'
  ),
  'SELECT @invalid_after := 0'
);
PREPARE stmt FROM @sql_invalid_after;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SELECT
  @invalid_before AS invalid_before,
  @deleted_rows AS deleted_rows,
  @invalid_after AS invalid_after,
  @cap_note AS cap_notes;

COMMIT;

SET sql_safe_updates = @OLD_SQL_SAFE_UPDATES;
SET foreign_key_checks = @OLD_FOREIGN_KEY_CHECKS;
SET unique_checks = @OLD_UNIQUE_CHECKS;
SET autocommit = @OLD_AUTOCOMMIT;

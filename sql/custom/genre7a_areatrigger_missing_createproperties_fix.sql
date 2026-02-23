/* GENRE 7A v2: Areatrigger spawns referencing missing CreatePropertiesId */

SET @APPLY_FIX = 1;
SET @MAX_DELETE = 5000;
SET @FORCE_DELETE = 0;

USE world;
SELECT DATABASE() AS active_database;

SET @OLD_SQL_SAFE_UPDATES = @@sql_safe_updates;
SET @OLD_FOREIGN_KEY_CHECKS = @@foreign_key_checks;
SET @OLD_UNIQUE_CHECKS = @@unique_checks;
SET @OLD_AUTOCOMMIT = @@autocommit;

SET SESSION sql_safe_updates = 0;
SET SESSION foreign_key_checks = 0;
SET SESSION unique_checks = 0;
SET SESSION autocommit = 0;
START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_create_col_matches;
CREATE TEMPORARY TABLE tmp_create_col_matches (
  column_name VARCHAR(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  lower_name VARCHAR(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  preferred_rank INT NOT NULL,
  PRIMARY KEY (column_name)
) ENGINE=InnoDB;

SET @areatrigger_exists = (
  SELECT COUNT(*)
  FROM information_schema.tables
  WHERE table_schema = 'world'
    AND table_name = 'areatrigger'
);

INSERT INTO tmp_create_col_matches (column_name, lower_name, preferred_rank)
SELECT
  c.column_name,
  LOWER(c.column_name) AS lower_name,
  CASE LOWER(c.column_name)
    WHEN 'createpropertiesid' THEN 1
    WHEN 'create_properties_id' THEN 2
    WHEN 'areatriggercreatepropertiesid' THEN 3
    WHEN 'area_trigger_create_properties_id' THEN 4
    ELSE 999
  END AS preferred_rank
FROM information_schema.columns c
WHERE c.table_schema = 'world'
  AND c.table_name = 'areatrigger'
  AND LOWER(c.column_name) REGEXP 'create.*propert';

SET @spawn_pk_col = (
  SELECT c.column_name
  FROM information_schema.columns c
  WHERE c.table_schema = 'world'
    AND c.table_name = 'areatrigger'
    AND c.column_name IN ('SpawnId', 'spawnId', 'guid', 'GUID', 'id', 'ID')
  ORDER BY FIELD(c.column_name, 'SpawnId', 'spawnId', 'guid', 'GUID', 'id', 'ID')
  LIMIT 1
);

SET @map_col = (
  SELECT c.column_name
  FROM information_schema.columns c
  WHERE c.table_schema = 'world'
    AND c.table_name = 'areatrigger'
    AND c.column_name IN ('map', 'Map', 'mapId', 'MapId')
  ORDER BY FIELD(c.column_name, 'map', 'Map', 'mapId', 'MapId')
  LIMIT 1
);

SET @create_properties_col = (
  SELECT m.column_name
  FROM tmp_create_col_matches m
  ORDER BY m.preferred_rank, CHAR_LENGTH(m.column_name), m.column_name
  LIMIT 1
);

SELECT 'Diagnostic: areatrigger create-properties column matches' AS note;
SELECT column_name, preferred_rank
FROM tmp_create_col_matches
ORDER BY preferred_rank, CHAR_LENGTH(column_name), column_name;

SELECT
  @areatrigger_exists AS areatrigger_table_exists,
  @spawn_pk_col AS detected_spawn_pk_column,
  @create_properties_col AS detected_create_properties_column,
  @map_col AS detected_map_column;

DROP TEMPORARY TABLE IF EXISTS tmp_create_property_ids;
CREATE TEMPORARY TABLE tmp_create_property_ids (
  id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

SET @w_acp_exists = (
  SELECT COUNT(*)
  FROM information_schema.tables
  WHERE table_schema = 'world'
    AND table_name = 'areatrigger_create_properties'
);
SET @w_acp_pk = (
  SELECT c.column_name
  FROM information_schema.columns c
  WHERE c.table_schema = 'world'
    AND c.table_name = 'areatrigger_create_properties'
    AND c.column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  ORDER BY FIELD(c.column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  LIMIT 1
);

SET @h_acp_exists = (
  SELECT COUNT(*)
  FROM information_schema.tables
  WHERE table_schema = 'hotfixes'
    AND table_name = 'areatrigger_create_properties'
);
SET @h_acp_pk = (
  SELECT c.column_name
  FROM information_schema.columns c
  WHERE c.table_schema = 'hotfixes'
    AND c.table_name = 'areatrigger_create_properties'
    AND c.column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  ORDER BY FIELD(c.column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  LIMIT 1
);

SET @w_acpt_exists = (
  SELECT COUNT(*)
  FROM information_schema.tables
  WHERE table_schema = 'world'
    AND table_name = 'areatrigger_create_properties_template'
);
SET @w_acpt_pk = (
  SELECT c.column_name
  FROM information_schema.columns c
  WHERE c.table_schema = 'world'
    AND c.table_name = 'areatrigger_create_properties_template'
    AND c.column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  ORDER BY FIELD(c.column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  LIMIT 1
);

SET @h_acpt_exists = (
  SELECT COUNT(*)
  FROM information_schema.tables
  WHERE table_schema = 'hotfixes'
    AND table_name = 'areatrigger_create_properties_template'
);
SET @h_acpt_pk = (
  SELECT c.column_name
  FROM information_schema.columns c
  WHERE c.table_schema = 'hotfixes'
    AND c.table_name = 'areatrigger_create_properties_template'
    AND c.column_name IN ('ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  ORDER BY FIELD(c.column_name, 'ID', 'Id', 'id', 'CreatePropertiesId', 'createPropertiesId')
  LIMIT 1
);

SELECT
  @w_acp_exists AS world_areatrigger_create_properties_exists,
  @w_acp_pk AS world_areatrigger_create_properties_pk,
  @h_acp_exists AS hotfixes_areatrigger_create_properties_exists,
  @h_acp_pk AS hotfixes_areatrigger_create_properties_pk,
  @w_acpt_exists AS world_areatrigger_create_properties_template_exists,
  @w_acpt_pk AS world_areatrigger_create_properties_template_pk,
  @h_acpt_exists AS hotfixes_areatrigger_create_properties_template_exists,
  @h_acpt_pk AS hotfixes_areatrigger_create_properties_template_pk;

SET @sql_pop_w_acp = IF(
  @w_acp_exists = 1 AND @w_acp_pk IS NOT NULL,
  CONCAT(
    'INSERT IGNORE INTO tmp_create_property_ids (id) ',
    'SELECT CAST(`', REPLACE(@w_acp_pk, '`', '``'), '` AS UNSIGNED) ',
    'FROM world.areatrigger_create_properties ',
    'WHERE CAST(`', REPLACE(@w_acp_pk, '`', '``'), '` AS UNSIGNED) > 0'
  ),
  'SELECT ''SKIP: world.areatrigger_create_properties unavailable or missing PK'' AS note'
);
PREPARE stmt_pop_w_acp FROM @sql_pop_w_acp;
EXECUTE stmt_pop_w_acp;
DEALLOCATE PREPARE stmt_pop_w_acp;

SET @sql_pop_h_acp = IF(
  @h_acp_exists = 1 AND @h_acp_pk IS NOT NULL,
  CONCAT(
    'INSERT IGNORE INTO tmp_create_property_ids (id) ',
    'SELECT CAST(`', REPLACE(@h_acp_pk, '`', '``'), '` AS UNSIGNED) ',
    'FROM hotfixes.areatrigger_create_properties ',
    'WHERE CAST(`', REPLACE(@h_acp_pk, '`', '``'), '` AS UNSIGNED) > 0'
  ),
  'SELECT ''SKIP: hotfixes.areatrigger_create_properties unavailable or missing PK'' AS note'
);
PREPARE stmt_pop_h_acp FROM @sql_pop_h_acp;
EXECUTE stmt_pop_h_acp;
DEALLOCATE PREPARE stmt_pop_h_acp;

SET @sql_pop_w_acpt = IF(
  @w_acpt_exists = 1 AND @w_acpt_pk IS NOT NULL,
  CONCAT(
    'INSERT IGNORE INTO tmp_create_property_ids (id) ',
    'SELECT CAST(`', REPLACE(@w_acpt_pk, '`', '``'), '` AS UNSIGNED) ',
    'FROM world.areatrigger_create_properties_template ',
    'WHERE CAST(`', REPLACE(@w_acpt_pk, '`', '``'), '` AS UNSIGNED) > 0'
  ),
  'SELECT ''SKIP: world.areatrigger_create_properties_template unavailable or missing PK'' AS note'
);
PREPARE stmt_pop_w_acpt FROM @sql_pop_w_acpt;
EXECUTE stmt_pop_w_acpt;
DEALLOCATE PREPARE stmt_pop_w_acpt;

SET @sql_pop_h_acpt = IF(
  @h_acpt_exists = 1 AND @h_acpt_pk IS NOT NULL,
  CONCAT(
    'INSERT IGNORE INTO tmp_create_property_ids (id) ',
    'SELECT CAST(`', REPLACE(@h_acpt_pk, '`', '``'), '` AS UNSIGNED) ',
    'FROM hotfixes.areatrigger_create_properties_template ',
    'WHERE CAST(`', REPLACE(@h_acpt_pk, '`', '``'), '` AS UNSIGNED) > 0'
  ),
  'SELECT ''SKIP: hotfixes.areatrigger_create_properties_template unavailable or missing PK'' AS note'
);
PREPARE stmt_pop_h_acpt FROM @sql_pop_h_acpt;
EXECUTE stmt_pop_h_acpt;
DEALLOCATE PREPARE stmt_pop_h_acpt;

SELECT COUNT(*) INTO @valid_property_ids_loaded
FROM tmp_create_property_ids;

DROP TEMPORARY TABLE IF EXISTS tmp_invalid_spawns;
CREATE TEMPORARY TABLE tmp_invalid_spawns (
  spawn_pk BIGINT UNSIGNED NOT NULL,
  create_property_id BIGINT UNSIGNED NOT NULL,
  map_id BIGINT NULL,
  PRIMARY KEY (spawn_pk)
) ENGINE=InnoDB;

SET @prereq_ok = IF(
  @areatrigger_exists = 1
  AND @spawn_pk_col IS NOT NULL
  AND @create_properties_col IS NOT NULL,
  1,
  0
);

SET @sql_build_invalid = IF(
  @prereq_ok = 1,
  CONCAT(
    'INSERT INTO tmp_invalid_spawns (spawn_pk, create_property_id, map_id) ',
    'SELECT ',
    'CAST(a.`', REPLACE(@spawn_pk_col, '`', '``'), '` AS UNSIGNED) AS spawn_pk, ',
    'CAST(a.`', REPLACE(@create_properties_col, '`', '``'), '` AS UNSIGNED) AS create_property_id, ',
    IF(
      @map_col IS NOT NULL,
      CONCAT('CAST(a.`', REPLACE(@map_col, '`', '``'), '` AS SIGNED) AS map_id '),
      'NULL AS map_id '
    ),
    'FROM world.areatrigger a ',
    'LEFT JOIN tmp_create_property_ids t ',
    'ON t.id = CAST(a.`', REPLACE(@create_properties_col, '`', '``'), '` AS UNSIGNED) ',
    'WHERE CAST(a.`', REPLACE(@create_properties_col, '`', '``'), '` AS UNSIGNED) > 0 ',
    'AND t.id IS NULL'
  ),
  'SELECT ''SKIP: required world.areatrigger table/columns not detected'' AS note'
);
PREPARE stmt_build_invalid FROM @sql_build_invalid;
EXECUTE stmt_build_invalid;
DEALLOCATE PREPARE stmt_build_invalid;

SELECT COUNT(*) INTO @invalid_before
FROM tmp_invalid_spawns;

SELECT
  @invalid_before AS invalid_before,
  @valid_property_ids_loaded AS valid_property_ids_loaded;

SELECT spawn_pk, create_property_id, map_id
FROM tmp_invalid_spawns
ORDER BY spawn_pk
LIMIT 50;

SET @sql_top_maps = IF(
  @map_col IS NOT NULL,
  'SELECT map_id, COUNT(*) AS invalid_count FROM tmp_invalid_spawns GROUP BY map_id ORDER BY invalid_count DESC, map_id ASC LIMIT 25',
  'SELECT ''SKIP: no map column detected on world.areatrigger'' AS note'
);
PREPARE stmt_top_maps FROM @sql_top_maps;
EXECUTE stmt_top_maps;
DEALLOCATE PREPARE stmt_top_maps;

SET @deleted_rows = 0;
SET @can_apply = IF(
  @APPLY_FIX = 1
  AND @prereq_ok = 1
  AND @invalid_before > 0
  AND (@invalid_before <= @MAX_DELETE OR @FORCE_DELETE = 1),
  1,
  0
);
SET @cap_note = CASE
  WHEN @APPLY_FIX <> 1 THEN 'SKIP: @APPLY_FIX is not 1'
  WHEN @prereq_ok <> 1 THEN 'SKIP: missing required world.areatrigger table/columns'
  WHEN @invalid_before = 0 THEN 'SKIP: no invalid rows found'
  WHEN @invalid_before > @MAX_DELETE AND @FORCE_DELETE = 0 THEN CONCAT('SKIP: invalid row count ', @invalid_before, ' exceeds @MAX_DELETE ', @MAX_DELETE, ' and @FORCE_DELETE=0')
  ELSE 'APPLY: deletion allowed'
END;

SELECT @cap_note AS apply_decision_note;

SET @sql_create_backup = IF(
  @can_apply = 1,
  'CREATE TABLE IF NOT EXISTS world.areatrigger_backup_genre7a LIKE world.areatrigger',
  'SELECT ''SKIP: backup table create not required'' AS note'
);
PREPARE stmt_create_backup FROM @sql_create_backup;
EXECUTE stmt_create_backup;
DEALLOCATE PREPARE stmt_create_backup;

SET @sql_backup_invalid = IF(
  @can_apply = 1,
  CONCAT(
    'INSERT IGNORE INTO world.areatrigger_backup_genre7a ',
    'SELECT a.* FROM world.areatrigger a ',
    'INNER JOIN tmp_invalid_spawns i ON i.spawn_pk = CAST(a.`', REPLACE(@spawn_pk_col, '`', '``'), '` AS UNSIGNED)'
  ),
  'SELECT ''SKIP: backup insert not required'' AS note'
);
PREPARE stmt_backup_invalid FROM @sql_backup_invalid;
EXECUTE stmt_backup_invalid;
DEALLOCATE PREPARE stmt_backup_invalid;

SET @sql_delete_invalid = IF(
  @can_apply = 1,
  CONCAT(
    'DELETE a FROM world.areatrigger a ',
    'INNER JOIN tmp_invalid_spawns i ON i.spawn_pk = CAST(a.`', REPLACE(@spawn_pk_col, '`', '``'), '` AS UNSIGNED)'
  ),
  'SELECT ''SKIP: delete not applied'' AS note'
);
PREPARE stmt_delete_invalid FROM @sql_delete_invalid;
EXECUTE stmt_delete_invalid;
DEALLOCATE PREPARE stmt_delete_invalid;

SET @deleted_rows = IF(@can_apply = 1, ROW_COUNT(), 0);

SET @invalid_after = @invalid_before;
SET @sql_recount_after = IF(
  @prereq_ok = 1,
  CONCAT(
    'SELECT COUNT(*) INTO @invalid_after ',
    'FROM world.areatrigger a ',
    'LEFT JOIN tmp_create_property_ids t ',
    'ON t.id = CAST(a.`', REPLACE(@create_properties_col, '`', '``'), '` AS UNSIGNED) ',
    'WHERE CAST(a.`', REPLACE(@create_properties_col, '`', '``'), '` AS UNSIGNED) > 0 ',
    'AND t.id IS NULL'
  ),
  'SELECT @invalid_after INTO @invalid_after'
);
PREPARE stmt_recount_after FROM @sql_recount_after;
EXECUTE stmt_recount_after;
DEALLOCATE PREPARE stmt_recount_after;

SELECT
  @invalid_before AS invalid_before,
  @deleted_rows AS deleted_rows,
  @invalid_after AS invalid_after,
  @cap_note AS cap_note;

COMMIT;

SET SESSION sql_safe_updates = @OLD_SQL_SAFE_UPDATES;
SET SESSION foreign_key_checks = @OLD_FOREIGN_KEY_CHECKS;
SET SESSION unique_checks = @OLD_UNIQUE_CHECKS;
SET SESSION autocommit = @OLD_AUTOCOMMIT;

SELECT
  @OLD_SQL_SAFE_UPDATES AS restored_sql_safe_updates,
  @OLD_FOREIGN_KEY_CHECKS AS restored_foreign_key_checks,
  @OLD_UNIQUE_CHECKS AS restored_unique_checks,
  @OLD_AUTOCOMMIT AS restored_autocommit;

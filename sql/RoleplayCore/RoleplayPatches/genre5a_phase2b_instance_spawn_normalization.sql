/* GENRE 5A (PHASE 2B): Instance-map spawn difficulty normalization */
USE `world`;
SELECT DATABASE() AS active_database;

SET @APPLY_FIX := 1;

SET @OLD_SQL_SAFE_UPDATES := @@SQL_SAFE_UPDATES;
SET @OLD_FOREIGN_KEY_CHECKS := @@FOREIGN_KEY_CHECKS;
SET @OLD_UNIQUE_CHECKS := @@UNIQUE_CHECKS;
SET @OLD_AUTOCOMMIT := @@AUTOCOMMIT;

SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;
SET AUTOCOMMIT = 0;
START TRANSACTION;

SET @md_schema := NULL;
SET @md_map_col := NULL;
SET @md_diff_col := NULL;
SET @has_md := 0;

SET @md_schema := (
  SELECT CASE
    WHEN EXISTS (
      SELECT 1 FROM INFORMATION_SCHEMA.TABLES
      WHERE TABLE_SCHEMA = 'world' AND TABLE_NAME = 'map_difficulty'
    ) THEN 'world'
    WHEN EXISTS (
      SELECT 1 FROM INFORMATION_SCHEMA.TABLES
      WHERE TABLE_SCHEMA = 'hotfixes' AND TABLE_NAME = 'map_difficulty'
    ) THEN 'hotfixes'
    ELSE NULL
  END
);

SET @has_md := IF(@md_schema IS NULL, 0, 1);

SELECT COLUMN_NAME INTO @md_map_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = @md_schema
  AND TABLE_NAME = 'map_difficulty'
  AND COLUMN_NAME IN ('MapID','MapId','mapID','mapId','map')
ORDER BY FIELD(COLUMN_NAME, 'MapID','MapId','mapID','mapId','map')
LIMIT 1;

SELECT COLUMN_NAME INTO @md_diff_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = @md_schema
  AND TABLE_NAME = 'map_difficulty'
  AND COLUMN_NAME IN ('DifficultyID','DifficultyId','difficulty','Difficulty')
ORDER BY FIELD(COLUMN_NAME, 'DifficultyID','DifficultyId','difficulty','Difficulty')
LIMIT 1;

SET @has_md := IF(@has_md = 1 AND @md_map_col IS NOT NULL AND @md_diff_col IS NOT NULL, 1, 0);

SELECT IF(@has_md = 1,
  CONCAT('OK: using ', @md_schema, '.map_difficulty with map=', @md_map_col, ', difficulty=', @md_diff_col),
  'SKIP: map_difficulty not available with required columns in world/hotfixes') AS note;

DROP TEMPORARY TABLE IF EXISTS tmp_allowed_diff;
CREATE TEMPORARY TABLE tmp_allowed_diff (
  mapId INT UNSIGNED NOT NULL,
  difficultyId INT UNSIGNED NOT NULL,
  PRIMARY KEY (mapId, difficultyId)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS tmp_allowed_min;
CREATE TEMPORARY TABLE tmp_allowed_min (
  mapId INT UNSIGNED NOT NULL,
  minDifficultyId INT UNSIGNED NOT NULL,
  PRIMARY KEY (mapId)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS tmp_allowed_mask;
CREATE TEMPORARY TABLE tmp_allowed_mask (
  mapId INT UNSIGNED NOT NULL,
  allowedMask BIGINT UNSIGNED NOT NULL,
  lowBit BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (mapId)
) ENGINE=InnoDB;

SET @sql := IF(@has_md = 1,
  CONCAT(
    'INSERT IGNORE INTO tmp_allowed_diff(mapId, difficultyId) ',
    'SELECT DISTINCT CAST(`', @md_map_col, '` AS UNSIGNED), CAST(`', @md_diff_col, '` AS UNSIGNED) ',
    'FROM `', @md_schema, '`.`map_difficulty` ',
    'WHERE `', @md_map_col, '` IS NOT NULL AND `', @md_diff_col, '` IS NOT NULL'
  ),
  'SELECT ''SKIP: tmp_allowed_diff population skipped (map_difficulty unavailable)'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

INSERT INTO tmp_allowed_min(mapId, minDifficultyId)
SELECT mapId, MIN(difficultyId)
FROM tmp_allowed_diff
GROUP BY mapId;

INSERT INTO tmp_allowed_mask(mapId, allowedMask, lowBit)
SELECT
  d.mapId,
  CAST(BIT_OR((CAST(1 AS UNSIGNED) << d.difficultyId)) AS UNSIGNED) AS allowedMask,
  CAST(BIT_OR((CAST(1 AS UNSIGNED) << d.difficultyId)) AS UNSIGNED) & (~CAST(BIT_OR((CAST(1 AS UNSIGNED) << d.difficultyId)) AS UNSIGNED) + 1) AS lowBit
FROM tmp_allowed_diff d
GROUP BY d.mapId
HAVING CAST(BIT_OR((CAST(1 AS UNSIGNED) << d.difficultyId)) AS UNSIGNED) <> 0;

SELECT COUNT(*) AS instance_maps_loaded FROM tmp_allowed_diff;

SET @creature_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature'
);
SET @creature_map_col := NULL;
SET @creature_guid_col := NULL;
SET @creature_spawn_col := NULL;
SET @creature_mode := NULL;
SET @creature_updated := 0;

SELECT COLUMN_NAME INTO @creature_map_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'creature'
  AND COLUMN_NAME IN ('map','Map','mapId','MapId')
ORDER BY FIELD(COLUMN_NAME, 'map','Map','mapId','MapId')
LIMIT 1;

SELECT COLUMN_NAME INTO @creature_guid_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'creature'
  AND COLUMN_NAME IN ('guid','GUID')
ORDER BY FIELD(COLUMN_NAME, 'guid','GUID')
LIMIT 1;

SELECT COLUMN_NAME INTO @creature_spawn_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'creature'
  AND COLUMN_NAME IN ('spawnDifficulties','SpawnDifficulties','spawn_difficulties','spawnMask','SpawnMask')
ORDER BY FIELD(COLUMN_NAME, 'spawnDifficulties','SpawnDifficulties','spawn_difficulties','spawnMask','SpawnMask')
LIMIT 1;

SET @creature_mode := CASE
  WHEN @creature_spawn_col IN ('spawnMask','SpawnMask') THEN 'mask'
  WHEN @creature_spawn_col IS NOT NULL THEN 'list'
  ELSE NULL
END;

SELECT IF(@creature_exists = 0, 'SKIP: creature table missing',
       IF(@creature_map_col IS NULL OR @creature_guid_col IS NULL OR @creature_spawn_col IS NULL,
         'SKIP: creature missing required map/guid/spawn column',
         CONCAT('OK: creature columns map=', @creature_map_col, ', guid=', @creature_guid_col, ', spawn=', @creature_spawn_col, ', mode=', @creature_mode)
       )) AS note;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode IS NOT NULL,
  IF(@creature_mode = 'mask',
    CONCAT(
      'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default_rows ',
      'FROM `creature` c JOIN tmp_allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` <> 1 ',
      'GROUP BY CAST(c.`', @creature_map_col, '` AS UNSIGNED) ORDER BY non_default_rows DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default_rows ',
      'FROM `creature` c JOIN tmp_allowed_diff ad ON ad.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'') ',
      'GROUP BY CAST(c.`', @creature_map_col, '` AS UNSIGNED) ORDER BY non_default_rows DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: creature non-default diagnostics unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode IS NOT NULL,
  IF(@creature_mode = 'mask',
    CONCAT(
      'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS invalid_rows ',
      'FROM `creature` c JOIN tmp_allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0) ',
      'GROUP BY CAST(c.`', @creature_map_col, '` AS UNSIGNED) ORDER BY invalid_rows DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT src.mapId, COUNT(*) AS invalid_rows FROM (',
      'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, c.`', @creature_spawn_col, '` AS val, ',
      'MAX(CASE WHEN ad.difficultyId IS NULL THEN 1 ELSE 0 END) AS has_bad, ',
      'SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) AS good_cnt ',
      'FROM `creature` c ',
      'JOIN tmp_allowed_min mn ON mn.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(c.`', @creature_spawn_col, '`, ''''), '' '', ''''), '','', ''","''), ''"]''), ''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
      'LEFT JOIN tmp_allowed_diff ad ON ad.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
      'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'') AND jt.tok REGEXP ''^[0-9]+$'' ',
      'GROUP BY CAST(c.`', @creature_map_col, '` AS UNSIGNED), c.`', @creature_spawn_col, '` ',
      ') src WHERE src.has_bad = 1 OR src.good_cnt = 0 GROUP BY src.mapId ORDER BY invalid_rows DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: creature invalid diagnostics unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

CREATE TABLE IF NOT EXISTS creature_backup_genre5a_phase2b LIKE creature;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'mask',
  CONCAT(
    'INSERT IGNORE INTO creature_backup_genre5a_phase2b SELECT c.* FROM creature c ',
    'JOIN tmp_allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
    'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: creature mask backup not required'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'mask' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE creature c ',
    'JOIN tmp_allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
    'SET c.`', @creature_spawn_col, '` = IF((c.`', @creature_spawn_col, '` & am.allowedMask) = 0, am.lowBit, (c.`', @creature_spawn_col, '` & am.allowedMask)) ',
    'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: creature mask update skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
SET @creature_updated := ROW_COUNT();
DEALLOCATE PREPARE stmt;

DROP TEMPORARY TABLE IF EXISTS tmp_creature_distinct;
CREATE TEMPORARY TABLE tmp_creature_distinct (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS tmp_creature_norm;
CREATE TEMPORARY TABLE tmp_creature_norm (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  newVal VARCHAR(255) NOT NULL,
  has_bad TINYINT(1) NOT NULL,
  good_cnt INT NOT NULL,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO tmp_creature_distinct(mapId, oldVal) ',
    'SELECT DISTINCT CAST(c.`', @creature_map_col, '` AS UNSIGNED), c.`', @creature_spawn_col, '` ',
    'FROM creature c JOIN tmp_allowed_min mn ON mn.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
    'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'')'
  ),
  'SELECT ''SKIP: creature list distinct build skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list',
  'INSERT INTO tmp_creature_norm(mapId, oldVal, newVal, has_bad, good_cnt) '
  'SELECT d.mapId, d.oldVal, '
  'COALESCE(NULLIF(GROUP_CONCAT(DISTINCT CASE WHEN ad.difficultyId IS NOT NULL THEN CAST(ad.difficultyId AS CHAR) END ORDER BY ad.difficultyId SEPARATOR '',''), ''''), CAST(mn.minDifficultyId AS CHAR)) AS newVal, '
  'MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END) AS has_bad, '
  'SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) AS good_cnt '
  'FROM tmp_creature_distinct d '
  'JOIN tmp_allowed_min mn ON mn.mapId = d.mapId '
  'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(d.oldVal, ''''), '' '', ''''), '','', ''","''), ''"]''), ''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt '
  'LEFT JOIN tmp_allowed_diff ad ON ad.mapId = d.mapId AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) '
  'GROUP BY d.mapId, d.oldVal, mn.minDifficultyId',
  'SELECT ''SKIP: creature list norm build skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO creature_backup_genre5a_phase2b SELECT c.* FROM creature c ',
    'JOIN tmp_creature_norm n ON n.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) AND CAST(n.oldVal AS BINARY(255)) = CAST(c.`', @creature_spawn_col, '` AS BINARY(255)) ',
    'WHERE (n.has_bad = 1 OR n.good_cnt = 0) AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(c.`', @creature_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: creature list backup skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE creature c ',
    'JOIN tmp_creature_norm n ON n.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) AND CAST(n.oldVal AS BINARY(255)) = CAST(c.`', @creature_spawn_col, '` AS BINARY(255)) ',
    'SET c.`', @creature_spawn_col, '` = n.newVal ',
    'WHERE (n.has_bad = 1 OR n.good_cnt = 0) AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(c.`', @creature_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: creature list update skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
SET @creature_updated := IF(@creature_mode = 'list', ROW_COUNT(), @creature_updated);
DEALLOCATE PREPARE stmt;

SET @go_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'gameobject'
);
SET @go_map_col := NULL;
SET @go_guid_col := NULL;
SET @go_spawn_col := NULL;
SET @go_mode := NULL;
SET @go_updated := 0;

SELECT COLUMN_NAME INTO @go_map_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'gameobject'
  AND COLUMN_NAME IN ('map','Map','mapId','MapId')
ORDER BY FIELD(COLUMN_NAME, 'map','Map','mapId','MapId')
LIMIT 1;

SELECT COLUMN_NAME INTO @go_guid_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'gameobject'
  AND COLUMN_NAME IN ('guid','GUID')
ORDER BY FIELD(COLUMN_NAME, 'guid','GUID')
LIMIT 1;

SELECT COLUMN_NAME INTO @go_spawn_col
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'gameobject'
  AND COLUMN_NAME IN ('spawnDifficulties','SpawnDifficulties','spawn_difficulties','spawnMask','SpawnMask')
ORDER BY FIELD(COLUMN_NAME, 'spawnDifficulties','SpawnDifficulties','spawn_difficulties','spawnMask','SpawnMask')
LIMIT 1;

SET @go_mode := CASE
  WHEN @go_spawn_col IN ('spawnMask','SpawnMask') THEN 'mask'
  WHEN @go_spawn_col IS NOT NULL THEN 'list'
  ELSE NULL
END;

SELECT IF(@go_exists = 0, 'SKIP: gameobject table missing',
       IF(@go_map_col IS NULL OR @go_guid_col IS NULL OR @go_spawn_col IS NULL,
         'SKIP: gameobject missing required map/guid/spawn column',
         CONCAT('OK: gameobject columns map=', @go_map_col, ', guid=', @go_guid_col, ', spawn=', @go_spawn_col, ', mode=', @go_mode)
       )) AS note;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode IS NOT NULL,
  IF(@go_mode = 'mask',
    CONCAT(
      'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default_rows ',
      'FROM `gameobject` g JOIN tmp_allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` <> 1 ',
      'GROUP BY CAST(g.`', @go_map_col, '` AS UNSIGNED) ORDER BY non_default_rows DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default_rows ',
      'FROM `gameobject` g JOIN tmp_allowed_diff ad ON ad.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` NOT IN ('''',''0'') ',
      'GROUP BY CAST(g.`', @go_map_col, '` AS UNSIGNED) ORDER BY non_default_rows DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: gameobject non-default diagnostics unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode IS NOT NULL,
  IF(@go_mode = 'mask',
    CONCAT(
      'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS invalid_rows ',
      'FROM `gameobject` g JOIN tmp_allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0) ',
      'GROUP BY CAST(g.`', @go_map_col, '` AS UNSIGNED) ORDER BY invalid_rows DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT src.mapId, COUNT(*) AS invalid_rows FROM (',
      'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, g.`', @go_spawn_col, '` AS val, ',
      'MAX(CASE WHEN ad.difficultyId IS NULL THEN 1 ELSE 0 END) AS has_bad, ',
      'SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) AS good_cnt ',
      'FROM `gameobject` g ',
      'JOIN tmp_allowed_min mn ON mn.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(g.`', @go_spawn_col, '`, ''''), '' '', ''''), '','', ''","''), ''"]''), ''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
      'LEFT JOIN tmp_allowed_diff ad ON ad.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
      'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` NOT IN ('''',''0'') AND jt.tok REGEXP ''^[0-9]+$'' ',
      'GROUP BY CAST(g.`', @go_map_col, '` AS UNSIGNED), g.`', @go_spawn_col, '` ',
      ') src WHERE src.has_bad = 1 OR src.good_cnt = 0 GROUP BY src.mapId ORDER BY invalid_rows DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: gameobject invalid diagnostics unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

CREATE TABLE IF NOT EXISTS gameobject_backup_genre5a_phase2b LIKE gameobject;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'mask',
  CONCAT(
    'INSERT IGNORE INTO gameobject_backup_genre5a_phase2b SELECT g.* FROM gameobject g ',
    'JOIN tmp_allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
    'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: gameobject mask backup not required'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'mask' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE gameobject g ',
    'JOIN tmp_allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
    'SET g.`', @go_spawn_col, '` = IF((g.`', @go_spawn_col, '` & am.allowedMask) = 0, am.lowBit, (g.`', @go_spawn_col, '` & am.allowedMask)) ',
    'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: gameobject mask update skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
SET @go_updated := ROW_COUNT();
DEALLOCATE PREPARE stmt;

DROP TEMPORARY TABLE IF EXISTS tmp_gameobject_distinct;
CREATE TEMPORARY TABLE tmp_gameobject_distinct (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS tmp_gameobject_norm;
CREATE TEMPORARY TABLE tmp_gameobject_norm (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  newVal VARCHAR(255) NOT NULL,
  has_bad TINYINT(1) NOT NULL,
  good_cnt INT NOT NULL,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO tmp_gameobject_distinct(mapId, oldVal) ',
    'SELECT DISTINCT CAST(g.`', @go_map_col, '` AS UNSIGNED), g.`', @go_spawn_col, '` ',
    'FROM gameobject g JOIN tmp_allowed_min mn ON mn.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
    'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` NOT IN ('''',''0'')'
  ),
  'SELECT ''SKIP: gameobject list distinct build skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list',
  'INSERT INTO tmp_gameobject_norm(mapId, oldVal, newVal, has_bad, good_cnt) '
  'SELECT d.mapId, d.oldVal, '
  'COALESCE(NULLIF(GROUP_CONCAT(DISTINCT CASE WHEN ad.difficultyId IS NOT NULL THEN CAST(ad.difficultyId AS CHAR) END ORDER BY ad.difficultyId SEPARATOR '',''), ''''), CAST(mn.minDifficultyId AS CHAR)) AS newVal, '
  'MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END) AS has_bad, '
  'SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) AS good_cnt '
  'FROM tmp_gameobject_distinct d '
  'JOIN tmp_allowed_min mn ON mn.mapId = d.mapId '
  'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(d.oldVal, ''''), '' '', ''''), '','', ''","''), ''"]''), ''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt '
  'LEFT JOIN tmp_allowed_diff ad ON ad.mapId = d.mapId AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) '
  'GROUP BY d.mapId, d.oldVal, mn.minDifficultyId',
  'SELECT ''SKIP: gameobject list norm build skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO gameobject_backup_genre5a_phase2b SELECT g.* FROM gameobject g ',
    'JOIN tmp_gameobject_norm n ON n.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) AND CAST(n.oldVal AS BINARY(255)) = CAST(g.`', @go_spawn_col, '` AS BINARY(255)) ',
    'WHERE (n.has_bad = 1 OR n.good_cnt = 0) AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(g.`', @go_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: gameobject list backup skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE gameobject g ',
    'JOIN tmp_gameobject_norm n ON n.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) AND CAST(n.oldVal AS BINARY(255)) = CAST(g.`', @go_spawn_col, '` AS BINARY(255)) ',
    'SET g.`', @go_spawn_col, '` = n.newVal ',
    'WHERE (n.has_bad = 1 OR n.good_cnt = 0) AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(g.`', @go_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: gameobject list update skipped'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
SET @go_updated := IF(@go_mode = 'list', ROW_COUNT(), @go_updated);
DEALLOCATE PREPARE stmt;

SET @creature_remaining_invalid := NULL;
SET @go_remaining_invalid := NULL;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode IS NOT NULL,
  IF(@creature_mode = 'mask',
    CONCAT(
      'SELECT COUNT(*) INTO @creature_remaining_invalid FROM creature c ',
      'JOIN tmp_allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0)'
    ),
    CONCAT(
      'SELECT COUNT(*) INTO @creature_remaining_invalid FROM (',
      'SELECT c.`', @creature_guid_col, '` FROM creature c ',
      'JOIN tmp_allowed_min mn ON mn.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(c.`', @creature_spawn_col, '`, ''''), '' '', ''''), '','', ''","''), ''"]''), ''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
      'LEFT JOIN tmp_allowed_diff ad ON ad.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
      'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'') ',
      'GROUP BY c.`', @creature_guid_col, '` HAVING MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END)=1 ',
      'OR SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END)=0',
      ') x'
    )
  ),
  'SELECT NULL INTO @creature_remaining_invalid'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode IS NOT NULL,
  IF(@go_mode = 'mask',
    CONCAT(
      'SELECT COUNT(*) INTO @go_remaining_invalid FROM gameobject g ',
      'JOIN tmp_allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0)'
    ),
    CONCAT(
      'SELECT COUNT(*) INTO @go_remaining_invalid FROM (',
      'SELECT g.`', @go_guid_col, '` FROM gameobject g ',
      'JOIN tmp_allowed_min mn ON mn.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(g.`', @go_spawn_col, '`, ''''), '' '', ''''), '','', ''","''), ''"]''), ''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
      'LEFT JOIN tmp_allowed_diff ad ON ad.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
      'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` NOT IN ('''',''0'') ',
      'GROUP BY g.`', @go_guid_col, '` HAVING MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END)=1 ',
      'OR SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END)=0',
      ') x'
    )
  ),
  'SELECT NULL INTO @go_remaining_invalid'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SELECT
  @APPLY_FIX AS apply_fix,
  @creature_updated AS creature_rows_updated,
  @go_updated AS gameobject_rows_updated,
  @creature_remaining_invalid AS creature_remaining_invalid,
  @go_remaining_invalid AS gameobject_remaining_invalid;

COMMIT;
SET SQL_SAFE_UPDATES = @OLD_SQL_SAFE_UPDATES;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS;
SET AUTOCOMMIT = @OLD_AUTOCOMMIT;

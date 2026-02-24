/* ================================================================== */
/* GENRE 5A Phase 2B v2 — Instance-map spawn difficulty normalization */
/* TrinityCore Midnight 12.x (TWW 11.1.7)                            */
/*                                                                    */
/* Normalizes creature/gameobject spawnDifficulties (list mode) or    */
/* spawnMask (bitmask mode) against map_difficulty to remove invalid  */
/* difficulty references for instance maps.                           */
/*                                                                    */
/* v2 fixes:                                                          */
/*   - Removed two embedded GitHub review comments                    */
/*   - DDL (backup table creation) moved BEFORE START TRANSACTION     */
/*   - COALESCE on session save/restore (NULL-proof)                  */
/*   - Non-numeric tokens in list mode now detected and flagged       */
/*     (e.g. '1,foo' was previously missed)                           */
/*   - Self-contained — safe to run standalone in HeidiSQL            */
/*                                                                    */
/* SET @APPLY_FIX := 0 for dry-run diagnostics only.                  */
/* SET @APPLY_FIX := 1 to apply mutations.                            */
/* ================================================================== */

USE `world`;
SELECT DATABASE() AS active_database;

SET @APPLY_FIX := 1;

/* ── Session snapshot ────────────────────────────────────────────── */
SET @OLD_SQL_SAFE_UPDATES   := COALESCE(@@SQL_SAFE_UPDATES, 1);
SET @OLD_FOREIGN_KEY_CHECKS := COALESCE(@@FOREIGN_KEY_CHECKS, 1);
SET @OLD_UNIQUE_CHECKS      := COALESCE(@@UNIQUE_CHECKS, 1);
SET @OLD_AUTOCOMMIT         := COALESCE(@@AUTOCOMMIT, 1);
SET @OLD_GC_MAX_LEN         := @@SESSION.group_concat_max_len;

SET SQL_SAFE_UPDATES             = 0;
SET FOREIGN_KEY_CHECKS           = 0;
SET UNIQUE_CHECKS                = 0;
SET AUTOCOMMIT                   = 0;
SET SESSION group_concat_max_len = 1000000;

/* ── Counters ────────────────────────────────────────────────────── */
SET @creature_updated := 0;
SET @go_updated       := 0;

/* ================================================================== */
/* MAP_DIFFICULTY DETECTION                                           */
/* ================================================================== */

SET @md_schema := (
  SELECT CASE
    WHEN EXISTS (SELECT 1 FROM information_schema.tables
                 WHERE table_schema = 'world' AND table_name = 'map_difficulty')
      THEN 'world'
    WHEN EXISTS (SELECT 1 FROM information_schema.tables
                 WHERE table_schema = 'hotfixes' AND table_name = 'map_difficulty')
      THEN 'hotfixes'
    ELSE NULL
  END
);
SET @has_md := IF(@md_schema IS NULL, 0, 1);

SELECT column_name INTO @md_map_col
FROM information_schema.columns
WHERE table_schema = @md_schema AND table_name = 'map_difficulty'
  AND column_name IN ('MapID','MapId','mapID','mapId','map')
ORDER BY FIELD(column_name,'MapID','MapId','mapID','mapId','map') LIMIT 1;

SELECT column_name INTO @md_diff_col
FROM information_schema.columns
WHERE table_schema = @md_schema AND table_name = 'map_difficulty'
  AND column_name IN ('DifficultyID','DifficultyId','difficulty','Difficulty')
ORDER BY FIELD(column_name,'DifficultyID','DifficultyId','difficulty','Difficulty') LIMIT 1;

SET @has_md := IF(@has_md = 1 AND @md_map_col IS NOT NULL AND @md_diff_col IS NOT NULL, 1, 0);

SELECT IF(@has_md = 1,
  CONCAT('OK: using ', @md_schema, '.map_difficulty (',
         @md_map_col, ', ', @md_diff_col, ')'),
  'SKIP: map_difficulty not available') AS map_difficulty_status;

/* ================================================================== */
/* TEMPORARY TABLES — allowed difficulties per map                    */
/* ================================================================== */

DROP TEMPORARY TABLE IF EXISTS _allowed_diff;
CREATE TEMPORARY TABLE _allowed_diff (
  mapId INT UNSIGNED NOT NULL,
  difficultyId INT UNSIGNED NOT NULL,
  PRIMARY KEY (mapId, difficultyId)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS _allowed_min;
CREATE TEMPORARY TABLE _allowed_min (
  mapId INT UNSIGNED NOT NULL,
  minDifficultyId INT UNSIGNED NOT NULL,
  PRIMARY KEY (mapId)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS _allowed_mask;
CREATE TEMPORARY TABLE _allowed_mask (
  mapId INT UNSIGNED NOT NULL,
  allowedMask BIGINT UNSIGNED NOT NULL,
  lowBit BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (mapId)
) ENGINE=InnoDB;

SET @sql := IF(@has_md = 1,
  CONCAT(
    'INSERT IGNORE INTO _allowed_diff(mapId, difficultyId) ',
    'SELECT DISTINCT CAST(`', @md_map_col, '` AS UNSIGNED), ',
    'CAST(`', @md_diff_col, '` AS UNSIGNED) ',
    'FROM `', @md_schema, '`.`map_difficulty` ',
    'WHERE `', @md_map_col, '` IS NOT NULL AND `', @md_diff_col, '` IS NOT NULL'
  ),
  'SELECT ''SKIP: _allowed_diff population skipped'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

INSERT INTO _allowed_min(mapId, minDifficultyId)
SELECT mapId, MIN(difficultyId) FROM _allowed_diff GROUP BY mapId;

INSERT INTO _allowed_mask(mapId, allowedMask, lowBit)
SELECT
  d.mapId,
  CAST(BIT_OR(CAST(1 AS UNSIGNED) << d.difficultyId) AS UNSIGNED),
  CAST(BIT_OR(CAST(1 AS UNSIGNED) << d.difficultyId) AS UNSIGNED)
    & (~CAST(BIT_OR(CAST(1 AS UNSIGNED) << d.difficultyId) AS UNSIGNED) + 1)
FROM _allowed_diff d
GROUP BY d.mapId
HAVING CAST(BIT_OR(CAST(1 AS UNSIGNED) << d.difficultyId) AS UNSIGNED) <> 0;

SELECT COUNT(*) AS instance_maps_loaded FROM _allowed_diff;

/* ================================================================== */
/* CREATURE SCHEMA DETECTION                                          */
/* ================================================================== */

SET @creature_exists := (
  SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = DATABASE() AND table_name = 'creature'
);

SELECT column_name INTO @creature_map_col
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'creature'
  AND column_name IN ('map','Map','mapId','MapId')
ORDER BY FIELD(column_name,'map','Map','mapId','MapId') LIMIT 1;

SELECT column_name INTO @creature_guid_col
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'creature'
  AND column_name IN ('guid','GUID')
ORDER BY FIELD(column_name,'guid','GUID') LIMIT 1;

SELECT column_name INTO @creature_spawn_col
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'creature'
  AND column_name IN ('spawnDifficulties','SpawnDifficulties','spawn_difficulties',
                      'spawnMask','SpawnMask')
ORDER BY FIELD(column_name,'spawnDifficulties','SpawnDifficulties','spawn_difficulties',
               'spawnMask','SpawnMask') LIMIT 1;

SET @creature_mode := CASE
  WHEN @creature_spawn_col IN ('spawnMask','SpawnMask') THEN 'mask'
  WHEN @creature_spawn_col IS NOT NULL THEN 'list'
  ELSE NULL
END;

SELECT IF(@creature_exists = 0, 'SKIP: creature table missing',
  IF(@creature_map_col IS NULL OR @creature_guid_col IS NULL OR @creature_spawn_col IS NULL,
    'SKIP: creature missing map/guid/spawn column',
    CONCAT('OK: creature mode=', @creature_mode,
           ' (', @creature_map_col, ', ', @creature_guid_col, ', ', @creature_spawn_col, ')')
  )) AS creature_status;

/* ================================================================== */
/* GAMEOBJECT SCHEMA DETECTION                                        */
/* ================================================================== */

SET @go_exists := (
  SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = DATABASE() AND table_name = 'gameobject'
);

SELECT column_name INTO @go_map_col
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'gameobject'
  AND column_name IN ('map','Map','mapId','MapId')
ORDER BY FIELD(column_name,'map','Map','mapId','MapId') LIMIT 1;

SELECT column_name INTO @go_guid_col
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'gameobject'
  AND column_name IN ('guid','GUID')
ORDER BY FIELD(column_name,'guid','GUID') LIMIT 1;

SELECT column_name INTO @go_spawn_col
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'gameobject'
  AND column_name IN ('spawnDifficulties','SpawnDifficulties','spawn_difficulties',
                      'spawnMask','SpawnMask')
ORDER BY FIELD(column_name,'spawnDifficulties','SpawnDifficulties','spawn_difficulties',
               'spawnMask','SpawnMask') LIMIT 1;

SET @go_mode := CASE
  WHEN @go_spawn_col IN ('spawnMask','SpawnMask') THEN 'mask'
  WHEN @go_spawn_col IS NOT NULL THEN 'list'
  ELSE NULL
END;

SELECT IF(@go_exists = 0, 'SKIP: gameobject table missing',
  IF(@go_map_col IS NULL OR @go_guid_col IS NULL OR @go_spawn_col IS NULL,
    'SKIP: gameobject missing map/guid/spawn column',
    CONCAT('OK: gameobject mode=', @go_mode,
           ' (', @go_map_col, ', ', @go_guid_col, ', ', @go_spawn_col, ')')
  )) AS gameobject_status;

/* ================================================================== */
/* BACKUP TABLES — before transaction (DDL causes implicit commit)    */
/* ================================================================== */

CREATE TABLE IF NOT EXISTS `creature_backup_genre5a_phase2b` LIKE `creature`;
CREATE TABLE IF NOT EXISTS `gameobject_backup_genre5a_phase2b` LIKE `gameobject`;

/* ================================================================== */
/* DIAGNOSTICS — non-default and invalid spawn rows                   */
/* ================================================================== */
SELECT 'DIAGNOSTICS' AS section;

/* ── creature non-default ────────────────────────────────────────── */
SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode IS NOT NULL,
  IF(@creature_mode = 'mask',
    CONCAT(
      'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default ',
      'FROM `creature` c JOIN _allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` <> 1 ',
      'GROUP BY 1 ORDER BY 2 DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default ',
      'FROM `creature` c JOIN _allowed_diff ad ON ad.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'') ',
      'GROUP BY 1 ORDER BY 2 DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: creature non-default diagnostics'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── creature invalid ────────────────────────────────────────────── */
SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode IS NOT NULL,
  IF(@creature_mode = 'mask',
    CONCAT(
      'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS invalid ',
      'FROM `creature` c JOIN _allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 ',
      'OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0) ',
      'GROUP BY 1 ORDER BY 2 DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT src.mapId, COUNT(*) AS invalid FROM (',
        'SELECT CAST(c.`', @creature_map_col, '` AS UNSIGNED) AS mapId, ',
        'c.`', @creature_spawn_col, '` AS val, ',
        'MAX(CASE WHEN ad.difficultyId IS NULL THEN 1 ELSE 0 END) AS has_bad, ',
        'MAX(CASE WHEN NOT (jt.tok REGEXP ''^[0-9]+$'') THEN 1 ELSE 0 END) AS has_nonnumeric, ',
        'SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) AS good_cnt ',
        'FROM `creature` c ',
        'JOIN _allowed_min mn ON mn.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
        'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(c.`', @creature_spawn_col, '`,''''),'' '',''''),'','',''","''),''"]''), ',
        '''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
        'LEFT JOIN _allowed_diff ad ON ad.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
        'AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
        'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'') ',
        'GROUP BY CAST(c.`', @creature_map_col, '` AS UNSIGNED), c.`', @creature_spawn_col, '`',
      ') src WHERE src.has_bad = 1 OR src.has_nonnumeric = 1 OR src.good_cnt = 0 ',
      'GROUP BY src.mapId ORDER BY invalid DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: creature invalid diagnostics'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── gameobject non-default ──────────────────────────────────────── */
SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode IS NOT NULL,
  IF(@go_mode = 'mask',
    CONCAT(
      'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default ',
      'FROM `gameobject` g JOIN _allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` <> 1 ',
      'GROUP BY 1 ORDER BY 2 DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS non_default ',
      'FROM `gameobject` g JOIN _allowed_diff ad ON ad.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` NOT IN ('''',''0'') ',
      'GROUP BY 1 ORDER BY 2 DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: gameobject non-default diagnostics'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── gameobject invalid ──────────────────────────────────────────── */
SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode IS NOT NULL,
  IF(@go_mode = 'mask',
    CONCAT(
      'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, COUNT(*) AS invalid ',
      'FROM `gameobject` g JOIN _allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 ',
      'OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0) ',
      'GROUP BY 1 ORDER BY 2 DESC LIMIT 25'
    ),
    CONCAT(
      'SELECT src.mapId, COUNT(*) AS invalid FROM (',
        'SELECT CAST(g.`', @go_map_col, '` AS UNSIGNED) AS mapId, ',
        'g.`', @go_spawn_col, '` AS val, ',
        'MAX(CASE WHEN ad.difficultyId IS NULL THEN 1 ELSE 0 END) AS has_bad, ',
        'MAX(CASE WHEN NOT (jt.tok REGEXP ''^[0-9]+$'') THEN 1 ELSE 0 END) AS has_nonnumeric, ',
        'SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) AS good_cnt ',
        'FROM `gameobject` g ',
        'JOIN _allowed_min mn ON mn.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
        'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(IFNULL(g.`', @go_spawn_col, '`,''''),'' '',''''),'','',''","''),''"]''), ',
        '''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
        'LEFT JOIN _allowed_diff ad ON ad.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
        'AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
        'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` NOT IN ('''',''0'') ',
        'GROUP BY CAST(g.`', @go_map_col, '` AS UNSIGNED), g.`', @go_spawn_col, '`',
      ') src WHERE src.has_bad = 1 OR src.has_nonnumeric = 1 OR src.good_cnt = 0 ',
      'GROUP BY src.mapId ORDER BY invalid DESC LIMIT 25'
    )
  ),
  'SELECT ''SKIP: gameobject invalid diagnostics'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* MUTATIONS — inside transaction (no DDL)                            */
/* ================================================================== */
START TRANSACTION;

/* ================================================================== */
/* CREATURE — MASK MODE                                               */
/* ================================================================== */
SELECT 'CREATURE MASK MODE' AS section;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'mask',
  CONCAT(
    'INSERT IGNORE INTO `creature_backup_genre5a_phase2b` SELECT c.* FROM `creature` c ',
    'JOIN _allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
    'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 ',
    'OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: creature mask backup'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'mask' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE `creature` c ',
    'JOIN _allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
    'SET c.`', @creature_spawn_col, '` = IF(',
      '(c.`', @creature_spawn_col, '` & am.allowedMask) = 0, ',
      'am.lowBit, ',
      '(c.`', @creature_spawn_col, '` & am.allowedMask)) ',
    'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 ',
    'OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: creature mask update'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @creature_updated := ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* CREATURE — LIST MODE                                               */
/* ================================================================== */
SELECT 'CREATURE LIST MODE' AS section;

DROP TEMPORARY TABLE IF EXISTS _c_distinct;
CREATE TEMPORARY TABLE _c_distinct (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS _c_norm;
CREATE TEMPORARY TABLE _c_norm (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  newVal VARCHAR(255) NOT NULL,
  needs_fix TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO _c_distinct(mapId, oldVal) ',
    'SELECT DISTINCT CAST(c.`', @creature_map_col, '` AS UNSIGNED), c.`', @creature_spawn_col, '` ',
    'FROM `creature` c ',
    'JOIN _allowed_min mn ON mn.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
    'WHERE c.`', @creature_spawn_col, '` IS NOT NULL ',
    'AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'')'
  ),
  'SELECT ''SKIP: creature list distinct'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Build normalized values — FIX: also flag non-numeric tokens */
SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list',
  CONCAT(
    'INSERT INTO _c_norm(mapId, oldVal, newVal, needs_fix) ',
    'SELECT d.mapId, d.oldVal, ',
    'COALESCE(NULLIF(',
      'GROUP_CONCAT(DISTINCT CASE WHEN ad.difficultyId IS NOT NULL ',
        'THEN CAST(ad.difficultyId AS CHAR) END ',
        'ORDER BY ad.difficultyId SEPARATOR '',''), ''''), ',
      'CAST(mn.minDifficultyId AS CHAR)) AS newVal, ',
    'IF(MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END) = 1 ',
      'OR MAX(CASE WHEN NOT (jt.tok REGEXP ''^[0-9]+$'') THEN 1 ELSE 0 END) = 1 ',
      'OR SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) = 0, 1, 0) AS needs_fix ',
    'FROM _c_distinct d ',
    'JOIN _allowed_min mn ON mn.mapId = d.mapId ',
    'JOIN JSON_TABLE(',
      'CONCAT(''["'', REPLACE(REPLACE(IFNULL(d.oldVal,''''),'' '',''''),'','',''","''), ''"]''), ',
      '''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
    'LEFT JOIN _allowed_diff ad ON ad.mapId = d.mapId ',
      'AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
    'GROUP BY d.mapId, d.oldVal, mn.minDifficultyId'
  ),
  'SELECT ''SKIP: creature list norm'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Backup rows that will change */
SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO `creature_backup_genre5a_phase2b` SELECT c.* FROM `creature` c ',
    'JOIN _c_norm n ON n.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'AND CAST(n.oldVal AS BINARY(255)) = CAST(c.`', @creature_spawn_col, '` AS BINARY(255)) ',
    'WHERE n.needs_fix = 1 ',
    'AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(c.`', @creature_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: creature list backup'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Apply */
SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode = 'list' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE `creature` c ',
    'JOIN _c_norm n ON n.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'AND CAST(n.oldVal AS BINARY(255)) = CAST(c.`', @creature_spawn_col, '` AS BINARY(255)) ',
    'SET c.`', @creature_spawn_col, '` = n.newVal ',
    'WHERE n.needs_fix = 1 ',
    'AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(c.`', @creature_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: creature list update'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @creature_updated := IF(@creature_mode = 'list', ROW_COUNT(), @creature_updated);
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* GAMEOBJECT — MASK MODE                                             */
/* ================================================================== */
SELECT 'GAMEOBJECT MASK MODE' AS section;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'mask',
  CONCAT(
    'INSERT IGNORE INTO `gameobject_backup_genre5a_phase2b` SELECT g.* FROM `gameobject` g ',
    'JOIN _allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
    'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 ',
    'OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: gameobject mask backup'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'mask' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE `gameobject` g ',
    'JOIN _allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
    'SET g.`', @go_spawn_col, '` = IF(',
      '(g.`', @go_spawn_col, '` & am.allowedMask) = 0, ',
      'am.lowBit, ',
      '(g.`', @go_spawn_col, '` & am.allowedMask)) ',
    'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 ',
    'OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0)'
  ),
  'SELECT ''SKIP: gameobject mask update'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @go_updated := ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* GAMEOBJECT — LIST MODE                                             */
/* ================================================================== */
SELECT 'GAMEOBJECT LIST MODE' AS section;

DROP TEMPORARY TABLE IF EXISTS _g_distinct;
CREATE TEMPORARY TABLE _g_distinct (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS _g_norm;
CREATE TEMPORARY TABLE _g_norm (
  mapId INT UNSIGNED NOT NULL,
  oldVal VARCHAR(255) NOT NULL,
  newVal VARCHAR(255) NOT NULL,
  needs_fix TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (mapId, oldVal)
) ENGINE=InnoDB;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO _g_distinct(mapId, oldVal) ',
    'SELECT DISTINCT CAST(g.`', @go_map_col, '` AS UNSIGNED), g.`', @go_spawn_col, '` ',
    'FROM `gameobject` g ',
    'JOIN _allowed_min mn ON mn.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
    'WHERE g.`', @go_spawn_col, '` IS NOT NULL ',
    'AND g.`', @go_spawn_col, '` NOT IN ('''',''0'')'
  ),
  'SELECT ''SKIP: gameobject list distinct'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Build normalized values — same non-numeric fix */
SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list',
  CONCAT(
    'INSERT INTO _g_norm(mapId, oldVal, newVal, needs_fix) ',
    'SELECT d.mapId, d.oldVal, ',
    'COALESCE(NULLIF(',
      'GROUP_CONCAT(DISTINCT CASE WHEN ad.difficultyId IS NOT NULL ',
        'THEN CAST(ad.difficultyId AS CHAR) END ',
        'ORDER BY ad.difficultyId SEPARATOR '',''), ''''), ',
      'CAST(mn.minDifficultyId AS CHAR)) AS newVal, ',
    'IF(MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END) = 1 ',
      'OR MAX(CASE WHEN NOT (jt.tok REGEXP ''^[0-9]+$'') THEN 1 ELSE 0 END) = 1 ',
      'OR SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) = 0, 1, 0) AS needs_fix ',
    'FROM _g_distinct d ',
    'JOIN _allowed_min mn ON mn.mapId = d.mapId ',
    'JOIN JSON_TABLE(',
      'CONCAT(''["'', REPLACE(REPLACE(IFNULL(d.oldVal,''''),'' '',''''),'','',''","''), ''"]''), ',
      '''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
    'LEFT JOIN _allowed_diff ad ON ad.mapId = d.mapId ',
      'AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
    'GROUP BY d.mapId, d.oldVal, mn.minDifficultyId'
  ),
  'SELECT ''SKIP: gameobject list norm'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list',
  CONCAT(
    'INSERT IGNORE INTO `gameobject_backup_genre5a_phase2b` SELECT g.* FROM `gameobject` g ',
    'JOIN _g_norm n ON n.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'AND CAST(n.oldVal AS BINARY(255)) = CAST(g.`', @go_spawn_col, '` AS BINARY(255)) ',
    'WHERE n.needs_fix = 1 ',
    'AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(g.`', @go_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: gameobject list backup'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode = 'list' AND @APPLY_FIX = 1,
  CONCAT(
    'UPDATE `gameobject` g ',
    'JOIN _g_norm n ON n.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'AND CAST(n.oldVal AS BINARY(255)) = CAST(g.`', @go_spawn_col, '` AS BINARY(255)) ',
    'SET g.`', @go_spawn_col, '` = n.newVal ',
    'WHERE n.needs_fix = 1 ',
    'AND NOT (CAST(n.newVal AS BINARY(255)) <=> CAST(g.`', @go_spawn_col, '` AS BINARY(255)))'
  ),
  'SELECT ''SKIP: gameobject list update'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @go_updated := IF(@go_mode = 'list', ROW_COUNT(), @go_updated);
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* VERIFICATION                                                       */
/* ================================================================== */
SELECT 'VERIFICATION' AS section;

SET @creature_remaining := NULL;
SET @go_remaining       := NULL;

SET @sql := IF(@has_md = 1 AND @creature_exists = 1 AND @creature_mode IS NOT NULL,
  IF(@creature_mode = 'mask',
    CONCAT(
      'SELECT COUNT(*) INTO @creature_remaining FROM `creature` c ',
      'JOIN _allowed_mask am ON am.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
      'WHERE ((c.`', @creature_spawn_col, '` & ~am.allowedMask) <> 0 ',
      'OR (c.`', @creature_spawn_col, '` & am.allowedMask) = 0)'
    ),
    CONCAT(
      'SELECT COUNT(*) INTO @creature_remaining FROM (',
        'SELECT c.`', @creature_guid_col, '` FROM `creature` c ',
        'JOIN _allowed_min mn ON mn.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
        'JOIN JSON_TABLE(',
          'CONCAT(''["'', REPLACE(REPLACE(IFNULL(c.`', @creature_spawn_col, '`,''''),'' '',''''),'','',''","''),''"]''), ',
          '''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
        'LEFT JOIN _allowed_diff ad ON ad.mapId = CAST(c.`', @creature_map_col, '` AS UNSIGNED) ',
          'AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
        'WHERE c.`', @creature_spawn_col, '` IS NOT NULL AND c.`', @creature_spawn_col, '` NOT IN ('''',''0'') ',
        'GROUP BY c.`', @creature_guid_col, '` ',
        'HAVING MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END) = 1 ',
        'OR MAX(CASE WHEN NOT (jt.tok REGEXP ''^[0-9]+$'') THEN 1 ELSE 0 END) = 1 ',
        'OR SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) = 0',
      ') x'
    )
  ),
  'SELECT NULL INTO @creature_remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@has_md = 1 AND @go_exists = 1 AND @go_mode IS NOT NULL,
  IF(@go_mode = 'mask',
    CONCAT(
      'SELECT COUNT(*) INTO @go_remaining FROM `gameobject` g ',
      'JOIN _allowed_mask am ON am.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
      'WHERE ((g.`', @go_spawn_col, '` & ~am.allowedMask) <> 0 ',
      'OR (g.`', @go_spawn_col, '` & am.allowedMask) = 0)'
    ),
    CONCAT(
      'SELECT COUNT(*) INTO @go_remaining FROM (',
        'SELECT g.`', @go_guid_col, '` FROM `gameobject` g ',
        'JOIN _allowed_min mn ON mn.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
        'JOIN JSON_TABLE(',
          'CONCAT(''["'', REPLACE(REPLACE(IFNULL(g.`', @go_spawn_col, '`,''''),'' '',''''),'','',''","''),''"]''), ',
          '''$[*]'' COLUMNS(tok VARCHAR(32) PATH ''$'')) jt ',
        'LEFT JOIN _allowed_diff ad ON ad.mapId = CAST(g.`', @go_map_col, '` AS UNSIGNED) ',
          'AND jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId = CAST(jt.tok AS UNSIGNED) ',
        'WHERE g.`', @go_spawn_col, '` IS NOT NULL AND g.`', @go_spawn_col, '` NOT IN ('''',''0'') ',
        'GROUP BY g.`', @go_guid_col, '` ',
        'HAVING MAX(CASE WHEN jt.tok REGEXP ''^[0-9]+$'' AND ad.difficultyId IS NULL THEN 1 ELSE 0 END) = 1 ',
        'OR MAX(CASE WHEN NOT (jt.tok REGEXP ''^[0-9]+$'') THEN 1 ELSE 0 END) = 1 ',
        'OR SUM(CASE WHEN ad.difficultyId IS NOT NULL THEN 1 ELSE 0 END) = 0',
      ') x'
    )
  ),
  'SELECT NULL INTO @go_remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── Results ─────────────────────────────────────────────────────── */
SELECT
  @APPLY_FIX          AS apply_fix,
  @creature_updated   AS creature_rows_updated,
  @go_updated         AS gameobject_rows_updated,
  IFNULL(@creature_remaining, 0) AS creature_remaining_invalid,
  IFNULL(@go_remaining, 0)       AS gameobject_remaining_invalid;

/* ── Cleanup temps ───────────────────────────────────────────────── */
DROP TEMPORARY TABLE IF EXISTS _c_distinct;
DROP TEMPORARY TABLE IF EXISTS _c_norm;
DROP TEMPORARY TABLE IF EXISTS _g_distinct;
DROP TEMPORARY TABLE IF EXISTS _g_norm;
DROP TEMPORARY TABLE IF EXISTS _allowed_diff;
DROP TEMPORARY TABLE IF EXISTS _allowed_min;
DROP TEMPORARY TABLE IF EXISTS _allowed_mask;

COMMIT;

/* ── Restore session ─────────────────────────────────────────────── */
SET SQL_SAFE_UPDATES             = COALESCE(@OLD_SQL_SAFE_UPDATES, 1);
SET FOREIGN_KEY_CHECKS           = COALESCE(@OLD_FOREIGN_KEY_CHECKS, 1);
SET UNIQUE_CHECKS                = COALESCE(@OLD_UNIQUE_CHECKS, 1);
SET AUTOCOMMIT                   = COALESCE(@OLD_AUTOCOMMIT, 1);
SET SESSION group_concat_max_len = CAST(COALESCE(@OLD_GC_MAX_LEN, 1024) AS UNSIGNED);

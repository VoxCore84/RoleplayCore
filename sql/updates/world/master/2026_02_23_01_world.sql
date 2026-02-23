USE `world`;
SELECT DATABASE() AS `active_database`;

SET @APPLY_FIX := 1;
SET @MAX_DELETE := 55000;
SET @MAX_UPDATE := 520000;
SET @FORCE_APPLY := 0;

SET @OLD_SQL_SAFE_UPDATES := @@sql_safe_updates;
SET @OLD_FOREIGN_KEY_CHECKS := @@foreign_key_checks;
SET @OLD_UNIQUE_CHECKS := @@unique_checks;
SET @OLD_AUTOCOMMIT := @@autocommit;

SET @delete_candidates := 0;
SET @update_candidates := 0;
SET @deleted_invalid_map := 0;
SET @updated_phase := 0;
SET @updated_model := 0;
SET @cap_note := 'DIAGNOSTIC: no changes requested';
SET @invalid_map_count := 0;
SET @invalid_phase_count := 0;
SET @invalid_model_count := 0;

SET sql_safe_updates = 0;
SET foreign_key_checks = 1;
SET unique_checks = 1;
SET autocommit = 0;

START TRANSACTION;

SET @go_exists := (
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = 'world' AND table_name = 'gameobject'
);
SET @cr_exists := (
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = 'world' AND table_name = 'creature'
);

SET @go_guid_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = 'world'
      AND table_name = 'gameobject'
      AND column_name IN ('guid','GUID','id','ID')
    ORDER BY FIELD(column_name, 'guid','GUID','id','ID')
    LIMIT 1
);
SET @go_map_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = 'world'
      AND table_name = 'gameobject'
      AND column_name IN ('map','Map','mapId','MapId')
    ORDER BY FIELD(column_name, 'map','Map','mapId','MapId')
    LIMIT 1
);
SET @go_phase_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = 'world'
      AND table_name = 'gameobject'
      AND column_name IN ('phaseid','PhaseId','PhaseID','phase_id')
    ORDER BY FIELD(column_name, 'phaseid','PhaseId','PhaseID','phase_id')
    LIMIT 1
);
SET @go_entry_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = 'world'
      AND table_name = 'gameobject'
      AND column_name IN ('entry','gameobjectid','GameObjectID','id')
    ORDER BY FIELD(column_name, 'entry','gameobjectid','GameObjectID','id')
    LIMIT 1
);

SET @cr_guid_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = 'world'
      AND table_name = 'creature'
      AND column_name IN ('guid','GUID','id','ID')
    ORDER BY FIELD(column_name, 'guid','GUID','id','ID')
    LIMIT 1
);
SET @cr_model_col := (
    SELECT CASE
        WHEN EXISTS (
            SELECT 1
            FROM information_schema.columns
            WHERE table_schema = 'world'
              AND table_name = 'creature'
              AND column_name = 'modelid'
        ) THEN 'modelid'
        ELSE (
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'world'
              AND table_name = 'creature'
              AND column_name IN ('modelId','ModelId','displayid','DisplayId','displayId')
            ORDER BY FIELD(column_name, 'modelId','ModelId','displayid','DisplayId','displayId')
            LIMIT 1
        )
    END
);
SET @cr_entry_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema = 'world'
      AND table_name = 'creature'
      AND column_name IN ('entry','creatureid','CreatureID','id')
    ORDER BY FIELD(column_name, 'entry','creatureid','CreatureID','id')
    LIMIT 1
);

SET @sql := IF(
    @go_exists = 1 AND @go_map_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @invalid_map_count FROM `world`.`gameobject` WHERE `',
        @go_map_col,
        '` IN (1470,1178,451,2100,1180)'
    ),
    'SELECT 0 INTO @invalid_map_count'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_phase_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @invalid_phase_count FROM `world`.`gameobject` WHERE `',
        @go_phase_col,
        '` IN (385942,7,42833) AND `',
        @go_phase_col,
        '` <> 0'
    ),
    'SELECT 0 INTO @invalid_phase_count'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @cr_exists = 1 AND @cr_model_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @invalid_model_count FROM `world`.`creature` WHERE `',
        @cr_model_col,
        '` IN (959,12346,14952,239,28283) AND `',
        @cr_model_col,
        '` <> 0'
    ),
    'SELECT 0 INTO @invalid_model_count'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @delete_candidates := COALESCE(@invalid_map_count, 0);
SET @update_candidates := COALESCE(@invalid_phase_count, 0) + COALESCE(@invalid_model_count, 0);
SET @caps_exceeded := IF(@delete_candidates > @MAX_DELETE OR @update_candidates > @MAX_UPDATE, 1, 0);
SET @apply_allowed := IF(@APPLY_FIX = 1 AND (@caps_exceeded = 0 OR @FORCE_APPLY = 1), 1, 0);
SET @cap_note := CASE
    WHEN @APPLY_FIX = 0 THEN 'DIAGNOSTIC: @APPLY_FIX=0, no data changed'
    WHEN @caps_exceeded = 1 AND @FORCE_APPLY = 0 THEN CONCAT('CAP BLOCKED: delete_candidates=', @delete_candidates, ', update_candidates=', @update_candidates)
    WHEN @apply_allowed = 1 THEN 'APPLY: caps satisfied, mutations enabled'
    ELSE 'DIAGNOSTIC: no data changed'
END;

SET @sql := IF(
    @go_exists = 1 AND @go_map_col IS NOT NULL,
    CONCAT(
        'SELECT ''DIAG_A_COUNT'' AS section_name, COUNT(*) AS row_count FROM `world`.`gameobject` WHERE `',
        @go_map_col,
        '` IN (1470,1178,451,2100,1180)'
    ),
    'SELECT ''SKIP: world.gameobject map diagnostics unavailable (table/column missing)'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_map_col IS NOT NULL,
    CONCAT(
        'SELECT `',
        @go_map_col,
        '` AS map_id, COUNT(*) AS row_count FROM `world`.`gameobject` WHERE `',
        @go_map_col,
        '` IN (1470,1178,451,2100,1180) GROUP BY `',
        @go_map_col,
        '` ORDER BY `',
        @go_map_col,
        '`'
    ),
    'SELECT ''SKIP: world.gameobject invalid-map breakdown unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_map_col IS NOT NULL,
    CONCAT(
        'SELECT `',
        @go_guid_col,
        '` AS guid, ',
        IF(@go_entry_col IS NOT NULL, CONCAT('`', @go_entry_col, '`'), 'NULL'),
        ' AS entry_id, `',
        @go_map_col,
        '` AS map_id FROM `world`.`gameobject` WHERE `',
        @go_map_col,
        '` IN (1470,1178,451,2100,1180) ORDER BY `',
        @go_guid_col,
        '` LIMIT 50'
    ),
    'SELECT ''SKIP: world.gameobject invalid-map sample unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_phase_col IS NOT NULL,
    CONCAT(
        'SELECT ''DIAG_B_COUNT'' AS section_name, COUNT(*) AS row_count FROM `world`.`gameobject` WHERE `',
        @go_phase_col,
        '` IN (385942,7,42833) AND `',
        @go_phase_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: world.gameobject phase diagnostics unavailable (table/column missing)'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_phase_col IS NOT NULL,
    CONCAT(
        'SELECT `',
        @go_phase_col,
        '` AS phaseid, COUNT(*) AS row_count FROM `world`.`gameobject` WHERE `',
        @go_phase_col,
        '` IN (385942,7,42833) AND `',
        @go_phase_col,
        '` <> 0 GROUP BY `',
        @go_phase_col,
        '` ORDER BY `',
        @go_phase_col,
        '`'
    ),
    'SELECT ''SKIP: world.gameobject invalid-phase breakdown unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_phase_col IS NOT NULL,
    CONCAT(
        'SELECT `',
        @go_guid_col,
        '` AS guid, ',
        IF(@go_entry_col IS NOT NULL, CONCAT('`', @go_entry_col, '`'), 'NULL'),
        ' AS entry_id, `',
        @go_phase_col,
        '` AS phaseid, ',
        IF(@go_map_col IS NOT NULL, CONCAT('`', @go_map_col, '`'), 'NULL'),
        ' AS map_id FROM `world`.`gameobject` WHERE `',
        @go_phase_col,
        '` IN (385942,7,42833) AND `',
        @go_phase_col,
        '` <> 0 ORDER BY `',
        @go_guid_col,
        '` LIMIT 50'
    ),
    'SELECT ''SKIP: world.gameobject invalid-phase sample unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @cr_exists = 1 AND @cr_model_col IS NOT NULL,
    CONCAT(
        'SELECT ''DIAG_C_COUNT'' AS section_name, COUNT(*) AS row_count FROM `world`.`creature` WHERE `',
        @cr_model_col,
        '` IN (959,12346,14952,239,28283) AND `',
        @cr_model_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: world.creature model diagnostics unavailable (table/column missing)'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @cr_exists = 1 AND @cr_model_col IS NOT NULL,
    CONCAT(
        'SELECT `',
        @cr_model_col,
        '` AS modelid, COUNT(*) AS row_count FROM `world`.`creature` WHERE `',
        @cr_model_col,
        '` IN (959,12346,14952,239,28283) AND `',
        @cr_model_col,
        '` <> 0 GROUP BY `',
        @cr_model_col,
        '` ORDER BY `',
        @cr_model_col,
        '`'
    ),
    'SELECT ''SKIP: world.creature invalid-model breakdown unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @cr_exists = 1 AND @cr_guid_col IS NOT NULL AND @cr_model_col IS NOT NULL,
    CONCAT(
        'SELECT `',
        @cr_guid_col,
        '` AS guid, ',
        IF(@cr_entry_col IS NOT NULL, CONCAT('`', @cr_entry_col, '`'), 'NULL'),
        ' AS entry_id, `',
        @cr_model_col,
        '` AS modelid FROM `world`.`creature` WHERE `',
        @cr_model_col,
        '` IN (959,12346,14952,239,28283) AND `',
        @cr_model_col,
        '` <> 0 ORDER BY `',
        @cr_guid_col,
        '` LIMIT 50'
    ),
    'SELECT ''SKIP: world.creature invalid-model sample unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_map_col IS NOT NULL,
    'CREATE TABLE IF NOT EXISTS `world`.`gameobject_backup_genre5c_invalid_map` LIKE `world`.`gameobject`',
    'SELECT ''SKIP: backup table gameobject_backup_genre5c_invalid_map not created'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_map_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `world`.`gameobject_backup_genre5c_invalid_map` SELECT go.* FROM `world`.`gameobject` go WHERE go.`',
        @go_map_col,
        '` IN (1470,1178,451,2100,1180)'
    ),
    'SELECT ''SKIP: backup insert for invalid-map gameobjects not run'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_map_col IS NOT NULL,
    CONCAT(
        'DELETE FROM `world`.`gameobject` WHERE `',
        @go_map_col,
        '` IN (1470,1178,451,2100,1180)'
    ),
    'SELECT ''SKIP: invalid-map gameobject delete not run'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
SET @deleted_invalid_map := IF(@apply_allowed = 1 AND @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_map_col IS NOT NULL, ROW_COUNT(), 0);
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_phase_col IS NOT NULL,
    'CREATE TABLE IF NOT EXISTS `world`.`gameobject_backup_genre5c_phase_fix` LIKE `world`.`gameobject`',
    'SELECT ''SKIP: backup table gameobject_backup_genre5c_phase_fix not created'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @go_exists = 1 AND @go_guid_col IS NOT NULL AND @go_phase_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `world`.`gameobject_backup_genre5c_phase_fix` SELECT go.* FROM `world`.`gameobject` go WHERE go.`',
        @go_phase_col,
        '` IN (385942,7,42833) AND go.`',
        @go_phase_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: backup insert for invalid-phase gameobjects not run'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @go_exists = 1 AND @go_phase_col IS NOT NULL,
    CONCAT(
        'UPDATE `world`.`gameobject` SET `',
        @go_phase_col,
        '` = 0 WHERE `',
        @go_phase_col,
        '` IN (385942,7,42833) AND `',
        @go_phase_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: invalid-phase gameobject update not run'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
SET @updated_phase := IF(@apply_allowed = 1 AND @go_exists = 1 AND @go_phase_col IS NOT NULL, ROW_COUNT(), 0);
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @cr_exists = 1 AND @cr_guid_col IS NOT NULL AND @cr_model_col IS NOT NULL,
    'CREATE TABLE IF NOT EXISTS `world`.`creature_backup_genre5c_model_fix` LIKE `world`.`creature`',
    'SELECT ''SKIP: backup table creature_backup_genre5c_model_fix not created'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @cr_exists = 1 AND @cr_guid_col IS NOT NULL AND @cr_model_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `world`.`creature_backup_genre5c_model_fix` SELECT c.* FROM `world`.`creature` c WHERE c.`',
        @cr_model_col,
        '` IN (959,12346,14952,239,28283) AND c.`',
        @cr_model_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: backup insert for invalid-model creatures not run'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @apply_allowed = 1 AND @cr_exists = 1 AND @cr_model_col IS NOT NULL,
    CONCAT(
        'UPDATE `world`.`creature` SET `',
        @cr_model_col,
        '` = 0 WHERE `',
        @cr_model_col,
        '` IN (959,12346,14952,239,28283) AND `',
        @cr_model_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: invalid-model creature update not run'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
SET @updated_model := IF(@apply_allowed = 1 AND @cr_exists = 1 AND @cr_model_col IS NOT NULL, ROW_COUNT(), 0);
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_map_col IS NOT NULL,
    CONCAT(
        'SELECT ''VERIFY_A_INVALID_MAP'' AS section_name, COUNT(*) AS remaining_rows FROM `world`.`gameobject` WHERE `',
        @go_map_col,
        '` IN (1470,1178,451,2100,1180)'
    ),
    'SELECT ''SKIP: verify invalid-map unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @go_exists = 1 AND @go_phase_col IS NOT NULL,
    CONCAT(
        'SELECT ''VERIFY_B_INVALID_PHASE'' AS section_name, COUNT(*) AS remaining_rows FROM `world`.`gameobject` WHERE `',
        @go_phase_col,
        '` IN (385942,7,42833) AND `',
        @go_phase_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: verify invalid-phase unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @cr_exists = 1 AND @cr_model_col IS NOT NULL,
    CONCAT(
        'SELECT ''VERIFY_C_INVALID_MODEL'' AS section_name, COUNT(*) AS remaining_rows FROM `world`.`creature` WHERE `',
        @cr_model_col,
        '` IN (959,12346,14952,239,28283) AND `',
        @cr_model_col,
        '` <> 0'
    ),
    'SELECT ''SKIP: verify invalid-model unavailable'' AS note'
);
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

SELECT
    @delete_candidates AS delete_candidates,
    @update_candidates AS update_candidates,
    @deleted_invalid_map AS deleted_invalid_map,
    @updated_phase AS updated_phase,
    @updated_model AS updated_model,
    @cap_note AS cap_note;

COMMIT;

SET sql_safe_updates = @OLD_SQL_SAFE_UPDATES;
SET foreign_key_checks = @OLD_FOREIGN_KEY_CHECKS;
SET unique_checks = @OLD_UNIQUE_CHECKS;
SET autocommit = @OLD_AUTOCOMMIT;

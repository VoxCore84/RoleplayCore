USE `world`;

SET @APPLY_FIX := 1;
SET @MAX_UPDATE := 25000;
SET @FORCE_UPDATE := 0;

SET @updated_rows := 0;
SET @candidates_before := 0;
SET @candidates_after := 0;
SET @cap_note := 'NOT_APPLIED';

SET @at_exists := (
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = 'world' AND table_name = 'areatrigger'
);

SELECT IF(@at_exists = 1, 'OK: world.areatrigger exists', 'SKIP: world.areatrigger does not exist') AS note;

SET @spawn_pk_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema='world' AND table_name='areatrigger'
      AND column_name IN ('SpawnId','spawnId','guid','GUID','id','ID')
    ORDER BY FIELD(column_name,'SpawnId','spawnId','guid','GUID','id','ID')
    LIMIT 1
);

SET @map_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema='world' AND table_name='areatrigger'
      AND column_name IN ('map','Map','mapId','MapId')
    ORDER BY FIELD(column_name,'map','Map','mapId','MapId')
    LIMIT 1
);

SET @create_prop_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema='world' AND table_name='areatrigger'
      AND LOWER(column_name) REGEXP 'create.*propert'
    ORDER BY (LOWER(column_name)='createpropertiesid') DESC,
             (LOWER(column_name)='createproperties') DESC,
             LENGTH(column_name)
    LIMIT 1
);

SET @difficulty_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema='world' AND table_name='areatrigger'
      AND column_name IN ('spawnDifficulties','SpawnDifficulties','spawn_difficulties','spawnMask','SpawnMask','difficulty','Difficulty','difficultyId','DifficultyId')
    ORDER BY FIELD(column_name,'spawnDifficulties','SpawnDifficulties','spawn_difficulties','spawnMask','SpawnMask','difficulty','Difficulty','difficultyId','DifficultyId')
    LIMIT 1
);

SET @difficulty_type := (
    SELECT data_type
    FROM information_schema.columns
    WHERE table_schema='world' AND table_name='areatrigger' AND column_name=@difficulty_col
    LIMIT 1
);

SET @difficulty_kind := (
    CASE
        WHEN @difficulty_col IS NULL THEN 'NONE'
        WHEN LOWER(@difficulty_col) LIKE '%mask%' THEN 'MASK'
        WHEN @difficulty_type IN ('char','varchar','text','tinytext','mediumtext','longtext') THEN 'LIST'
        WHEN LOWER(@difficulty_col) IN ('spawndifficulties','spawn_difficulties') THEN 'LIST'
        ELSE 'SCALAR'
    END
);

SET @md_world_exists := (
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema='world' AND table_name='map_difficulty'
);
SET @md_hotfix_exists := (
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema='hotfixes' AND table_name='map_difficulty'
);
SET @md_schema := (
    CASE
        WHEN @md_world_exists = 1 THEN 'world'
        WHEN @md_hotfix_exists = 1 THEN 'hotfixes'
        ELSE NULL
    END
);

SET @md_map_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema=@md_schema AND table_name='map_difficulty'
      AND column_name IN ('MapID','MapId','mapID','mapId','map')
    ORDER BY FIELD(column_name,'MapID','MapId','mapID','mapId','map')
    LIMIT 1
);

SET @md_diff_col := (
    SELECT column_name
    FROM information_schema.columns
    WHERE table_schema=@md_schema AND table_name='map_difficulty'
      AND column_name IN ('DifficultyID','DifficultyId','difficulty','Difficulty')
    ORDER BY FIELD(column_name,'DifficultyID','DifficultyId','difficulty','Difficulty')
    LIMIT 1
);

SELECT
    @spawn_pk_col AS detected_spawn_pk_col,
    @map_col AS detected_map_col,
    @create_prop_col AS detected_create_properties_col,
    @difficulty_col AS detected_difficulty_col,
    @difficulty_type AS detected_difficulty_type,
    @difficulty_kind AS detected_difficulty_kind,
    @md_schema AS detected_map_difficulty_schema,
    @md_map_col AS detected_map_difficulty_map_col,
    @md_diff_col AS detected_map_difficulty_difficulty_col;

DROP TEMPORARY TABLE IF EXISTS tmp_instance_maps;
CREATE TEMPORARY TABLE tmp_instance_maps (
    mapId BIGINT NOT NULL,
    PRIMARY KEY (mapId)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS tmp_map_allowed;
CREATE TEMPORARY TABLE tmp_map_allowed (
    mapId BIGINT NOT NULL,
    allowedMask BIGINT UNSIGNED NOT NULL,
    minDiff INT NOT NULL,
    allowedList TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    PRIMARY KEY (mapId)
) ENGINE=InnoDB;

SET @sql_md := (
    CASE
        WHEN @md_schema IS NOT NULL AND @md_map_col IS NOT NULL AND @md_diff_col IS NOT NULL THEN
            CONCAT(
                'INSERT INTO tmp_map_allowed (mapId, allowedMask, minDiff, allowedList) ',
                'SELECT CAST(`', @md_map_col, '` AS SIGNED) AS mapId, ',
                'BIT_OR(CASE WHEN CAST(`', @md_diff_col, '` AS SIGNED) BETWEEN 0 AND 62 THEN (1 << CAST(`', @md_diff_col, '` AS SIGNED)) ELSE 0 END) AS allowedMask, ',
                'MIN(CAST(`', @md_diff_col, '` AS SIGNED)) AS minDiff, ',
                'GROUP_CONCAT(DISTINCT CAST(`', @md_diff_col, '` AS SIGNED) ORDER BY CAST(`', @md_diff_col, '` AS SIGNED) SEPARATOR '','') AS allowedList ',
                'FROM `', @md_schema, '`.`map_difficulty` GROUP BY CAST(`', @md_map_col, '` AS SIGNED)'
            )
        ELSE
            'SELECT ''SKIP: map_difficulty metadata unavailable'' AS note'
    END
);
PREPARE stmt_md FROM @sql_md;
EXECUTE stmt_md;
DEALLOCATE PREPARE stmt_md;

INSERT IGNORE INTO tmp_instance_maps (mapId)
SELECT mapId FROM tmp_map_allowed;

DROP TEMPORARY TABLE IF EXISTS tmp_at_scan;
CREATE TEMPORARY TABLE tmp_at_scan (
    spawnPK BIGINT NOT NULL,
    mapId BIGINT NULL,
    createPropertiesId BIGINT NULL,
    diff_raw TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    diff_num BIGINT NULL,
    PRIMARY KEY (spawnPK),
    KEY idx_mapId (mapId)
) ENGINE=InnoDB;

SET @sql_scan := (
    CASE
        WHEN @at_exists = 1 AND @spawn_pk_col IS NOT NULL AND @map_col IS NOT NULL AND @difficulty_col IS NOT NULL THEN
            CONCAT(
                'INSERT INTO tmp_at_scan (spawnPK, mapId, createPropertiesId, diff_raw, diff_num) ',
                'SELECT CAST(`', @spawn_pk_col, '` AS SIGNED), ',
                'CAST(`', @map_col, '` AS SIGNED), ',
                CASE WHEN @create_prop_col IS NOT NULL THEN CONCAT('CAST(`', @create_prop_col, '` AS SIGNED)') ELSE 'NULL' END,
                ', CAST(`', @difficulty_col, '` AS CHAR), ',
                'CASE ',
                'WHEN CAST(`', @difficulty_col, '` AS CHAR) REGEXP ''^-?[0-9]+$'' THEN CAST(`', @difficulty_col, '` AS SIGNED) ',
                'ELSE NULL END ',
                'FROM `world`.`areatrigger`'
            )
        ELSE
            'SELECT ''SKIP: required areatrigger columns unavailable'' AS note'
    END
);
PREPARE stmt_scan FROM @sql_scan;
EXECUTE stmt_scan;
DEALLOCATE PREPARE stmt_scan;

DROP TEMPORARY TABLE IF EXISTS tmp_apply;
CREATE TEMPORARY TABLE tmp_apply (
    spawnPK BIGINT NOT NULL,
    new_diff_num BIGINT NULL,
    new_diff_text TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    PRIMARY KEY (spawnPK)
) ENGINE=InnoDB;

SET @sql_apply_build := (
    CASE
        WHEN @difficulty_kind = 'MASK' THEN
            CONCAT(
                'INSERT INTO tmp_apply (spawnPK, new_diff_num, new_diff_text) ',
                'SELECT s.spawnPK, ',
                'CASE ',
                'WHEN i.mapId IS NULL THEN 1 ',
                'WHEN a.allowedMask > 0 THEN ',
                'CASE WHEN (COALESCE(s.diff_num,0) & a.allowedMask) > 0 THEN (COALESCE(s.diff_num,0) & a.allowedMask) ELSE (1 << a.minDiff) END ',
                'ELSE COALESCE(s.diff_num,0) END AS new_diff_num, NULL ',
                'FROM tmp_at_scan s ',
                'LEFT JOIN tmp_instance_maps i ON i.mapId = s.mapId ',
                'LEFT JOIN tmp_map_allowed a ON a.mapId = s.mapId ',
                'WHERE (i.mapId IS NULL AND COALESCE(s.diff_num,0) <> 1) ',
                'OR (i.mapId IS NOT NULL AND a.allowedMask > 0 AND NOT (COALESCE(s.diff_num,0) <=> ',
                'CASE WHEN (COALESCE(s.diff_num,0) & a.allowedMask) > 0 THEN (COALESCE(s.diff_num,0) & a.allowedMask) ELSE (1 << a.minDiff) END))'
            )
        WHEN @difficulty_kind = 'LIST' THEN
            'SELECT ''INFO: building LIST candidates'' AS note'
        ELSE
            'SELECT ''SKIP: unsupported difficulty kind for mutation'' AS note'
    END
);
PREPARE stmt_apply_build FROM @sql_apply_build;
EXECUTE stmt_apply_build;
DEALLOCATE PREPARE stmt_apply_build;

DROP TEMPORARY TABLE IF EXISTS tmp_list_tokens;
CREATE TEMPORARY TABLE tmp_list_tokens (
    spawnPK BIGINT NOT NULL,
    diffId INT NOT NULL,
    PRIMARY KEY (spawnPK, diffId)
) ENGINE=InnoDB;

SET @sql_list_tokens := (
    CASE
        WHEN @difficulty_kind = 'LIST' THEN
            CONCAT(
                'INSERT IGNORE INTO tmp_list_tokens (spawnPK, diffId) ',
                'SELECT s.spawnPK, CAST(j.v AS SIGNED) AS diffId ',
                'FROM tmp_at_scan s ',
                'JOIN JSON_TABLE(CONCAT(''["'', REPLACE(REPLACE(REPLACE(COALESCE(s.diff_raw, ''''), '' '', ''''), '','', ''","''), ''|'', ''","''), ''"]''), ''$[*]'' COLUMNS (v VARCHAR(32) PATH ''$'')) j ',
                'ON 1=1 ',
                'WHERE j.v REGEXP ''^-?[0-9]+$'''
            )
        ELSE
            'SELECT ''SKIP: list tokenization not required'' AS note'
    END
);
PREPARE stmt_list_tokens FROM @sql_list_tokens;
EXECUTE stmt_list_tokens;
DEALLOCATE PREPARE stmt_list_tokens;

DROP TEMPORARY TABLE IF EXISTS tmp_list_norm;
CREATE TEMPORARY TABLE tmp_list_norm (
    spawnPK BIGINT NOT NULL,
    normList TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    PRIMARY KEY (spawnPK)
) ENGINE=InnoDB;

INSERT INTO tmp_list_norm (spawnPK, normList)
SELECT t.spawnPK,
       GROUP_CONCAT(DISTINCT t.diffId ORDER BY t.diffId SEPARATOR ',') AS normList
FROM tmp_list_tokens t
JOIN tmp_at_scan s ON s.spawnPK = t.spawnPK
JOIN tmp_map_allowed a ON a.mapId = s.mapId
WHERE t.diffId >= 0 AND ((1 << t.diffId) & a.allowedMask) > 0
GROUP BY t.spawnPK;

SET @sql_apply_list := (
    CASE
        WHEN @difficulty_kind = 'LIST' THEN
            CONCAT(
                'INSERT INTO tmp_apply (spawnPK, new_diff_num, new_diff_text) ',
                'SELECT s.spawnPK, NULL, ',
                'CASE ',
                'WHEN i.mapId IS NULL THEN ''0'' ',
                'WHEN a.mapId IS NOT NULL THEN COALESCE(n.normList, CAST(a.minDiff AS CHAR)) ',
                'ELSE COALESCE(s.diff_raw, ''0'') END AS new_diff_text ',
                'FROM tmp_at_scan s ',
                'LEFT JOIN tmp_instance_maps i ON i.mapId = s.mapId ',
                'LEFT JOIN tmp_map_allowed a ON a.mapId = s.mapId ',
                'LEFT JOIN tmp_list_norm n ON n.spawnPK = s.spawnPK ',
                'WHERE (i.mapId IS NULL AND NOT (CAST(COALESCE(NULLIF(TRIM(s.diff_raw), ''''), ''0'') AS BINARY(255)) <=> CAST(''0'' AS BINARY(255)))) ',
                'OR (i.mapId IS NOT NULL AND a.mapId IS NOT NULL AND NOT (CAST(COALESCE(n.normList, CAST(a.minDiff AS CHAR)) AS BINARY(255)) <=> CAST(COALESCE(NULLIF(TRIM(s.diff_raw), ''''), ''0'') AS BINARY(255))))'
            )
        ELSE
            'SELECT ''SKIP: list normalization not required'' AS note'
    END
);
PREPARE stmt_apply_list FROM @sql_apply_list;
EXECUTE stmt_apply_list;
DEALLOCATE PREPARE stmt_apply_list;

SET @sql_count_before := 'SELECT COUNT(*) INTO @candidates_before FROM tmp_apply';
PREPARE stmt_count_before FROM @sql_count_before;
EXECUTE stmt_count_before;
DEALLOCATE PREPARE stmt_count_before;

SELECT @candidates_before AS candidates_before;

SET @sql_noninst := (
    CASE
        WHEN @difficulty_kind = 'MASK' THEN
            'SELECT COUNT(*) AS non_default_non_instance FROM tmp_at_scan s LEFT JOIN tmp_instance_maps i ON i.mapId=s.mapId WHERE i.mapId IS NULL AND COALESCE(s.diff_num,0) <> 1'
        WHEN @difficulty_kind = 'LIST' THEN
            'SELECT COUNT(*) AS non_default_non_instance FROM tmp_at_scan s LEFT JOIN tmp_instance_maps i ON i.mapId=s.mapId WHERE i.mapId IS NULL AND NOT (CAST(COALESCE(NULLIF(TRIM(s.diff_raw), ''''), ''0'') AS BINARY(255)) <=> CAST(''0'' AS BINARY(255)))'
        ELSE
            'SELECT 0 AS non_default_non_instance'
    END
);
PREPARE stmt_noninst FROM @sql_noninst;
EXECUTE stmt_noninst;
DEALLOCATE PREPARE stmt_noninst;

SET @sql_inst_invalid := (
    CASE
        WHEN @md_schema IS NULL OR @difficulty_kind='NONE' THEN
            'SELECT 0 AS invalid_instance_rows'
        WHEN @difficulty_kind='MASK' THEN
            'SELECT COUNT(*) AS invalid_instance_rows FROM tmp_at_scan s JOIN tmp_map_allowed a ON a.mapId=s.mapId WHERE a.allowedMask > 0 AND (COALESCE(s.diff_num,0) & a.allowedMask) = 0'
        WHEN @difficulty_kind='LIST' THEN
            'SELECT COUNT(*) AS invalid_instance_rows FROM tmp_at_scan s JOIN tmp_map_allowed a ON a.mapId=s.mapId LEFT JOIN tmp_list_norm n ON n.spawnPK=s.spawnPK WHERE a.mapId IS NOT NULL AND (CAST(COALESCE(n.normList, '''') AS BINARY(255)) <=> CAST('''' AS BINARY(255)))'
        ELSE
            'SELECT 0 AS invalid_instance_rows'
    END
);
PREPARE stmt_inst_invalid FROM @sql_inst_invalid;
EXECUTE stmt_inst_invalid;
DEALLOCATE PREPARE stmt_inst_invalid;

SELECT s.spawnPK, s.mapId, s.diff_raw AS difficulty_value, s.createPropertiesId
FROM tmp_at_scan s
JOIN tmp_apply a ON a.spawnPK = s.spawnPK
ORDER BY s.mapId, s.spawnPK
LIMIT 50;

SET @can_apply := IF(@APPLY_FIX=1 AND (@candidates_before <= @MAX_UPDATE OR @FORCE_UPDATE=1), 1, 0);
SET @cap_note := IF(@APPLY_FIX=0, 'DIAGNOSTICS_ONLY', IF(@can_apply=1, 'APPLY_OK', CONCAT('CAP_BLOCKED: ', @candidates_before, ' > ', @MAX_UPDATE)));
SELECT @cap_note AS cap_note;

SET @sql_backup_create := (
    CASE
        WHEN @can_apply = 1 AND @spawn_pk_col IS NOT NULL THEN
            'CREATE TABLE IF NOT EXISTS `world`.`areatrigger_backup_genre7b_difficulty` LIKE `world`.`areatrigger`'
        ELSE
            'SELECT ''SKIP: backup table create not required'' AS note'
    END
);
PREPARE stmt_backup_create FROM @sql_backup_create;
EXECUTE stmt_backup_create;
DEALLOCATE PREPARE stmt_backup_create;

SET @sql_backup_insert := (
    CASE
        WHEN @can_apply = 1 AND @spawn_pk_col IS NOT NULL THEN
            CONCAT(
                'INSERT INTO `world`.`areatrigger_backup_genre7b_difficulty` ',
                'SELECT atb.* FROM `world`.`areatrigger` atb JOIN tmp_apply ta ON ta.spawnPK = CAST(atb.`', @spawn_pk_col, '` AS SIGNED)'
            )
        ELSE
            'SELECT ''SKIP: backup not required'' AS note'
    END
);
PREPARE stmt_backup_insert FROM @sql_backup_insert;
EXECUTE stmt_backup_insert;
DEALLOCATE PREPARE stmt_backup_insert;

SET @sql_update := (
    CASE
        WHEN @can_apply = 1 AND @difficulty_kind = 'MASK' AND @spawn_pk_col IS NOT NULL AND @difficulty_col IS NOT NULL THEN
            CONCAT(
                'UPDATE `world`.`areatrigger` atu JOIN tmp_apply ta ON ta.spawnPK = CAST(atu.`', @spawn_pk_col, '` AS SIGNED) ',
                'SET atu.`', @difficulty_col, '` = ta.new_diff_num'
            )
        WHEN @can_apply = 1 AND @difficulty_kind = 'LIST' AND @spawn_pk_col IS NOT NULL AND @difficulty_col IS NOT NULL THEN
            CONCAT(
                'UPDATE `world`.`areatrigger` atu JOIN tmp_apply ta ON ta.spawnPK = CAST(atu.`', @spawn_pk_col, '` AS SIGNED) ',
                'SET atu.`', @difficulty_col, '` = ta.new_diff_text'
            )
        ELSE
            'SELECT ''SKIP: update not executed'' AS note'
    END
);
PREPARE stmt_update FROM @sql_update;
EXECUTE stmt_update;
DEALLOCATE PREPARE stmt_update;

SET @updated_rows := IF(@can_apply=1, ROW_COUNT(), 0);
SELECT @updated_rows AS updated_rows;

TRUNCATE TABLE tmp_at_scan;
PREPARE stmt_scan2 FROM @sql_scan;
EXECUTE stmt_scan2;
DEALLOCATE PREPARE stmt_scan2;

TRUNCATE TABLE tmp_list_tokens;
PREPARE stmt_list_tokens2 FROM @sql_list_tokens;
EXECUTE stmt_list_tokens2;
DEALLOCATE PREPARE stmt_list_tokens2;

TRUNCATE TABLE tmp_list_norm;
INSERT INTO tmp_list_norm (spawnPK, normList)
SELECT t.spawnPK,
       GROUP_CONCAT(DISTINCT t.diffId ORDER BY t.diffId SEPARATOR ',') AS normList
FROM tmp_list_tokens t
JOIN tmp_at_scan s ON s.spawnPK = t.spawnPK
JOIN tmp_map_allowed a ON a.mapId = s.mapId
WHERE t.diffId >= 0 AND ((1 << t.diffId) & a.allowedMask) > 0
GROUP BY t.spawnPK;

SET @sql_count_after := (
    CASE
        WHEN @difficulty_kind = 'MASK' THEN
            'SELECT COUNT(*) INTO @candidates_after FROM tmp_at_scan s LEFT JOIN tmp_instance_maps i ON i.mapId=s.mapId LEFT JOIN tmp_map_allowed a ON a.mapId=s.mapId WHERE (i.mapId IS NULL AND COALESCE(s.diff_num,0) <> 1) OR (i.mapId IS NOT NULL AND a.allowedMask > 0 AND (COALESCE(s.diff_num,0) & a.allowedMask)=0)'
        WHEN @difficulty_kind = 'LIST' THEN
            'SELECT COUNT(*) INTO @candidates_after FROM tmp_at_scan s LEFT JOIN tmp_instance_maps i ON i.mapId=s.mapId LEFT JOIN tmp_map_allowed a ON a.mapId=s.mapId LEFT JOIN tmp_list_norm n ON n.spawnPK=s.spawnPK WHERE (i.mapId IS NULL AND NOT (CAST(COALESCE(NULLIF(TRIM(s.diff_raw), ''''), ''0'') AS BINARY(255)) <=> CAST(''0'' AS BINARY(255)))) OR (i.mapId IS NOT NULL AND a.mapId IS NOT NULL AND (CAST(COALESCE(n.normList, '''') AS BINARY(255)) <=> CAST('''' AS BINARY(255))))'
        ELSE
            'SELECT 0 INTO @candidates_after'
    END
);
PREPARE stmt_count_after FROM @sql_count_after;
EXECUTE stmt_count_after;
DEALLOCATE PREPARE stmt_count_after;

SELECT @candidates_before AS candidates_before, @updated_rows AS updated_rows, @candidates_after AS candidates_after, @cap_note AS cap_note;

SET @tbl := 'areatrigger_create_properties';
SET @sch := 'world';
SET @flags_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl AND column_name IN ('Flags','flags','flag','Flag') ORDER BY FIELD(column_name,'Flags','flags','flag','Flag') LIMIT 1);
SET @pk_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl ORDER BY (column_key='PRI') DESC, FIELD(column_name,'ID','Id','id','AreaTriggerCreatePropertiesId','areatriggerCreatePropertiesId') DESC, ordinal_position LIMIT 1);
SET @sql_flags := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value, COUNT(*) AS row_count FROM `',@sch,'`.`',@tbl,'` GROUP BY CAST(`',@flags_col,'` AS UNSIGNED) ORDER BY row_count DESC LIMIT 25') ELSE CONCAT('SELECT ''SKIP: no flags column in ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags FROM @sql_flags;
EXECUTE stmt_flags;
DEALLOCATE PREPARE stmt_flags;
SET @sql_flags_sample := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@pk_col,'` AS SIGNED) AS row_pk, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value FROM `',@sch,'`.`',@tbl,'` WHERE CAST(`',@flags_col,'` AS UNSIGNED) <> 0 OR CAST(`',@flags_col,'` AS UNSIGNED) >= 2147483648 ORDER BY CAST(`',@flags_col,'` AS UNSIGNED) DESC LIMIT 50') ELSE CONCAT('SELECT ''SKIP: no flags samples for ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags_sample FROM @sql_flags_sample;
EXECUTE stmt_flags_sample;
DEALLOCATE PREPARE stmt_flags_sample;

SET @tbl := 'areatrigger_create_properties';
SET @sch := 'hotfixes';
SET @flags_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl AND column_name IN ('Flags','flags','flag','Flag') ORDER BY FIELD(column_name,'Flags','flags','flag','Flag') LIMIT 1);
SET @pk_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl ORDER BY (column_key='PRI') DESC, FIELD(column_name,'ID','Id','id','AreaTriggerCreatePropertiesId','areatriggerCreatePropertiesId') DESC, ordinal_position LIMIT 1);
SET @sql_flags := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value, COUNT(*) AS row_count FROM `',@sch,'`.`',@tbl,'` GROUP BY CAST(`',@flags_col,'` AS UNSIGNED) ORDER BY row_count DESC LIMIT 25') ELSE CONCAT('SELECT ''SKIP: no flags column in ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags2 FROM @sql_flags;
EXECUTE stmt_flags2;
DEALLOCATE PREPARE stmt_flags2;
SET @sql_flags_sample := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@pk_col,'` AS SIGNED) AS row_pk, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value FROM `',@sch,'`.`',@tbl,'` WHERE CAST(`',@flags_col,'` AS UNSIGNED) <> 0 OR CAST(`',@flags_col,'` AS UNSIGNED) >= 2147483648 ORDER BY CAST(`',@flags_col,'` AS UNSIGNED) DESC LIMIT 50') ELSE CONCAT('SELECT ''SKIP: no flags samples for ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags_sample2 FROM @sql_flags_sample;
EXECUTE stmt_flags_sample2;
DEALLOCATE PREPARE stmt_flags_sample2;

SET @tbl := 'areatrigger_create_properties_template';
SET @sch := 'world';
SET @flags_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl AND column_name IN ('Flags','flags','flag','Flag') ORDER BY FIELD(column_name,'Flags','flags','flag','Flag') LIMIT 1);
SET @pk_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl ORDER BY (column_key='PRI') DESC, FIELD(column_name,'ID','Id','id','AreaTriggerCreatePropertiesId','areatriggerCreatePropertiesId') DESC, ordinal_position LIMIT 1);
SET @sql_flags := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value, COUNT(*) AS row_count FROM `',@sch,'`.`',@tbl,'` GROUP BY CAST(`',@flags_col,'` AS UNSIGNED) ORDER BY row_count DESC LIMIT 25') ELSE CONCAT('SELECT ''SKIP: no flags column in ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags3 FROM @sql_flags;
EXECUTE stmt_flags3;
DEALLOCATE PREPARE stmt_flags3;
SET @sql_flags_sample := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@pk_col,'` AS SIGNED) AS row_pk, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value FROM `',@sch,'`.`',@tbl,'` WHERE CAST(`',@flags_col,'` AS UNSIGNED) <> 0 OR CAST(`',@flags_col,'` AS UNSIGNED) >= 2147483648 ORDER BY CAST(`',@flags_col,'` AS UNSIGNED) DESC LIMIT 50') ELSE CONCAT('SELECT ''SKIP: no flags samples for ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags_sample3 FROM @sql_flags_sample;
EXECUTE stmt_flags_sample3;
DEALLOCATE PREPARE stmt_flags_sample3;

SET @tbl := 'areatrigger_create_properties_template';
SET @sch := 'hotfixes';
SET @flags_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl AND column_name IN ('Flags','flags','flag','Flag') ORDER BY FIELD(column_name,'Flags','flags','flag','Flag') LIMIT 1);
SET @pk_col := (SELECT column_name FROM information_schema.columns WHERE table_schema=@sch AND table_name=@tbl ORDER BY (column_key='PRI') DESC, FIELD(column_name,'ID','Id','id','AreaTriggerCreatePropertiesId','areatriggerCreatePropertiesId') DESC, ordinal_position LIMIT 1);
SET @sql_flags := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value, COUNT(*) AS row_count FROM `',@sch,'`.`',@tbl,'` GROUP BY CAST(`',@flags_col,'` AS UNSIGNED) ORDER BY row_count DESC LIMIT 25') ELSE CONCAT('SELECT ''SKIP: no flags column in ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags4 FROM @sql_flags;
EXECUTE stmt_flags4;
DEALLOCATE PREPARE stmt_flags4;
SET @sql_flags_sample := (CASE WHEN @flags_col IS NOT NULL THEN CONCAT('SELECT ''',@sch,'.',@tbl,''' AS source_table, CAST(`',@pk_col,'` AS SIGNED) AS row_pk, CAST(`',@flags_col,'` AS UNSIGNED) AS flags_value FROM `',@sch,'`.`',@tbl,'` WHERE CAST(`',@flags_col,'` AS UNSIGNED) <> 0 OR CAST(`',@flags_col,'` AS UNSIGNED) >= 2147483648 ORDER BY CAST(`',@flags_col,'` AS UNSIGNED) DESC LIMIT 50') ELSE CONCAT('SELECT ''SKIP: no flags samples for ',@sch,'.',@tbl,''' AS note') END);
PREPARE stmt_flags_sample4 FROM @sql_flags_sample;
EXECUTE stmt_flags_sample4;
DEALLOCATE PREPARE stmt_flags_sample4;

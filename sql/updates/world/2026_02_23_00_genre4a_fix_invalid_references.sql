/* ================================================================== */
/* GENRE 4A v2 — Gossip / NPC Text / Creature Text orphan cleanup     */
/* TrinityCore Midnight 12.x (TWW 11.1.7)                            */
/*                                                                    */
/* Targets:                                                           */
/*   A) gossip_menu     → zero TextID pointing to missing npc_text    */
/*   B) gossip_menu_option → zero ActionMenuID / ActionPoiID refs     */
/*   C) npc_text        → zero BroadcastTextID* missing from hotfixes */
/*   D) creature_text   → zero invalid Broadcast/Sound/Emote/Range   */
/*                                                                    */
/* Safety:                                                            */
/*   - Backup tables created before every mutation                    */
/*   - Session variables saved & restored with COALESCE fallback      */
/*   - Cross-schema lookup: prefers `hotfixes`, falls back to world   */
/*   - Fully self-contained — safe to run standalone in HeidiSQL      */
/*                                                                    */
/* IMPORTANT: Run the COMPLETE file. Do not paste partial fragments.  */
/* ================================================================== */

USE `world`;
SELECT DATABASE() AS active_database;

/* ── Session snapshot (with COALESCE guard for restore) ────────── */
SET @OLD_SQL_SAFE_UPDATES   := COALESCE(@@SQL_SAFE_UPDATES, 1);
SET @OLD_FOREIGN_KEY_CHECKS := COALESCE(@@FOREIGN_KEY_CHECKS, 1);
SET @OLD_UNIQUE_CHECKS      := COALESCE(@@UNIQUE_CHECKS, 1);
SET @OLD_AUTOCOMMIT         := COALESCE(@@AUTOCOMMIT, 1);
SET @OLD_GC_MAX_LEN         := @@SESSION.group_concat_max_len;

SET SQL_SAFE_UPDATES              = 0;
SET FOREIGN_KEY_CHECKS            = 0;
SET UNIQUE_CHECKS                 = 0;
SET AUTOCOMMIT                    = 0;
SET SESSION group_concat_max_len  = 1000000;

START TRANSACTION;

/* ── Counters ────────────────────────────────────────────────────── */
SET @rows_gossip_menu         := 0;
SET @rows_gossip_menu_option  := 0;
SET @rows_npc_text            := 0;
SET @rows_creature_text       := 0;

SET @ver_gm_invalid_textid            := 0;
SET @ver_gmo_invalid_actionmenuid     := 0;
SET @ver_gmo_invalid_actionpoiid      := 0;
SET @ver_npc_invalid_broadcast_refs   := 0;
SET @ver_ct_invalid_broadcast         := 0;
SET @ver_ct_invalid_sound             := 0;
SET @ver_ct_invalid_emote             := 0;
SET @ver_ct_invalid_textrange         := 0;

SET @hotfixes_schema := 'hotfixes';

/* ================================================================== */
/* A) gossip_menu → npc_text                                          */
/* ================================================================== */
SELECT 'SECTION A: gossip_menu invalid TextID' AS section;

SET @has_gossip_menu := (
    SELECT COUNT(*) FROM information_schema.tables
    WHERE table_schema = DATABASE() AND table_name = 'gossip_menu'
);

SET @gm_menu_col := (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'gossip_menu'
      AND LOWER(c.column_name) IN ('menuid','menu_id','id')
    ORDER BY FIELD(LOWER(c.column_name),'menuid','menu_id','id')
    LIMIT 1
);

SET @gm_text_col := (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'gossip_menu'
      AND LOWER(c.column_name) IN ('textid','text_id')
    ORDER BY FIELD(LOWER(c.column_name),'textid','text_id')
    LIMIT 1
);

SET @has_npc_text := (
    SELECT COUNT(*) FROM information_schema.tables
    WHERE table_schema = DATABASE() AND table_name = 'npc_text'
);

SET @npc_pk_col := (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'npc_text'
      AND LOWER(c.column_name) IN ('id','entry')
    ORDER BY FIELD(LOWER(c.column_name),'id','entry')
    LIMIT 1
);

/* A: backup */
SET @sql := IF(
    @has_gossip_menu = 1,
    'CREATE TABLE IF NOT EXISTS `gossip_menu_backup_genre4a` LIKE `gossip_menu`',
    'SELECT ''SKIP: table gossip_menu does not exist.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_gossip_menu = 1 AND @has_npc_text = 1 AND @gm_text_col IS NOT NULL AND @npc_pk_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `gossip_menu_backup_genre4a` ',
        'SELECT gm.* FROM `gossip_menu` gm ',
        'WHERE gm.`', @gm_text_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `npc_text` nt WHERE nt.`', @npc_pk_col, '` = gm.`', @gm_text_col, '`)'
    ),
    'SELECT ''SKIP: gossip_menu backup requires TextID + npc_text PK.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* A: mutate */
SET @sql := IF(
    @has_gossip_menu = 1 AND @has_npc_text = 1 AND @gm_text_col IS NOT NULL AND @npc_pk_col IS NOT NULL,
    CONCAT(
        'UPDATE `gossip_menu` gm ',
        'SET gm.`', @gm_text_col, '` = 0 ',
        'WHERE gm.`', @gm_text_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `npc_text` nt WHERE nt.`', @npc_pk_col, '` = gm.`', @gm_text_col, '`)'
    ),
    'SELECT ''SKIP: gossip_menu update skipped (missing dependency).'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_gossip_menu := @rows_gossip_menu + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* B) gossip_menu_option → ActionMenuID / ActionPoiID                 */
/* ================================================================== */
SELECT 'SECTION B: gossip_menu_option invalid refs' AS section;

SET @has_gmo := (
    SELECT COUNT(*) FROM information_schema.tables
    WHERE table_schema = DATABASE() AND table_name = 'gossip_menu_option'
);

SET @gmo_action_menu_col := (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'gossip_menu_option'
      AND LOWER(c.column_name) IN ('actionmenuid','action_menu_id')
    ORDER BY FIELD(LOWER(c.column_name),'actionmenuid','action_menu_id')
    LIMIT 1
);

SET @gmo_action_poi_col := (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'gossip_menu_option'
      AND LOWER(c.column_name) IN ('actionpoiid','action_poi_id')
    ORDER BY FIELD(LOWER(c.column_name),'actionpoiid','action_poi_id')
    LIMIT 1
);

SET @poi_table := (
    SELECT t.table_name
    FROM information_schema.tables t
    WHERE t.table_schema = DATABASE()
      AND t.table_name IN ('points_of_interest','point_of_interest')
    ORDER BY FIELD(t.table_name,'points_of_interest','point_of_interest')
    LIMIT 1
);

SET @poi_id_col := (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = @poi_table
      AND LOWER(c.column_name) IN ('id','entry')
    ORDER BY FIELD(LOWER(c.column_name),'id','entry')
    LIMIT 1
);

/* B: backup table */
SET @sql := IF(
    @has_gmo = 1,
    'CREATE TABLE IF NOT EXISTS `gossip_menu_option_backup_genre4a` LIKE `gossip_menu_option`',
    'SELECT ''SKIP: table gossip_menu_option does not exist.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* B-1: ActionMenuID backup + update */
SET @sql := IF(
    @has_gmo = 1 AND @has_gossip_menu = 1 AND @gmo_action_menu_col IS NOT NULL AND @gm_menu_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `gossip_menu_option_backup_genre4a` ',
        'SELECT gmo.* FROM `gossip_menu_option` gmo ',
        'WHERE gmo.`', @gmo_action_menu_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `gossip_menu` gm WHERE gm.`', @gm_menu_col, '` = gmo.`', @gmo_action_menu_col, '`)'
    ),
    'SELECT ''SKIP: ActionMenuID backup skipped (missing dependency).'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_gmo = 1 AND @has_gossip_menu = 1 AND @gmo_action_menu_col IS NOT NULL AND @gm_menu_col IS NOT NULL,
    CONCAT(
        'UPDATE `gossip_menu_option` gmo ',
        'SET gmo.`', @gmo_action_menu_col, '` = 0 ',
        'WHERE gmo.`', @gmo_action_menu_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `gossip_menu` gm WHERE gm.`', @gm_menu_col, '` = gmo.`', @gmo_action_menu_col, '`)'
    ),
    'SELECT ''SKIP: ActionMenuID update skipped (missing dependency).'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_gossip_menu_option := @rows_gossip_menu_option + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* B-2: ActionPoiID backup + update */
SET @sql := IF(
    @has_gmo = 1 AND @poi_table IS NOT NULL AND @poi_id_col IS NOT NULL AND @gmo_action_poi_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `gossip_menu_option_backup_genre4a` ',
        'SELECT gmo.* FROM `gossip_menu_option` gmo ',
        'WHERE gmo.`', @gmo_action_poi_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `', @poi_table, '` poi WHERE poi.`', @poi_id_col, '` = gmo.`', @gmo_action_poi_col, '`)'
    ),
    'SELECT ''SKIP: ActionPoiID backup skipped (missing dependency).'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_gmo = 1 AND @poi_table IS NOT NULL AND @poi_id_col IS NOT NULL AND @gmo_action_poi_col IS NOT NULL,
    CONCAT(
        'UPDATE `gossip_menu_option` gmo ',
        'SET gmo.`', @gmo_action_poi_col, '` = 0 ',
        'WHERE gmo.`', @gmo_action_poi_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `', @poi_table, '` poi WHERE poi.`', @poi_id_col, '` = gmo.`', @gmo_action_poi_col, '`)'
    ),
    'SELECT ''SKIP: ActionPoiID update skipped (missing dependency).'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_gossip_menu_option := @rows_gossip_menu_option + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* C) npc_text BroadcastTextID* columns                               */
/* ================================================================== */
SELECT 'SECTION C: npc_text invalid BroadcastTextID refs' AS section;

SET @broadcast_text_schema := (
    SELECT t.table_schema
    FROM information_schema.tables t
    WHERE t.table_name = 'broadcast_text'
      AND t.table_schema IN (DATABASE(), @hotfixes_schema)
    ORDER BY FIELD(t.table_schema, @hotfixes_schema, DATABASE())
    LIMIT 1
);

SET @has_broadcast_text := IF(@broadcast_text_schema IS NULL, 0, 1);

SET @broadcast_text_ref := IF(
    @broadcast_text_schema IS NULL, NULL,
    CONCAT('`', @broadcast_text_schema, '`.`broadcast_text`')
);

SET @bt_pk_col := (
    SELECT c.column_name
    FROM information_schema.columns c
    WHERE c.table_schema = @broadcast_text_schema AND c.table_name = 'broadcast_text'
      AND LOWER(c.column_name) = 'id'
    LIMIT 1
);

SET @npc_bt_cols_count := (
    SELECT COUNT(*)
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'npc_text'
      AND LOWER(c.column_name) REGEXP '^broadcasttextid[0-9]+$'
);

/* Build dynamic WHERE condition across all BroadcastTextID* columns */
SET @npc_invalid_cond := (
    SELECT GROUP_CONCAT(
        CONCAT(
            '(nt.`', c.column_name, '` <> 0 AND NOT EXISTS (',
            'SELECT 1 FROM ', @broadcast_text_ref, ' bt WHERE bt.`', @bt_pk_col, '` = nt.`', c.column_name, '`))'
        )
        ORDER BY c.ordinal_position SEPARATOR ' OR '
    )
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'npc_text'
      AND LOWER(c.column_name) REGEXP '^broadcasttextid[0-9]+$'
);

/* Build dynamic SET expr: zero each invalid BroadcastTextID individually */
SET @npc_set_expr := (
    SELECT GROUP_CONCAT(
        CONCAT(
            'nt.`', c.column_name, '` = IF(nt.`', c.column_name, '` <> 0 AND NOT EXISTS (',
            'SELECT 1 FROM ', @broadcast_text_ref, ' bt WHERE bt.`', @bt_pk_col, '` = nt.`', c.column_name,
            '`), 0, nt.`', c.column_name, '`)'
        )
        ORDER BY c.ordinal_position SEPARATOR ', '
    )
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'npc_text'
      AND LOWER(c.column_name) REGEXP '^broadcasttextid[0-9]+$'
);

/* Build SUM expression for verification */
SET @npc_invalid_sum_expr := (
    SELECT GROUP_CONCAT(
        CONCAT(
            '(nt.`', c.column_name, '` <> 0 AND NOT EXISTS (',
            'SELECT 1 FROM ', @broadcast_text_ref, ' bt WHERE bt.`', @bt_pk_col, '` = nt.`', c.column_name, '`))'
        )
        ORDER BY c.ordinal_position SEPARATOR ' + '
    )
    FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'npc_text'
      AND LOWER(c.column_name) REGEXP '^broadcasttextid[0-9]+$'
);

/* Sanity: if any expression is NULL here, the GROUP_CONCAT failed or deps are missing */
SELECT
    LENGTH(@npc_invalid_cond)    AS cond_len,
    LENGTH(@npc_set_expr)        AS set_len,
    LENGTH(@npc_invalid_sum_expr) AS sum_len,
    IF(@npc_invalid_cond IS NULL AND @npc_bt_cols_count > 0,
       'WARNING: GROUP_CONCAT returned NULL — check group_concat_max_len or broadcast_text deps',
       'OK') AS gc_status;

/* C: backup */
SET @sql := IF(
    @has_npc_text = 1,
    'CREATE TABLE IF NOT EXISTS `npc_text_backup_genre4a` LIKE `npc_text`',
    'SELECT ''SKIP: table npc_text does not exist.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_npc_text = 1 AND @has_broadcast_text = 1 AND @bt_pk_col IS NOT NULL AND @npc_bt_cols_count > 0,
    CONCAT(
        'INSERT IGNORE INTO `npc_text_backup_genre4a` ',
        'SELECT nt.* FROM `npc_text` nt WHERE ', @npc_invalid_cond
    ),
    'SELECT ''SKIP: npc_text backup skipped (missing broadcast_text or BroadcastTextID* columns).'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* C: mutate */
SET @sql := IF(
    @has_npc_text = 1 AND @has_broadcast_text = 1 AND @bt_pk_col IS NOT NULL AND @npc_bt_cols_count > 0,
    CONCAT('UPDATE `npc_text` nt SET ', @npc_set_expr, ' WHERE ', @npc_invalid_cond),
    'SELECT ''SKIP: npc_text update skipped (missing broadcast_text or BroadcastTextID* columns).'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_npc_text := @rows_npc_text + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* D) creature_text — Broadcast / Sound / Emote / TextRange           */
/* ================================================================== */
SELECT 'SECTION D: creature_text invalid refs' AS section;

SET @has_creature_text := (
    SELECT COUNT(*) FROM information_schema.tables
    WHERE table_schema = DATABASE() AND table_name = 'creature_text'
);

SET @ct_bt_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'creature_text'
      AND LOWER(c.column_name) = 'broadcasttextid' LIMIT 1
);
SET @ct_sound_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'creature_text'
      AND LOWER(c.column_name) = 'sound' LIMIT 1
);
SET @ct_emote_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'creature_text'
      AND LOWER(c.column_name) = 'emote' LIMIT 1
);
SET @ct_textrange_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'creature_text'
      AND LOWER(c.column_name) = 'textrange' LIMIT 1
);
SET @ct_textrangemin_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'creature_text'
      AND LOWER(c.column_name) = 'textrangemin' LIMIT 1
);
SET @ct_textrangemax_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = DATABASE() AND c.table_name = 'creature_text'
      AND LOWER(c.column_name) = 'textrangemax' LIMIT 1
);

/* Sound lookup table (hotfixes preferred) */
SET @sound_schema := (
    SELECT t.table_schema FROM information_schema.tables t
    WHERE t.table_name IN ('sound_entries','soundkit','sound_kit')
      AND t.table_schema IN (DATABASE(), @hotfixes_schema)
    ORDER BY FIELD(t.table_schema, @hotfixes_schema, DATABASE()),
             FIELD(t.table_name, 'sound_entries','soundkit','sound_kit')
    LIMIT 1
);
SET @sound_table := (
    SELECT t.table_name FROM information_schema.tables t
    WHERE t.table_name IN ('sound_entries','soundkit','sound_kit')
      AND t.table_schema = @sound_schema
    ORDER BY FIELD(t.table_name,'sound_entries','soundkit','sound_kit')
    LIMIT 1
);
SET @sound_ref := IF(@sound_schema IS NULL OR @sound_table IS NULL, NULL,
    CONCAT('`', @sound_schema, '`.`', @sound_table, '`'));
SET @sound_id_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = @sound_schema AND c.table_name = @sound_table
      AND LOWER(c.column_name) = 'id' LIMIT 1
);

/* Emotes lookup table (hotfixes preferred) */
SET @emotes_schema := (
    SELECT t.table_schema FROM information_schema.tables t
    WHERE t.table_name = 'emotes'
      AND t.table_schema IN (DATABASE(), @hotfixes_schema)
    ORDER BY FIELD(t.table_schema, @hotfixes_schema, DATABASE())
    LIMIT 1
);
SET @has_emotes := IF(@emotes_schema IS NULL, 0, 1);
SET @emotes_ref := IF(@emotes_schema IS NULL, NULL,
    CONCAT('`', @emotes_schema, '`.`emotes`'));
SET @emote_id_col := (
    SELECT c.column_name FROM information_schema.columns c
    WHERE c.table_schema = @emotes_schema AND c.table_name = 'emotes'
      AND LOWER(c.column_name) = 'id' LIMIT 1
);

/* D: backup table */
SET @sql := IF(
    @has_creature_text = 1,
    'CREATE TABLE IF NOT EXISTS `creature_text_backup_genre4a` LIKE `creature_text`',
    'SELECT ''SKIP: table creature_text does not exist.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* D-1: BroadcastTextID */
SET @sql := IF(
    @has_creature_text = 1 AND @has_broadcast_text = 1 AND @ct_bt_col IS NOT NULL AND @bt_pk_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `creature_text_backup_genre4a` ',
        'SELECT ct.* FROM `creature_text` ct WHERE ct.`', @ct_bt_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @broadcast_text_ref, ' bt WHERE bt.`', @bt_pk_col, '` = ct.`', @ct_bt_col, '`)'
    ),
    'SELECT ''SKIP: creature_text BroadcastText backup skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @has_broadcast_text = 1 AND @ct_bt_col IS NOT NULL AND @bt_pk_col IS NOT NULL,
    CONCAT(
        'UPDATE `creature_text` ct SET ct.`', @ct_bt_col, '` = 0 ',
        'WHERE ct.`', @ct_bt_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @broadcast_text_ref, ' bt WHERE bt.`', @bt_pk_col, '` = ct.`', @ct_bt_col, '`)'
    ),
    'SELECT ''SKIP: creature_text BroadcastText update skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_creature_text := @rows_creature_text + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* D-2: Sound */
SET @sql := IF(
    @has_creature_text = 1 AND @ct_sound_col IS NOT NULL AND @sound_table IS NOT NULL AND @sound_id_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `creature_text_backup_genre4a` ',
        'SELECT ct.* FROM `creature_text` ct WHERE ct.`', @ct_sound_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @sound_ref, ' s WHERE s.`', @sound_id_col, '` = ct.`', @ct_sound_col, '`)'
    ),
    'SELECT ''SKIP: creature_text Sound backup skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @ct_sound_col IS NOT NULL AND @sound_table IS NOT NULL AND @sound_id_col IS NOT NULL,
    CONCAT(
        'UPDATE `creature_text` ct SET ct.`', @ct_sound_col, '` = 0 ',
        'WHERE ct.`', @ct_sound_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @sound_ref, ' s WHERE s.`', @sound_id_col, '` = ct.`', @ct_sound_col, '`)'
    ),
    'SELECT ''SKIP: creature_text Sound update skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_creature_text := @rows_creature_text + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* D-3: Emote */
SET @sql := IF(
    @has_creature_text = 1 AND @ct_emote_col IS NOT NULL AND @has_emotes = 1 AND @emote_id_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `creature_text_backup_genre4a` ',
        'SELECT ct.* FROM `creature_text` ct WHERE ct.`', @ct_emote_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @emotes_ref, ' e WHERE e.`', @emote_id_col, '` = ct.`', @ct_emote_col, '`)'
    ),
    'SELECT ''SKIP: creature_text Emote backup skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @ct_emote_col IS NOT NULL AND @has_emotes = 1 AND @emote_id_col IS NOT NULL,
    CONCAT(
        'UPDATE `creature_text` ct SET ct.`', @ct_emote_col, '` = 0 ',
        'WHERE ct.`', @ct_emote_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @emotes_ref, ' e WHERE e.`', @emote_id_col, '` = ct.`', @ct_emote_col, '`)'
    ),
    'SELECT ''SKIP: creature_text Emote update skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_creature_text := @rows_creature_text + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* D-4: TextRange (single column, 0–4 valid) */
SET @sql := IF(
    @has_creature_text = 1 AND @ct_textrange_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `creature_text_backup_genre4a` ',
        'SELECT ct.* FROM `creature_text` ct ',
        'WHERE ct.`', @ct_textrange_col, '` < 0 OR ct.`', @ct_textrange_col, '` > 4'
    ),
    'SELECT ''SKIP: creature_text TextRange backup skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @ct_textrange_col IS NOT NULL,
    CONCAT(
        'UPDATE `creature_text` ct SET ct.`', @ct_textrange_col, '` = 0 ',
        'WHERE ct.`', @ct_textrange_col, '` < 0 OR ct.`', @ct_textrange_col, '` > 4'
    ),
    'SELECT ''SKIP: creature_text TextRange update skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_creature_text := @rows_creature_text + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* D-5: TextRangeMin / TextRangeMax (min<0, max<0, or min>max) */
SET @sql := IF(
    @has_creature_text = 1 AND @ct_textrangemin_col IS NOT NULL AND @ct_textrangemax_col IS NOT NULL,
    CONCAT(
        'INSERT IGNORE INTO `creature_text_backup_genre4a` ',
        'SELECT ct.* FROM `creature_text` ct ',
        'WHERE ct.`', @ct_textrangemin_col, '` < 0 ',
        'OR ct.`', @ct_textrangemax_col, '` < 0 ',
        'OR ct.`', @ct_textrangemin_col, '` > ct.`', @ct_textrangemax_col, '`'
    ),
    'SELECT ''SKIP: creature_text TextRangeMin/Max backup skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @ct_textrangemin_col IS NOT NULL AND @ct_textrangemax_col IS NOT NULL,
    CONCAT(
        'UPDATE `creature_text` ct ',
        'SET ct.`', @ct_textrangemin_col, '` = 0, ct.`', @ct_textrangemax_col, '` = 0 ',
        'WHERE ct.`', @ct_textrangemin_col, '` < 0 ',
        'OR ct.`', @ct_textrangemax_col, '` < 0 ',
        'OR ct.`', @ct_textrangemin_col, '` > ct.`', @ct_textrangemax_col, '`'
    ),
    'SELECT ''SKIP: creature_text TextRangeMin/Max update skipped.'' AS note'
);
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @rows_creature_text := @rows_creature_text + ROW_COUNT();
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* VERIFICATION                                                       */
/* ================================================================== */
SELECT 'VERIFICATION' AS section;

SET @sql := IF(
    @has_gossip_menu = 1 AND @has_npc_text = 1 AND @gm_text_col IS NOT NULL AND @npc_pk_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @ver_gm_invalid_textid FROM `gossip_menu` gm ',
        'WHERE gm.`', @gm_text_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `npc_text` nt WHERE nt.`', @npc_pk_col, '` = gm.`', @gm_text_col, '`)'
    ),
    'SELECT 0 INTO @ver_gm_invalid_textid'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_gmo = 1 AND @has_gossip_menu = 1 AND @gmo_action_menu_col IS NOT NULL AND @gm_menu_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @ver_gmo_invalid_actionmenuid FROM `gossip_menu_option` gmo ',
        'WHERE gmo.`', @gmo_action_menu_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `gossip_menu` gm WHERE gm.`', @gm_menu_col, '` = gmo.`', @gmo_action_menu_col, '`)'
    ),
    'SELECT 0 INTO @ver_gmo_invalid_actionmenuid'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_gmo = 1 AND @gmo_action_poi_col IS NOT NULL AND @poi_table IS NOT NULL AND @poi_id_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @ver_gmo_invalid_actionpoiid FROM `gossip_menu_option` gmo ',
        'WHERE gmo.`', @gmo_action_poi_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM `', @poi_table, '` poi WHERE poi.`', @poi_id_col, '` = gmo.`', @gmo_action_poi_col, '`)'
    ),
    'SELECT 0 INTO @ver_gmo_invalid_actionpoiid'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_npc_text = 1 AND @has_broadcast_text = 1 AND @bt_pk_col IS NOT NULL AND @npc_bt_cols_count > 0,
    CONCAT('SELECT IFNULL(SUM(', @npc_invalid_sum_expr, '),0) INTO @ver_npc_invalid_broadcast_refs FROM `npc_text` nt'),
    'SELECT 0 INTO @ver_npc_invalid_broadcast_refs'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @has_broadcast_text = 1 AND @ct_bt_col IS NOT NULL AND @bt_pk_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @ver_ct_invalid_broadcast FROM `creature_text` ct ',
        'WHERE ct.`', @ct_bt_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @broadcast_text_ref, ' bt WHERE bt.`', @bt_pk_col, '` = ct.`', @ct_bt_col, '`)'
    ),
    'SELECT 0 INTO @ver_ct_invalid_broadcast'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @ct_sound_col IS NOT NULL AND @sound_table IS NOT NULL AND @sound_id_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @ver_ct_invalid_sound FROM `creature_text` ct ',
        'WHERE ct.`', @ct_sound_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @sound_ref, ' s WHERE s.`', @sound_id_col, '` = ct.`', @ct_sound_col, '`)'
    ),
    'SELECT 0 INTO @ver_ct_invalid_sound'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @ct_emote_col IS NOT NULL AND @has_emotes = 1 AND @emote_id_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @ver_ct_invalid_emote FROM `creature_text` ct ',
        'WHERE ct.`', @ct_emote_col, '` <> 0 ',
        'AND NOT EXISTS (SELECT 1 FROM ', @emotes_ref, ' e WHERE e.`', @emote_id_col, '` = ct.`', @ct_emote_col, '`)'
    ),
    'SELECT 0 INTO @ver_ct_invalid_emote'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(
    @has_creature_text = 1 AND @ct_textrange_col IS NOT NULL,
    CONCAT(
        'SELECT COUNT(*) INTO @ver_ct_invalid_textrange FROM `creature_text` ct ',
        'WHERE ct.`', @ct_textrange_col, '` < 0 OR ct.`', @ct_textrange_col, '` > 4'
    ),
    'SELECT 0 INTO @ver_ct_invalid_textrange'
);
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── Results ─────────────────────────────────────────────────────── */
SELECT
    @rows_gossip_menu        AS changed_gossip_menu,
    @rows_gossip_menu_option AS changed_gossip_menu_option,
    @rows_npc_text           AS changed_npc_text,
    @rows_creature_text      AS changed_creature_text;

SELECT
    IFNULL(@ver_gm_invalid_textid, 0)        AS remaining_gm_textid,
    IFNULL(@ver_gmo_invalid_actionmenuid, 0)  AS remaining_gmo_actionmenuid,
    IFNULL(@ver_gmo_invalid_actionpoiid, 0)   AS remaining_gmo_actionpoiid,
    IFNULL(@ver_npc_invalid_broadcast_refs, 0) AS remaining_npc_broadcast,
    IFNULL(@ver_ct_invalid_broadcast, 0)       AS remaining_ct_broadcast,
    IFNULL(@ver_ct_invalid_sound, 0)           AS remaining_ct_sound,
    IFNULL(@ver_ct_invalid_emote, 0)           AS remaining_ct_emote,
    IFNULL(@ver_ct_invalid_textrange, 0)       AS remaining_ct_textrange;

COMMIT;

/* ── Restore session (COALESCE guards against NULL) ──────────────── */
SET SQL_SAFE_UPDATES             = COALESCE(@OLD_SQL_SAFE_UPDATES, 1);
SET FOREIGN_KEY_CHECKS           = COALESCE(@OLD_FOREIGN_KEY_CHECKS, 1);
SET UNIQUE_CHECKS                = COALESCE(@OLD_UNIQUE_CHECKS, 1);
SET AUTOCOMMIT                   = COALESCE(@OLD_AUTOCOMMIT, 1);
SET SESSION group_concat_max_len = COALESCE(@OLD_GC_MAX_LEN, 1024);

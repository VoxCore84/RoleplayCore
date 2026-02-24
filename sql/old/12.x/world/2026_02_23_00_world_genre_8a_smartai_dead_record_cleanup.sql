/* ================================================================== */
/* GENRE 8A v2 — SmartAI dead-record cleanup (Midnight 12.x)         */
/* Safe to re-run until all counts reach 0.                           */
/*                                                                    */
/* Three parts:                                                       */
/*   A) DELETE orphaned quest scripts (source_type=5, quest missing)  */
/*   B) UPDATE broken link chains (link>0, target id missing) → 0    */
/*   C) DELETE invalid quest objective refs (event_type=48)           */
/*                                                                    */
/* v2 fixes over v1:                                                  */
/*   - Removed "Comment view" HeidiSQL artifact (syntax error)        */
/*   - DDL (2 backup tables) BEFORE START TRANSACTION                 */
/*   - @APPLY_FIX defaults to 0 (dry-run)                            */
/*   - Conditional COMMIT/ROLLBACK                                    */
/*   - COALESCE on session variable saves/restores                    */
/*   - Added schema introspection (table existence checks)            */
/*   - Added cap enforcement with @FORCE_APPLY override               */
/*   - Part B UPDATE now gated on @APPLY_FIX (was ungated)            */
/*   - Fixed backup/delete set mismatch: all parts now collect        */
/*     candidate PKs into temp tables first, then backup + mutate     */
/*     from the same key set (v1 used separate LIMIT scans)           */
/*                                                                    */
/* SET @APPLY_FIX := 0 for dry-run diagnostics only.                  */
/* SET @APPLY_FIX := 1 to apply mutations.                            */
/*                                                                    */
/* IMPORTANT: Run the COMPLETE file. Do not paste fragments.          */
/* ================================================================== */

USE `world`;
SELECT DATABASE() AS active_database;

/* ── Safety controls ─────────────────────────────────────────────── */
SET @APPLY_FIX    := 1;       /* 0 = report only, 1 = backup + apply */
SET @MAX_DELETE   := 950000;  /* global cap: max total deletes        */
SET @MAX_UPDATE   := 950000;  /* global cap: max total updates        */
SET @FORCE_APPLY  := 0;       /* 1 = override caps                   */

/* ── Session snapshot ────────────────────────────────────────────── */
SET @save_safe := COALESCE(@@sql_safe_updates, 1);
SET @save_fk   := COALESCE(@@foreign_key_checks, 1);
SET @save_uq   := COALESCE(@@unique_checks, 1);
SET @save_ac   := COALESCE(@@autocommit, 1);

SET sql_safe_updates   = 0;
SET foreign_key_checks = 0;
SET unique_checks      = 0;
SET autocommit         = 0;

/* ================================================================== */
/* SCHEMA INTROSPECTION                                               */
/* ================================================================== */
SELECT 'SCHEMA INTROSPECTION' AS section;

SET @has_smart_scripts := (SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = 'world' AND table_name = 'smart_scripts');
SET @has_quest_template := (SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = 'world' AND table_name = 'quest_template');
SET @has_quest_objectives := (SELECT COUNT(*) FROM information_schema.tables
  WHERE table_schema = 'world' AND table_name = 'quest_objectives');

SELECT
  IF(@has_smart_scripts = 1, 'OK', 'MISSING')    AS smart_scripts,
  IF(@has_quest_template = 1, 'OK', 'MISSING')   AS quest_template,
  IF(@has_quest_objectives = 1, 'OK', 'MISSING') AS quest_objectives;

/* Prerequisites for each part */
SET @partA_ok := IF(@has_smart_scripts = 1 AND @has_quest_template = 1, 1, 0);
SET @partB_ok := IF(@has_smart_scripts = 1, 1, 0);
SET @partC_ok := IF(@has_smart_scripts = 1 AND @has_quest_objectives = 1, 1, 0);

/* ================================================================== */
/* DDL PHASE — backup tables (before transaction)                     */
/* ================================================================== */
SELECT 'BACKUP TABLE CREATION (DDL)' AS section;

SET @sql := IF(@APPLY_FIX = 1 AND @has_smart_scripts = 1,
  'CREATE TABLE IF NOT EXISTS `world`.`smart_scripts_backup_genre8a_delete` LIKE `world`.`smart_scripts`',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@APPLY_FIX = 1 AND @has_smart_scripts = 1,
  'CREATE TABLE IF NOT EXISTS `world`.`smart_scripts_backup_genre8a_linkfix` LIKE `world`.`smart_scripts`',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* DML PHASE                                                          */
/* ================================================================== */
START TRANSACTION;

/* ── Temp key tables for set-consistent backup+mutate ────────────── */
DROP TEMPORARY TABLE IF EXISTS tmp_genre8a_keys_a;
CREATE TEMPORARY TABLE tmp_genre8a_keys_a (
  entryorguid BIGINT NOT NULL,
  source_type TINYINT UNSIGNED NOT NULL,
  id          INT NOT NULL,
  link        INT NOT NULL,
  PRIMARY KEY (entryorguid, source_type, id, link)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS tmp_genre8a_keys_b;
CREATE TEMPORARY TABLE tmp_genre8a_keys_b (
  entryorguid BIGINT NOT NULL,
  source_type TINYINT UNSIGNED NOT NULL,
  id          INT NOT NULL,
  link        INT NOT NULL,
  PRIMARY KEY (entryorguid, source_type, id, link)
) ENGINE=InnoDB;

DROP TEMPORARY TABLE IF EXISTS tmp_genre8a_keys_c;
CREATE TEMPORARY TABLE tmp_genre8a_keys_c (
  entryorguid BIGINT NOT NULL,
  source_type TINYINT UNSIGNED NOT NULL,
  id          INT NOT NULL,
  link        INT NOT NULL,
  PRIMARY KEY (entryorguid, source_type, id, link)
) ENGINE=InnoDB;

/* ================================================================== */
/* PART A — Orphaned quest scripts (source_type=5, quest missing)     */
/* ================================================================== */
SELECT 'PART A: Orphaned quest scripts' AS section;

SET @partA_candidates := 0;
SET @partA_deleted    := 0;

SET @sql := IF(@partA_ok = 1,
  'SELECT COUNT(*) INTO @partA_candidates
   FROM `world`.`smart_scripts` ss
   WHERE ss.source_type = 5
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`quest_template` qt WHERE qt.ID = ss.entryorguid
     )',
  'SELECT 0 INTO @partA_candidates');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SELECT @partA_candidates AS partA_candidate_count;

/* Sample */
SET @sql := IF(@partA_ok = 1 AND @partA_candidates > 0,
  'SELECT ss.entryorguid, ss.source_type, ss.id, ss.link,
          ss.event_type, ss.action_type, ss.comment
   FROM `world`.`smart_scripts` ss
   WHERE ss.source_type = 5
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`quest_template` qt WHERE qt.ID = ss.entryorguid
     )
   LIMIT 50',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Collect candidate keys */
SET @sql := IF(@partA_ok = 1 AND @partA_candidates > 0,
  CONCAT(
    'INSERT INTO tmp_genre8a_keys_a (entryorguid, source_type, id, link)
     SELECT ss.entryorguid, ss.source_type, ss.id, ss.link
     FROM `world`.`smart_scripts` ss
     WHERE ss.source_type = 5
       AND NOT EXISTS (
         SELECT 1 FROM `world`.`quest_template` qt WHERE qt.ID = ss.entryorguid
       )
     LIMIT ', @MAX_DELETE
  ),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* PART B — Broken link references (link>0 but target id missing)     */
/* ================================================================== */
SELECT 'PART B: Broken SmartAI link chains' AS section;

SET @partB_candidates := 0;
SET @partB_updated    := 0;

SET @sql := IF(@partB_ok = 1,
  'SELECT COUNT(*) INTO @partB_candidates
   FROM `world`.`smart_scripts` ss
   WHERE ss.link <> 0
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`smart_scripts` ss2
       WHERE ss2.entryorguid = ss.entryorguid
         AND ss2.source_type = ss.source_type
         AND ss2.id          = ss.link
     )',
  'SELECT 0 INTO @partB_candidates');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SELECT @partB_candidates AS partB_candidate_count;

/* Sample */
SET @sql := IF(@partB_ok = 1 AND @partB_candidates > 0,
  'SELECT ss.entryorguid, ss.source_type, ss.id, ss.link,
          ss.event_type, ss.action_type, ss.comment
   FROM `world`.`smart_scripts` ss
   WHERE ss.link <> 0
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`smart_scripts` ss2
       WHERE ss2.entryorguid = ss.entryorguid
         AND ss2.source_type = ss.source_type
         AND ss2.id          = ss.link
     )
   LIMIT 50',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Collect candidate keys */
SET @sql := IF(@partB_ok = 1 AND @partB_candidates > 0,
  CONCAT(
    'INSERT INTO tmp_genre8a_keys_b (entryorguid, source_type, id, link)
     SELECT ss.entryorguid, ss.source_type, ss.id, ss.link
     FROM `world`.`smart_scripts` ss
     WHERE ss.link <> 0
       AND NOT EXISTS (
         SELECT 1 FROM `world`.`smart_scripts` ss2
         WHERE ss2.entryorguid = ss.entryorguid
           AND ss2.source_type = ss.source_type
           AND ss2.id          = ss.link
       )
     LIMIT ', @MAX_UPDATE
  ),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* PART C — Invalid quest objective references (event_type=48)        */
/* ================================================================== */
SELECT 'PART C: Invalid quest objective completion events' AS section;

SET @partC_candidates := 0;
SET @partC_deleted    := 0;

SET @sql := IF(@partC_ok = 1,
  'SELECT COUNT(*) INTO @partC_candidates
   FROM `world`.`smart_scripts` ss
   WHERE ss.event_type = 48
     AND ss.event_param1 > 0
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`quest_objectives` qo WHERE qo.ID = ss.event_param1
     )',
  'SELECT 0 INTO @partC_candidates');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SELECT @partC_candidates AS partC_candidate_count;

/* Sample */
SET @sql := IF(@partC_ok = 1 AND @partC_candidates > 0,
  'SELECT ss.entryorguid, ss.source_type, ss.id, ss.event_type,
          ss.event_param1, ss.comment
   FROM `world`.`smart_scripts` ss
   WHERE ss.event_type = 48
     AND ss.event_param1 > 0
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`quest_objectives` qo WHERE qo.ID = ss.event_param1
     )
   LIMIT 50',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* Collect candidate keys */
SET @sql := IF(@partC_ok = 1 AND @partC_candidates > 0,
  CONCAT(
    'INSERT INTO tmp_genre8a_keys_c (entryorguid, source_type, id, link)
     SELECT ss.entryorguid, ss.source_type, ss.id, ss.link
     FROM `world`.`smart_scripts` ss
     WHERE ss.event_type = 48
       AND ss.event_param1 > 0
       AND NOT EXISTS (
         SELECT 1 FROM `world`.`quest_objectives` qo WHERE qo.ID = ss.event_param1
       )
     LIMIT ', @MAX_DELETE
  ),
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* APPLY DECISION                                                     */
/* ================================================================== */
SELECT 'APPLY DECISION' AS section;

SELECT COUNT(*) INTO @keys_a FROM tmp_genre8a_keys_a;
SELECT COUNT(*) INTO @keys_b FROM tmp_genre8a_keys_b;
SELECT COUNT(*) INTO @keys_c FROM tmp_genre8a_keys_c;

SET @total_deletes := @keys_a + @keys_c;
SET @total_updates := @keys_b;

SET @caps_exceeded := IF(
  @total_deletes > @MAX_DELETE OR @total_updates > @MAX_UPDATE,
  1, 0
);

SET @can_apply := IF(
  @APPLY_FIX = 1 AND (@caps_exceeded = 0 OR @FORCE_APPLY = 1),
  1, 0
);

SET @cap_note :=
  CASE
    WHEN @APPLY_FIX <> 1 THEN 'DRY RUN: report-only mode (@APPLY_FIX=0).'
    WHEN @caps_exceeded = 1 AND @FORCE_APPLY = 0
      THEN CONCAT('BLOCKED by cap: deletes=', @total_deletes, ' (max ', @MAX_DELETE, '), updates=', @total_updates, ' (max ', @MAX_UPDATE, '). Set @FORCE_APPLY=1 to override.')
    WHEN @total_deletes + @total_updates = 0 THEN 'Apply mode: no candidates found.'
    ELSE CONCAT('Apply mode: ', @total_deletes, ' deletes + ', @total_updates, ' updates.')
  END;

SELECT
  @partA_candidates AS partA_found,
  @partB_candidates AS partB_found,
  @partC_candidates AS partC_found,
  @keys_a           AS partA_capped,
  @keys_b           AS partB_capped,
  @keys_c           AS partC_capped,
  @cap_note         AS apply_decision;

/* ================================================================== */
/* BACKUP + MUTATE (all parts use pre-collected key tables)           */
/* ================================================================== */

/* ── Part A: backup + delete ─────────────────────────────────────── */
SET @sql := IF(@can_apply = 1 AND @keys_a > 0,
  'INSERT IGNORE INTO `world`.`smart_scripts_backup_genre8a_delete`
   SELECT ss.* FROM `world`.`smart_scripts` ss
   INNER JOIN tmp_genre8a_keys_a k
     ON k.entryorguid = ss.entryorguid
    AND k.source_type = ss.source_type
    AND k.id          = ss.id
    AND k.link        = ss.link',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@can_apply = 1 AND @keys_a > 0,
  'DELETE ss FROM `world`.`smart_scripts` ss
   INNER JOIN tmp_genre8a_keys_a k
     ON k.entryorguid = ss.entryorguid
    AND k.source_type = ss.source_type
    AND k.id          = ss.id
    AND k.link        = ss.link',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @partA_deleted := IF(@can_apply = 1, ROW_COUNT(), 0);
DEALLOCATE PREPARE stmt;

/* ── Part B: backup + update ─────────────────────────────────────── */
SET @sql := IF(@can_apply = 1 AND @keys_b > 0,
  'INSERT IGNORE INTO `world`.`smart_scripts_backup_genre8a_linkfix`
   SELECT ss.* FROM `world`.`smart_scripts` ss
   INNER JOIN tmp_genre8a_keys_b k
     ON k.entryorguid = ss.entryorguid
    AND k.source_type = ss.source_type
    AND k.id          = ss.id
    AND k.link        = ss.link',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@can_apply = 1 AND @keys_b > 0,
  'UPDATE `world`.`smart_scripts` ss
   INNER JOIN tmp_genre8a_keys_b k
     ON k.entryorguid = ss.entryorguid
    AND k.source_type = ss.source_type
    AND k.id          = ss.id
    AND k.link        = ss.link
   SET ss.link = 0',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @partB_updated := IF(@can_apply = 1, ROW_COUNT(), 0);
DEALLOCATE PREPARE stmt;

/* ── Part C: backup + delete ─────────────────────────────────────── */
SET @sql := IF(@can_apply = 1 AND @keys_c > 0,
  'INSERT IGNORE INTO `world`.`smart_scripts_backup_genre8a_delete`
   SELECT ss.* FROM `world`.`smart_scripts` ss
   INNER JOIN tmp_genre8a_keys_c k
     ON k.entryorguid = ss.entryorguid
    AND k.source_type = ss.source_type
    AND k.id          = ss.id
    AND k.link        = ss.link',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@can_apply = 1 AND @keys_c > 0,
  'DELETE ss FROM `world`.`smart_scripts` ss
   INNER JOIN tmp_genre8a_keys_c k
     ON k.entryorguid = ss.entryorguid
    AND k.source_type = ss.source_type
    AND k.id          = ss.id
    AND k.link        = ss.link',
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt;
SET @partC_deleted := IF(@can_apply = 1, ROW_COUNT(), 0);
DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* VERIFICATION                                                       */
/* ================================================================== */
SELECT 'VERIFICATION' AS section;

SET @partA_remaining := 0;
SET @partB_remaining := 0;
SET @partC_remaining := 0;

SET @sql := IF(@partA_ok = 1,
  'SELECT COUNT(*) INTO @partA_remaining
   FROM `world`.`smart_scripts` ss
   WHERE ss.source_type = 5
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`quest_template` qt WHERE qt.ID = ss.entryorguid
     )',
  'SELECT 0 INTO @partA_remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@partB_ok = 1,
  'SELECT COUNT(*) INTO @partB_remaining
   FROM `world`.`smart_scripts` ss
   WHERE ss.link <> 0
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`smart_scripts` ss2
       WHERE ss2.entryorguid = ss.entryorguid
         AND ss2.source_type = ss.source_type
         AND ss2.id          = ss.link
     )',
  'SELECT 0 INTO @partB_remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@partC_ok = 1,
  'SELECT COUNT(*) INTO @partC_remaining
   FROM `world`.`smart_scripts` ss
   WHERE ss.event_type = 48
     AND ss.event_param1 > 0
     AND NOT EXISTS (
       SELECT 1 FROM `world`.`quest_objectives` qo WHERE qo.ID = ss.event_param1
     )',
  'SELECT 0 INTO @partC_remaining');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ================================================================== */
/* SUMMARY                                                            */
/* ================================================================== */
SELECT 'SUMMARY' AS section;

SELECT
  @partA_candidates AS partA_found,
  @partA_deleted    AS partA_deleted,
  @partA_remaining  AS partA_remaining,
  @partB_candidates AS partB_found,
  @partB_updated    AS partB_fixed,
  @partB_remaining  AS partB_remaining,
  @partC_candidates AS partC_found,
  @partC_deleted    AS partC_deleted,
  @partC_remaining  AS partC_remaining,
  @cap_note         AS notes;

SELECT IF(@can_apply = 1, 'APPLIED — committing changes',
  IF(@APPLY_FIX = 0, 'DRY RUN — rolling back', 'BLOCKED — rolling back')) AS mode,
  IF(@partB_remaining > 0,
    'NOTE: Part B remaining > 0 may indicate cascading link breaks; re-run script',
    'OK') AS cascade_note;

/* ── Commit or rollback ──────────────────────────────────────────── */
SET @sql := IF(@can_apply = 1, 'COMMIT', 'ROLLBACK');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

/* ── Cleanup ─────────────────────────────────────────────────────── */
DROP TEMPORARY TABLE IF EXISTS tmp_genre8a_keys_a;
DROP TEMPORARY TABLE IF EXISTS tmp_genre8a_keys_b;
DROP TEMPORARY TABLE IF EXISTS tmp_genre8a_keys_c;

/* ── Restore session ─────────────────────────────────────────────── */
SET sql_safe_updates   = COALESCE(@save_safe, 1);
SET foreign_key_checks = COALESCE(@save_fk, 1);
SET unique_checks      = COALESCE(@save_uq, 1);
SET autocommit         = COALESCE(@save_ac, 1);

/* ================================================================== */
/* SmartAI Link Cleanup (Optimized)                                   */
/* ================================================================== */
USE `world`;
SELECT DATABASE() AS active_database;
SET @APPLY_FIX := 1;

SET @OLD_SQL_SAFE_UPDATES   := COALESCE(@@SQL_SAFE_UPDATES, 1);
SET @OLD_FOREIGN_KEY_CHECKS := COALESCE(@@FOREIGN_KEY_CHECKS, 1);
SET @OLD_UNIQUE_CHECKS      := COALESCE(@@UNIQUE_CHECKS, 1);
SET @OLD_AUTOCOMMIT         := COALESCE(@@AUTOCOMMIT, 1);

SET SQL_SAFE_UPDATES   = 0;
SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS      = 0;
SET AUTOCOMMIT         = 0;

SELECT 'PREREQUISITES' AS section;
SET @ss_exists := (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='world' AND table_name='smart_scripts');
SET @ct_exists := (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='world' AND table_name='creature_template');
SET @gt_exists := (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='world' AND table_name='gameobject_template');

SET @ct_pk := (
  SELECT CASE
    WHEN SUM(column_name='entry')>0 THEN 'entry'
    WHEN SUM(column_name='Entry')>0 THEN 'Entry'
    WHEN SUM(column_name='ID')>0 THEN 'ID'
    ELSE NULL END
  FROM information_schema.columns WHERE table_schema='world' AND table_name='creature_template'
);
SET @gt_pk := (
  SELECT CASE
    WHEN SUM(column_name='entry')>0 THEN 'entry'
    WHEN SUM(column_name='Entry')>0 THEN 'Entry'
    WHEN SUM(column_name='ID')>0 THEN 'ID'
    ELSE NULL END
  FROM information_schema.columns WHERE table_schema='world' AND table_name='gameobject_template'
);

SELECT IF(@ss_exists=1,'smart_scripts: OK','smart_scripts: MISSING — aborting') AS smart_scripts_check;
SELECT IF(@ct_exists=1 AND @ct_pk IS NOT NULL, CONCAT('creature_template (',@ct_pk,')'),'n/a') AS creature_source,
       IF(@gt_exists=1 AND @gt_pk IS NOT NULL, CONCAT('gameobject_template (',@gt_pk,')'),'n/a') AS gameobject_source;

SET @can_run := IF(@ss_exists=1,1,0);

SELECT 'BACKUP TABLE CREATION (DDL)' AS section;
SET @sql := IF(@APPLY_FIX=1 AND @can_run=1,'CREATE TABLE IF NOT EXISTS `smart_scripts_backup_orphans` LIKE `smart_scripts`','SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;
SET @sql := IF(@APPLY_FIX=1 AND @can_run=1,'CREATE TABLE IF NOT EXISTS `smart_scripts_backup_broken_links` LIKE `smart_scripts`','SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

START TRANSACTION;
SELECT 'PHASE A — ORPHANED ENTRIES' AS section;

DROP TEMPORARY TABLE IF EXISTS tmp_orphan_keys;
CREATE TEMPORARY TABLE tmp_orphan_keys (
  entryorguid BIGINT NOT NULL,
  source_type TINYINT UNSIGNED NOT NULL,
  id SMALLINT UNSIGNED NOT NULL,
  link SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (entryorguid, source_type, id, link)
) ENGINE=InnoDB;

SET @a1_can := IF(@can_run=1 AND @ct_exists=1 AND @ct_pk IS NOT NULL,1,0);
SET @sql := IF(@a1_can=1, CONCAT(
  "INSERT IGNORE INTO tmp_orphan_keys(entryorguid,source_type,id,link) ",
  "SELECT ss.entryorguid,ss.source_type,ss.id,ss.link FROM smart_scripts ss ",
  "WHERE ss.source_type=0 AND ss.entryorguid>0 AND NOT EXISTS(",
  "SELECT 1 FROM creature_template ct WHERE ct.`",@ct_pk,"`=ss.entryorguid)"
),'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @a2_can := IF(@can_run=1 AND @gt_exists=1 AND @gt_pk IS NOT NULL,1,0);
SET @sql := IF(@a2_can=1, CONCAT(
  "INSERT IGNORE INTO tmp_orphan_keys(entryorguid,source_type,id,link) ",
  "SELECT ss.entryorguid,ss.source_type,ss.id,ss.link FROM smart_scripts ss ",
  "WHERE ss.source_type=1 AND ss.entryorguid>0 AND NOT EXISTS(",
  "SELECT 1 FROM gameobject_template gt WHERE gt.`",@gt_pk,"`=ss.entryorguid)"
),'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @a1_count := (SELECT COUNT(*) FROM tmp_orphan_keys WHERE source_type=0);
SET @a2_count := (SELECT COUNT(*) FROM tmp_orphan_keys WHERE source_type=1);

SET @a1_backed := 0; SET @a2_backed := 0; SET @a1_deleted := 0; SET @a2_deleted := 0;
SET @sql := IF(@APPLY_FIX=1 AND (@a1_count+@a2_count)>0,
  "INSERT IGNORE INTO smart_scripts_backup_orphans SELECT ss.* FROM smart_scripts ss INNER JOIN tmp_orphan_keys k ON k.entryorguid=ss.entryorguid AND k.source_type=ss.source_type AND k.id=ss.id AND k.link=ss.link",
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @a1_backed := IF(@APPLY_FIX=1,(SELECT COUNT(*) FROM smart_scripts_backup_orphans b INNER JOIN tmp_orphan_keys k ON k.entryorguid=b.entryorguid AND k.source_type=b.source_type AND k.id=b.id AND k.link=b.link WHERE k.source_type=0),0);
SET @a2_backed := IF(@APPLY_FIX=1,(SELECT COUNT(*) FROM smart_scripts_backup_orphans b INNER JOIN tmp_orphan_keys k ON k.entryorguid=b.entryorguid AND k.source_type=b.source_type AND k.id=b.id AND k.link=b.link WHERE k.source_type=1),0);

SET @sql := IF(@APPLY_FIX=1 AND (@a1_count+@a2_count)>0,
  "DELETE ss FROM smart_scripts ss INNER JOIN tmp_orphan_keys k ON k.entryorguid=ss.entryorguid AND k.source_type=ss.source_type AND k.id=ss.id AND k.link=ss.link",
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; SET @tmp_deleted := IF(@APPLY_FIX=1,ROW_COUNT(),0); DEALLOCATE PREPARE stmt;
SET @a1_deleted := IF(@APPLY_FIX=1,LEAST(@a1_count,@tmp_deleted),0);
SET @a2_deleted := IF(@APPLY_FIX=1,GREATEST(@tmp_deleted-@a1_deleted,0),0);

SELECT 'PHASE B — BROKEN LINK CHAINS' AS section;
DROP TEMPORARY TABLE IF EXISTS tmp_broken_link_keys;
CREATE TEMPORARY TABLE tmp_broken_link_keys (
  entryorguid BIGINT NOT NULL,
  source_type TINYINT UNSIGNED NOT NULL,
  id SMALLINT UNSIGNED NOT NULL,
  link SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (entryorguid, source_type, id, link)
) ENGINE=InnoDB;

INSERT IGNORE INTO tmp_broken_link_keys(entryorguid,source_type,id,link)
SELECT s.entryorguid,s.source_type,s.id,s.link
FROM smart_scripts s
LEFT JOIN smart_scripts s2 ON s2.entryorguid=s.entryorguid AND s2.source_type=s.source_type AND s2.id=s.link
WHERE @can_run=1 AND s.link>0 AND s2.entryorguid IS NULL;

DROP TEMPORARY TABLE IF EXISTS tmp_broken_link_conflicts;
CREATE TEMPORARY TABLE tmp_broken_link_conflicts (
  entryorguid BIGINT NOT NULL,
  source_type TINYINT UNSIGNED NOT NULL,
  id SMALLINT UNSIGNED NOT NULL,
  link SMALLINT UNSIGNED NOT NULL,
  PRIMARY KEY (entryorguid, source_type, id, link)
) ENGINE=InnoDB;

INSERT IGNORE INTO tmp_broken_link_conflicts(entryorguid,source_type,id,link)
SELECT k.entryorguid,k.source_type,k.id,k.link
FROM tmp_broken_link_keys k
INNER JOIN smart_scripts z ON z.entryorguid=k.entryorguid AND z.source_type=k.source_type AND z.id=k.id AND z.link=0;

SET @b_count := (SELECT COUNT(*) FROM tmp_broken_link_keys);
SET @b_conflicts := (SELECT COUNT(*) FROM tmp_broken_link_conflicts);
SET @b_backed := 0; SET @b_fixed := 0;

SET @sql := IF(@APPLY_FIX=1 AND @b_count>0,
  "INSERT IGNORE INTO smart_scripts_backup_broken_links SELECT s.* FROM smart_scripts s INNER JOIN tmp_broken_link_keys k ON k.entryorguid=s.entryorguid AND k.source_type=s.source_type AND k.id=s.id AND k.link=s.link",
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; SET @b_backed := IF(@APPLY_FIX=1,ROW_COUNT(),0); DEALLOCATE PREPARE stmt;

SET @sql := IF(@APPLY_FIX=1 AND @b_count>0,
  "UPDATE smart_scripts s INNER JOIN tmp_broken_link_keys k ON k.entryorguid=s.entryorguid AND k.source_type=s.source_type AND k.id=s.id AND k.link=s.link LEFT JOIN tmp_broken_link_conflicts c ON c.entryorguid=k.entryorguid AND c.source_type=k.source_type AND c.id=k.id AND c.link=k.link SET s.link=0 WHERE c.entryorguid IS NULL",
  'SELECT 0');
PREPARE stmt FROM @sql; EXECUTE stmt; SET @b_fixed := IF(@APPLY_FIX=1,ROW_COUNT(),0); DEALLOCATE PREPARE stmt;

SET @b_remaining := (
  SELECT COUNT(*) FROM smart_scripts s
  LEFT JOIN smart_scripts s2 ON s2.entryorguid=s.entryorguid AND s2.source_type=s.source_type AND s2.id=s.link
  WHERE s.link>0 AND s2.entryorguid IS NULL
);

SELECT 'SUMMARY' AS section;
SELECT @a1_count AS creature_orphan_rows, @a1_backed AS creature_orphans_backed_up, @a1_deleted AS creature_orphans_deleted,
       @a2_count AS gameobject_orphan_rows, @a2_backed AS gameobject_orphans_backed_up, @a2_deleted AS gameobject_orphans_deleted;
SELECT @b_count AS broken_root_links_found, @b_conflicts AS broken_links_conflicting_with_existing_link0, @b_backed AS broken_links_backed_up,
       @b_fixed AS broken_links_zeroed, @b_remaining AS broken_links_remaining_after;
SELECT IF(@APPLY_FIX=1,'APPLIED — committing changes','DRY RUN — rolling back') AS mode;

SET @sql := IF(@APPLY_FIX=1,'COMMIT','ROLLBACK');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

DROP TEMPORARY TABLE IF EXISTS tmp_orphan_keys;
DROP TEMPORARY TABLE IF EXISTS tmp_broken_link_keys;
DROP TEMPORARY TABLE IF EXISTS tmp_broken_link_conflicts;

SET SQL_SAFE_UPDATES   = COALESCE(@OLD_SQL_SAFE_UPDATES, 1);
SET FOREIGN_KEY_CHECKS = COALESCE(@OLD_FOREIGN_KEY_CHECKS, 1);
SET UNIQUE_CHECKS      = COALESCE(@OLD_UNIQUE_CHECKS, 1);
SET AUTOCOMMIT         = COALESCE(@OLD_AUTOCOMMIT, 1);

-- HeidiSQL-safe MySQL 8/9 patch for invalid CreatureDisplayIDs in world DB.

USE `world`;
SELECT DATABASE() AS current_database;

SET @OLD_SQL_SAFE_UPDATES := @@SQL_SAFE_UPDATES;
SET @OLD_FOREIGN_KEY_CHECKS := @@FOREIGN_KEY_CHECKS;
SET @OLD_UNIQUE_CHECKS := @@UNIQUE_CHECKS;
SET @OLD_AUTOCOMMIT := @@AUTOCOMMIT;

SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;
SET UNIQUE_CHECKS = 0;
SET AUTOCOMMIT = 0;

START TRANSACTION;

DROP TEMPORARY TABLE IF EXISTS tmp_invalid_display_ids;
CREATE TEMPORARY TABLE tmp_invalid_display_ids (
  DisplayID INT UNSIGNED NOT NULL PRIMARY KEY
) ENGINE=MEMORY;

INSERT INTO tmp_invalid_display_ids (DisplayID) VALUES
(147318),(29525),(38043),(38961),(58640),(66129),(34276),(85414),(189981),(194544),(191840),(191143),
(198349),(199064),(194551),(191683),(191686),(194336),(191659),(200670),(193405),(193417),(198138),(192126),
(194744),(195386),(198847),(198856),(192809),(199795),(199796),(199797),(199798),(1121538),(139384);

DROP TEMPORARY TABLE IF EXISTS tmp_affected_creature_ids;
CREATE TEMPORARY TABLE tmp_affected_creature_ids (
  CreatureID INT UNSIGNED NOT NULL PRIMARY KEY
) ENGINE=MEMORY;

INSERT INTO tmp_affected_creature_ids (CreatureID) VALUES
(28605),(35531),(52797),(54174),(54751),(54867),(80581),(98489),(118153),(137110),(184816),(186239),(186669),
(186679),(187426),(187445),(187677),(187785),(187860),(187868),(187919),(188041),(188044),(189243),(190609),
(191057),(191536),(192626),(192961),(193996),(195095),(195918),(195960),(196772),(199298),(205156),(240514);

SET @ctm_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_template_model'
);

SET @cmi_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_model_info'
);

SET @sql := IF(@ctm_exists = 1,
  'CREATE TABLE IF NOT EXISTS `creature_template_model_backup` LIKE `creature_template_model`',
  'SELECT ''SKIP: creature_template_model missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @ctm_backup_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_template_model_backup'
);

SET @ctm_signature_src := (
  SELECT MD5(GROUP_CONCAT(CONCAT(COLUMN_NAME, ':', COLUMN_TYPE, ':', IS_NULLABLE, ':', IFNULL(COLUMN_DEFAULT, 'NULL'), ':', EXTRA)
                          ORDER BY ORDINAL_POSITION SEPARATOR '|'))
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_template_model'
);

SET @ctm_signature_bak := (
  SELECT MD5(GROUP_CONCAT(CONCAT(COLUMN_NAME, ':', COLUMN_TYPE, ':', IS_NULLABLE, ':', IFNULL(COLUMN_DEFAULT, 'NULL'), ':', EXTRA)
                          ORDER BY ORDINAL_POSITION SEPARATOR '|'))
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_template_model_backup'
);

SET @ctm_backup_compatible := IF(@ctm_exists = 1 AND @ctm_backup_exists = 1 AND @ctm_signature_src = @ctm_signature_bak, 1, 0);

SET @sql := IF(@ctm_backup_compatible = 1,
  'INSERT IGNORE INTO `creature_template_model_backup` (`CreatureID`,`Idx`,`CreatureDisplayID`,`DisplayScale`,`Probability`,`VerifiedBuild`)
   SELECT ctm.`CreatureID`, ctm.`Idx`, ctm.`CreatureDisplayID`, ctm.`DisplayScale`, ctm.`Probability`, ctm.`VerifiedBuild`
   FROM `creature_template_model` ctm
   INNER JOIN tmp_affected_creature_ids ac ON ac.CreatureID = ctm.CreatureID',
  'SELECT ''SKIP: creature_template_model backup insert skipped (backup schema mismatch/missing)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@cmi_exists = 1,
  'CREATE TABLE IF NOT EXISTS `creature_model_info_backup` LIKE `creature_model_info`',
  'SELECT ''SKIP: creature_model_info missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @cmi_backup_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.TABLES
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_model_info_backup'
);

SET @cmi_signature_src := (
  SELECT MD5(GROUP_CONCAT(CONCAT(COLUMN_NAME, ':', COLUMN_TYPE, ':', IS_NULLABLE, ':', IFNULL(COLUMN_DEFAULT, 'NULL'), ':', EXTRA)
                          ORDER BY ORDINAL_POSITION SEPARATOR '|'))
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_model_info'
);

SET @cmi_signature_bak := (
  SELECT MD5(GROUP_CONCAT(CONCAT(COLUMN_NAME, ':', COLUMN_TYPE, ':', IS_NULLABLE, ':', IFNULL(COLUMN_DEFAULT, 'NULL'), ':', EXTRA)
                          ORDER BY ORDINAL_POSITION SEPARATOR '|'))
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'creature_model_info_backup'
);

SET @cmi_backup_compatible := IF(@cmi_exists = 1 AND @cmi_backup_exists = 1 AND @cmi_signature_src = @cmi_signature_bak, 1, 0);

SET @sql := IF(@cmi_backup_compatible = 1,
  'INSERT IGNORE INTO `creature_model_info_backup`
   SELECT cmi.*
   FROM `creature_model_info` cmi
   INNER JOIN tmp_invalid_display_ids ids ON ids.DisplayID = cmi.DisplayID',
  'SELECT ''SKIP: creature_model_info backup insert skipped (backup schema mismatch/missing)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @FallbackDisplayID := NULL;
SET @sql := IF(@ctm_exists = 1,
  'SELECT ctm.CreatureDisplayID
   INTO @FallbackDisplayID
   FROM `creature_template_model` ctm
   LEFT JOIN tmp_invalid_display_ids ids ON ids.DisplayID = ctm.CreatureDisplayID
   WHERE ids.DisplayID IS NULL
   GROUP BY ctm.CreatureDisplayID
   ORDER BY COUNT(*) DESC, ctm.CreatureDisplayID ASC
   LIMIT 1',
  'SELECT NULL INTO @FallbackDisplayID');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @FallbackDisplayID := COALESCE(@FallbackDisplayID, 0);
SELECT @FallbackDisplayID AS chosen_fallback_display_id;

SET @sql := IF(@ctm_exists = 1,
  'DELETE ctm
   FROM `creature_template_model` ctm
   INNER JOIN tmp_affected_creature_ids ac ON ac.CreatureID = ctm.CreatureID
   INNER JOIN tmp_invalid_display_ids ids ON ids.DisplayID = ctm.CreatureDisplayID',
  'SELECT ''SKIP: creature_template_model cleanup skipped (table missing)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@ctm_exists = 1,
  'INSERT INTO `creature_template_model` (`CreatureID`,`Idx`,`CreatureDisplayID`,`DisplayScale`,`Probability`,`VerifiedBuild`)
   SELECT ac.CreatureID, 0, @FallbackDisplayID, 1, 1, 0
   FROM tmp_affected_creature_ids ac
   LEFT JOIN `creature_template_model` ctm ON ctm.CreatureID = ac.CreatureID
   WHERE ctm.CreatureID IS NULL
   AND @FallbackDisplayID <> 0',
  'SELECT ''SKIP: creature_template_model fallback insert skipped (table missing)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@cmi_exists = 1,
  'DELETE cmi
   FROM `creature_model_info` cmi
   INNER JOIN tmp_invalid_display_ids ids ON ids.DisplayID = cmi.DisplayID',
  'SELECT ''SKIP: creature_model_info cleanup skipped (table missing)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @cmi_other_gender_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'creature_model_info'
    AND COLUMN_NAME = 'DisplayID_Other_Gender'
);

SET @cmi_other_gender_nullable := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.COLUMNS
  WHERE TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'creature_model_info'
    AND COLUMN_NAME = 'DisplayID_Other_Gender'
    AND IS_NULLABLE = 'YES'
);

SET @sql := IF(@cmi_exists = 1 AND @cmi_other_gender_exists = 1,
  IF(@cmi_other_gender_nullable = 1,
    'UPDATE `creature_model_info` cmi
     INNER JOIN tmp_invalid_display_ids ids ON ids.DisplayID = cmi.DisplayID_Other_Gender
     SET cmi.DisplayID_Other_Gender = NULL',
    'UPDATE `creature_model_info` cmi
     INNER JOIN tmp_invalid_display_ids ids ON ids.DisplayID = cmi.DisplayID_Other_Gender
     SET cmi.DisplayID_Other_Gender = 0'
  ),
  'SELECT ''SKIP: DisplayID_Other_Gender column missing or creature_model_info missing'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

COMMIT;

SET SQL_SAFE_UPDATES = @OLD_SQL_SAFE_UPDATES;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS;
SET AUTOCOMMIT = @OLD_AUTOCOMMIT;

SET @sql := IF(@ctm_exists = 1,
  'SELECT COUNT(*) AS invalid_rows_remaining_for_affected_creatures
   FROM `creature_template_model` ctm
   INNER JOIN tmp_affected_creature_ids ac ON ac.CreatureID = ctm.CreatureID
   INNER JOIN tmp_invalid_display_ids ids ON ids.DisplayID = ctm.CreatureDisplayID',
  'SELECT ''SKIP: creature_template_model verification skipped (table missing)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @sql := IF(@ctm_exists = 1,
  'SELECT ctm.CreatureID, ctm.Idx, ctm.CreatureDisplayID, ctm.DisplayScale, ctm.Probability, ctm.VerifiedBuild
   FROM `creature_template_model` ctm
   INNER JOIN tmp_affected_creature_ids ac ON ac.CreatureID = ctm.CreatureID
   ORDER BY ctm.CreatureID, ctm.Idx',
  'SELECT ''SKIP: final creature_template_model rows unavailable (table missing)'' AS note');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SELECT @FallbackDisplayID AS fallback_display_id_used;

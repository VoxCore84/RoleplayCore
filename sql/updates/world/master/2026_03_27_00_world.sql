--
-- Add size column to creature table (TC upstream: spawn size override)
-- Uses procedure to be idempotent
--
SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='world' AND TABLE_NAME='creature' AND COLUMN_NAME='size');
SET @sql = IF(@col_exists = 0, 'ALTER TABLE `creature` ADD COLUMN `size` float NOT NULL DEFAULT 0 AFTER `StringId`', 'SELECT 1');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

--
-- Add size and visibility columns to gameobject table (TC upstream: spawn overrides)
--
SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='world' AND TABLE_NAME='gameobject' AND COLUMN_NAME='size');
SET @sql = IF(@col_exists = 0, 'ALTER TABLE `gameobject` ADD COLUMN `size` float NOT NULL DEFAULT 0 AFTER `StringId`', 'SELECT 1');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

SET @col_exists = (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='world' AND TABLE_NAME='gameobject' AND COLUMN_NAME='visibility');
SET @sql = IF(@col_exists = 0, 'ALTER TABLE `gameobject` ADD COLUMN `visibility` float NOT NULL DEFAULT 0 AFTER `size`', 'SELECT 1');
PREPARE stmt FROM @sql; EXECUTE stmt; DEALLOCATE PREPARE stmt;

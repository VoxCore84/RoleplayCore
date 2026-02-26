CREATE TABLE IF NOT EXISTS `character_transmog_outfit_situations` (
  `guid` bigint unsigned NOT NULL COMMENT 'Character GUID',
  `setguid` bigint unsigned NOT NULL COMMENT 'Equipment set GUID',
  `situationID` int unsigned NOT NULL DEFAULT '0',
  `specID` int unsigned NOT NULL DEFAULT '0',
  `loadoutID` int unsigned NOT NULL DEFAULT '0',
  `equipmentSetID` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`guid`,`setguid`,`situationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Transmog outfit auto-switch situations';

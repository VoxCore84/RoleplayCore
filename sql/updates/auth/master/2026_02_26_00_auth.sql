CREATE TABLE IF NOT EXISTS `battlenet_transmog_set_favorites` (
  `battlenetAccountId` int unsigned NOT NULL,
  `transmogSetId` int unsigned NOT NULL,
  PRIMARY KEY (`battlenetAccountId`, `transmogSetId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

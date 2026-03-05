-- 2026_03_05_00_hotfixes.sql
-- Remove 363 redundant hotfix rows verified identical to retail DB2 binary data via DBCD cross-reference audit

-- ============================================================================
-- FULLY REDUNDANT TABLES (all rows match retail DB2 — delete all)
-- ============================================================================

-- creature (137 rows — all redundant)
DELETE FROM `creature` WHERE `VerifiedBuild` > 0;
DELETE FROM `hotfix_data` WHERE `TableHash` = 0xC9D6B6B3 AND `RecordId` IN (SELECT `ID` FROM `creature`);

-- azerite_unlock_mapping (65 rows — all redundant)
DELETE FROM `azerite_unlock_mapping` WHERE `VerifiedBuild` > 0;

-- content_tuning (3 rows — all redundant)
DELETE FROM `content_tuning` WHERE `VerifiedBuild` > 0;

-- item_squish_era (2 rows — all redundant)
DELETE FROM `item_squish_era` WHERE `VerifiedBuild` > 0;

-- artifact_power_picker (1 row — all redundant)
DELETE FROM `artifact_power_picker` WHERE `VerifiedBuild` > 0;

-- artifact_quest_xp (1 row — all redundant)
DELETE FROM `artifact_quest_xp` WHERE `VerifiedBuild` > 0;

-- trait_tree_x_trait_cost (1 row — all redundant)
DELETE FROM `trait_tree_x_trait_cost` WHERE `VerifiedBuild` > 0;

-- ============================================================================
-- PARTIALLY REDUNDANT TABLES (only specific IDs match retail DB2)
-- ============================================================================

-- spell_effect (62 of 175 rows redundant)
DELETE FROM `spell_effect` WHERE `ID` IN (
  127395,343726,355675,355845,357832,359136,359455,360583,738673,753424,
  818428,1014783,1024677,1056034,1082444,1082461,1082691,1083147,1092070,1092071,
  1094147,1106780,1119399,1119400,1160701,1160702,1170662,1180344,1180358,1186803,
  1210975,1229111,1229413,1240626,1254949,1264720,1265452,1266631,1273545,1276520,
  1278238,1279168,1283577,1283580,1290447,1290516,1290580,1290585,1295475,1296046,
  1296165,1296190,1298728,1299683,1300817,1301978,1302167,1304684,1304823,1304824,
  1304836,1305701
);

-- spell_item_enchantment (36 of 1181 rows redundant)
DELETE FROM `spell_item_enchantment` WHERE `ID` IN (
  7425,7426,7427,7428,7429,7430,7431,7432,7433,7434,7435,7436,
  7966,7967,7978,7979,7980,7981,7982,7983,
  8006,8007,8008,8009,8010,8011,
  8036,8037,8038,8039,8040,8041,
  8612,8613,8614,8615
);

-- modified_crafting_item (27 of 28 rows redundant)
DELETE FROM `modified_crafting_item` WHERE `ID` IN (
  208564,208565,208566,211878,211879,211880,212318,
  236963,236965,237015,237016,241284,241285,241318,241319,
  242787,243434,243442,243448,244835,244838,244839,244840,244849,
  251993,257751,257752
);

-- location (19 of 58 rows redundant)
DELETE FROM `location` WHERE `ID` IN (
  137054,137073,137076,137101,137107,137108,137110,137112,
  137183,137185,137186,186021,257993,
  274615,274616,274617,274620,525570,525571
);

-- tact_key (7 of 425 rows redundant)
DELETE FROM `tact_key` WHERE `ID` IN (246,7856,7921,7989,7994,8112,8135);

-- light (2 of 5 rows redundant)
DELETE FROM `light` WHERE `ID` IN (8977,13715);

-- ============================================================================
-- CLEANUP: Remove orphaned hotfix_data entries for deleted rows
-- ============================================================================
DELETE hd FROM `hotfix_data` hd
  LEFT JOIN `creature` t ON hd.`RecordId` = t.`ID`
  WHERE hd.`TableHash` = 0xC9D6B6B3 AND t.`ID` IS NULL AND hd.`Status` = 1;

DELETE hd FROM `hotfix_data` hd
  LEFT JOIN `azerite_unlock_mapping` t ON hd.`RecordId` = t.`ID`
  WHERE hd.`TableHash` = 0x699E0ADA AND t.`ID` IS NULL AND hd.`Status` = 1;

DELETE hd FROM `hotfix_data` hd
  LEFT JOIN `content_tuning` t ON hd.`RecordId` = t.`ID`
  WHERE hd.`TableHash` = 0x07D75165 AND t.`ID` IS NULL AND hd.`Status` = 1;

DELETE hd FROM `hotfix_data` hd
  LEFT JOIN `item_squish_era` t ON hd.`RecordId` = t.`ID`
  WHERE hd.`TableHash` = 0xE66E0D0C AND t.`ID` IS NULL AND hd.`Status` = 1;

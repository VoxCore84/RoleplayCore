-- 2026_02_26_01_world.sql
-- Clean up orphaned loot templates, conditions, and creature_text

-- 1. Delete orphaned creature_loot_template entries (4,206 entries / ~134K rows)
--    These loot tables are not referenced by any creature_template_difficulty.LootID,
--    nor used as a reference target by other loot rows or reference_loot_template.
DELETE FROM creature_loot_template
WHERE Entry NOT IN (SELECT LootID FROM (SELECT LootID FROM creature_template_difficulty WHERE LootID > 0) AS sub)
AND Entry NOT IN (SELECT Item FROM (SELECT Item FROM creature_loot_template WHERE ItemType = 1) AS sub2)
AND Entry NOT IN (SELECT Entry FROM (SELECT Entry FROM reference_loot_template) AS sub3);

-- 2. Delete orphaned gameobject_loot_template entries (5,900 entries)
--    These loot tables are not referenced by any gameobject_template.Data1 (chest/fishing/gathering),
--    nor used as a reference target.
DELETE FROM gameobject_loot_template
WHERE Entry NOT IN (SELECT Data1 FROM (SELECT Data1 FROM gameobject_template WHERE type IN (3,25,50) AND Data1 > 0) AS sub)
AND Entry NOT IN (SELECT Item FROM (SELECT Item FROM gameobject_loot_template WHERE ItemType = 1) AS sub2)
AND Entry NOT IN (SELECT Entry FROM (SELECT Entry FROM reference_loot_template) AS sub3);

-- 3. Delete orphaned conditions referencing non-existent creature_loot_template rows (5 rows)
DELETE FROM conditions
WHERE SourceTypeOrReferenceId = 1
AND NOT EXISTS (
    SELECT 1 FROM creature_loot_template clt
    WHERE clt.Entry = conditions.SourceGroup AND clt.Item = conditions.SourceEntry
);

-- 4. Delete creature_text with CreatureID = 0 (15 orphaned Rifleman Middlecamp rows)
DELETE FROM creature_text WHERE CreatureID = 0;

-- 5. UPSTREAM: DH Voidglare Boon spell script
DELETE FROM `spell_script_names` WHERE `ScriptName`='spell_dh_voidglare_boon';
INSERT INTO `spell_script_names` (`spell_id`, `ScriptName`) VALUES
(473728, 'spell_dh_voidglare_boon');

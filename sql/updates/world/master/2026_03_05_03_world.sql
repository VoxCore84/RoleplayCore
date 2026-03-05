-- 2026_03_05_03_world.sql
-- Fix 3 pre-existing AIName data errors found during QA

-- AIName='0' is not a valid AI class name — clear to empty (uses default AI)
UPDATE `creature_template` SET `AIName` = '' WHERE `entry` IN (36955, 37554) AND `AIName` = '0';

-- AIName='CombaAI' is a typo for 'CombatAI'
UPDATE `creature_template` SET `AIName` = 'CombatAI' WHERE `entry` = 134093 AND `AIName` = 'CombaAI';

-- Clean up 8 orphaned GUID-based smart_scripts referencing deleted creature spawns
DELETE FROM `smart_scripts` WHERE `source_type` = 0 AND `entryorguid` IN (-3000090306, -3000090305, -3000090276, -3000090274, -136553, -56281, -456, -455)
AND NOT EXISTS (SELECT 1 FROM `creature` c WHERE c.`guid` = ABS(`entryorguid`));

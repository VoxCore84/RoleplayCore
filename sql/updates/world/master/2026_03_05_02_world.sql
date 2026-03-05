-- 2026_03_05_02_world.sql
-- Fix: restore AIName='SmartAI' for 181 creatures that have GUID-based smart_scripts
-- but no entry-based scripts. The original _01 only checked entry-based scripts;
-- _01 was later patched to include GUID checks for future re-runs, but this corrective
-- SQL was needed to undo the damage from the original application. Idempotent/no-op if
-- _01 already includes the GUID check before first application.

UPDATE `creature_template` ct
SET ct.`AIName` = 'SmartAI'
WHERE ct.`AIName` = ''
AND NOT EXISTS (
    SELECT 1 FROM `smart_scripts` ss
    WHERE ss.`entryorguid` = ct.`entry` AND ss.`source_type` = 0
)
AND EXISTS (
    SELECT 1 FROM `creature` c
    JOIN `smart_scripts` ss ON ss.`entryorguid` = -(CAST(c.`guid` AS SIGNED)) AND ss.`source_type` = 0
    WHERE c.`id` = ct.`entry`
);

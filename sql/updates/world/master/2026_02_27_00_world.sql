-- 2026_02_27_00_world.sql
-- Fix companion creature unit_class values (eliminates 5 boot warnings)

UPDATE `creature_template` SET `unit_class` = 1 WHERE `entry` = 500001; -- Warrior (Tank) - UNIT_CLASS_WARRIOR
UPDATE `creature_template` SET `unit_class` = 4 WHERE `entry` = 500002; -- Rogue (Melee) - UNIT_CLASS_ROGUE
UPDATE `creature_template` SET `unit_class` = 1 WHERE `entry` = 500003; -- Hunter (Ranged) - UNIT_CLASS_WARRIOR
UPDATE `creature_template` SET `unit_class` = 8 WHERE `entry` = 500004; -- Mage (Caster) - UNIT_CLASS_MAGE
UPDATE `creature_template` SET `unit_class` = 2 WHERE `entry` = 500005; -- Priest (Healer) - UNIT_CLASS_PALADIN (mana)

-- UPSTREAM: Priest Evangelism spell scripts and proc
DELETE FROM `spell_script_names` WHERE `ScriptName` IN ('spell_pri_evangelism','spell_pri_power_word_radiance_evangelism');
INSERT INTO `spell_script_names` (`spell_id`,`ScriptName`) VALUES
(472433,'spell_pri_evangelism'),
(194509,'spell_pri_power_word_radiance_evangelism');

DELETE FROM `spell_proc` WHERE `SpellId` IN (472433);
INSERT INTO `spell_proc` (`SpellId`,`SchoolMask`,`SpellFamilyName`,`SpellFamilyMask0`,`SpellFamilyMask1`,`SpellFamilyMask2`,`SpellFamilyMask3`,`ProcFlags`,`ProcFlags2`,`SpellTypeMask`,`SpellPhaseMask`,`HitMask`,`AttributesMask`,`DisableEffectsMask`,`ProcsPerMinute`,`Chance`,`Cooldown`,`Charges`) VALUES
(472433,0x00,6,0x00400000,0x00000000,0x00000000,0x00000000,0x0,0x0,0x0,0x0,0x0,0x10,0x0,0,0,0,0); -- Evangelism

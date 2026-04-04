-- 2026_04_04_08_world.sql
-- Warlock Phase 5 Tier B: Summon spell handlers — creature ScriptNames + spell_script_names

-- Creature ScriptNames for pet AIs
-- IMPORTANT: Clear AIName to prevent SmartAI from overriding C++ ScriptName
UPDATE `creature_template` SET `ScriptName` = 'npc_warl_imp_lord' WHERE `entry` = 258584;
UPDATE `creature_template` SET `ScriptName` = 'npc_warl_vilefiend', `AIName` = '' WHERE `entry` = 135816;
UPDATE `creature_template` SET `ScriptName` = 'npc_warl_doomguard' WHERE `entry` = 250785;
UPDATE `creature_template` SET `ScriptName` = 'npc_warl_infernal', `AIName` = '' WHERE `entry` = 89;

-- Spell script bindings
INSERT INTO `spell_script_names` (`spell_id`, `ScriptName`) VALUES
(267216, 'spell_warl_inner_demons'),
(1276452, 'spell_warl_grimoire_imp_lord'),
(1251778, 'spell_warl_summon_vilefiend');

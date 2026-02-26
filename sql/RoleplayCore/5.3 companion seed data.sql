-- ============================================================================
-- Companion Squad System — Seed Data
-- Run against: world
-- Creates creature_template entries and companion_roster entries
-- creature_template entries use 500000+ range to avoid conflicts
-- ============================================================================

-- Companion creature templates (minimal — ScriptName is the key part)
-- These use entry range 500001-500010 for companion NPCs
-- HealthModifier/DamageModifier live in creature_template_difficulty, not creature_template

INSERT IGNORE INTO `creature_template` (`entry`, `name`, `subname`, `ScriptName`, `faction`, `npcflag`, `unit_flags`, `BaseAttackTime`) VALUES
(500001, 'Companion Warrior',   'Tank',       'CompanionAI', 35, 0, 0, 2000),
(500002, 'Companion Rogue',     'Melee DPS',  'CompanionAI', 35, 0, 0, 2000),
(500003, 'Companion Hunter',    'Ranged DPS', 'CompanionAI', 35, 0, 0, 2000),
(500004, 'Companion Mage',      'Caster DPS', 'CompanionAI', 35, 0, 0, 2000),
(500005, 'Companion Priest',    'Healer',     'CompanionAI', 35, 0, 0, 2000);

-- Difficulty entries for scaling (DifficultyID 0 = normal)
INSERT IGNORE INTO `creature_template_difficulty` (`Entry`, `DifficultyID`, `HealthModifier`, `DamageModifier`) VALUES
(500001, 0, 5.0, 1.0),
(500002, 0, 3.0, 1.5),
(500003, 0, 3.0, 1.2),
(500004, 0, 2.5, 1.3),
(500005, 0, 2.5, 0.5);

-- Roster entries
-- Spells are placeholders — tune via SQL later with real spell IDs
-- spell1 = primary ability, spell2 = secondary, spell3 = utility
REPLACE INTO `companion_roster` (`entry`, `name`, `role`, `spell1`, `spell2`, `spell3`, `cooldown1`, `cooldown2`, `cooldown3`) VALUES
(500001, 'Warrior',  0, 0, 0, 0, 8000, 12000, 15000),   -- Tank
(500002, 'Rogue',    1, 0, 0, 0, 6000, 10000, 15000),    -- Melee
(500003, 'Hunter',   2, 0, 0, 0, 5000, 10000, 15000),    -- Ranged
(500004, 'Mage',     3, 0, 0, 0, 5000, 10000, 15000),    -- Caster
(500005, 'Priest',   4, 0, 0, 0, 6000, 10000, 20000);    -- Healer

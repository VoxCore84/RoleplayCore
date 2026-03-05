-- 2026_03_05_29_world.sql
-- Stormwind ambient NPC scripts — 11 entries, ~377 spawns
-- Adds SmartAI for guards, dock workers, citizens, refugees, children, dracthyr
-- Uses reasoning from existing patterns (Guard 68, Elly Langston 1328, Marcus Jonathan 466)

-- ============================================================
-- 1. Enable SmartAI on all target entries
-- ============================================================
UPDATE `creature_template` SET `AIName`='SmartAI' WHERE `entry` IN (29712, 100449, 29152, 251797, 246154, 246155, 42421, 194437, 141504, 198461, 193812) AND `AIName`='';

-- ============================================================
-- 2. SMART_SCRIPTS
-- ============================================================
-- TextEmote IDs (verified from Guard 68 / Elly Langston 1328):
--   5=Applaud, 17=Bow, 22=Chicken, 34=Dance, 41=Flex, 58=Kiss,
--   77=Rude, 78=Salute, 84=Shy, 101=Wave
-- Emote animation IDs:
--   1=TALK, 2=BOW, 4=CHEER, 25=POINT, 26=SHY, 33=CRY, 66=SALUTE,
--   69=READY_UNARMED, 92=USE_STANDING, 274=WORK_NOPRE, 381=STAND_GUARD, 393=SIT_GROUND

-- ── Stormwind Harbor Guard (29712) — 85 spawns ──
-- Stand at attention, respond to /salute, periodic vigilance
DELETE FROM `smart_scripts` WHERE `entryorguid`=29712 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(29712, 0, 0, 0, 11, 0, 100, 0, 0, 0, 0, 0, 0, 5, 381, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - On Respawn - Set Emote State Stand Guard'),
(29712, 0, 1, 0, 22, 0, 100, 0, 78, 15000, 15000, 0, 0, 10, 66, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - On Receive Salute - Play Emote Salute'),
(29712, 0, 2, 0, 22, 0, 100, 0, 78, 15000, 15000, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - On Receive Salute - Say Line 0'),
(29712, 0, 3, 0, 1, 0, 100, 0, 120000, 300000, 120000, 300000, 0, 10, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - OOC 2-5min - Play Emote Talk'),
(29712, 0, 4, 0, 1, 0, 30, 0, 180000, 600000, 180000, 600000, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - OOC 3-10min 30% - Say Line 1');

-- ── Stormwind Royal Guard (100449) — 35 spawns ──
-- Stoic, respond to /salute and /bow
DELETE FROM `smart_scripts` WHERE `entryorguid`=100449 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(100449, 0, 0, 0, 11, 0, 100, 0, 0, 0, 0, 0, 0, 5, 381, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Royal Guard - On Respawn - Set Emote State Stand Guard'),
(100449, 0, 1, 0, 22, 0, 100, 0, 78, 15000, 15000, 0, 0, 10, 66, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Royal Guard - On Receive Salute - Play Emote Salute'),
(100449, 0, 2, 0, 22, 0, 100, 0, 17, 15000, 15000, 0, 0, 10, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Royal Guard - On Receive Bow - Play Emote Bow');

-- ── Stormwind Dock Worker (29152) — 46 spawns ──
-- Working animation, periodic labor commentary
DELETE FROM `smart_scripts` WHERE `entryorguid`=29152 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(29152, 0, 0, 0, 11, 0, 100, 0, 0, 0, 0, 0, 0, 5, 274, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - On Respawn - Set Emote State Work'),
(29152, 0, 1, 0, 1, 0, 100, 0, 180000, 600000, 180000, 600000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - OOC 3-10min - Say Line 0'),
(29152, 0, 2, 0, 22, 0, 100, 0, 101, 15000, 15000, 0, 0, 10, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - On Receive Wave - Play Emote Talk');

-- ── Interested Citizen (251797) — 49 spawns ──
-- Animated townsfolk, periodic gossip and emotes
DELETE FROM `smart_scripts` WHERE `entryorguid`=251797 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(251797, 0, 0, 0, 1, 0, 100, 0, 60000, 180000, 60000, 180000, 0, 10, 25, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Interested Citizen - OOC 1-3min - Play Emote Point'),
(251797, 0, 1, 0, 1, 0, 100, 0, 90000, 240000, 90000, 240000, 0, 10, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Interested Citizen - OOC 1.5-4min - Play Emote Talk'),
(251797, 0, 2, 0, 1, 0, 50, 0, 180000, 600000, 180000, 600000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Interested Citizen - OOC 3-10min 50% - Say Line 0'),
(251797, 0, 3, 0, 1, 0, 30, 0, 120000, 360000, 120000, 360000, 0, 10, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Interested Citizen - OOC 2-6min 30% - Play Emote Cheer');

-- ── Suspicious Citizen (246154) — 25 spawns ──
-- Shifty behavior, nervous emotes
DELETE FROM `smart_scripts` WHERE `entryorguid`=246154 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(246154, 0, 0, 0, 1, 0, 100, 0, 60000, 180000, 60000, 180000, 0, 10, 26, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - OOC 1-3min - Play Emote Shy'),
(246154, 0, 1, 0, 1, 0, 50, 0, 180000, 600000, 180000, 600000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - OOC 3-10min 50% - Say Line 0'),
(246154, 0, 2, 0, 1, 0, 100, 0, 90000, 240000, 90000, 240000, 0, 10, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - OOC 1.5-4min - Play Emote Talk');

-- ── Suspicious Citizen (246155) — 25 spawns ──
DELETE FROM `smart_scripts` WHERE `entryorguid`=246155 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(246155, 0, 0, 0, 1, 0, 100, 0, 60000, 180000, 60000, 180000, 0, 10, 26, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - OOC 1-3min - Play Emote Shy'),
(246155, 0, 1, 0, 1, 0, 50, 0, 180000, 600000, 180000, 600000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - OOC 3-10min 50% - Say Line 0'),
(246155, 0, 2, 0, 1, 0, 100, 0, 90000, 240000, 90000, 240000, 0, 10, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - OOC 1.5-4min - Play Emote Talk');

-- ── Stormwind Fisherman (42421) — 14 spawns ──
-- Fishing animation, periodic fishing talk
DELETE FROM `smart_scripts` WHERE `entryorguid`=42421 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(42421, 0, 0, 0, 11, 0, 100, 0, 0, 0, 0, 0, 0, 5, 92, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Fisherman - On Respawn - Set Emote State Use Standing'),
(42421, 0, 1, 0, 1, 0, 100, 0, 120000, 360000, 120000, 360000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Stormwind Fisherman - OOC 2-6min - Say Line 0');

-- ── Salty Deckhand (194437) — 25 spawns ──
-- Working animation, sailor commentary
DELETE FROM `smart_scripts` WHERE `entryorguid`=194437 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(194437, 0, 0, 0, 11, 0, 100, 0, 0, 0, 0, 0, 0, 5, 274, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Salty Deckhand - On Respawn - Set Emote State Work'),
(194437, 0, 1, 0, 1, 0, 100, 0, 180000, 600000, 180000, 600000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Salty Deckhand - OOC 3-10min - Say Line 0');

-- ── Wounded Refugee (141504) — 15 spawns ──
-- Sitting on ground, periodic crying
DELETE FROM `smart_scripts` WHERE `entryorguid`=141504 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(141504, 0, 0, 0, 11, 0, 100, 0, 0, 0, 0, 0, 0, 5, 393, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Wounded Refugee - On Respawn - Set Emote State Sit Ground'),
(141504, 0, 1, 0, 1, 0, 100, 0, 60000, 180000, 60000, 180000, 0, 10, 33, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Wounded Refugee - OOC 1-3min - Play Emote Cry'),
(141504, 0, 2, 0, 1, 0, 50, 0, 180000, 600000, 180000, 600000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Wounded Refugee - OOC 3-10min 50% - Say Line 0');

-- ── Curious Dracthyr (198461) — 9 spawns ──
-- Pointing at landmarks, marveling at Stormwind
DELETE FROM `smart_scripts` WHERE `entryorguid`=198461 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(198461, 0, 0, 0, 1, 0, 100, 0, 60000, 180000, 60000, 180000, 0, 10, 25, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - OOC 1-3min - Play Emote Point'),
(198461, 0, 1, 0, 1, 0, 100, 0, 90000, 300000, 90000, 300000, 0, 10, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - OOC 1.5-5min - Play Emote Talk'),
(198461, 0, 2, 0, 1, 0, 100, 0, 120000, 420000, 120000, 420000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - OOC 2-7min - Say Line 0'),
(198461, 0, 3, 0, 22, 0, 100, 0, 101, 15000, 15000, 0, 0, 10, 101, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - On Receive Wave - Play Emote Wave');

-- ── Expedition Trainee (193812) — 9 spawns ──
-- Combat practice stance, periodic training emotes
DELETE FROM `smart_scripts` WHERE `entryorguid`=193812 AND `source_type`=0;
INSERT INTO `smart_scripts` (`entryorguid`,`source_type`,`id`,`link`,`event_type`,`event_phase_mask`,`event_chance`,`event_flags`,`event_param1`,`event_param2`,`event_param3`,`event_param4`,`event_param5`,`action_type`,`action_param1`,`action_param2`,`action_param3`,`action_param4`,`action_param5`,`action_param6`,`target_type`,`target_param1`,`target_param2`,`target_param3`,`target_param4`,`target_x`,`target_y`,`target_z`,`target_o`,`comment`) VALUES
(193812, 0, 0, 0, 11, 0, 100, 0, 0, 0, 0, 0, 0, 5, 69, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - On Respawn - Set Emote State Ready Unarmed'),
(193812, 0, 1, 0, 1, 0, 100, 0, 45000, 120000, 45000, 120000, 0, 10, 36, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - OOC 45s-2min - Play Emote Attack 2H'),
(193812, 0, 2, 0, 1, 0, 50, 0, 180000, 600000, 180000, 600000, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - OOC 3-10min 50% - Say Line 0'),
(193812, 0, 3, 0, 22, 0, 100, 0, 78, 15000, 15000, 0, 0, 10, 66, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - On Receive Salute - Play Emote Salute');

-- ============================================================
-- 3. CREATURE_TEXT — ambient dialogue
-- ============================================================
-- Type: 0=SAY, 2=TEXT_EMOTE, 6=EMOTE (yellow italic)

-- Harbor Guard (29712)
DELETE FROM `creature_text` WHERE `CreatureID`=29712;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(29712, 0, 0, 'Citizen.', 0, 0, 100, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - Salute response'),
(29712, 1, 0, 'All clear.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - Periodic 1'),
(29712, 1, 1, 'Stay vigilant.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - Periodic 2'),
(29712, 1, 2, 'Keep your eyes on the water.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - Periodic 3'),
(29712, 1, 3, 'Nothing to report.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Stormwind Harbor Guard - Periodic 4');

-- Dock Worker (29152)
DELETE FROM `creature_text` WHERE `CreatureID`=29152;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(29152, 0, 0, 'These crates aren''t going to move themselves.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - Periodic 1'),
(29152, 0, 1, 'Another shipment from Kul Tiras.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - Periodic 2'),
(29152, 0, 2, 'Watch your step on the docks.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - Periodic 3'),
(29152, 0, 3, 'The harbor master wants this done by sundown.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - Periodic 4'),
(29152, 0, 4, 'Heavy load today...', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Dock Worker - Periodic 5');

-- Interested Citizen (251797)
DELETE FROM `creature_text` WHERE `CreatureID`=251797;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(251797, 0, 0, 'Did you hear the latest news from the keep?', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Interested Citizen - Periodic 1'),
(251797, 0, 1, 'Times are changing around here.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Interested Citizen - Periodic 2'),
(251797, 0, 2, 'I heard adventurers have been pouring in from all over.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Interested Citizen - Periodic 3'),
(251797, 0, 3, 'Have you seen those dragon folk? Remarkable!', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Interested Citizen - Periodic 4'),
(251797, 0, 4, 'The trade district has been busier than ever.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Interested Citizen - Periodic 5');

-- Suspicious Citizen (246154)
DELETE FROM `creature_text` WHERE `CreatureID`=246154;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(246154, 0, 0, 'Mind your own business.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 1'),
(246154, 0, 1, 'I''m just... passing through.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 2'),
(246154, 0, 2, 'Don''t look at me like that.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 3'),
(246154, 0, 3, 'Nothing to see here. Move along.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 4');

-- Suspicious Citizen (246155)
DELETE FROM `creature_text` WHERE `CreatureID`=246155;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(246155, 0, 0, 'Keep walking, friend.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 1'),
(246155, 0, 1, 'You didn''t see anything.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 2'),
(246155, 0, 2, 'I have my reasons for being here.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 3'),
(246155, 0, 3, 'The guards ask too many questions...', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Suspicious Citizen - Periodic 4');

-- Fisherman (42421)
DELETE FROM `creature_text` WHERE `CreatureID`=42421;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(42421, 0, 0, 'I think I got a bite!', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Fisherman - Periodic 1'),
(42421, 0, 1, 'Nothing biting today...', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Fisherman - Periodic 2'),
(42421, 0, 2, 'The fish aren''t what they used to be.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Fisherman - Periodic 3'),
(42421, 0, 3, 'Patience... patience...', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Fisherman - Periodic 4'),
(42421, 0, 4, 'Should''ve brought more bait.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Stormwind Fisherman - Periodic 5');

-- Salty Deckhand (194437)
DELETE FROM `creature_text` WHERE `CreatureID`=194437;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(194437, 0, 0, 'Heave ho!', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Salty Deckhand - Periodic 1'),
(194437, 0, 1, 'Mind the rigging!', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Salty Deckhand - Periodic 2'),
(194437, 0, 2, 'She''s a fine vessel, she is.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Salty Deckhand - Periodic 3'),
(194437, 0, 3, 'The sea calls to me...', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Salty Deckhand - Periodic 4'),
(194437, 0, 4, 'Stow that cargo below deck!', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Salty Deckhand - Periodic 5');

-- Wounded Refugee (141504)
DELETE FROM `creature_text` WHERE `CreatureID`=141504;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(141504, 0, 0, 'The pain... it won''t stop.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Wounded Refugee - Periodic 1'),
(141504, 0, 1, 'I just want to go home.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Wounded Refugee - Periodic 2'),
(141504, 0, 2, 'We lost everything...', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Wounded Refugee - Periodic 3'),
(141504, 0, 3, 'Is anyone coming to help us?', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Wounded Refugee - Periodic 4');

-- Curious Dracthyr (198461)
DELETE FROM `creature_text` WHERE `CreatureID`=198461;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(198461, 0, 0, 'Remarkable architecture!', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - Periodic 1'),
(198461, 0, 1, 'How do they build so tall without wings?', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - Periodic 2'),
(198461, 0, 2, 'So many different races all in one place...', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - Periodic 3'),
(198461, 0, 3, 'I must document this for the Weyrn.', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - Periodic 4'),
(198461, 0, 4, 'The energy of this city is invigorating!', 0, 0, 20, 0, 0, 0, 0, 0, 0, 'Curious Dracthyr - Periodic 5');

-- Expedition Trainee (193812)
DELETE FROM `creature_text` WHERE `CreatureID`=193812;
INSERT INTO `creature_text` (`CreatureID`,`GroupID`,`ID`,`Text`,`Type`,`Language`,`Probability`,`Emote`,`Duration`,`Sound`,`SoundPlayType`,`BroadcastTextId`,`TextRange`,`comment`) VALUES
(193812, 0, 0, 'One more set!', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - Periodic 1'),
(193812, 0, 1, 'I''ll be ready for whatever''s out there.', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - Periodic 2'),
(193812, 0, 2, 'Hah! Take that!', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - Periodic 3'),
(193812, 0, 3, 'Focus... breathe... strike!', 0, 0, 25, 0, 0, 0, 0, 0, 0, 'Expedition Trainee - Periodic 4');

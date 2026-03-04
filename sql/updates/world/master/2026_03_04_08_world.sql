-- 2026_03_04_08_world.sql
-- RoleplayCore — Remove duplicate DNT bunny spawns for entry 198363
-- "(Bunny) Crow's Nest [DNT]" has 3 copies at identical coords on map 0.
-- Keep lowest guid (3000072198), delete the other two.

DELETE FROM `creature` WHERE `guid` IN (3000072252, 3000091392) AND `id` = 198363;
DELETE FROM `creature_addon` WHERE `guid` IN (3000072252, 3000091392);

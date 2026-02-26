-- 2026_02_25_58_world.sql
-- Clean up orphan npc_vendor entries: missing creature_templates and non-existent items

-- Remove vendor entries for creatures that have no creature_template (4 entries: 54943, 500511, 500537, 500542)
DELETE FROM `npc_vendor` WHERE `entry` IN (54943, 500511, 500537, 500542);

-- Remove vendor entries referencing items that don't exist in 12.x ItemSparse DB2
-- Negative/placeholder ID
DELETE FROM `npc_vendor` WHERE `item` = -34040;

-- Removed/deprecated items (verified missing from ItemSparse 12.0.1.66066)
DELETE FROM `npc_vendor` WHERE `item` IN (
    50164, 56162, 60405,
    99712, 99742, 99743, 99744, 99745, 99746, 99747, 99748, 99749,
    99750, 99751, 99752, 99753, 99754, 99755, 99756,
    101538, 102457, 113193,
    128444, 128475, 128482, 128490,
    137178, 137401,
    139381, 139382, 139383,
    151060,
    156530, 156724, 156725, 156726, 156727, 156758, 156760, 156761,
    156762, 156763, 156764, 156765, 156766, 156767, 156768, 156769,
    156770, 156771, 156772, 156773, 156774, 156775, 156776, 156777,
    156778, 156779, 156780, 156781, 156782, 156783, 156784, 156785,
    156786, 156787, 156788, 156789, 156790, 156791, 156793,
    160105, 160106,
    162355,
    168207, 170540,
    185350,
    200918, 200924, 201000, 201001,
    223284, 224761, 228913
);

# Auth Key System Notes

## How It Works
- `build_info` table: `build`, `majorVersion`, `minorVersion`, `bugfixVersion`
- `build_auth_key` table: `build`, `platform` (Win/Mac), `arch` (x64/A64), `type` (WoW/WoWC), `key` (binary 16)
- Keys are 16-byte (128-bit) values, stored as hex literals (e.g., `0x64C1CBF59BC8EE9B6681FCD5A5A14F7B`)
- Used in HMAC-SHA512 at `WorldSocket.cpp:670-700`: `HMAC(SHA512(sessionKey || authKey), localChallenge || serverChallenge || seed)`
- Client computes same HMAC with key baked into Wow.exe — must match server's result
- Loaded at startup via `ClientBuildInfo.cpp:135-201`

## Current Status (Mar 5 2026) — BUILD 66263 BYPASS ACTIVE
- **Client**: 12.0.1.66263 (Battle.net auto-updated from 66220)
- **Server**: Build 66263 registered in `build_info`, realmlist updated to 66263
- **Auth keys**: NOT YET PUBLISHED by TC — temporary bypass active in WorldSocket.cpp
- **Bypass**: Commit `e3fc8cd9d6` — logs `TC_LOG_WARN` instead of rejecting when key missing
- **DB**: `build_info` has 66263, `build_auth_key` has DELETE placeholders (no INSERT yet)
- **SQL trail**: `sql/updates/auth/master/2026_03_05_00_auth.sql` (has commented-out key INSERT template)
- **Pushed**: Yes — bypass is in remote, will be reverted when TC publishes keys
- **Action needed**: When TC publishes 66263 keys → fill SQL, apply to DB, revert WorldSocket.cpp bypass

## Previous Status (Build 66220) — RESOLVED
- All 7 auth keys applied (Win/Mac, x64/A64, WoW/WoWC)
- Bypass reverted: Commit `8bbd610fc7`
- SQL: `sql/updates/auth/master/2026_03_04_00_auth.sql`

## Auth Key Extraction (for future self-service)
- Keys are VMProtect-obfuscated in Wow.exe, can't be found statically
- **Method**: Runtime debugging — launch Wow.exe via Arctium, attach debugger, read key from memory during HMAC computation
- **Tools**: x64dbg + [WoWDumpFix](https://github.com/adde88/WoWDumpFix) (patches anti-debug byte in ntdll!DbgBreakPoint), or Frida
- **Anti-debug**: WoW patches `ntdll!DbgBreakPoint` 0xCC→0xC3 to prevent debugger attachment
- Shauren likely has this automated — keys appear within hours of new builds
- Each build needs keys for: Win/x64/WoW, Win/x64/WoWC, Win/A64/WoW, Mac/x64/WoW, Mac/x64/WoWC, Mac/A64/WoW, Mac/A64/WoWC

## TC Merge Artifact Fixed
- `SellAllJunkItems` was duplicated in ItemPackets.h, ItemPackets.cpp, WorldSession.h, ItemHandler.cpp
- Kept TC's newer `const&` version (uses `CanSellItemToVendor`), removed old non-const `&` version
- Pushed as `50fb430e43`

## Preventing Future Auto-Updates
- In Battle.net settings, set WoW to "Update when I launch the game" instead of auto-update
- Don't launch WoW through Battle.net — use Arctium directly

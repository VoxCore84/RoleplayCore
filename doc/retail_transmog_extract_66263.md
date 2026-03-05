# Retail Transmog Data Extract (Build 66263)
> Extracted from WoW retail client `C:\WoW\_retail_\` on 2026-03-05
> For use in transmog debugging sessions

## Contents
1. TransmogSpy SavedVariables (GROSTOLIS account — retail)
2. TransmogSpy SavedVariables (1#1 account — private server)
3. FrameXML.log error
4. Transmog-related Hotfix.log entries (retail CDN hotfixes)
5. AccountData.log transmog CVars

---

## 1. TransmogSpy — GROSTOLIS (retail, 12KB)

TransmogSpyDB = {
["log"] = {
"[TransmogSpy 23:31:56] |cff44ff44Hooked: C_TransmogOutfitInfo.SetPendingTransmog|r",
"[TransmogSpy 23:31:56] |cff44ff44Hooked: C_TransmogOutfitInfo.CommitAndApplyAllPending (post-hook)|r",
"[TransmogSpy 23:31:56] |cff44ff44TransmogSpy loaded.|r",
"[TransmogSpy 23:31:56]   Registered 11/14 events",
"[TransmogSpy 23:31:56]   Type /tspy help for commands.",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOGRIFY_UPDATE|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOGRIFY_SUCCESS|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOG_COLLECTION_UPDATED|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOG_COLLECTION_SOURCE_ADDED|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOG_COLLECTION_SOURCE_REMOVED|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOG_COLLECTION_CAMERA_UPDATE|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOG_SEARCH_UPDATED|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOG_SETS_UPDATE_FAVORITE|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ TRANSMOG_SOURCE_COLLECTABILITY_UPDATE|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ VIEWED_TRANSMOG_OUTFIT_CHANGED|r",
"[TransmogSpy 23:31:56]   |cff44ff44+ VIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r",
"[TransmogSpy 23:32:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:32:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:32:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:32:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:32:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:33:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:33:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:33:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:33:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:33:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:37:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:37:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:37:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:37:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:37:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:40:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:40:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:40:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:40:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=190679 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=190681 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=190676 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=190682 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=190680 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=190677 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=190684 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=190678 displayType=1",
"[TransmogSpy 23:41:05] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=0 transmogID=190683 displayType=1",
"[TransmogSpy 23:41:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 23:41:07] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=295490 displayType=1",
"[TransmogSpy 23:41:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 23:41:09] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=42327 displayType=1",
"[TransmogSpy 23:41:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:41:13] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=46211 displayType=1",
"[TransmogSpy 23:41:15] |cffffff44CommitAndApplyAllPending|r: useDiscount=true (post-hook, pending already cleared)",
"[TransmogSpy 23:41:15]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:41:15] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:41:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:41:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:41:19] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:41:19] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:41:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:41:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:41:24] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:41:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:41:26] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:41:26] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:41:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:41:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:41:35] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=86454 displayType=1",
"[TransmogSpy 23:41:35] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=84590 displayType=1",
"[TransmogSpy 23:41:35] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=84588 displayType=1",
"[TransmogSpy 23:41:35] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=84593 displayType=1",
"[TransmogSpy 23:41:35] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=84586 displayType=1",
"[TransmogSpy 23:41:35] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=84594 displayType=1",
"[TransmogSpy 23:41:35] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=84584 displayType=1",
"[TransmogSpy 23:41:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:41:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:41:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:41:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:41:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:41:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:41:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:42:08] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:08] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:42:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:42:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 23:42:16] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 23:42:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:42:17] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 23:42:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 23:42:19] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=2 transmogID=185598 displayType=1",
"[TransmogSpy 23:42:21] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:42:21]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:42:21] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:42:23] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 23:42:27] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:27] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 23:42:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:42:32] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=77344 displayType=3",
"[TransmogSpy 23:42:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 23:42:34] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 23:42:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 23:42:36] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:42:36]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:42:36] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:42:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 23:42:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:42:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 23:42:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:42:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 23:42:41] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 23:42:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 23:42:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 8]",
"[TransmogSpy 23:42:53] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 23:42:54] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=295500 displayType=1",
"[TransmogSpy 23:42:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 23:42:58] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=22002 displayType=1",
"[TransmogSpy 23:43:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:43:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:43:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:43:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:43:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 23:43:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:43:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 23:44:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:44:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:44:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 23:44:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:45:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:45:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
},
}

---

## 2. TransmogSpy — 1#1 (private server, 179KB)

TransmogSpyDB = {
["log"] = {
"[TransmogSpy 20:08:38] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:08:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:08:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 20:08:44] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:08:44] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:08:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 20:08:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:08:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 20:08:51] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=302233 displayType=1",
"[TransmogSpy 20:08:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 20:08:52] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=302065 displayType=1",
"[TransmogSpy 20:08:54] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=6351 displayType=1",
"[TransmogSpy 20:08:56] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:08:56]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:08:56] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:08:56] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:08:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 20:09:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:09:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:09:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 20:09:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:09:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 20:09:19] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=13010 displayType=1",
"[TransmogSpy 20:09:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 20:09:22] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=3923 displayType=1",
"[TransmogSpy 20:09:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 20:09:26] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=288004 displayType=1",
"[TransmogSpy 20:09:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 20:09:28] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=195321 displayType=1",
"[TransmogSpy 20:09:29] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:09:29]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:09:29] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:09:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:09:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 20:20:48] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 20:20:48] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 20:20:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:20:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:20:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:20:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:20:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 14:57:12] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 14:57:12] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 14:57:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:57:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:57:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:57:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:57:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 14:58:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:58:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:58:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 14:58:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:58:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 14:58:12] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=229610 displayType=1",
"[TransmogSpy 14:58:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 14:58:14] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=168248 displayType=1",
"[TransmogSpy 14:58:16] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 14:58:16]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 14:58:16] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 14:58:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:58:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 14:58:22] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:58:22] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:58:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 14:58:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:58:25] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=297862 displayType=1",
"[TransmogSpy 14:58:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 14:58:26] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=300625 displayType=1",
"[TransmogSpy 14:58:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 14:58:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 14:58:33] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=302045 displayType=1",
"[TransmogSpy 14:58:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 14:58:34] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=303515 displayType=1",
"[TransmogSpy 14:58:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 14:58:36] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=302548 displayType=1",
"[TransmogSpy 14:58:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 14:58:38] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=292921 displayType=1",
"[TransmogSpy 14:58:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 14:58:39] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=195320 displayType=1",
"[TransmogSpy 14:58:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 14:58:41] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=301573 displayType=1",
"[TransmogSpy 14:58:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 8]",
"[TransmogSpy 14:58:42] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=301648 displayType=1",
"[TransmogSpy 14:58:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 9]",
"[TransmogSpy 14:58:43] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=302538 displayType=1",
"[TransmogSpy 14:58:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 10]",
"[TransmogSpy 14:58:44] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=302512 displayType=1",
"[TransmogSpy 14:58:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 11]",
"[TransmogSpy 14:58:45] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=303121 displayType=1",
"[TransmogSpy 14:58:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 14:58:47] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=302233 displayType=1",
"[TransmogSpy 14:58:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 14:58:48] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=302065 displayType=1",
"[TransmogSpy 14:58:50] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=6351 displayType=1",
"[TransmogSpy 14:58:52] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 14:58:52]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 14:58:52] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 14:58:53] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:58:53] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 14:59:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:59:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:59:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 14:59:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:59:06] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=301316 displayType=1",
"[TransmogSpy 14:59:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 14:59:09] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=301574 displayType=1",
"[TransmogSpy 14:59:15] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=303445 displayType=1",
"[TransmogSpy 14:59:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 14:59:18] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=298160 displayType=1",
"[TransmogSpy 14:59:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 14:59:23] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=301448 displayType=1",
"[TransmogSpy 14:59:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 14:59:27] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=222844 displayType=1",
"[TransmogSpy 14:59:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 14:59:29] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=8250 displayType=1",
"[TransmogSpy 14:59:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 14:59:32] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=288304 displayType=1",
"[TransmogSpy 14:59:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 8]",
"[TransmogSpy 14:59:35] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=296367 displayType=1",
"[TransmogSpy 14:59:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 9]",
"[TransmogSpy 14:59:37] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=301421 displayType=1",
"[TransmogSpy 14:59:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 10]",
"[TransmogSpy 14:59:39] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=301606 displayType=1",
"[TransmogSpy 14:59:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 11]",
"[TransmogSpy 14:59:41] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=303621 displayType=1",
"[TransmogSpy 14:59:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 14:59:43] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=295238 displayType=1",
"[TransmogSpy 14:59:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 14:59:45] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=298856 displayType=1",
"[TransmogSpy 14:59:50] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=5388 displayType=1",
"[TransmogSpy 14:59:52] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=5391 displayType=1",
"[TransmogSpy 14:59:55] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=6174 displayType=1",
"[TransmogSpy 14:59:57] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 14:59:57]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 14:59:57] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 14:59:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:59:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 15:00:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 15:00:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 15:00:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 15:00:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 15:00:13] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 15:00:13]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 15:00:13] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 15:00:14] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 15:00:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 15:03:38] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 15:03:38] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 15:03:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 15:03:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 15:03:52] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=301316 displayType=1",
"[TransmogSpy 15:03:53] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 15:03:54] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=301574 displayType=1",
"[TransmogSpy 15:03:57] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=303445 displayType=1",
"[TransmogSpy 15:04:04] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 15:04:08] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=302307 displayType=1",
"[TransmogSpy 15:04:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 15:04:17] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=301056 displayType=1",
"[TransmogSpy 15:04:18] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=302539 displayType=1",
"[TransmogSpy 15:04:18] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=302542 displayType=1",
"[TransmogSpy 15:04:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 15:04:22] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=218284 displayType=1",
"[TransmogSpy 15:04:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 15:04:24] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=84536 displayType=1",
"[TransmogSpy 15:04:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 15:04:26] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=285642 displayType=1",
"[TransmogSpy 15:04:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 8]",
"[TransmogSpy 15:04:28] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=298064 displayType=1",
"[TransmogSpy 15:04:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 9]",
"[TransmogSpy 15:04:29] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=301618 displayType=1",
"[TransmogSpy 15:04:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 10]",
"[TransmogSpy 15:04:31] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=301613 displayType=1",
"[TransmogSpy 15:04:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 11]",
"[TransmogSpy 15:04:32] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=300821 displayType=1",
"[TransmogSpy 15:04:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 15:04:34] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=298861 displayType=1",
"[TransmogSpy 15:04:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 15:04:36] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=295247 displayType=1",
"[TransmogSpy 15:04:38] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=5390 displayType=1",
"[TransmogSpy 15:05:06] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 15:05:06]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 15:05:06] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 15:05:07] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 15:05:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 16:13:35] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 16:13:35] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 16:13:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 16:13:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 16:13:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 16:13:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 16:13:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 16:18:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 16:18:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 16:18:19] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 16:18:19]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 16:18:19] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 16:18:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 16:18:25] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:25] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 16:18:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 16:18:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 16:18:28] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 16:18:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 16:18:29] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 16:18:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 16:18:31] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=303842 displayType=1",
"[TransmogSpy 16:18:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 16:18:33] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=296357 displayType=1",
"[TransmogSpy 16:18:34] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 16:18:34]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 16:18:34] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 16:18:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 16:18:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 16:18:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 16:18:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 16:18:43] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=303842 displayType=1",
"[TransmogSpy 16:18:44] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=302174 displayType=1",
"[TransmogSpy 16:18:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 16:18:45] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=296357 displayType=1",
"[TransmogSpy 16:18:47] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=5360 displayType=3",
"[TransmogSpy 16:18:48] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 16:18:48]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 16:18:48] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 16:18:48] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 16:18:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 17:11:10] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 17:11:10] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 17:11:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:11:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:11:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:11:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:11:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 17:12:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 17:12:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:12:10] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 17:12:10]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 17:12:10] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 17:12:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:12:18] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:18] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:12:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:12:23] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 17:12:23]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 17:12:23] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 17:12:24] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:12:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:12:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:12:39] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 17:12:39]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 17:12:39] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 17:12:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:12:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:13:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:13:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 17:13:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:13:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:13:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 17:13:12] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=303842 displayType=1",
"[TransmogSpy 17:13:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 17:13:14] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=296357 displayType=1",
"[TransmogSpy 17:13:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 17:13:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 17:13:17] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=304056 displayType=1",
"[TransmogSpy 17:13:20] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 17:13:20]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 17:13:20] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 17:13:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:13:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 17:13:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:13:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 17:13:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 17:13:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:13:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 17:13:58] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=302174 displayType=1",
"[TransmogSpy 17:13:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 17:14:00] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=300586 displayType=1",
"[TransmogSpy 17:14:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 17:14:02] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=300590 displayType=1",
"[TransmogSpy 17:14:04] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 17:14:04]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 17:14:04] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 17:14:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:14:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 17:14:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:14:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 17:14:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 17:14:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:14:50] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 17:14:50]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 17:14:50] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 17:15:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:15:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:15:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:15:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 17:15:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:15:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:15:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 17:15:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:35:44] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 18:35:44] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 18:35:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 18:35:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 18:35:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 18:35:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 18:35:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 18:39:49] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:39:49] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:39:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 18:39:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:39:54] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=297862 displayType=1",
"[TransmogSpy 18:39:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 18:39:56] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=300625 displayType=1",
"[TransmogSpy 18:39:59] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=302045 displayType=1",
"[TransmogSpy 18:40:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 18:40:01] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=303515 displayType=1",
"[TransmogSpy 18:40:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 18:40:06] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=302548 displayType=1",
"[TransmogSpy 18:40:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 18:40:08] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=229610 displayType=1",
"[TransmogSpy 18:40:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 18:40:09] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=168248 displayType=1",
"[TransmogSpy 18:40:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 18:40:11] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=302645 displayType=1",
"[TransmogSpy 18:40:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 8]",
"[TransmogSpy 18:40:12] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=301604 displayType=1",
"[TransmogSpy 18:40:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 9]",
"[TransmogSpy 18:40:14] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=302534 displayType=1",
"[TransmogSpy 18:40:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 10]",
"[TransmogSpy 18:40:15] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=302512 displayType=1",
"[TransmogSpy 18:40:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 11]",
"[TransmogSpy 18:40:16] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=301639 displayType=1",
"[TransmogSpy 18:40:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 18:40:25] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=301108 displayType=1",
"[TransmogSpy 18:40:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 18:40:27] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=298149 displayType=1",
"[TransmogSpy 18:40:29] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:40:29]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:40:29] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:40:31] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:40:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 18:40:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:40:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:40:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 18:40:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:40:38] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=5360 displayType=3",
"[TransmogSpy 18:40:39] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:40:39]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:40:39] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:40:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:40:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:40:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:40:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:40:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:40:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:40:49] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=303522 displayType=1",
"[TransmogSpy 18:40:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 18:40:50] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=296522 displayType=1",
"[TransmogSpy 18:40:54] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=296527 displayType=1",
"[TransmogSpy 18:40:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 18:40:55] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=307647 displayType=1",
"[TransmogSpy 18:40:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 18:40:57] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=303601 displayType=1",
"[TransmogSpy 18:40:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 18:40:58] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=302817 displayType=1",
"[TransmogSpy 18:40:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 18:41:00] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=249021 displayType=1",
"[TransmogSpy 18:41:00] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=249019 displayType=1",
"[TransmogSpy 18:41:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 18:41:01] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=303589 displayType=1",
"[TransmogSpy 18:41:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 8]",
"[TransmogSpy 18:41:02] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=302158 displayType=1",
"[TransmogSpy 18:41:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 9]",
"[TransmogSpy 18:41:04] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=303593 displayType=1",
"[TransmogSpy 18:41:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 10]",
"[TransmogSpy 18:41:05] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=303112 displayType=1",
"[TransmogSpy 18:41:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 11]",
"[TransmogSpy 18:41:06] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=303621 displayType=1",
"[TransmogSpy 18:41:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 18:41:08] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=303949 displayType=1",
"[TransmogSpy 18:41:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 18:41:09] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=303460 displayType=1",
"[TransmogSpy 18:41:10] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=6836 displayType=1",
"[TransmogSpy 18:41:12] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:41:12]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:41:12] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:41:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:41:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 18:41:21] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:41:21] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:41:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 18:41:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:41:23] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:41:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:41:25] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:41:25] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:41:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:41:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:42:08] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:42:08]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:42:08] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:42:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:42:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:42:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:42:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:42:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:42:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:42:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 18:42:22] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:42:22]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:42:22] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:42:24] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:42:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 18:42:47] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:42:47] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:42:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 18:42:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:42:53] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 18:42:54] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=303643 displayType=1",
"[TransmogSpy 18:42:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 18:42:57] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=304056 displayType=1",
"[TransmogSpy 18:42:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 18:42:59] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=249021 displayType=1",
"[TransmogSpy 18:43:01] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:43:01]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:43:01] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:43:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:43:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 18:43:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:43:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:43:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 18:43:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:44:33] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:44:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:27:23] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 20:27:23] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 20:27:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:27:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:27:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:27:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:27:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:29:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:29:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:29:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:29:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:29:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:29:21] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:29:21]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:29:21] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:29:21] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:29:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:29:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:29:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:29:56] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=0 displayType=2",
"[TransmogSpy 20:29:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 20:29:58] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=0 displayType=2",
"[TransmogSpy 20:29:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 20:30:00] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=0 displayType=2",
"[TransmogSpy 20:30:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 20:30:01] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=0 displayType=2",
"[TransmogSpy 20:30:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 20:30:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 20:30:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:30:07] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:30:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:30:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:30:11] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=300448 displayType=1",
"[TransmogSpy 20:30:13] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:30:13]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:30:13] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:30:14] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:30:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:30:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:30:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:31:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 20:31:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 20:31:21] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:31:21]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:31:21] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:31:21] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 20:31:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 20:31:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:31:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 20:31:33] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=287092 displayType=1",
"[TransmogSpy 20:31:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 20:31:34] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=296357 displayType=1",
"[TransmogSpy 20:31:36] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:31:36]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:31:36] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:31:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 20:31:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 20:31:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:31:42] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=5360 displayType=3",
"[TransmogSpy 20:31:43] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:31:43]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:31:43] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:31:44] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:31:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:31:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:31:48] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=7100 displayType=1",
"[TransmogSpy 20:31:50] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:31:50]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:31:50] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:31:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:31:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:32:27] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:32:27] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:32:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:32:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:32:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:33:07] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:33:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:33:42] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:33:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:33:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:33:48] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:33:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:11:15] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 22:11:15] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 22:11:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 22:11:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 22:11:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 22:11:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 22:11:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 22:13:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 22:13:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:13:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:52] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:52] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:53] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:53] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:53] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:53] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:56] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:56] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:56] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:13:56] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:07] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:07] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:12] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:14:12]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:14:12] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:14:12] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:23] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:23] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:37] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:14:37]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:14:37] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:14:38] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:14:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:14:49] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=300449 displayType=1",
"[TransmogSpy 22:14:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 22:14:51] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=300464 displayType=1",
"[TransmogSpy 22:14:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 22:14:52] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=303643 displayType=1",
"[TransmogSpy 22:14:53] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 22:14:53] |cffffff44SetPendingTransmog|r: slot=4(CHEST) type=0 option=0 transmogID=300427 displayType=1",
"[TransmogSpy 22:14:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 22:14:55] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=304236 displayType=1",
"[TransmogSpy 22:14:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 22:14:56] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=249020 displayType=1",
"[TransmogSpy 22:14:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 22:14:57] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=300483 displayType=1",
"[TransmogSpy 22:14:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 8]",
"[TransmogSpy 22:14:58] |cffffff44SetPendingTransmog|r: slot=8(HANDS) type=0 option=0 transmogID=300443 displayType=1",
"[TransmogSpy 22:14:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 9]",
"[TransmogSpy 22:14:59] |cffffff44SetPendingTransmog|r: slot=9(WAIST) type=0 option=0 transmogID=300475 displayType=1",
"[TransmogSpy 22:15:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 10]",
"[TransmogSpy 22:15:00] |cffffff44SetPendingTransmog|r: slot=10(LEGS) type=0 option=0 transmogID=300459 displayType=1",
"[TransmogSpy 22:15:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 11]",
"[TransmogSpy 22:15:01] |cffffff44SetPendingTransmog|r: slot=11(FEET) type=0 option=0 transmogID=303622 displayType=1",
"[TransmogSpy 22:15:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 22:15:02] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=300590 displayType=1",
"[TransmogSpy 22:15:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:15:03] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=303922 displayType=1",
"[TransmogSpy 22:15:05] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=7100 displayType=1",
"[TransmogSpy 22:15:07] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:15:07]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:15:07] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:15:08] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:15:19] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:19] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:15:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:15:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:24] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:15:24]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:15:24] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:15:24] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:15:26] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:26] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:15:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:15:29] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:15:29]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:15:29] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:15:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:15:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:16:14] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:14] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:16:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:16:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:30] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:30] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:35] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:16:35]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:16:35] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:16:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:16:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:16:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:16:49] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:16:49]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:16:49] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:16:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:16:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:32] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:17:32]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:17:32] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:17:34] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:17:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:17:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:18:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 22:18:04] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:18:04]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:18:04] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:18:04] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:04] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:18:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:18:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:18:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 4]",
"[TransmogSpy 22:18:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 22:18:10] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 22:18:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 22:18:11] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 22:18:12] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:18:12]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:18:12] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:18:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 22:18:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 22:18:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:18:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 22:18:25] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=300590 displayType=1",
"[TransmogSpy 22:18:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:18:26] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=303922 displayType=1",
"[TransmogSpy 22:18:27] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:18:27]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:18:27] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:18:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:18:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:18:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:18:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:18:37] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=300586 displayType=1",
"[TransmogSpy 22:18:39] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:18:39]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:18:39] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:18:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:18:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:18:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:18:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 22:18:44] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=300590 displayType=1",
"[TransmogSpy 22:18:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:18:46] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=300586 displayType=1",
"[TransmogSpy 22:18:47] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:18:47]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:18:47] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:18:48] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:18:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:19:10] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:10] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 22:19:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:19:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 22:19:13] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=300590 displayType=1",
"[TransmogSpy 22:19:16] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=7100 displayType=1",
"[TransmogSpy 22:19:17] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:19:17]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:19:17] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:19:18] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 22:19:26] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:26] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 22:19:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:19:28] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=8553 displayType=1",
"[TransmogSpy 22:19:30] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:19:30]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:19:30] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:19:31] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:19:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:19:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:19:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 22:19:41] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=303638 displayType=1",
"[TransmogSpy 22:19:43] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:19:43]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:19:43] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:19:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:19:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 22:29:04] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 22:29:04] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 22:29:04] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 22:29:04] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 22:29:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:29:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:29:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:29:29] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:29:29]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:29:29] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:29:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:29:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:29:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:29:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 22:29:44] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:29:44]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:29:44] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:29:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 22:29:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 22:29:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 22:29:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 22:29:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 22:30:01] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=301736 displayType=1",
"[TransmogSpy 22:30:03] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 22:30:03]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 22:30:03] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 22:30:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 22:30:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 23:22:24] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 23:22:24] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 23:22:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:22:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:22:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:22:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:22:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:32:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:32:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:32:29] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:32:29]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:32:29] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:32:30] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:32:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:32:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:32:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 23:32:41] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=301307 displayType=1",
"[TransmogSpy 23:32:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:32:42] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=292218 displayType=1",
"[TransmogSpy 23:32:45] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=7100 displayType=1",
"[TransmogSpy 23:32:47] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:32:47]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:32:47] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:32:47] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:32:54] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:54] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:32:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:32:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 23:32:56] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=292921 displayType=1",
"[TransmogSpy 23:32:58] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:32:58]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:32:58] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:32:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:32:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 23:33:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 23:33:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:33:14] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:33:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:33:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:33:28] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:33:28]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:33:28] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:33:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:33:34] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:34] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:33:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:33:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 23:33:40] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 23:33:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 23:33:41] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 23:33:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 23:33:42] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 23:33:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 23:33:44] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 23:33:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 23:33:45] |cffffff44SetPendingTransmog|r: slot=7(WRIST) type=0 option=0 transmogID=104604 displayType=3",
"[TransmogSpy 23:33:46] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:33:46]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:33:46] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:33:47] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:33:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 23:34:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:34:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:34:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 23:34:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:34:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 23:34:42] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=303842 displayType=1",
"[TransmogSpy 23:34:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:34:43] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=303922 displayType=1",
"[TransmogSpy 23:34:45] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=1 option=1 transmogID=5360 displayType=3",
"[TransmogSpy 23:34:46] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:34:46]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:34:46] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:34:47] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:34:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:36:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:36:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:36:15] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:36:15]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:36:15] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:36:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:36:23] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:23] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:36:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:36:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 23:36:28] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=300590 displayType=1",
"[TransmogSpy 23:36:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:36:30] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=5 transmogID=300586 displayType=1",
"[TransmogSpy 23:36:32] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 23:36:32]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 23:36:32] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 23:36:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:36:49] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:49] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 18]",
"[TransmogSpy 23:36:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:36:54] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 23:36:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 23:49:31] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 23:49:31] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 23:49:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:49:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:49:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:49:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:49:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:55:24] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 23:55:24] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 23:55:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:55:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:55:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:55:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:55:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:57:17] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 23:57:17] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 23:57:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:57:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:57:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:57:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:57:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:57:33] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 23:57:33] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 23:57:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:57:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:57:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:57:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:57:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 23:59:49] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 23:59:49] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 23:59:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:59:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 23:59:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:59:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 23:59:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:43:06] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 00:43:06] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 00:43:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:43:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:43:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:43:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:43:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:47:58] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 00:47:58] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 00:47:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:47:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:47:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:47:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:48:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:49:20] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 00:49:20] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 00:49:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:49:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:49:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:49:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:49:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:52:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:53:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:53:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:53:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:53:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:53:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:53:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:53:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:53:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:53:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:53:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 00:54:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:54:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:54:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 00:54:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:54:50] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 00:54:50]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 00:54:50] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 00:54:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:54:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:55:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:55:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 00:55:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:55:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:55:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:55:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:56:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:57:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:57:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:57:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:57:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:57:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:57:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:57:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:57:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:58:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:58:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:58:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 00:58:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:58:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:58:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 00:58:22] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=290226 displayType=1",
"[TransmogSpy 00:58:26] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 00:58:26]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 00:58:26] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 00:58:26] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:58:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 00:58:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:58:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 00:58:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 00:58:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:58:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 00:58:34] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 00:58:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:58:35] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 00:58:36] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 00:58:36]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 00:58:36] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 00:58:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:58:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:59:33] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:33] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 00:59:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:59:38] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 00:59:38]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 00:59:38] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 00:59:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:59:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:59:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:59:52] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 00:59:52]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 00:59:52] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 00:59:52] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:59:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 00:59:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:59:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:00:05] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 01:00:05]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 01:00:05] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 01:00:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:00:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:00:10] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:00:10] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 01:00:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:00:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:00:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 01:00:24] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=114080 displayType=3",
"[TransmogSpy 01:00:25] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=114080 displayType=3",
"[TransmogSpy 01:01:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:01:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 02:00:23] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 02:00:23] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 02:00:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 02:00:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 02:00:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 02:00:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 02:00:26] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 02:05:48] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 02:05:48] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 02:05:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 02:05:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 02:05:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 02:05:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 02:05:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 02:06:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 02:06:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:07] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 02:06:07]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 02:06:07] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 02:06:07] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:19] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 02:06:19]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 02:06:19] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 02:06:19] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:22] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:22] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:27] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 02:06:27]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 02:06:27] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 02:06:27] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:06:34] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 02:06:34]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 02:06:34] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 02:06:34] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:06:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:07:14] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:07:14] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 02:07:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:07:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:07:22] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 02:07:22]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 02:07:22] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 02:07:22] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:07:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:07:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:07:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 02:07:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:07:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 02:07:40] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 02:07:40]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 02:07:40] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 02:07:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 02:07:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:07:19] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 03:07:19] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 03:07:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:07:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:07:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:07:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:07:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 03:07:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 03:07:32] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 03:07:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 03:07:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:07:42] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 03:07:42]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 03:07:42] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 03:07:42] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 03:07:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:08:24] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 03:08:24] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 03:08:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:08:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:08:31] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 03:08:31]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 03:08:31] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 03:08:31] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 03:08:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:08:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 03:08:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 03:08:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:08:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:08:46] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 03:08:46]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 03:08:46] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 03:08:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 03:08:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:16:45] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 03:16:45] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 03:16:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:16:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:16:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:16:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:16:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:21:16] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 03:21:16] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 03:21:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:21:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:21:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:21:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:21:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 03:22:31] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 03:22:31] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 03:22:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:22:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 03:22:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:22:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 03:22:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:35:41] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 12:35:41] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 12:35:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 12:35:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 12:35:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 12:35:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 12:35:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 12:37:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:37:29] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:37:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 12:37:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:37] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 12:38:37]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 12:38:37] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 12:38:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:45] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 12:38:45]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 12:38:45] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 12:38:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:38:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:38:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:39:01] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 12:39:01]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 12:39:01] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 12:39:02] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:39:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:39:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:39:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:39:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:39:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:39:56] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 12:39:56]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 12:39:56] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 12:41:01] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 12:41:01]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 12:41:01] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 12:41:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:41:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:41:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:41:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 12:41:12] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=0 displayType=2",
"[TransmogSpy 12:41:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 12:41:28] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=2 transmogID=302237 displayType=1",
"[TransmogSpy 12:41:30] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 12:41:30]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 12:41:30] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 12:41:30] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 12:41:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 23]",
"[TransmogSpy 12:41:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:41:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 12:41:39] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=295683 displayType=1",
"[TransmogSpy 12:41:42] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 12:41:42]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 12:41:42] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 12:41:42] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 12:41:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 12:41:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:41:57] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:41:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:42:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:42:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:42:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:42:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 12:42:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 12:44:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:44:18] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:44:18] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:44:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:44:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:44:21] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 12:44:21] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 12:44:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 13:04:00] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 13:04:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 14:05:33] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 14:05:33] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 14:05:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:05:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:05:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:05:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:05:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 14:07:42] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:07:42] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:07:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 14:07:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:08:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:08:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:08:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:08:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:08:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:08:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:09:12] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 14:09:12]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 14:09:12] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 14:09:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:09:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:09:48] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:09:48] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:09:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:09:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:10:33] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 14:10:33]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 14:10:33] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 14:10:33] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:10:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:11:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:11:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:11:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:11:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:11:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:11:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:11:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:11:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 14:11:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:11:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:11:35] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 14:11:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 14:21:48] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 14:21:48] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 14:21:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:21:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:21:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:21:48] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:21:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 14:22:22] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 14:22:22] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 14:22:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:22:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 14:22:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:22:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 14:22:22] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 17:22:45] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 17:22:45] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 17:22:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:22:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:22:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:22:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:22:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 17:23:40] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 17:23:40] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 17:23:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:23:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:23:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:23:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:23:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 17:24:00] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 17:24:00] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 17:24:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:24:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:24:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:24:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:24:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 17:26:15] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 17:26:15] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 17:26:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:26:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:26:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:26:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:26:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 17:27:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 17:27:54] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 17:27:54] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 17:27:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:27:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 17:27:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:27:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 17:27:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:43:17] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 18:43:17] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 18:43:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 18:43:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 18:43:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 18:43:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 18:43:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 18:44:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 18:44:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 18:44:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 18:44:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 18:44:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 18:45:33] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:45:33] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:45:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 18:45:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:47:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:47:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:47:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:47:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 18:47:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:47:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 18:47:32] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=77344 displayType=3",
"[TransmogSpy 18:47:33] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:47:33]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:47:33] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:49:10] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 18:49:10]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 18:49:10] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 18:49:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 18:49:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:02:18] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 20:02:18] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 20:02:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:02:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:02:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:02:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:02:21] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:05:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:05:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:05:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:05:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:05:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:29:12] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 20:29:12] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 20:29:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:29:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:29:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:29:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:29:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:30:00] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 20:30:00] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 20:30:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:30:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:30:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:30:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:30:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:35:57] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 20:35:57] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 20:35:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:35:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:35:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:35:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:35:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:36:43] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 20:36:43] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 20:36:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:36:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 20:36:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:36:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:36:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:43:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:43:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:43:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 20:43:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:44:08] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:44:08] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:44:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:44:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:44:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:44:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:44:39] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:44:39]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:44:39] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:44:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:44:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:44:42] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:44:42] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:44:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:44:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:44:44] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=77344 displayType=3",
"[TransmogSpy 20:44:45] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:44:45]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:44:45] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:44:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:44:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:45:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:45:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:45:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:45:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:45:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:45:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:45:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 20:45:43] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 20:45:43]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 20:45:43] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 20:45:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:45:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:46:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:46:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 20:46:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:46:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 20:47:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 20:47:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 00:59:38] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 00:59:38] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 00:59:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:59:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 00:59:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:59:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 00:59:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 01:16:09] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 01:16:09] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 01:16:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:16:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:16:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:16:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:16:12] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 01:18:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:18:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:18:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:18:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:18:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 01:24:19] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 01:24:19] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 01:24:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:24:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:24:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:24:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:24:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 01:26:17] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 01:26:17] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 01:26:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:26:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:26:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:26:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:26:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 01:37:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 01:37:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:37:15] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 01:37:15]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 01:37:15] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 01:37:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:37:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:37] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:37:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:37:46] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 01:37:46]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 01:37:46] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 01:37:47] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:37:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 01:37:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:37:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:38:05] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 01:38:05]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 01:38:05] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 01:38:05] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:38:05] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:38:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:38:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 01:38:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:38:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:38:38] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:38:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:38:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:38:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 01:38:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:38:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 01:39:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 01:39:04] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=298602 displayType=1",
"[TransmogSpy 01:39:06] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 01:39:06]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 01:39:06] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 01:39:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 01:39:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 01:59:54] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 01:59:54] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 01:59:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:59:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 01:59:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:59:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 01:59:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 04:45:39] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 04:45:39] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 04:45:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 04:45:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 04:45:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 04:45:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 04:45:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 04:54:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:54:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 04:54:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 04:54:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:54:46] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 04:54:46]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 04:54:46] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 04:54:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:54:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:54:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:54:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 04:54:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:54:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:55:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 04:55:00] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 04:55:06] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=297500 displayType=1",
"[TransmogSpy 04:55:09] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 04:55:09]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 04:55:09] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 04:55:10] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:55:10] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 04:55:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:55:15] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 04:55:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 04:55:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:55:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 04:55:18] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=303948 displayType=1",
"[TransmogSpy 04:55:19] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 19]",
"[TransmogSpy 04:55:20] |cffffff44SetPendingTransmog|r: slot=13(OFFHAND) type=0 option=4 transmogID=303927 displayType=1",
"[TransmogSpy 04:55:22] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 04:55:22]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 04:55:22] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 04:55:23] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:55:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 19]",
"[TransmogSpy 04:56:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:56:11] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 04:56:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 19]",
"[TransmogSpy 04:56:11] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:56:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:56:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:56:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:56:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 04:56:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:56:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 04:56:26] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 04:56:26]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 04:56:26] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 04:56:27] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 04:56:27] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 05:31:15] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 05:31:15] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 05:31:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:31:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:31:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:31:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:31:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 05:32:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:32:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:32:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:32:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:32:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 05:33:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:33:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:33:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:33:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:33:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 05:37:42] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 05:37:42] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 05:37:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:37:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 05:37:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:37:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 05:37:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 06:39:32] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 06:39:32] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 06:39:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 06:39:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 06:39:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 06:39:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 06:39:35] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:00:14] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:00:14] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:00:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:00:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:00:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:00:14] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:00:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:01:56] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:01:56] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:01:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:01:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:01:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:01:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:01:57] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:03:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:03:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:03:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:03:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:03:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:06:02] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:06:02] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:06:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:06:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:06:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:06:02] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:06:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:06:37] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:06:37] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:06:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:06:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:06:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:06:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:06:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:19:19] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:19:19] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:19:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:19:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:19:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:19:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:19:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:23:55] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:23:55] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:23:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:23:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:23:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:23:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:23:56] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:24:51] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:24:51] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:24:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:24:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:24:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:24:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:24:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:33:38] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:33:38] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:33:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:33:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:33:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:33:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:33:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:46:44] |cff44ffffTRANSMOG_COLLECTION_UPDATED|r: args=[nil, nil, nil, nil]",
"[TransmogSpy 09:46:44] |cff44ffffTRANSMOG_SETS_UPDATE_FAVORITE|r: args=[none]",
"[TransmogSpy 09:46:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:46:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[2, nil]",
"[TransmogSpy 09:46:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:46:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[3, nil]",
"[TransmogSpy 09:46:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:47:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:36] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:47:36] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:47:38] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:47:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:39] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:47:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:47:49] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:47:49]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:47:49] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:47:49] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:47:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:47:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:47:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:47:54] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:48:05] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=297501 displayType=1",
"[TransmogSpy 09:48:07] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=297501 displayType=1",
"[TransmogSpy 09:48:14] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:48:14]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:48:14] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:48:16] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:48:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:49:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:20] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:49:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:49:43] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:43] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:49:44] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:44] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:49:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:49:49] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:49:49]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:49:49] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:49:51] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:49:53] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:53] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:49:53] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:49:53] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:51:00] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:51:00]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:51:00] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:51:01] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:51:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:51:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:51:03] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:51:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:51:03] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:51:07] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:51:09] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:51:12] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=114080 displayType=3",
"[TransmogSpy 09:51:13] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:51:14] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:51:15] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:51:17] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=108785 displayType=3",
"[TransmogSpy 09:51:18] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 09:51:19] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=108785 displayType=3",
"[TransmogSpy 09:51:20] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 09:51:23] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 09:51:23] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 09:51:24] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 09:51:25] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 09:51:34] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=195324 displayType=1",
"[TransmogSpy 09:51:34] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=195323 displayType=1",
"[TransmogSpy 09:51:36] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:51:36]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:51:36] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:51:38] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:51:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 09:51:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:51:41] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:51:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 09:51:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:51:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:51:43] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=302174 displayType=1",
"[TransmogSpy 09:51:45] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:51:45]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:51:45] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:51:46] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:51:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:54:30] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:54:30] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:54:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:54:30] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:54:37] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:54:39] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=114080 displayType=3",
"[TransmogSpy 09:54:41] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:54:42] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:54:42] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 09:54:44] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 09:54:44] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 09:54:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 09:54:46] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 09:54:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 7]",
"[TransmogSpy 09:54:47] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:54:49] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:54:49]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:54:49] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:54:50] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:54:50] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:54:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:54:58] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:54:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:54:58] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:54:59] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:55:02] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:55:04] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:55:05] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:55:05]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:55:05] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:55:06] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:55:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:55:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:55:13] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:55:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:55:13] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:55:16] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:55:18] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:55:19] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:55:20] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=114080 displayType=3",
"[TransmogSpy 09:55:20] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:55:22] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:55:25] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:55:26] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=303846 displayType=1",
"[TransmogSpy 09:55:31] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 19]",
"[TransmogSpy 09:55:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:55:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 19]",
"[TransmogSpy 09:55:51] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:55:58] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76538 displayType=1",
"[TransmogSpy 09:56:06] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 14]",
"[TransmogSpy 09:56:19] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=304077 displayType=1",
"[TransmogSpy 09:56:21] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=304082 displayType=1",
"[TransmogSpy 09:56:23] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=304084 displayType=1",
"[TransmogSpy 09:56:28] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=1 transmogID=224735 displayType=1",
"[TransmogSpy 09:56:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:56:33] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76834 displayType=1",
"[TransmogSpy 09:56:35] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76538 displayType=1",
"[TransmogSpy 09:56:38] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:56:39] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=77344 displayType=3",
"[TransmogSpy 09:56:41] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:56:41] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 09:56:44] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:56:44]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:56:44] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:56:45] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:56:45] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:57:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:57:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:57:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:57:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:57:18] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 09:57:20] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:57:21] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76829 displayType=1",
"[TransmogSpy 09:57:23] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76823 displayType=1",
"[TransmogSpy 09:57:27] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76837 displayType=1",
"[TransmogSpy 09:57:32] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:57:33] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=77344 displayType=3",
"[TransmogSpy 09:57:34] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:57:35] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:57:38] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:57:39] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:57:40] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 09:57:42] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=108785 displayType=3",
"[TransmogSpy 09:57:46] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 6]",
"[TransmogSpy 09:57:48] |cffffff44SetPendingTransmog|r: slot=5(TABARD) type=0 option=0 transmogID=83203 displayType=3",
"[TransmogSpy 09:57:49] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 5]",
"[TransmogSpy 09:57:50] |cffffff44SetPendingTransmog|r: slot=6(SHIRT) type=0 option=0 transmogID=83202 displayType=3",
"[TransmogSpy 09:57:52] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 12]",
"[TransmogSpy 09:57:55] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:57:57] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76829 displayType=1",
"[TransmogSpy 09:58:00] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=80758 displayType=1",
"[TransmogSpy 09:58:01] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=80759 displayType=1",
"[TransmogSpy 09:58:02] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=80757 displayType=1",
"[TransmogSpy 09:58:02] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=80756 displayType=1",
"[TransmogSpy 09:58:02] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76838 displayType=1",
"[TransmogSpy 09:58:03] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76837 displayType=1",
"[TransmogSpy 09:58:03] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76836 displayType=1",
"[TransmogSpy 09:58:03] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76833 displayType=1",
"[TransmogSpy 09:58:04] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76832 displayType=1",
"[TransmogSpy 09:58:04] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76830 displayType=1",
"[TransmogSpy 09:58:04] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76829 displayType=1",
"[TransmogSpy 09:58:05] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76825 displayType=1",
"[TransmogSpy 09:58:05] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76824 displayType=1",
"[TransmogSpy 09:58:06] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76831 displayType=1",
"[TransmogSpy 09:58:06] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76827 displayType=1",
"[TransmogSpy 09:58:07] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76823 displayType=1",
"[TransmogSpy 09:58:07] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76822 displayType=1",
"[TransmogSpy 09:58:08] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76821 displayType=1",
"[TransmogSpy 09:58:08] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76820 displayType=1",
"[TransmogSpy 09:58:09] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76835 displayType=1",
"[TransmogSpy 09:58:10] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76834 displayType=1",
"[TransmogSpy 09:58:12] |cffffff44SetPendingTransmog|r: slot=12(MAINHAND) type=0 option=8 transmogID=76834 displayType=1",
"[TransmogSpy 09:58:16] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:58:16]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:58:16] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:58:17] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:58:17] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:58:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:58:28] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:58:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 29]",
"[TransmogSpy 09:58:28] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:58:29] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:58:30] |cffffff44SetPendingTransmog|r: slot=3(BACK) type=0 option=0 transmogID=77345 displayType=3",
"[TransmogSpy 09:58:31] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:58:31]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:58:31] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:58:33] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:58:33] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:58:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:58:40] |cff44ffffVIEWED_TRANSMOG_OUTFIT_CHANGED|r: args=[none]",
"[TransmogSpy 09:58:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 3]",
"[TransmogSpy 09:58:40] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 1]",
"[TransmogSpy 09:58:51] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=297969 displayType=1",
"[TransmogSpy 09:58:53] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=299106 displayType=1",
"[TransmogSpy 09:58:55] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=295452 displayType=1",
"[TransmogSpy 09:58:58] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=300847 displayType=1",
"[TransmogSpy 09:59:00] |cffffff44SetPendingTransmog|r: slot=0(HEAD) type=0 option=0 transmogID=299164 displayType=1",
"[TransmogSpy 09:59:01] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
"[TransmogSpy 09:59:02] |cffffff44SetPendingTransmog|r: slot=1(SHOULDER) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:59:05] |cffffff44SetPendingTransmog|r: slot=2(?) type=0 option=0 transmogID=77343 displayType=3",
"[TransmogSpy 09:59:08] |cffffff44CommitAndApplyAllPending|r: useDiscount=false (post-hook, pending already cleared)",
"[TransmogSpy 09:59:08]   HasPendingOutfitTransmogs=true (should be false now)",
"[TransmogSpy 09:59:08] |cffffff44  (deferred comparison waiting for server response event)|r",
"[TransmogSpy 09:59:09] |cff44ffffVIEWED_TRANSMOG_OUTFIT_SITUATIONS_CHANGED|r: args=[none]",
"[TransmogSpy 09:59:09] |cff44ffffTRANSMOG_SEARCH_UPDATED|r: args=[1, 2]",
},
}

---

## 3. FrameXML.log — TransmogSpy Error
```
3/5 12:28:31.810  Interface/AddOns/TransmogSpy/TransmogSpy.lua:1 Interface/AddOns/TransmogSpy/TransmogSpy.lua:1184: '=' expected near 'continue'
```

---

## 4. Transmog Hotfix.log Entries (retail CDN)
=== TRANSMOG HOTFIX ENTRIES FROM RETAIL ===
Source: C:/WoW/_retail_/Logs/Hotfix.log (build 66263)

--- Table Counts ---
   3667 TransmogHoliday
    733 CollectableSourceVendorSparse
    733 CollectableSourceVendor
    153 ItemModifiedAppearanceExtra
    153 ItemModifiedAppearance
     73 CollectableSourceInfo
     54 ItemAppearance
     11 TransmogSet
      8 CollectableSourceEncounterSparse
      8 CollectableSourceEncounter
      6 TransmogSetItem

--- Full Entries ---
3/5 11:45:49.854  	103458 Table TransmogHoliday RecID 265100 VALIDATION_RESULT_INVALID
3/5 11:45:49.854  	103462 Table CollectableSourceInfo RecID 179889 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceInfo RecID 179920 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237398 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237398 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237399 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237399 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237400 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237400 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237401 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237401 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237402 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237402 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237403 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237403 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237404 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237404 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237405 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237405 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237406 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237406 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237407 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237407 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237444 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237444 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237445 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237445 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237446 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237446 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237447 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237447 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237448 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237448 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237449 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237449 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237450 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237450 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237451 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237451 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237452 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237452 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 237453 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 237453 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 244794 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 244794 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendorSparse RecID 244855 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103462 Table CollectableSourceVendor RecID 244855 VALIDATION_RESULT_VALID
3/5 11:45:49.854  	103470 Table TransmogHoliday RecID 264672 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200323 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200332 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200341 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200350 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200359 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200368 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200377 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200386 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200395 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200404 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200413 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200422 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 200431 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202438 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202447 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202456 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202465 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202474 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202483 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202492 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202501 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202510 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202519 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202528 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202537 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 202546 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207176 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207186 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207195 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207204 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207213 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207222 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207231 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207240 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207249 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207258 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207267 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207276 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103471 Table TransmogHoliday RecID 207285 VALIDATION_RESULT_INVALID
3/5 11:45:49.869  	103497 Table TransmogHoliday RecID 259240 VALIDATION_RESULT_INVALID
3/5 11:45:49.885  	103586 Table TransmogHoliday RecID 42106 VALIDATION_RESULT_INVALID
3/5 11:45:49.885  	103586 Table TransmogHoliday RecID 258136 VALIDATION_RESULT_INVALID
3/5 11:45:49.885  	103586 Table TransmogSet RecID 5335 VALIDATION_RESULT_NOTPUBLIC
3/5 11:45:49.885  	103596 Table TransmogSetItem RecID 100965 VALIDATION_RESULT_DELETE
3/5 11:45:49.885  	103596 Table TransmogSetItem RecID 100967 VALIDATION_RESULT_DELETE
3/5 11:45:49.885  	103596 Table TransmogSetItem RecID 101128 VALIDATION_RESULT_VALID
3/5 11:45:49.885  	103596 Table TransmogSetItem RecID 101129 VALIDATION_RESULT_VALID
3/5 11:45:49.885  	103596 Table TransmogSetItem RecID 105521 VALIDATION_RESULT_VALID
3/5 11:45:49.885  	103596 Table TransmogSetItem RecID 105522 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103605 Table TransmogHoliday RecID 252246 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103638 Table TransmogHoliday RecID 269897 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103638 Table TransmogHoliday RecID 269898 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103638 Table TransmogSet RecID 4968 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103655 Table TransmogHoliday RecID 243434 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103655 Table TransmogHoliday RecID 243442 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103655 Table TransmogHoliday RecID 243448 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245028 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245028 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245029 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245029 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245030 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245030 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245031 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245031 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245032 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245032 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245033 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245033 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245034 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245034 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245035 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245035 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245036 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245036 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245037 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245037 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245038 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245038 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245039 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245039 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245040 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245040 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245041 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245041 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245042 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245042 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245043 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245043 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245044 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245044 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245045 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245045 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245046 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245046 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245047 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245047 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245048 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245048 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245049 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245049 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245050 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245050 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245051 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245051 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendorSparse RecID 245052 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103669 Table CollectableSourceVendor RecID 245052 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269972 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269973 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269974 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269978 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269979 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269980 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269981 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269982 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269985 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269986 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269987 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table TransmogHoliday RecID 269988 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304843 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304843 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304844 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304844 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304845 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304845 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304846 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304846 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304847 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304847 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304848 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304848 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304849 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304849 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304850 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304850 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304851 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304851 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304852 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304852 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304853 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304853 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103733 Table ItemModifiedAppearance RecID 304854 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103733 Table ItemModifiedAppearanceExtra RecID 304854 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103746 Table TransmogHoliday RecID 263298 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103746 Table TransmogHoliday RecID 263299 VALIDATION_RESULT_INVALID
3/5 11:45:49.901  	103748 Table CollectableSourceEncounterSparse RecID 63648 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103748 Table CollectableSourceEncounter RecID 63648 VALIDATION_RESULT_DELETE
3/5 11:45:49.901  	103748 Table CollectableSourceEncounterSparse RecID 63785 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103748 Table CollectableSourceEncounter RecID 63785 VALIDATION_RESULT_VALID
3/5 11:45:49.901  	103748 Table CollectableSourceInfo RecID 180008 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceInfo RecID 180010 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73777 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73777 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73778 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73778 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73779 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73779 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73786 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73786 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73787 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73787 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73788 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73788 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73792 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73792 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73793 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73793 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73794 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73794 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73795 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73795 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73796 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73796 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73797 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73797 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73802 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73802 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73803 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73803 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73804 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73804 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73810 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73810 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73811 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73811 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73812 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73812 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73816 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73816 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73817 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73817 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73818 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73818 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73822 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73822 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73823 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73823 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73824 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73824 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73825 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73825 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73826 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73826 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73827 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73827 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73831 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73831 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73832 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73832 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73833 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73833 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73837 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73837 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73838 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73838 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73839 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73839 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73840 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73840 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73841 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73841 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73843 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73843 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73844 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73844 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73845 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73845 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73850 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73850 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73851 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73851 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73852 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73852 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73855 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73855 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73856 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73856 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73857 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73857 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73865 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73865 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73866 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73866 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73867 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73867 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73875 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73875 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73876 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73876 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73877 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73877 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73886 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73886 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73887 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73887 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73888 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73888 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73895 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73895 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73896 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73896 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73897 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73897 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73905 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73905 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73906 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73906 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73907 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73907 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73922 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73922 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73923 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73923 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73924 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73924 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73932 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73932 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73933 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73933 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73934 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73934 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73935 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73935 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73936 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73936 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73937 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73937 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73945 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73945 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73946 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73946 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73947 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73947 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73955 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73955 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73956 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73956 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73957 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73957 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73965 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73965 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73966 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73966 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73967 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73967 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73975 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73975 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73976 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73976 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73977 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73977 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73988 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73988 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73989 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73989 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73990 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73990 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73992 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73992 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73993 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73993 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 73994 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 73994 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74000 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74000 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74001 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74001 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74002 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74002 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74006 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74006 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74007 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74007 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74008 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74008 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74009 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74009 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74013 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74013 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74014 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74014 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74018 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74018 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74019 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74019 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74020 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74020 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74022 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74022 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74025 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74025 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74026 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74026 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74027 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74027 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74028 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74028 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74029 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74029 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74036 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74036 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74037 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74037 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74038 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74038 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74042 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74042 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74043 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74043 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74044 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74044 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74045 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74045 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74046 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74046 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74047 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74047 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74054 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74054 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74055 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74055 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74056 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74056 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74060 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74060 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74061 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74061 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74062 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74062 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74066 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74066 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74067 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74067 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 74068 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 74068 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 75949 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 75949 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 75950 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 75950 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 75951 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 75951 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 77055 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 77055 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 77056 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 77056 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 77057 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 77057 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 157326 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 157326 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 157327 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 157327 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 157328 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 157328 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 157329 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 157329 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 157330 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 157330 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 158391 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 158391 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 158392 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 158392 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 158393 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 158393 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 159177 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 159177 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 159178 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 159178 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 159179 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 159179 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245055 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245055 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245056 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245056 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245057 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245057 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245058 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245058 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245059 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245059 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245060 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245060 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245061 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245061 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245062 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245062 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245063 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245063 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245064 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245064 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245065 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245065 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245066 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245066 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245067 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245067 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245068 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245068 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245069 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245069 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245070 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245070 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245071 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245071 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245072 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245072 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245073 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245073 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245074 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245074 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245075 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245075 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245076 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245076 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245077 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245077 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245078 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245078 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245079 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245079 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245080 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245080 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245081 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245081 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245082 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245082 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245083 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245083 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245084 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245084 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245085 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245085 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245086 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245086 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245087 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245087 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245088 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245088 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245089 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245089 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245090 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245090 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245091 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245091 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245092 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245092 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245093 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245093 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245094 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245094 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245095 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245095 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245096 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245096 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245097 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245097 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245098 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245098 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245099 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245099 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245100 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245100 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245101 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245101 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245102 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245102 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245103 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245103 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245104 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245104 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245105 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245105 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245106 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245106 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245107 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245107 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245108 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245108 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245109 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245109 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245110 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245110 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245111 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245111 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245112 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245112 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245113 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245113 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245114 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245114 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245115 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245115 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245116 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245116 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245117 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245117 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245118 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245118 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245119 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245119 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245120 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245120 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245121 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245121 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245122 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245122 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245123 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245123 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245124 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245124 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245125 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245125 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245126 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245126 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245127 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245127 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245128 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245128 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245129 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245129 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245130 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245130 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245131 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245131 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245132 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245132 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245133 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245133 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245134 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245134 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245135 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245135 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245136 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245136 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245137 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245137 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245138 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245138 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245139 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245139 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245140 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245140 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245141 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245141 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245142 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245142 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245143 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245143 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245144 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245144 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245145 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245145 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245146 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245146 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245147 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245147 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245148 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245148 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245149 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245149 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245150 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245150 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245151 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245151 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245152 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245152 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245153 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245153 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245154 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245154 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245155 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245155 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245156 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245156 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245157 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245157 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245158 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245158 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245159 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245159 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245160 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245160 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245161 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245161 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245162 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245162 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245163 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245163 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245164 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245164 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245165 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245165 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245166 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245166 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245167 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245167 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245168 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245168 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245169 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245169 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245170 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245170 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245171 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245171 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245172 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245172 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245173 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245173 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245174 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245174 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245175 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245175 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245176 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245176 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245177 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245177 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245178 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245178 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245179 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245179 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245180 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245180 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245181 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245181 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245182 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245182 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245183 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245183 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245184 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245184 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245185 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245185 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendorSparse RecID 245186 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table CollectableSourceVendor RecID 245186 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table TransmogHoliday RecID 269992 VALIDATION_RESULT_INVALID
3/5 11:45:49.917  	103788 Table ItemModifiedAppearance RecID 304855 VALIDATION_RESULT_VALID
3/5 11:45:49.917  	103788 Table ItemModifiedAppearanceExtra RecID 304855 VALIDATION_RESULT_DELETE
3/5 11:45:49.917  	103791 Table TransmogHoliday RecID 259221 VALIDATION_RESULT_INVALID
3/5 11:45:49.917  	103814 Table TransmogHoliday RecID 238677 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256626 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256627 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256628 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256629 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256630 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256631 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256632 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256633 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256634 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256635 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256641 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256643 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256644 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256646 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256649 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103870 Table TransmogHoliday RecID 256654 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103883 Table TransmogHoliday RecID 259366 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103887 Table TransmogHoliday RecID 256702 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103887 Table TransmogHoliday RecID 256706 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103887 Table TransmogHoliday RecID 256710 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103887 Table TransmogHoliday RecID 256712 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103887 Table TransmogHoliday RecID 256719 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103950 Table TransmogHoliday RecID 238543 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103952 Table TransmogHoliday RecID 238581 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103953 Table TransmogHoliday RecID 238538 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103954 Table TransmogHoliday RecID 238595 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103955 Table TransmogHoliday RecID 238572 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103955 Table TransmogHoliday RecID 238573 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103955 Table TransmogHoliday RecID 238574 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103955 Table TransmogHoliday RecID 238577 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103955 Table TransmogHoliday RecID 238578 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103955 Table TransmogHoliday RecID 238579 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103956 Table TransmogHoliday RecID 238584 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103957 Table TransmogHoliday RecID 238583 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103958 Table TransmogHoliday RecID 263458 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103959 Table TransmogHoliday RecID 238549 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103959 Table TransmogHoliday RecID 238550 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103959 Table TransmogHoliday RecID 238551 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103959 Table TransmogHoliday RecID 238552 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103960 Table TransmogHoliday RecID 238540 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103961 Table TransmogHoliday RecID 238592 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103962 Table TransmogHoliday RecID 238537 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103963 Table TransmogHoliday RecID 267655 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103964 Table TransmogHoliday RecID 259190 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103993 Table TransmogHoliday RecID 258294 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103993 Table TransmogHoliday RecID 262880 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	103997 Table TransmogHoliday RecID 257241 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	104015 Table TransmogHoliday RecID 241284 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	104015 Table TransmogHoliday RecID 241285 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	104015 Table TransmogHoliday RecID 241318 VALIDATION_RESULT_INVALID
3/5 11:45:49.933  	104015 Table TransmogHoliday RecID 241319 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104021 Table TransmogHoliday RecID 248409 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104028 Table ItemModifiedAppearance RecID 300855 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104028 Table ItemModifiedAppearanceExtra RecID 300855 VALIDATION_RESULT_DELETE
3/5 11:45:49.948  	104079 Table TransmogHoliday RecID 256701 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104079 Table TransmogHoliday RecID 256703 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104079 Table TransmogHoliday RecID 256705 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104079 Table TransmogHoliday RecID 256707 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104079 Table TransmogHoliday RecID 256709 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104079 Table TransmogHoliday RecID 256711 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104079 Table TransmogHoliday RecID 256713 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256639 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256655 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256657 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256658 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256659 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256660 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256661 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256662 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256663 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256664 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256665 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256666 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256667 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256668 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256669 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256670 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 256671 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 259368 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 259371 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104082 Table TransmogHoliday RecID 259457 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104092 Table TransmogHoliday RecID 267053 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104092 Table TransmogHoliday RecID 267055 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104092 Table TransmogHoliday RecID 267057 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104092 Table TransmogHoliday RecID 267061 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104092 Table TransmogHoliday RecID 267063 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104096 Table TransmogHoliday RecID 259182 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104096 Table TransmogHoliday RecID 268476 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104096 Table TransmogHoliday RecID 268478 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180011 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180012 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180013 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180014 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180015 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180016 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180017 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceInfo RecID 180018 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245187 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245187 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245188 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245188 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245189 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245189 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245190 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245190 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245191 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245191 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245192 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245192 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245193 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245193 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendorSparse RecID 245194 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104106 Table CollectableSourceVendor RecID 245194 VALIDATION_RESULT_VALID
3/5 11:45:49.948  	104113 Table TransmogHoliday RecID 253625 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259231 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259233 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259235 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259237 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259317 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259318 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259319 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104140 Table TransmogHoliday RecID 259322 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104142 Table TransmogHoliday RecID 259206 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104142 Table TransmogHoliday RecID 259208 VALIDATION_RESULT_INVALID
3/5 11:45:49.948  	104142 Table TransmogHoliday RecID 259210 VALIDATION_RESULT_INVALID
3/5 11:45:49.963  	104198 Table TransmogHoliday RecID 250225 VALIDATION_RESULT_INVALID
3/5 11:45:49.963  	104211 Table TransmogHoliday RecID 253244 VALIDATION_RESULT_INVALID
3/5 11:45:49.963  	104211 Table TransmogHoliday RecID 253257 VALIDATION_RESULT_INVALID
3/5 11:45:49.963  	104211 Table TransmogHoliday RecID 253296 VALIDATION_RESULT_INVALID
3/5 11:45:49.963  	104211 Table TransmogHoliday RecID 253404 VALIDATION_RESULT_INVALID
3/5 11:45:49.963  	104211 Table TransmogHoliday RecID 256141 VALIDATION_RESULT_INVALID
3/5 11:45:49.963  	104211 Table TransmogHoliday RecID 258840 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104251 Table TransmogHoliday RecID 240484 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104251 Table TransmogHoliday RecID 240485 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104272 Table TransmogHoliday RecID 238526 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104272 Table TransmogHoliday RecID 238527 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104272 Table TransmogHoliday RecID 242547 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104272 Table TransmogHoliday RecID 245653 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104272 Table TransmogHoliday RecID 248017 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104272 Table TransmogHoliday RecID 248142 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104272 Table TransmogHoliday RecID 251543 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104332 Table TransmogHoliday RecID 262793 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104336 Table TransmogSet RecID 5336 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104336 Table TransmogSet RecID 5381 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104336 Table TransmogSet RecID 5382 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104355 Table TransmogHoliday RecID 258321 VALIDATION_RESULT_INVALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293078 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293078 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293079 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293079 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293080 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293080 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293081 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293081 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293082 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293082 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293083 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293083 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293084 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293084 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293085 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293085 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293086 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293086 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293087 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293087 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293088 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293088 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293089 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293089 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293090 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293090 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293091 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293091 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293092 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293092 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293093 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293093 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293094 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293094 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293095 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293095 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293096 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293096 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293097 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293097 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293098 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293098 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293099 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293099 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293100 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293100 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293101 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293101 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293102 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293102 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293103 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293103 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293104 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293104 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293105 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293105 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293106 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293106 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293107 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293107 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293108 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293108 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293109 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293109 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293110 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293110 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293111 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293111 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293112 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293112 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293113 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293113 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293114 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293114 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293115 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293115 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293116 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293116 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293117 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293117 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293118 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293118 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293119 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293119 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293120 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293120 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293121 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293121 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293122 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293122 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293123 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293123 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 293248 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 293248 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295411 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295411 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295412 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295412 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295413 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295413 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295414 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295414 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295415 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295415 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295416 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295416 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295417 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295417 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 295418 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 295418 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298275 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298275 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298276 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298276 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298277 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298277 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298278 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298278 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298279 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298279 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298280 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298280 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298281 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298281 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298282 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298282 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298283 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298283 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298284 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298284 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298285 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298285 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298286 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298286 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298287 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298287 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298288 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298288 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298289 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298289 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298290 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298290 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298291 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298291 VALIDATION_RESULT_DELETE
3/5 11:45:49.978  	104365 Table ItemModifiedAppearance RecID 298292 VALIDATION_RESULT_VALID
3/5 11:45:49.978  	104365 Table ItemModifiedAppearanceExtra RecID 298292 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298293 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298293 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298294 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298294 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298295 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298295 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298296 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298296 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298297 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298297 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298298 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298298 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298299 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298299 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298300 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298300 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298301 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298301 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298302 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298302 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298303 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298303 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298304 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298304 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298305 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298305 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298306 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298306 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298307 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298307 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298308 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298308 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298309 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298309 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298310 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298310 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298311 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298311 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298312 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298312 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298313 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298313 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298314 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298314 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298315 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298315 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298316 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298316 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298317 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298317 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298318 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298318 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298319 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298319 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 298320 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 298320 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 304839 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 304839 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104365 Table ItemModifiedAppearance RecID 304840 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104365 Table ItemModifiedAppearanceExtra RecID 304840 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104376 Table TransmogHoliday RecID 244174 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256625 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256637 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256638 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256640 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256647 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256652 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256653 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104378 Table TransmogHoliday RecID 256656 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104388 Table TransmogHoliday RecID 251110 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104388 Table TransmogHoliday RecID 265701 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104392 Table TransmogHoliday RecID 245829 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 232382 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 236953 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 236954 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 239594 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240207 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240208 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240926 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240927 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240928 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240929 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240930 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104445 Table TransmogHoliday RecID 240931 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104456 Table TransmogHoliday RecID 230722 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104456 Table TransmogHoliday RecID 244354 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104456 Table TransmogHoliday RecID 248242 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104464 Table TransmogHoliday RecID 250229 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104468 Table TransmogHoliday RecID 250244 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104471 Table TransmogHoliday RecID 262431 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266263 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266264 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266265 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266266 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266267 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266268 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266269 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266270 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 266271 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270430 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270431 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270433 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270439 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270440 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270441 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270442 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270443 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table TransmogHoliday RecID 270444 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304104 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304104 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304105 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304105 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304106 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304106 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304107 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304107 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304108 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304108 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304109 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304109 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304112 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304112 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 304113 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 304113 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305111 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305111 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305112 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305112 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305114 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305114 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305115 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305115 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305116 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305116 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305117 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305117 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305118 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305118 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104475 Table ItemModifiedAppearance RecID 305119 VALIDATION_RESULT_VALID
3/5 11:45:49.994  	104475 Table ItemModifiedAppearanceExtra RecID 305119 VALIDATION_RESULT_DELETE
3/5 11:45:49.994  	104478 Table TransmogHoliday RecID 258737 VALIDATION_RESULT_INVALID
3/5 11:45:49.994  	104478 Table TransmogHoliday RecID 266239 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104537 Table TransmogHoliday RecID 259996 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104560 Table TransmogHoliday RecID 253508 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104564 Table TransmogHoliday RecID 262349 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104565 Table TransmogHoliday RecID 265528 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104565 Table TransmogHoliday RecID 265530 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104565 Table TransmogHoliday RecID 265532 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104565 Table TransmogHoliday RecID 265534 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104565 Table TransmogHoliday RecID 265536 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104578 Table TransmogHoliday RecID 242787 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104599 Table TransmogHoliday RecID 252421 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104636 Table TransmogHoliday RecID 248138 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104651 Table TransmogHoliday RecID 251518 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104664 Table TransmogHoliday RecID 269269 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 236963 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 236965 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 237015 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 237016 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 247811 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 257751 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 257752 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104666 Table TransmogHoliday RecID 266262 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180005 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180019 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180020 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180021 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180022 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180023 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180024 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180025 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180026 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceInfo RecID 180027 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245024 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245024 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245025 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245025 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245026 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245026 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245027 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245027 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245195 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245195 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245196 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245196 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245197 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245197 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245198 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245198 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245199 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245199 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245200 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245200 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245201 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245201 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245202 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245202 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendorSparse RecID 245203 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table CollectableSourceVendor RecID 245203 VALIDATION_RESULT_VALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 17704 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 17721 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 32915 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 32917 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 32918 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 32919 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 32920 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 33017 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 33018 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 33019 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 33020 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 33021 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 33957 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 34140 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37127 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37128 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37597 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37893 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37894 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37895 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37896 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 37897 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 38175 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 49120 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 49128 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 51804 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 51805 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 51806 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 51807 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 51808 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 66540 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 68172 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 68173 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 68174 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 68175 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 68176 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 71325 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 71326 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 71331 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 71332 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 87569 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 87570 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 93625 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 107217 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 107218 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135679 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135680 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135684 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135688 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135792 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135793 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135796 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135801 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135905 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135906 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135909 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 135914 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136018 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136019 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136022 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136027 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136861 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136862 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136863 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136864 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136865 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136866 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136867 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136868 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136869 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136870 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136871 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136872 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136879 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136880 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136881 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136882 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136885 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136886 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136887 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 136888 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138364 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138365 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138366 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138367 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138368 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138369 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138370 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138371 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138372 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138373 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138374 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 138375 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142648 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142649 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142652 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142653 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142656 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142657 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142761 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142762 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142765 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142766 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142769 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142770 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142874 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142875 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142878 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142879 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142882 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142883 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142987 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142988 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142991 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142992 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142995 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 142996 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143286 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143287 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143288 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143289 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143290 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143291 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143292 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143293 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143294 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143295 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143296 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143297 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143304 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143305 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143306 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143307 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143310 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143311 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143312 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143313 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143316 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143317 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143318 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 143319 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144534 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144535 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144536 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144537 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144538 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144539 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144540 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144541 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144542 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144543 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144544 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144545 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144546 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144547 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144548 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144549 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144550 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144551 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144552 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144553 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144554 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144555 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144556 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 144557 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145026 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145027 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145028 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145029 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145030 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145031 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145032 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145033 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145034 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145035 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145036 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145037 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145038 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145039 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145040 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145041 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145042 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145043 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145044 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145045 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145046 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145047 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145048 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145049 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145376 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145377 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145378 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145379 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145380 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145381 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145382 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145383 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145384 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145385 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145386 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145387 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145388 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145389 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145390 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145391 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145392 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145393 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145394 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145395 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145396 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145397 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145398 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145399 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145868 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145869 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145870 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145871 VALIDATION_RESULT_INVALID
3/5 11:45:50.009  	104681 Table TransmogHoliday RecID 145872 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145873 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145874 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145875 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145876 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145877 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145878 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145879 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145880 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145881 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145882 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145883 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145884 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145885 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145886 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145887 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145888 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145889 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145890 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 145891 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147122 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147128 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147134 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147140 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147145 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147152 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147158 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147163 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147170 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147176 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147181 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147188 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147909 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147910 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147911 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147912 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147913 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147914 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147915 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147916 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147917 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147918 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147919 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147920 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147921 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147922 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147923 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147924 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147925 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147926 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147927 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147928 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147929 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147930 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147931 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 147932 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148402 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148403 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148404 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148405 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148406 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148407 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148408 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148409 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148410 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148411 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148412 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148413 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148414 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148415 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148416 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148417 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148418 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148419 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148420 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148421 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148422 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148423 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148424 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148425 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148894 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148895 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148896 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148897 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148898 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148899 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148900 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148901 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148902 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148903 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148904 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148905 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148906 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148907 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148908 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148909 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148910 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148911 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148912 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148913 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148914 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148915 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148916 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 148917 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149505 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149506 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149507 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149508 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149509 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149510 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149511 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149512 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149513 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149514 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149515 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149516 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149517 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149518 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149519 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149520 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149521 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149522 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149523 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149524 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149525 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149526 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149527 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149528 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149756 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149757 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149758 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149759 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149760 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149761 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149762 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149763 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149764 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149765 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149766 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149767 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149768 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149769 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149770 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149771 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149772 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149773 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149774 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149775 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149776 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149777 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149778 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 149779 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150002 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150003 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150004 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150005 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150006 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150007 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150008 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150009 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150010 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150011 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150012 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150013 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150014 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150015 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150016 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150017 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150018 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150019 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150020 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150021 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150022 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150023 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150024 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 150025 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 151790 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 151791 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 151792 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152113 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152119 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152125 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152131 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152136 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152143 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152149 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152154 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152161 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152167 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152172 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 152179 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167207 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167208 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167212 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167213 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167214 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167215 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167220 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167221 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167222 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167223 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167226 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167227 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167229 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167230 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 167998 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 169448 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188236 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188237 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188238 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188239 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188240 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188241 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188242 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188243 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188244 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188245 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188246 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188247 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188248 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188249 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188250 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188251 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188628 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188629 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188630 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188631 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188632 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188633 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188634 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188635 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188636 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188637 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188638 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188639 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188846 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188871 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188872 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188873 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188882 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188891 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188900 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188909 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188918 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188927 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188936 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 188945 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 190065 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 190066 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 190203 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 190204 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206588 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206589 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206590 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206591 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206592 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206593 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206594 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206764 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206765 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206766 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206767 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206768 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206769 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206770 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206776 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206777 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206778 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206779 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206780 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206781 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206782 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206783 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206784 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206785 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206786 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206788 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206789 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206790 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206791 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206792 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206793 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206794 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206795 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206796 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206797 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206798 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206799 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206800 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206801 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206802 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206803 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206804 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206806 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206807 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206808 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206809 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206810 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206812 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206814 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206816 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206817 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206818 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206819 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206821 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206822 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206823 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206824 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206825 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206826 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206827 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206828 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206829 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206831 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206832 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206833 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206834 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206835 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206836 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206837 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206838 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206839 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206840 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206841 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206842 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206843 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206844 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206845 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206846 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206847 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206848 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206849 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206850 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206851 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206852 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206853 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206854 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206855 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206856 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206857 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206858 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206860 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206861 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206862 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206863 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206864 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206865 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206866 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206867 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206868 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206869 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206870 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206871 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206872 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206873 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206874 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206875 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206876 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206877 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206878 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206879 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206880 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206881 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206882 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206883 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206884 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206885 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206886 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206887 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206888 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206889 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206890 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206891 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206892 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206893 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206894 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206895 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206896 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206897 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206898 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206899 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206900 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206901 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206902 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206903 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206904 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206905 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206906 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206907 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206908 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206909 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206910 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206911 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206912 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206913 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206914 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206915 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206916 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206917 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206918 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206919 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206920 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206921 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206922 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206923 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206924 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 206925 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 207014 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 207015 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 207016 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 207017 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 207018 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 207044 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 207045 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 208149 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 208150 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 208423 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 208832 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 209038 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 209039 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 209040 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 209053 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210065 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210066 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210067 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210068 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210071 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210072 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210073 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210074 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210075 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 210076 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211096 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211097 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211099 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211145 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211159 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211259 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211294 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211295 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211298 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211299 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211877 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211881 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211882 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211883 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211884 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211885 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211886 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211887 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211888 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211926 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 211928 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212336 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212607 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212626 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212644 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212686 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212874 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212875 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212876 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212877 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212878 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212879 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212880 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 212881 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213436 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213585 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213586 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213587 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213588 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213589 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213590 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213591 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213592 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213593 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 213635 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216727 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216728 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216729 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216730 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216731 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216732 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216733 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216734 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216735 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216755 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216756 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216763 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216765 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216774 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216775 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216776 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216777 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216778 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216779 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216780 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216984 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216985 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216986 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216987 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216988 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216989 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216990 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216991 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216992 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216993 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 216994 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217738 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217739 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217740 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217741 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217742 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217743 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217744 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217745 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217746 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217747 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217748 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217749 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217750 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217751 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217752 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217753 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217754 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217755 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217756 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217757 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217758 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217759 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217760 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217761 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217762 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217763 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217764 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217765 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217766 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217767 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217768 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217769 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217770 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217771 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217772 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217773 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217774 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217775 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217776 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217777 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217778 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217779 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217780 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217781 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217782 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217783 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217784 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217785 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217786 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217787 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217788 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217789 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217790 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217791 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217792 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217793 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217794 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217795 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217796 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217797 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217798 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217799 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217800 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217801 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217802 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217803 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217804 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217805 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217806 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217807 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217808 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217809 VALIDATION_RESULT_INVALID
3/5 11:45:50.026  	104681 Table TransmogHoliday RecID 217810 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 217811 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 217812 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 217813 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 217815 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 219348 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 219349 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223550 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223551 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223552 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223553 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223554 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223555 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223556 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223566 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223568 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223598 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223599 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223600 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223601 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223602 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223603 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223604 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223605 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 223606 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224195 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224196 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224197 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224198 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224199 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224200 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224201 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224202 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224203 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224204 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224205 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224206 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224207 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224208 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224209 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224210 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224211 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224212 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224213 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224214 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224215 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224216 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224217 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224218 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224219 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224220 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224221 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224222 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224223 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224224 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224225 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224226 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224227 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224228 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224229 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224230 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224231 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224241 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224242 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224243 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224244 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224245 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224246 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224247 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224248 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224249 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224468 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224469 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224470 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224471 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224472 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224473 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224474 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224475 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224476 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224894 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224895 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224896 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224897 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224898 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224899 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224900 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224901 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224902 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224923 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224924 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224925 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224926 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224927 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224928 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224929 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224930 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224931 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224951 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224952 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224953 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224954 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224955 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224956 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224957 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224958 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224959 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224983 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224984 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224985 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224986 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224987 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224988 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224989 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224990 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 224991 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225010 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225011 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225012 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225013 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225014 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225015 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225016 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225017 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225018 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225037 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225038 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225039 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225040 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225041 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225042 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225043 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225044 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225045 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225069 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225070 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225071 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225072 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225073 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225074 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225075 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225076 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225077 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225096 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225097 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225098 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225099 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225100 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225101 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225102 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225103 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225104 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225124 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225125 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225126 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225127 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225128 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225129 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225130 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225131 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225132 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225151 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225152 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225153 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225154 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225155 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225156 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225157 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225158 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 225159 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226363 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226427 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226453 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226454 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226455 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226456 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226457 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226458 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226461 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 226690 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 227795 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 228784 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 228785 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 228786 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 228788 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 229818 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 229819 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 229820 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 229821 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 230035 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 230056 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 230076 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 231906 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 231907 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232479 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232480 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232481 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232482 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232483 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232484 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232910 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 232916 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 233221 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 233239 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 233928 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 233929 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 233932 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234448 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234709 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234710 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234711 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234712 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234713 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234714 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 234715 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 235021 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 235150 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 235212 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 235214 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 235279 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 238952 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 239170 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 239214 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 241644 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 241645 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 241647 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242409 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242438 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242892 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242893 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242894 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242895 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242896 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242897 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242898 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242899 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242900 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242901 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242902 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242903 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242904 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242905 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242906 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242907 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242908 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242909 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242910 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242911 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242912 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242913 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242914 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242915 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242916 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242917 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242918 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242920 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242921 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242922 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242923 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242924 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242925 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242926 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242927 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242928 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242929 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242930 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242931 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242932 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242933 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242934 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242935 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242936 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242937 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242938 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242939 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242940 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242941 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242942 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242943 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242944 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242945 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242946 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242948 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242953 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242954 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242955 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242956 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242957 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242958 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242959 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242960 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242961 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242962 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242963 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242964 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242965 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242966 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242967 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242968 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242969 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242970 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242971 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242972 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242973 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242974 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242975 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242976 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242977 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242978 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242979 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242990 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242991 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242992 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242993 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242994 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242995 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242996 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242997 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 242998 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 243101 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 243327 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 243336 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244228 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244229 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244230 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244313 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244314 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244317 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244318 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244319 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244323 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244352 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244371 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244372 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244373 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244374 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244375 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244376 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244377 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244378 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244379 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244392 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244393 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244394 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244395 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244396 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244397 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244398 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244399 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244400 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244401 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244412 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244413 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244414 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244415 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244416 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244417 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244418 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244419 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244420 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244443 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244444 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244446 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244447 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 244448 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245305 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245312 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245323 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245326 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245396 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245406 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245407 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245408 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245412 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245414 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245415 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245416 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245418 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245421 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245428 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245432 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245436 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245441 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245459 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245484 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245496 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245499 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245502 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245503 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245509 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245513 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245514 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245517 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245534 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245557 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245559 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245600 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245601 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245602 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245618 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245621 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245622 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245623 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245950 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 245959 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246066 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246111 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246228 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246229 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246230 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246231 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246232 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246233 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246234 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246235 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246410 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246413 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246420 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246423 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246460 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246486 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246488 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246489 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246500 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246629 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246630 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246631 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246632 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246633 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246634 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246635 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246636 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246637 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246638 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246639 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246640 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246641 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246642 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246643 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246644 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246645 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246646 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246647 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246648 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246649 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246650 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246651 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246652 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246653 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246654 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246655 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246656 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246657 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246658 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246659 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246660 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246662 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246663 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246664 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246665 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246666 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246667 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246668 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246669 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246670 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246672 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246673 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246674 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246675 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246676 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246677 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246678 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246679 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246685 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246693 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246700 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246705 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246708 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246709 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246786 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246793 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246966 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246967 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246968 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246969 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246970 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246971 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246972 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246991 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246995 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 246997 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247220 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247222 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247224 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247225 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247661 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247669 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247714 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247715 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247716 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247717 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247728 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247731 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247733 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247735 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247736 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247738 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247752 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247767 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247856 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247897 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247898 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247899 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247900 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247901 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247903 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247904 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247905 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247909 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247916 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247918 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247920 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247922 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247923 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247925 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247964 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247965 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247966 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247967 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247968 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247969 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247971 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247972 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247974 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247975 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247976 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247977 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247978 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247979 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247980 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247981 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247983 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247984 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247985 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247986 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247987 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247988 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247989 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 247990 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248010 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248106 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248107 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248108 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248109 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248110 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248111 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248113 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248114 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248118 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248119 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248120 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248121 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248210 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248211 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248212 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248213 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248214 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248215 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248216 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248217 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248218 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248245 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248319 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248320 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248321 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248322 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248323 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248324 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248325 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248326 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248394 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248654 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248657 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 248933 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249143 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249434 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249435 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249436 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249560 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249561 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249562 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249563 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249564 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249565 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 249904 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 250706 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 250707 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 250708 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 250709 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251482 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251495 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251542 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251546 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251550 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251563 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251564 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251565 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251566 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251567 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251568 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251569 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251570 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251571 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251572 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251573 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251574 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251575 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251576 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251577 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251578 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251579 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251580 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251581 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251582 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251583 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251584 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251585 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251586 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251587 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251588 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251589 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251590 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251591 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251592 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251593 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251594 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251595 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251596 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251597 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251598 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251599 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251600 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251601 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251602 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251603 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251604 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251605 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251606 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251607 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251608 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251609 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251610 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251611 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251612 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 251655 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 252035 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 252389 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 252397 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 252399 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 252401 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 252755 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 252758 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253022 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253036 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253039 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253164 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253165 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253167 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253169 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253171 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253250 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253252 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253253 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253380 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253381 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253552 VALIDATION_RESULT_INVALID
3/5 11:45:50.040  	104681 Table TransmogHoliday RecID 253553 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 253554 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 253555 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 254736 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 255973 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 256170 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 256171 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 256356 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 256427 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 256430 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 256680 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 256681 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257035 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257036 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257037 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257038 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257039 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257040 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257041 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257042 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257043 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257044 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257045 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257046 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257047 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257048 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257049 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257050 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257051 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257052 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257053 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257093 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257094 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257095 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257096 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257097 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257098 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257100 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257101 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257102 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257400 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257402 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257404 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257406 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257409 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257420 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257689 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257693 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257694 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257695 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257696 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257725 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 257806 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258135 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258190 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258191 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258192 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258193 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258194 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258195 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258196 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258197 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258198 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258199 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258200 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258201 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258202 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258203 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258204 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258205 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258206 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258207 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258208 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258209 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258210 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258211 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258212 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258213 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258214 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258215 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258216 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258220 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258222 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258224 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258225 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258226 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258227 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258235 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258237 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258238 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258239 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258240 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258242 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258244 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258245 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258247 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258248 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258250 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258252 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258253 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258289 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258298 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258302 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258303 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258557 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258558 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258559 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258560 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258561 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258742 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258748 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258812 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258814 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258815 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258816 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258817 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258820 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258821 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258822 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258824 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258825 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258826 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258827 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258828 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258829 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258830 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258831 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258832 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 258833 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 260415 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 260699 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262347 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262354 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262355 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262356 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262450 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262451 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262452 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262455 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262456 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262457 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262458 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262459 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262460 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262461 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262465 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262468 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262470 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262589 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262590 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 262663 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 263027 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 263500 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 263501 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 263502 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 263503 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 263504 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 263506 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264676 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264677 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264678 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264679 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264705 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264706 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264707 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264708 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264709 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264710 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264711 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264712 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264713 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264899 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 264900 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 268038 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 268039 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 268041 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 269009 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogHoliday RecID 269743 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104681 Table TransmogSet RecID 5163 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104681 Table TransmogSet RecID 5373 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104681 Table TransmogSet RecID 5374 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104681 Table TransmogSet RecID 5375 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104681 Table TransmogSet RecID 5376 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104694 Table TransmogHoliday RecID 211812 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104736 Table TransmogHoliday RecID 151060 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104736 Table TransmogHoliday RecID 271616 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104741 Table TransmogHoliday RecID 45195 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180233 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180234 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180235 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180236 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180237 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180238 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180239 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180240 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180241 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180242 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180243 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceInfo RecID 180244 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245238 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245238 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245239 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245239 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245240 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245240 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245241 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245241 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245242 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245242 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245243 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245243 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245244 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245244 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245245 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245245 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245246 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245246 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245247 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245247 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245248 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245248 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245249 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245249 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245250 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245250 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245251 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245251 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245252 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245252 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245253 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245253 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245254 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245254 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245255 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245255 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245256 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245256 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245257 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245257 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245258 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245258 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245259 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245259 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245260 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245260 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245261 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245261 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245262 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245262 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245263 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245263 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245264 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245264 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245265 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245265 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245266 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245266 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245267 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245267 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245268 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245268 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245269 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245269 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245270 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245270 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245271 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245271 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245272 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245272 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245273 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245273 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245274 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245274 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245275 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245275 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245276 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245276 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245277 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245277 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245278 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245278 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245279 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245279 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245280 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245280 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245281 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245281 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245282 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245282 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245283 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245283 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245284 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245284 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245285 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245285 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245286 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245286 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245287 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245287 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245288 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245288 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245289 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245289 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245290 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245290 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245291 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245291 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245292 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245292 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245293 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245293 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245294 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245294 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245295 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245295 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245296 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245296 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245297 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245297 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245298 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245298 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245299 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245299 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245300 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245300 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245301 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245301 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245302 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245302 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245303 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245303 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245304 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245304 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245305 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245305 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245306 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245306 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245307 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245307 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245308 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245308 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245309 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245309 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245310 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245310 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245311 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245311 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245312 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245312 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245313 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245313 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245314 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245314 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245315 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245315 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245316 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245316 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245317 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245317 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245318 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245318 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245319 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245319 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245320 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245320 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245321 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245321 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245322 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245322 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245323 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245323 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245324 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245324 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245325 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245325 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245326 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245326 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245327 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245327 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245328 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245328 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245329 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245329 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245330 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245330 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245331 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245331 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245332 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245332 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245333 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245333 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245334 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245334 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245335 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245335 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245336 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245336 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245337 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245337 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245338 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245338 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245339 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245339 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245340 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245340 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245341 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245341 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245342 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245342 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245343 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245343 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245344 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245344 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245345 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245345 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245346 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245346 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245347 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245347 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245348 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245348 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245349 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245349 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245350 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245350 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245351 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245351 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245352 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245352 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245353 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245353 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245354 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245354 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245355 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245355 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245356 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245356 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245357 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245357 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245358 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245358 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245359 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245359 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245360 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245360 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245361 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245361 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245362 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245362 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245363 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245363 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245364 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245364 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245365 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245365 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245366 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245366 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245367 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245367 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245368 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245368 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245369 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245369 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245370 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245370 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245371 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245371 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245372 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245372 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendorSparse RecID 245373 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table CollectableSourceVendor RecID 245373 VALIDATION_RESULT_VALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 256764 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 260785 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 263383 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264278 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264279 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264280 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264281 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264282 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264283 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264384 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264396 VALIDATION_RESULT_INVALID
3/5 11:45:50.057  	104743 Table TransmogHoliday RecID 264397 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104857 Table TransmogHoliday RecID 248555 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104898 Table TransmogHoliday RecID 259113 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104898 Table TransmogHoliday RecID 259115 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104898 Table TransmogHoliday RecID 268695 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296176 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296176 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296177 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296177 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296178 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296178 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296179 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296179 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296180 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296180 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296181 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296181 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296182 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296182 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 296183 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 296183 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 307647 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 307647 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 307648 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 307648 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 307649 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 307649 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104917 Table ItemModifiedAppearance RecID 307650 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104917 Table ItemModifiedAppearanceExtra RecID 307650 VALIDATION_RESULT_DELETE
3/5 11:45:50.072  	104927 Table TransmogHoliday RecID 250794 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104927 Table TransmogHoliday RecID 250795 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104927 Table TransmogHoliday RecID 250796 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104941 Table TransmogHoliday RecID 271703 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104941 Table TransmogHoliday RecID 271704 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104941 Table TransmogHoliday RecID 271710 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104941 Table TransmogHoliday RecID 271712 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104941 Table TransmogHoliday RecID 271714 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245377 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245377 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245378 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245378 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245379 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245379 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245380 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245380 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245381 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245381 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245382 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245382 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245383 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245383 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245384 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245384 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245385 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245385 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245386 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245386 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245387 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245387 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245388 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245388 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245389 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245389 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245390 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245390 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245391 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245391 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245392 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245392 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245393 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245393 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245394 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245394 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245395 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245395 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245396 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245396 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245397 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245397 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245398 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245398 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245399 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245399 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245400 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245400 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245401 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245401 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245402 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245402 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245403 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245403 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245404 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245404 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245405 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245405 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245406 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245406 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245407 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245407 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245408 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245408 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245409 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245409 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245410 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245410 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245411 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245411 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245412 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245412 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245413 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245413 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245414 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245414 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245415 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245415 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245416 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245416 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245417 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245417 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245418 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245418 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245419 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245419 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245420 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245420 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245421 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245421 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245422 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245422 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245423 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245423 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245424 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245424 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245425 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245425 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245426 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245426 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245427 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245427 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245428 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245428 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245429 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245429 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245430 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245430 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendorSparse RecID 245431 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104948 Table CollectableSourceVendor RecID 245431 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104972 Table TransmogHoliday RecID 248485 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196586 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196587 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196588 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196589 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196590 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196591 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196592 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196593 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196594 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196595 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196596 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196597 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196598 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196599 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196600 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196601 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196602 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196603 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196604 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 196605 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202621 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202622 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202623 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202624 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202625 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202626 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202627 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202628 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202629 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202630 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202631 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202632 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202633 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202634 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202635 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202636 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202637 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202638 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202639 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 202640 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 206046 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207462 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207463 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207464 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207465 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207466 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207467 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207468 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207469 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207470 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207471 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207472 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207473 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207474 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207475 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207476 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207477 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207478 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207479 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207480 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 207481 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 210947 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217316 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217317 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217318 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217319 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217320 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217321 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217322 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217323 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217324 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217325 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217326 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217327 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217328 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217329 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217330 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217331 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217332 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217333 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217334 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217335 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104990 Table TransmogHoliday RecID 217408 VALIDATION_RESULT_INVALID
3/5 11:45:50.072  	104994 Table ItemModifiedAppearance RecID 298172 VALIDATION_RESULT_VALID
3/5 11:45:50.072  	104994 Table ItemModifiedAppearanceExtra RecID 298172 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105022 Table TransmogHoliday RecID 268480 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105026 Table TransmogHoliday RecID 245777 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105026 Table TransmogHoliday RecID 259205 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105026 Table ItemAppearance RecID 127462 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105026 Table ItemAppearance RecID 130110 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105026 Table ItemAppearance RecID 130111 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105026 Table ItemModifiedAppearance RecID 292897 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105026 Table ItemModifiedAppearanceExtra RecID 292897 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105026 Table ItemModifiedAppearance RecID 292898 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105026 Table ItemModifiedAppearanceExtra RecID 292898 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105053 Table CollectableSourceVendorSparse RecID 239630 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105053 Table CollectableSourceVendor RecID 239630 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105053 Table CollectableSourceVendorSparse RecID 239631 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105053 Table CollectableSourceVendor RecID 239631 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105053 Table CollectableSourceVendorSparse RecID 239745 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105053 Table CollectableSourceVendor RecID 239745 VALIDATION_RESULT_DELETE
3/5 11:45:50.088  	105053 Table CollectableSourceVendorSparse RecID 245432 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105053 Table CollectableSourceVendor RecID 245432 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105053 Table CollectableSourceVendorSparse RecID 245433 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105053 Table CollectableSourceVendor RecID 245433 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105053 Table CollectableSourceVendorSparse RecID 245434 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105053 Table CollectableSourceVendor RecID 245434 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105060 Table TransmogHoliday RecID 226147 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105060 Table TransmogHoliday RecID 226257 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105060 Table TransmogHoliday RecID 244335 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105075 Table TransmogHoliday RecID 246604 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105109 Table TransmogHoliday RecID 251174 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105109 Table TransmogHoliday RecID 251217 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105130 Table TransmogHoliday RecID 263975 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105179 Table TransmogHoliday RecID 230285 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105179 Table TransmogHoliday RecID 230286 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105179 Table TransmogHoliday RecID 230287 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105215 Table TransmogHoliday RecID 262351 VALIDATION_RESULT_INVALID
3/5 11:45:50.088  	105293 Table CollectableSourceInfo RecID 173243 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105293 Table CollectableSourceInfo RecID 173244 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105293 Table CollectableSourceInfo RecID 173245 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105293 Table CollectableSourceInfo RecID 173246 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180515 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180516 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180517 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180518 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180519 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180520 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180521 VALIDATION_RESULT_VALID
3/5 11:45:50.088  	105322 Table CollectableSourceInfo RecID 180522 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180523 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180524 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180525 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180526 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180527 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180528 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180529 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceInfo RecID 180530 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245439 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245439 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245440 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245440 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245441 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245441 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245442 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245442 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245443 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245443 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245444 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245444 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245445 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245445 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245446 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245446 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245447 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245447 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245448 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245448 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245449 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245449 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245450 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245450 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245451 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245451 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245452 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245452 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245453 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245453 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245454 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245454 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245455 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245455 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245456 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245456 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245457 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245457 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245458 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245458 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245459 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245459 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245460 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245460 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245461 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245461 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245462 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245462 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245463 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245463 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245464 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245464 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245465 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245465 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245466 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245466 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245467 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245467 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245468 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245468 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245469 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245469 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245470 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245470 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245471 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245471 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245472 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245472 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245473 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245473 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245474 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245474 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245475 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245475 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245476 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245476 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245477 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245477 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245478 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245478 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245479 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245479 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245480 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245480 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245481 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245481 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245482 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245482 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245483 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245483 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245484 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245484 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245485 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245485 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendorSparse RecID 245486 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table CollectableSourceVendor RecID 245486 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259055 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259056 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259057 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259058 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259059 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259060 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259061 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259062 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259063 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259064 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259065 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259066 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259067 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259068 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259069 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105322 Table TransmogHoliday RecID 259070 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180531 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180532 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180534 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180535 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180536 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180537 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180538 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180539 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180540 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180541 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180542 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180543 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180544 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180545 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180546 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180547 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceInfo RecID 180548 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245487 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245487 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245488 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245488 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245489 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245489 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245490 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245490 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245491 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245491 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245492 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245492 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245493 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245493 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245494 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245494 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245495 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245495 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245496 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245496 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245497 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245497 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245498 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245498 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245499 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245499 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245500 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245500 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245501 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245501 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245502 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245502 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245503 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245503 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245504 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245504 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245505 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245505 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245506 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245506 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245507 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245507 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245508 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245508 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245509 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245509 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245510 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245510 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245511 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245511 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245512 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245512 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245513 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245513 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245514 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245514 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245515 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245515 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245516 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245516 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245517 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245517 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245518 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245518 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245519 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245519 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245520 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245520 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245521 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245521 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245522 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245522 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245523 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245523 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245524 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245524 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245525 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245525 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245526 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245526 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245527 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245527 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245528 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245528 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245529 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245529 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245530 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245530 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245531 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245531 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245532 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245532 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245533 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245533 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245534 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245534 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245535 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245535 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245536 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245536 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245537 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245537 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245538 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245538 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245539 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245539 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245540 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245540 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245541 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245541 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245542 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245542 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245543 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245543 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245544 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245544 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245545 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245545 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245546 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245546 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245547 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245547 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245548 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245548 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245549 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245549 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245550 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245550 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245551 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245551 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245552 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245552 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245553 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245553 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245554 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245554 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245555 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245555 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245556 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245556 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245557 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245557 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245558 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245558 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245559 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245559 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245560 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245560 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245561 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245561 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245562 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245562 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245563 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245563 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245564 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245564 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245565 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245565 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245566 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245566 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245567 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245567 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245568 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245568 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245569 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245569 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245570 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245570 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245571 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245571 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245572 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245572 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245573 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245573 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245574 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245574 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245575 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245575 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245576 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245576 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245577 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245577 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245578 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245578 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245579 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245579 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245580 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245580 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245581 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245581 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245582 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245582 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245583 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245583 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245584 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245584 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245585 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245585 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245586 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245586 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245587 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245587 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245588 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245588 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245589 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245589 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245590 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245590 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245591 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245591 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245592 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245592 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245593 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245593 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245594 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245594 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245595 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245595 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245596 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245596 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245597 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245597 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245598 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245598 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245599 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245599 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245600 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245600 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245601 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245601 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245602 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245602 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245603 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245603 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245604 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245604 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245605 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245605 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245606 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245606 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245607 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245607 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245608 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245608 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245609 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245609 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245610 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245610 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245611 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245611 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245612 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245612 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245613 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245613 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245614 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245614 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245615 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245615 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245616 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245616 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245617 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245617 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245618 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245618 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245619 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245619 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245620 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245620 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245621 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245621 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245622 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245622 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245623 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245623 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245624 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245624 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245625 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245625 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245626 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245626 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245627 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245627 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245628 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245628 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245629 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245629 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendorSparse RecID 245630 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105338 Table CollectableSourceVendor RecID 245630 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105350 Table TransmogHoliday RecID 231756 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105350 Table TransmogHoliday RecID 231757 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105350 Table TransmogHoliday RecID 231767 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105350 Table TransmogHoliday RecID 231768 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105350 Table TransmogHoliday RecID 231769 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105370 Table TransmogHoliday RecID 245345 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105370 Table TransmogHoliday RecID 259172 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105370 Table TransmogHoliday RecID 259174 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105370 Table TransmogHoliday RecID 259176 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105370 Table TransmogHoliday RecID 259178 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105370 Table TransmogHoliday RecID 259180 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105370 Table TransmogHoliday RecID 259184 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105376 Table TransmogHoliday RecID 257180 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105376 Table TransmogHoliday RecID 257199 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105376 Table TransmogHoliday RecID 257240 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105376 Table TransmogHoliday RecID 257445 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105376 Table TransmogHoliday RecID 260696 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105376 Table TransmogHoliday RecID 260697 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105376 Table TransmogHoliday RecID 263579 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105397 Table TransmogHoliday RecID 238020 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounterSparse RecID 51185 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounter RecID 51185 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounterSparse RecID 53931 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounter RecID 53931 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounterSparse RecID 53932 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounter RecID 53932 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounterSparse RecID 53933 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounter RecID 53933 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounterSparse RecID 53934 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounter RecID 53934 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounterSparse RecID 53935 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceEncounter RecID 53935 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105413 Table CollectableSourceInfo RecID 180533 VALIDATION_RESULT_VALID
3/5 11:45:50.104  	105442 Table TransmogHoliday RecID 238377 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105442 Table TransmogHoliday RecID 238382 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105445 Table TransmogHoliday RecID 259230 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105445 Table TransmogHoliday RecID 259232 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105456 Table TransmogHoliday RecID 244588 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105456 Table TransmogHoliday RecID 244589 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105456 Table TransmogHoliday RecID 244590 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105460 Table TransmogHoliday RecID 246594 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105557 Table TransmogHoliday RecID 271631 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105557 Table TransmogHoliday RecID 271709 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105557 Table TransmogHoliday RecID 271711 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105557 Table TransmogHoliday RecID 271713 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105557 Table TransmogHoliday RecID 271715 VALIDATION_RESULT_INVALID
3/5 11:45:50.104  	105602 Table TransmogHoliday RecID 265804 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264519 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264520 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264521 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264522 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264523 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264524 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264525 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264526 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264527 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264528 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264529 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264530 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264531 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264532 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264533 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264534 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264535 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264536 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264537 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264538 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264539 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264540 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264541 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264542 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264543 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264544 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264545 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264546 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264547 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264548 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264549 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264550 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264551 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264552 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264553 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264554 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264555 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264556 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264557 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264558 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264559 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264560 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264561 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264562 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264563 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264564 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264565 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264566 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264567 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264568 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264569 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264570 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264571 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264572 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264573 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264574 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264575 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264576 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264577 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264578 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264579 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264580 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264581 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264582 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264583 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264584 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264585 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264586 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264588 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264589 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264591 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264592 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264593 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264594 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264595 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264596 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264597 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264598 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264599 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264600 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264601 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264602 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264603 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264604 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264605 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264606 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264607 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264608 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264609 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264610 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264611 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264612 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264613 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264614 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264615 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264616 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264617 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264618 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264619 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264620 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264621 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264622 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264623 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264624 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264625 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264626 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264627 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264628 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264629 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264630 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264631 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264632 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264633 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264634 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264635 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264637 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264638 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264639 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264640 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264641 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264642 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264643 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264644 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264645 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264646 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264647 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264648 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264649 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264650 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264651 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264910 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264911 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264912 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table TransmogHoliday RecID 264913 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105610 Table ItemModifiedAppearance RecID 303470 VALIDATION_RESULT_VALID
3/5 11:45:50.119  	105610 Table ItemModifiedAppearanceExtra RecID 303470 VALIDATION_RESULT_DELETE
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237828 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237829 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237830 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237831 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237832 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237833 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237834 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237835 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237836 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237837 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237838 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237839 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237840 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237841 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237842 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237843 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237844 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237845 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237846 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237847 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237848 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237849 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237850 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237901 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237902 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237903 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237904 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237905 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237906 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237907 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237908 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237909 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237910 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237911 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237912 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237913 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237914 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237915 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237916 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237917 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237918 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237919 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237920 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237921 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237922 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237923 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237924 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237925 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237926 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237927 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237928 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237929 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237930 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237931 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 237932 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239648 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239649 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239650 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239651 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239652 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239653 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239654 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239655 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239656 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239657 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239658 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239659 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239660 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239661 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239662 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239663 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239664 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239668 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239669 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239670 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239671 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239672 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239673 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239674 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239675 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239676 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239677 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239678 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239679 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239680 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239681 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239682 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239683 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239684 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 239685 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 240948 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 240950 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 240952 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 241139 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 241140 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 241340 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244178 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244179 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244463 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244472 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244553 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244554 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244555 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244556 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244557 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244558 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244559 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244560 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244561 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244562 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244563 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244564 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244565 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244566 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244567 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244568 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244569 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244570 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244571 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244572 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244573 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244574 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244575 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244576 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244577 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244578 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244579 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244580 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244581 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244582 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244583 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244584 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244585 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244586 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244587 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244593 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244596 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244600 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244601 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244602 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244605 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244606 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244609 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244610 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244611 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244612 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244613 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244614 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244679 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244735 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244736 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244737 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244738 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244739 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244740 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244741 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244742 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244743 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244744 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244745 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244746 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244747 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244748 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244749 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244750 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244751 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244752 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244753 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244754 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244755 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244756 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244757 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244758 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244759 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244760 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244761 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244762 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244764 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244765 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244766 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244767 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244768 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244769 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244770 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244771 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244772 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244773 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 244774 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245337 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245338 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245339 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245340 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245341 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245342 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245344 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245752 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245753 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245768 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245769 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245770 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245771 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245772 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245773 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245868 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245869 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 245870 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248018 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248019 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248020 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248021 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248022 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248023 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248024 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248025 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248026 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248027 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248028 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248029 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248030 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248031 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248032 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248033 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248034 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248035 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248036 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248037 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248038 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248039 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248040 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248041 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248042 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248043 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248044 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248045 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248046 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248047 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248048 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248049 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248050 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248051 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248052 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248053 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248054 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248055 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248056 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248057 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248058 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248059 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248061 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248062 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248063 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248064 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248065 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248066 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248067 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248068 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248069 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248070 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248071 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248072 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248074 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248075 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248076 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248077 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248078 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248080 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 248084 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249275 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249276 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249277 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249278 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249279 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249280 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249281 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249283 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249284 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249286 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249287 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249288 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249293 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249294 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249295 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249296 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249298 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249302 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249303 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249304 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249305 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249306 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249307 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249308 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249309 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249310 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249311 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249312 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249313 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249314 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249315 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249316 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249317 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249318 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249319 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249320 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249321 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249322 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249323 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249324 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249325 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249326 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249327 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249328 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249329 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249330 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249331 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249332 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249333 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249334 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249335 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249336 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249337 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249339 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249340 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249341 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249342 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249343 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249344 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249345 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249346 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249368 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249369 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249370 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249371 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249373 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249374 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249376 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249377 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249380 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249381 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249382 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249610 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249619 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249620 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249621 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249622 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249623 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249624 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249625 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249626 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249627 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249628 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249629 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249630 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249631 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249632 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249633 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249634 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249635 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249636 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249637 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249638 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249639 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249640 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249641 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249642 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249643 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249644 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249645 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249646 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249647 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249648 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249649 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249650 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249651 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249652 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249653 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249654 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249655 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249656 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249657 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249658 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249659 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249660 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249661 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249662 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249664 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249665 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249667 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249669 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249670 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249671 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249672 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249676 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249677 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249805 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249806 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249807 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249808 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249809 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249810 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249811 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249912 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249913 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249914 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249915 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249919 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249920 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249921 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249922 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249925 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249947 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249948 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249949 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249950 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249951 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249952 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249953 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249954 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249955 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249956 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249957 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249958 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249959 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249960 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249961 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249962 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249963 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249964 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249965 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249966 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249967 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249968 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249969 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249970 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249971 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249972 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249973 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249974 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249975 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249976 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249977 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249978 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249979 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249980 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249981 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249982 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249983 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249984 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249985 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249986 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249987 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249988 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249989 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249990 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249991 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249992 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249993 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249994 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249995 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249996 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249997 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249998 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 249999 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250000 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250001 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250002 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250003 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250004 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250005 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250006 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250007 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250008 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250009 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250010 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250011 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250012 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250013 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250014 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250015 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250016 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250017 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250018 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250019 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250020 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250021 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250022 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250023 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250024 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250025 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250026 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250027 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250028 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250029 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250030 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250031 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250032 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250033 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250034 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250035 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250036 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250037 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250038 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250039 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250040 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250041 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250042 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250043 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250044 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250045 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250046 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250047 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250048 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250049 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250050 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250051 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250052 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250053 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250054 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250055 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250056 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250057 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250058 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250059 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250060 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250061 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250062 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250063 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250247 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250355 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250356 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250361 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250446 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250447 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250448 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250449 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250450 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250451 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250452 VALIDATION_RESULT_INVALID
3/5 11:45:50.119  	105611 Table TransmogHoliday RecID 250453 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250454 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250455 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250456 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250457 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250458 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250459 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250460 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250461 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250462 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250470 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250471 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250472 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250473 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250474 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250475 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250476 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250477 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250478 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250479 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 250480 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251073 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251076 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251116 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251241 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251242 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251250 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251251 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251252 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251253 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251254 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251255 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251256 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251257 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251258 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251259 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251260 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251274 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251275 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251276 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251277 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251513 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251719 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251720 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251721 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251722 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251724 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251725 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251726 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251727 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251728 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251729 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251730 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251731 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251732 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251733 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251734 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251774 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251782 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251783 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251784 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251785 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251786 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251787 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251788 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251789 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251790 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251791 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251792 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251816 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251817 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251818 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251819 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251822 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251823 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251824 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251825 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251826 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251828 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251829 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251830 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251831 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251832 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251882 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251883 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251884 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251885 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 251935 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 252677 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255262 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255263 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255264 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255265 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255266 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255267 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255268 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255269 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255270 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255271 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255272 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255273 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255274 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255275 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255276 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255277 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255278 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255279 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255280 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255281 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255282 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255283 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255284 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255285 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255286 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255287 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255288 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255289 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255290 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255291 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255292 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255293 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255294 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255295 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255296 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255297 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255298 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255299 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255300 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255301 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255302 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255303 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255304 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255305 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255306 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255307 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255308 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255309 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255310 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255311 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255312 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255313 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255314 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255315 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255316 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255317 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255318 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255319 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255320 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255321 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255322 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255323 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255324 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255325 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255326 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255327 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255328 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255329 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255330 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255331 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255332 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255333 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255334 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255335 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255336 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255337 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255338 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255339 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255340 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255341 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255342 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255343 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255344 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255345 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255346 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255347 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255348 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255349 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255350 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255351 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255352 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255353 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255354 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255355 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255356 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255357 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255358 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255359 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255360 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255361 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255362 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255363 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255364 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255365 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255366 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255367 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255368 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255369 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255370 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255371 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255372 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255373 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255374 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255375 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255376 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255377 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255378 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255379 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255380 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255381 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255382 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255383 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255384 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255385 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255386 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255387 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255388 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255389 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255390 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255391 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255392 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255393 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255394 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255395 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255396 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255397 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255398 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255399 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255400 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255401 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255402 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255404 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255405 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255406 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255407 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255408 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255409 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255410 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255411 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255412 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255413 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255414 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255415 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255416 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255417 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255418 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255419 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255420 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255421 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255422 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255423 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255424 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255425 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255426 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255427 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255429 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255430 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255431 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255432 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255433 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255434 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255435 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255436 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255437 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255438 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255439 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255440 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255441 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255442 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255443 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255444 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255445 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255446 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255447 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255448 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255449 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255450 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255451 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255452 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255453 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255454 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255455 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255456 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255457 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255458 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255459 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255460 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255461 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255462 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255463 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255464 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255465 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255466 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255467 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255468 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255469 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255470 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255471 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255472 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255473 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255474 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255475 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255476 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255477 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255478 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255479 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255480 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255481 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255482 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255483 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255484 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255485 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255486 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255487 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255488 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255489 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255490 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255491 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255492 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255493 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255494 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255495 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255496 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255497 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255498 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255499 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255500 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255501 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255502 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255503 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255504 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255505 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255506 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255507 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255508 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255509 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255510 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255511 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255512 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255513 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255514 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255515 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255516 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255517 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255518 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255519 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255520 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255521 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255522 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255523 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255524 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255525 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255526 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255527 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255528 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255529 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255530 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255531 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255532 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255533 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255534 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255535 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255536 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255537 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255538 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255539 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255540 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255541 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255542 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255543 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255544 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255545 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255546 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255547 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255548 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255549 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255550 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255551 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255552 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255553 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255554 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255555 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255556 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255557 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255558 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255559 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255560 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255561 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255562 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255563 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255564 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255565 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255566 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255567 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255568 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255569 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255570 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255571 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255572 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255573 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255574 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255575 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255576 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255578 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255579 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255580 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255581 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255582 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255583 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255584 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255585 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255586 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255587 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255588 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255589 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255590 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255591 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255592 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255593 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255594 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255595 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255596 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255597 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255598 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255599 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255600 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255601 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255602 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255603 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255604 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255605 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255606 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255607 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255608 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255609 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255610 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255611 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255612 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255613 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255614 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255615 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255616 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255617 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255619 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255620 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255621 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255622 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255623 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255624 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255625 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255626 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255627 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255628 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255629 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255630 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255631 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255632 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255633 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255634 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255635 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255636 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255637 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255638 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255639 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255882 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255883 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255884 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255885 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255886 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255887 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255888 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255889 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255890 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255891 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255892 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255893 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255894 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255895 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255896 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255897 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255898 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255899 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255900 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255901 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255902 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255903 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255904 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255905 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255906 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255907 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255908 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255909 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255910 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255911 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255912 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255913 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255914 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255915 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255916 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255917 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255918 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255919 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255920 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255921 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255922 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255923 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255924 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255925 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255926 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255927 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255928 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255929 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255930 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255931 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255932 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255933 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255934 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255935 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255936 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255937 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255938 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 255939 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258908 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258909 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258910 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258911 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258912 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258913 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258914 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258915 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258916 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258917 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258918 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258919 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258920 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258921 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258922 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258923 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258924 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258925 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258926 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258927 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258928 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258929 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258930 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258931 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258932 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258933 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258934 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258935 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258936 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258937 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258938 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258939 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258940 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258941 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258942 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258943 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258944 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258945 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258946 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258947 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258948 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258949 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258950 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258951 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258952 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258953 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258954 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258955 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258956 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258957 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258958 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258959 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258960 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258961 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 258962 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 259462 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 260187 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 260188 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 260189 VALIDATION_RESULT_INVALID
3/5 11:45:50.136  	105611 Table TransmogHoliday RecID 260235 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260370 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260371 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260372 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260373 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260374 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260375 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260376 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260377 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260408 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260414 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 260423 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262375 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262376 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262669 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262670 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262671 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262672 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262673 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262674 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262675 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262677 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262678 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262729 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262730 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262731 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262732 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262733 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262735 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262737 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262738 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 262739 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263282 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263349 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263351 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263352 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263353 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263374 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263375 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263376 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263378 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263416 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263419 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263427 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263429 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263447 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263480 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263481 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263482 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263484 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263485 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263486 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 263487 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264415 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264417 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264418 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264421 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264422 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264423 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264424 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264425 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264427 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264428 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264429 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264431 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264432 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264433 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264694 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 264701 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 265336 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 265337 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 265601 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 266207 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 266208 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 266209 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 266210 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 266314 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 266317 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267076 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267077 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267267 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267268 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267270 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267271 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267371 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267375 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267417 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267469 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 267491 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 268326 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 268327 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 268365 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 268475 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 268477 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105611 Table TransmogHoliday RecID 268921 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105614 Table TransmogHoliday RecID 242643 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105638 Table TransmogHoliday RecID 247234 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105638 Table TransmogHoliday RecID 254319 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121798 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121799 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121800 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121801 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121802 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121803 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121804 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121805 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121806 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121807 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121808 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121809 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121810 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121811 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121812 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121813 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121814 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121815 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121816 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121817 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121818 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121819 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121820 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121821 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121822 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121823 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121824 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121825 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121826 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121827 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121828 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121829 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121830 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121831 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121832 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121833 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121834 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121835 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121836 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121837 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121838 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121839 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121840 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121841 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105654 Table ItemAppearance RecID 121842 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105668 Table TransmogHoliday RecID 238379 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105678 Table ItemAppearance RecID 44559 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105678 Table ItemAppearance RecID 44560 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105678 Table ItemAppearance RecID 44561 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105678 Table ItemAppearance RecID 44562 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105678 Table ItemAppearance RecID 44563 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105678 Table ItemAppearance RecID 44564 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105689 Table CollectableSourceInfo RecID 180622 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105689 Table CollectableSourceVendorSparse RecID 246010 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105689 Table CollectableSourceVendor RecID 246010 VALIDATION_RESULT_VALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 263265 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 263267 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 263268 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 263269 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 264507 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 265739 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 265740 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267479 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267480 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267481 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267482 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267604 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267605 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267606 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267607 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267638 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267639 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267640 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267641 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267642 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105696 Table TransmogHoliday RecID 267643 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105705 Table TransmogHoliday RecID 250082 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 244668 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 245939 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 246414 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 248809 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 252666 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 252667 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 252668 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105736 Table TransmogHoliday RecID 252669 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105740 Table TransmogHoliday RecID 239642 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105746 Table TransmogHoliday RecID 244173 VALIDATION_RESULT_INVALID
3/5 11:45:50.150  	105816 Table TransmogSet RecID 5407 VALIDATION_RESULT_VALID
3/5 11:45:50.166  	105858 Table ItemModifiedAppearance RecID 307643 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105858 Table ItemModifiedAppearanceExtra RecID 307643 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105858 Table ItemModifiedAppearance RecID 307644 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105858 Table ItemModifiedAppearanceExtra RecID 307644 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105858 Table ItemModifiedAppearance RecID 307645 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105858 Table ItemModifiedAppearanceExtra RecID 307645 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105858 Table ItemModifiedAppearance RecID 307646 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105858 Table ItemModifiedAppearanceExtra RecID 307646 VALIDATION_RESULT_DELETE
3/5 11:45:50.166  	105893 Table TransmogHoliday RecID 262798 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 237950 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 237951 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 237952 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 238014 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 238015 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 238016 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 238017 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 238018 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 239635 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 239636 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 239637 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 239638 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 239639 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 239640 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 240957 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 240958 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 240959 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 240960 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244176 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244621 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244622 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244623 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244624 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244625 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244626 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244628 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244630 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244708 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244710 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244712 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244714 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244716 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244718 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 244720 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 245776 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 245778 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105896 Table TransmogHoliday RecID 245780 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105915 Table TransmogHoliday RecID 265816 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105915 Table TransmogHoliday RecID 265828 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105924 Table TransmogHoliday RecID 251162 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105947 Table TransmogHoliday RecID 241299 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105947 Table TransmogHoliday RecID 245907 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105951 Table TransmogHoliday RecID 265030 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105956 Table TransmogHoliday RecID 262616 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105969 Table TransmogHoliday RecID 245343 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105977 Table TransmogHoliday RecID 241142 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105977 Table TransmogHoliday RecID 241143 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105977 Table TransmogHoliday RecID 241144 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105980 Table TransmogHoliday RecID 240947 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105980 Table TransmogHoliday RecID 240949 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243946 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243947 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243948 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243949 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243950 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243951 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243952 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243953 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243960 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243961 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243962 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243963 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243964 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243965 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243966 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243967 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243968 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243969 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243970 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243971 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243972 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243973 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243974 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243975 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243976 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243977 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243978 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243979 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243980 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243981 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243982 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243983 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243988 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243989 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243990 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243991 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243992 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243993 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243994 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243995 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243996 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243997 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243998 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 243999 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244000 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244001 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244002 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244003 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244004 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244005 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244006 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244007 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244008 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244009 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244018 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244019 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244020 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244021 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244022 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244023 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244024 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244025 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244026 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244027 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244028 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244029 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244030 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244031 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244032 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244033 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244034 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244035 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244036 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 244037 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 268032 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 268033 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105985 Table TransmogHoliday RecID 268034 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105998 Table TransmogHoliday RecID 259086 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	105998 Table TransmogHoliday RecID 260979 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106008 Table TransmogHoliday RecID 240951 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106009 Table TransmogHoliday RecID 251149 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106018 Table TransmogHoliday RecID 232791 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106018 Table TransmogHoliday RecID 267573 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 241617 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 241618 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 241620 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 241621 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 241622 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 241623 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 241625 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 243088 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 243090 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 243242 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 243243 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 243495 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 244118 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 244169 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 244538 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 244780 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 244781 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 244782 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 244783 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 245498 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 245535 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 245941 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 245985 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 245992 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 246402 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 246407 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 246408 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 246415 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 246416 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253437 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253439 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253441 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253443 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253451 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253457 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253467 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253469 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253479 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253485 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253488 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253490 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253493 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253495 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253497 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106019 Table TransmogHoliday RecID 253506 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106020 Table TransmogHoliday RecID 230724 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106043 Table TransmogHoliday RecID 245751 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106043 Table TransmogHoliday RecID 246304 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106043 Table TransmogHoliday RecID 246305 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106043 Table TransmogHoliday RecID 246306 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106043 Table TransmogHoliday RecID 246307 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106046 Table TransmogHoliday RecID 244763 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106047 Table TransmogHoliday RecID 246951 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106047 Table TransmogHoliday RecID 248680 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106050 Table TransmogHoliday RecID 257256 VALIDATION_RESULT_INVALID
3/5 11:45:50.166  	106101 Table TransmogHoliday RecID 267277 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 267393 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 264923 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 259368 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 259350 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 259079 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 250864 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 249275 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 244146 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 242522 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 166268 VALIDATION_RESULT_INVALID
3/5 12:20:02.988  	106148 Table TransmogHoliday RecID 166267 VALIDATION_RESULT_INVALID
3/5 12:27:03.240  	105911 Table TransmogHoliday RecID 268479 VALIDATION_RESULT_INVALID
3/5 12:30:03.252  	106124 Table TransmogHoliday RecID 242304 VALIDATION_RESULT_INVALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendorSparse RecID 237358 VALIDATION_RESULT_VALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendor RecID 237358 VALIDATION_RESULT_VALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendorSparse RecID 237359 VALIDATION_RESULT_VALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendor RecID 237359 VALIDATION_RESULT_VALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendorSparse RecID 237360 VALIDATION_RESULT_VALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendor RecID 237360 VALIDATION_RESULT_VALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendorSparse RecID 237361 VALIDATION_RESULT_VALID
3/5 12:31:03.263  	106125 Table CollectableSourceVendor RecID 237361 VALIDATION_RESULT_VALID

---

## 5. AccountData.log — Transmog CVars
```
SET transmogrifySourceFilters ""
SET transmogrifySetsFilters ""
SET transmogHideIgnoredSlots "1"
SET wardrobeSetsFilters "B"
SET lastTransmogCustomSetIDNoSpec "0"
SET transmogrifySourceFilters ""
SET transmogrifySetsFilters ""
SET transmogHideIgnoredSlots "1"
SET wardrobeSetsFilters "B"
SET lastTransmogCustomSetIDNoSpec "0"
SET transmogrifySourceFilters ""
SET transmogrifySetsFilters ""
SET transmogHideIgnoredSlots "1"
SET wardrobeSetsFilters "B"
SET lastTransmogCustomSetIDNoSpec "0"
SET lastTransmogCustomSetIDNoSpec "0"
SET lastTransmogCustomSetIDNoSpec "0"
SET transmogrifySourceFilters ""
SET transmogrifySetsFilters ""
SET transmogHideIgnoredSlots "1"
SET wardrobeSetsFilters "B"
SET lastTransmogCustomSetIDNoSpec "0"
SET transmogrifySourceFilters ""
SET transmogrifySetsFilters ""
SET transmogHideIgnoredSlots "1"
SET wardrobeSetsFilters "B"
SET lastTransmogCustomSetIDNoSpec "0"
SET transmogrifySourceFilters ""
SET transmogrifySetsFilters ""
SET transmogHideIgnoredSlots "1"
SET wardrobeSetsFilters "B"
SET lastTransmogCustomSetIDNoSpec "0"
SET lastTransmogCustomSetIDNoSpec "0"
SET lastTransmogCustomSetIDNoSpec "0"
SET transmogrifySourceFilters ""
SET transmogrifySetsFilters ""
SET transmogHideIgnoredSlots "1"
SET wardrobeSetsFilters "B"
SET lastTransmogCustomSetIDNoSpec "0"
SET wardrobeSetsFilters ""
SET wardrobeShowCollected "0"
SET wardrobeSetsFilters ""
SET wardrobeShowCollected "0"
SET wardrobeSetsFilters ""
SET wardrobeShowCollected "0"
```

---

## 6. TransmogBridge SavedVariables
No TransmogBridge.lua files found in either account.

---

## Notes
- **GROSTOLIS** = retail Battle.net account (connected to live Blizzard servers)
- **1#1** = private server account (connected to RoleplayCore)
- TransmogSpy `goto continue` syntax at line 1184 causes `/tspy items` command to fail (FrameXML error)
- All other TransmogSpy hooks and event logging work correctly
- Hotfix.log shows 76,650 total hotfix entries from retail; transmog subset extracted above


---

## 6. BetterWardrobe SavedVariables

### Account: GROSTOLIS

BetterWardrobe_Options = {
["profileKeys"] = {
["Pusclown - Dentarg"] = "Default",
["Regorek - Dentarg"] = "Default",
["Novera - Dentarg"] = "Default",
["Cylde - Dentarg"] = "Default",
["Fryday - Dentarg"] = "Default",
["Draxtwo - Dentarg"] = "Default",
},
["profiles"] = {
["Default"] = {
},
},
}
BetterWardrobe_CharacterData = {
["profileKeys"] = {
["Pusclown - Dentarg"] = "Pusclown - Dentarg",
["Regorek - Dentarg"] = "Regorek - Dentarg",
["Novera - Dentarg"] = "Novera - Dentarg",
["Cylde - Dentarg"] = "Cylde - Dentarg",
["Fryday - Dentarg"] = "Fryday - Dentarg",
["Draxtwo - Dentarg"] = "Draxtwo - Dentarg",
},
}
BetterWardrobe_SavedSetData = {
["global"] = {
["sets"] = {
["Pusclown - Dentarg"] = {
},
["Regorek - Dentarg"] = {
},
["Novera - Dentarg"] = {
},
["Cylde - Dentarg"] = {
},
["Fryday - Dentarg"] = {
},
["Draxtwo - Dentarg"] = {
},
},
},
["profileKeys"] = {
["Pusclown - Dentarg"] = "Pusclown - Dentarg",
["Regorek - Dentarg"] = "Regorek - Dentarg",
["Novera - Dentarg"] = "Novera - Dentarg",
["Cylde - Dentarg"] = "Cylde - Dentarg",
["Fryday - Dentarg"] = "Fryday - Dentarg",
["Draxtwo - Dentarg"] = "Draxtwo - Dentarg",
},
["profiles"] = {
["Novera - Dentarg"] = {
},
["Pusclown - Dentarg"] = {
},
["Cylde - Dentarg"] = {
},
["Draxtwo - Dentarg"] = {
},
},
}
BetterWardrobe_SubstituteItemData = {
["profileKeys"] = {
["Pusclown - Dentarg"] = "Default",
["Regorek - Dentarg"] = "Default",
["Novera - Dentarg"] = "Default",
["Cylde - Dentarg"] = "Default",
["Fryday - Dentarg"] = "Default",
["Draxtwo - Dentarg"] = "Default",
},
["profiles"] = {
["Default"] = {
},
},
}
BetterWardrobe_ListData = {
["favoritesDB"] = {
["profileKeys"] = {
["Pusclown - Dentarg"] = "Pusclown - Dentarg",
["Regorek - Dentarg"] = "Regorek - Dentarg",
["Novera - Dentarg"] = "Novera - Dentarg",
["Cylde - Dentarg"] = "Cylde - Dentarg",
["Fryday - Dentarg"] = "Fryday - Dentarg",
["Draxtwo - Dentarg"] = "Draxtwo - Dentarg",
},
["profiles"] = {
["Pusclown - Dentarg"] = {
},
["Regorek - Dentarg"] = {
},
["Novera - Dentarg"] = {
},
["Cylde - Dentarg"] = {
},
["Draxtwo - Dentarg"] = {
},
["Fryday - Dentarg"] = {
},
},
},
["collectionListDB"] = {
["profileKeys"] = {
["Pusclown - Dentarg"] = "Pusclown - Dentarg",
["Regorek - Dentarg"] = "Regorek - Dentarg",
["Novera - Dentarg"] = "Novera - Dentarg",
["Cylde - Dentarg"] = "Cylde - Dentarg",
["Fryday - Dentarg"] = "Fryday - Dentarg",
["Draxtwo - Dentarg"] = "Draxtwo - Dentarg",
},
["profiles"] = {
["Pusclown - Dentarg"] = {
},
["Regorek - Dentarg"] = {
},
["Novera - Dentarg"] = {
},
["Cylde - Dentarg"] = {
},
["Fryday - Dentarg"] = {
},
["Draxtwo - Dentarg"] = {
},
},
},
["lastUpdte"] = 1,
["OutfitDB"] = {
["profileKeys"] = {
["Pusclown - Dentarg"] = "Pusclown - Dentarg",
["Regorek - Dentarg"] = "Regorek - Dentarg",
["Novera - Dentarg"] = "Novera - Dentarg",
["Cylde - Dentarg"] = "Cylde - Dentarg",
["Fryday - Dentarg"] = "Fryday - Dentarg",
["Draxtwo - Dentarg"] = "Draxtwo - Dentarg",
},
},
["HiddenAppearanceDB"] = {
["profileKeys"] = {
["Pusclown - Dentarg"] = "Pusclown - Dentarg",
["Regorek - Dentarg"] = "Regorek - Dentarg",
["Novera - Dentarg"] = "Novera - Dentarg",
["Cylde - Dentarg"] = "Cylde - Dentarg",
["Fryday - Dentarg"] = "Fryday - Dentarg",
["Draxtwo - Dentarg"] = "Draxtwo - Dentarg",
},
["profiles"] = {
["Pusclown - Dentarg"] = {
},
["Regorek - Dentarg"] = {
},
["Novera - Dentarg"] = {
},
["Cylde - Dentarg"] = {
},
["Draxtwo - Dentarg"] = {
},
["Fryday - Dentarg"] = {
},
},
},
}
BetterWardrobe_Mogitdata = nil
BetterWardrobe_Updates = {
["8_4"] = true,
}
BTT = nil

### Account: 1#1

BetterWardrobe_Options = {
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Default",
["Stableslot - Draconic-WoW"] = "Default",
["Dagda - Draconic-WoW"] = "Default",
["Graham - Draconic-WoW"] = "Default",
["Levara - Draconic-WoW"] = "Default",
["Reese - Draconic-WoW"] = "Default",
["Nando - Draconic-WoW"] = "Default",
["Azert - Draconic-WoW"] = "Default",
["Rameth - Draconic-WoW"] = "Default",
["Gunnar - Draconic-WoW"] = "Default",
["Krista - Draconic-WoW"] = "Default",
["Tav - Draconic-WoW"] = "Default",
["Kashel - Draconic-WoW"] = "Default",
["Stonebreaker - Draconic-WoW"] = "Default",
["Consecrazy - Draconic-WoW"] = "Default",
["Carlo - Draconic-WoW"] = "Default",
["Parthos - Draconic-WoW"] = "Default",
["Melrose - Draconic-WoW"] = "Default",
["Azra - Draconic-WoW"] = "Default",
["Benny - Draconic-WoW"] = "Default",
["Primarch - Draconic-WoW"] = "Default",
["Meltface - Draconic-WoW"] = "Default",
["Shavonda - Draconic-WoW"] = "Default",
["Felonme - Draconic-WoW"] = "Default",
["Red - Draconic-WoW"] = "Default",
["Shapow - Draconic-WoW"] = "Default",
["Vela - Draconic-WoW"] = "Default",
["Starweaver - Draconic-WoW"] = "Default",
["Hammerme - Draconic-WoW"] = "Default",
["Testtest - Draconic-WoW"] = "Default",
["Mercer - Draconic-WoW"] = "Default",
["Golo - Draconic-WoW"] = "Default",
["Sorn - Draconic-WoW"] = "Default",
["Khazel - Draconic-WoW"] = "Default",
["Kefka - Draconic-WoW"] = "Default",
["Sicalicious - Draconic-WoW"] = "Default",
["Penance - Draconic-WoW"] = "Default",
["Deez - Draconic-WoW"] = "Default",
["Holden - Draconic-WoW"] = "Default",
["Utherd - Draconic-WoW"] = "Default",
["Umbralight - Draconic-WoW"] = "Default",
["Earthevo - Draconic-WoW"] = "Default",
["Talairn - Draconic-WoW"] = "Default",
["Hexcuseme - Draconic-WoW"] = "Default",
["Vulkan - Draconic-WoW"] = "Default",
["Quiverme - Draconic-WoW"] = "Default",
["Nikaj - Draconic-WoW"] = "Default",
["Reynolds - Draconic-WoW"] = "Default",
["Van - Draconic-WoW"] = "Default",
["Thornhand - Draconic-WoW"] = "Default",
["Blocksmith - Draconic-WoW"] = "Default",
["Sanstus - Draconic-WoW"] = "Default",
["Jobe - Draconic-WoW"] = "Default",
["Artanis - Draconic-WoW"] = "Default",
["Koby - Draconic-WoW"] = "Default",
["Zhago - Draconic-WoW"] = "Default",
["Orias - Draconic-WoW"] = "Default",
["Hatcher - Draconic-WoW"] = "Default",
["Zarah - Draconic-WoW"] = "Default",
["Adnap - Draconic-WoW"] = "Default",
["Sampson - Draconic-WoW"] = "Default",
["Leyline - Draconic-WoW"] = "Default",
["Hemogoblin - Draconic-WoW"] = "Default",
["Marvo - Draconic-WoW"] = "Default",
["Gantz - Draconic-WoW"] = "Default",
["Draxtwo - Draconic-WoW"] = "Default",
["Oomah - Draconic-WoW"] = "Default",
["Foehawk - Draconic-WoW"] = "Default",
["Dix - Draconic-WoW"] = "Default",
["Havik - Draconic-WoW"] = "Default",
["Yancy - Draconic-WoW"] = "Default",
["Thirstseal - Draconic-WoW"] = "Default",
["Nolan - Draconic-WoW"] = "Default",
["Momonga - Draconic-WoW"] = "Default",
["Kardol - Draconic-WoW"] = "Default",
["Ikanoa - Draconic-WoW"] = "Default",
["Derek - Draconic-WoW"] = "Default",
["Ava - Draconic-WoW"] = "Default",
["Cedrick - Draconic-WoW"] = "Default",
["Dreya - Draconic-WoW"] = "Default",
["Vaedan - Draconic-WoW"] = "Default",
["Korik - Draconic-WoW"] = "Default",
["Parah - Draconic-WoW"] = "Default",
["Alaana - Draconic-WoW"] = "Default",
["Celestra - Draconic-WoW"] = "Default",
["Thiccplates - Draconic-WoW"] = "Default",
["Valanese - Draconic-WoW"] = "Default",
["Hitcap - Draconic-WoW"] = "Default",
["Kalano - Draconic-WoW"] = "Default",
["Roland - Draconic-WoW"] = "Default",
["Lars - Draconic-WoW"] = "Default",
["Sebas - Draconic-WoW"] = "Default",
["Voxghar - Draconic-WoW"] = "Default",
["Payton - Draconic-WoW"] = "Default",
["Zezima - Draconic-WoW"] = "Default",
["Laaj - Draconic-WoW"] = "Default",
["Punchline - Draconic-WoW"] = "Default",
["Lia - Draconic-WoW"] = "Default",
["Warren - Draconic-WoW"] = "Default",
["Davos - Draconic-WoW"] = "Default",
["Tredwell - Draconic-WoW"] = "Default",
["Shamwow - Draconic-WoW"] = "Default",
["Mogh - Draconic-WoW"] = "Default",
["Padrik - Draconic-WoW"] = "Default",
["Leonard - Draconic-WoW"] = "Default",
["Danvers - Draconic-WoW"] = "Default",
["Adepta - Draconic-WoW"] = "Default",
["Kaitlan - Draconic-WoW"] = "Default",
["Tywin - Draconic-WoW"] = "Default",
["Elden - Draconic-WoW"] = "Default",
["Ren - Draconic-WoW"] = "Default",
["Sebastian - Draconic-WoW"] = "Default",
["Boris - Draconic-WoW"] = "Default",
["Prak - Draconic-WoW"] = "Default",
["Whirlwinded - Draconic-WoW"] = "Default",
["Coggle - Draconic-WoW"] = "Default",
["Moremojo - Draconic-WoW"] = "Default",
["Mega - Draconic-WoW"] = "Default",
["Danath - Draconic-WoW"] = "Default",
["Brax - Draconic-WoW"] = "Default",
["Theodore - Draconic-WoW"] = "Default",
["Kodetha - Draconic-WoW"] = "Default",
["Sica - Draconic-WoW"] = "Default",
["Aimme - Draconic-WoW"] = "Default",
["Tavish - Draconic-WoW"] = "Default",
["Robb - Draconic-WoW"] = "Default",
["Anega - Draconic-WoW"] = "Default",
["Ballistics - Draconic-WoW"] = "Default",
["Griffith - Draconic-WoW"] = "Default",
["Frag - Draconic-WoW"] = "Default",
["Eversong - Draconic-WoW"] = "Default",
["Banks - Draconic-WoW"] = "Default",
["Justicaris - Draconic-WoW"] = "Default",
["Xenos - Draconic-WoW"] = "Default",
["Celina - Draconic-WoW"] = "Default",
["Baku - Draconic-WoW"] = "Default",
["Regis - Draconic-WoW"] = "Default",
["Kuthbert - Draconic-WoW"] = "Default",
["Austen - Draconic-WoW"] = "Default",
["Harlem - Draconic-WoW"] = "Default",
["Vampstamp - Draconic-WoW"] = "Default",
["Ashford - Draconic-WoW"] = "Default",
["Jackson - Draconic-WoW"] = "Default",
["Kurtak - Draconic-WoW"] = "Default",
["Silva - Draconic-WoW"] = "Default",
["Hoof - Draconic-WoW"] = "Default",
["Erett - Draconic-WoW"] = "Default",
["Zhad - Draconic-WoW"] = "Default",
["Makaio - Draconic-WoW"] = "Default",
["Alice - Draconic-WoW"] = "Default",
["Shanna - Draconic-WoW"] = "Default",
["Shale - Draconic-WoW"] = "Default",
["Xavik - Draconic-WoW"] = "Default",
["Pedaar - Draconic-WoW"] = "Default",
["Phea - Draconic-WoW"] = "Default",
["Channa - Draconic-WoW"] = "Default",
["Bishop - Draconic-WoW"] = "Default",
["Edwards - Draconic-WoW"] = "Default",
["Cecil - Draconic-WoW"] = "Default",
["Cyric - Draconic-WoW"] = "Default",
["Kalzak - Draconic-WoW"] = "Default",
["Grammon - Draconic-WoW"] = "Default",
["Oroth - Draconic-WoW"] = "Default",
["Astaron - Draconic-WoW"] = "Default",
["Invaris - Draconic-WoW"] = "Default",
["Ralzin - Draconic-WoW"] = "Default",
["Zital - Draconic-WoW"] = "Default",
["Grayson - Draconic-WoW"] = "Default",
["Leyla - Draconic-WoW"] = "Default",
["Astraea - Draconic-WoW"] = "Default",
["Elaria - Draconic-WoW"] = "Default",
["Argyle - Draconic-WoW"] = "Default",
["Boltaction - Draconic-WoW"] = "Default",
["Esi - Draconic-WoW"] = "Default",
["Raynaud - Draconic-WoW"] = "Default",
["Tonka - Draconic-WoW"] = "Default",
["Highcliff - Draconic-WoW"] = "Default",
["Marlon - Draconic-WoW"] = "Default",
["Kora - Draconic-WoW"] = "Default",
["Yaaru - Draconic-WoW"] = "Default",
["Qwendy - Draconic-WoW"] = "Default",
["Shadowban - Draconic-WoW"] = "Default",
["Alexius - Draconic-WoW"] = "Default",
["Lolth - Draconic-WoW"] = "Default",
["Nelson - Draconic-WoW"] = "Default",
["Eve - Draconic-WoW"] = "Default",
["Zaibach - Draconic-WoW"] = "Default",
["Magna - Draconic-WoW"] = "Default",
["Satren - Draconic-WoW"] = "Default",
["Xathos - Draconic-WoW"] = "Default",
["Crackhammer - Draconic-WoW"] = "Default",
["Sava - Draconic-WoW"] = "Default",
["Perapera - Draconic-WoW"] = "Default",
["Ruugar - Draconic-WoW"] = "Default",
["Sic - Draconic-WoW"] = "Default",
["Vandrus - Draconic-WoW"] = "Default",
["Smiteme - Draconic-WoW"] = "Default",
["Kazil - Draconic-WoW"] = "Default",
["Meatstick - Draconic-WoW"] = "Default",
["Auria - Draconic-WoW"] = "Default",
["Ironsides - Draconic-WoW"] = "Default",
["Harold - Draconic-WoW"] = "Default",
["Davin - Draconic-WoW"] = "Default",
["Halztraz - Draconic-WoW"] = "Default",
["Tylosh - Draconic-WoW"] = "Default",
["Hexappeal - Draconic-WoW"] = "Default",
["Korla - Draconic-WoW"] = "Default",
["Judgemental - Draconic-WoW"] = "Default",
["Morvane - Draconic-WoW"] = "Default",
["Feltide - Draconic-WoW"] = "Default",
["Hexandchill - Draconic-WoW"] = "Default",
["Rahddon - Draconic-WoW"] = "Default",
["Piuy - Draconic-WoW"] = "Default",
["Kelmenvor - Draconic-WoW"] = "Default",
["Solanna - Draconic-WoW"] = "Default",
["Totemtease - Draconic-WoW"] = "Default",
["Dazlith - Draconic-WoW"] = "Default",
["Dermot - Draconic-WoW"] = "Default",
["Larixa - Draconic-WoW"] = "Default",
["Enoch - Draconic-WoW"] = "Default",
["Arred - Draconic-WoW"] = "Default",
["Zenat - Draconic-WoW"] = "Default",
["Lisbeth - Draconic-WoW"] = "Default",
["Ironward - Draconic-WoW"] = "Default",
["Crakash - Draconic-WoW"] = "Default",
["Oren - Draconic-WoW"] = "Default",
["Mojoe - Draconic-WoW"] = "Default",
["Harandor - Draconic-WoW"] = "Default",
["Rageagainst - Draconic-WoW"] = "Default",
["Movado - Draconic-WoW"] = "Default",
["Ada - Draconic-WoW"] = "Default",
["Tristian - Draconic-WoW"] = "Default",
["Lambert - Draconic-WoW"] = "Default",
["Pakmojo - Draconic-WoW"] = "Default",
["Rend - Draconic-WoW"] = "Default",
["Roone - Draconic-WoW"] = "Default",
["Huk - Draconic-WoW"] = "Default",
["Lunaris - Draconic-WoW"] = "Default",
["Teo - Draconic-WoW"] = "Default",
["Zara - Draconic-WoW"] = "Default",
["Siiri - Draconic-WoW"] = "Default",
["Sophia - Draconic-WoW"] = "Default",
["Iridian - Draconic-WoW"] = "Default",
["Shieldhero - Draconic-WoW"] = "Default",
["Nolen - Draconic-WoW"] = "Default",
["Endra - Draconic-WoW"] = "Default",
["Wangz - Draconic-WoW"] = "Default",
["Nana - Draconic-WoW"] = "Default",
["Volkaris - Draconic-WoW"] = "Default",
["Magnus - Draconic-WoW"] = "Default",
["Theya - Draconic-WoW"] = "Default",
["Atrissa - Draconic-WoW"] = "Default",
["Quincy - Draconic-WoW"] = "Default",
["Mav - Draconic-WoW"] = "Default",
["Anders - Draconic-WoW"] = "Default",
["Daamis - Draconic-WoW"] = "Default",
["Moroes - Draconic-WoW"] = "Default",
["Pakkah - Draconic-WoW"] = "Default",
["Hoz - Draconic-WoW"] = "Default",
["Sarsam - Draconic-WoW"] = "Default",
["Mika - Draconic-WoW"] = "Default",
["Packwarden - Draconic-WoW"] = "Default",
},
["profiles"] = {
["Default"] = {
["IgnoreClassRestrictions"] = true,
["ShowHidden"] = true,
["CurrentFactionSets"] = false,
["ShowItemIDTooltips"] = true,
},
},
}
BetterWardrobe_CharacterData = {
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Erovia - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Dagda - Draconic-WoW"] = "Dagda - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Rameth - Draconic-WoW"] = "Rameth - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Krista - Draconic-WoW"] = "Krista - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Consecrazy - Draconic-WoW"] = "Consecrazy - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Parthos - Draconic-WoW"] = "Parthos - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Azra - Draconic-WoW"] = "Azra - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Felonme - Draconic-WoW"] = "Felonme - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Vela - Draconic-WoW"] = "Vela - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Hammerme - Draconic-WoW"] = "Hammerme - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Sorn - Draconic-WoW"] = "Sorn - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Penance - Draconic-WoW"] = "Penance - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Holden - Draconic-WoW"] = "Holden - Draconic-WoW",
["Utherd - Draconic-WoW"] = "Utherd - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Hexcuseme - Draconic-WoW"] = "Hexcuseme - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Quiverme - Draconic-WoW"] = "Quiverme - Draconic-WoW",
["Nikaj - Draconic-WoW"] = "Nikaj - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Blocksmith - Draconic-WoW"] = "Blocksmith - Draconic-WoW",
["Sanstus - Draconic-WoW"] = "Sanstus - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Artanis - Draconic-WoW"] = "Artanis - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Orias - Draconic-WoW"] = "Orias - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Zarah - Draconic-WoW"] = "Zarah - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Leyline - Draconic-WoW"] = "Leyline - Draconic-WoW",
["Hemogoblin - Draconic-WoW"] = "Hemogoblin - Draconic-WoW",
["Marvo - Draconic-WoW"] = "Marvo - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Foehawk - Draconic-WoW"] = "Foehawk - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Thirstseal - Draconic-WoW"] = "Thirstseal - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Ikanoa - Draconic-WoW"] = "Ikanoa - Draconic-WoW",
["Derek - Draconic-WoW"] = "Derek - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Alaana - Draconic-WoW"] = "Alaana - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Thiccplates - Draconic-WoW"] = "Thiccplates - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Punchline - Draconic-WoW"] = "Punchline - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Shamwow - Draconic-WoW"] = "Shamwow - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Leonard - Draconic-WoW"] = "Leonard - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Tywin - Draconic-WoW"] = "Tywin - Draconic-WoW",
["Elden - Draconic-WoW"] = "Elden - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Sebastian - Draconic-WoW"] = "Sebastian - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Whirlwinded - Draconic-WoW"] = "Whirlwinded - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Danath - Draconic-WoW"] = "Danath - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Aimme - Draconic-WoW"] = "Aimme - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Eversong - Draconic-WoW"] = "Eversong - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Kuthbert - Draconic-WoW"] = "Kuthbert - Draconic-WoW",
["Austen - Draconic-WoW"] = "Austen - Draconic-WoW",
["Harlem - Draconic-WoW"] = "Harlem - Draconic-WoW",
["Vampstamp - Draconic-WoW"] = "Vampstamp - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Jackson - Draconic-WoW"] = "Jackson - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Silva - Draconic-WoW"] = "Silva - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Makaio - Draconic-WoW"] = "Makaio - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Shanna - Draconic-WoW"] = "Shanna - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Xavik - Draconic-WoW"] = "Xavik - Draconic-WoW",
["Pedaar - Draconic-WoW"] = "Pedaar - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Channa - Draconic-WoW"] = "Channa - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Kalzak - Draconic-WoW"] = "Kalzak - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Oroth - Draconic-WoW"] = "Oroth - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Astraea - Draconic-WoW"] = "Astraea - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Boltaction - Draconic-WoW"] = "Boltaction - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Tonka - Draconic-WoW"] = "Tonka - Draconic-WoW",
["Highcliff - Draconic-WoW"] = "Highcliff - Draconic-WoW",
["Marlon - Draconic-WoW"] = "Marlon - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Yaaru - Draconic-WoW"] = "Yaaru - Draconic-WoW",
["Qwendy - Draconic-WoW"] = "Qwendy - Draconic-WoW",
["Shadowban - Draconic-WoW"] = "Shadowban - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Zaibach - Draconic-WoW"] = "Zaibach - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Sava - Draconic-WoW"] = "Sava - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Smiteme - Draconic-WoW"] = "Smiteme - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Ironsides - Draconic-WoW"] = "Ironsides - Draconic-WoW",
["Harold - Draconic-WoW"] = "Harold - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Hexappeal - Draconic-WoW"] = "Hexappeal - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Judgemental - Draconic-WoW"] = "Judgemental - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Feltide - Draconic-WoW"] = "Feltide - Draconic-WoW",
["Hexandchill - Draconic-WoW"] = "Hexandchill - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Totemtease - Draconic-WoW"] = "Totemtease - Draconic-WoW",
["Dazlith - Draconic-WoW"] = "Dazlith - Draconic-WoW",
["Dermot - Draconic-WoW"] = "Dermot - Draconic-WoW",
["Larixa - Draconic-WoW"] = "Larixa - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Arred - Draconic-WoW"] = "Arred - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Ironward - Draconic-WoW"] = "Ironward - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Harandor - Draconic-WoW"] = "Harandor - Draconic-WoW",
["Rageagainst - Draconic-WoW"] = "Rageagainst - Draconic-WoW",
["Movado - Draconic-WoW"] = "Movado - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Lambert - Draconic-WoW"] = "Lambert - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Rend - Draconic-WoW"] = "Rend - Draconic-WoW",
["Roone - Draconic-WoW"] = "Roone - Draconic-WoW",
["Huk - Draconic-WoW"] = "Huk - Draconic-WoW",
["Lunaris - Draconic-WoW"] = "Lunaris - Draconic-WoW",
["Teo - Draconic-WoW"] = "Teo - Draconic-WoW",
["Zara - Draconic-WoW"] = "Zara - Draconic-WoW",
["Siiri - Draconic-WoW"] = "Siiri - Draconic-WoW",
["Sophia - Draconic-WoW"] = "Sophia - Draconic-WoW",
["Iridian - Draconic-WoW"] = "Iridian - Draconic-WoW",
["Shieldhero - Draconic-WoW"] = "Shieldhero - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Nana - Draconic-WoW"] = "Nana - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Pakkah - Draconic-WoW"] = "Pakkah - Draconic-WoW",
["Hoz - Draconic-WoW"] = "Hoz - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Packwarden - Draconic-WoW"] = "Packwarden - Draconic-WoW",
},
}
BetterWardrobe_SavedSetData = {
["global"] = {
["sets"] = {
["Mika - Draconic-WoW"] = {
},
["Hoz - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Quincy - Draconic-WoW"] = {
},
["Sica - Draconic-WoW"] = {
},
["Nando - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Ballistics - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Carlo - Draconic-WoW"] = {
},
["Parthos - Draconic-WoW"] = {
},
["Xenos - Draconic-WoW"] = {
},
["Celina - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Kuthbert - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Meltface - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Silva - Draconic-WoW"] = {
},
["Red - Draconic-WoW"] = {
},
["Vela - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Erett - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Makaio - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Shale - Draconic-WoW"] = {
},
["Pedaar - Draconic-WoW"] = {
},
["Khazel - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Kefka - Draconic-WoW"] = {
},
["Channa - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Cyric - Draconic-WoW"] = {
},
["Utherd - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Artanis - Draconic-WoW"] = {
},
["Enoch - Draconic-WoW"] = {
},
["Zhago - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Zarah - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sampson - Draconic-WoW"] = {
},
["Marvo - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Oomah - Draconic-WoW"] = {
},
["Raynaud - Draconic-WoW"] = {
},
["Dix - Draconic-WoW"] = {
},
["Perapera - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Satren - Draconic-WoW"] = {
},
["Dagda - Draconic-WoW"] = {
},
["Iridian - Draconic-WoW"] = {
},
["Marlon - Draconic-WoW"] = {
},
["Sarsam - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Highcliff - Draconic-WoW"] = {
},
["Danath - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Yaaru - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Theya - Draconic-WoW"] = {
},
["Derek - Draconic-WoW"] = {
},
["Ren - Draconic-WoW"] = {
},
["Cedrick - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Vaedan - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Parah - Draconic-WoW"] = {
},
["Nana - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Sava - Draconic-WoW"] = {
},
["Nikaj - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Koby - Draconic-WoW"] = {
},
["Hitcap - Draconic-WoW"] = {
},
["Argyle - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Auria - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Lars - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Halztraz - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Theodore - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Payton - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Wangz - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Voxghar - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Hoof - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Crakash - Draconic-WoW"] = {
},
["Lambert - Draconic-WoW"] = {
},
["Mojoe - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Thornhand - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Mogh - Draconic-WoW"] = {
},
["Padrik - Draconic-WoW"] = {
},
["Huk - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Zara - Draconic-WoW"] = {
},
["Siiri - Draconic-WoW"] = {
},
["Yancy - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Gunnar - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
{
["outfitID"] = 0,
["sources"] = {
190154,
0,
190152,
0,
190148,
190150,
190156,
190153,
190157,
190155,
0,
0,
0,
0,
0,
116336,
116336,
0,
0,
},
["name"] = "Purple",
["icon"] = 2444253,
["index"] = 1,
},
{
["outfitID"] = 1,
["sources"] = {
190154,
0,
190152,
0,
190148,
190150,
190156,
190153,
190157,
190155,
0,
0,
0,
0,
0,
116336,
116336,
0,
0,
},
["name"] = "White",
["icon"] = 2444253,
["index"] = 2,
},
},
["Kelmenvor - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Volkaris - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Shanna - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Moroes - Draconic-WoW"] = {
},
["Austen - Draconic-WoW"] = {
},
["Orias - Draconic-WoW"] = {
},
["Anders - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Sophia - Draconic-WoW"] = {
},
},
},
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Erovia - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Dagda - Draconic-WoW"] = "Dagda - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Rameth - Draconic-WoW"] = "Rameth - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Krista - Draconic-WoW"] = "Krista - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Consecrazy - Draconic-WoW"] = "Consecrazy - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Parthos - Draconic-WoW"] = "Parthos - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Azra - Draconic-WoW"] = "Azra - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Felonme - Draconic-WoW"] = "Felonme - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Vela - Draconic-WoW"] = "Vela - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Hammerme - Draconic-WoW"] = "Hammerme - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Sorn - Draconic-WoW"] = "Sorn - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Penance - Draconic-WoW"] = "Penance - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Holden - Draconic-WoW"] = "Holden - Draconic-WoW",
["Utherd - Draconic-WoW"] = "Utherd - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Hexcuseme - Draconic-WoW"] = "Hexcuseme - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Quiverme - Draconic-WoW"] = "Quiverme - Draconic-WoW",
["Nikaj - Draconic-WoW"] = "Nikaj - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Blocksmith - Draconic-WoW"] = "Blocksmith - Draconic-WoW",
["Sanstus - Draconic-WoW"] = "Sanstus - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Artanis - Draconic-WoW"] = "Artanis - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Orias - Draconic-WoW"] = "Orias - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Zarah - Draconic-WoW"] = "Zarah - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Leyline - Draconic-WoW"] = "Leyline - Draconic-WoW",
["Hemogoblin - Draconic-WoW"] = "Hemogoblin - Draconic-WoW",
["Marvo - Draconic-WoW"] = "Marvo - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Foehawk - Draconic-WoW"] = "Foehawk - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Thirstseal - Draconic-WoW"] = "Thirstseal - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Ikanoa - Draconic-WoW"] = "Ikanoa - Draconic-WoW",
["Derek - Draconic-WoW"] = "Derek - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Alaana - Draconic-WoW"] = "Alaana - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Thiccplates - Draconic-WoW"] = "Thiccplates - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Punchline - Draconic-WoW"] = "Punchline - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Shamwow - Draconic-WoW"] = "Shamwow - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Leonard - Draconic-WoW"] = "Leonard - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Tywin - Draconic-WoW"] = "Tywin - Draconic-WoW",
["Elden - Draconic-WoW"] = "Elden - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Sebastian - Draconic-WoW"] = "Sebastian - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Whirlwinded - Draconic-WoW"] = "Whirlwinded - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Danath - Draconic-WoW"] = "Danath - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Aimme - Draconic-WoW"] = "Aimme - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Eversong - Draconic-WoW"] = "Eversong - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Kuthbert - Draconic-WoW"] = "Kuthbert - Draconic-WoW",
["Austen - Draconic-WoW"] = "Austen - Draconic-WoW",
["Harlem - Draconic-WoW"] = "Harlem - Draconic-WoW",
["Vampstamp - Draconic-WoW"] = "Vampstamp - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Jackson - Draconic-WoW"] = "Jackson - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Silva - Draconic-WoW"] = "Silva - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Makaio - Draconic-WoW"] = "Makaio - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Shanna - Draconic-WoW"] = "Shanna - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Xavik - Draconic-WoW"] = "Xavik - Draconic-WoW",
["Pedaar - Draconic-WoW"] = "Pedaar - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Channa - Draconic-WoW"] = "Channa - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Kalzak - Draconic-WoW"] = "Kalzak - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Oroth - Draconic-WoW"] = "Oroth - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Astraea - Draconic-WoW"] = "Astraea - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Boltaction - Draconic-WoW"] = "Boltaction - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Tonka - Draconic-WoW"] = "Tonka - Draconic-WoW",
["Highcliff - Draconic-WoW"] = "Highcliff - Draconic-WoW",
["Marlon - Draconic-WoW"] = "Marlon - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Yaaru - Draconic-WoW"] = "Yaaru - Draconic-WoW",
["Qwendy - Draconic-WoW"] = "Qwendy - Draconic-WoW",
["Shadowban - Draconic-WoW"] = "Shadowban - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Zaibach - Draconic-WoW"] = "Zaibach - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Sava - Draconic-WoW"] = "Sava - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Smiteme - Draconic-WoW"] = "Smiteme - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Ironsides - Draconic-WoW"] = "Ironsides - Draconic-WoW",
["Harold - Draconic-WoW"] = "Harold - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Hexappeal - Draconic-WoW"] = "Hexappeal - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Judgemental - Draconic-WoW"] = "Judgemental - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Feltide - Draconic-WoW"] = "Feltide - Draconic-WoW",
["Hexandchill - Draconic-WoW"] = "Hexandchill - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Totemtease - Draconic-WoW"] = "Totemtease - Draconic-WoW",
["Dazlith - Draconic-WoW"] = "Dazlith - Draconic-WoW",
["Dermot - Draconic-WoW"] = "Dermot - Draconic-WoW",
["Larixa - Draconic-WoW"] = "Larixa - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Arred - Draconic-WoW"] = "Arred - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Ironward - Draconic-WoW"] = "Ironward - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Harandor - Draconic-WoW"] = "Harandor - Draconic-WoW",
["Rageagainst - Draconic-WoW"] = "Rageagainst - Draconic-WoW",
["Movado - Draconic-WoW"] = "Movado - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Lambert - Draconic-WoW"] = "Lambert - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Rend - Draconic-WoW"] = "Rend - Draconic-WoW",
["Roone - Draconic-WoW"] = "Roone - Draconic-WoW",
["Huk - Draconic-WoW"] = "Huk - Draconic-WoW",
["Lunaris - Draconic-WoW"] = "Lunaris - Draconic-WoW",
["Teo - Draconic-WoW"] = "Teo - Draconic-WoW",
["Zara - Draconic-WoW"] = "Zara - Draconic-WoW",
["Siiri - Draconic-WoW"] = "Siiri - Draconic-WoW",
["Sophia - Draconic-WoW"] = "Sophia - Draconic-WoW",
["Iridian - Draconic-WoW"] = "Iridian - Draconic-WoW",
["Shieldhero - Draconic-WoW"] = "Shieldhero - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Nana - Draconic-WoW"] = "Nana - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Pakkah - Draconic-WoW"] = "Pakkah - Draconic-WoW",
["Hoz - Draconic-WoW"] = "Hoz - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Packwarden - Draconic-WoW"] = "Packwarden - Draconic-WoW",
},
["profiles"] = {
["Mika - Draconic-WoW"] = {
},
["Hoz - Draconic-WoW"] = {
},
["Orias - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sampson - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Marvo - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Highcliff - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Parthos - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Marlon - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Zarah - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Yaaru - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Austen - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Kuthbert - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Anders - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Nana - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Vela - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Hexandchill - Draconic-WoW"] = {
},
["Iridian - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Punchline - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Pedaar - Draconic-WoW"] = {
},
["Utherd - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Lambert - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Channa - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Shamwow - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Huk - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Zara - Draconic-WoW"] = {
},
["Siiri - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Sophia - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Nikaj - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Theya - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Artanis - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
},
}
BetterWardrobe_SubstituteItemData = {
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Default",
["Stableslot - Draconic-WoW"] = "Default",
["Dagda - Draconic-WoW"] = "Default",
["Graham - Draconic-WoW"] = "Default",
["Levara - Draconic-WoW"] = "Default",
["Reese - Draconic-WoW"] = "Default",
["Nando - Draconic-WoW"] = "Default",
["Azert - Draconic-WoW"] = "Default",
["Rameth - Draconic-WoW"] = "Default",
["Gunnar - Draconic-WoW"] = "Default",
["Krista - Draconic-WoW"] = "Default",
["Tav - Draconic-WoW"] = "Default",
["Kashel - Draconic-WoW"] = "Default",
["Stonebreaker - Draconic-WoW"] = "Default",
["Consecrazy - Draconic-WoW"] = "Default",
["Carlo - Draconic-WoW"] = "Default",
["Parthos - Draconic-WoW"] = "Default",
["Melrose - Draconic-WoW"] = "Default",
["Azra - Draconic-WoW"] = "Default",
["Benny - Draconic-WoW"] = "Default",
["Primarch - Draconic-WoW"] = "Default",
["Meltface - Draconic-WoW"] = "Default",
["Shavonda - Draconic-WoW"] = "Default",
["Felonme - Draconic-WoW"] = "Default",
["Red - Draconic-WoW"] = "Default",
["Shapow - Draconic-WoW"] = "Default",
["Vela - Draconic-WoW"] = "Default",
["Starweaver - Draconic-WoW"] = "Default",
["Hammerme - Draconic-WoW"] = "Default",
["Testtest - Draconic-WoW"] = "Default",
["Mercer - Draconic-WoW"] = "Default",
["Golo - Draconic-WoW"] = "Default",
["Sorn - Draconic-WoW"] = "Default",
["Khazel - Draconic-WoW"] = "Default",
["Kefka - Draconic-WoW"] = "Default",
["Sicalicious - Draconic-WoW"] = "Default",
["Penance - Draconic-WoW"] = "Default",
["Deez - Draconic-WoW"] = "Default",
["Holden - Draconic-WoW"] = "Default",
["Utherd - Draconic-WoW"] = "Default",
["Umbralight - Draconic-WoW"] = "Default",
["Earthevo - Draconic-WoW"] = "Default",
["Talairn - Draconic-WoW"] = "Default",
["Hexcuseme - Draconic-WoW"] = "Default",
["Vulkan - Draconic-WoW"] = "Default",
["Quiverme - Draconic-WoW"] = "Default",
["Nikaj - Draconic-WoW"] = "Default",
["Reynolds - Draconic-WoW"] = "Default",
["Van - Draconic-WoW"] = "Default",
["Thornhand - Draconic-WoW"] = "Default",
["Blocksmith - Draconic-WoW"] = "Default",
["Sanstus - Draconic-WoW"] = "Default",
["Jobe - Draconic-WoW"] = "Default",
["Artanis - Draconic-WoW"] = "Default",
["Koby - Draconic-WoW"] = "Default",
["Zhago - Draconic-WoW"] = "Default",
["Orias - Draconic-WoW"] = "Default",
["Hatcher - Draconic-WoW"] = "Default",
["Zarah - Draconic-WoW"] = "Default",
["Adnap - Draconic-WoW"] = "Default",
["Sampson - Draconic-WoW"] = "Default",
["Leyline - Draconic-WoW"] = "Default",
["Hemogoblin - Draconic-WoW"] = "Default",
["Marvo - Draconic-WoW"] = "Default",
["Gantz - Draconic-WoW"] = "Default",
["Draxtwo - Draconic-WoW"] = "Default",
["Oomah - Draconic-WoW"] = "Default",
["Foehawk - Draconic-WoW"] = "Default",
["Dix - Draconic-WoW"] = "Default",
["Havik - Draconic-WoW"] = "Default",
["Yancy - Draconic-WoW"] = "Default",
["Thirstseal - Draconic-WoW"] = "Default",
["Nolan - Draconic-WoW"] = "Default",
["Momonga - Draconic-WoW"] = "Default",
["Kardol - Draconic-WoW"] = "Default",
["Ikanoa - Draconic-WoW"] = "Default",
["Derek - Draconic-WoW"] = "Default",
["Ava - Draconic-WoW"] = "Default",
["Cedrick - Draconic-WoW"] = "Default",
["Dreya - Draconic-WoW"] = "Default",
["Vaedan - Draconic-WoW"] = "Default",
["Korik - Draconic-WoW"] = "Default",
["Parah - Draconic-WoW"] = "Default",
["Alaana - Draconic-WoW"] = "Default",
["Celestra - Draconic-WoW"] = "Default",
["Thiccplates - Draconic-WoW"] = "Default",
["Valanese - Draconic-WoW"] = "Default",
["Hitcap - Draconic-WoW"] = "Default",
["Kalano - Draconic-WoW"] = "Default",
["Roland - Draconic-WoW"] = "Default",
["Lars - Draconic-WoW"] = "Default",
["Sebas - Draconic-WoW"] = "Default",
["Voxghar - Draconic-WoW"] = "Default",
["Payton - Draconic-WoW"] = "Default",
["Zezima - Draconic-WoW"] = "Default",
["Laaj - Draconic-WoW"] = "Default",
["Punchline - Draconic-WoW"] = "Default",
["Lia - Draconic-WoW"] = "Default",
["Warren - Draconic-WoW"] = "Default",
["Davos - Draconic-WoW"] = "Default",
["Tredwell - Draconic-WoW"] = "Default",
["Shamwow - Draconic-WoW"] = "Default",
["Mogh - Draconic-WoW"] = "Default",
["Padrik - Draconic-WoW"] = "Default",
["Leonard - Draconic-WoW"] = "Default",
["Danvers - Draconic-WoW"] = "Default",
["Adepta - Draconic-WoW"] = "Default",
["Kaitlan - Draconic-WoW"] = "Default",
["Tywin - Draconic-WoW"] = "Default",
["Elden - Draconic-WoW"] = "Default",
["Ren - Draconic-WoW"] = "Default",
["Sebastian - Draconic-WoW"] = "Default",
["Boris - Draconic-WoW"] = "Default",
["Prak - Draconic-WoW"] = "Default",
["Whirlwinded - Draconic-WoW"] = "Default",
["Coggle - Draconic-WoW"] = "Default",
["Moremojo - Draconic-WoW"] = "Default",
["Mega - Draconic-WoW"] = "Default",
["Danath - Draconic-WoW"] = "Default",
["Brax - Draconic-WoW"] = "Default",
["Theodore - Draconic-WoW"] = "Default",
["Kodetha - Draconic-WoW"] = "Default",
["Sica - Draconic-WoW"] = "Default",
["Aimme - Draconic-WoW"] = "Default",
["Tavish - Draconic-WoW"] = "Default",
["Robb - Draconic-WoW"] = "Default",
["Anega - Draconic-WoW"] = "Default",
["Ballistics - Draconic-WoW"] = "Default",
["Griffith - Draconic-WoW"] = "Default",
["Frag - Draconic-WoW"] = "Default",
["Eversong - Draconic-WoW"] = "Default",
["Banks - Draconic-WoW"] = "Default",
["Justicaris - Draconic-WoW"] = "Default",
["Xenos - Draconic-WoW"] = "Default",
["Celina - Draconic-WoW"] = "Default",
["Baku - Draconic-WoW"] = "Default",
["Regis - Draconic-WoW"] = "Default",
["Kuthbert - Draconic-WoW"] = "Default",
["Austen - Draconic-WoW"] = "Default",
["Harlem - Draconic-WoW"] = "Default",
["Vampstamp - Draconic-WoW"] = "Default",
["Ashford - Draconic-WoW"] = "Default",
["Jackson - Draconic-WoW"] = "Default",
["Kurtak - Draconic-WoW"] = "Default",
["Silva - Draconic-WoW"] = "Default",
["Hoof - Draconic-WoW"] = "Default",
["Erett - Draconic-WoW"] = "Default",
["Zhad - Draconic-WoW"] = "Default",
["Makaio - Draconic-WoW"] = "Default",
["Alice - Draconic-WoW"] = "Default",
["Shanna - Draconic-WoW"] = "Default",
["Shale - Draconic-WoW"] = "Default",
["Xavik - Draconic-WoW"] = "Default",
["Pedaar - Draconic-WoW"] = "Default",
["Phea - Draconic-WoW"] = "Default",
["Channa - Draconic-WoW"] = "Default",
["Bishop - Draconic-WoW"] = "Default",
["Edwards - Draconic-WoW"] = "Default",
["Cecil - Draconic-WoW"] = "Default",
["Cyric - Draconic-WoW"] = "Default",
["Kalzak - Draconic-WoW"] = "Default",
["Grammon - Draconic-WoW"] = "Default",
["Oroth - Draconic-WoW"] = "Default",
["Astaron - Draconic-WoW"] = "Default",
["Invaris - Draconic-WoW"] = "Default",
["Ralzin - Draconic-WoW"] = "Default",
["Zital - Draconic-WoW"] = "Default",
["Grayson - Draconic-WoW"] = "Default",
["Leyla - Draconic-WoW"] = "Default",
["Astraea - Draconic-WoW"] = "Default",
["Elaria - Draconic-WoW"] = "Default",
["Argyle - Draconic-WoW"] = "Default",
["Boltaction - Draconic-WoW"] = "Default",
["Esi - Draconic-WoW"] = "Default",
["Raynaud - Draconic-WoW"] = "Default",
["Tonka - Draconic-WoW"] = "Default",
["Highcliff - Draconic-WoW"] = "Default",
["Marlon - Draconic-WoW"] = "Default",
["Kora - Draconic-WoW"] = "Default",
["Yaaru - Draconic-WoW"] = "Default",
["Qwendy - Draconic-WoW"] = "Default",
["Shadowban - Draconic-WoW"] = "Default",
["Alexius - Draconic-WoW"] = "Default",
["Lolth - Draconic-WoW"] = "Default",
["Nelson - Draconic-WoW"] = "Default",
["Eve - Draconic-WoW"] = "Default",
["Zaibach - Draconic-WoW"] = "Default",
["Magna - Draconic-WoW"] = "Default",
["Satren - Draconic-WoW"] = "Default",
["Xathos - Draconic-WoW"] = "Default",
["Crackhammer - Draconic-WoW"] = "Default",
["Sava - Draconic-WoW"] = "Default",
["Perapera - Draconic-WoW"] = "Default",
["Ruugar - Draconic-WoW"] = "Default",
["Sic - Draconic-WoW"] = "Default",
["Vandrus - Draconic-WoW"] = "Default",
["Smiteme - Draconic-WoW"] = "Default",
["Kazil - Draconic-WoW"] = "Default",
["Meatstick - Draconic-WoW"] = "Default",
["Auria - Draconic-WoW"] = "Default",
["Ironsides - Draconic-WoW"] = "Default",
["Harold - Draconic-WoW"] = "Default",
["Davin - Draconic-WoW"] = "Default",
["Halztraz - Draconic-WoW"] = "Default",
["Tylosh - Draconic-WoW"] = "Default",
["Hexappeal - Draconic-WoW"] = "Default",
["Korla - Draconic-WoW"] = "Default",
["Judgemental - Draconic-WoW"] = "Default",
["Morvane - Draconic-WoW"] = "Default",
["Feltide - Draconic-WoW"] = "Default",
["Hexandchill - Draconic-WoW"] = "Default",
["Rahddon - Draconic-WoW"] = "Default",
["Piuy - Draconic-WoW"] = "Default",
["Kelmenvor - Draconic-WoW"] = "Default",
["Solanna - Draconic-WoW"] = "Default",
["Totemtease - Draconic-WoW"] = "Default",
["Dazlith - Draconic-WoW"] = "Default",
["Dermot - Draconic-WoW"] = "Default",
["Larixa - Draconic-WoW"] = "Default",
["Enoch - Draconic-WoW"] = "Default",
["Arred - Draconic-WoW"] = "Default",
["Zenat - Draconic-WoW"] = "Default",
["Lisbeth - Draconic-WoW"] = "Default",
["Ironward - Draconic-WoW"] = "Default",
["Crakash - Draconic-WoW"] = "Default",
["Oren - Draconic-WoW"] = "Default",
["Mojoe - Draconic-WoW"] = "Default",
["Harandor - Draconic-WoW"] = "Default",
["Rageagainst - Draconic-WoW"] = "Default",
["Movado - Draconic-WoW"] = "Default",
["Ada - Draconic-WoW"] = "Default",
["Tristian - Draconic-WoW"] = "Default",
["Lambert - Draconic-WoW"] = "Default",
["Pakmojo - Draconic-WoW"] = "Default",
["Rend - Draconic-WoW"] = "Default",
["Roone - Draconic-WoW"] = "Default",
["Huk - Draconic-WoW"] = "Default",
["Lunaris - Draconic-WoW"] = "Default",
["Teo - Draconic-WoW"] = "Default",
["Zara - Draconic-WoW"] = "Default",
["Siiri - Draconic-WoW"] = "Default",
["Sophia - Draconic-WoW"] = "Default",
["Iridian - Draconic-WoW"] = "Default",
["Shieldhero - Draconic-WoW"] = "Default",
["Nolen - Draconic-WoW"] = "Default",
["Endra - Draconic-WoW"] = "Default",
["Wangz - Draconic-WoW"] = "Default",
["Nana - Draconic-WoW"] = "Default",
["Volkaris - Draconic-WoW"] = "Default",
["Magnus - Draconic-WoW"] = "Default",
["Theya - Draconic-WoW"] = "Default",
["Atrissa - Draconic-WoW"] = "Default",
["Quincy - Draconic-WoW"] = "Default",
["Mav - Draconic-WoW"] = "Default",
["Anders - Draconic-WoW"] = "Default",
["Daamis - Draconic-WoW"] = "Default",
["Moroes - Draconic-WoW"] = "Default",
["Pakkah - Draconic-WoW"] = "Default",
["Hoz - Draconic-WoW"] = "Default",
["Sarsam - Draconic-WoW"] = "Default",
["Mika - Draconic-WoW"] = "Default",
["Packwarden - Draconic-WoW"] = "Default",
},
["profiles"] = {
["Default"] = {
},
},
}
BetterWardrobe_ListData = {
["favoritesDB"] = {
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Erovia - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Dagda - Draconic-WoW"] = "Dagda - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Rameth - Draconic-WoW"] = "Rameth - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Krista - Draconic-WoW"] = "Krista - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Consecrazy - Draconic-WoW"] = "Consecrazy - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Parthos - Draconic-WoW"] = "Parthos - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Azra - Draconic-WoW"] = "Azra - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Felonme - Draconic-WoW"] = "Felonme - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Vela - Draconic-WoW"] = "Vela - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Hammerme - Draconic-WoW"] = "Hammerme - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Sorn - Draconic-WoW"] = "Sorn - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Penance - Draconic-WoW"] = "Penance - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Holden - Draconic-WoW"] = "Holden - Draconic-WoW",
["Utherd - Draconic-WoW"] = "Utherd - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Hexcuseme - Draconic-WoW"] = "Hexcuseme - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Quiverme - Draconic-WoW"] = "Quiverme - Draconic-WoW",
["Nikaj - Draconic-WoW"] = "Nikaj - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Blocksmith - Draconic-WoW"] = "Blocksmith - Draconic-WoW",
["Sanstus - Draconic-WoW"] = "Sanstus - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Artanis - Draconic-WoW"] = "Artanis - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Orias - Draconic-WoW"] = "Orias - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Zarah - Draconic-WoW"] = "Zarah - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Leyline - Draconic-WoW"] = "Leyline - Draconic-WoW",
["Hemogoblin - Draconic-WoW"] = "Hemogoblin - Draconic-WoW",
["Marvo - Draconic-WoW"] = "Marvo - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Foehawk - Draconic-WoW"] = "Foehawk - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Thirstseal - Draconic-WoW"] = "Thirstseal - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Ikanoa - Draconic-WoW"] = "Ikanoa - Draconic-WoW",
["Derek - Draconic-WoW"] = "Derek - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Alaana - Draconic-WoW"] = "Alaana - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Thiccplates - Draconic-WoW"] = "Thiccplates - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Punchline - Draconic-WoW"] = "Punchline - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Shamwow - Draconic-WoW"] = "Shamwow - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Leonard - Draconic-WoW"] = "Leonard - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Tywin - Draconic-WoW"] = "Tywin - Draconic-WoW",
["Elden - Draconic-WoW"] = "Elden - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Sebastian - Draconic-WoW"] = "Sebastian - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Whirlwinded - Draconic-WoW"] = "Whirlwinded - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Danath - Draconic-WoW"] = "Danath - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Aimme - Draconic-WoW"] = "Aimme - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Eversong - Draconic-WoW"] = "Eversong - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Kuthbert - Draconic-WoW"] = "Kuthbert - Draconic-WoW",
["Austen - Draconic-WoW"] = "Austen - Draconic-WoW",
["Harlem - Draconic-WoW"] = "Harlem - Draconic-WoW",
["Vampstamp - Draconic-WoW"] = "Vampstamp - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Jackson - Draconic-WoW"] = "Jackson - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Silva - Draconic-WoW"] = "Silva - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Makaio - Draconic-WoW"] = "Makaio - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Shanna - Draconic-WoW"] = "Shanna - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Xavik - Draconic-WoW"] = "Xavik - Draconic-WoW",
["Pedaar - Draconic-WoW"] = "Pedaar - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Channa - Draconic-WoW"] = "Channa - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Kalzak - Draconic-WoW"] = "Kalzak - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Oroth - Draconic-WoW"] = "Oroth - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Astraea - Draconic-WoW"] = "Astraea - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Boltaction - Draconic-WoW"] = "Boltaction - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Tonka - Draconic-WoW"] = "Tonka - Draconic-WoW",
["Highcliff - Draconic-WoW"] = "Highcliff - Draconic-WoW",
["Marlon - Draconic-WoW"] = "Marlon - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Yaaru - Draconic-WoW"] = "Yaaru - Draconic-WoW",
["Qwendy - Draconic-WoW"] = "Qwendy - Draconic-WoW",
["Shadowban - Draconic-WoW"] = "Shadowban - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Zaibach - Draconic-WoW"] = "Zaibach - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Sava - Draconic-WoW"] = "Sava - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Smiteme - Draconic-WoW"] = "Smiteme - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Ironsides - Draconic-WoW"] = "Ironsides - Draconic-WoW",
["Harold - Draconic-WoW"] = "Harold - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Hexappeal - Draconic-WoW"] = "Hexappeal - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Judgemental - Draconic-WoW"] = "Judgemental - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Feltide - Draconic-WoW"] = "Feltide - Draconic-WoW",
["Hexandchill - Draconic-WoW"] = "Hexandchill - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Totemtease - Draconic-WoW"] = "Totemtease - Draconic-WoW",
["Dazlith - Draconic-WoW"] = "Dazlith - Draconic-WoW",
["Dermot - Draconic-WoW"] = "Dermot - Draconic-WoW",
["Larixa - Draconic-WoW"] = "Larixa - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Arred - Draconic-WoW"] = "Arred - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Ironward - Draconic-WoW"] = "Ironward - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Harandor - Draconic-WoW"] = "Harandor - Draconic-WoW",
["Rageagainst - Draconic-WoW"] = "Rageagainst - Draconic-WoW",
["Movado - Draconic-WoW"] = "Movado - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Lambert - Draconic-WoW"] = "Lambert - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Rend - Draconic-WoW"] = "Rend - Draconic-WoW",
["Roone - Draconic-WoW"] = "Roone - Draconic-WoW",
["Huk - Draconic-WoW"] = "Huk - Draconic-WoW",
["Lunaris - Draconic-WoW"] = "Lunaris - Draconic-WoW",
["Teo - Draconic-WoW"] = "Teo - Draconic-WoW",
["Zara - Draconic-WoW"] = "Zara - Draconic-WoW",
["Siiri - Draconic-WoW"] = "Siiri - Draconic-WoW",
["Sophia - Draconic-WoW"] = "Sophia - Draconic-WoW",
["Iridian - Draconic-WoW"] = "Iridian - Draconic-WoW",
["Shieldhero - Draconic-WoW"] = "Shieldhero - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Nana - Draconic-WoW"] = "Nana - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Pakkah - Draconic-WoW"] = "Pakkah - Draconic-WoW",
["Hoz - Draconic-WoW"] = "Hoz - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Packwarden - Draconic-WoW"] = "Packwarden - Draconic-WoW",
},
["profiles"] = {
["Whirlwinded - Draconic-WoW"] = {
},
["Hoz - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Aimme - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Parthos - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Kuthbert - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Austen - Draconic-WoW"] = {
},
["Shavonda - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Nana - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Vela - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Iridian - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Pedaar - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Channa - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Utherd - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Nikaj - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Artanis - Draconic-WoW"] = {
},
["Orias - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Zarah - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sampson - Draconic-WoW"] = {
},
["Marvo - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Highcliff - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Marlon - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Yaaru - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Ava - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Judgemental - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Hexandchill - Draconic-WoW"] = {
},
["Mika - Draconic-WoW"] = {
},
["Anders - Draconic-WoW"] = {
},
["Punchline - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Lambert - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Huk - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Zara - Draconic-WoW"] = {
},
["Siiri - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Shieldhero - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Ironsides - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Theya - Draconic-WoW"] = {
},
["Sophia - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
},
},
["collectionListDB"] = {
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Erovia - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Dagda - Draconic-WoW"] = "Dagda - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Rameth - Draconic-WoW"] = "Rameth - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Krista - Draconic-WoW"] = "Krista - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Consecrazy - Draconic-WoW"] = "Consecrazy - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Parthos - Draconic-WoW"] = "Parthos - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Azra - Draconic-WoW"] = "Azra - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Felonme - Draconic-WoW"] = "Felonme - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Vela - Draconic-WoW"] = "Vela - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Hammerme - Draconic-WoW"] = "Hammerme - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Sorn - Draconic-WoW"] = "Sorn - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Penance - Draconic-WoW"] = "Penance - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Holden - Draconic-WoW"] = "Holden - Draconic-WoW",
["Utherd - Draconic-WoW"] = "Utherd - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Hexcuseme - Draconic-WoW"] = "Hexcuseme - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Quiverme - Draconic-WoW"] = "Quiverme - Draconic-WoW",
["Nikaj - Draconic-WoW"] = "Nikaj - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Blocksmith - Draconic-WoW"] = "Blocksmith - Draconic-WoW",
["Sanstus - Draconic-WoW"] = "Sanstus - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Artanis - Draconic-WoW"] = "Artanis - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Orias - Draconic-WoW"] = "Orias - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Zarah - Draconic-WoW"] = "Zarah - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Leyline - Draconic-WoW"] = "Leyline - Draconic-WoW",
["Hemogoblin - Draconic-WoW"] = "Hemogoblin - Draconic-WoW",
["Marvo - Draconic-WoW"] = "Marvo - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Foehawk - Draconic-WoW"] = "Foehawk - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Thirstseal - Draconic-WoW"] = "Thirstseal - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Ikanoa - Draconic-WoW"] = "Ikanoa - Draconic-WoW",
["Derek - Draconic-WoW"] = "Derek - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Alaana - Draconic-WoW"] = "Alaana - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Thiccplates - Draconic-WoW"] = "Thiccplates - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Punchline - Draconic-WoW"] = "Punchline - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Shamwow - Draconic-WoW"] = "Shamwow - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Leonard - Draconic-WoW"] = "Leonard - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Tywin - Draconic-WoW"] = "Tywin - Draconic-WoW",
["Elden - Draconic-WoW"] = "Elden - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Sebastian - Draconic-WoW"] = "Sebastian - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Whirlwinded - Draconic-WoW"] = "Whirlwinded - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Danath - Draconic-WoW"] = "Danath - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Aimme - Draconic-WoW"] = "Aimme - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Eversong - Draconic-WoW"] = "Eversong - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Kuthbert - Draconic-WoW"] = "Kuthbert - Draconic-WoW",
["Austen - Draconic-WoW"] = "Austen - Draconic-WoW",
["Harlem - Draconic-WoW"] = "Harlem - Draconic-WoW",
["Vampstamp - Draconic-WoW"] = "Vampstamp - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Jackson - Draconic-WoW"] = "Jackson - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Silva - Draconic-WoW"] = "Silva - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Makaio - Draconic-WoW"] = "Makaio - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Shanna - Draconic-WoW"] = "Shanna - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Xavik - Draconic-WoW"] = "Xavik - Draconic-WoW",
["Pedaar - Draconic-WoW"] = "Pedaar - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Channa - Draconic-WoW"] = "Channa - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Kalzak - Draconic-WoW"] = "Kalzak - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Oroth - Draconic-WoW"] = "Oroth - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Astraea - Draconic-WoW"] = "Astraea - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Boltaction - Draconic-WoW"] = "Boltaction - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Tonka - Draconic-WoW"] = "Tonka - Draconic-WoW",
["Highcliff - Draconic-WoW"] = "Highcliff - Draconic-WoW",
["Marlon - Draconic-WoW"] = "Marlon - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Yaaru - Draconic-WoW"] = "Yaaru - Draconic-WoW",
["Qwendy - Draconic-WoW"] = "Qwendy - Draconic-WoW",
["Shadowban - Draconic-WoW"] = "Shadowban - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Zaibach - Draconic-WoW"] = "Zaibach - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Sava - Draconic-WoW"] = "Sava - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Smiteme - Draconic-WoW"] = "Smiteme - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Ironsides - Draconic-WoW"] = "Ironsides - Draconic-WoW",
["Harold - Draconic-WoW"] = "Harold - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Hexappeal - Draconic-WoW"] = "Hexappeal - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Judgemental - Draconic-WoW"] = "Judgemental - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Feltide - Draconic-WoW"] = "Feltide - Draconic-WoW",
["Hexandchill - Draconic-WoW"] = "Hexandchill - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Totemtease - Draconic-WoW"] = "Totemtease - Draconic-WoW",
["Dazlith - Draconic-WoW"] = "Dazlith - Draconic-WoW",
["Dermot - Draconic-WoW"] = "Dermot - Draconic-WoW",
["Larixa - Draconic-WoW"] = "Larixa - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Arred - Draconic-WoW"] = "Arred - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Ironward - Draconic-WoW"] = "Ironward - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Harandor - Draconic-WoW"] = "Harandor - Draconic-WoW",
["Rageagainst - Draconic-WoW"] = "Rageagainst - Draconic-WoW",
["Movado - Draconic-WoW"] = "Movado - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Lambert - Draconic-WoW"] = "Lambert - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Rend - Draconic-WoW"] = "Rend - Draconic-WoW",
["Roone - Draconic-WoW"] = "Roone - Draconic-WoW",
["Huk - Draconic-WoW"] = "Huk - Draconic-WoW",
["Lunaris - Draconic-WoW"] = "Lunaris - Draconic-WoW",
["Teo - Draconic-WoW"] = "Teo - Draconic-WoW",
["Zara - Draconic-WoW"] = "Zara - Draconic-WoW",
["Siiri - Draconic-WoW"] = "Siiri - Draconic-WoW",
["Sophia - Draconic-WoW"] = "Sophia - Draconic-WoW",
["Iridian - Draconic-WoW"] = "Iridian - Draconic-WoW",
["Shieldhero - Draconic-WoW"] = "Shieldhero - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Nana - Draconic-WoW"] = "Nana - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Pakkah - Draconic-WoW"] = "Pakkah - Draconic-WoW",
["Hoz - Draconic-WoW"] = "Hoz - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Packwarden - Draconic-WoW"] = "Packwarden - Draconic-WoW",
},
["profiles"] = {
["Mika - Draconic-WoW"] = {
},
["Hoz - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Quincy - Draconic-WoW"] = {
},
["Sica - Draconic-WoW"] = {
},
["Nando - Draconic-WoW"] = {
},
["Azert - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Ballistics - Draconic-WoW"] = {
},
["Griffith - Draconic-WoW"] = {
},
["Kashel - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Carlo - Draconic-WoW"] = {
},
["Parthos - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Celina - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Kuthbert - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Meltface - Draconic-WoW"] = {
},
["Shavonda - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Kurtak - Draconic-WoW"] = {
},
["Silva - Draconic-WoW"] = {
},
["Hoof - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Vela - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Erett - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Testtest - Draconic-WoW"] = {
},
["Endra - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Shale - Draconic-WoW"] = {
},
["Pedaar - Draconic-WoW"] = {
},
["Khazel - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Kefka - Draconic-WoW"] = {
},
["Channa - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Cyric - Draconic-WoW"] = {
},
["Utherd - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Earthevo - Draconic-WoW"] = {
},
["Talairn - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Thornhand - Draconic-WoW"] = {
},
["Ralzin - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Zenat - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Artanis - Draconic-WoW"] = {
},
["Enoch - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Dagda - Draconic-WoW"] = {
},
["Zhago - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Anders - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Sophia - Draconic-WoW"] = {
},
["Orias - Draconic-WoW"] = {
},
["Zarah - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Theya - Draconic-WoW"] = {
},
["Sampson - Draconic-WoW"] = {
},
["Ren - Draconic-WoW"] = {
},
["Danath - Draconic-WoW"] = {
},
["Nana - Draconic-WoW"] = {
},
["Marvo - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Gunnar - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Oomah - Draconic-WoW"] = {
},
["Esi - Draconic-WoW"] = {
},
["Red - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Shanna - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Raynaud - Draconic-WoW"] = {
},
["Perapera - Draconic-WoW"] = {
},
["Dix - Draconic-WoW"] = {
},
["Davin - Draconic-WoW"] = {
},
["Highcliff - Draconic-WoW"] = {
},
["Sarsam - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Satren - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Wangz - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Marlon - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Yaaru - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Derek - Draconic-WoW"] = {
},
["Ava - Draconic-WoW"] = {
},
["Cedrick - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Vaedan - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Parah - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Sava - Draconic-WoW"] = {
},
["Argyle - Draconic-WoW"] = {
},
["Kodetha - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Hitcap - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Auria - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Lars - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Halztraz - Draconic-WoW"] = {
},
["Yancy - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Hexandchill - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Payton - Draconic-WoW"] = {
},
["Zezima - Draconic-WoW"] = {
},
["Laaj - Draconic-WoW"] = {
},
["Punchline - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Kelmenvor - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Xenos - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Davos - Draconic-WoW"] = {
},
["Crakash - Draconic-WoW"] = {
},
["Lambert - Draconic-WoW"] = {
},
["Mojoe - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Voxghar - Draconic-WoW"] = {
},
["Koby - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Shamwow - Draconic-WoW"] = {
},
["Theodore - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Mogh - Draconic-WoW"] = {
},
["Padrik - Draconic-WoW"] = {
},
["Huk - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Zara - Draconic-WoW"] = {
},
["Siiri - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Piuy - Draconic-WoW"] = {
},
["Tylosh - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Volkaris - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Nikaj - Draconic-WoW"] = {
},
["Makaio - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
["lists"] = {
{
["item"] = {
[23975] = true,
[23976] = true,
[97173] = true,
[23977] = true,
[97177] = true,
[97179] = true,
[97181] = true,
[23979] = true,
[37827] = true,
[37822] = true,
[37823] = true,
[23981] = true,
[37825] = true,
[23982] = true,
[37858] = true,
[37828] = true,
[37829] = true,
[37826] = true,
[37824] = true,
[97176] = true,
[97171] = true,
[23980] = true,
[23978] = true,
[97184] = true,
[11168] = true,
},
["set"] = {
[4133] = {
[97177] = true,
[97181] = true,
[11168] = true,
[97184] = true,
[97179] = true,
[97176] = true,
[97173] = true,
[97171] = true,
},
[1663] = {
[37829] = true,
[37822] = true,
[37823] = true,
[37824] = true,
[37825] = true,
[37826] = true,
[37827] = true,
[37828] = true,
[37858] = true,
},
[71] = {
[23982] = true,
[23976] = true,
[23977] = true,
[23978] = true,
[23979] = true,
[23980] = true,
[23981] = true,
[23975] = true,
},
},
},
},
},
["Moroes - Draconic-WoW"] = {
},
["Austen - Draconic-WoW"] = {
},
["Iridian - Draconic-WoW"] = {
},
["Boris - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
},
},
["lastUpdte"] = 1,
["OutfitDB"] = {
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Erovia - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Dagda - Draconic-WoW"] = "Dagda - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Rameth - Draconic-WoW"] = "Rameth - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Krista - Draconic-WoW"] = "Krista - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Consecrazy - Draconic-WoW"] = "Consecrazy - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Parthos - Draconic-WoW"] = "Parthos - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Azra - Draconic-WoW"] = "Azra - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Felonme - Draconic-WoW"] = "Felonme - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Vela - Draconic-WoW"] = "Vela - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Hammerme - Draconic-WoW"] = "Hammerme - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Sorn - Draconic-WoW"] = "Sorn - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Penance - Draconic-WoW"] = "Penance - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Holden - Draconic-WoW"] = "Holden - Draconic-WoW",
["Utherd - Draconic-WoW"] = "Utherd - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Hexcuseme - Draconic-WoW"] = "Hexcuseme - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Quiverme - Draconic-WoW"] = "Quiverme - Draconic-WoW",
["Nikaj - Draconic-WoW"] = "Nikaj - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Blocksmith - Draconic-WoW"] = "Blocksmith - Draconic-WoW",
["Sanstus - Draconic-WoW"] = "Sanstus - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Artanis - Draconic-WoW"] = "Artanis - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Orias - Draconic-WoW"] = "Orias - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Zarah - Draconic-WoW"] = "Zarah - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Leyline - Draconic-WoW"] = "Leyline - Draconic-WoW",
["Hemogoblin - Draconic-WoW"] = "Hemogoblin - Draconic-WoW",
["Marvo - Draconic-WoW"] = "Marvo - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Foehawk - Draconic-WoW"] = "Foehawk - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Thirstseal - Draconic-WoW"] = "Thirstseal - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Ikanoa - Draconic-WoW"] = "Ikanoa - Draconic-WoW",
["Derek - Draconic-WoW"] = "Derek - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Alaana - Draconic-WoW"] = "Alaana - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Thiccplates - Draconic-WoW"] = "Thiccplates - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Punchline - Draconic-WoW"] = "Punchline - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Shamwow - Draconic-WoW"] = "Shamwow - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Leonard - Draconic-WoW"] = "Leonard - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Tywin - Draconic-WoW"] = "Tywin - Draconic-WoW",
["Elden - Draconic-WoW"] = "Elden - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Sebastian - Draconic-WoW"] = "Sebastian - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Whirlwinded - Draconic-WoW"] = "Whirlwinded - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Danath - Draconic-WoW"] = "Danath - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Aimme - Draconic-WoW"] = "Aimme - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Eversong - Draconic-WoW"] = "Eversong - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Kuthbert - Draconic-WoW"] = "Kuthbert - Draconic-WoW",
["Austen - Draconic-WoW"] = "Austen - Draconic-WoW",
["Harlem - Draconic-WoW"] = "Harlem - Draconic-WoW",
["Vampstamp - Draconic-WoW"] = "Vampstamp - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Jackson - Draconic-WoW"] = "Jackson - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Silva - Draconic-WoW"] = "Silva - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Makaio - Draconic-WoW"] = "Makaio - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Shanna - Draconic-WoW"] = "Shanna - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Xavik - Draconic-WoW"] = "Xavik - Draconic-WoW",
["Pedaar - Draconic-WoW"] = "Pedaar - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Channa - Draconic-WoW"] = "Channa - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Kalzak - Draconic-WoW"] = "Kalzak - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Oroth - Draconic-WoW"] = "Oroth - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Astraea - Draconic-WoW"] = "Astraea - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Boltaction - Draconic-WoW"] = "Boltaction - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Tonka - Draconic-WoW"] = "Tonka - Draconic-WoW",
["Highcliff - Draconic-WoW"] = "Highcliff - Draconic-WoW",
["Marlon - Draconic-WoW"] = "Marlon - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Yaaru - Draconic-WoW"] = "Yaaru - Draconic-WoW",
["Qwendy - Draconic-WoW"] = "Qwendy - Draconic-WoW",
["Shadowban - Draconic-WoW"] = "Shadowban - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Zaibach - Draconic-WoW"] = "Zaibach - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Sava - Draconic-WoW"] = "Sava - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Smiteme - Draconic-WoW"] = "Smiteme - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Ironsides - Draconic-WoW"] = "Ironsides - Draconic-WoW",
["Harold - Draconic-WoW"] = "Harold - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Hexappeal - Draconic-WoW"] = "Hexappeal - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Judgemental - Draconic-WoW"] = "Judgemental - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Feltide - Draconic-WoW"] = "Feltide - Draconic-WoW",
["Hexandchill - Draconic-WoW"] = "Hexandchill - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Totemtease - Draconic-WoW"] = "Totemtease - Draconic-WoW",
["Dazlith - Draconic-WoW"] = "Dazlith - Draconic-WoW",
["Dermot - Draconic-WoW"] = "Dermot - Draconic-WoW",
["Larixa - Draconic-WoW"] = "Larixa - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Arred - Draconic-WoW"] = "Arred - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Ironward - Draconic-WoW"] = "Ironward - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Harandor - Draconic-WoW"] = "Harandor - Draconic-WoW",
["Rageagainst - Draconic-WoW"] = "Rageagainst - Draconic-WoW",
["Movado - Draconic-WoW"] = "Movado - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Lambert - Draconic-WoW"] = "Lambert - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Rend - Draconic-WoW"] = "Rend - Draconic-WoW",
["Roone - Draconic-WoW"] = "Roone - Draconic-WoW",
["Huk - Draconic-WoW"] = "Huk - Draconic-WoW",
["Lunaris - Draconic-WoW"] = "Lunaris - Draconic-WoW",
["Teo - Draconic-WoW"] = "Teo - Draconic-WoW",
["Zara - Draconic-WoW"] = "Zara - Draconic-WoW",
["Siiri - Draconic-WoW"] = "Siiri - Draconic-WoW",
["Sophia - Draconic-WoW"] = "Sophia - Draconic-WoW",
["Iridian - Draconic-WoW"] = "Iridian - Draconic-WoW",
["Shieldhero - Draconic-WoW"] = "Shieldhero - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Nana - Draconic-WoW"] = "Nana - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Pakkah - Draconic-WoW"] = "Pakkah - Draconic-WoW",
["Hoz - Draconic-WoW"] = "Hoz - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Packwarden - Draconic-WoW"] = "Packwarden - Draconic-WoW",
},
},
["HiddenAppearanceDB"] = {
["profileKeys"] = {
["Erovia - Draconic-WoW"] = "Erovia - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Dagda - Draconic-WoW"] = "Dagda - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Rameth - Draconic-WoW"] = "Rameth - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Krista - Draconic-WoW"] = "Krista - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Consecrazy - Draconic-WoW"] = "Consecrazy - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Parthos - Draconic-WoW"] = "Parthos - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Azra - Draconic-WoW"] = "Azra - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Felonme - Draconic-WoW"] = "Felonme - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Vela - Draconic-WoW"] = "Vela - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Hammerme - Draconic-WoW"] = "Hammerme - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Sorn - Draconic-WoW"] = "Sorn - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Penance - Draconic-WoW"] = "Penance - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Holden - Draconic-WoW"] = "Holden - Draconic-WoW",
["Utherd - Draconic-WoW"] = "Utherd - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Hexcuseme - Draconic-WoW"] = "Hexcuseme - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Quiverme - Draconic-WoW"] = "Quiverme - Draconic-WoW",
["Nikaj - Draconic-WoW"] = "Nikaj - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Blocksmith - Draconic-WoW"] = "Blocksmith - Draconic-WoW",
["Sanstus - Draconic-WoW"] = "Sanstus - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Artanis - Draconic-WoW"] = "Artanis - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Orias - Draconic-WoW"] = "Orias - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Zarah - Draconic-WoW"] = "Zarah - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Leyline - Draconic-WoW"] = "Leyline - Draconic-WoW",
["Hemogoblin - Draconic-WoW"] = "Hemogoblin - Draconic-WoW",
["Marvo - Draconic-WoW"] = "Marvo - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Foehawk - Draconic-WoW"] = "Foehawk - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Thirstseal - Draconic-WoW"] = "Thirstseal - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Ikanoa - Draconic-WoW"] = "Ikanoa - Draconic-WoW",
["Derek - Draconic-WoW"] = "Derek - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Alaana - Draconic-WoW"] = "Alaana - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Thiccplates - Draconic-WoW"] = "Thiccplates - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Punchline - Draconic-WoW"] = "Punchline - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Shamwow - Draconic-WoW"] = "Shamwow - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Leonard - Draconic-WoW"] = "Leonard - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Tywin - Draconic-WoW"] = "Tywin - Draconic-WoW",
["Elden - Draconic-WoW"] = "Elden - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Sebastian - Draconic-WoW"] = "Sebastian - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Whirlwinded - Draconic-WoW"] = "Whirlwinded - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Danath - Draconic-WoW"] = "Danath - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Aimme - Draconic-WoW"] = "Aimme - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Eversong - Draconic-WoW"] = "Eversong - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Kuthbert - Draconic-WoW"] = "Kuthbert - Draconic-WoW",
["Austen - Draconic-WoW"] = "Austen - Draconic-WoW",
["Harlem - Draconic-WoW"] = "Harlem - Draconic-WoW",
["Vampstamp - Draconic-WoW"] = "Vampstamp - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Jackson - Draconic-WoW"] = "Jackson - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Silva - Draconic-WoW"] = "Silva - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Makaio - Draconic-WoW"] = "Makaio - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Shanna - Draconic-WoW"] = "Shanna - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Xavik - Draconic-WoW"] = "Xavik - Draconic-WoW",
["Pedaar - Draconic-WoW"] = "Pedaar - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Channa - Draconic-WoW"] = "Channa - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Kalzak - Draconic-WoW"] = "Kalzak - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Oroth - Draconic-WoW"] = "Oroth - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Astraea - Draconic-WoW"] = "Astraea - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Boltaction - Draconic-WoW"] = "Boltaction - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Tonka - Draconic-WoW"] = "Tonka - Draconic-WoW",
["Highcliff - Draconic-WoW"] = "Highcliff - Draconic-WoW",
["Marlon - Draconic-WoW"] = "Marlon - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Yaaru - Draconic-WoW"] = "Yaaru - Draconic-WoW",
["Qwendy - Draconic-WoW"] = "Qwendy - Draconic-WoW",
["Shadowban - Draconic-WoW"] = "Shadowban - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Zaibach - Draconic-WoW"] = "Zaibach - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Sava - Draconic-WoW"] = "Sava - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Smiteme - Draconic-WoW"] = "Smiteme - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Ironsides - Draconic-WoW"] = "Ironsides - Draconic-WoW",
["Harold - Draconic-WoW"] = "Harold - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Hexappeal - Draconic-WoW"] = "Hexappeal - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Judgemental - Draconic-WoW"] = "Judgemental - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Feltide - Draconic-WoW"] = "Feltide - Draconic-WoW",
["Hexandchill - Draconic-WoW"] = "Hexandchill - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Totemtease - Draconic-WoW"] = "Totemtease - Draconic-WoW",
["Dazlith - Draconic-WoW"] = "Dazlith - Draconic-WoW",
["Dermot - Draconic-WoW"] = "Dermot - Draconic-WoW",
["Larixa - Draconic-WoW"] = "Larixa - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Arred - Draconic-WoW"] = "Arred - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Ironward - Draconic-WoW"] = "Ironward - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Harandor - Draconic-WoW"] = "Harandor - Draconic-WoW",
["Rageagainst - Draconic-WoW"] = "Rageagainst - Draconic-WoW",
["Movado - Draconic-WoW"] = "Movado - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Lambert - Draconic-WoW"] = "Lambert - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Rend - Draconic-WoW"] = "Rend - Draconic-WoW",
["Roone - Draconic-WoW"] = "Roone - Draconic-WoW",
["Huk - Draconic-WoW"] = "Huk - Draconic-WoW",
["Lunaris - Draconic-WoW"] = "Lunaris - Draconic-WoW",
["Teo - Draconic-WoW"] = "Teo - Draconic-WoW",
["Zara - Draconic-WoW"] = "Zara - Draconic-WoW",
["Siiri - Draconic-WoW"] = "Siiri - Draconic-WoW",
["Sophia - Draconic-WoW"] = "Sophia - Draconic-WoW",
["Iridian - Draconic-WoW"] = "Iridian - Draconic-WoW",
["Shieldhero - Draconic-WoW"] = "Shieldhero - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Nana - Draconic-WoW"] = "Nana - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Pakkah - Draconic-WoW"] = "Pakkah - Draconic-WoW",
["Hoz - Draconic-WoW"] = "Hoz - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Packwarden - Draconic-WoW"] = "Packwarden - Draconic-WoW",
},
["profiles"] = {
["Whirlwinded - Draconic-WoW"] = {
},
["Hoz - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Aimme - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Parthos - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Kuthbert - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Shavonda - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Nana - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Vela - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Sophia - Draconic-WoW"] = {
},
["Pedaar - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Channa - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Utherd - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Nikaj - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Artanis - Draconic-WoW"] = {
},
["Orias - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Zarah - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sampson - Draconic-WoW"] = {
},
["Marvo - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Highcliff - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Marlon - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Yaaru - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Ava - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Judgemental - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Hexandchill - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Anders - Draconic-WoW"] = {
},
["Mika - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Punchline - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Larixa - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Lambert - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Austen - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Shamwow - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Ironsides - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Huk - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Zara - Draconic-WoW"] = {
},
["Siiri - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Shieldhero - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Iridian - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Theya - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
},
},
}
BetterWardrobe_Mogitdata = nil
BetterWardrobe_Updates = {
["8_4"] = true,
}
BTT = nil

### Account: 25#1

BetterWardrobe_Options = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Default",
["Godfrey  - Draconic-WoW"] = "Default",
["Suva - Draconic-WoW"] = "Default",
["Zagard - Draconic-WoW"] = "Default",
["Shabam - Draconic-WoW"] = "Default",
["Kohrs - Draconic-WoW"] = "Default",
["Krenshaw - Draconic-WoW"] = "Default",
["Seline - Draconic-WoW"] = "Default",
["Thraxxis - Draconic-WoW"] = "Default",
["Osbert - Draconic-WoW"] = "Default",
["Slade - Draconic-WoW"] = "Default",
["Apollo - Draconic-WoW"] = "Default",
["Reid - Draconic-WoW"] = "Default",
["Zorbban - Draconic-WoW"] = "Default",
["Noblesse - Draconic-WoW"] = "Default",
["Keith - Draconic-WoW"] = "Default",
["Hobbes - Draconic-WoW"] = "Default",
["Voxdominus - Draconic-WoW"] = "Default",
["Zagar - Draconic-WoW"] = "Default",
["Raiford - Draconic-WoW"] = "Default",
["Tiene - Draconic-WoW"] = "Default",
["Primp - Draconic-WoW"] = "Default",
["Testtesttest - Draconic-WoW"] = "Default",
["Rocklobster - Draconic-WoW"] = "Default",
["Perenda - Draconic-WoW"] = "Default",
["Laria - Draconic-WoW"] = "Default",
["Devos - Draconic-WoW"] = "Default",
["Korban - Draconic-WoW"] = "Default",
["Karshran - Draconic-WoW"] = "Default",
["Grebbelz - Draconic-WoW"] = "Default",
},
["profiles"] = {
["Default"] = {
["ShowHidden"] = true,
},
},
}
BetterWardrobe_CharacterData = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Phriix - Draconic-WoW",
["Godfrey  - Draconic-WoW"] = "Godfrey  - Draconic-WoW",
["Suva - Draconic-WoW"] = "Suva - Draconic-WoW",
["Zagard - Draconic-WoW"] = "Zagard - Draconic-WoW",
["Shabam - Draconic-WoW"] = "Shabam - Draconic-WoW",
["Kohrs - Draconic-WoW"] = "Kohrs - Draconic-WoW",
["Krenshaw - Draconic-WoW"] = "Krenshaw - Draconic-WoW",
["Seline - Draconic-WoW"] = "Seline - Draconic-WoW",
["Thraxxis - Draconic-WoW"] = "Thraxxis - Draconic-WoW",
["Osbert - Draconic-WoW"] = "Osbert - Draconic-WoW",
["Slade - Draconic-WoW"] = "Slade - Draconic-WoW",
["Apollo - Draconic-WoW"] = "Apollo - Draconic-WoW",
["Reid - Draconic-WoW"] = "Reid - Draconic-WoW",
["Zorbban - Draconic-WoW"] = "Zorbban - Draconic-WoW",
["Noblesse - Draconic-WoW"] = "Noblesse - Draconic-WoW",
["Keith - Draconic-WoW"] = "Keith - Draconic-WoW",
["Hobbes - Draconic-WoW"] = "Hobbes - Draconic-WoW",
["Voxdominus - Draconic-WoW"] = "Voxdominus - Draconic-WoW",
["Zagar - Draconic-WoW"] = "Zagar - Draconic-WoW",
["Raiford - Draconic-WoW"] = "Raiford - Draconic-WoW",
["Tiene - Draconic-WoW"] = "Tiene - Draconic-WoW",
["Primp - Draconic-WoW"] = "Primp - Draconic-WoW",
["Testtesttest - Draconic-WoW"] = "Testtesttest - Draconic-WoW",
["Rocklobster - Draconic-WoW"] = "Rocklobster - Draconic-WoW",
["Perenda - Draconic-WoW"] = "Perenda - Draconic-WoW",
["Laria - Draconic-WoW"] = "Laria - Draconic-WoW",
["Devos - Draconic-WoW"] = "Devos - Draconic-WoW",
["Korban - Draconic-WoW"] = "Korban - Draconic-WoW",
["Karshran - Draconic-WoW"] = "Karshran - Draconic-WoW",
["Grebbelz - Draconic-WoW"] = "Grebbelz - Draconic-WoW",
},
}
BetterWardrobe_SavedSetData = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Phriix - Draconic-WoW",
["Godfrey  - Draconic-WoW"] = "Godfrey  - Draconic-WoW",
["Suva - Draconic-WoW"] = "Suva - Draconic-WoW",
["Zagard - Draconic-WoW"] = "Zagard - Draconic-WoW",
["Shabam - Draconic-WoW"] = "Shabam - Draconic-WoW",
["Kohrs - Draconic-WoW"] = "Kohrs - Draconic-WoW",
["Krenshaw - Draconic-WoW"] = "Krenshaw - Draconic-WoW",
["Seline - Draconic-WoW"] = "Seline - Draconic-WoW",
["Thraxxis - Draconic-WoW"] = "Thraxxis - Draconic-WoW",
["Osbert - Draconic-WoW"] = "Osbert - Draconic-WoW",
["Slade - Draconic-WoW"] = "Slade - Draconic-WoW",
["Apollo - Draconic-WoW"] = "Apollo - Draconic-WoW",
["Reid - Draconic-WoW"] = "Reid - Draconic-WoW",
["Zorbban - Draconic-WoW"] = "Zorbban - Draconic-WoW",
["Noblesse - Draconic-WoW"] = "Noblesse - Draconic-WoW",
["Keith - Draconic-WoW"] = "Keith - Draconic-WoW",
["Hobbes - Draconic-WoW"] = "Hobbes - Draconic-WoW",
["Voxdominus - Draconic-WoW"] = "Voxdominus - Draconic-WoW",
["Zagar - Draconic-WoW"] = "Zagar - Draconic-WoW",
["Raiford - Draconic-WoW"] = "Raiford - Draconic-WoW",
["Tiene - Draconic-WoW"] = "Tiene - Draconic-WoW",
["Primp - Draconic-WoW"] = "Primp - Draconic-WoW",
["Testtesttest - Draconic-WoW"] = "Testtesttest - Draconic-WoW",
["Rocklobster - Draconic-WoW"] = "Rocklobster - Draconic-WoW",
["Perenda - Draconic-WoW"] = "Perenda - Draconic-WoW",
["Laria - Draconic-WoW"] = "Laria - Draconic-WoW",
["Devos - Draconic-WoW"] = "Devos - Draconic-WoW",
["Korban - Draconic-WoW"] = "Korban - Draconic-WoW",
["Karshran - Draconic-WoW"] = "Karshran - Draconic-WoW",
["Grebbelz - Draconic-WoW"] = "Grebbelz - Draconic-WoW",
},
["global"] = {
["sets"] = {
["Phriix - Draconic-WoW"] = {
},
["Suva - Draconic-WoW"] = {
},
["Shabam - Draconic-WoW"] = {
},
["Kohrs - Draconic-WoW"] = {
},
["Seline - Draconic-WoW"] = {
},
["Krenshaw - Draconic-WoW"] = {
},
["Osbert - Draconic-WoW"] = {
},
["Slade - Draconic-WoW"] = {
},
["Hobbes - Draconic-WoW"] = {
},
["Reid - Draconic-WoW"] = {
},
["Apollo - Draconic-WoW"] = {
},
["Noblesse - Draconic-WoW"] = {
},
["Keith - Draconic-WoW"] = {
},
["Zorbban - Draconic-WoW"] = {
},
["Voxdominus - Draconic-WoW"] = {
},
["Zagar - Draconic-WoW"] = {
},
["Raiford - Draconic-WoW"] = {
},
["Tiene - Draconic-WoW"] = {
},
["Primp - Draconic-WoW"] = {
},
["Testtesttest - Draconic-WoW"] = {
},
["Rocklobster - Draconic-WoW"] = {
},
["Perenda - Draconic-WoW"] = {
},
["Laria - Draconic-WoW"] = {
},
["Devos - Draconic-WoW"] = {
},
["Korban - Draconic-WoW"] = {
},
["Karshran - Draconic-WoW"] = {
},
["Grebbelz - Draconic-WoW"] = {
},
},
},
["profiles"] = {
["Noblesse - Draconic-WoW"] = {
},
["Osbert - Draconic-WoW"] = {
},
["Suva - Draconic-WoW"] = {
},
["Voxdominus - Draconic-WoW"] = {
},
["Zagar - Draconic-WoW"] = {
},
["Shabam - Draconic-WoW"] = {
},
["Tiene - Draconic-WoW"] = {
},
["Seline - Draconic-WoW"] = {
},
["Keith - Draconic-WoW"] = {
},
["Zorbban - Draconic-WoW"] = {
},
["Slade - Draconic-WoW"] = {
},
["Krenshaw - Draconic-WoW"] = {
},
["Karshran - Draconic-WoW"] = {
},
["Grebbelz - Draconic-WoW"] = {
},
},
}
BetterWardrobe_SubstituteItemData = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Default",
["Godfrey  - Draconic-WoW"] = "Default",
["Suva - Draconic-WoW"] = "Default",
["Zagard - Draconic-WoW"] = "Default",
["Shabam - Draconic-WoW"] = "Default",
["Kohrs - Draconic-WoW"] = "Default",
["Krenshaw - Draconic-WoW"] = "Default",
["Seline - Draconic-WoW"] = "Default",
["Thraxxis - Draconic-WoW"] = "Default",
["Osbert - Draconic-WoW"] = "Default",
["Slade - Draconic-WoW"] = "Default",
["Apollo - Draconic-WoW"] = "Default",
["Reid - Draconic-WoW"] = "Default",
["Zorbban - Draconic-WoW"] = "Default",
["Noblesse - Draconic-WoW"] = "Default",
["Keith - Draconic-WoW"] = "Default",
["Hobbes - Draconic-WoW"] = "Default",
["Voxdominus - Draconic-WoW"] = "Default",
["Zagar - Draconic-WoW"] = "Default",
["Raiford - Draconic-WoW"] = "Default",
["Tiene - Draconic-WoW"] = "Default",
["Primp - Draconic-WoW"] = "Default",
["Testtesttest - Draconic-WoW"] = "Default",
["Rocklobster - Draconic-WoW"] = "Default",
["Perenda - Draconic-WoW"] = "Default",
["Laria - Draconic-WoW"] = "Default",
["Devos - Draconic-WoW"] = "Default",
["Korban - Draconic-WoW"] = "Default",
["Karshran - Draconic-WoW"] = "Default",
["Grebbelz - Draconic-WoW"] = "Default",
},
["profiles"] = {
["Default"] = {
},
},
}
BetterWardrobe_ListData = {
["favoritesDB"] = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Phriix - Draconic-WoW",
["Godfrey  - Draconic-WoW"] = "Godfrey  - Draconic-WoW",
["Suva - Draconic-WoW"] = "Suva - Draconic-WoW",
["Zagard - Draconic-WoW"] = "Zagard - Draconic-WoW",
["Shabam - Draconic-WoW"] = "Shabam - Draconic-WoW",
["Kohrs - Draconic-WoW"] = "Kohrs - Draconic-WoW",
["Krenshaw - Draconic-WoW"] = "Krenshaw - Draconic-WoW",
["Seline - Draconic-WoW"] = "Seline - Draconic-WoW",
["Thraxxis - Draconic-WoW"] = "Thraxxis - Draconic-WoW",
["Osbert - Draconic-WoW"] = "Osbert - Draconic-WoW",
["Slade - Draconic-WoW"] = "Slade - Draconic-WoW",
["Apollo - Draconic-WoW"] = "Apollo - Draconic-WoW",
["Reid - Draconic-WoW"] = "Reid - Draconic-WoW",
["Zorbban - Draconic-WoW"] = "Zorbban - Draconic-WoW",
["Noblesse - Draconic-WoW"] = "Noblesse - Draconic-WoW",
["Keith - Draconic-WoW"] = "Keith - Draconic-WoW",
["Hobbes - Draconic-WoW"] = "Hobbes - Draconic-WoW",
["Voxdominus - Draconic-WoW"] = "Voxdominus - Draconic-WoW",
["Zagar - Draconic-WoW"] = "Zagar - Draconic-WoW",
["Raiford - Draconic-WoW"] = "Raiford - Draconic-WoW",
["Tiene - Draconic-WoW"] = "Tiene - Draconic-WoW",
["Primp - Draconic-WoW"] = "Primp - Draconic-WoW",
["Testtesttest - Draconic-WoW"] = "Testtesttest - Draconic-WoW",
["Rocklobster - Draconic-WoW"] = "Rocklobster - Draconic-WoW",
["Perenda - Draconic-WoW"] = "Perenda - Draconic-WoW",
["Laria - Draconic-WoW"] = "Laria - Draconic-WoW",
["Devos - Draconic-WoW"] = "Devos - Draconic-WoW",
["Korban - Draconic-WoW"] = "Korban - Draconic-WoW",
["Karshran - Draconic-WoW"] = "Karshran - Draconic-WoW",
["Grebbelz - Draconic-WoW"] = "Grebbelz - Draconic-WoW",
},
["profiles"] = {
["Noblesse - Draconic-WoW"] = {
},
["Osbert - Draconic-WoW"] = {
},
["Suva - Draconic-WoW"] = {
},
["Voxdominus - Draconic-WoW"] = {
},
["Zagar - Draconic-WoW"] = {
},
["Shabam - Draconic-WoW"] = {
},
["Tiene - Draconic-WoW"] = {
},
["Primp - Draconic-WoW"] = {
},
["Seline - Draconic-WoW"] = {
},
["Krenshaw - Draconic-WoW"] = {
},
["Hobbes - Draconic-WoW"] = {
},
["Zorbban - Draconic-WoW"] = {
},
["Slade - Draconic-WoW"] = {
},
["Keith - Draconic-WoW"] = {
},
["Karshran - Draconic-WoW"] = {
},
["Grebbelz - Draconic-WoW"] = {
},
},
},
["collectionListDB"] = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Phriix - Draconic-WoW",
["Godfrey  - Draconic-WoW"] = "Godfrey  - Draconic-WoW",
["Suva - Draconic-WoW"] = "Suva - Draconic-WoW",
["Zagard - Draconic-WoW"] = "Zagard - Draconic-WoW",
["Shabam - Draconic-WoW"] = "Shabam - Draconic-WoW",
["Kohrs - Draconic-WoW"] = "Kohrs - Draconic-WoW",
["Krenshaw - Draconic-WoW"] = "Krenshaw - Draconic-WoW",
["Seline - Draconic-WoW"] = "Seline - Draconic-WoW",
["Thraxxis - Draconic-WoW"] = "Thraxxis - Draconic-WoW",
["Osbert - Draconic-WoW"] = "Osbert - Draconic-WoW",
["Slade - Draconic-WoW"] = "Slade - Draconic-WoW",
["Apollo - Draconic-WoW"] = "Apollo - Draconic-WoW",
["Reid - Draconic-WoW"] = "Reid - Draconic-WoW",
["Zorbban - Draconic-WoW"] = "Zorbban - Draconic-WoW",
["Noblesse - Draconic-WoW"] = "Noblesse - Draconic-WoW",
["Keith - Draconic-WoW"] = "Keith - Draconic-WoW",
["Hobbes - Draconic-WoW"] = "Hobbes - Draconic-WoW",
["Voxdominus - Draconic-WoW"] = "Voxdominus - Draconic-WoW",
["Zagar - Draconic-WoW"] = "Zagar - Draconic-WoW",
["Raiford - Draconic-WoW"] = "Raiford - Draconic-WoW",
["Tiene - Draconic-WoW"] = "Tiene - Draconic-WoW",
["Primp - Draconic-WoW"] = "Primp - Draconic-WoW",
["Testtesttest - Draconic-WoW"] = "Testtesttest - Draconic-WoW",
["Rocklobster - Draconic-WoW"] = "Rocklobster - Draconic-WoW",
["Perenda - Draconic-WoW"] = "Perenda - Draconic-WoW",
["Laria - Draconic-WoW"] = "Laria - Draconic-WoW",
["Devos - Draconic-WoW"] = "Devos - Draconic-WoW",
["Korban - Draconic-WoW"] = "Korban - Draconic-WoW",
["Karshran - Draconic-WoW"] = "Karshran - Draconic-WoW",
["Grebbelz - Draconic-WoW"] = "Grebbelz - Draconic-WoW",
},
["profiles"] = {
["Phriix - Draconic-WoW"] = {
},
["Suva - Draconic-WoW"] = {
},
["Shabam - Draconic-WoW"] = {
},
["Kohrs - Draconic-WoW"] = {
},
["Seline - Draconic-WoW"] = {
},
["Krenshaw - Draconic-WoW"] = {
},
["Osbert - Draconic-WoW"] = {
},
["Slade - Draconic-WoW"] = {
},
["Hobbes - Draconic-WoW"] = {
},
["Reid - Draconic-WoW"] = {
},
["Apollo - Draconic-WoW"] = {
},
["Noblesse - Draconic-WoW"] = {
},
["Keith - Draconic-WoW"] = {
},
["Zorbban - Draconic-WoW"] = {
},
["Voxdominus - Draconic-WoW"] = {
},
["Zagar - Draconic-WoW"] = {
},
["Raiford - Draconic-WoW"] = {
},
["Tiene - Draconic-WoW"] = {
},
["Primp - Draconic-WoW"] = {
},
["Testtesttest - Draconic-WoW"] = {
},
["Rocklobster - Draconic-WoW"] = {
},
["Perenda - Draconic-WoW"] = {
},
["Laria - Draconic-WoW"] = {
},
["Devos - Draconic-WoW"] = {
},
["Korban - Draconic-WoW"] = {
},
["Karshran - Draconic-WoW"] = {
},
["Grebbelz - Draconic-WoW"] = {
},
},
},
["lastUpdte"] = 1,
["OutfitDB"] = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Phriix - Draconic-WoW",
["Godfrey  - Draconic-WoW"] = "Godfrey  - Draconic-WoW",
["Suva - Draconic-WoW"] = "Suva - Draconic-WoW",
["Zagard - Draconic-WoW"] = "Zagard - Draconic-WoW",
["Shabam - Draconic-WoW"] = "Shabam - Draconic-WoW",
["Kohrs - Draconic-WoW"] = "Kohrs - Draconic-WoW",
["Krenshaw - Draconic-WoW"] = "Krenshaw - Draconic-WoW",
["Seline - Draconic-WoW"] = "Seline - Draconic-WoW",
["Thraxxis - Draconic-WoW"] = "Thraxxis - Draconic-WoW",
["Osbert - Draconic-WoW"] = "Osbert - Draconic-WoW",
["Slade - Draconic-WoW"] = "Slade - Draconic-WoW",
["Apollo - Draconic-WoW"] = "Apollo - Draconic-WoW",
["Reid - Draconic-WoW"] = "Reid - Draconic-WoW",
["Zorbban - Draconic-WoW"] = "Zorbban - Draconic-WoW",
["Noblesse - Draconic-WoW"] = "Noblesse - Draconic-WoW",
["Keith - Draconic-WoW"] = "Keith - Draconic-WoW",
["Hobbes - Draconic-WoW"] = "Hobbes - Draconic-WoW",
["Voxdominus - Draconic-WoW"] = "Voxdominus - Draconic-WoW",
["Zagar - Draconic-WoW"] = "Zagar - Draconic-WoW",
["Raiford - Draconic-WoW"] = "Raiford - Draconic-WoW",
["Tiene - Draconic-WoW"] = "Tiene - Draconic-WoW",
["Primp - Draconic-WoW"] = "Primp - Draconic-WoW",
["Testtesttest - Draconic-WoW"] = "Testtesttest - Draconic-WoW",
["Rocklobster - Draconic-WoW"] = "Rocklobster - Draconic-WoW",
["Perenda - Draconic-WoW"] = "Perenda - Draconic-WoW",
["Laria - Draconic-WoW"] = "Laria - Draconic-WoW",
["Devos - Draconic-WoW"] = "Devos - Draconic-WoW",
["Korban - Draconic-WoW"] = "Korban - Draconic-WoW",
["Karshran - Draconic-WoW"] = "Karshran - Draconic-WoW",
["Grebbelz - Draconic-WoW"] = "Grebbelz - Draconic-WoW",
},
},
["HiddenAppearanceDB"] = {
["profileKeys"] = {
["Phriix - Draconic-WoW"] = "Phriix - Draconic-WoW",
["Godfrey  - Draconic-WoW"] = "Godfrey  - Draconic-WoW",
["Suva - Draconic-WoW"] = "Suva - Draconic-WoW",
["Zagard - Draconic-WoW"] = "Zagard - Draconic-WoW",
["Shabam - Draconic-WoW"] = "Shabam - Draconic-WoW",
["Kohrs - Draconic-WoW"] = "Kohrs - Draconic-WoW",
["Krenshaw - Draconic-WoW"] = "Krenshaw - Draconic-WoW",
["Seline - Draconic-WoW"] = "Seline - Draconic-WoW",
["Thraxxis - Draconic-WoW"] = "Thraxxis - Draconic-WoW",
["Osbert - Draconic-WoW"] = "Osbert - Draconic-WoW",
["Slade - Draconic-WoW"] = "Slade - Draconic-WoW",
["Apollo - Draconic-WoW"] = "Apollo - Draconic-WoW",
["Reid - Draconic-WoW"] = "Reid - Draconic-WoW",
["Zorbban - Draconic-WoW"] = "Zorbban - Draconic-WoW",
["Noblesse - Draconic-WoW"] = "Noblesse - Draconic-WoW",
["Keith - Draconic-WoW"] = "Keith - Draconic-WoW",
["Hobbes - Draconic-WoW"] = "Hobbes - Draconic-WoW",
["Voxdominus - Draconic-WoW"] = "Voxdominus - Draconic-WoW",
["Zagar - Draconic-WoW"] = "Zagar - Draconic-WoW",
["Raiford - Draconic-WoW"] = "Raiford - Draconic-WoW",
["Tiene - Draconic-WoW"] = "Tiene - Draconic-WoW",
["Primp - Draconic-WoW"] = "Primp - Draconic-WoW",
["Testtesttest - Draconic-WoW"] = "Testtesttest - Draconic-WoW",
["Rocklobster - Draconic-WoW"] = "Rocklobster - Draconic-WoW",
["Perenda - Draconic-WoW"] = "Perenda - Draconic-WoW",
["Laria - Draconic-WoW"] = "Laria - Draconic-WoW",
["Devos - Draconic-WoW"] = "Devos - Draconic-WoW",
["Korban - Draconic-WoW"] = "Korban - Draconic-WoW",
["Karshran - Draconic-WoW"] = "Karshran - Draconic-WoW",
["Grebbelz - Draconic-WoW"] = "Grebbelz - Draconic-WoW",
},
["profiles"] = {
["Noblesse - Draconic-WoW"] = {
},
["Osbert - Draconic-WoW"] = {
},
["Suva - Draconic-WoW"] = {
},
["Voxdominus - Draconic-WoW"] = {
},
["Zagar - Draconic-WoW"] = {
},
["Shabam - Draconic-WoW"] = {
},
["Tiene - Draconic-WoW"] = {
},
["Primp - Draconic-WoW"] = {
},
["Seline - Draconic-WoW"] = {
},
["Krenshaw - Draconic-WoW"] = {
},
["Hobbes - Draconic-WoW"] = {
},
["Zorbban - Draconic-WoW"] = {
},
["Slade - Draconic-WoW"] = {
},
["Keith - Draconic-WoW"] = {
},
["Karshran - Draconic-WoW"] = {
},
["Grebbelz - Draconic-WoW"] = {
},
},
},
}
BetterWardrobe_Mogitdata = nil
BetterWardrobe_Updates = {
["8_4"] = true,
}
BTT = nil

### Account: 29#1

BetterWardrobe_Options = {
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Default",
["Coggle - Draconic-WoW"] = "Default",
["Stableslot - Draconic-WoW"] = "Default",
["Moremojo - Draconic-WoW"] = "Default",
["Mega - Draconic-WoW"] = "Default",
["Daamis - Draconic-WoW"] = "Default",
["Brax - Draconic-WoW"] = "Default",
["Reese - Draconic-WoW"] = "Default",
["Quincy - Draconic-WoW"] = "Default",
["Sica - Draconic-WoW"] = "Default",
["Nando - Draconic-WoW"] = "Default",
["Azert - Draconic-WoW"] = "Default",
["Robb - Draconic-WoW"] = "Default",
["Anega - Draconic-WoW"] = "Default",
["Korban - Draconic"] = "Default",
["Ballistics - Draconic-WoW"] = "Default",
["Griffith - Draconic-WoW"] = "Default",
["Kashel - Draconic-WoW"] = "Default",
["Frag - Draconic-WoW"] = "Default",
["Banks - Draconic-WoW"] = "Default",
["Mav - Draconic-WoW"] = "Default",
["Justicaris - Draconic-WoW"] = "Default",
["Carlo - Draconic-WoW"] = "Default",
["Xenos - Draconic-WoW"] = "Default",
["Celina - Draconic-WoW"] = "Default",
["Melrose - Draconic-WoW"] = "Default",
["Regis - Draconic-WoW"] = "Default",
["Benny - Draconic-WoW"] = "Default",
["Primarch - Draconic-WoW"] = "Default",
["Meltface - Draconic-WoW"] = "Default",
["Shavonda - Draconic-WoW"] = "Default",
["Ashford - Draconic-WoW"] = "Default",
["Kurtak - Draconic-WoW"] = "Default",
["Hoof - Draconic-WoW"] = "Default",
["Shapow - Draconic-WoW"] = "Default",
["Starweaver - Draconic-WoW"] = "Default",
["Erett - Draconic-WoW"] = "Default",
["Zhad - Draconic-WoW"] = "Default",
["Testtest - Draconic-WoW"] = "Default",
["Endra - Draconic-WoW"] = "Default",
["Alice - Draconic-WoW"] = "Default",
["Golo - Draconic-WoW"] = "Default",
["Shale - Draconic-WoW"] = "Default",
["Khazel - Draconic-WoW"] = "Default",
["Phea - Draconic-WoW"] = "Default",
["Kefka - Draconic-WoW"] = "Default",
["Pakmojo - Draconic-WoW"] = "Default",
["Edwards - Draconic-WoW"] = "Default",
["Deez - Draconic-WoW"] = "Default",
["Cyric - Draconic-WoW"] = "Default",
["Lisbeth - Draconic-WoW"] = "Default",
["Earthevo - Draconic-WoW"] = "Default",
["Talairn - Draconic-WoW"] = "Default",
["Vulkan - Draconic-WoW"] = "Default",
["Kelmenvor - Draconic-WoW"] = "Default",
["Astaron - Draconic-WoW"] = "Default",
["Reynolds - Draconic-WoW"] = "Default",
["Van - Draconic-WoW"] = "Default",
["Invaris - Draconic-WoW"] = "Default",
["Ralzin - Draconic-WoW"] = "Default",
["Zital - Draconic-WoW"] = "Default",
["Zenat - Draconic-WoW"] = "Default",
["Leyla - Draconic-WoW"] = "Default",
["Piuy - Draconic-WoW"] = "Default",
["Zhago - Draconic-WoW"] = "Default",
["Morvane - Draconic-WoW"] = "Default",
["Korla - Draconic-WoW"] = "Default",
["Adnap - Draconic-WoW"] = "Default",
["Argyle - Draconic-WoW"] = "Default",
["Gantz - Draconic-WoW"] = "Default",
["Draxtwo - Draconic-WoW"] = "Default",
["Oomah - Draconic-WoW"] = "Default",
["Esi - Draconic-WoW"] = "Default",
["Raynaud - Draconic-WoW"] = "Default",
["Dix - Draconic-WoW"] = "Default",
["Perapera - Draconic-WoW"] = "Default",
["Magna - Draconic-WoW"] = "Default",
["Satren - Draconic-WoW"] = "Default",
["Umbralight - Draconic-WoW"] = "Default",
["Tav - Draconic-WoW"] = "Default",
["Kora - Draconic-WoW"] = "Default",
["Nolan - Draconic-WoW"] = "Default",
["Lolth - Draconic-WoW"] = "Default",
["Tavish - Draconic-WoW"] = "Default",
["Momonga - Draconic-WoW"] = "Default",
["Stonebreaker - Draconic-WoW"] = "Default",
["Kardol - Draconic-WoW"] = "Default",
["Theya - Draconic-WoW"] = "Default",
["Ren - Draconic-WoW"] = "Default",
["Ava - Draconic-WoW"] = "Default",
["Cedrick - Draconic-WoW"] = "Default",
["Eve - Draconic-WoW"] = "Default",
["Vaedan - Draconic-WoW"] = "Default",
["Korik - Draconic-WoW"] = "Default",
["Parah - Draconic-WoW"] = "Default",
["Dreya - Draconic-WoW"] = "Default",
["Crackhammer - Draconic-WoW"] = "Default",
["Gunnar - Draconic-WoW"] = "Default",
["Vandrus - Draconic-WoW"] = "Default",
["Grayson - Draconic-WoW"] = "Default",
["Valanese - Draconic-WoW"] = "Default",
["Theodore - Draconic-WoW"] = "Default",
["Hitcap - Draconic-WoW"] = "Default",
["Ruugar - Draconic-WoW"] = "Default",
["Kalano - Draconic-WoW"] = "Default",
["Auria - Draconic-WoW"] = "Default",
["Roland - Draconic-WoW"] = "Default",
["Lars - Draconic-WoW"] = "Default",
["Solanna - Draconic-WoW"] = "Default",
["Halztraz - Draconic-WoW"] = "Default",
["Tristian - Draconic-WoW"] = "Default",
["Sarsam - Draconic-WoW"] = "Default",
["Kodetha - Draconic-WoW"] = "Default",
["Davin - Draconic-WoW"] = "Default",
["Sebas - Draconic-WoW"] = "Default",
["Meatstick - Draconic-WoW"] = "Default",
["Voxghar - Draconic-WoW"] = "Default",
["Payton - Draconic-WoW"] = "Default",
["Rahddon - Draconic-WoW"] = "Default",
["Zezima - Draconic-WoW"] = "Default",
["Laaj - Draconic-WoW"] = "Default",
["Sampson - Draconic-WoW"] = "Default",
["Lia - Draconic-WoW"] = "Default",
["Graham - Draconic-WoW"] = "Default",
["Grammon - Draconic-WoW"] = "Default",
["Warren - Draconic-WoW"] = "Default",
["Thornhand - Draconic-WoW"] = "Default",
["Hatcher - Draconic-WoW"] = "Default",
["Kazil - Draconic-WoW"] = "Default",
["Davos - Draconic-WoW"] = "Default",
["Crakash - Draconic-WoW"] = "Default",
["Tredwell - Draconic-WoW"] = "Default",
["Mojoe - Draconic-WoW"] = "Default",
["Xathos - Draconic-WoW"] = "Default",
["Magnus - Draconic-WoW"] = "Default",
["Celestra - Draconic-WoW"] = "Default",
["Ada - Draconic-WoW"] = "Default",
["Koby - Draconic-WoW"] = "Default",
["Baku - Draconic-WoW"] = "Default",
["Cecil - Draconic-WoW"] = "Default",
["Mogh - Draconic-WoW"] = "Default",
["Padrik - Draconic-WoW"] = "Default",
["Havik - Draconic-WoW"] = "Default",
["Sicalicious - Draconic-WoW"] = "Default",
["Nelson - Draconic-WoW"] = "Default",
["Boris - Draconic-WoW"] = "Default",
["Wangz - Draconic-WoW"] = "Default",
["Danvers - Draconic-WoW"] = "Default",
["Elaria - Draconic-WoW"] = "Default",
["Tylosh - Draconic-WoW"] = "Default",
["Nolen - Draconic-WoW"] = "Default",
["Oren - Draconic-WoW"] = "Default",
["Adepta - Draconic-WoW"] = "Default",
["Enoch - Draconic-WoW"] = "Default",
["Kaitlan - Draconic-WoW"] = "Default",
["Volkaris - Draconic-WoW"] = "Default",
["Yancy - Draconic-WoW"] = "Default",
["Atrissa - Draconic-WoW"] = "Default",
["Jobe - Draconic-WoW"] = "Default",
["Red - Draconic-WoW"] = "Default",
["Bishop - Draconic-WoW"] = "Default",
["Sic - Draconic-WoW"] = "Default",
["Moroes - Draconic-WoW"] = "Default",
["Mercer - Draconic-WoW"] = "Default",
["Alexius - Draconic-WoW"] = "Default",
["Anders - Draconic-WoW"] = "Default",
["Prak - Draconic-WoW"] = "Default",
["Levara - Draconic-WoW"] = "Default",
},
["profiles"] = {
["Default"] = {
["ShowHidden"] = true,
["CurrentFactionSets"] = false,
["ShowItemIDTooltips"] = true,
},
},
}
BetterWardrobe_CharacterData = {
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Korban - Draconic"] = "Korban - Draconic",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
},
}
BetterWardrobe_SavedSetData = {
["global"] = {
["sets"] = {
["Mika - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Quincy - Draconic-WoW"] = {
},
["Sica - Draconic-WoW"] = {
},
["Nando - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Korban - Draconic"] = {
},
["Ballistics - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Carlo - Draconic-WoW"] = {
},
["Xenos - Draconic-WoW"] = {
},
["Celina - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Meltface - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Red - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Erett - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Shale - Draconic-WoW"] = {
},
["Khazel - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Kefka - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Cyric - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Enoch - Draconic-WoW"] = {
},
["Zhago - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sampson - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Oomah - Draconic-WoW"] = {
},
["Raynaud - Draconic-WoW"] = {
},
["Dix - Draconic-WoW"] = {
},
["Perapera - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Satren - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Cedrick - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Vaedan - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Parah - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Hitcap - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Auria - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Lars - Draconic-WoW"] = {
},
["Halztraz - Draconic-WoW"] = {
},
["Koby - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Sarsam - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Payton - Draconic-WoW"] = {
},
["Theodore - Draconic-WoW"] = {
},
["Theya - Draconic-WoW"] = {
},
["Ren - Draconic-WoW"] = {
},
["Kelmenvor - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Gunnar - Draconic-WoW"] = {
},
["Crakash - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Mojoe - Draconic-WoW"] = {
},
["Voxghar - Draconic-WoW"] = {
},
["Yancy - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Mogh - Draconic-WoW"] = {
},
["Padrik - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Thornhand - Draconic-WoW"] = {
},
["Wangz - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Hoof - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
{
["outfitID"] = 0,
["sources"] = {
190154,
0,
190152,
0,
190148,
190150,
190156,
190153,
190157,
190155,
0,
0,
0,
0,
0,
116336,
116336,
0,
0,
},
["name"] = "Purple",
["icon"] = 2444253,
["index"] = 1,
},
{
["outfitID"] = 1,
["sources"] = {
190154,
0,
190152,
0,
190148,
190150,
190156,
190153,
190157,
190155,
0,
0,
0,
0,
0,
116336,
116336,
0,
0,
},
["name"] = "White",
["icon"] = 2444253,
["index"] = 2,
},
},
["Mav - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Volkaris - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Moroes - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Argyle - Draconic-WoW"] = {
},
["Anders - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
},
},
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Korban - Draconic"] = "Korban - Draconic",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
},
["profiles"] = {
["Mika - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Korban - Draconic"] = {
},
},
}
BetterWardrobe_SubstituteItemData = {
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Default",
["Coggle - Draconic-WoW"] = "Default",
["Stableslot - Draconic-WoW"] = "Default",
["Moremojo - Draconic-WoW"] = "Default",
["Mega - Draconic-WoW"] = "Default",
["Daamis - Draconic-WoW"] = "Default",
["Brax - Draconic-WoW"] = "Default",
["Reese - Draconic-WoW"] = "Default",
["Quincy - Draconic-WoW"] = "Default",
["Sica - Draconic-WoW"] = "Default",
["Nando - Draconic-WoW"] = "Default",
["Azert - Draconic-WoW"] = "Default",
["Robb - Draconic-WoW"] = "Default",
["Anega - Draconic-WoW"] = "Default",
["Korban - Draconic"] = "Default",
["Ballistics - Draconic-WoW"] = "Default",
["Griffith - Draconic-WoW"] = "Default",
["Kashel - Draconic-WoW"] = "Default",
["Frag - Draconic-WoW"] = "Default",
["Banks - Draconic-WoW"] = "Default",
["Mav - Draconic-WoW"] = "Default",
["Justicaris - Draconic-WoW"] = "Default",
["Carlo - Draconic-WoW"] = "Default",
["Xenos - Draconic-WoW"] = "Default",
["Celina - Draconic-WoW"] = "Default",
["Melrose - Draconic-WoW"] = "Default",
["Regis - Draconic-WoW"] = "Default",
["Benny - Draconic-WoW"] = "Default",
["Primarch - Draconic-WoW"] = "Default",
["Meltface - Draconic-WoW"] = "Default",
["Shavonda - Draconic-WoW"] = "Default",
["Ashford - Draconic-WoW"] = "Default",
["Kurtak - Draconic-WoW"] = "Default",
["Hoof - Draconic-WoW"] = "Default",
["Shapow - Draconic-WoW"] = "Default",
["Starweaver - Draconic-WoW"] = "Default",
["Erett - Draconic-WoW"] = "Default",
["Zhad - Draconic-WoW"] = "Default",
["Testtest - Draconic-WoW"] = "Default",
["Endra - Draconic-WoW"] = "Default",
["Alice - Draconic-WoW"] = "Default",
["Golo - Draconic-WoW"] = "Default",
["Shale - Draconic-WoW"] = "Default",
["Khazel - Draconic-WoW"] = "Default",
["Phea - Draconic-WoW"] = "Default",
["Kefka - Draconic-WoW"] = "Default",
["Pakmojo - Draconic-WoW"] = "Default",
["Edwards - Draconic-WoW"] = "Default",
["Deez - Draconic-WoW"] = "Default",
["Cyric - Draconic-WoW"] = "Default",
["Lisbeth - Draconic-WoW"] = "Default",
["Earthevo - Draconic-WoW"] = "Default",
["Talairn - Draconic-WoW"] = "Default",
["Vulkan - Draconic-WoW"] = "Default",
["Kelmenvor - Draconic-WoW"] = "Default",
["Astaron - Draconic-WoW"] = "Default",
["Reynolds - Draconic-WoW"] = "Default",
["Van - Draconic-WoW"] = "Default",
["Invaris - Draconic-WoW"] = "Default",
["Ralzin - Draconic-WoW"] = "Default",
["Zital - Draconic-WoW"] = "Default",
["Zenat - Draconic-WoW"] = "Default",
["Leyla - Draconic-WoW"] = "Default",
["Piuy - Draconic-WoW"] = "Default",
["Zhago - Draconic-WoW"] = "Default",
["Morvane - Draconic-WoW"] = "Default",
["Korla - Draconic-WoW"] = "Default",
["Adnap - Draconic-WoW"] = "Default",
["Argyle - Draconic-WoW"] = "Default",
["Gantz - Draconic-WoW"] = "Default",
["Draxtwo - Draconic-WoW"] = "Default",
["Oomah - Draconic-WoW"] = "Default",
["Esi - Draconic-WoW"] = "Default",
["Raynaud - Draconic-WoW"] = "Default",
["Dix - Draconic-WoW"] = "Default",
["Perapera - Draconic-WoW"] = "Default",
["Magna - Draconic-WoW"] = "Default",
["Satren - Draconic-WoW"] = "Default",
["Umbralight - Draconic-WoW"] = "Default",
["Tav - Draconic-WoW"] = "Default",
["Kora - Draconic-WoW"] = "Default",
["Nolan - Draconic-WoW"] = "Default",
["Lolth - Draconic-WoW"] = "Default",
["Tavish - Draconic-WoW"] = "Default",
["Momonga - Draconic-WoW"] = "Default",
["Stonebreaker - Draconic-WoW"] = "Default",
["Kardol - Draconic-WoW"] = "Default",
["Theya - Draconic-WoW"] = "Default",
["Ren - Draconic-WoW"] = "Default",
["Ava - Draconic-WoW"] = "Default",
["Cedrick - Draconic-WoW"] = "Default",
["Eve - Draconic-WoW"] = "Default",
["Vaedan - Draconic-WoW"] = "Default",
["Korik - Draconic-WoW"] = "Default",
["Parah - Draconic-WoW"] = "Default",
["Dreya - Draconic-WoW"] = "Default",
["Crackhammer - Draconic-WoW"] = "Default",
["Gunnar - Draconic-WoW"] = "Default",
["Vandrus - Draconic-WoW"] = "Default",
["Grayson - Draconic-WoW"] = "Default",
["Valanese - Draconic-WoW"] = "Default",
["Theodore - Draconic-WoW"] = "Default",
["Hitcap - Draconic-WoW"] = "Default",
["Ruugar - Draconic-WoW"] = "Default",
["Kalano - Draconic-WoW"] = "Default",
["Auria - Draconic-WoW"] = "Default",
["Roland - Draconic-WoW"] = "Default",
["Lars - Draconic-WoW"] = "Default",
["Solanna - Draconic-WoW"] = "Default",
["Halztraz - Draconic-WoW"] = "Default",
["Tristian - Draconic-WoW"] = "Default",
["Sarsam - Draconic-WoW"] = "Default",
["Kodetha - Draconic-WoW"] = "Default",
["Davin - Draconic-WoW"] = "Default",
["Sebas - Draconic-WoW"] = "Default",
["Meatstick - Draconic-WoW"] = "Default",
["Voxghar - Draconic-WoW"] = "Default",
["Payton - Draconic-WoW"] = "Default",
["Rahddon - Draconic-WoW"] = "Default",
["Zezima - Draconic-WoW"] = "Default",
["Laaj - Draconic-WoW"] = "Default",
["Sampson - Draconic-WoW"] = "Default",
["Lia - Draconic-WoW"] = "Default",
["Graham - Draconic-WoW"] = "Default",
["Grammon - Draconic-WoW"] = "Default",
["Warren - Draconic-WoW"] = "Default",
["Thornhand - Draconic-WoW"] = "Default",
["Hatcher - Draconic-WoW"] = "Default",
["Kazil - Draconic-WoW"] = "Default",
["Davos - Draconic-WoW"] = "Default",
["Crakash - Draconic-WoW"] = "Default",
["Tredwell - Draconic-WoW"] = "Default",
["Mojoe - Draconic-WoW"] = "Default",
["Xathos - Draconic-WoW"] = "Default",
["Magnus - Draconic-WoW"] = "Default",
["Celestra - Draconic-WoW"] = "Default",
["Ada - Draconic-WoW"] = "Default",
["Koby - Draconic-WoW"] = "Default",
["Baku - Draconic-WoW"] = "Default",
["Cecil - Draconic-WoW"] = "Default",
["Mogh - Draconic-WoW"] = "Default",
["Padrik - Draconic-WoW"] = "Default",
["Havik - Draconic-WoW"] = "Default",
["Sicalicious - Draconic-WoW"] = "Default",
["Nelson - Draconic-WoW"] = "Default",
["Boris - Draconic-WoW"] = "Default",
["Wangz - Draconic-WoW"] = "Default",
["Danvers - Draconic-WoW"] = "Default",
["Elaria - Draconic-WoW"] = "Default",
["Tylosh - Draconic-WoW"] = "Default",
["Nolen - Draconic-WoW"] = "Default",
["Oren - Draconic-WoW"] = "Default",
["Adepta - Draconic-WoW"] = "Default",
["Enoch - Draconic-WoW"] = "Default",
["Kaitlan - Draconic-WoW"] = "Default",
["Volkaris - Draconic-WoW"] = "Default",
["Yancy - Draconic-WoW"] = "Default",
["Atrissa - Draconic-WoW"] = "Default",
["Jobe - Draconic-WoW"] = "Default",
["Red - Draconic-WoW"] = "Default",
["Bishop - Draconic-WoW"] = "Default",
["Sic - Draconic-WoW"] = "Default",
["Moroes - Draconic-WoW"] = "Default",
["Mercer - Draconic-WoW"] = "Default",
["Alexius - Draconic-WoW"] = "Default",
["Anders - Draconic-WoW"] = "Default",
["Prak - Draconic-WoW"] = "Default",
["Levara - Draconic-WoW"] = "Default",
},
["profiles"] = {
["Default"] = {
},
},
}
BetterWardrobe_ListData = {
["favoritesDB"] = {
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Korban - Draconic"] = "Korban - Draconic",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
},
["profiles"] = {
["Mika - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Ava - Draconic-WoW"] = {
},
["Shavonda - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Korban - Draconic"] = {
},
},
},
["collectionListDB"] = {
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Korban - Draconic"] = "Korban - Draconic",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
},
["profiles"] = {
["Mika - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Quincy - Draconic-WoW"] = {
},
["Sica - Draconic-WoW"] = {
},
["Nando - Draconic-WoW"] = {
},
["Azert - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Korban - Draconic"] = {
},
["Ballistics - Draconic-WoW"] = {
},
["Griffith - Draconic-WoW"] = {
},
["Kashel - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Carlo - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Celina - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Meltface - Draconic-WoW"] = {
},
["Shavonda - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Kurtak - Draconic-WoW"] = {
},
["Hoof - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Erett - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Testtest - Draconic-WoW"] = {
},
["Endra - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Shale - Draconic-WoW"] = {
},
["Khazel - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Kefka - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Cyric - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Earthevo - Draconic-WoW"] = {
},
["Talairn - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Thornhand - Draconic-WoW"] = {
},
["Ralzin - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Zenat - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Enoch - Draconic-WoW"] = {
},
["Zhago - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sampson - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Oomah - Draconic-WoW"] = {
},
["Esi - Draconic-WoW"] = {
},
["Raynaud - Draconic-WoW"] = {
},
["Dix - Draconic-WoW"] = {
},
["Perapera - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Satren - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Anders - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Theya - Draconic-WoW"] = {
},
["Ren - Draconic-WoW"] = {
},
["Ava - Draconic-WoW"] = {
},
["Cedrick - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Vaedan - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Parah - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Gunnar - Draconic-WoW"] = {
},
["Sarsam - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Hitcap - Draconic-WoW"] = {
},
["Piuy - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Auria - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Lars - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Halztraz - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Argyle - Draconic-WoW"] = {
},
["Kodetha - Draconic-WoW"] = {
},
["Davin - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Voxghar - Draconic-WoW"] = {
},
["Payton - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Zezima - Draconic-WoW"] = {
},
["Laaj - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Theodore - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Koby - Draconic-WoW"] = {
},
["Davos - Draconic-WoW"] = {
},
["Crakash - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Mojoe - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Xenos - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Kelmenvor - Draconic-WoW"] = {
},
["Mogh - Draconic-WoW"] = {
},
["Padrik - Draconic-WoW"] = {
},
["Yancy - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Wangz - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Tylosh - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Volkaris - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Red - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
["lists"] = {
{
["item"] = {
[23975] = true,
[23976] = true,
[97173] = true,
[23977] = true,
[97177] = true,
[97179] = true,
[97181] = true,
[23979] = true,
[37858] = true,
[37822] = true,
[37823] = true,
[23981] = true,
[37825] = true,
[23982] = true,
[37827] = true,
[37828] = true,
[37829] = true,
[37826] = true,
[37824] = true,
[97176] = true,
[97171] = true,
[23980] = true,
[23978] = true,
[97184] = true,
[11168] = true,
},
["set"] = {
[4133] = {
[97177] = true,
[97181] = true,
[11168] = true,
[97184] = true,
[97179] = true,
[97176] = true,
[97173] = true,
[97171] = true,
},
[1663] = {
[37829] = true,
[37822] = true,
[37823] = true,
[37824] = true,
[37825] = true,
[37826] = true,
[37827] = true,
[37828] = true,
[37858] = true,
},
[71] = {
[23982] = true,
[23976] = true,
[23977] = true,
[23978] = true,
[23979] = true,
[23980] = true,
[23981] = true,
[23975] = true,
},
},
},
},
},
["Moroes - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Boris - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
},
},
["lastUpdte"] = 1,
["OutfitDB"] = {
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Korban - Draconic"] = "Korban - Draconic",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
},
},
["HiddenAppearanceDB"] = {
["profileKeys"] = {
["Mika - Draconic-WoW"] = "Mika - Draconic-WoW",
["Coggle - Draconic-WoW"] = "Coggle - Draconic-WoW",
["Stableslot - Draconic-WoW"] = "Stableslot - Draconic-WoW",
["Moremojo - Draconic-WoW"] = "Moremojo - Draconic-WoW",
["Mega - Draconic-WoW"] = "Mega - Draconic-WoW",
["Daamis - Draconic-WoW"] = "Daamis - Draconic-WoW",
["Brax - Draconic-WoW"] = "Brax - Draconic-WoW",
["Reese - Draconic-WoW"] = "Reese - Draconic-WoW",
["Quincy - Draconic-WoW"] = "Quincy - Draconic-WoW",
["Sica - Draconic-WoW"] = "Sica - Draconic-WoW",
["Nando - Draconic-WoW"] = "Nando - Draconic-WoW",
["Azert - Draconic-WoW"] = "Azert - Draconic-WoW",
["Robb - Draconic-WoW"] = "Robb - Draconic-WoW",
["Anega - Draconic-WoW"] = "Anega - Draconic-WoW",
["Korban - Draconic"] = "Korban - Draconic",
["Ballistics - Draconic-WoW"] = "Ballistics - Draconic-WoW",
["Griffith - Draconic-WoW"] = "Griffith - Draconic-WoW",
["Kashel - Draconic-WoW"] = "Kashel - Draconic-WoW",
["Frag - Draconic-WoW"] = "Frag - Draconic-WoW",
["Banks - Draconic-WoW"] = "Banks - Draconic-WoW",
["Mav - Draconic-WoW"] = "Mav - Draconic-WoW",
["Justicaris - Draconic-WoW"] = "Justicaris - Draconic-WoW",
["Carlo - Draconic-WoW"] = "Carlo - Draconic-WoW",
["Xenos - Draconic-WoW"] = "Xenos - Draconic-WoW",
["Celina - Draconic-WoW"] = "Celina - Draconic-WoW",
["Melrose - Draconic-WoW"] = "Melrose - Draconic-WoW",
["Regis - Draconic-WoW"] = "Regis - Draconic-WoW",
["Benny - Draconic-WoW"] = "Benny - Draconic-WoW",
["Primarch - Draconic-WoW"] = "Primarch - Draconic-WoW",
["Meltface - Draconic-WoW"] = "Meltface - Draconic-WoW",
["Shavonda - Draconic-WoW"] = "Shavonda - Draconic-WoW",
["Ashford - Draconic-WoW"] = "Ashford - Draconic-WoW",
["Kurtak - Draconic-WoW"] = "Kurtak - Draconic-WoW",
["Hoof - Draconic-WoW"] = "Hoof - Draconic-WoW",
["Shapow - Draconic-WoW"] = "Shapow - Draconic-WoW",
["Starweaver - Draconic-WoW"] = "Starweaver - Draconic-WoW",
["Erett - Draconic-WoW"] = "Erett - Draconic-WoW",
["Zhad - Draconic-WoW"] = "Zhad - Draconic-WoW",
["Testtest - Draconic-WoW"] = "Testtest - Draconic-WoW",
["Endra - Draconic-WoW"] = "Endra - Draconic-WoW",
["Alice - Draconic-WoW"] = "Alice - Draconic-WoW",
["Golo - Draconic-WoW"] = "Golo - Draconic-WoW",
["Shale - Draconic-WoW"] = "Shale - Draconic-WoW",
["Khazel - Draconic-WoW"] = "Khazel - Draconic-WoW",
["Phea - Draconic-WoW"] = "Phea - Draconic-WoW",
["Kefka - Draconic-WoW"] = "Kefka - Draconic-WoW",
["Pakmojo - Draconic-WoW"] = "Pakmojo - Draconic-WoW",
["Edwards - Draconic-WoW"] = "Edwards - Draconic-WoW",
["Deez - Draconic-WoW"] = "Deez - Draconic-WoW",
["Cyric - Draconic-WoW"] = "Cyric - Draconic-WoW",
["Lisbeth - Draconic-WoW"] = "Lisbeth - Draconic-WoW",
["Earthevo - Draconic-WoW"] = "Earthevo - Draconic-WoW",
["Talairn - Draconic-WoW"] = "Talairn - Draconic-WoW",
["Vulkan - Draconic-WoW"] = "Vulkan - Draconic-WoW",
["Kelmenvor - Draconic-WoW"] = "Kelmenvor - Draconic-WoW",
["Astaron - Draconic-WoW"] = "Astaron - Draconic-WoW",
["Reynolds - Draconic-WoW"] = "Reynolds - Draconic-WoW",
["Van - Draconic-WoW"] = "Van - Draconic-WoW",
["Invaris - Draconic-WoW"] = "Invaris - Draconic-WoW",
["Ralzin - Draconic-WoW"] = "Ralzin - Draconic-WoW",
["Zital - Draconic-WoW"] = "Zital - Draconic-WoW",
["Zenat - Draconic-WoW"] = "Zenat - Draconic-WoW",
["Leyla - Draconic-WoW"] = "Leyla - Draconic-WoW",
["Piuy - Draconic-WoW"] = "Piuy - Draconic-WoW",
["Zhago - Draconic-WoW"] = "Zhago - Draconic-WoW",
["Morvane - Draconic-WoW"] = "Morvane - Draconic-WoW",
["Korla - Draconic-WoW"] = "Korla - Draconic-WoW",
["Adnap - Draconic-WoW"] = "Adnap - Draconic-WoW",
["Argyle - Draconic-WoW"] = "Argyle - Draconic-WoW",
["Gantz - Draconic-WoW"] = "Gantz - Draconic-WoW",
["Draxtwo - Draconic-WoW"] = "Draxtwo - Draconic-WoW",
["Oomah - Draconic-WoW"] = "Oomah - Draconic-WoW",
["Esi - Draconic-WoW"] = "Esi - Draconic-WoW",
["Raynaud - Draconic-WoW"] = "Raynaud - Draconic-WoW",
["Dix - Draconic-WoW"] = "Dix - Draconic-WoW",
["Perapera - Draconic-WoW"] = "Perapera - Draconic-WoW",
["Magna - Draconic-WoW"] = "Magna - Draconic-WoW",
["Satren - Draconic-WoW"] = "Satren - Draconic-WoW",
["Umbralight - Draconic-WoW"] = "Umbralight - Draconic-WoW",
["Tav - Draconic-WoW"] = "Tav - Draconic-WoW",
["Kora - Draconic-WoW"] = "Kora - Draconic-WoW",
["Nolan - Draconic-WoW"] = "Nolan - Draconic-WoW",
["Lolth - Draconic-WoW"] = "Lolth - Draconic-WoW",
["Tavish - Draconic-WoW"] = "Tavish - Draconic-WoW",
["Momonga - Draconic-WoW"] = "Momonga - Draconic-WoW",
["Stonebreaker - Draconic-WoW"] = "Stonebreaker - Draconic-WoW",
["Kardol - Draconic-WoW"] = "Kardol - Draconic-WoW",
["Theya - Draconic-WoW"] = "Theya - Draconic-WoW",
["Ren - Draconic-WoW"] = "Ren - Draconic-WoW",
["Ava - Draconic-WoW"] = "Ava - Draconic-WoW",
["Cedrick - Draconic-WoW"] = "Cedrick - Draconic-WoW",
["Eve - Draconic-WoW"] = "Eve - Draconic-WoW",
["Vaedan - Draconic-WoW"] = "Vaedan - Draconic-WoW",
["Korik - Draconic-WoW"] = "Korik - Draconic-WoW",
["Parah - Draconic-WoW"] = "Parah - Draconic-WoW",
["Dreya - Draconic-WoW"] = "Dreya - Draconic-WoW",
["Crackhammer - Draconic-WoW"] = "Crackhammer - Draconic-WoW",
["Gunnar - Draconic-WoW"] = "Gunnar - Draconic-WoW",
["Vandrus - Draconic-WoW"] = "Vandrus - Draconic-WoW",
["Grayson - Draconic-WoW"] = "Grayson - Draconic-WoW",
["Valanese - Draconic-WoW"] = "Valanese - Draconic-WoW",
["Theodore - Draconic-WoW"] = "Theodore - Draconic-WoW",
["Hitcap - Draconic-WoW"] = "Hitcap - Draconic-WoW",
["Ruugar - Draconic-WoW"] = "Ruugar - Draconic-WoW",
["Kalano - Draconic-WoW"] = "Kalano - Draconic-WoW",
["Auria - Draconic-WoW"] = "Auria - Draconic-WoW",
["Roland - Draconic-WoW"] = "Roland - Draconic-WoW",
["Lars - Draconic-WoW"] = "Lars - Draconic-WoW",
["Solanna - Draconic-WoW"] = "Solanna - Draconic-WoW",
["Halztraz - Draconic-WoW"] = "Halztraz - Draconic-WoW",
["Tristian - Draconic-WoW"] = "Tristian - Draconic-WoW",
["Sarsam - Draconic-WoW"] = "Sarsam - Draconic-WoW",
["Kodetha - Draconic-WoW"] = "Kodetha - Draconic-WoW",
["Davin - Draconic-WoW"] = "Davin - Draconic-WoW",
["Sebas - Draconic-WoW"] = "Sebas - Draconic-WoW",
["Meatstick - Draconic-WoW"] = "Meatstick - Draconic-WoW",
["Voxghar - Draconic-WoW"] = "Voxghar - Draconic-WoW",
["Payton - Draconic-WoW"] = "Payton - Draconic-WoW",
["Rahddon - Draconic-WoW"] = "Rahddon - Draconic-WoW",
["Zezima - Draconic-WoW"] = "Zezima - Draconic-WoW",
["Laaj - Draconic-WoW"] = "Laaj - Draconic-WoW",
["Sampson - Draconic-WoW"] = "Sampson - Draconic-WoW",
["Lia - Draconic-WoW"] = "Lia - Draconic-WoW",
["Graham - Draconic-WoW"] = "Graham - Draconic-WoW",
["Grammon - Draconic-WoW"] = "Grammon - Draconic-WoW",
["Warren - Draconic-WoW"] = "Warren - Draconic-WoW",
["Thornhand - Draconic-WoW"] = "Thornhand - Draconic-WoW",
["Hatcher - Draconic-WoW"] = "Hatcher - Draconic-WoW",
["Kazil - Draconic-WoW"] = "Kazil - Draconic-WoW",
["Davos - Draconic-WoW"] = "Davos - Draconic-WoW",
["Crakash - Draconic-WoW"] = "Crakash - Draconic-WoW",
["Tredwell - Draconic-WoW"] = "Tredwell - Draconic-WoW",
["Mojoe - Draconic-WoW"] = "Mojoe - Draconic-WoW",
["Xathos - Draconic-WoW"] = "Xathos - Draconic-WoW",
["Magnus - Draconic-WoW"] = "Magnus - Draconic-WoW",
["Celestra - Draconic-WoW"] = "Celestra - Draconic-WoW",
["Ada - Draconic-WoW"] = "Ada - Draconic-WoW",
["Koby - Draconic-WoW"] = "Koby - Draconic-WoW",
["Baku - Draconic-WoW"] = "Baku - Draconic-WoW",
["Cecil - Draconic-WoW"] = "Cecil - Draconic-WoW",
["Mogh - Draconic-WoW"] = "Mogh - Draconic-WoW",
["Padrik - Draconic-WoW"] = "Padrik - Draconic-WoW",
["Havik - Draconic-WoW"] = "Havik - Draconic-WoW",
["Sicalicious - Draconic-WoW"] = "Sicalicious - Draconic-WoW",
["Nelson - Draconic-WoW"] = "Nelson - Draconic-WoW",
["Boris - Draconic-WoW"] = "Boris - Draconic-WoW",
["Wangz - Draconic-WoW"] = "Wangz - Draconic-WoW",
["Danvers - Draconic-WoW"] = "Danvers - Draconic-WoW",
["Elaria - Draconic-WoW"] = "Elaria - Draconic-WoW",
["Tylosh - Draconic-WoW"] = "Tylosh - Draconic-WoW",
["Nolen - Draconic-WoW"] = "Nolen - Draconic-WoW",
["Oren - Draconic-WoW"] = "Oren - Draconic-WoW",
["Adepta - Draconic-WoW"] = "Adepta - Draconic-WoW",
["Enoch - Draconic-WoW"] = "Enoch - Draconic-WoW",
["Kaitlan - Draconic-WoW"] = "Kaitlan - Draconic-WoW",
["Volkaris - Draconic-WoW"] = "Volkaris - Draconic-WoW",
["Yancy - Draconic-WoW"] = "Yancy - Draconic-WoW",
["Atrissa - Draconic-WoW"] = "Atrissa - Draconic-WoW",
["Jobe - Draconic-WoW"] = "Jobe - Draconic-WoW",
["Red - Draconic-WoW"] = "Red - Draconic-WoW",
["Bishop - Draconic-WoW"] = "Bishop - Draconic-WoW",
["Sic - Draconic-WoW"] = "Sic - Draconic-WoW",
["Moroes - Draconic-WoW"] = "Moroes - Draconic-WoW",
["Mercer - Draconic-WoW"] = "Mercer - Draconic-WoW",
["Alexius - Draconic-WoW"] = "Alexius - Draconic-WoW",
["Anders - Draconic-WoW"] = "Anders - Draconic-WoW",
["Prak - Draconic-WoW"] = "Prak - Draconic-WoW",
["Levara - Draconic-WoW"] = "Levara - Draconic-WoW",
},
["profiles"] = {
["Mika - Draconic-WoW"] = {
},
["Morvane - Draconic-WoW"] = {
},
["Stableslot - Draconic-WoW"] = {
},
["Korla - Draconic-WoW"] = {
},
["Mega - Draconic-WoW"] = {
},
["Daamis - Draconic-WoW"] = {
},
["Brax - Draconic-WoW"] = {
},
["Nelson - Draconic-WoW"] = {
},
["Tavish - Draconic-WoW"] = {
},
["Gantz - Draconic-WoW"] = {
},
["Draxtwo - Draconic-WoW"] = {
},
["Tav - Draconic-WoW"] = {
},
["Frag - Draconic-WoW"] = {
},
["Banks - Draconic-WoW"] = {
},
["Mav - Draconic-WoW"] = {
},
["Ruugar - Draconic-WoW"] = {
},
["Justicaris - Draconic-WoW"] = {
},
["Magna - Draconic-WoW"] = {
},
["Magnus - Draconic-WoW"] = {
},
["Kora - Draconic-WoW"] = {
},
["Baku - Draconic-WoW"] = {
},
["Regis - Draconic-WoW"] = {
},
["Momonga - Draconic-WoW"] = {
},
["Benny - Draconic-WoW"] = {
},
["Primarch - Draconic-WoW"] = {
},
["Ava - Draconic-WoW"] = {
},
["Shavonda - Draconic-WoW"] = {
},
["Korik - Draconic-WoW"] = {
},
["Ashford - Draconic-WoW"] = {
},
["Crackhammer - Draconic-WoW"] = {
},
["Valanese - Draconic-WoW"] = {
},
["Shapow - Draconic-WoW"] = {
},
["Alexius - Draconic-WoW"] = {
},
["Kalano - Draconic-WoW"] = {
},
["Dreya - Draconic-WoW"] = {
},
["Roland - Draconic-WoW"] = {
},
["Lolth - Draconic-WoW"] = {
},
["Starweaver - Draconic-WoW"] = {
},
["Jobe - Draconic-WoW"] = {
},
["Levara - Draconic-WoW"] = {
},
["Vandrus - Draconic-WoW"] = {
},
["Stonebreaker - Draconic-WoW"] = {
},
["Kazil - Draconic-WoW"] = {
},
["Xathos - Draconic-WoW"] = {
},
["Invaris - Draconic-WoW"] = {
},
["Mercer - Draconic-WoW"] = {
},
["Rahddon - Draconic-WoW"] = {
},
["Golo - Draconic-WoW"] = {
},
["Alice - Draconic-WoW"] = {
},
["Moremojo - Draconic-WoW"] = {
},
["Elaria - Draconic-WoW"] = {
},
["Lia - Draconic-WoW"] = {
},
["Reese - Draconic-WoW"] = {
},
["Nolan - Draconic-WoW"] = {
},
["Warren - Draconic-WoW"] = {
},
["Meatstick - Draconic-WoW"] = {
},
["Astaron - Draconic-WoW"] = {
},
["Havik - Draconic-WoW"] = {
},
["Phea - Draconic-WoW"] = {
},
["Tristian - Draconic-WoW"] = {
},
["Tredwell - Draconic-WoW"] = {
},
["Graham - Draconic-WoW"] = {
},
["Adnap - Draconic-WoW"] = {
},
["Sicalicious - Draconic-WoW"] = {
},
["Bishop - Draconic-WoW"] = {
},
["Ada - Draconic-WoW"] = {
},
["Pakmojo - Draconic-WoW"] = {
},
["Edwards - Draconic-WoW"] = {
},
["Lisbeth - Draconic-WoW"] = {
},
["Deez - Draconic-WoW"] = {
},
["Umbralight - Draconic-WoW"] = {
},
["Nolen - Draconic-WoW"] = {
},
["Oren - Draconic-WoW"] = {
},
["Cecil - Draconic-WoW"] = {
},
["Hatcher - Draconic-WoW"] = {
},
["Kardol - Draconic-WoW"] = {
},
["Danvers - Draconic-WoW"] = {
},
["Melrose - Draconic-WoW"] = {
},
["Vulkan - Draconic-WoW"] = {
},
["Grammon - Draconic-WoW"] = {
},
["Zhad - Draconic-WoW"] = {
},
["Adepta - Draconic-WoW"] = {
},
["Robb - Draconic-WoW"] = {
},
["Kaitlan - Draconic-WoW"] = {
},
["Celestra - Draconic-WoW"] = {
},
["Reynolds - Draconic-WoW"] = {
},
["Atrissa - Draconic-WoW"] = {
},
["Van - Draconic-WoW"] = {
},
["Solanna - Draconic-WoW"] = {
},
["Sebas - Draconic-WoW"] = {
},
["Sic - Draconic-WoW"] = {
},
["Eve - Draconic-WoW"] = {
},
["Zital - Draconic-WoW"] = {
},
["Grayson - Draconic-WoW"] = {
},
["Leyla - Draconic-WoW"] = {
},
["Prak - Draconic-WoW"] = {
},
["Korban - Draconic"] = {
},
},
},
}
BetterWardrobe_Mogitdata = nil
BetterWardrobe_Updates = {
["8_4"] = true,
}
BTT = nil


---

## 7. CollectorHelper SavedVariables

### Account: GROSTOLIS

settings = {
["autoShowNews"] = true,
["version"] = "2.5.4",
["showCostFrame"] = true,
["hideMerchantOwned"] = true,
["softCollect"] = false,
}
lfrCollected = {
[1448] = {
["wings"] = {
false,
false,
false,
false,
false,
},
},
[2096] = {
["wings"] = {
false,
},
},
[1205] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2164] = {
["wings"] = {
false,
false,
false,
},
},
[1008] = {
["wings"] = {
false,
false,
},
},
[1520] = {
["wings"] = {
false,
false,
false,
},
},
[1009] = {
["wings"] = {
false,
false,
},
},
[1648] = {
["wings"] = {
false,
},
},
[996] = {
["wings"] = {
false,
},
},
[2217] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1530] = {
["wings"] = {
false,
false,
false,
false,
},
},
[967] = {
["wings"] = {
false,
false,
},
},
[1676] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1098] = {
["wings"] = {
false,
false,
false,
false,
},
},
[0] = {
["wings"] = {
false,
},
},
[2070] = {
["wings"] = {
false,
false,
false,
},
},
[1712] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2481] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2450] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1228] = {
["wings"] = {
false,
false,
false,
},
},
[1136] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1861] = {
["wings"] = {
false,
false,
false,
},
},
[2296] = {
["wings"] = {
false,
false,
false,
false,
},
},
}
recipeCollected = {
["Draxtwo-Dentarg"] = {
},
}

### Account: 1#1

settings = {
["autoShowNews"] = true,
["version"] = "2.6.0",
["showCostFrame"] = true,
["showHousingFrame"] = true,
["hideMerchantOwned"] = false,
["housingDuplicateCount"] = 1,
["softCollect"] = true,
}
lfrCollected = {
[1448] = {
["wings"] = {
false,
false,
false,
false,
false,
},
},
[2096] = {
["wings"] = {
false,
},
},
[1205] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2164] = {
["wings"] = {
false,
false,
false,
},
},
[1008] = {
["wings"] = {
false,
false,
},
},
[1520] = {
["wings"] = {
false,
false,
false,
},
},
[1009] = {
["wings"] = {
false,
false,
},
},
[1648] = {
["wings"] = {
false,
},
},
[996] = {
["wings"] = {
false,
},
},
[2217] = {
["wings"] = {
false,
false,
false,
false,
},
},
[967] = {
["wings"] = {
false,
false,
},
},
[1530] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1676] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1098] = {
["wings"] = {
false,
false,
false,
false,
},
},
[0] = {
["wings"] = {
false,
},
},
[2070] = {
["wings"] = {
false,
false,
false,
},
},
[1712] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2450] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2481] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1228] = {
["wings"] = {
false,
false,
false,
},
},
[1136] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1861] = {
["wings"] = {
false,
false,
false,
},
},
[2296] = {
["wings"] = {
false,
false,
false,
false,
},
},
}
recipeCollected = {
["Lolth-Draconic-WoW"] = {
},
["Mogh-Draconic-WoW"] = {
},
["Melrose-Draconic-WoW"] = {
},
["Carlo-Draconic-WoW"] = {
},
["Benny-Draconic-WoW"] = {
},
["Quincy-Draconic-WoW"] = {
},
["Channa-Draconic-WoW"] = {
},
["Sic-Draconic-WoW"] = {
},
["Sicalicious-Draconic-WoW"] = {
},
["Draxtwo-Draconic-WoW"] = {
},
["Korla-Draconic-WoW"] = {
},
["Xathos-Draconic-WoW"] = {
},
["Deez-Draconic-WoW"] = {
},
["Nelson-Draconic-WoW"] = {
},
["Kazil-Draconic-WoW"] = {
},
["Padrik-Draconic-WoW"] = {
},
["Argyle-Draconic-WoW"] = {
},
}

### Account: 29#1

settings = {
["autoShowNews"] = true,
["version"] = "2.6.0",
["showCostFrame"] = true,
["showHousingFrame"] = true,
["hideMerchantOwned"] = false,
["housingDuplicateCount"] = 1,
["softCollect"] = true,
}
lfrCollected = {
[1448] = {
["wings"] = {
false,
false,
false,
false,
false,
},
},
[2096] = {
["wings"] = {
false,
},
},
[1205] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2164] = {
["wings"] = {
false,
false,
false,
},
},
[1008] = {
["wings"] = {
false,
false,
},
},
[1520] = {
["wings"] = {
false,
false,
false,
},
},
[1009] = {
["wings"] = {
false,
false,
},
},
[1648] = {
["wings"] = {
false,
},
},
[996] = {
["wings"] = {
false,
},
},
[2217] = {
["wings"] = {
false,
false,
false,
false,
},
},
[967] = {
["wings"] = {
false,
false,
},
},
[1530] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1676] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1098] = {
["wings"] = {
false,
false,
false,
false,
},
},
[0] = {
["wings"] = {
false,
},
},
[2070] = {
["wings"] = {
false,
false,
false,
},
},
[1712] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2450] = {
["wings"] = {
false,
false,
false,
false,
},
},
[2481] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1228] = {
["wings"] = {
false,
false,
false,
},
},
[1136] = {
["wings"] = {
false,
false,
false,
false,
},
},
[1861] = {
["wings"] = {
false,
false,
false,
},
},
[2296] = {
["wings"] = {
false,
false,
false,
false,
},
},
}
recipeCollected = {
["Lolth-Draconic-WoW"] = {
},
["Mogh-Draconic-WoW"] = {
},
["Melrose-Draconic-WoW"] = {
},
["Carlo-Draconic-WoW"] = {
},
["Benny-Draconic-WoW"] = {
},
["Quincy-Draconic-WoW"] = {
},
["Korban-Draconic"] = {
},
["Sic-Draconic-WoW"] = {
},
["Sicalicious-Draconic-WoW"] = {
},
["Draxtwo-Draconic-WoW"] = {
},
["Korla-Draconic-WoW"] = {
},
["Xathos-Draconic-WoW"] = {
},
["Deez-Draconic-WoW"] = {
},
["Nelson-Draconic-WoW"] = {
},
["Kazil-Draconic-WoW"] = {
},
["Padrik-Draconic-WoW"] = {
},
["Argyle-Draconic-WoW"] = {
},
}


---

## 8. TransmogCleanup SavedVariables

### Account: GROSTOLIS

TransmogCleanupDB = {
["ignoredItems"] = {
[122602] = true,
[95051] = true,
[45690] = true,
[84661] = true,
[17901] = true,
[17903] = true,
[17905] = true,
[51560] = true,
[17909] = true,
[63379] = true,
[28585] = true,
[122603] = true,
[37118] = true,
[48933] = true,
[127842] = true,
[52251] = true,
[48957] = true,
[17691] = true,
[65360] = true,
[122604] = true,
[45691] = true,
[93672] = true,
[63352] = true,
[44314] = true,
[30542] = true,
[30544] = true,
[46874] = true,
[109262] = true,
[75274] = true,
[52252] = true,
[48954] = true,
[35750] = true,
[58487] = true,
[6948] = true,
[63206] = true,
[45688] = true,
[64488] = true,
[44934] = true,
[32757] = true,
[17900] = true,
[17902] = true,
[17904] = true,
[51558] = true,
[17908] = true,
[9149] = true,
[68775] = true,
[40585] = true,
[22631] = true,
[44315] = true,
[50287] = true,
[48955] = true,
[35751] = true,
[64457] = true,
[17690] = true,
[17907] = true,
[17906] = true,
[65274] = true,
[63207] = true,
[35748] = true,
[45689] = true,
[68776] = true,
[44935] = true,
[44050] = true,
[87215] = true,
[31080] = true,
[18984] = true,
[51559] = true,
[44324] = true,
[63378] = true,
[35749] = true,
[44322] = true,
[37863] = true,
[44323] = true,
[122601] = true,
[95050] = true,
[13503] = true,
[68777] = true,
[58483] = true,
[103678] = true,
[63353] = true,
[128024] = true,
[18986] = true,
[48956] = true,
[45858] = true,
[128023] = true,
[40586] = true,
[54452] = true,
[51557] = true,
[19970] = true,
},
["sellMode"] = {
["safe"] = true,
["verbose"] = false,
},
["filters"] = {
["bind"] = {
true,
true,
true,
},
["learned"] = {
true,
true,
},
["ilvl"] = 400,
["onuse"] = true,
["quality"] = {
true,
true,
true,
true,
[0] = true,
},
},
}

### Account: 1#1

TransmogCleanupDB = {
["ignoredItems"] = {
[122602] = true,
[95051] = true,
[45690] = true,
[84661] = true,
[17901] = true,
[17903] = true,
[17905] = true,
[51560] = true,
[17909] = true,
[63379] = true,
[28585] = true,
[122603] = true,
[37118] = true,
[48933] = true,
[127842] = true,
[52251] = true,
[48957] = true,
[17691] = true,
[65360] = true,
[122604] = true,
[45691] = true,
[93672] = true,
[63352] = true,
[44314] = true,
[30542] = true,
[30544] = true,
[46874] = true,
[109262] = true,
[75274] = true,
[52252] = true,
[48954] = true,
[35750] = true,
[58487] = true,
[6948] = true,
[63206] = true,
[45688] = true,
[64488] = true,
[44934] = true,
[32757] = true,
[17900] = true,
[17902] = true,
[17904] = true,
[51558] = true,
[17908] = true,
[9149] = true,
[68775] = true,
[44315] = true,
[22631] = true,
[50287] = true,
[17690] = true,
[19970] = true,
[35751] = true,
[64457] = true,
[40585] = true,
[17906] = true,
[45858] = true,
[65274] = true,
[63207] = true,
[35748] = true,
[54452] = true,
[68776] = true,
[44935] = true,
[44050] = true,
[87215] = true,
[31080] = true,
[18984] = true,
[18986] = true,
[44324] = true,
[63378] = true,
[35749] = true,
[44322] = true,
[37863] = true,
[44323] = true,
[103678] = true,
[95050] = true,
[13503] = true,
[68777] = true,
[58483] = true,
[122601] = true,
[63353] = true,
[128024] = true,
[51559] = true,
[48956] = true,
[45689] = true,
[128023] = true,
[40586] = true,
[48955] = true,
[17907] = true,
[51557] = true,
},
["sellMode"] = {
["safe"] = true,
["verbose"] = false,
},
["filters"] = {
["bind"] = {
true,
true,
true,
},
["learned"] = {
true,
true,
},
["ilvl"] = 400,
["onuse"] = true,
["quality"] = {
true,
true,
true,
true,
[0] = true,
},
},
}

### Account: 29#1

TransmogCleanupDB = {
["ignoredItems"] = {
[122602] = true,
[95051] = true,
[45690] = true,
[84661] = true,
[17901] = true,
[17903] = true,
[17905] = true,
[51560] = true,
[17909] = true,
[63379] = true,
[28585] = true,
[122603] = true,
[37118] = true,
[48933] = true,
[127842] = true,
[52251] = true,
[48957] = true,
[17691] = true,
[65360] = true,
[122604] = true,
[45691] = true,
[93672] = true,
[63352] = true,
[44314] = true,
[30542] = true,
[30544] = true,
[46874] = true,
[109262] = true,
[75274] = true,
[52252] = true,
[48954] = true,
[35750] = true,
[58487] = true,
[6948] = true,
[63206] = true,
[45688] = true,
[64488] = true,
[44934] = true,
[32757] = true,
[17900] = true,
[17902] = true,
[17904] = true,
[51558] = true,
[17908] = true,
[9149] = true,
[68775] = true,
[44315] = true,
[22631] = true,
[50287] = true,
[17690] = true,
[19970] = true,
[35751] = true,
[64457] = true,
[40585] = true,
[17906] = true,
[45858] = true,
[65274] = true,
[63207] = true,
[35748] = true,
[54452] = true,
[68776] = true,
[44935] = true,
[44050] = true,
[87215] = true,
[31080] = true,
[18984] = true,
[18986] = true,
[44324] = true,
[63378] = true,
[35749] = true,
[44322] = true,
[37863] = true,
[44323] = true,
[103678] = true,
[95050] = true,
[13503] = true,
[68777] = true,
[58483] = true,
[122601] = true,
[63353] = true,
[128024] = true,
[51559] = true,
[48956] = true,
[45689] = true,
[128023] = true,
[40586] = true,
[48955] = true,
[17907] = true,
[51557] = true,
},
["sellMode"] = {
["safe"] = true,
["verbose"] = false,
},
["filters"] = {
["bind"] = {
true,
true,
true,
},
["learned"] = {
true,
true,
},
["ilvl"] = 400,
["onuse"] = true,
["quality"] = {
true,
true,
true,
true,
[0] = true,
},
},
}


---

## 9. TransmogCleaner SavedVariables

### Account: GROSTOLIS

TransmogCleanerSettings = {
["skipExpansions"] = {
false,
true,
true,
true,
true,
true,
true,
true,
true,
true,
[254] = false,
},
["skipList"] = {
},
["minItemLevel"] = 0,
["maxItemLevel"] = 380,
["nameFilter"] = "",
["itemTypes"] = {
["Equip"] = true,
["Consumable"] = false,
["TradeGoods"] = false,
["Misc"] = false,
},
["maxReqLevel"] = 79,
["quality"] = {
false,
false,
true,
false,
false,
[0] = false,
},
}

### Account: 1#1

TransmogCleanerSettings = {
["skipExpansions"] = {
false,
true,
true,
true,
true,
true,
true,
true,
true,
true,
[254] = false,
},
["skipList"] = {
},
["minItemLevel"] = 0,
["maxItemLevel"] = 380,
["nameFilter"] = "",
["itemTypes"] = {
["Equip"] = true,
["Consumable"] = false,
["Misc"] = false,
["TradeGoods"] = false,
},
["maxReqLevel"] = 79,
["quality"] = {
false,
false,
true,
false,
false,
[0] = false,
},
}

### Account: 29#1

TransmogCleanerSettings = {
["skipExpansions"] = {
false,
true,
true,
true,
true,
true,
true,
true,
true,
true,
[254] = false,
},
["skipList"] = {
},
["minItemLevel"] = 0,
["maxItemLevel"] = 380,
["nameFilter"] = "",
["itemTypes"] = {
["Equip"] = true,
["Consumable"] = false,
["Misc"] = false,
["TradeGoods"] = false,
},
["maxReqLevel"] = 79,
["quality"] = {
false,
false,
true,
false,
false,
[0] = false,
},
}


---

## 10. Additional Transmog CVars (from AccountData.log.old)

wardrobeShowAllFactions = 1
wardrobeShowAllRaces = 1

(These 2 CVars appear in AccountData.log.old but not the current AccountData.log)


---

## Completeness Notes

This file contains ALL transmog-related data extracted from the retail WoW 12.0.1.66263 client:

### SavedVariables (addon data)
1. **TransmogSpy** -- GROSTOLIS (141 entries) + 1#1 (2,001 entries)
2. **BetterWardrobe** -- GROSTOLIS (165 lines) + 1#1 (3,757 lines) + 25#1 (502 lines) + 29#1 (2,694 lines)
3. **CollectorHelper** -- GROSTOLIS (176 lines) + 1#1 (210 lines) + 29#1 (210 lines)
4. **TransmogCleanup** -- GROSTOLIS + 1#1 + 29#1 (118 lines each)
5. **TransmogCleaner** -- GROSTOLIS + 1#1 + 29#1 (36 lines each)

### Client logs
6. **FrameXML.log** -- TransmogSpy `goto continue` error at line 1184
7. **Hotfix.log** -- 5,600+ transmog-related entries (TransmogHoliday, TransmogSet, TransmogSetItem, TransmogSetGroup, TransmogIllusion, TransmogDefaultLevel)
8. **AccountData.log** -- Transmog CVars (wardrobeRecentItems, transmogCurrentSpecOnly, wardrobeShowAllFactions, wardrobeShowAllRaces)

### NOT found / empty
- **TransmogBridge** -- No SavedVariables files found (addon not installed on retail)
- **DBCache_parsed.txt** -- 0 transmog matches
- **Hotfix.log.old** -- Does not exist

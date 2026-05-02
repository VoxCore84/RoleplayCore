---
name: SME Sweep and Master File Quality Standards
description: Lessons from session 248 — ask for standard before writing, verify agent output, bake path conventions into prompts, build verification scripts upfront
type: feedback
originSessionId: 174a12f5-5f19-4cfb-89ce-c071fb0f30fc
---
# SME Sweep + Master File Creation — Learned Standards

## Ask for the quality template BEFORE writing
**Why:** Session 248 wrote 16 _MASTER.md files, then user showed the SAPR Attorney Reference Packet as the standard, and all 16 had to be rewritten. Double cost.
**How to apply:** Before creating any batch of structured documents, ask: "Do you have a template or quality standard I should match?"

## Verify agent output before claiming completion
**Why:** 6 of 16 agent-written files had errors (wrong file counts, fabricated merge claim, wrong memory paths, hallucinated contact). User asked "are these 100% correct?" and the honest answer was "I haven't verified all 16."
**How to apply:** After agent batch completes, run automated verification (filename existence, path resolution, file counts, duration math) BEFORE reporting to user. Read back at least a sample. Never claim "complete" without evidence.

## Bake conventions into agent prompts
**Why:** 3 agents independently used wrong memory path (`C:/Users/atayl/VoxCore/memory/` instead of `~/.claude/projects/C--Users-atayl-VoxCore/memory/`). One agent fabricated a folder merge that never happened.
**How to apply:** Include in every _MASTER.md agent prompt:
- "Memory paths use `~/.claude/projects/C--Users-atayl-VoxCore/memory/`"
- "Run `find` to verify file count before writing"
- "Do not claim files were moved/merged unless you did it yourself"
- "Verify at least 3 filenames exist on disk before referencing them"

## Build verification scripts FIRST
**Why:** The 4-pass verification (filename existence, path resolution, file counts, duration math) was written reactively after user challenged accuracy. Should have been ready before the first claim of completion.
**How to apply:** For any batch document creation, write the verification script before launching agents. Run it immediately after agents complete.

## SAPR Packet is the _MASTER.md standard
The reference standard for all _MASTER.md files is `C:\Users\atayl\Desktop\Taylor_SAPR_Attorney_Reference_Packet_MASTER.md`. Required sections: Document Control, Orientation, Executive Overview, Issue/Gap Matrix, Key Documents (with specific content), domain-appropriate sections (Chronology, Contacts, Legal Authorities, Records Preservation), Cross-References. Duration counts pinned to a specific date. Hedging on unverified claims. No fabricated contact info.

## Smaller agent batches = better quality
Agents writing 4-6 files per batch showed quality degradation on later files. Prefer 1-2 files per agent or explicit "verify each before starting the next" instructions.

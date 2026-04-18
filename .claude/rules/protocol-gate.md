# Protocol & Binary Work — MANDATORY Pre-Implementation Gate

Applies to: packet parsing, opcode handlers, crypto/key derivation, DB2 field mapping, sniffer work (VoxSniffer, CalmSniffer), any file with "Packet", "Opcode", "Socket", "Crypto", "HMAC", "Sniffer" in the name, any Protocol/ directory work.

## HARD RULE: Verify raw data BEFORE writing implementation code

Every protocol/binary task must complete these gates IN ORDER before writing production code:

### Gate 1: Dump Raw Data
- Display actual hex bytes of the data being processed (not parsed structures)
- For packets: show raw hex from WPP output or pcap, annotated with field boundaries
- For crypto: write out algorithm steps with concrete test vectors
- For DB2: show CSV header row and 2-3 sample data rows from Wago export

### Gate 2: Document Wire Format
- Write a field map: `offset | size | type | name | example_value`
- Verify header size against actual traffic (don't assume — 4, 6, and 8 byte headers all exist)
- Verify opcode against the client build's opcode table (opcodes shift between builds)
- Verify direction (CMSG vs SMSG) — TCP direction logic errors are silent and devastating

### Gate 3: Minimal Verification
- Parse one known-good sample by hand (hex dump → expected field values)
- If modifying existing code: run it against test input and capture BEFORE state
- For key derivation: compute expected output from test vectors before coding

### Gate 4: Then Implement
- Only now write the production code
- After implementing: re-run the Gate 3 sample and compare output

## Known Failure Modes (from real sessions)

| Failure | Root Cause | Gate That Catches It |
|---------|-----------|---------------------|
| Buffered parsed frames instead of raw TCP | Worked at wrong layer | Gate 1 |
| Wrong opcode, compiles but processes wrong packet | Didn't verify opcode table | Gate 2 |
| Missing banner/handshake skip | Didn't dump initial bytes | Gate 1 |
| Header size wrong (assumed 4, was 6) | Didn't measure actual traffic | Gate 2 |
| TCP direction reversed | Didn't verify CMSG vs SMSG | Gate 2 |
| Field offset drift from prior field size error | Didn't verify each field boundary | Gate 2 |

## DESCRIBE Before SQL
For any DB2 table work: `DESCRIBE hotfixes.<table>` AND cross-reference against Wago CSV headers BEFORE writing INSERT/UPDATE statements. Column names and order change between builds.

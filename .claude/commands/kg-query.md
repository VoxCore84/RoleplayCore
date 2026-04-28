---
description: "Query the Knowledge Graph — entity lookup, mentions, relations, stats, dedup"
---

# /kg-query — Knowledge Graph Query

Parse `$ARGUMENTS` to determine which subcommand to run. If no arguments, show stats.

## Subcommands

### No args / `stats` — Show KG statistics
Run: `python -m tools.excluded_daemon.kg.query --stats`
Report: total entities/mentions/relations, breakdown by kind, top 10 persons.

### `<name>` — Look up an entity by name
Run: `python -m tools.excluded_daemon.kg.query "<name>"`
Report: canonical name, kind, mention count, metadata, top 5 mentions with source doc paths.

If multiple entities match, show all of them with IDs.

### `--kind <type>` — List all entities of a kind
Run: `python -m tools.excluded_daemon.kg.query --kind <type> --all`
Valid kinds: person, org, date, case_number, regulation, amount, location

### `mentions <id>` — Show all mentions for entity ID
Run: `python -m tools.excluded_daemon.kg.query --mentions <id>`
Report: each mention with doc_path and context snippet.

### `relations <id>` — Show relations for entity ID
Run: `python -m tools.excluded_daemon.kg.query --relations <id>`
Report: subject → predicate → object with confidence.

### `scan` — Run contradiction scanner
Run: `python -m tools.excluded_daemon.jobs.contradiction`
Report: number of contradictions found, path to report file. Summarize top 5 findings inline.

### `build` — Check build status or trigger incremental build
Run: `python -c "import sqlite3; conn=sqlite3.connect('.cache/excluded_kg.db'); print(f'Entities: {conn.execute(\"SELECT COUNT(*) FROM entities\").fetchone()[0]:,}'); print(f'Mentions: {conn.execute(\"SELECT COUNT(*) FROM mentions\").fetchone()[0]:,}'); print(f'Relations: {conn.execute(\"SELECT COUNT(*) FROM relations\").fetchone()[0]:,}'); print(f'Unique docs: {conn.execute(\"SELECT COUNT(DISTINCT doc_path) FROM mentions\").fetchone()[0]:,}')"`

If the user says "rebuild" or "build --reset", confirm before running (it takes hours).

### `dedup` — Find duplicate entities
Run: `python -c "
import sqlite3, json
conn = sqlite3.connect('.cache/excluded_kg.db')
conn.row_factory = sqlite3.Row
# Find potential duplicates: same kind, similar canonical names
rows = conn.execute('''
    SELECT a.id as a_id, a.name as a_name, a.canonical as a_canon,
           b.id as b_id, b.name as b_name, b.canonical as b_canon, a.kind
    FROM entities a, entities b
    WHERE a.kind = b.kind AND a.id < b.id
    AND (a.canonical LIKE '%' || b.canonical || '%' OR b.canonical LIKE '%' || a.canonical || '%')
    AND length(a.canonical) > 3 AND length(b.canonical) > 3
    LIMIT 30
''').fetchall()
for r in rows:
    ac = conn.execute('SELECT COUNT(*) FROM mentions WHERE entity_id=?', (r['a_id'],)).fetchone()[0]
    bc = conn.execute('SELECT COUNT(*) FROM mentions WHERE entity_id=?', (r['b_id'],)).fetchone()[0]
    print(f'  [{r[\"kind\"]}] \"{r[\"a_name\"]}\" ({ac} mentions) <-> \"{r[\"b_name\"]}\" ({bc} mentions)')
conn.close()
"`

Report potential merges. Do NOT auto-merge without user confirmation.

## Help Text (shown with no args after stats)
```
/kg-query — Knowledge Graph (24,854 entities from 1,484 documents)

Usage:
  /kg-query                    Show KG statistics
  /kg-query Amy Little         Look up entity by name
  /kg-query --kind person      List all persons
  /kg-query --kind regulation  List all regulations
  /kg-query mentions 7         Show mentions for entity #7
  /kg-query relations 7        Show relations for entity #7
  /kg-query scan               Run contradiction scanner
  /kg-query build              Check build status
  /kg-query dedup              Find duplicate entities

DB: .cache/excluded_kg.db | Auto-maintained by daemon (new files → NER → KG)
```

-- Knowledge Graph schema for the Excluded/ corpus.
-- SQLite DB at .cache/excluded_kg.db

CREATE TABLE IF NOT EXISTS entities (
    id          INTEGER PRIMARY KEY,
    kind        TEXT NOT NULL,
    name        TEXT NOT NULL,
    canonical   TEXT NOT NULL,
    first_seen  TEXT,
    last_seen   TEXT,
    metadata    TEXT DEFAULT '{}',
    UNIQUE(kind, canonical)
);

CREATE TABLE IF NOT EXISTS mentions (
    id          INTEGER PRIMARY KEY,
    entity_id   INTEGER NOT NULL REFERENCES entities(id),
    chunk_id    TEXT NOT NULL,
    doc_path    TEXT NOT NULL,
    line_hint   TEXT DEFAULT '',
    context     TEXT NOT NULL,
    confidence  REAL DEFAULT 0.8,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS relations (
    id          INTEGER PRIMARY KEY,
    subject_id  INTEGER NOT NULL REFERENCES entities(id),
    predicate   TEXT NOT NULL,
    object_id   INTEGER NOT NULL REFERENCES entities(id),
    source_chunk TEXT NOT NULL,
    confidence  REAL DEFAULT 0.7,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_mentions_entity ON mentions(entity_id);
CREATE INDEX IF NOT EXISTS idx_mentions_doc ON mentions(doc_path);
CREATE INDEX IF NOT EXISTS idx_relations_subject ON relations(subject_id);
CREATE INDEX IF NOT EXISTS idx_relations_object ON relations(object_id);
CREATE INDEX IF NOT EXISTS idx_entities_kind ON entities(kind);
CREATE INDEX IF NOT EXISTS idx_entities_canonical ON entities(canonical);

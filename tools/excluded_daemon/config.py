"""Runtime config for the Excluded daemon.

Edit here, not via env — simpler and checked into git alongside the code.
"""
from pathlib import Path

# Source corpus root
EXCLUDED_ROOT = Path("C:/Users/atayl/Desktop/Excluded")

# Repo + caches
REPO_ROOT = Path("C:/Users/atayl/VoxCore")
CACHE_ROOT = REPO_ROOT / ".cache"
DAEMON_CACHE = CACHE_ROOT / "excluded_daemon"
QUEUE_FILE = DAEMON_CACHE / "queue.jsonl"
PID_FILE = DAEMON_CACHE / "daemon.pid"
STATE_FILE = DAEMON_CACHE / "state.json"

# Log output
LOG_DIR = REPO_ROOT / "AI_Studio" / "Reports" / "daemon"
LOG_FILE = LOG_DIR / "excluded_daemon.log"

# Pipeline tool references
EXTRACT_CACHE_PY = REPO_ROOT / "tools" / "extract_cache.py"
OCR_IMAGES_PY = REPO_ROOT / "tools" / "ocr_images.py"
AUDIO_TRANSCRIBE_PY = REPO_ROOT / "tools" / "audio_transcribe.py"
MBOX_INDEX_PY = REPO_ROOT / "tools" / "mbox" / "index.py"
RAG_BUILD_PY = REPO_ROOT / "tools" / "rag_build.py"
FTS_BUILD_PY = REPO_ROOT / "tools" / "excluded_fts_build.py"

# ---------------------------------------------------------------------------
# Routing policy
# ---------------------------------------------------------------------------

EXTRACTABLE_EXTS = {".pdf", ".docx", ".doc", ".eml", ".msg", ".md", ".txt", ".rtf"}
OCR_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}
AUDIO_EXTS = {".m4a", ".mp3", ".wav", ".ogg", ".flac"}
MBOX_EXTS = {".mbox"}

# Extensions we explicitly ignore
SKIP_EXTS = {
    ".dll", ".exe", ".lnk", ".ini", ".conf",
    ".sql", ".cpp", ".lua", ".py", ".toc", ".js", ".ts",
    ".gitignore", ".bak", ".tmp", ".swp",
    ".ds_store",
}

# Folder-level exclusions (do not watch/index)
SKIP_FOLDERS = {
    "LoreWalkerTDB",          # CalmCore parked here
    "unredact",               # internal pipeline workspace
    "_Archive",               # retired material, lower priority
    "takeout-20260411T200559Z-3-001",  # separate indexing path
}

# Sub-path patterns that must never be indexed (chain-of-custody writable zones)
# Currently no zones block reads — Case_Reference is read-only but indexable.
# Daemon must never WRITE to any path under Case_Reference/.
READONLY_PATHS = [
    "IMPORTANT DOCS/Case_Reference",
]

# Folders whose new-file events emit a one-line briefing notification
# to AI_Studio/Reports/scheduled/new_items_<date>.md. Read at session-start.
HIGH_PRIORITY_FOLDERS = {
    "IMPORTANT DOCS/Case_Reference/04_LEGAL_CORRESPONDENCE",
    "IMPORTANT DOCS/Case_Reference/01_APPEALS_AND_QAI",
    "IMPORTANT DOCS/Case_Reference/05_EVIDENCE_SCREENSHOTS",
    "IMPORTANT DOCS/Case_Reference/08_CONGRESSIONAL",
    "IMPORTANT DOCS/Case_Reference/09_SECURITY_CLEARANCE",
    "IMPORTANT DOCS/Case_Reference/11_EMAILS",
    "IMPORTANT DOCS/Monday_HAF_Call_13Apr2026",
    "IMPORTANT DOCS/Angel_VA",
    "IMPORTANT DOCS/Finances",
}

# Content-scan security patterns — regexes applied to the first 4KB of any
# text-extractable file before it enters any pipeline. Two-stage defense
# (Pattern A from UKB Playbook 01): filename gate + content gate.
SECURITY_CONTENT_PATTERNS = [
    # Bare SSN (3-2-4 with separators)
    r"\b\d{3}-\d{2}-\d{4}\b",
    # Common credential assignment syntaxes
    r"(?i)\bpassword\s*[:=]\s*\S+",
    r"(?i)\bapi[_-]?key\s*[:=]\s*\S+",
    r"(?i)\bsecret[_-]?key\s*[:=]\s*\S+",
    # Private-key PEM headers
    r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----",
    # AWS access key pattern
    r"\bAKIA[0-9A-Z]{16}\b",
]

# ---------------------------------------------------------------------------
# Security filter
# ---------------------------------------------------------------------------
# Filenames (case-insensitive substring match) that must never be indexed.
# If matched, the daemon logs a SECURITY event, skips all pipelines, and
# does NOT place the content in any cache/index.

SECURITY_FILENAMES = [
    "pword",                   # Pword.txt
    "password",                # password*.txt
    "recovery-codes",
    "backup-codes",
    "credentials",
    "secret",
    "api-key",
    "apikey",
    ".env",
    "id_rsa",
    "id_ed25519",
]

# Folder names whose contents are never indexed
SECURITY_FOLDERS = {"Credentials", "Secrets", ".ssh", ".gnupg"}

# ---------------------------------------------------------------------------
# Concurrency limits
# ---------------------------------------------------------------------------

MAX_EXTRACT_WORKERS = 4
MAX_OCR_WORKERS = 4
MAX_AUDIO_WORKERS = 1    # GPU-bound if nightly torch installed
MAX_LLM_WORKERS = 2
MAX_INDEX_WORKERS = 1    # single writer owns ChromaDB + FTS5

# ---------------------------------------------------------------------------
# Knowledge Graph
# ---------------------------------------------------------------------------

KG_DB = CACHE_ROOT / "excluded_kg.db"
KG_SCHEMA = Path(__file__).resolve().parent / "kg" / "schema.sql"

# ---------------------------------------------------------------------------
# Ollama / local LLM
# ---------------------------------------------------------------------------

OLLAMA_URL = "http://localhost:11434"
NER_MODEL = "qwen3.5:27b-q4_K_M"
NER_TIMEOUT = 120          # seconds per chunk
NER_CHUNK_SIZE = 2000      # chars per NER request
NER_CHUNK_OVERLAP = 200

# ---------------------------------------------------------------------------
# Contradiction scanner
# ---------------------------------------------------------------------------

CONTRADICTION_INTERVAL = 21600  # 6 hours
PERSONS_ROSTER = CACHE_ROOT / "persons" / "persons.json"

# Debounce window before firing a pipeline on a file — word processors emit
# many events during save. We coalesce to the final quiet state.
DEBOUNCE_SECONDS = 5.0

# ---------------------------------------------------------------------------
# Memory cap — pause LLM workers if system memory gets tight
# ---------------------------------------------------------------------------

MEMORY_PAUSE_THRESHOLD_PCT = 80.0

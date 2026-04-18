#!/usr/bin/env python3
"""Validate deliverables after Claude claims completion.

3-pass validator: structure, hallucination detection, quality sweep.
Usage: python tools/validate_deliverable.py <path> [--type auto|markdown|sql|code] [--strict] [--json]
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

PLACEHOLDER_PATTERNS = [
    r'\bTODO\b', r'\bFIXME\b', r'\bTBD\b', r'\bXXX\b',
    r'\bplaceholder\b', r'\blorem ipsum\b', r'\bexample\.com\b',
    r'\bfoo\b.*\bbar\b.*\bbaz\b',
]

FILE_REF_PATTERNS = [
    r'`([A-Za-z]:\\[^`\n]+)`',               # Windows paths in backticks
    r'`((?:src|tools|doc|sql|\.claude)/[^`\n]+)`',  # Unix-style project paths
    r'(?:created|modified|wrote|updated|edited)\s+(?:file\s+)?`?([^\s`\n,]+\.\w+)`?',
]


class Result:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.oks = []

    def err(self, pass_name, msg, line=None):
        loc = f" (line {line})" if line else ""
        self.errors.append({"pass": pass_name, "msg": msg + loc, "level": "ERR"})

    def warn(self, pass_name, msg, line=None):
        loc = f" (line {line})" if line else ""
        self.warnings.append({"pass": pass_name, "msg": msg + loc, "level": "WARN"})

    def ok(self, pass_name, msg):
        self.oks.append({"pass": pass_name, "msg": msg, "level": "OK"})

    @property
    def exit_code(self):
        if self.errors:
            return 2
        if self.warnings:
            return 1
        return 0


def detect_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in ('.md', '.markdown'):
        return 'markdown'
    if ext == '.sql':
        return 'sql'
    if ext in ('.py', '.cpp', '.h', '.hpp', '.c', '.lua', '.js', '.ts'):
        return 'code'
    return 'markdown'


def read_file(path: Path) -> tuple[str, list[str]]:
    text = path.read_text(encoding='utf-8', errors='replace')
    return text, text.splitlines()


# === PASS 1: Structure ===

def pass1_markdown(lines: list[str], result: Result):
    headers = []
    in_code_block = False
    code_blocks_with_lang = 0
    code_blocks_total = 0
    unclosed_fence = False

    for i, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            if not in_code_block:
                code_blocks_total += 1
                lang = line.strip()[3:].strip()
                if lang:
                    code_blocks_with_lang += 1
                in_code_block = True
            else:
                in_code_block = False

        if not in_code_block and re.match(r'^#{1,6}\s+\S', line):
            headers.append((i, line.strip()))

    if in_code_block:
        result.err("Structure", "Unclosed code fence (``` without matching close)")
        unclosed_fence = True

    if not headers:
        result.warn("Structure", "No section headers found")
    else:
        result.ok("Structure", f"Section headers: {len(headers)} found")

    # Check empty sections
    empty_sections = 0
    for idx in range(len(headers) - 1):
        start_line = headers[idx][0]
        end_line = headers[idx + 1][0]
        content = '\n'.join(lines[start_line:end_line - 1]).strip()
        if not content:
            empty_sections += 1
            result.warn("Structure", f"Empty section: {headers[idx][1]}", headers[idx][0])
    if empty_sections == 0 and headers:
        result.ok("Structure", "All sections have content")

    if code_blocks_total > 0:
        no_lang = code_blocks_total - code_blocks_with_lang
        if no_lang > 0:
            result.warn("Structure", f"{no_lang}/{code_blocks_total} code blocks missing language tag")
        else:
            result.ok("Structure", f"Code blocks: {code_blocks_total}/{code_blocks_total} have language tags")

    # Placeholder check (skip lines that are string/regex definitions)
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith(("r'", "r\"", "'", "\"")) and stripped.endswith(("',", "',", "\",", "\"")):
            continue
        for pat in PLACEHOLDER_PATTERNS:
            if re.search(pat, line, re.IGNORECASE):
                result.warn("Structure", f"Placeholder marker: {pat.strip(chr(92)).strip('b')}", i)
                break

    # Internal link check
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    broken_links = 0
    total_links = 0
    for i, line in enumerate(lines, 1):
        for match in link_pattern.finditer(line):
            target = match.group(2)
            if target.startswith('http') or target.startswith('#') or target.startswith('mailto:'):
                continue
            total_links += 1
            target_clean = target.split('#')[0]
            if target_clean and not Path(target_clean).exists():
                broken_links += 1
                result.warn("Structure", f"Broken link: {target_clean}", i)
    if total_links > 0 and broken_links == 0:
        result.ok("Structure", f"Internal links: {total_links}/{total_links} resolve")

    # Table validation
    table_issues = check_markdown_tables(lines)
    for issue in table_issues:
        result.warn("Structure", issue["msg"], issue["line"])
    if not table_issues:
        result.ok("Structure", "Markdown tables consistent")


def pass1_sql(text: str, lines: list[str], result: Result):
    # Unbalanced parens
    open_p = text.count('(')
    close_p = text.count(')')
    if open_p != close_p:
        result.err("Structure", f"Unbalanced parentheses: {open_p} open, {close_p} close")
    else:
        result.ok("Structure", "Parentheses balanced")

    # VALUES column count vs INSERT column list
    insert_re = re.compile(
        r'INSERT\s+INTO\s+\S+\s*\(([^)]+)\)\s*VALUES\s*\(([^)]+)\)',
        re.IGNORECASE | re.DOTALL
    )
    mismatches = 0
    for m in insert_re.finditer(text):
        cols = len([c.strip() for c in m.group(1).split(',') if c.strip()])
        vals = len([v.strip() for v in m.group(2).split(',') if v.strip()])
        if cols != vals:
            pos = text[:m.start()].count('\n') + 1
            result.err("Structure", f"INSERT column/value mismatch: {cols} cols, {vals} vals", pos)
            mismatches += 1
    if mismatches == 0:
        result.ok("Structure", "INSERT column/value counts match")

    # Missing semicolons (statements that don't end with ;)
    statements = re.split(r';\s*\n', text.strip())
    if statements and statements[-1].strip() and not statements[-1].strip().endswith(';'):
        last_kw = re.match(r'\s*(INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|SELECT)', statements[-1], re.IGNORECASE)
        if last_kw:
            result.warn("Structure", "Last SQL statement may be missing semicolon")

    for pat in PLACEHOLDER_PATTERNS:
        for i, line in enumerate(lines, 1):
            if re.search(pat, line, re.IGNORECASE):
                result.warn("Structure", f"Placeholder in SQL: {pat.strip(chr(92)).strip('b')}", i)
                break


def pass1_code(text: str, lines: list[str], path: Path, result: Result):
    ext = path.suffix.lower()
    # Brace matching for C-family
    if ext in ('.cpp', '.h', '.hpp', '.c'):
        opens = text.count('{')
        closes = text.count('}')
        if opens != closes:
            result.err("Structure", f"Unbalanced braces: {opens} open, {closes} close")
        else:
            result.ok("Structure", "Braces balanced")

    # For code, only flag TODO/FIXME in comments (not in strings or variable names)
    comment_pats = [r'\bTODO\b', r'\bFIXME\b', r'\bXXX\b', r'\bHACK\b']
    comment_markers = {'.py': '#', '.lua': '--', '.cpp': '//', '.h': '//', '.hpp': '//', '.c': '//', '.js': '//', '.ts': '//'}
    marker = comment_markers.get(ext, '#')
    for i, line in enumerate(lines, 1):
        if marker in line:
            comment_part = line[line.index(marker):]
            for pat in comment_pats:
                if re.search(pat, comment_part, re.IGNORECASE):
                    result.warn("Structure", f"TODO/FIXME in comment", i)
                    break

    if os.path.getsize(path) == 0:
        result.err("Structure", "File is empty (0 bytes)")


# === PASS 2: Hallucination Check ===

def pass2_hallucination(text: str, lines: list[str], result: Result):
    found_refs = 0
    missing_refs = 0

    for pattern in FILE_REF_PATTERNS:
        for i, line in enumerate(lines, 1):
            for m in re.finditer(pattern, line, re.IGNORECASE):
                ref = m.group(1).strip().rstrip('.,;:)')
                if not ref or len(ref) < 4:
                    continue
                found_refs += 1
                ref_path = Path(ref)
                if not ref_path.is_absolute():
                    ref_path = Path.cwd() / ref
                if not ref_path.exists():
                    missing_refs += 1
                    result.err("Hallucination", f"Path not found: {ref}", i)

    if found_refs > 0 and missing_refs == 0:
        result.ok("Hallucination", f"File references: {found_refs}/{found_refs} exist")
    elif found_refs == 0:
        result.ok("Hallucination", "No file path references to verify")

    # Copy-paste / repetition detection
    if len(lines) > 20:
        chunks = []
        for i in range(0, len(lines) - 3):
            chunk = '\n'.join(lines[i:i+4]).strip()
            if len(chunk) > 80:
                chunks.append((i + 1, chunk))
        seen = {}
        dupes = 0
        for line_num, chunk in chunks:
            if chunk in seen and line_num - seen[chunk] > 5:
                result.warn("Hallucination", f"Repeated block (~4 lines) at lines {seen[chunk]} and {line_num}", line_num)
                dupes += 1
                if dupes >= 3:
                    break
            seen[chunk] = line_num
        if dupes == 0:
            result.ok("Hallucination", "No copy-paste artifacts detected")

    # Check for "created file X" claims against git
    created_pattern = re.compile(r'(?:created|wrote|generated)\s+(?:file\s+)?`?([^\s`\n,]+\.\w+)`?', re.IGNORECASE)
    git_claims = 0
    git_missing = 0
    for i, line in enumerate(lines, 1):
        for m in created_pattern.finditer(line):
            fpath = m.group(1).strip()
            if len(fpath) < 4:
                continue
            git_claims += 1
            p = Path(fpath)
            if not p.is_absolute():
                p = Path.cwd() / p
            if not p.exists():
                git_missing += 1
                result.err("Hallucination", f"Claimed created file not found: {fpath}", i)
    if git_claims > 0 and git_missing == 0:
        result.ok("Hallucination", f"Created-file claims: {git_claims}/{git_claims} verified")


# === PASS 3: Quality Sweep ===

def pass3_quality(text: str, lines: list[str], path: Path, result: Result):
    # Duplicate section headers (markdown)
    if path.suffix.lower() in ('.md', '.markdown'):
        headers = []
        for i, line in enumerate(lines, 1):
            m = re.match(r'^(#{1,6})\s+(.+)', line)
            if m:
                headers.append((i, m.group(1), m.group(2).strip()))
        seen_headers = {}
        for line_num, level, title in headers:
            key = f"{level} {title}"
            if key in seen_headers:
                result.warn("Quality", f"Duplicate header: '{title}' (also at line {seen_headers[key]})", line_num)
            seen_headers[key] = line_num

    # Stale date references
    import datetime
    today = datetime.date.today()
    date_pattern = re.compile(r'(\d{4})[/-](\d{1,2})[/-](\d{1,2})')
    for i, line in enumerate(lines, 1):
        if re.search(r'(?:current|now|today|latest|as of)', line, re.IGNORECASE):
            for m in date_pattern.finditer(line):
                try:
                    ref_date = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                    if (today - ref_date).days > 30:
                        result.warn("Quality", f"Possibly stale date '{m.group(0)}' marked as current ({(today - ref_date).days}d old)", i)
                except ValueError:
                    pass

    # Encoding check
    try:
        path.read_bytes().decode('utf-8')
        result.ok("Quality", "File encoding: valid UTF-8")
    except UnicodeDecodeError:
        result.warn("Quality", "File contains non-UTF-8 bytes")

    # Zero-byte check
    if path.stat().st_size == 0:
        result.err("Quality", "File is zero bytes")


def check_markdown_tables(lines: list[str]) -> list[dict]:
    issues = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect table: line with |, followed by separator line with |---|
        if '|' in line and i + 1 < len(lines) and re.match(r'^[\s|:-]+$', lines[i + 1]):
            header_cols = len([c for c in line.split('|') if c.strip() != ''])
            j = i + 2
            while j < len(lines) and '|' in lines[j]:
                row_cols = len([c for c in lines[j].split('|') if c.strip() != ''])
                if row_cols != header_cols and lines[j].strip():
                    issues.append({
                        "line": j + 1,
                        "msg": f"Table row has {row_cols} cols, header has {header_cols}"
                    })
                j += 1
            i = j
        else:
            i += 1
    return issues


def validate_directory(dirpath: Path, result: Result):
    files = list(dirpath.rglob('*'))
    real_files = [f for f in files if f.is_file()]
    if not real_files:
        result.err("Structure", f"Directory is empty: {dirpath}")
        return

    result.ok("Structure", f"Directory contains {len(real_files)} files")

    has_index = any(f.name.lower() in ('readme.md', 'index.md', 'index.json') for f in real_files)
    if not has_index:
        result.warn("Structure", "No README.md or index file in directory")

    zero_byte = [f for f in real_files if f.stat().st_size == 0]
    if zero_byte:
        for f in zero_byte[:5]:
            result.err("Structure", f"Zero-byte file: {f.name}")
    else:
        result.ok("Structure", "No zero-byte files")


def format_text(result: Result) -> str:
    out = []

    for pass_name in ["Structure", "Hallucination", "Quality"]:
        items = [x for x in result.oks + result.warnings + result.errors if x["pass"] == pass_name]
        if not items:
            continue
        out.append(f"\n=== Pass: {pass_name} ===")
        for item in items:
            prefix = {"OK": "  OK ", "WARN": " WARN", "ERR": " ERR "}[item["level"]]
            out.append(f"  {prefix}  {item['msg']}")

    out.append(f"\nRESULT: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
    return '\n'.join(out)


def format_json(result: Result) -> str:
    return json.dumps({
        "errors": result.errors,
        "warnings": result.warnings,
        "oks": result.oks,
        "summary": {
            "error_count": len(result.errors),
            "warning_count": len(result.warnings),
            "ok_count": len(result.oks),
            "exit_code": result.exit_code,
        }
    }, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Validate deliverables after completion claims")
    parser.add_argument("path", help="File or directory to validate")
    parser.add_argument("--type", choices=["auto", "markdown", "sql", "code"], default="auto")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(f"ERR: Path not found: {args.path}", file=sys.stderr)
        sys.exit(2)

    result = Result()

    if target.is_dir():
        validate_directory(target, result)
        for f in sorted(target.rglob('*')):
            if f.is_file() and f.suffix.lower() in ('.md', '.sql', '.py', '.cpp', '.h', '.lua'):
                file_result = Result()
                run_file_validation(f, args.type, file_result)
                result.errors.extend(file_result.errors)
                result.warnings.extend(file_result.warnings)
                result.oks.extend(file_result.oks)
    else:
        run_file_validation(target, args.type, result)

    if args.strict:
        result.errors.extend(result.warnings)
        result.warnings = []

    if args.json:
        print(format_json(result))
    else:
        print(format_text(result))

    sys.exit(result.exit_code)


def run_file_validation(path: Path, type_hint: str, result: Result):
    ftype = type_hint if type_hint != "auto" else detect_type(path)
    text, lines = read_file(path)

    # Pass 1
    if ftype == 'markdown':
        pass1_markdown(lines, result)
    elif ftype == 'sql':
        pass1_sql(text, lines, result)
    elif ftype == 'code':
        pass1_code(text, lines, path, result)

    # Pass 2
    pass2_hallucination(text, lines, result)

    # Pass 3
    pass3_quality(text, lines, path, result)


if __name__ == "__main__":
    main()

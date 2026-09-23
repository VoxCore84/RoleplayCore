"""apply_edits.py — asserted exact-match edits from a JSON spec.

Why: the Bash tool re-escapes inline commands (backslashes, backticks, \\"),
so multi-file text edits are safest as a spec file applied by Python. Every
edit must match exactly once (or already be applied), files are read and
written as bytes (line endings preserved), and the run reports per edit.

Usage:
    python tools/apply_edits.py SPEC.json [--root DIR] [--dry-run]

SPEC.json is a list of objects:
    {"path": "rel/or/abs", "old": "...", "new": "...", "label": "what"}
    {"path": "...", "rewrite": "path/to/content.md", "label": "..."}   # whole-file replace
    {"path": "...", "append": "text", "unless": "marker", "label": "..."}  # append if marker absent

Exit 1 if any edit failed (0 or >1 matches). Idempotent: an edit whose `new`
text is already present and whose `old` is absent is reported as skipped.
"""
import argparse
import json
import os
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('spec')
    ap.add_argument('--root', default='.')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    spec = json.load(open(a.spec, encoding='utf-8'))
    failures = 0
    for e in spec:
        label = e.get('label') or e['path']
        p = e['path'] if os.path.isabs(e['path']) else os.path.join(a.root, e['path'])
        if not os.path.exists(p):
            print(f'[FAIL] {label}: missing {p}'); failures += 1; continue
        s = open(p, 'rb').read().decode('utf-8')
        if 'rewrite' in e:
            content = open(e['rewrite'], 'rb').read().decode('utf-8')
            if s == content:
                print(f'[skip] {label} (identical)'); continue
            if not a.dry_run:
                open(p, 'wb').write(content.encode('utf-8'))
            print(f'[ok]   {label} (rewritten)'); continue
        if 'append' in e:
            if e.get('unless') and e['unless'] in s:
                print(f'[skip] {label} (marker present)'); continue
            if not a.dry_run:
                open(p, 'wb').write((s.rstrip('\n') + '\n' + e['append']).encode('utf-8'))
            print(f'[ok]   {label} (appended)'); continue
        old, new = e['old'], e['new']
        if new in s and old not in s:
            print(f'[skip] {label} (already applied)'); continue
        n = s.count(old)
        if n != 1:
            print(f'[FAIL] {label}: old text found {n}x in {p}'); failures += 1; continue
        if not a.dry_run:
            open(p, 'wb').write(s.replace(old, new).encode('utf-8'))
        print(f'[ok]   {label}')
    print(f'\n{"DRY RUN — " if a.dry_run else ""}failures: {failures}')
    sys.exit(1 if failures else 0)


if __name__ == '__main__':
    main()

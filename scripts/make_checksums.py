#!/usr/bin/env python3
"""
make_checksums.py - SHA-256 for every file in a folder.

Usage:
    python make_checksums.py [folder]

Writes CHECKSUMS.csv: filename, size, sha256.
Defaults to the current folder. Skips itself and CHECKSUMS.csv.

Reads only.
"""
import sys, os, csv, hashlib, datetime

SKIP = {'CHECKSUMS.csv', 'make_checksums.py'}


def sha256(path, buf=1 << 20):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            b = f.read(buf)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    rows = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for fn in sorted(filenames):
            if fn in SKIP or fn.startswith('.'):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace('\\', '/')
            rows.append({
                'file': rel,
                'size_bytes': os.path.getsize(full),
                'sha256': sha256(full),
            })

    out = os.path.join(root, 'CHECKSUMS.csv')
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['file', 'size_bytes', 'sha256'])
        w.writeheader()
        w.writerows(rows)

    print(f"Generated {datetime.datetime.now().isoformat(timespec='seconds')}")
    for r in rows:
        print(f"{r['sha256']}  {r['size_bytes']:>12,}  {r['file']}")
    print(f"\nWROTE  {out}  ({len(rows)} files)")


if __name__ == '__main__':
    main()

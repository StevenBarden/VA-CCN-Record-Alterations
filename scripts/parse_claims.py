#!/usr/bin/env python3
"""
parse_claims.py - read Optum VA Community Care portal exports and write a CSV.

Usage:
    python parse_claims.py <file.pdf> [more.pdf ...]

Writes:
    claims.csv       one row per claim, per source file
    services.csv     one row per procedure line item

Prints the SHA-256 of every file it reads, so the output can be tied to
exactly the inputs that produced it.

Requires:
    pip install pymupdf

Reads only. Never modifies a source file.
"""
import sys, os, re, csv, hashlib

try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        print("Install PyMuPDF first:  pip install pymupdf")
        sys.exit(1)

CLAIM = re.compile(
    r'(Medical|Dental|Pharmacy)\s*Claim\s*#\s*(\S+)'
    r'[\s\S]{0,600}?Date of Service:\s*([0-9/ ]+)'
    r'[\s\S]{0,400}?Provider:\s*\n?\s*([^\n]+)'
    r'[\s\S]{0,300}?Submitted Date:\s*([0-9/ NA]+)'
    r'[\s\S]{0,300}?Amount Billed:\s*([^\n]+)',
    re.I)

CODE = re.compile(r'^\s*(D\d{4})\s*$', re.M)


def sha256(path, buf=1 << 20):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            b = f.read(buf)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def clean(s):
    return re.sub(r'\s+', ' ', s).strip()


def money(s):
    s = re.sub(r'[^0-9.]', '', s.replace(' ', ''))
    try:
        return float(s)
    except ValueError:
        return ''


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    claims, services = [], []

    for path in sys.argv[1:]:
        if not os.path.exists(path):
            print(f"NOT FOUND  {path}")
            continue

        name = os.path.basename(path)
        print("=" * 70)
        print(f"FILE      {name}")
        print(f"SIZE      {os.path.getsize(path):,} bytes")
        print(f"SHA-256   {sha256(path)}")

        doc = pymupdf.open(path)
        print(f"PAGES     {doc.page_count}")

        text = ''.join(doc[i].get_text() for i in range(doc.page_count))

        n = 0
        for m in CLAIM.finditer(text):
            n += 1
            claims.append({
                'source': name,
                'type': m.group(1).title(),
                'claim': m.group(2),
                'date_of_service': clean(m.group(3)),
                'provider': clean(m.group(4)),
                'submitted': clean(m.group(5)),
                'amount_billed': money(m.group(6)),
            })
            block = text[m.end(): m.end() + 4000]
            stop = CLAIM.search(block)
            if stop:
                block = block[:stop.start()]
            for c in CODE.findall(block):
                services.append({
                    'source': name,
                    'claim': m.group(2),
                    'code': c,
                })
        print(f"CLAIMS    {n}")

    with open('claims.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=[
            'source', 'type', 'claim', 'date_of_service',
            'provider', 'submitted', 'amount_billed'])
        w.writeheader()
        w.writerows(claims)

    with open('services.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['source', 'claim', 'code'])
        w.writeheader()
        w.writerows(services)

    print("=" * 70)
    print(f"WROTE  claims.csv   ({len(claims)} rows)")
    print(f"WROTE  services.csv ({len(services)} rows)")
    print()
    print("These files are extracted text. Before relying on any single row,")
    print("open the source PDF to the claim and read it.")


if __name__ == '__main__':
    main()

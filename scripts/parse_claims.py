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

--------------------------------------------------------------------------
PARSED MUST EQUAL STATED.

Each export prints its own result count on page one -- "135 Results",
"137 Results". This script reads that number, compares it to the number of
claims it actually parsed, and says so on every run. If the two disagree it
prints PARSE GAP and exits non-zero.

That check exists because this script was wrong. An earlier version of it
reported 134 claims for the 11 March 2024 export and 133 for the 28 November
2025 export, against printed totals of 135 and 137. Nothing was missing from
the records -- the pattern below required the claim header, date of service,
provider, submitted date and amount to all fall inside fixed character
windows, and a claim whose text ran longer than those windows was dropped
without a word. A parser that under-counts in silence is worse than no
parser, so it is no longer able to be silent.

Two things fixed:

  1. No character windows. The text is split on the claim headers and each
     claim's fields are read from its own block.

  2. Identifiers may contain spaces that the scan inserted -- "L 150XBR470000",
     "J 179XSMZH0000". A pattern demanding six contiguous characters matched
     only the leading letter and skipped the claim. The identifier is read to
     the end of the line and the spaces are stripped afterwards.
--------------------------------------------------------------------------
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

# The claim header. Everything up to the next header belongs to this claim.
# The identifier runs to the end of the line; scanner-inserted spaces are
# stripped after the match, never inside the pattern.
HEAD = re.compile(
    r'(Medical|Dental|Pharmacy)\s*Claim\s*#\s*([A-Za-z0-9][A-Za-z0-9 ]*)', re.I)

ID_MIN, ID_MAX = 6, 26

F_DOS = re.compile(r'Date of Service:\s*([0-9/ ]+)', re.I)
F_SUB = re.compile(r'Submitted Date:\s*([0-9/ NA]+)', re.I)
F_AMT = re.compile(r'Amount Billed:\s*([^\n]+)', re.I)
F_PROV = re.compile(r'Provider:\s*\n?\s*([^\n]+)', re.I)

# "135 Results" on page one
STATED = re.compile(r'([\d,]{1,6})\s*Results?', re.I)

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
    gaps = []

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

        stated = STATED.search(text)
        stated_n = int(stated.group(1).replace(',', '')) if stated else None

        heads = list(HEAD.finditer(text))
        n = 0
        rejected = []

        for i, m in enumerate(heads):
            raw = m.group(2).strip()
            cid = raw.replace(' ', '')
            if not (ID_MIN <= len(cid) <= ID_MAX):
                rejected.append(raw)
                continue

            start = m.end()
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            block = text[start:end]

            def g(rx):
                r = rx.search(block)
                return r.group(1) if r else ''

            n += 1
            claims.append({
                'source': name,
                'type': m.group(1).title(),
                'claim': cid,
                'date_of_service': clean(g(F_DOS)),
                'provider': clean(g(F_PROV)),
                'submitted': clean(g(F_SUB)),
                'amount_billed': money(g(F_AMT)),
            })

            for c in CODE.findall(block):
                services.append({'source': name, 'claim': cid, 'code': c})

        print(f"STATED    {stated_n if stated_n is not None else '?'}   (printed on page one)")
        print(f"PARSED    {n}")

        if rejected:
            print(f"REJECTED  {len(rejected)} header(s) on identifier length: {rejected[:5]}")

        if stated_n is None:
            print("CHECK     no printed result count found -- cannot verify")
        elif stated_n == n:
            print("CHECK     OK -- parsed equals stated")
        else:
            print(f"CHECK     *** PARSE GAP *** stated {stated_n}, parsed {n}")
            gaps.append((name, stated_n, n))

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

    if gaps:
        print()
        print("PARSE GAP on:")
        for name, s, p in gaps:
            print(f"  {name}: page says {s}, parser read {p}")
        print("The parser lost blocks. Nothing is missing from the records.")
        print("Do not rely on these counts until the gap is closed.")
        sys.exit(1)

    print()
    print("Parsed equals stated on every file.")


if __name__ == '__main__':
    main()

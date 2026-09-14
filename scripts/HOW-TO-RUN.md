# How to check this yourself

You do not have to take my word for anything here. Three commands.

## 1. Install Python and one library

Python 3.9 or newer, from python.org. Then:

```
pip install pymupdf
```

## 2. Read the exports

From the folder holding the PDFs:

```
python scripts/parse_claims.py *.pdf
```

This prints the SHA-256 of every file it reads and writes two files:

- `claims.csv` — one row per claim, per source export
- `services.csv` — one row per procedure code

## 3. Verify the files have not changed

```
python scripts/make_checksums.py
```

Compare the output against `CHECKSUMS.csv` in this repository. If a line
differs, the file differs.

---

## What to look at

Open `claims.csv` in a spreadsheet and sort by claim number.

A claim that appears in one export and not another, or that carries a
different date or amount between exports, will sit on adjacent rows.

## A caution about the output

`claims.csv` and `services.csv` are extracted text. Optical character
recognition and text extraction both make mistakes — a trailing zero read
as a one, a dollar amount mangled.

**Before relying on any single row, open the source PDF and read the page.**
I made that mistake myself while assembling this, and that is why the
warning is here.

The scripts read only. They do not modify the PDFs.

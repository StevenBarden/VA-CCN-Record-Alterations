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

**It also checks itself.** Each export prints its own result count on its
first page. The script reads that number, compares it to the number of
claims it actually parsed, and prints both on every run:

```
STATED    135   (printed on page one)
PARSED    135
CHECK     OK -- parsed equals stated
```

If those two numbers disagree it prints `*** PARSE GAP ***` and exits
non-zero. A gap means the parser lost blocks — it does not mean claims are
missing from the records, and the counts should not be relied on until it
is closed.

Expected output on the three exports published here:

| File | Stated | Parsed |
|---|---|---|
| `Reference 01 - Optum OCR 20240311.pdf` | 135 | 135 |
| `Reference 02 - Optum OCR 20251128.pdf` | 137 | 137 |
| `Reference 03 - Optum OCR 20251214.pdf` | 18 | 18 |

Sorting `claims.csv` by type gives 122 medical and 13 dental in the first
export, and 115 medical and 22 dental in the second. Those are the figures
quoted in the README.

## 3. Verify the files have not changed

```
python scripts/make_checksums.py
```

Compare the output against `SHA256SUMS.txt` in this repository. If a line
differs, the file differs.

On Windows you can also run `Get-FileHash -Algorithm SHA256 "<filename>"`.
On macOS or Linux, `sha256sum -c "<filename>.sha256"`.

---

## What to look at

Open `claims.csv` in a spreadsheet and sort by claim number.

A claim that appears in one export and not another, or that carries a
different date or amount between exports, will sit on adjacent rows.

## A caution about the output

`claims.csv` and `services.csv` are extracted text. Optical character
recognition and text extraction both make mistakes — a trailing zero read
as a one, a dollar amount mangled, a space dropped into the middle of a
claim number.

**Before relying on any single row, open the source PDF and read the page.**
I made that mistake myself while assembling this, and that is why the
warning is here.

## This script was wrong, and that is why it now checks itself

An earlier version of `parse_claims.py` reported 134 claims for the
11 March 2024 export and 133 for the 28 November 2025 export, against
printed totals of 135 and 137. It printed those numbers without comment.

Nothing was missing from the records. The pattern required a claim's header,
date of service, provider, submitted date and amount to all fall inside
fixed character windows, and any claim whose text ran longer was dropped
silently. Separately, some claim numbers carry spaces inserted by the
scanner — `L 150XBR470000` — and a pattern demanding unbroken characters
matched only the leading letter and skipped the claim.

Both are fixed. The stated-versus-parsed check was added so that a failure
of this kind cannot be silent again. The reasoning is written into the top
of the script so it does not get undone.

The scripts read only. They do not modify the PDFs.

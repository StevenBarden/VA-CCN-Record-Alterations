# Document Guide

Every file in this repository has a companion `.sha256` checksum, and `SHA256SUMS.txt` lists them all. On Windows: `Get-FileHash -Algorithm SHA256 "<filename>"`. On macOS or Linux: `sha256sum -c "<filename>.sha256"`. The date each file was published is in this repository's commit history.

Below, one section per document: what it is, where it came from, what it shows, what it does not show, and how to verify it.

---

## Reference 01 — Optum OCR 20240311.pdf

**What it is.** A capture of my own claims history from the Optum VA Community Care Network veteran portal, taken on 11 March 2024. Forty pages.

**Where it came from.** My own portal account. No filter. The first page states the result count: **135 Results**.

**What it shows.** The complete claims history as Optum presented it to me on that date. It is the earliest of the three captures and the baseline the other two are compared against. It contains the $6,568.00 claim under its original identifier, the four D7310 alveoloplasty line items at $386.00 each, the September and November 2021 hospital admissions, and four separate submissions of one InPhyNet date of service.

**What it does not show.** This is a patient-facing portal view, not a VA record and not adjudicated-payment data. Amounts shown are as billed. What was actually paid is established by the Explanations of Benefit, which are not in this repository.

**How to verify.** `Reference 01 - Optum OCR 20240311.pdf.sha256`, or `SHA256SUMS.txt`. `scripts/parse_claims.py` regenerates the counts.

---

## Reference 02 — Optum OCR 20251128.pdf

**What it is.** The same claims history from the same portal account, captured 28 November 2025 — twenty months later. Forty-four pages.

**Where it came from.** My own portal account. No filter. The first page states **137 Results**.

**What it shows.** What the same account contained twenty months later. Both this file and Reference 01 state their own totals and neither is filtered, which is what makes them comparable.

Against Reference 01: medical claims fall from 122 to 115; dental claims rise from 13 to 22, which is expected. The $6,568.00 claim is absent. The four D7310 line items are absent. The September 2021 hospital admission is absent — the date 09/06/2021 occurs five times in Reference 01 and zero times here. The D7320 alveoloplasty billed in March 2024 appears here for the first time.

**What it does not show.** Same caveat as Reference 01 — portal view, billed amounts. It also does not explain any of the differences. It is one of two observations.

**How to verify.** `Reference 02 - Optum OCR 20251128.pdf.sha256`. The counts are reproducible with `scripts/parse_claims.py`.

---

## Reference 03 — Optum OCR 20251214.pdf

**What it is.** A third capture of the same account, 14 December 2025. Nine pages.

**Where it came from.** My own portal account, **filtered to dental claims with a paid status**. The first page states **18 Results**. The filter is stated here because it matters: this file is not comparable to the other two on volume, only on content.

This was captured during the session in which portal access was lost. Access has not been restored and no further attempt has been made.

**What it shows.** The $6,568.00 claim, absent from Reference 02, is present again — identifier ending 0001 rather than 0000, submitted date 10/01/2024 rather than 10/18/2022, and a facility name where the field previously read N/A. The procedure contents are identical to the original. The four D7310 line items are present again. Both $4,775.00 denture claims appear.

Because this export is filtered to **paid** claims, everything in it was paid.

**What it does not show.** It is filtered, so nothing can be concluded from a claim's absence here. No medical claim appears, so no medical claim has a third observation.

**How to verify.** `Reference 03 - Optum OCR 20251214.pdf.sha256`.

---

## Optum-Record-Alterations-Evidence-v3.pdf

**What it is.** The compiled exhibit. Forty-five pages: a summary of the findings, then the source pages themselves grouped by finding, each group preceded by a divider page explaining what to look for and which export it came from.

**Where it came from.** Assembled by me from the three Reference exports. **No source page has been edited, cropped, redacted or re-rendered.** Only the divider pages were created for the compilation.

**What it shows.** Six findings, each traced to a page in a Reference export.

**What it does not show.** It asserts no intent and reaches no conclusion about cause. Two items of its wording are stronger than the record supports and are superseded by the README: its page 2 heading, and its description of the interval as "nearly two years" — the interval is eighteen months. Where this exhibit and the README's Corrections section disagree, the README governs.

**How to verify.** Every page citation in this document points at a page in Reference 01, 02 or 03, which are in this repository. Check any of them directly.

---

## Optum-Claim-Index-v1.xlsx

**What it is.** The same material as a working spreadsheet — one row per claim.

**Where it came from.** Built by me from the three Reference exports.

**What it shows.** A separate column for each export, so a claim's presence or absence can be filtered directly rather than read across three PDFs. A second sheet, *Legend and Sources*, explains every column and states the caveats.

**What it does not show.** It is a derived index, not a source. Where the spreadsheet and a Reference export disagree, **the export is correct**. Nothing in this file should be relied on without checking the underlying page.

**How to verify.** `Optum-Claim-Index-v1.xlsx.sha256`, and every row cites the export it came from.

---

## Barden - Steven - 033026 Optum VA CCN Government Relations Response.pdf

**What it is.** Optum's written response to a congressional inquiry, 30 March 2026. Two pages, addressed to Senator Ashley Moody, signed by Optum's Congressional Inquiry Department.

**Where it came from.** The Senator's office. It was not sent to me; I have it because the office forwarded it.

**What it shows.** In Optum's own words: that its Payment Integrity department confirmed receipt of a fraud, waste and abuse report in September 2024; that its Clinical Quality department confirmed receipt of two quality referrals, on 27 March 2024 and 10 September 2024; that *"Optum properly reports all findings related to both FWA and PQI investigations to the Department of Veterans Affairs as contractually required"*; that this letter *"will serve as the only formal communication"* on either investigation; and that my portal account *"is active and does not appear locked as of March 27, 2026."*

**What it does not show.** It does not address the claims data. It states no finding or outcome. The portal statement describes an account status checked on one date; it is not an access log and does not speak to what happened on 15 December 2025.

**How to verify.** The letter carries Optum's own Letter ID on both pages. The Senator's office holds the original.

---

## Barden - Steven - 050526 Optum VA CCN Government Relations response.pdf

**What it is.** Optum's response to the Senator's follow-up questions, 5 May 2026. Two pages, same office, answers printed in blue beneath each question.

**Where it came from.** The Senator's office.

**What it shows.** Three answers, in Optum's own words:

- *"A Veteran who submits a potential fraud tip is not considered directly involved in Optum's Program Integrity Department's investigation."*
- *"PQI submissions are reviewed internally by Optum's Clinical Quality Team and Veterans are not involved in the review or investigation process."*
- *"When a Potential Quality Issue (PQI) Reporting Form is submitted, a confirmation of receipt is not sent to the submitter. Additionally, the outcomes of Clinical Quality reviews are not shared with Veterans."*

Read with the 30 March letter: the person who reports is not a participant, receives no confirmation, receives no outcome, and one letter is the only communication that will issue.

**What it does not show.** It does not say the reports were mishandled. It describes what is disclosed, not what was found.

**How to verify.** Letter ID on both pages. The Senator's office holds the original.

---

## scripts/

**What it is.** Short Python scripts and instructions, so that any reader can regenerate the figures rather than take them on trust.

**Where it came from.** Written for this repository.

**What it shows.** `parse_claims.py` reads the three Reference exports and prints the claim counts. `make_checksums.py` prints the SHA-256 of every file it reads. `HOW-TO-RUN.md` is written for someone who has never installed Python.

**What it does not show.** The scripts read the PDF text layer, which can differ from the printed page. Every figure that matters has also been checked against the page image. **Matching claim identifiers across exports by text comparison is not reliable and is not done here** — optical character recognition alone produces dozens of false differences.

**How to verify.** Run them.

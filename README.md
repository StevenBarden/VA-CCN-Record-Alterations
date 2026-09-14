# Optum VA CCN — Record Alterations

Steven Barden — Optum VA Community Care Network, Region 3, contract 36C79119D0006

Three exports of one Optum VA CCN account, taken across twenty-one months. They do not agree with each other.

An SF95 administrative claim has been filed. Complaints were submitted to the VA Office of Inspector General and the FBI on 15 December 2025; no response was received from either. No qui tam complaint and no lawsuit.

---

## Read in this order

**1. `Optum-Record-Alterations-Evidence-v3.pdf`** — start here.

Forty-five pages. A one-page summary of the findings, followed by the source pages themselves, grouped by finding, each preceded by a page explaining what to look for and which export it came from. A claim index and a provenance statement close it out.

No source page has been edited, cropped, redacted or re-rendered. Only the divider pages were created for the compilation.

**2. `Optum-Claim-Index-v1.xlsx`** — the same material as a working spreadsheet.

Eighty-seven claims. Separate columns for each export so a claim's presence or absence can be filtered directly. Flags for claims absent from the second export and for claims over $5,000. A legend sheet explains the columns and states the caveats.

**3. The three source exports** — the raw material, unmodified.

| File | Pulled | Results | Filter |
|---|---|---|---|
| `Reference 01 - Optum OCR 20240311.pdf` | 11 March 2024 | 135 | none |
| `Reference 02 - Optum OCR 20251128.pdf` | 28 November 2025 | 137 | none |
| `Reference 03 - Optum OCR 20251214.pdf` | 14 December 2025 | 18 | dental, paid only |

Reference 03 was captured during the session in which portal access was lost. Access has not been restored and no further attempt has been made.

**4. The correspondence.**

| File | Date | From |
|---|---|---|
| `Barden - Steven - 033026 Optum VA CCN Government Relations Response.pdf` | 30 March 2026 | Optum |
| `Barden - Steven - 042726 JAHVA Response.pdf` | 27 April 2026 | James A. Haley VA Hospital |
| `Barden - Steven - 050526 Optum VA CCN Government Relations response.pdf` | 5 May 2026 | Optum |

These are the replies to questions put to Optum by the office of Senator Ashley Moody. The March 30 letter contains the assertion that the portal account was active and not locked as of 27 March 2026, which the exports contradict. The May 5 letter invokes 38 C.F.R. § 5705 as the basis for withholding, and states that it will serve as the only formal communication on the matter.

**5. `scripts/`** — read the exports yourself.

See `scripts/HOW-TO-RUN.md`. Three commands. The scripts print the SHA-256 of every file they read, so the output can be tied to exactly these files.

---

## What the exports show

**A claim deleted and rebuilt.** $6,568.00, Green, James Russell IV, date of service 13 September 2022. Present in the first export, identifier ending 0000, submitted 10/18/2022. Absent entirely from the second. Present in the third, identifier ending 0001, submitted date 10/01/2024, with a facility name added. Procedure contents identical. The third export is filtered to paid claims.

**A procedure billed and not performed.** The companion claim, $8,217.00, date of service 11 September 2022, carries four alveoloplasty line items at $386.00 each — **D7310, "alveoloplasty in conjunction with extractions, 4+ teeth or tooth spaces, per quadrant."**

The alveoloplasty was performed eighteen months later, on 29 March 2024, by a different surgeon — claim `24122W393626020000`, Christian, David Joseph, $3,240.00. It is billed there as **D7320, "alveoloplasty not in conjunction with extractions,"** four quadrants at $125.00. D7320 is the code that applies when the procedure is performed on its own rather than alongside extractions.

Both claims reconcile exactly to their billed totals.

The four D7310 line items are present in the first export, absent from the second, and present again in the third.

**The same identifier change on a hospital bill.** Tampa General Hospital, $19,648.23, date of service 6 June 2021. Identifier ends 0000 in the first export and 0001 in the second. Date of service, submitted date, amount and provider are unchanged. Different provider, different service line, no connection to the dental matter.

**An entire hospital admission removed.** The September 2021 admission — ten claims across three days including $40,762.62 to Tampa General Hospital — appears in the first export and nowhere in the second. The date 09/06/2021 occurs five times in the first file and zero times in the second. The November 2021 admission is likewise absent. Twenty-five claims in total are present in the first complete export and absent from the second.

**Duplicate submissions across four providers.** Same date of service, submitted repeatedly under different identifiers. InPhyNet Contracting four times at $2,337.00 across six and a half months. Perez three times. Khalil three times. Davila twice.

**Two identical denture claims, both paid.** Ackley, Andrea. Same service date, same $4,775.00, same procedure codes, same line-item amounts, submitted fifty-two days apart. Both appear in the paid-filtered export. $9,550.00 for one set of dentures.

---

## Precision

Only the Green claim is observed to disappear and return. The third export is filtered to dental claims, so no medical claim has a third observation. The hospital claims above are established as present in the first export and absent from the second. Nothing further is asserted about them.

All amounts are as billed. Amounts actually paid will differ and are established by the Explanations of Benefit, which are not included here.

Two items should be confirmed visually against the original PDFs before being relied on in a filing: the H170X045X identifier change, and the absence of the four alveoloplasty line items from claim 22262W207984320000 in the second export.

Nothing here asserts intent. The question being asked is what these records mean.

---

## Corrections

I have written things about this matter that later proved wrong, and I have corrected them rather than removing them.

In a complaint filed 15 December 2025 I stated that the corrective alveoloplasty was performed on 23 August 2024, twenty-three months after it was billed. That was wrong. I had merged two separate procedures. The alveoloplasty was 29 March 2024 — eighteen months. The August 2024 claim is `24235W437304320000`, D6010 surgical placement of implant body, which is the implant work, not the alveoloplasty.

Where anything I have said earlier conflicts with what is here, what is here is current.

---

## Still being gathered

The following exist and are being assembled. They are not in this repository yet.

- The signed Optum VA CCN dispute and complaint form, dated 21 March 2024. This establishes that the billing was reported to Optum before the records changed.
- Correspondence to the VA implant board, September 2024, stating the original treatment plan and reporting the missing alveoloplasty.
- The complete VA medical record, Blue Button export, multiple versions taken on different dates.
- Secure messages spanning several years.
- The Explanations of Benefit for the claims listed in the spreadsheet.

Available immediately on request.

---

Steven Barden
Bradenton, Florida
steven.barden@outlook.com

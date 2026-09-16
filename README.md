# Optum VA CCN — Record Alterations

Steven Barden — Optum VA Community Care Network, Region 3, contract 36C79119D0006

Three exports of one Optum VA CCN account, taken across twenty-one months. They do not agree with each other.

Complaints were submitted to the VA Office of Inspector General and the FBI on 15 December 2025; no response has been received. No qui tam complaint and no lawsuit.

---

## Publication log

| Batch | Published | What went up |
|---|---|---|
| **1** | **16 September 2026** | The three source exports · both Optum letters to Senator Moody · the compiled exhibit · the claim index · the scripts · SHA-256 checksums for every file |

Each batch is a dated row here and a timestamped commit in this repository's public history. **Nothing is ever removed.** Later batches add; where later material corrects something earlier, the correction is added beside it and dated.

Every file is checksummed and the commit history is public, so any change to what is published here — **including by me** — is visible to anyone who checks.

---

## What this is about, and what it is not

**This concerns UnitedHealth Group and Optum, the contractor administering VA Community Care Network Region 3, and the records it produced.** That is the whole subject.

I do not believe this is how the VA operates, and the Department of Veterans Affairs is the payer here — these claims were submitted to VA's contractor and paid with public money.

This is not unique. VA's Office of Inspector General identified **$325.5 million in unauthorized community care dental procedures across 847,800 procedures** in FY2022 through FY2025 — report 23-00749-171, 8 August 2024. That figure describes billing. **What happened to me is not a billing figure and I am not presenting it as one.**

It does not concern the people inside these organizations who do this work properly, and there are many of them. Nothing here should be read as a judgment on an organization as a whole.

I am not an auditor and this is not an audit. I am a patient who kept his own records and read them.

---

## This record set is current, and it is continuing

**Current as of 16 September 2026. It is not complete, and it is not presented as complete.**

Further material is under review: additional captures of this same account taken on other dates, records from a separate facility, and the Explanations of Benefit for the claims listed here. None of it is published yet, for one reason — it has not been verified to the standard applied to what is here.

That standard is stated so it can be checked: every figure in this repository has been read against the page it came from, not inferred from a text search, and the scripts that reproduce the counts are included. Two earlier findings of mine failed that check and were withdrawn; both withdrawals are recorded below rather than deleted.

Material will be added as it clears the same check. **Nothing already published will be removed.** Where later material corrects something here, the correction will be added alongside it and dated. Each addition appears in the publication log above and as a timestamped commit.

---

## Read in this order

**1. `Optum-Record-Alterations-Evidence-v3.pdf`** — start here.

Forty-five pages. A one-page summary of the findings, followed by the source pages themselves, grouped by finding, each preceded by a page explaining what to look for and which export it came from.

No source page has been edited, cropped, redacted or re-rendered. Only the divider pages were created for the compilation.

**2. `Optum-Claim-Index-v1.xlsx`** — the same material as a working spreadsheet.

Separate columns for each export so a claim's presence or absence can be filtered directly. A legend sheet explains the columns and states the caveats.

**3. The three source exports** — the raw material, unmodified.

| File | Pulled | Results | Filter |
|---|---|---|---|
| `Reference 01 - Optum OCR 20240311.pdf` | 11 March 2024 | 135 | none |
| `Reference 02 - Optum OCR 20251128.pdf` | 28 November 2025 | 137 | none |
| `Reference 03 - Optum OCR 20251214.pdf` | 14 December 2025 | 18 | dental, paid only |

Each file states its own result count on its first page.

Reference 03 was captured during the session in which portal access was lost. Access has not been restored and no further attempt has been made.

**4. The correspondence.**

| File | Date | From |
|---|---|---|
| `Barden - Steven - 033026 Optum VA CCN Government Relations Response.pdf` | 30 March 2026 | Optum |
| `Barden - Steven - 050526 Optum VA CCN Government Relations response.pdf` | 5 May 2026 | Optum |

These are Optum's replies to questions put to it by the office of Senator Ashley Moody.

The 30 March letter confirms receipt of a fraud, waste and abuse report in September 2024 and two quality referrals on 27 March 2024 and 10 September 2024, states that Optum reports all such findings to the Department of Veterans Affairs as contractually required, and states that the portal account was active and not locked as of 27 March 2026.

The 5 May letter answers the Senator's follow-up questions. It states that a veteran who submits a fraud report is not considered directly involved in the investigation, that veterans are not involved in the quality review, that no confirmation of receipt is sent, and that outcomes are not shared. The 30 March letter states it will serve as the only formal communication on the matter.

**Optum's letters confirm in writing to a United States Senator that the referrals exist, and give their dates. The same letters state that the person who filed them will not be told what came of them.**

Both letters cite "38 C.F.R § 5705" as the basis for withholding.

**5. `scripts/`** — read the exports yourself. See `scripts/HOW-TO-RUN.md`.

**6. `DOCUMENT-GUIDE.md`** — what every file here is: where it came from, what it shows, what it does not show, and how to verify it.

---

## What the exports show

**A claim deleted and rebuilt.** $6,568.00, Green, James Russell IV, date of service 13 September 2022. Present in the first export, identifier ending 0000, submitted 10/18/2022, facility field N/A. Absent entirely from the second. Present in the third, identifier ending 0001, submitted date 10/01/2024, with a facility name added. Procedure contents identical. The third export is filtered to paid claims.

**The same work billed under two codes, eighteen months apart.** The companion claim, $8,217.00, date of service 11 September 2022, carries four alveoloplasty line items at $386.00 each — **D7310, "alveoloplasty in conjunction with extractions, 4+ teeth or tooth spaces, per quadrant."**

The alveoloplasty was performed eighteen months later, on 29 March 2024, by a different surgeon — claim `24122W393626020000`, Christian, David Joseph, $3,240.00. It is billed there as **D7320, "alveoloplasty not in conjunction with extractions,"** four quadrants at $125.00. D7320 is the code that applies when the procedure is performed on its own rather than alongside extractions.

Both claims reconcile exactly to their billed totals.

The four D7310 line items are present in the first export, absent from the second, and present again in the third.

**The same identifier change on a hospital bill.** Tampa General Hospital, $19,648.23, date of service 6 June 2021. Identifier ends 0000 in the first export and 0001 in the second. Date of service, submitted date, amount and provider are unchanged. Different provider, different service line, no connection to the dental matter.

**An entire hospital admission removed.** The September 2021 admission — ten claims across three days including $40,762.62 to Tampa General Hospital — appears in the first export and nowhere in the second. The date 09/06/2021 occurs five times in the first file and zero times in the second. The November 2021 admission is likewise absent.

Between the two complete exports, medical claims fall from 122 to 115. Dental claims rise from 13 to 22, which is expected — there was dental work in between. Medical claims from 2021 cannot decrease.

**Repeated submissions of one date of service.** InPhyNet Contracting, $2,337.00, date of service 6 June 2021, submitted four separate times — 4 August 2021, 7 October 2021, 29 November 2021 and 16 February 2022. **All four are marked Denied. None was paid.** The record does not show what the provider was told after any of the four.

**Two identical denture claims, both paid.** Ackley, Andrea. Same date of service 17 June 2024, same $4,775.00, same procedure codes, same line-item amounts, submitted 18 June 2024 and 9 August 2024 — fifty-two days apart. Both appear in the paid-filtered export. $9,550.00 for one set of dentures.

---

## Integrity

Every file here has a companion `.sha256` checksum, and `SHA256SUMS.txt` lists them all, so any reader can confirm that what they downloaded is what was published.

On Windows: `Get-FileHash -Algorithm SHA256 "<filename>"`. On macOS or Linux: `sha256sum -c "<filename>.sha256"`. The date each file was published is in this repository's commit history.

**The source documents are published as received.** Nothing has been removed, redacted or reformatted — including my own Optum member ID, which appears on my records. Altering a source document, for any reason, would defeat the purpose of publishing it.

---

## Terms

| Term | Meaning |
|---|---|
| CCN | Community Care Network — the program that sends veterans to non-VA providers |
| Region 3 | Florida and the southeast |
| Third-party administrator | The company paid to run a region, build the provider network and process claims. Region 3 is Optum |
| 36C79119D0006 | The current Region 3 CCN contract |
| 36C10G26R0004 | The successor dental solicitation, VA Strategic Acquisition Center |
| SEOC | Standardized Episode of Care — the set of codes a referral authorizes |
| Alveoloplasty | Reshaping the jawbone after teeth are removed, so a denture can seat |
| D7310 | The code used when that bone work is done **during** the extraction surgery |
| D7320 | The code used when it is done **on its own**, separately |
| Quadrant | One of the four corners of the mouth. Billed per quadrant |
| FWA | Fraud, Waste and Abuse — the contractor's own reporting channel |
| PQI | Potential Quality Issue — the contractor's clinical-quality referral |

---

## Precision

Only the Green claim is observed to disappear and return. The third export is filtered to dental claims, so no medical claim has a third observation. The hospital claims above are established as present in the first export and absent from the second. Nothing further is asserted about them.

All amounts are as billed. Amounts actually paid will differ and are established by the Explanations of Benefit, which are not included here.

The figure of $1,544.00 does not appear in any source document. It is four printed line items at $386.00 each.

Matching claim identifiers across exports by text comparison is not reliable — optical character recognition alone produces dozens of false differences, and it produced two false findings of mine before it was caught. Every comparison stated above was confirmed by reading the rendered page.

Nothing here asserts intent. The question being asked is what these records mean.

---

## Corrections

I have written things about this matter that later proved wrong, and I have corrected them rather than removing them.

In a complaint filed 15 December 2025 I stated that the corrective alveoloplasty was performed on 23 August 2024, twenty-three months after it was billed. That was wrong. I had merged two separate procedures. The alveoloplasty was 29 March 2024 — eighteen months. The August 2024 claim is `24235W437304320000`, D6010 surgical placement of implant body, which is the implant work, not the alveoloplasty.

I previously stated that twenty-five claims present in the first complete export were absent from the second. That figure came from matching identifiers across exports and is not supportable. The defensible statement is the one above: medical claims fall from 122 to 115.

I previously described repeated submissions by one provider without noting that all four were denied. They were. That is stated above.

Where anything I have said earlier conflicts with what is here, what is here is current.

---

## Still being gathered

These exist and are being assembled. They are not in this repository yet.

- The signed Optum VA CCN dispute and complaint form, dated 21 March 2024. This establishes that the billing was reported to Optum before the records changed.
- Correspondence to the implant board, September 2024, stating the original treatment plan and reporting the missing alveoloplasty.
- Additional captures of this same account taken on other dates.
- My complete medical record, Blue Button export, multiple versions taken on different dates.
- The Explanations of Benefit for the claims listed in the spreadsheet.

Available immediately on request.

---

Steven Barden  
Bradenton, Florida  
steven.barden@outlook.com

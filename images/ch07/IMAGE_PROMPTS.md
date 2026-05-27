# Chapter 7 – Image Generation Prompts

## Image 1: Bank Reconciliation Framework
- **Filename**: `fig7-1.png` (bank-reconciliation-framework)
- **Used in**: Section 8 (Bank Reconciliation: Summary Framework), Figure 7-1
- **Description**: A comprehensive diagram showing the complete bank reconciliation structure — Bank side and Book side flowing down to the same "Correct Cash Balance."

### GPT/Gemini Prompt:
```
Create a clean, professional educational diagram for an introductory accounting textbook showing the complete bank reconciliation structure. Use a modern flat design with a white background.

The diagram should show two parallel columns side by side:

LEFT COLUMN (Bank Side) — use a blue color scheme (#1565c0 header):
- Top box: "Ending Balance per BANK STATEMENT" (blue background, white text)
- Below it, a vertical flow:
  - "+ Deposits in Transit" (green text with + sign)
  - "− Outstanding Checks" (red text with − sign)
  - "+/− Bank Errors" (orange text)
- Arrow pointing down to bottom box

RIGHT COLUMN (Book Side) — use a green color scheme (#2e7d32 header):
- Top box: "Ending Balance per BOOKS" (green background, white text)
- Below it, a vertical flow:
  - "+ Bank Collections" (green text)
  - "+ EFT Receipts" (green text)
  - "+ Interest Revenue" (green text)
  - "− Service Charges" (red text)
  - "− NSF Checks" (red text)
  - "− EFT Payments" (red text)
  - "+/− Book Errors" (orange text)
- Arrow pointing down to bottom box

BOTTOM: Both columns converge into a single highlighted box at the center bottom:
- "CORRECT (ADJUSTED) CASH BALANCE" (dark navy background #1a3a5c, white text, bold)
- A "=" sign or "Must be equal" label connecting the two arrows

Add a callout note at the bottom right: "★ Only BOOK side items require journal entries"

Style: Clean, professional, suitable for a college textbook. No decorative elements. Use clear sans-serif fonts. The diagram should be approximately 900×600 pixels.
```

---

## Image 2: Internal Control Objectives
- **Filename**: `fig7-2.png` (internal-control-objectives)
- **Used in**: Section 1 (What Is Internal Control?), optional supplementary figure
- **Description**: A visual showing the four objectives of internal control radiating from a central "Internal Control" hub.

### GPT/Gemini Prompt:
```
Create a clean, professional educational diagram for an introductory accounting textbook showing the four objectives of internal control.

Design: A central circle or shield icon labeled "INTERNAL CONTROL" in dark navy (#1a3a5c), with four branches radiating outward to four rounded rectangles:

1. Top-left: "Safeguard Assets" — with a small lock/shield icon, light blue background
2. Top-right: "Encourage Policy Compliance" — with a small checklist icon, light green background
3. Bottom-left: "Promote Operational Efficiency" — with a small gear/speedometer icon, light orange background
4. Bottom-right: "Ensure Accurate Records" — with a small ledger/document icon, light purple background

Each rectangle should have the objective title in bold and a one-line subtitle:
1. "Protect company resources from theft and waste"
2. "Ensure employees follow company procedures"
3. "Reduce waste and maximize productivity"
4. "Maintain reliable financial information"

Style: Modern flat design, white background, clean sans-serif fonts, professional and suitable for a college textbook. Approximately 800×500 pixels.
```

---

## Image 3: Bank Statement Components
- **Filename**: `fig7-3.png` (bank-statement-components)
- **Used in**: Section 4 (The Bank Statement), optional supplementary figure
- **Description**: An annotated illustration of a sample bank statement showing key components (beginning/ending balance, deposits, checks cleared, debit/credit memos).

### GPT/Gemini Prompt:
```
Create a clean, professional illustration of a simplified bank statement for an introductory accounting textbook. White background, modern flat design.

Show a stylized bank statement document with the following clearly labeled sections:

HEADER:
- Bank name: "First National Bank"
- Account holder: "Laird Company"
- Statement period: "April 1 – April 30, 2026"

BODY (simplified table format):
- Beginning Balance: $5,900
- Deposits and Credits section: show 2-3 line items (deposits, EFT receipt, interest earned) — highlight "CM" (Credit Memorandum) labels
- Checks and Debits section: show 2-3 line items (cleared checks, service charge, NSF check) — highlight "DM" (Debit Memorandum) labels
- Ending Balance: $12,720

ANNOTATIONS (callout arrows pointing to relevant parts):
1. Arrow to deposits → "Credit Memorandum (CM): Increases your account"
2. Arrow to service charge → "Debit Memorandum (DM): Decreases your account"
3. Arrow to ending balance → "Compare this to your Cash ledger balance"

Color scheme: Professional blue tones (#1a3a5c, #2b579a). Use green for credit items, red for debit items. Clean sans-serif fonts. Approximately 850×550 pixels.
```

---

## Image 4: Journal Entries Flow from Bank Reconciliation
- **Filename**: `fig7-4.png` (recon-journal-entry-flow)
- **Used in**: Section 10 (Journal Entries from the Bank Reconciliation), optional supplementary figure
- **Description**: A flowchart showing that only Book side items flow into journal entries, while Bank side items do not.

### GPT/Gemini Prompt:
```
Create a clean, professional flowchart for an introductory accounting textbook illustrating which bank reconciliation items require journal entries.

Layout: Two paths diverging from a bank reconciliation document icon at the top.

LEFT PATH (Bank Side) — Blue color scheme:
- Box: "Bank Side Adjustments"
- Items listed: "Deposits in Transit, Outstanding Checks, Bank Errors"
- Arrow pointing down to:
- Red X mark or stop sign with text: "NO Journal Entry Needed"
- Small note: "Already recorded in company's books"

RIGHT PATH (Book Side) — Green color scheme:
- Box: "Book Side Adjustments"
- Items listed: "Bank Collections, EFT, Service Charges, NSF Checks, Interest, Book Errors"
- Arrow pointing down to:
- Green checkmark with text: "JOURNAL ENTRIES REQUIRED"
- Arrow continuing down to:
- Box: "Post to General Ledger" with an icon of a T-account or ledger book
- Arrow continuing down to:
- Box: "Cash ledger balance = Adjusted balance" (highlighted in gold/yellow)

Style: Modern flat design, white background, clear visual hierarchy. Use sans-serif fonts. Color code consistently (blue for bank, green for book). Approximately 700×800 pixels.
```

---

## Priority Summary

| # | Image | Status | Priority |
|---|-------|--------|----------|
| 1 | fig7-1.png (bank-reconciliation-framework) | Needed | **High** — Referenced in HTML as Figure 7-1 |
| 2 | fig7-2.png (internal-control-objectives) | Optional | Medium — Enhances Section 1 |
| 3 | fig7-3.png (bank-statement-components) | Optional | Medium — Enhances Section 4 |
| 4 | fig7-4.png (recon-journal-entry-flow) | Optional | Medium — Enhances Section 10 |

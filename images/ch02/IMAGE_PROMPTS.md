# Chapter 2 — Image Generation Prompts

**공통 스타일 지침 (모든 이미지에 적용):**
- Clean, modern textbook illustration style
- White or very light gray background
- Sans-serif font (e.g., Arial, Helvetica)
- Color scheme: navy blue (#1a3a5c) primary, medium blue (#2b579a) secondary, red (#c0392b) accent
- No decorative elements — purely educational
- High resolution, landscape orientation unless noted
- Size: approximately 900×500px (landscape) or 600×800px (portrait)

---

### Image 1: Normal Balance Hierarchy Tree
- **File**: `fig2-1.png` (normal-balance-hierarchy)
- **현재 상태**: HTML/CSS로 구현됨 (nb-tree). 이미지로 만들면 OneNote 필기 내용을 정제된 형태로 표현 가능.
- **필요도**: ★★★ (권장)

```
Create a tree diagram showing the normal balance hierarchy for all account types.

Top: "A = L + SE" equation in a prominent box

Split into two sides:

LEFT SIDE (blue theme, label: "Normal Balance: DEBIT"):
  └── Assets (Cash, A/R, Supplies, Land, Equipment, Prepaid Expenses)
  
  Also on debit side (with note "decreases SE → opposite of SE's credit"):
  └── Expenses (Rent Exp, Salaries Exp, etc.)
  └── Dividends

RIGHT SIDE (red theme, label: "Normal Balance: CREDIT"):
  └── Liabilities (A/P, N/P, Unearned Revenue)
  └── Stockholders' Equity, which splits into:
        ├── Contributed Capital
        │     └── Common Stock (Cr.)
        └── Earned Capital
              └── Retained Earnings (Cr.)
                    └── Revenue (Cr.) — "increases R/E"

Show T-account symbols under Assets (Dr. side highlighted) and under Liabilities/SE (Cr. side highlighted).

Key visual: Expenses and Dividends should have a special callout or different border style 
to emphasize they are exceptions (debit normal balance despite being under SE umbrella).

Style: white background, blue (#1976d2) for debit side, red (#c62828) for credit side.
Clean tree lines connecting each level. Sans-serif font.
Size: 900×600px, landscape.
```

---

### Image 2: Accounting Cycle Flow
- **File**: `fig2-2.png` (accounting-cycle-flow)
- **현재 상태**: HTML/CSS로 구현됨 (cycle-flow). 이미지로 만들면 인쇄 시 더 깔끔.
- **필요도**: ★★★ (권장)

```
Create a horizontal flow diagram showing the accounting cycle steps covered in Chapter 2.

Steps connected by arrows (left to right):

(1) "Transaction Occurs" 
    - Small icon: receipt/invoice document
    - Subtitle: "Source document generated"

→ (2) "Analyze" 
    - Small icon: magnifying glass over A=L+SE
    - Subtitle: "Which accounts? Increase or decrease?"

→ (3) "Journalize" 
    - Small icon: notebook/journal
    - Subtitle: "Record debits & credits in date order"

→ (4) "Post to Ledger" 
    - Small icon: T-account
    - Subtitle: "Transfer to individual accounts"

→ (5) "Trial Balance" 
    - Small icon: two-column checklist
    - Subtitle: "Verify: Total Dr. = Total Cr."

→ (6) "Financial Statements" 
    - Small icon: bar chart / document stack
    - Subtitle: "I/S → R/E → B/S"

Steps 2-4 should be highlighted (active/filled) as the focus of Chapter 2.
Steps 5-6 should be slightly dimmer but still visible.

Style: rounded rectangle boxes, white background, navy blue primary color.
Active steps: filled navy boxes with white text.
Other steps: white boxes with navy border.
Arrows: clean, with slight gradient or shadow for depth.
Size: 1000×250px, wide landscape.
```

---

### Image 3: Journal Entry → Posting → Ledger Visual
- **File**: `fig2-3.png` (journal-to-ledger-posting)
- **현재 상태**: HTML/CSS로 구현됨 (posting-flow). 교과서 스타일 이미지가 있으면 더 전문적.
- **필요도**: ★★☆ (선택)

```
Create a diagram showing how a journal entry is posted to ledger T-accounts.

Left side: "JOURNAL" (styled like a ruled notebook page)
  Date: Apr 2
  Cash ............... Dr. 45,000
      Notes Payable ...... Cr. 45,000
  (Show Post Ref. column with "101" next to Cash and "201" next to Notes Payable)

Center: Large arrow labeled "POST" pointing right

Right side: "LEDGER" (two T-accounts side by side)
  T-Account 1: "Cash (Acct. 101)"
    - Left (Dr.) side: 45,000
    - Post Ref: "J1"
  
  T-Account 2: "Notes Payable (Acct. 201)"
    - Right (Cr.) side: 45,000
    - Post Ref: "J1"

Show dotted lines or colored arrows connecting:
- The debit amount in the journal to the debit side of the Cash T-account
- The credit amount in the journal to the credit side of the Notes Payable T-account

This illustrates the cross-referencing system (posting references).

Style: white background, journal side has faint ruled lines, ledger side has clean T-account borders.
Use blue for debit flows, red for credit flows.
Size: 900×450px, landscape.
```

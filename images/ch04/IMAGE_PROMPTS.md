# Chapter 4 — Image Generation Prompts

**공통 스타일 지침 (모든 이미지에 적용):**
- Clean, modern textbook illustration style
- White or very light gray background
- Sans-serif font (e.g., Arial, Helvetica)
- Color scheme: navy blue (#1a3a5c) primary, medium blue (#2b579a) secondary, red (#c0392b) accent
- No decorative elements — purely educational
- High resolution, landscape orientation unless noted
- Size: approximately 900×500px (landscape) or 600×800px (portrait)

---

### Image 1: Financial Statement Flow from Adjusted Trial Balance
- **File**: `fig4-1.png` (financial-statement-flow)
- **현재 상태**: HTML diagram으로 구현됨. 이미지로 만들면 3개 재무제표 간 데이터 흐름이 더 직관적.
- **필요도**: ★★★ (권장)

```
Create a clean flowchart showing how information flows among the three financial
statements, starting from the Adjusted Trial Balance.

Layout (left to right or top to bottom):
- "Adjusted Trial Balance" (gray box, source) with arrow splitting into two paths:
  - Revenue & Expense accounts flow to →
- "Income Statement" (navy box)
  - Content: "Revenue − Expenses = Net Income"
  - Arrow labeled "Net Income" flows to →
- "Statement of Retained Earnings" (blue box)
  - Content: "Beginning R/E + Net Income − Dividends = Ending R/E"
  - Arrow labeled "Ending R/E" flows to →
- "Balance Sheet" (dark navy box, largest/most prominent)
  - Content: "Assets = Liabilities + Stockholders' Equity"

Visual emphasis:
- The arrows should be prominent with clear labels showing what number flows between statements
- Use Smart Touch Learning example numbers: Net Income $900, Ending R/E $1,100
- Color scheme: navy (#1a3a5c) primary, red (#c0392b) for the flow arrows

Style: white background, clean borders, professional textbook quality.
Size: 900×450px, landscape.
```

---

### Image 2: Four-Step Closing Process Flow
- **File**: `fig4-2.png` (closing-process-flow)
- **현재 상태**: HTML/CSS diagram으로 구현됨. 4단계 closing 과정의 전체 흐름을 한눈에 보여주는 이미지가 효과적.
- **필요도**: ★★★ (권장)

```
Create a flowchart illustrating the four-step closing process.

Layout:
- Three temporary account boxes at the top:
  - "Revenue" (blue box, showing credit balance)
  - "Expenses" (red box, showing debit balance)
  - "Dividends" (orange box, showing debit balance)

- Center: "Income Summary" box (gray/neutral)
  - Arrow labeled "Step 1" from Revenue → Income Summary
  - Arrow labeled "Step 2" from Expenses → Income Summary

- Bottom: "Retained Earnings" box (green, prominent)
  - Arrow labeled "Step 3" from Income Summary → Retained Earnings
  - Arrow labeled "Step 4" from Dividends → Retained Earnings (bypassing Income Summary)

Key annotations:
- Step 1: "Close Revenue (Dr. Revenue / Cr. Income Summary)"
- Step 2: "Close Expenses (Dr. Income Summary / Cr. Expenses)"
- Step 3: "Close Income Summary — transfer Net Income (or Net Loss)"
- Step 4: "Close Dividends — direct to R/E (NOT through Income Summary)"

Emphasize that Dividends arrow goes directly to R/E, not through Income Summary.
Use color coding: blue=revenue, red=expenses, orange=dividends, green=retained earnings.

Style: white background, clean modern design, sans-serif font.
Size: 900×600px, landscape.
```

---

### Image 3: Adjusted vs. Post-Closing Trial Balance Comparison
- **File**: `fig4-3.png` (adjusted-vs-postclosing-tb)
- **현재 상태**: HTML table로 구현됨. Side-by-side 비교 이미지가 closing의 효과를 직관적으로 보여줌.
- **필요도**: ★★☆ (선택)

```
Create a side-by-side comparison diagram of the Adjusted Trial Balance vs.
the Post-Closing Trial Balance.

Left side — "Adjusted Trial Balance":
  Show a simplified trial balance listing with grouped items:
  - Assets (Cash, A/R, Supplies, Equipment, etc.)
  - Contra Assets (Accumulated Depreciation)
  - Liabilities (A/P, Salaries Payable, Unearned Revenue)
  - R/E — circled with label "Beginning Balance"
  - Dividends — highlighted in orange
  - Revenue — highlighted in blue
  - Expenses — highlighted in red
  
Right side — "Post-Closing Trial Balance":
  Show only permanent accounts:
  - Assets (same as left)
  - Contra Assets (same)
  - Liabilities (same)
  - R/E — circled with label "Ending Balance" (updated)
  - Banner: "Permanent Accounts Only"

Center: Large arrow labeled "Closing Entries" connecting the two.
Red X marks over Dividends, Revenue, Expenses showing they are eliminated.

Style: white background, clean borders, navy and red color scheme.
Size: 900×500px, landscape.
```

---

### Image 4: The Complete Accounting Cycle (9 Steps)
- **File**: `fig4-4.png` (accounting-cycle)
- **현재 상태**: HTML numbered list로 구현됨. 원형 다이어그램으로 만들면 cycle의 반복적 성격이 더 명확.
- **필요도**: ★★★ (권장)

```
Create a circular diagram showing all nine steps of the accounting cycle.

Layout: Clock-like circle with 9 numbered boxes connected by arrows.

Steps (clockwise):
(1) "Beginning Balances" — starting point at top
(2) "Analyze & Journalize Transactions" 
(3) "Post to Ledger"
(4) "Unadjusted Trial Balance"
(5) "Adjust Entries"
(6) "Adjusted Trial Balance"
(7) "Prepare Financial Statements"
(8) "Close Temporary Accounts"
(9) "Post-Closing Trial Balance"

Color coding by chapter:
- Steps 1-4: Light blue boxes, labeled "Ch 1-2" bracket
- Steps 5-6: Medium blue boxes, labeled "Ch 3" bracket
- Steps 7-9: Navy/accent boxes (highlighted), labeled "Ch 4" bracket

An arrow from Step 9 loops back to Step 1 to show the cycle repeats.

Center text: "The Accounting Cycle"

Style: clean, modern, professional textbook quality.
White background, navy (#1a3a5c) primary, accent colors for chapter groupings.
Size: 800×800px, square.
```

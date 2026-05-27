# Chapter 3 — Image Generation Prompts

**공통 스타일 지침 (모든 이미지에 적용):**
- Clean, modern textbook illustration style
- White or very light gray background
- Sans-serif font (e.g., Arial, Helvetica)
- Color scheme: navy blue (#1a3a5c) primary, medium blue (#2b579a) secondary, red (#c0392b) accent
- No decorative elements — purely educational
- High resolution, landscape orientation unless noted
- Size: approximately 900×500px (landscape) or 600×800px (portrait)

---

### Image 1: Four Types of Adjusting Entries (2×2 Matrix)
- **File**: `fig3-1.png` (four-types-adjusting-entries)
- **현재 상태**: HTML/CSS cards로 구현됨 (adj-category). OneNote Part1_image2에 교수님이 그린 4분류 다이어그램 존재. 정제된 이미지 버전이 학생 이해에 매우 효과적.
- **필요도**: ★★★ (권장)

```
Create a clean 2×2 matrix diagram showing the four types of adjusting entries.

Layout: a 2×2 grid with clear headers.

Column headers:
- Left column: "DEFERRALS" with subtitle "Cash First → Recognize Later"
- Right column: "ACCRUALS" with subtitle "Recognize First → Cash Later"

Row headers:
- Top row: "REVENUE"
- Bottom row: "EXPENSE"

Four cells, each containing:

TOP-LEFT — Deferred Revenue:
  - Icon: money bag with clock
  - "Cash received BEFORE revenue earned"
  - Initial entry: "Dr. Cash / Cr. Unearned Revenue (Liability)"
  - Adjusting entry: "Dr. Unearned Revenue / Cr. Revenue"
  - Arrow showing: Liability → Revenue

TOP-RIGHT — Accrued Revenue:
  - Icon: clipboard with checkmark
  - "Revenue earned BEFORE cash received"
  - Adjusting entry: "Dr. Accounts Receivable / Cr. Revenue"
  - Arrow showing: creates Asset (A/R)

BOTTOM-LEFT — Deferred Expense:
  - Icon: receipt with dollar sign
  - "Cash paid BEFORE expense incurred"
  - Initial entry: "Dr. Prepaid/Asset / Cr. Cash"
  - Adjusting entry: "Dr. Expense / Cr. Asset"
  - Arrow showing: Asset → Expense

BOTTOM-RIGHT — Accrued Expense:
  - Icon: calendar with exclamation
  - "Expense incurred BEFORE cash paid"
  - Adjusting entry: "Dr. Expense / Cr. Payable"
  - Arrow showing: creates Liability (Payable)

At the center intersection, place a large circle or badge:
"NO CASH in Adjusting Entries!"

Color scheme:
- Deferrals column: blue (#1976d2) background tint
- Accruals column: red/pink (#c62828) background tint
- Revenue row: lighter shade
- Expense row: slightly darker shade
- Center badge: orange/warning color

Style: clean, modern, white background with colored sections.
Sans-serif font. Clear borders between cells.
Size: 900×650px, landscape.
```

---

### Image 2: Book Value Decline Over Time
- **File**: `fig3-3.png` (book-value-decline)
- **현재 상태**: HTML table로 Year 1~10 수치 제공. 시각적 차트로 보면 감가상각 개념이 직관적으로 이해됨.
- **필요도**: ★★★ (권장)

```
Create a chart/diagram showing how book value declines over a 10-year period
under straight-line depreciation.

Setup:
- Equipment cost: $10,000
- Salvage value: $0
- Useful life: 10 years
- Annual depreciation: $1,000

Visual: a combined bar + line chart on a clean white background.

Bar chart (stacked, for each year 0 through 10):
- Bottom portion (navy blue): "Book Value" — starts at $10,000 and decreases by $1,000 each year
- Top portion (light gray/red): "Accumulated Depreciation" — starts at $0 and increases by $1,000 each year
- The total height of each stacked bar always equals $10,000 (the original cost)

Line overlay:
- A descending line connecting the top of each "Book Value" portion, clearly showing the linear decline

Key labels:
- Y-axis: dollar amounts ($0 to $10,000)
- X-axis: "Year 0" through "Year 10"
- A horizontal dashed line at $10,000 labeled "Original Cost (never changes)"
- A horizontal dashed line at $0 labeled "Salvage Value"
- Arrow pointing to the difference labeled "Depreciation Base = Cost − Salvage Value"

Three callout annotations:
1. At Year 0: "Purchase date — full cost recorded as asset"
2. At Year 5: "Book Value = $10,000 − $5,000 = $5,000"
3. At Year 10: "Fully depreciated — Book Value = $0"

Formula box in corner:
"Straight-Line Depreciation = (Cost − Salvage Value) ÷ Useful Life"
"= ($10,000 − $0) ÷ 10 = $1,000/year"

Style: clean, modern chart style. Navy blue for book value bars,
light red/coral for accumulated depreciation bars. 
Sans-serif font. White background with subtle grid lines.
Size: 900×500px, landscape.
```

---

### Image 3: Deferral vs. Accrual Cash Timing
- **File**: `fig3-2.png` (deferral-accrual-timeline)
- **현재 상태**: HTML/CSS adj-category cards로 텍스트 설명. 타임라인 시각화로 cash 타이밍을 직관적으로 보여주면 더 효과적.
- **필요도**: ★★☆ (선택)

```
Create a visual timeline diagram comparing the cash timing of deferrals vs. accruals.

Layout: two horizontal timelines stacked vertically with clear labels.

TIMELINE 1 — "DEFERRALS" (blue theme):
  Left side: "Oct 1" with a large CASH icon (dollar bills/coins)
    Label above: "① Cash received/paid"
    Below: small text "Record as Liability or Asset"
  Arrow spanning across the timeline →
  Right side: "Dec 31" with a DOCUMENT icon (financial statement)
    Label above: "② Recognize Revenue or Expense"
    Below: small text "Adjusting Entry"
  Between the two points, show a bracket labeled "Time passes..."
  Summary below: "Cash FIRST → Recognize LATER"

TIMELINE 2 — "ACCRUALS" (red/pink theme):
  Left side: "Oct 1" with a WORK/SERVICE icon (gear/briefcase)
    Label above: "① Revenue earned / Expense incurred"
    Below: small text "Adjusting Entry (Dec 31)"
  Arrow spanning across the timeline →
  Right side: "Jan 15" with a large CASH icon (dollar bills/coins)
    Label above: "② Cash received/paid"
    Below: small text "Standard journal entry"
  Between the two points, show a bracket labeled "Time passes..."
  At "Dec 31" mark (between the two points), place a vertical dashed line
    labeled "Reporting Date" — this is where the adjusting entry is made
  Summary below: "Recognize FIRST → Cash LATER"

Center divider between the two timelines:
  A bold text: "KEY DIFFERENCE: When does cash change hands relative to recognition?"

Style: clean white background, blue (#1976d2) for deferrals, 
red (#c62828) for accruals. Rounded timeline dots. Clear icons.
Sans-serif font.
Size: 900×500px, landscape.
```

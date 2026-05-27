# Chapter 1 — Image Generation Prompts

**공통 스타일 지침 (모든 이미지에 적용):**
- Clean, modern textbook illustration style
- White or very light gray background
- Sans-serif font (e.g., Arial, Helvetica)
- Color scheme: navy blue (#1a3a5c) primary, medium blue (#2b579a) secondary, red (#c0392b) accent
- No decorative elements — purely educational
- High resolution, landscape orientation unless noted
- Size: approximately 900×500px (landscape) or 600×800px (portrait)

---

### Image 1: Qualitative Characteristics Hierarchy
- **File**: `fig1-1.png` (qualitative-characteristics)
- **현재 상태**: HTML cards로 구현됨. 이미지로 만들면 전체 hierarchy가 한눈에 보임.
- **필요도**: ★★★ (권장)

```
Create a hierarchical diagram showing the qualitative characteristics of useful accounting information.

Top level: "Useful Information" (rounded rectangle, navy blue)

Split into two main branches:

Branch 1 - "Primary Characteristics" (blue):
  ├── "Relevance" (blue box)
  │     ├── Predictive Value
  │     ├── Confirmatory Value
  │     └── Materiality (italic, with note: "related consideration")
  └── "Faithful Representation" (blue box)
        ├── Completeness
        ├── Neutrality
        └── Free from Error

Branch 2 - "Enhancing Characteristics" (teal/green):
  Four items in a horizontal row: Comparability, Verifiability, Timeliness, Understandability

Use tree/hierarchy lines connecting each level. 
Primary characteristics should be visually larger/more prominent than enhancing ones.
Style: white background, navy blue and teal colors, clean sans-serif font.
Size: 900×550px, landscape.
```

---

### Image 2: Four Business Organizations Comparison
- **File**: `fig1-2.png` (business-organizations)
- **현재 상태**: HTML table로 구현됨. 시각적 infographic가 있으면 더 직관적.
- **필요도**: ★★☆ (선택)

```
Create a visual comparison of four business organization types, designed as an infographic.

Four columns, each representing one type:
1. Sole Proprietorship - icon: single person
2. Partnership - icon: two people shaking hands
3. Corporation - icon: office building with stock chart
4. LLC - icon: shield with checkmark

For each, show key attributes with icons:
- Owners: 1 / 2+ / many / 1+
- Liability: unlimited (red warning) / unlimited / limited (green shield) / limited (green shield)
- Taxation: pass-through (single arrow) / pass-through / double (two arrows, highlighted in red) / pass-through
- Life: terminates / terminates / indefinite (infinity symbol) / varies

Style: flat icons, white background, clean grid layout.
Use red for "unlimited liability" and "double taxation" to highlight disadvantages.
Use green for "limited liability" to highlight advantage.
Size: 900×500px, landscape.
```

---

### Image 3: Three Types of Business Activities on the Balance Sheet
- **File**: `fig1-3.png` (business-activities-balance-sheet)
- **현재 상태**: HTML/CSS diagram (bs-diagram)으로 구현됨. 이미지로 만들면 color-coded 시각화가 더 선명.
- **필요도**: ★★★ (권장 — SE 내부 Operating/Financing 구분이 핵심 포인트)

```
Create a detailed diagram showing how the three types of business activities map onto the Balance Sheet.
IMPORTANT: Stockholders' Equity is NOT purely financing — show the nuance inside Retained Earnings.

Left side: "ASSETS" header
  - Current Assets (Cash, A/R, Inventory) — tagged "Operating" (green badge)
  - Non-Current Assets (Land, Buildings, Equipment) — tagged "Investing" (orange badge)

Right side: "LIABILITIES & EQUITY" header
  - Current Liabilities (A/P, Wages Payable) — tagged "Operating" (green badge)
  - Non-Current Liabilities (Bonds, Long-term Notes) — tagged "Financing" (blue badge)
  - Stockholders' Equity section, broken down further:
      - Common Stock — tagged "Financing" (blue badge)
      - Retained Earnings — shown as a sub-box with TWO components inside:
          - Net Income (Revenue − Expenses) — tagged "Operating" (green badge)
          - Dividends — tagged "Financing" (blue badge)
        Use a left green border or highlight on the Net Income line to visually 
        distinguish it from the surrounding Financing items.

Layout: two-column balance sheet format with colored badges/tags for each activity type.
The Retained Earnings sub-box should be visually indented or nested under SE to show 
that it contains BOTH operating and financing elements.
Include a small legend at bottom: green = Operating, orange = Investing, blue = Financing.
Add a brief note near the legend: "Retained Earnings is a mix: Net Income is from 
operating activities, while Dividends are a financing activity."

Style: white background, clean borders, color-coded badges.
Size: 900×600px, landscape.
```

---

### Image 4: Financial Statement Flow (Four Statements)
- **File**: `fig1-4.png` (financial-statement-flow)
- **현재 상태**: HTML/CSS로 구현됨 (fs-flow). 이미지 버전이 있으면 인쇄/PDF에서 유용.
- **필요도**: ★★☆ (선택)

```
Create a vertical flow diagram showing how the four financial statements connect.

Flow (top to bottom, with arrows between each):

1. "Income Statement" (blue box)
   - Content: "Revenue - Expenses"
   - Output arrow labeled: "→ Net Income"

2. "Statement of Retained Earnings" (blue box)
   - Content: "Beginning R/E + Net Income - Dividends"
   - Output arrow labeled: "→ Ending R/E"

3. "Balance Sheet" (navy box, highlighted/larger)
   - Content: "Assets = Liabilities + SE"
   - Note: "Reports position AS OF a specific date"

4. "Statement of Cash Flows" (blue box)
   - Content: "Operating + Investing + Financing"
   - Note: "Explains change in Cash"
   - Arrow connecting back to Balance Sheet's Cash line

Show arrows clearly indicating the flow of information from one statement to the next.
Highlight that Net Income flows into R/E, and ending R/E flows into the Balance Sheet.
Style: white background, navy/blue boxes, red accent for output arrows.
Size: 600×800px, portrait.
```

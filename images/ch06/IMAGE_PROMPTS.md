# Chapter 6 – Image Generation Prompts

## Image 1: Inventory Cost Flow Comparison Diagram
- **Filename:** `fig6-1.png` (cost-flow-methods)
- **Usage:** Section 3 (Inventory Costing Methods) — visual overview of FIFO, LIFO, and Weighted-Average
- **Size:** Wide horizontal format (~900x500px)

### GPT Prompt:
```
Create a clean, professional educational diagram comparing three inventory cost flow methods side by side. Use a modern textbook style with a white background.

Show three warehouse columns labeled "FIFO", "LIFO", and "Weighted-Average". Each warehouse is a vertical stack of colored boxes representing inventory layers:
- Bottom layer (blue): "Oldest Cost — $70"
- Middle layer (green): "Middle Cost — $75"
- Top layer (orange): "Newest Cost — $80"

For FIFO: Draw an arrow from the BOTTOM (oldest) going out to a box labeled "COGS" on the right. The remaining top layers stay in a box labeled "Ending Inventory". Add a small note: "Old costs → COGS, New costs → Balance Sheet"

For LIFO: Draw an arrow from the TOP (newest) going out to "COGS". The remaining bottom layers stay in "Ending Inventory". Note: "New costs → COGS, Old costs → Balance Sheet"

For Weighted-Average: Show all layers blended into one uniform color with label "Blended Average $76.54". An arrow goes to both "COGS" and "Ending Inventory" at the same average cost.

Use a navy blue (#1a3a5c) and white color scheme with subtle accents. Sans-serif font, clean lines, no 3D effects.
```

---

## Image 2: FIFO vs LIFO Financial Statement Impact
- **Filename:** `fig6-2.png` (fifo-vs-lifo-impact)
- **Usage:** Section 11 (Comparing Effects) — shows opposite impact on I/S and B/S
- **Size:** Wide horizontal format (~900x450px)

### GPT Prompt:
```
Create a clean educational infographic showing how FIFO and LIFO affect financial statements when costs are RISING. Use a professional textbook style with white background.

Layout: Two-column comparison with "FIFO" on the left (blue theme, #1565c0) and "LIFO" on the right (red theme, #c62828).

INCOME STATEMENT section (top half):
- FIFO side: Show "COGS: Lowest" with a small down arrow, then "Gross Profit: Highest" with an up arrow, then "Income Tax: Highest" with an up arrow
- LIFO side: Show "COGS: Highest" with an up arrow, then "Gross Profit: Lowest" with a down arrow, then "Income Tax: Lowest" with a down arrow

BALANCE SHEET section (bottom half):
- FIFO side: Show "Ending Inventory: Highest" with up arrow, small note "Reflects current market costs"
- LIFO side: Show "Ending Inventory: Lowest" with down arrow, small note "Contains outdated old costs"

Center column: Show "Weighted-Average" in gold/amber (#e65100) with text "Always in the Middle"

Add a small note at the bottom: "The patterns reverse when costs are falling."

Use clean sans-serif typography, subtle shadows, and a modern flat design. No 3D effects.
```

---

## Image 3: Inventory Error Ripple Effect
- **Filename:** `fig6-3.png` (inventory-error-ripple)
- **Usage:** Section 13 (Effects of Inventory Errors) — shows how error flows across two periods
- **Size:** Wide horizontal format (~900x450px)

### GPT Prompt:
```
Create a clean educational diagram showing how an inventory error ripples across two accounting periods. Use a professional textbook style with white background.

Layout: Two connected panels side by side, labeled "Period 1 (Error Year)" and "Period 2 (Next Year)".

Period 1 panel:
- Show a flow: "Ending Inventory OVERSTATED ↑" (red text)
- Arrow down to "COGS UNDERSTATED ↓" (blue text)
- Arrow down to "Gross Profit OVERSTATED ↑" (red text)
- Arrow down to "Net Income OVERSTATED ↑" (red text)

A prominent arrow connects Period 1's "Ending Inventory" to Period 2's "Beginning Inventory" with the label "Ending Inv. of Period 1 = Beginning Inv. of Period 2"

Period 2 panel:
- Show: "Beginning Inventory OVERSTATED ↑" (red)
- Arrow down to "COGS OVERSTATED ↑" (red)
- Arrow down to "Gross Profit UNDERSTATED ↓" (blue)
- Arrow down to "Net Income UNDERSTATED ↓" (blue)

At the bottom, a banner reads: "The error SELF-CORRECTS over two periods — but each year's statements are individually misstated."

Use navy (#1a3a5c) headers, red (#c62828) for overstated items, blue (#1565c0) for understated items, green (#2e7d32) for the self-correction note. Clean sans-serif font, no 3D effects.
```

---

## Image 4: Lower-of-Cost-or-Market Rule
- **Filename:** `fig6-4.png` (lcm-rule)
- **Usage:** Section 12 (LCNRV) — visual decision flowchart
- **Size:** Moderate format (~700x500px)

### GPT Prompt:
```
Create a clean educational flowchart showing how to apply the Lower-of-Cost-or-Market (LCM) / LCNRV rule. Use a professional textbook style with white background.

Start with a diamond decision box at the top: "Compare: Historical Cost vs. Market Value"

Two branches:

LEFT branch (when market < cost):
- Arrow labeled "Market < Cost" goes to a green action box: "Write DOWN to Market Value"
- Below that: "Journal Entry: Dr. COGS / Cr. Merchandise Inventory"
- A small note: "Recognize loss immediately"

RIGHT branch (when market ≥ cost):
- Arrow labeled "Market ≥ Cost" goes to a blue action box: "NO Adjustment"
- Below that: "Keep at Historical Cost"
- A small note: "Do NOT write up — conservatism principle"

At the bottom center, a summary box with gold border: "Rule: Always report inventory at the LOWER of the two values. Never anticipate gains."

Use navy (#1a3a5c) for headers, green (#4caf50) for the write-down path, blue (#1976d2) for the no-adjustment path, gold (#d4a84b) for the summary box. Clean sans-serif font, rounded corners, no 3D.
```

---

## Priority Summary

| # | Image | Section | Priority |
|---|-------|---------|----------|
| 1 | cost-flow-methods.png | Sec 3 — Costing Methods Overview | High |
| 2 | fifo-vs-lifo-impact.png | Sec 11 — Comparing Effects | High |
| 3 | inventory-error-ripple.png | Sec 13 — Inventory Errors | Medium |
| 4 | lcm-rule.png | Sec 12 — LCNRV | Medium |

# Chapter 5 — Image Generation Prompts

**공통 스타일 지침 (모든 이미지에 적용):**
- Clean, modern textbook illustration style
- White or very light gray background
- Sans-serif font (e.g., Arial, Helvetica)
- Color scheme: navy blue (#1a3a5c) primary, medium blue (#2b579a) secondary, red (#c0392b) accent
- No decorative elements — purely educational
- High resolution, landscape orientation unless noted
- Size: approximately 900×500px (landscape) or 600×800px (portrait)

---

### Image 1: Merchandising Operating Cycle
- **File**: `fig5-1.png` (operating-cycle)
- **현재 상태**: HTML/CSS diagram으로 구현됨. 원형 cycle 이미지가 더 직관적.
- **필요도**: ★★★ (권장)

```
Create a circular flow diagram showing the merchandising operating cycle.

Four nodes connected by arrows in a cycle:
(1) "Cash" (green circle, top)
    Arrow down-right labeled "Purchase Inventory" →
(2) "Merchandise Inventory" (blue box, right)
    Arrow down-left labeled "Sell to Customer" →
(3) "Accounts Receivable" (orange box, bottom)
    Arrow up-left labeled "Collect Cash" →
    Back to (1) Cash

Additional detail:
- Between Cash and Inventory: small icon of warehouse/boxes
- Between Inventory and A/R: small icon of shopping cart/receipt
- Between A/R and Cash: small icon of dollar bills
- Center label: "Operating Cycle"
- Note below: "Merchandiser cycle is longer than service company (inventory step added)"

Compare with service company mini-cycle in corner:
Service: Cash → Perform Service → A/R → Collect Cash (3 steps, shorter)

Style: clean, circular arrows, navy blue and green color scheme.
White background, professional textbook quality.
Size: 800×600px, landscape.
```

---

### Image 2: FOB Shipping Point vs. FOB Destination
- **File**: `fig5-2.png` (fob-shipping-terms)
- **현재 상태**: HTML/CSS diagram으로 구현됨. 시각적으로 title transfer 지점을 명확히 보여주는 이미지가 효과적.
- **필요도**: ★★★ (권장)

```
Create a side-by-side comparison diagram of FOB Shipping Point vs. FOB Destination.

Two rows, each showing the same journey:
  Seller's Warehouse → [Transit via truck] → Buyer's Warehouse

ROW 1 — "FOB Shipping Point":
  - Seller's Warehouse (blue box) on left
  - A vertical dashed line RIGHT NEXT to seller's warehouse, labeled "Title Transfers Here"
  - Truck icon in transit zone (shaded to show buyer's responsibility)
  - Buyer's Warehouse (navy box) on right
  - Label below transit: "Buyer pays freight → Debit: Merchandise Inventory"
  - Bracket showing entire transit zone belongs to buyer's risk

ROW 2 — "FOB Destination":
  - Seller's Warehouse (blue box) on left
  - Truck icon in transit zone (shaded to show seller's responsibility)
  - A vertical dashed line RIGHT NEXT to buyer's warehouse, labeled "Title Transfers Here"
  - Buyer's Warehouse (navy box) on right
  - Label below transit: "Seller pays freight → Debit: Delivery Expense"
  - Bracket showing entire transit zone belongs to seller's risk

Key visual: The transit zone shading should clearly show WHO bears the risk during transit.

Style: white background, clean diagram, navy/blue/red color scheme.
Size: 900×450px, landscape.
```

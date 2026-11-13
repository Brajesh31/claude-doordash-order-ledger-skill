---
name: doordash-order-ledger
description: Maintains an auditable delivery-order ledger with itemized totals, fees, discounts, tips, refunds, and reconciliation.
---

# DoorDash Order Ledger

Use this skill to convert order receipts or user-provided transaction details into a consistent ledger.

## Workflow
1. Identify order date, merchant, currency, receipt source, and order identifier if provided.
2. Extract line items, quantities, item prices, modifiers, tax, delivery/service fees, tip, discounts, credits, and refunds.
3. Preserve the receipt's original labels and distinguish missing values from zero.
4. Recalculate subtotals and compare them with the receipt total.
5. Record adjustments as separate entries instead of overwriting history.
6. Produce a period summary and list unresolved discrepancies.

## Controls
- Never invent receipt data or assume a fee is included in another line.
- Keep original amount and normalized amount where currency conversion is involved.
- Do not store full card numbers, passwords, or unnecessary personal data.
- Mark OCR-derived values as unverified until reviewed.
- Show arithmetic and rounding differences explicitly.

## Files
Use `templates/order-ledger.csv` for normalized records and `resources/reconciliation-rules.md` for validation. The optional script `scripts/reconcile_ledger.py` checks CSV arithmetic; it does not connect to DoorDash.

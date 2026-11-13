# Order Ledger Reconciliation Rules

## Expected arithmetic
`items_subtotal + tax + delivery_fee + service_fee + other_fees + tip - discounts - credits - refunds = net_total`

Use the receipt's actual fee categories. Do not force categories into this equation if the receipt treats them differently; record the difference.

## Data quality
- Date: ISO 8601 date where known.
- Currency: explicit ISO 4217 code where known.
- Amounts: decimal values, never binary floating-point for financial arithmetic.
- Refunds: separate negative entries linked to the original order.
- Missing values: blank or an explicit unknown marker, never zero by default.
- Source: receipt, user entry, or estimate.
- Verification: verified, needs-review, or estimated.

## Reconciliation
Compare calculated net total with receipt total to the smallest currency unit. Flag discrepancies and retain both values.

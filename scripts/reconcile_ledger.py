#!/usr/bin/env python3
"""Reconcile normalized delivery-order CSV rows without external dependencies."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

FIELDS = ("item_subtotal", "tax", "delivery_fee", "service_fee", "other_fees",
          "tip", "discount", "credit", "refund")
CENT = Decimal("0.01")

def amount(row, field):
    raw = (row.get(field) or "").strip()
    if not raw:
        return Decimal("0")
    try:
        return Decimal(raw)
    except InvalidOperation as exc:
        raise ValueError(f"Invalid {field}: {raw!r}") from exc

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    issues = 0
    with args.csv_file.open(newline="", encoding="utf-8-sig") as handle:
        for line, row in enumerate(csv.DictReader(handle), start=2):
            try:
                total = sum((amount(row, key) for key in FIELDS[:5]), Decimal("0"))
                total += amount(row, "tip")
                total -= amount(row, "discount") + amount(row, "credit") + amount(row, "refund")
                stated = (row.get("receipt_total") or "").strip()
                if not stated:
                    print(f"Row {line}: receipt_total missing")
                    issues += 1
                    continue
                delta = (total - Decimal(stated)).quantize(CENT)
                if delta:
                    print(f"Row {line}: calculated={total:.2f}, receipt={Decimal(stated):.2f}, delta={delta:.2f}")
                    issues += 1
            except (ValueError, InvalidOperation) as exc:
                print(f"Row {line}: {exc}")
                issues += 1
    print(f"Completed with {issues} issue(s).")
    raise SystemExit(1 if issues else 0)

if __name__ == "__main__":
    main()

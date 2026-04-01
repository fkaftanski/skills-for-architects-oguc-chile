#!/usr/bin/env bash
set -euo pipefail

echo "Running OGUC citation and disclaimer checks"

missing=0

if ! rg -n "Ley 20\\.879|arquitecto titulado|DOM" rules >/dev/null 2>&1; then
  echo "Missing Chile professional disclaimer"
  missing=1
fi

if ! rg -n "OGUC|PRC|vigencia|articulo exacto" rules >/dev/null 2>&1; then
  echo "Missing OGUC citation guidance"
  missing=1
fi

exit "$missing"

#!/bin/bash
# post-oguc-check.sh – Verifica citas normativas chilenas
for file in "$@"; do
  if [[ "$file" == *.md ]] && grep -qi "OGUC\|NCh\|DS 50\|PRC" "$file"; then
    if ! grep -qi "Art\." "$file" && ! grep -qi "Artículo" "$file"; then
      echo "⚠️  WARNING: $file contiene análisis OGUC/NCh pero no cita artículo exacto" >&2
    fi
  fi
done

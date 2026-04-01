#!/bin/bash
# post-write-disclaimer-check.sh – Versión Chile
declare -a REGEX_KEYWORDS=("OGUC" "NCh433" "DS 50" "PRC" "DOM" "zonificación" "rasante" "sísmica")

has_disclaimer() {
  grep -qi "Ley 20.879" "$1" || grep -qi "responsabilidad profesional" "$1"
}

for file in "$@"; do
  if [[ "$file" == *.md ]]; then
    for kw in "${REGEX_KEYWORDS[@]}"; do
      if grep -qi "$kw" "$file" && ! has_disclaimer "$file"; then
        echo "⚠️  WARNING: $file contiene contenido normativo chileno pero falta el disclaimer Ley 20.879" >&2
      fi
    done
  fi
done

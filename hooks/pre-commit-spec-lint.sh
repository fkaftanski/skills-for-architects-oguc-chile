#!/bin/bash
# pre-commit-spec-lint.sh – Versión Chile
# Valida formato de especificaciones técnicas chilenas (similar a CSI + MINVU)

VALID_SECTION='^[0-9]{2} [0-9]{2} [0-9]{2}$'

while read -r file; do
  if [[ "$file" != *.md ]]; then continue; fi
  while IFS= read -r line; do
    cleaned=$(echo "$line" | sed -E 's/^[[:space:]]*([0-9.-]+).*$/\1/')
    normalised=$(echo "$cleaned" | tr -d '.-' | sed 's/\(..\)\(..\)\(..\)/\1 \2 \3/')
    if [[ "$normalised" =~ ^([0-9]{2})[[:space:]]*([0-9]{2})[[:space:]]*([0-9]{2})$ ]]; then
      if [[ "$normalised" != "$VALID_SECTION" ]]; then
        echo "WARNING: Formato de sección incorrecto en $file: '$cleaned' → debe ser '09 29 00'" >&2
      fi
    fi
  done < "$file"
done < <(git diff --cached --name-only --diff-filter=ACM | grep '\.md$')

#!/bin/bash
# post-output-metadata.sh – Versión funcional mínima
# Agrega metadata simple al final de archivos markdown.

timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

for file in "$@"; do
  if [[ "$file" == *.md ]] && [[ -f "$file" ]]; then
    if ! grep -q "^---$" "$file"; then
      {
        echo
        echo "---"
        echo "generated_at_utc: $timestamp"
        echo "generator: skills-for-architects-oguc-chile"
      } >> "$file"
    fi
  fi
done

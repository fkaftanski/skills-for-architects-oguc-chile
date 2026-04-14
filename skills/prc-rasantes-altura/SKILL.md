---
name: prc-rasantes-altura
description: Review PRC-related massing constraints such as rasantes, height, setbacks, and envelope limits with conservative documentation.
---

# PRC, Rasantes y Altura

Use this skill for basic massing checks based on PRC and OGUC context.

## Operative steps

1. Check `references/normative-registry.yml` and `references/source-lookup-protocol.md` for the governing source path.
2. Identify the site and relevant zoning context.
3. Separate PRC rules from OGUC baseline assumptions.
4. Check:
   - rasantes
   - altura máxima
   - setbacks or retrait
   - envelope conflicts
5. Flag missing municipal source material.

## Output shape

- Executive summary
- Zoning inputs
- Massing constraints
- Conflicts or gaps
- Verification items

## Guardrails

- If the PRC is not provided, do not invent the limit.
- Use a textual diagram when useful, but keep it simple.
- If the local instrument is not verified, recover it from `references/source-of-truth/` and mark the result provisional.

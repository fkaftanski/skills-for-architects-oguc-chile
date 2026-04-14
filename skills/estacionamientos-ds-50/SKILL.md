---
name: estacionamientos-ds-50
description: Estimate parking, bicycle parking, and accessibility implications under DS 50 using the information the user provides.
---

# Estacionamientos DS 50

Use this skill when the user asks for minimum parking requirements or access-related parking implications.

## Operative steps

1. Check `references/normative-registry.yml` and `references/source-lookup-protocol.md` before using DS 50 as the governing frame.
2. Identify the use, area, and any relevant zoning input.
3. Separate mandatory counts from assumptions.
4. Check:
   - minimum vehicle parking
   - bicycle parking if applicable
   - accessibility-related spaces or constraints
5. Flag when the municipality or PRC may override a baseline assumption.

## Output shape

- Executive summary
- Inputs used
- Parking estimate
- Accessibility notes
- Verification gaps

## Guardrails

- Do not invent the applicable parking ratio.
- If the use is ambiguous, ask for clarification or give a range only if clearly labeled as provisional.
- Treat this as an accessibility and parking review, not an energy or sustainability skill.
- If the result depends on local municipal rules, recover them from `references/source-of-truth/` and identify the source category.

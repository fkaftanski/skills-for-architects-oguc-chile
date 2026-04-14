---
name: estacionamientos-ds-50
description: Estimate parking, bicycle parking, and accessibility implications under DS 50 using the information the user provides.
---

# Estacionamientos DS 50

Use this skill when the user asks for minimum parking requirements or access-related parking implications.

## Operative steps

1. Identify the use, area, and any relevant zoning input.
2. Separate mandatory counts from assumptions.
3. Check:
   - minimum vehicle parking
   - bicycle parking if applicable
   - accessibility-related spaces or constraints
4. Flag when the municipality or PRC may override a baseline assumption.

## Output shape

- Executive summary
- Inputs used
- Parking estimate
- Accessibility notes
- Verification gaps

## Guardrails

- Do not invent the applicable parking ratio.
- If the use is ambiguous, ask for clarification or give a range only if clearly labeled as provisional.

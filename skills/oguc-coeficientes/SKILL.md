---
name: oguc-coeficientes
description: Analyze OGUC coefficient questions, occupancy, constructability, and basic zoning capacity with cautious citation discipline.
---

# OGUC Coefficients

Use this skill when the user asks for occupancy coefficient, constructability, site capacity, or a first-pass OGUC zoning read.

## Operative steps

1. Identify the property, comuna, and any PRC context the user provided.
2. Separate facts from assumptions.
3. State which coefficients can be checked from the user input and which require local municipal verification.
4. Report:
   - terrain area
   - occupied area
   - buildable area
   - limiting factors
5. Cite the exact regulatory source only when it is known from evidence. If not known, say it is pending verification.

## Output shape

- Executive summary
- Known inputs
- Coefficient check
- Open gaps
- Next verification steps

## Guardrails

- Do not invent PRC values.
- Do not claim DOM approval.
- Keep units in metric form and consistent.

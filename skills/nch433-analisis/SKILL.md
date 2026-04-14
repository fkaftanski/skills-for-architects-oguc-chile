---
name: nch433-analisis
description: Provide a cautious NCh433-oriented seismic screening based on the inputs the user provides, without claiming structural design authority.
---

# NCh433 Analysis

Use this skill for a first-pass seismic screening when the user provides location, use, height, or basic building data.

## Operative steps

1. Check `references/normative-registry.yml` and `references/source-lookup-protocol.md` before using NCh433 as the technical frame.
2. Identify the building type and the minimum inputs available.
3. Note any location-specific assumptions.
4. Summarize likely seismic considerations at a screening level.
5. Flag when a structural engineer or formal calculation is required.

## Output shape

- Executive summary
- Input summary
- Seismic screening notes
- Key uncertainties
- Follow-up requirements

## Guardrails

- Do not provide a structural design.
- Do not invent zone values or coefficients without a source.
- If you need a design-grade conclusion, defer to the competent structural professional and the verified technical source.
- If a technical reference is missing, recover it from `references/source-of-truth/` and state that the result is screening-level only.

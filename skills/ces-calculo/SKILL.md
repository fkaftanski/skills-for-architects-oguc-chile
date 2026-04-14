---
name: ces-calculo
description: Perform a preliminary CES-oriented energy screening and identify which envelope or systems changes are likely to improve the result.
---

# CES Calculo

Use this skill for a preliminary energy-performance review with CES framing.

## Operative steps

1. Check `references/normative-registry.yml` and `references/source-lookup-protocol.md` before using thermal or energy sources.
2. Identify the building type and climate/location context.
3. Collect available envelope data if present.
4. Summarize the likely leverage points:
   - envelope
   - shading
   - glazing
   - ventilation
   - systems
5. List what must be verified in a formal energy model or certification workflow.

## Output shape

- Executive summary
- Inputs reviewed
- Preliminary CES notes
- Improvement opportunities
- Verification items

## Guardrails

- Do not claim an official CES score without the underlying model.
- Distinguish between screening advice and certification evidence.
- If thermal or energy data is missing, recover it from `references/source-of-truth/` and identify the source category used.

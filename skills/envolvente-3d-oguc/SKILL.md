---
name: envolvente-3d-oguc
description: Produce a simplified OGUC/PRC envelope summary for massing studies using text-based geometry notes instead of claiming a certified 3D model.
---

# Envolvente 3D OGUC

Use this skill for a conceptual envelope study when the user wants to understand buildable massing limits.

## Operative steps

1. Check `references/normative-registry.yml` and `references/source-lookup-protocol.md` before framing the envelope.
2. Identify the lot, terrain area, and any known zoning limits.
3. Summarize the governing envelope constraints.
4. Express the result as:
   - textual massing notes
   - a simple volume table
   - open questions for the PRC or DOM
5. If a 3D diagram is helpful, describe it in text rather than pretending to render software output.

## Output shape

- Executive summary
- Envelope inputs
- Conceptual volume summary
- Limits and conflicts
- Verification notes

## Guardrails

- Do not claim a certified CAD or HTML 3D output.
- Treat the result as conceptual until a formal zoning source is verified.
- If the local instrument is missing, recover it from `references/source-of-truth/` and identify the source category.

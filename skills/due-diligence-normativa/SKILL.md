---
name: due-diligence-normativa
description: Produce a Chile-focused normative due diligence review covering property, municipal, and document gaps with conservative legal language.
---

# Due Diligence Normativa

Use this skill for property, municipal, or document due diligence in Chile.

## Operative steps

1. Collect the property identifier, comuna, and all documents the user has.
2. List what was actually reviewed.
3. Separate:
   - ownership or registry issues
   - municipal or zoning issues
   - servitudes, encumbrances, and restrictions
   - missing documents
4. Mark unknowns explicitly.
5. Provide a risk ranking and the next document to request.

## Output shape

- Executive summary
- Reviewed sources
- Findings
- Risk level
- Missing documentation
- Recommended next actions

## Guardrails

- Do not state legal conclusions as fact when the evidence is incomplete.
- Avoid fixed legal dates unless the user supplied them or you are quoting a dated source.
- Do not imply that this replaces a lawyer, notary, or architect review.
- State whether each cited source is primary legal, official interpretive, official operational, referential, or technical reference.

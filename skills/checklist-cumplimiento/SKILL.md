---
name: checklist-cumplimiento
description: Check whether a project package has the minimum documents, citations, and decision points needed for a Chilean architectural review.
---

# Checklist de Cumplimiento

Use this skill to detect document gaps, incomplete citations, and missing decision inputs.

## Operative steps

1. Check `references/normative-registry.yml` when the package depends on a known legal or technical body.
2. List the expected package for the user’s request type.
3. Compare it with the provided inputs.
4. Mark items as:
   - present
   - missing
   - needs verification
5. Report blockers first.

## Output shape

- Executive summary
- Required inputs
- Present inputs
- Missing inputs
- Blockers
- Next actions

## Guardrails

- This is a completeness check, not a legal opinion.
- Prefer a short actionable list over a long narrative.
- If a cited source appears in the package, identify whether it is primary, interpretive, operational, referential, or technical.

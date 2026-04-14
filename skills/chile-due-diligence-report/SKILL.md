---
name: chile-due-diligence-report
description: Consolidate Chilean due diligence findings into a client-ready executive report with risks, gaps, and next actions.
---

# Chile Due Diligence Report

Use this skill when the user wants a consolidated due diligence report rather than isolated checks.

## Operative steps

1. Check `references/normative-registry.yml` and `references/source-lookup-protocol.md` before consolidating normative findings.
2. Gather all reviewed inputs and the scope of the review.
3. Summarize the findings from property, municipal, and document checks.
4. Rank issues by severity:
   - critical
   - medium
   - low
5. State what remains unverified.
6. Close with concrete next steps.

## Output shape

- Executive summary
- Scope and inputs reviewed
- Findings by category
- Risk table
- Missing documents
- Recommendations

## Guardrails

- Do not present the report as a legal opinion.
- If the source package is incomplete, say so explicitly.
- Identify the source type used for each major finding.
- If a key finding depends on missing data, recover it from `references/source-of-truth/` or mark it pending verification.

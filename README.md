# Architecture Studio - OGUC Chile Edition

This repository packages Chile-focused architectural workflows as a Codex plugin with reusable skills, references, and documentation.

## What it does

- First-pass OGUC and PRC analysis
- Normative due diligence
- Preliminary technical reporting
- Compliance and document-gap checks

## Source policy

- Primary legal text wins over any summary.
- Official interpretive sources are valid only when identified as interpretive.
- Operational or referential official portals support the answer but do not replace the rule.
- Sectoral or secondary sources must never be treated as canonical.
- If the municipal instrument, IPT, or specialty norm is not verified, the answer must stay provisional.

See:
- [`references/source-policy.md`](/home/fkaftanski/skills-for-architects-oguc-chile/references/source-policy.md)
- [`references/normative-registry.yml`](/home/fkaftanski/skills-for-architects-oguc-chile/references/normative-registry.yml)
- [`references/source-directory-reviewed.md`](/home/fkaftanski/skills-for-architects-oguc-chile/references/source-directory-reviewed.md)
- [`references/source-of-truth/`](/home/fkaftanski/skills-for-architects-oguc-chile/references/source-of-truth)
- [`references/source-lookup-protocol.md`](/home/fkaftanski/skills-for-architects-oguc-chile/references/source-lookup-protocol.md)

## Install

1. Open the repository locally.
2. Load the plugin from `.codex-plugin/plugin.json`.
3. Point Codex at the repository root so it can read `skills/`, `references/`, and `docs/`.

## Repository structure

```text
.
├── .codex-plugin/
├── AGENTS.md
├── docs/
├── references/
├── references/source-of-truth/
├── skills/
├── LICENSE
└── MIGRATION_REPORT.md
```

## Available skills

- `oguc-coeficientes`
- `due-diligence-normativa`
- `chile-due-diligence-report`
- `prc-rasantes-altura`
- `informe-tecnico-preliminar`
- `checklist-cumplimiento`
- `nch433-analisis`
- `nch461-refuerzo`
- `ces-calculo`
- `estacionamientos-ds-50`
- `edificios-esenciales-ds61`
- `envolvente-3d-oguc`

## How to use

Use the skill that matches the task, then provide the minimum useful inputs.

Examples:

```text
Analyze this site for OGUC coefficients using the area and zoning note provided.
Prepare a normative due diligence summary for this Rol SII and list missing documents.
Consolidate the due diligence findings into a client-ready risk report.
Review rasantes and height constraints for this PRC excerpt.
Draft a preliminary technical report with assumptions, findings, and risks.
Run a compliance checklist and prioritize missing documents.
Provide a first-pass NCh433 seismic screening for this building.
Screen the retrofit implications of this existing structure under NCh461.
Prepare a preliminary CES-oriented energy review and identify improvement levers.
Estimate parking and accessibility implications under DS 50 for this mixed-use project.
Screen whether this use may qualify as an essential building under DS 61.
Summarize a conceptual OGUC envelope for this lot and identify open zoning questions.
```

## Limits

- This repository supports technical review, not final municipal approval.
- Regulatory conclusions require source verification.
- Legal or professional responsibility remains with the licensed professional in charge.
- If a PRC, OGUC article, or municipal rule is not directly supplied or verified, mark it as pending verification rather than guessing.
- For structural, electrical, sanitary, environmental, or patrimonial matters, contrast the primary legal text with the technically competent source before concluding.
- If missing data must be recovered, use `references/source-of-truth/` and follow `references/source-lookup-protocol.md`.

# Migration Report

## Summary

The repository was refactored from a Claude-oriented prompt library into a Codex-oriented plugin package with formal skills, references, and clear documentation.
It was then expanded with a normative source policy, a registry, and a review of source hierarchy.

## QA pass

- Consolidated duplicated README content into a single canonical install/use guide.
- Confirmed every skill directory has a valid `SKILL.md` frontmatter block.
- Checked the canonical package path is `.codex-plugin/plugin.json`.

## Changes made

- Added `.codex-plugin/plugin.json` as the plugin entrypoint.
- Added formal skills under `skills/`.
- Added `references/` for normative guardrails.
- Added `docs/ARCHITECTURE.md` and `docs/USAGE.md`.
- Added `AGENTS.md` with maintainer guidance.
- Added a second wave of skills for due diligence reporting, seismic screening, retrofit screening, and CES-oriented energy review.
- Added a third wave of skills for DS 50 parking, DS 61 essential-building screening, and OGUC envelope studies.
- Reworded documentation to remove unsupported claims and Claude-specific installation language.
- Added source policy, source directory review, normative registry, disclaimer, and change log.
- Added a `references/source-of-truth/` directory for authoritative source recovery.

## Files created

- `.codex-plugin/plugin.json`
- `skills/oguc-coeficientes/SKILL.md`
- `skills/due-diligence-normativa/SKILL.md`
- `skills/prc-rasantes-altura/SKILL.md`
- `skills/informe-tecnico-preliminar/SKILL.md`
- `skills/checklist-cumplimiento/SKILL.md`
- `skills/chile-due-diligence-report/SKILL.md`
- `skills/nch433-analisis/SKILL.md`
- `skills/nch461-refuerzo/SKILL.md`
- `skills/ces-calculo/SKILL.md`
- `skills/estacionamientos-ds-50/SKILL.md`
- `skills/edificios-esenciales-ds61/SKILL.md`
- `skills/envolvente-3d-oguc/SKILL.md`
- `skills/README.md`
- `references/normativa-notes.md`
- `references/source-policy.md`
- `references/source-categories.yml`
- `references/normative-registry.yml`
- `references/source-directory-reviewed.md`
- `references/disclaimer-profesional-chile.md`
- `references/change-log.md`
- `references/source-of-truth/README.md`
- `docs/ARCHITECTURE.md`
- `docs/USAGE.md`
- `docs/NORMATIVE_AUDIT.md`
- `AGENTS.md`
- `MIGRATION_REPORT.md`
- `references/urbanismo-base/README.md`
- `references/accesibilidad/README.md`
- `references/estructuras/README.md`
- `references/especialidades-electricas/README.md`
- `references/habitabilidad-energia/README.md`
- `references/copropiedad/README.md`
- `references/ambiental-patrimonio/README.md`
- `references/infraestructura-digital-energetica/README.md`

## Files removed or deprecated

- The old Claude plugin manifest path is no longer the canonical entrypoint.
- The old agent/plugin hierarchy is deprecated as the main technical interface.

## Design decisions

- Kept the skill set intentionally small and operational.
- Preserved the useful Chilean domain content, but removed overconfident legal phrasing.
- Used conservative wording for normative claims and disclaimers.
- Avoided inventing a complex plugin graph before the core package is stable.

## Risks pending

- Exact canonical URLs for every registry item still need verification before external publication.
- Some specialty topics remain represented by screening skills rather than design-grade tools.
- Future updates must keep the registry and change log synchronized when norms change.

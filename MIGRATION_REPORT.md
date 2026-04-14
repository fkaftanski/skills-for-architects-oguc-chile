# Migration Report

## Summary

The repository was refactored from a Claude-oriented prompt library into a Codex-oriented plugin package with formal skills, references, and clear documentation.

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
- Added `.agents/plugins/marketplace.json` as a local marketplace example.
- Added a second wave of skills for due diligence reporting, seismic screening, retrofit screening, and CES-oriented energy review.
- Added a third wave of skills for DS 50 parking, DS 61 essential-building screening, and OGUC envelope studies.
- Reworded documentation to remove unsupported claims and Claude-specific installation language.

## Files created

- `.codex-plugin/plugin.json`
- `.agents/plugins/marketplace.json`
- `skills/oguc-coeficientes/SKILL.md`
- `skills/due-diligence-normativa/SKILL.md`
- `skills/prc-rasantes-altura/SKILL.md`
- `skills/informe-tecnico-preliminar/SKILL.md`
- `skills/checklist-cumplimiento/SKILL.md`
- `skills/README.md`
- `references/normativa-notes.md`
- `docs/ARCHITECTURE.md`
- `docs/USAGE.md`
- `AGENTS.md`
- `MIGRATION_REPORT.md`

## Files removed or deprecated

- The old Claude plugin manifest path is no longer the canonical entrypoint.
- The old agent/plugin hierarchy is deprecated as the main technical interface.

## Design decisions

- Kept the skill set intentionally small and operational.
- Preserved the useful Chilean domain content, but removed overconfident legal phrasing.
- Used conservative wording for normative claims and disclaimers.
- Avoided inventing a complex plugin graph before the core package is stable.

## Risks pending

- Some legacy files still exist in the repo tree and can be removed in a follow-up cleanup pass.
- The repository still contains historical content that is not part of the new canonical Codex path.
- The skills are intentionally narrow and may need expansion after real usage feedback.

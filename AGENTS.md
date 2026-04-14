# AGENTS.md

## Purpose

This repo packages Chile-specific architectural workflows for Codex.

## Normative principles

- Primary legal sources outrank interpretive, operational, referential, technical, and sectoral sources.
- Source category must be stated when it matters.
- DS 50 is treated as accessibility universal.
- Electrical consumer installations must use the RIC / Decreto 08 working frame, not Norma 4 as the primary reference.
- Disclaimers must be sober and must not cite weak or irrelevant legal bases.

## Structure convention

- Plugin manifest: `.codex-plugin/plugin.json`
- Skills: `skills/<skill-name>/SKILL.md`
- References: `references/`
- Recovery directory: `references/source-of-truth/`
- Lookup protocol: `references/source-lookup-protocol.md`
- Documentation: `docs/`

## Validation

- Keep manifests valid JSON.
- Keep each skill narrowly scoped and operational.
- Check that the README matches the actual tree.
- Prefer explicit gaps over implied certainty.
- Resolve missing data through the source lookup protocol before answering.
- Run `make validate-registry` when editing `references/normative-registry.yml` or normative skills.

## Editorial restrictions

- Avoid legal overclaims.
- Do not state that a workflow replaces human review.
- Keep references to OGUC/PRC/NCh/DS precise and conservative.
- Do not use hardcoded vigency phrases unless they are attached to a registry entry or a dated source.
- For predial or communal questions, contrast the official norm with the local instrument before concluding.
- Do not treat the recovery directory as a normative source; it is a lookup aid.

## Done criteria

- The plugin loads from `.codex-plugin/plugin.json`.
- Each skill has valid frontmatter.
- Documentation explains install, use, and limits.
- No obsolete Claude-specific structure is required for basic use.
- Any normative answer can name its source category and hierarchy.
- Missing data can be recovered from `references/source-of-truth/` using a documented sequence.

# AGENTS.md

## Purpose

This repo packages Chile-specific architectural workflows for Codex.

## Structure convention

- Plugin manifest: `.codex-plugin/plugin.json`
- Skills: `skills/<skill-name>/SKILL.md`
- References: `references/`
- Documentation: `docs/`

## Validation

- Keep manifests valid JSON.
- Keep each skill narrowly scoped and operational.
- Check that the README matches the actual tree.
- Prefer explicit gaps over implied certainty.

## Editorial restrictions

- Avoid legal overclaims.
- Do not state that a workflow replaces human review.
- Keep references to OGUC/PRC/NCh/DS precise and conservative.

## Done criteria

- The plugin loads from `.codex-plugin/plugin.json`.
- Each skill has valid frontmatter.
- Documentation explains install, use, and limits.
- No obsolete Claude-specific structure is required for basic use.

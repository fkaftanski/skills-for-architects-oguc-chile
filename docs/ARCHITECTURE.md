# Architecture

## Purpose

This repository packages Chile-focused architectural assistance as a Codex plugin with reusable skills.

## Structure

- `.codex-plugin/plugin.json` - plugin manifest for Codex
- `skills/<skill-name>/SKILL.md` - reusable task-specific skills
- `references/` - normative notes and guardrails
- `docs/` - usage and architecture documentation

## Reference layers

- `references/source-policy.md` - source hierarchy and allowed use cases
- `references/normative-registry.yml` - central registry of legal and technical bodies
- `references/source-directory-reviewed.md` - reviewed directory with keep/exclude decisions
- `references/disclaimer-profesional-chile.md` - reusable professional disclaimer
- `references/change-log.md` - normative change log

## Design decisions

- Keep the plugin manifest minimal.
- Keep skills narrowly scoped and operational.
- Separate normative guidance from reusable behavior.
- Prefer conservative wording over legal certainty.

## Non-goals

- This repo does not attempt to encode all OGUC or PRC rules exhaustively.
- This repo does not replace professional review or municipal approval.
- This repo does not promote secondary or sectoral sources to primary status.

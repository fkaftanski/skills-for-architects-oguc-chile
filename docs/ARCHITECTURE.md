# Architecture

## Purpose

This repository packages Chile-focused architectural assistance as a Codex plugin with reusable skills.

## Structure

- `.codex-plugin/plugin.json` - plugin manifest for Codex
- `skills/<skill-name>/SKILL.md` - reusable task-specific skills
- `references/` - normative notes and guardrails
- `docs/` - usage and architecture documentation

## Design decisions

- Keep the plugin manifest minimal.
- Keep skills narrowly scoped and operational.
- Separate normative guidance from reusable behavior.
- Prefer conservative wording over legal certainty.

## Non-goals

- This repo does not attempt to encode all OGUC or PRC rules exhaustively.
- This repo does not replace professional review or municipal approval.

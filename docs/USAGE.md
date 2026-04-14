# Usage

## Installation

1. Place the repository in a local workspace.
2. Load the plugin from `.codex-plugin/plugin.json`.
3. Point Codex to the repo so it can resolve `skills/` and `references/`.
4. Use `references/normative-registry.yml` as the first stop when a question depends on source hierarchy or vigency.

## Example prompts

- `Analyze the property under OGUC coefficients for Las Condes using the provided site area and zoning note.`
- `Prepare a normative due diligence summary for this Rol SII with the attached documents.`
- `Consolidate the due diligence findings into a client-ready risk report.`
- `Review rasantes and height constraints for this PRC excerpt and identify gaps.`
- `Draft a preliminary technical report with assumptions, findings, and risks.`
- `Run a compliance checklist for the project package and list missing documents first.`
- `Provide a first-pass NCh433 seismic screening for this building.`
- `Screen the retrofit implications of this existing structure under NCh461.`
- `Prepare a preliminary CES-oriented energy review and identify improvement levers.`
- `Estimate parking and accessibility implications under DS 50 for this mixed-use project.`
- `Screen whether this use may qualify as an essential building under DS 61.`
- `Summarize a conceptual OGUC envelope for this lot and identify open zoning questions.`

## Validation workflow

1. Check that every `SKILL.md` has valid frontmatter.
2. Confirm `.codex-plugin/plugin.json` exists and is valid JSON.
3. Ensure docs do not reference obsolete Claude-specific paths.
4. Verify the repo tree matches the documentation.
5. For any normative response, identify the source category before answering.
6. When a rule or decree is updated, add the change to `references/change-log.md` and the registry.
7. When data is missing, use `references/source-of-truth/` to locate a verified official source before answering.
8. Follow `references/source-lookup-protocol.md` when choosing between primary, interpretive, operational, referential, technical, or secondary sources.

# Source Policy

## Purpose

This repository uses a source hierarchy to prevent secondary or contextual sources from being treated as primary normative authority.

## Source categories

### primary_legal

- Definition: Official legal or regulatory text published by the competent authority or the official legal repository.
- Confidence: highest
- Use cases: binding norm, baseline regulatory text, explicit legal wording.
- Prohibitions: do not replace with summaries, blogs, or commentary.
- Priority in skills: first choice for normative claims.

### official_interpretive

- Definition: Official circulars, instructions, or interpretive guidance issued by the competent authority.
- Confidence: high
- Use cases: application criteria, administrative interpretation, operational guidance.
- Prohibitions: do not treat as the law itself when the text is interpretive.
- Priority in skills: second choice after primary legal text.

### official_operational

- Definition: Official operational portals, service desks, or technical platforms used to process or query official procedures.
- Confidence: medium-high
- Use cases: forms, status checks, operational lookups, submission workflows.
- Prohibitions: do not cite as the source of the legal rule itself.
- Priority in skills: support evidence, not rule creation.

### official_referential

- Definition: Official maps, visors, indexes, or search tools that provide reference context but are not in themselves binding norms.
- Confidence: medium
- Use cases: locate IPT, visualize boundaries, orient the user.
- Prohibitions: do not convert referential data into binding values without verifying the underlying source.
- Priority in skills: context only.

### technical_reference

- Definition: Technical standards, registries, and competent technical references from recognized technical bodies.
- Confidence: medium-high
- Use cases: engineering, installations, performance criteria, technical methodology.
- Prohibitions: do not present as legal authority unless the legal framework explicitly incorporates it.
- Priority in skills: specialty-specific technical support.

### sectoral_secondary

- Definition: Sectoral or gremial sources that may be useful for practice but are not authoritative normative sources.
- Confidence: medium-low
- Use cases: context, market practices, industry interpretation.
- Prohibitions: do not use as the basis for binding normative conclusions.
- Priority in skills: background only.

### exclude_from_core

- Definition: Sources that may be useful for context but must not feed automatic normative answers.
- Confidence: low for normative use
- Use cases: general background, external commentary, or non-authoritative context.
- Prohibitions: do not use as a primary normative source.
- Priority in skills: excluded from core normative flow.

## Operating rules

- Priority order: `primary_legal` -> `official_interpretive` -> `official_operational` -> `official_referential` -> `technical_reference` -> `sectoral_secondary` -> `exclude_from_core`.
- If a response uses a non-primary category, the response must say so explicitly.
- If source hierarchy is ambiguous, default to the more conservative classification.
- Predial or communal queries must contrast the official norm with the local instrument before giving a categorical answer.
- Structural, electrical, sanitary, or environmental claims must be checked against the technically competent source before stating a conclusion.
- Skills may use `references/source-of-truth/` as the recovery directory for missing data.
- Skills should follow `references/source-lookup-protocol.md` when recovering missing data.

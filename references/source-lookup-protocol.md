# Source Lookup Protocol

## Purpose

This protocol defines how skills should recover missing data without violating source hierarchy.

## Lookup sequence

1. Check `references/normative-registry.yml` for the normative body or topic.
2. If the needed detail is missing, consult `references/source-of-truth/`.
3. Prefer the smallest authoritative source that resolves the question.
4. If multiple sources conflict, use the higher-ranked source from `references/source-policy.md`.

## Category handling

### primary_legal

- Use directly for the normative rule.
- Do not downgrade or paraphrase into uncertainty unless the text itself is ambiguous.

### official_interpretive

- Use when the question is about application or administrative criteria.
- State that the answer is interpretive, not the legal text itself.

### official_operational

- Use to locate or verify a process, filing, status, or operational requirement.
- Do not use as the source of the rule itself.

### official_referential

- Use to orient the user, locate a jurisdiction, or identify a document.
- Do not infer binding values from it without a primary source.

### technical_reference

- Use for technical screening in the domain of the competent body.
- Do not convert a technical reference into a legal rule unless the legal framework explicitly incorporates it.

### sectoral_secondary

- Use only for background context.
- Never use as the sole basis for a normative conclusion.

### exclude_from_core

- Do not use in automatic normative answers.
- Only keep as optional context when explicitly requested.

## Escalation rules

- If the query is predial or communal, verify the local instrument after the national source.
- If the query is structural, electrical, sanitary, environmental, or patrimonial, verify the competent technical or legal source before concluding.
- If the registry or source-of-truth directory cannot resolve the matter, mark the answer as pending verification.

## Required output behavior

- Identify the source category used.
- Name the registry item or source-of-truth portal consulted.
- State whether the answer is direct, interpretive, operational, referential, or technical.
- Avoid categorical claims when the source is not primary or not verified.

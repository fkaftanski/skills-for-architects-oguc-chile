# Architecture Studio - OGUC Chile Edition

This repository is a Codex-oriented knowledge package for Chilean architecture, urbanism, and related technical review workflows. It combines reusable skills, a normative registry, a source hierarchy, and a curated recovery directory for missing data.

## Beta status and scope

This repository is in beta.

It is designed for:

- first-pass OGUC and PRC review
- normative due diligence
- preliminary technical reporting
- document and compliance gap checks
- screening-level structural, accessibility, energy, and envelope workflows

It is not designed to replace:

- municipal verification
- local instrument review
- specialty calculations
- professional judgment by the competent architect, engineer, or advisor

## Source policy

The repository uses a strict source hierarchy.

- Primary legal sources outrank every other category.
- Official interpretive sources may guide application, but do not replace the legal text.
- Official operational and referential sources are used to locate, verify, or support data, not to create binding rules.
- Technical references support specialty screening, but do not become legal authority unless the legal framework incorporates them.
- Sectoral or gremial sources are context only.

Core files:

- [`references/source-policy.md`](/home/fkaftanski/skills-for-architects-oguc-chile/references/source-policy.md)
- [`references/source-categories.yml`](/home/fkaftanski/skills-for-architects-oguc-chile/references/source-categories.yml)
- [`references/normative-registry.yml`](/home/fkaftanski/skills-for-architects-oguc-chile/references/normative-registry.yml)
- [`references/source-lookup-protocol.md`](/home/fkaftanski/skills-for-architects-oguc-chile/references/source-lookup-protocol.md)
- [`references/source-of-truth/README.md`](</home/fkaftanski/skills-for-architects-oguc-chile/references/source-of-truth/README.md>)

## Current repository structure

```text
.
├── .codex-plugin/
├── AGENTS.md
├── FINAL_AUDIT_REPORT.md
├── MIGRATION_REPORT.md
├── docs/
├── references/
│   ├── normative-registry.yml
│   ├── source-policy.md
│   ├── source-categories.yml
│   ├── source-directory-reviewed.md
│   ├── source-lookup-protocol.md
│   ├── source-of-truth/
│   └── domain folders
└── skills/
```

The active plugin manifest is [`/.codex-plugin/plugin.json`](/home/fkaftanski/skills-for-architects-oguc-chile/.codex-plugin/plugin.json).

The current skill surface is documented in [`skills/README.md`](/home/fkaftanski/skills-for-architects-oguc-chile/skills/README.md).

## Real compatibility

Supported target:

- Codex or a local workflow that can read this repository as a file-based plugin/skills package

Partially usable:

- other AI environments that can consume the markdown files manually

Not guaranteed:

- one-click installation in third-party desktop tools
- automatic plugin discovery outside the Codex-oriented structure
- any environment that expects the old Claude plugin format

For actual usage and validation steps, see [`docs/USAGE.md`](/home/fkaftanski/skills-for-architects-oguc-chile/docs/USAGE.md).

## System limits

- Predial and communal answers remain provisional until the applicable local instrument is verified.
- Structural, electrical, sanitary, environmental, patrimonial, and similar specialty matters require contrast with the competent technical source and the professional competent for the matter.
- The repository is intentionally screening-oriented in several domains.
- The recovery directory `references/source-of-truth/` is curated, but not flat in authority. Skills must still apply the source hierarchy.

## Maintaining vigency

This repository does not rely on hardcoded claims of vigency without a control mechanism.

When a norm, decree, circular, or technical frame changes:

1. update [`references/normative-registry.yml`](/home/fkaftanski/skills-for-architects-oguc-chile/references/normative-registry.yml)
2. update [`references/change-log.md`](/home/fkaftanski/skills-for-architects-oguc-chile/references/change-log.md)
3. run `make validate-registry`
4. review impacted skills and docs

The registry validator is defined in [`scripts/validate_registry.py`](/home/fkaftanski/skills-for-architects-oguc-chile/scripts/validate_registry.py).

## Professional warning

This repository is a technical and documentary support layer.

- It does not issue permits, approvals, or official rulings.
- It does not replace professional review, signature, or responsibility.
- If a source is missing or not verified, the answer should remain explicitly provisional.

The reusable wording lives in [`references/disclaimer-profesional-chile.md`](/home/fkaftanski/skills-for-architects-oguc-chile/references/disclaimer-profesional-chile.md).

#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required to run scripts/validate_registry.py", file=sys.stderr)
    print("Install it with: python3 -m pip install pyyaml", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "references" / "normative-registry.yml"
SKILLS_DIR = REPO_ROOT / "skills"

REQUIRED_FIELDS = {
    "id",
    "nombre",
    "tipo",
    "órgano",
    "materia",
    "estado",
    "jerarquía",
    "fecha_base",
    "última_actualización_conocida",
    "url_canónica",
    "fuente_primaria",
    "fuente_secundaria",
    "skill_owner",
    "notas_de_uso",
    "check_vigencia_required",
}

VALID_CATEGORIES = {
    "primary_legal",
    "official_interpretive",
    "official_operational",
    "official_referential",
    "technical_reference",
    "sectoral_secondary",
    "exclude_from_core",
}

# Token -> registry ids that satisfy the citation
CITED_NORMS = {
    "LGUC": {"lguc"},
    "OGUC": {"oguc-ds-47-1992"},
    "DDU": {"ddu"},
    "DS 50": {"ds-50-accesibilidad"},
    "DS50": {"ds-50-accesibilidad"},
    "DS 61": {"ds-61-sismica"},
    "DS61": {"ds-61-sismica"},
    "NCh433": {"nch433-2026"},
    "NCh461": {"nch461"},
    "RIC": {"ric-decreto-08"},
    "Decreto 08": {"ric-decreto-08"},
    "Ley 21.442": {"ley-21442-copropiedad", "reglamento-ley-21442"},
    "21.442": {"ley-21442-copropiedad", "reglamento-ley-21442"},
    "Ley 20.958": {"ley-20958"},
    "20.958": {"ley-20958"},
    "4.1.10": {"oguc-4-1-10-termica"},
    "Ley 21.305": {"ley-21305"},
    "21.305": {"ley-21305"},
    "DS 40": {"ds-40-2012-seia"},
    "DS40": {"ds-40-2012-seia"},
    "Ley 17.288": {"ley-17288-patrimonio"},
    "17.288": {"ley-17288-patrimonio"},
}


def load_registry() -> list[dict]:
    try:
        data = yaml.safe_load(REGISTRY_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: registry file not found: {REGISTRY_PATH}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(data, dict) or not isinstance(data.get("registry"), list):
        print("ERROR: references/normative-registry.yml must contain a top-level 'registry' list", file=sys.stderr)
        sys.exit(2)
    return data["registry"]


def load_skill_dirs() -> set[str]:
    return {p.name for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").exists()}


def validate_registry_entries(entries: list[dict], skill_dirs: set[str]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()

    for index, entry in enumerate(entries, start=1):
        label = entry.get("id", f"<missing-id-{index}>")
        if not isinstance(entry, dict):
            errors.append(f"registry entry #{index} is not a mapping")
            continue

        missing_fields = sorted(field for field in REQUIRED_FIELDS if field not in entry)
        if missing_fields:
            errors.append(f"{label}: missing required fields: {', '.join(missing_fields)}")

        entry_id = entry.get("id")
        if entry_id in seen_ids:
            errors.append(f"{label}: duplicate id")
        elif entry_id is not None:
            seen_ids.add(entry_id)

        category = entry.get("jerarquía")
        if category not in VALID_CATEGORIES:
            errors.append(f"{label}: invalid category '{category}'")

        url = entry.get("url_canónica")
        if not isinstance(url, str) or not url.strip():
            errors.append(f"{label}: url_canónica is empty")
        elif not re.match(r"^https?://", url):
            errors.append(f"{label}: url_canónica must start with http:// or https://")

        owner = entry.get("skill_owner")
        if owner and owner not in skill_dirs:
            errors.append(f"{label}: skill_owner '{owner}' does not exist under skills/")

        check_vigencia = entry.get("check_vigencia_required")
        if not isinstance(check_vigencia, bool):
            errors.append(f"{label}: check_vigencia_required must be boolean")

    return errors


def validate_skill_citations(registry_entries: list[dict]) -> list[str]:
    errors: list[str] = []
    registry_ids = {entry.get("id") for entry in registry_entries}

    for skill_file in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        cited_here: set[str] = set()
        for token, expected_ids in CITED_NORMS.items():
            if token in text:
                cited_here.update(expected_ids)
        missing = sorted(registry_id for registry_id in cited_here if registry_id not in registry_ids)
        if missing:
            errors.append(
                f"{skill_file.relative_to(REPO_ROOT)}: cites norms missing from registry: {', '.join(missing)}"
            )

    return errors


def main() -> int:
    registry_entries = load_registry()
    skill_dirs = load_skill_dirs()

    errors = []
    errors.extend(validate_registry_entries(registry_entries, skill_dirs))
    errors.extend(validate_skill_citations(registry_entries))

    if errors:
        print("Registry validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Registry validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Architecture Studio – OGUC Chile Edition

> Agents, skills y rules para arquitectos chilenos — 100 % adaptado a **OGUC, PRC, MINVU, NCh433, DS 50, DS 61, SII, Conservador, SEREMI y normativa nacional**.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**8 agents**, **42 skills**, **9 rules** y **3 hooks** organizados por ciclo de proyecto chileno.  
Creado por un **Arquitecto OGUC** con 15+ años de experiencia.

## Arquitectura (Chile)

```text
/studio → router OGUC
├── agents/ (8)
│   ├── site-planner
│   ├── chile-due-diligence-expert          ← NUEVO
│   ├── chile-zoning-expert                ← NUEVO
│   ├── workplace-strategist
│   ├── product-and-materials-researcher
│   ├── ffe-designer
│   ├── sustainability-specialist (adaptado DS 50 + CES)
│   └── brand-manager
├── plugins/ (11)
│   ├── 00-due-diligence-chile
│   ├── 01-site-planning-chile
│   ├── 02-zoning-oguc-prc                 ← NUEVO
│   ├── 03-programming
│   ├── 04-specifications
│   ├── 05-sustainability-chile
│   ├── 06-materials-research
│   ├── 07-presentations
│   ├── 08-normativa-sismica               ← NUEVO
│   ├── 09-eficiencia-energetica           ← NUEVO
│   └── 10-dispatcher-oguc
├── rules/ (9)
└── hooks/
```

## Instalación inmediata (Claude Desktop)

1. Abre **Customize** → **Browse plugins** → **+** → **Add marketplace from GitHub**
2. Ingresa: `TU_USUARIO/skills-for-architects-oguc-chile`

## Uso

```text
/studio Avenida Apoquindo 4500, Las Condes
/studio Due diligence Rol SII 123-45-6789
/studio Analiza este plano según OGUC y PRC Providencia
/studio Programa para oficina 120 personas
```

`/skills` para ver todo el menú.

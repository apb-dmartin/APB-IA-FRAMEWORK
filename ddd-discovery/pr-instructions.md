---
id: "ddd-pr-instructions-apim-v1.0"
name: "Instrucciones de PR — carga inicial de dominios"
description: >-
  Pasos para abrir el PR de la carga inicial de 21 dominios de negocio (modelo
  enriquecido con APB_KNOWLEDGE_BASE.md) en APB-DOMAIN-CATALOG. Fase 3 del
  protocolo apb-agent-ddd-v1.0 (Autonomy Level 1: el PR lo abre un humano).
type: "reference"
source: "apb-agent-ddd-v1.0 (ejecutor: Claude)"
last_updated: "2026-06-30"
status: "draft — pendiente autorización de Débora para commit/PR"
---

# Instrucciones de PR — carga inicial de dominios

> ⚠️ El agente DDD es **Autonomy Level 1**: no abre PRs ni hace commits. Estos pasos
> los ejecuta un humano cuando Débora lo autorice.

## Qué se ha generado (working tree del submodule APB-DOMAIN-CATALOG)

- `domains/<dominio>/domain.md` × 21 (estado `proposed`, `source: apb-agent-ddd-v1.0`,
  enriquecido con `APB_KNOWLEDGE_BASE.md`).
- `catalog/DOMAINS.md` actualizado (21 dominios propuestos).
- `scaffolding/scripts/validate_catalog.py` (nuevo — anti-repetición: valida
  `domain.md`/`bc-*.md` contra los esquemas; `21 dominios, 0 errores`, exit 0).

## Pasos para abrir el PR

```bash
cd "APB-DOMAIN-CATALOG"
git checkout -b feat/carga-inicial-dominios-apim   # ya existe — añadir commit nuevo
git add domains/ catalog/DOMAINS.md scaffolding/scripts/validate_catalog.py
git commit -m "feat: enriquecer dominios de negocio con APB_KNOWLEDGE_BASE.md (15 -> 21) + corregir SOJA"
git push -u origin feat/carga-inicial-dominios-apim
gh pr create --fill   # rellenar el PULL_REQUEST_TEMPLATE.md
```

## Checklist del PR (de PULL_REQUEST_TEMPLATE.md)

- [x] Revisado `catalog/DOMAINS.md` — no existían dominios equivalentes (catálogo vacío).
- [x] Archivos en `domains/<nombre>/domain.md`.
- [x] Campos REQUIRED rellenos; `status: proposed`; `proposed_date: 2026-06-30`.
- [x] `reviewer: "Arquitectura APB"`.
- [x] Generado por IA → `source: apb-agent-ddd-v1.0`.
- [x] `validate_catalog.py` → 21 dominios, 0 errores, exit 0.

## Para los revisores (Arquitectura APB + experto de negocio)

Decisiones de frontera pendientes (ver `notes` de cada `domain.md`):
1. **Operaciones Marítimas / Cruceros / Líneas Regulares** — ¿peer o subdominios?
   (requiere experto de negocio; Débora declinó decidirlo — preguntas en
   `interview-questions.md` A1–A2, D5–D7).
2. **Inspección y Control** INS vs PIF vs EQV — ¿1 dominio o varios?
3. **Suministros a Buques** MDE vs OPS — ¿1 dominio o 2?
4. **Transporte Terrestre / Ferrocarril** — ¿FER dominio propio confirmado?
5. **Integraciones Externas y EDI** — identificar el producto de cada API aún
   desconocida (DGS, ESF, ESM, FLO, IPB, MPA, MST, RESPONSIBLE, GPC, ROSS).
6. **Facturación** — confirmar clasificación supporting vs core.

## Nota de seguimiento (Débora, 2026-06-30)

Pendiente de abrir como punto de plan: **runtime de orquestación**. Esta sesión
se ejecutó manualmente (sin motor que invoque agentes/skills de forma programática
ni que fuerce la carga de providers declarados) — la causa raíz del error inicial
de SOJA fue precisamente que el ejecutor humano-en-el-bucle se saltó el paso
"cargar `prov-apb-knowledge-v1.0` antes de ejecutar" que el agente sí declara en
su frontmatter. Refuerza el punto #77 de `PLAN_FASES_FUTURAS.md` (Azure Durable
Functions / LangGraph / Temporal).

## Diferido a sesión futura

- **Bounded contexts** (`bc-*.md`): requieren acceso a código/BBDD
  (`apb-sub-ddd-code-v1.0` + `apb-sub-ddd-db-v1.0`).
- **Descomposición del monolito SOSTRAT** a DOCKS (Fase 1).

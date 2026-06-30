---
id: "ddd-pr-instructions-apim-v1.0"
name: "Instrucciones de PR — carga inicial de dominios"
description: >-
  Pasos para abrir el PR de la carga inicial de 15 dominios de negocio en
  APB-DOMAIN-CATALOG. Fase 3 del protocolo apb-agent-ddd-v1.0 (Autonomy Level 1:
  el PR lo abre un humano, no el agente).
type: "reference"
source: "apb-agent-ddd-v1.0 (ejecutor: Claude)"
last_updated: "2026-06-30"
status: "draft — pendiente autorización de Débora para commit/PR"
---

# Instrucciones de PR — carga inicial de dominios

> ⚠️ El agente DDD es **Autonomy Level 1**: no abre PRs ni hace commits. Estos pasos
> los ejecuta un humano cuando Débora lo autorice.

## Qué se ha generado (working tree del submodule APB-DOMAIN-CATALOG)

- `domains/<dominio>/domain.md` × 15 (estado `proposed`, `source: apb-agent-ddd-v1.0`).
- `catalog/DOMAINS.md` actualizado (15 dominios propuestos).

## Pasos para abrir el PR

```bash
cd "APB-DOMAIN-CATALOG"
git checkout -b feat/carga-inicial-dominios-apim
git add domains/ catalog/DOMAINS.md
git commit -m "feat: carga inicial de 15 dominios de negocio (Sesión Análisis Dominios)"
git push -u origin feat/carga-inicial-dominios-apim
gh pr create --fill   # rellenar el PULL_REQUEST_TEMPLATE.md
```

## Checklist del PR (de PULL_REQUEST_TEMPLATE.md)

- [x] Revisado `catalog/DOMAINS.md` — no existían dominios equivalentes (catálogo vacío).
- [x] Archivos en `domains/<nombre>/domain.md`.
- [x] Campos REQUIRED rellenos; `status: proposed`; `proposed_date: 2026-06-30`.
- [x] `reviewer: "Arquitectura APB"`.
- [x] Generado por IA → `source: apb-agent-ddd-v1.0`.

## Para los revisores (Arquitectura APB + experto de negocio)

Decisiones de frontera pendientes (ver `notes` de cada `domain.md`):
1. **Escalas / Cruceros / Líneas Regulares** — ¿peer o subdominios? (requiere
   experto de negocio; preguntas en `interview-questions.md` A1–A2, D5–D7).
2. **Inspección** INS vs PIF — ¿1 dominio o 2?
3. **Energía** MDE vs OPS — ¿1 dominio o 2?
4. **Transporte Terrestre** — ¿FER (ferrocarril) dominio propio?
5. **Integraciones de mercado** — identificar el producto de cada API
   (ROSS, GPC, DGS, ESF, ESM, FLO, IPB, MPA, MST, RESPONSIBLE) y reasignar si procede.
6. **Facturación** — confirmar clasificación supporting vs core.

## Diferido a sesión futura

- **Bounded contexts** (`bc-*.md`): requieren acceso a código/BBDD
  (`apb-sub-ddd-code-v1.0` + `apb-sub-ddd-db-v1.0`).
- **Descomposición del monolito SOSTRAT** a DOCKS (Fase 1).

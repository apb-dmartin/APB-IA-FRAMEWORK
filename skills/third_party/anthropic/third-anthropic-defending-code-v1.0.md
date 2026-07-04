---
id: "third-anthropic-defending-code-v1.0"
name: "Skill: Defending Code (Anthropic)"
description: "Adaptación de las skills oficiales de Anthropic para seguridad defensiva de código (anthropics/defending-code-reference-harness): threat-model, vuln-scan (SAST), triage, patch y customize. Enriquece el dominio security del framework para modelado de amenazas, escaneo estático, triaje/dedup de hallazgos y generación de parches candidatos — siempre con revisión humana. NO incluye el harness autónomo de escaneo (requiere sandbox gVisor, fuera del stack APB)."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad / Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
source_repo: "https://github.com/anthropics/defending-code-reference-harness"
source_license: "Apache 2.0"
source_commit: "b5b61c82144c70914ec330c20359b3e83bd65ef7"
created_date: "2026-07-04"
review_date: "2026-07-04"
---

# Skill: Defending Code (Anthropic)

---

## Descripción

Adaptación de las skills interactivas del repositorio **oficial de Anthropic**
`anthropics/defending-code-reference-harness` (Apache 2.0), un pipeline de referencia
para descubrimiento y remediación de vulnerabilidades con Claude. Este descriptor cubre
las **5 skills de lectura/análisis** aptas para uso sin sandbox:

| Skill original | Función |
|---|---|
| `/threat-model` | Construcción de modelos de amenaza sobre un código/servicio |
| `/vuln-scan` | Escaneo estático de vulnerabilidades (SAST) |
| `/triage` | Verificación, deduplicación y ranking de hallazgos de seguridad |
| `/patch` | Generación de parches candidatos (propuesta, no aplicación) |
| `/customize` | Adaptación del pipeline a otros lenguajes/frameworks |

> **Exclusión deliberada (decisión Arquitectura APB, 2026-07-04):** el **harness autónomo
> de escaneo** (pipeline de 7 etapas Recon→Find→Verify→Dedupe→Report→Patch) **no se
> incorpora** — rechaza ejecutarse fuera de un sandbox gVisor + Docker, infraestructura
> ajena al stack APB. Solo se adoptan las skills de análisis interactivo.

## Nota de gobernanza y solapes

- **Solape con `apb-sec-threat-model-v1.0` y `third-openai-threat-model-v1.0`:** el
  `/threat-model` de este repo es una alternativa/refuerzo, no un reemplazo — usar la skill
  APB como principal y esta como contraste de segunda opinión.
- **Complementa a [[apb-agent-quality-compliance-v1.0]] (#86):** los hallazgos de
  `/vuln-scan` y `/triage` son una fuente natural para el agente de cumplimiento de calidad
  (que ya deduplica contra Jira y ofrece PR).
- **`/vuln-scan` es SAST, no DAST:** no cierra el gap R10 (DAST/OWASP ZAP), que sigue abierto.
- **Frente a `mukul975/Anthropic-Cybersecurity-Skills`:** aquel repo (ya incorporado como
  `third-mukul-*`) **no es de Anthropic** pese al nombre; este sí. No se duplica: mukul aporta
  catálogo amplio mapeado a MITRE ATT&CK/NIST; este aporta el pipeline defensivo oficial.

## Adaptación APB

- Los parches de `/patch` son **propuestas** — nunca se aplican ni se mergean sin revisión
  humana (POLICY_AI_USAGE §6-7; principio SYSTEM.md §2.1 regla 2).
- Hallazgos Critical/High: no divulgar en canales no clasificados (GOVERNANCE.md §5).
- Requiere validación de **Ciberseguridad** antes de pasar de `draft` a `candidate`.

## Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-uso | Ciberseguridad | Autorización del alcance del escaneo/modelado |
| Post-hallazgos | Ciberseguridad / Arquitectura | Validación de severidad y del parche propuesto antes de cualquier PR |

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-04 | Arquitectura APB | Incorporación (Sesión 19, punto #79) — 5 skills de análisis, harness gVisor excluido |

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*

# APB AI Framework — Temas pendientes (handover)

> Lista consolidada. El detalle vivo está en `discovery/PLAN_FASES_FUTURAS.md` (planificación), `discovery/HANDOFF_TECNICOS.md` (framework) y `discovery/ddd-sostrat-mj8/HANDOFF_SOSTRAT.md` (SÒSTRAT). En caso de discrepancia, prevalecen esos documentos. Prioridad: 🔴 alta · 🟡 media · 🟢 baja.

## A. Seguridad y compliance
| ID | Tema | Prio |
|---|---|---|
| S0 | Verificar que `.env` (tokens SonarQube) nunca se commiteó; rotar tokens al traspasar | 🔴 |
| S1 | Co-aprobar los 5 componentes candidatos (two-eyes, Ciberseguridad) | 🔴 |
| #94 | Decidir destino de publicación de la serie DDD SÒSTRAT (el repo es **público**; contiene información de negocio) antes de cualquier `git push` | 🔴 |
| S3 | Auditar que el plugin M365 no expone credenciales AKV | 🟡 |
| S4 | Reducir scopes OAuth de adapter-rovo (`write:confluence-content` demasiado amplio) | 🟡 |
| S5 | Ejecutar `apb-gov-org-risk-report` por agente/skill antes de desplegar | 🟡 |
| S6 | Validar DPIA/clasificación de datos con DPO (RGPD art. 30/35, ENS) | 🟡 |
| S7 | Gestión de supply chain de 59 componentes de terceros sin SHA verificado | 🟡 |
| S8 | Desactivar GitHub Actions del repo deprecado `apb-ai-skills` | 🟢 |

## B. Gobernanza
- Arrancar el ciclo de aprobación: **0 componentes APB propios aprobados**. Definir revisores y calendario.
- Activar la revisión semestral y verificar que `review-reminder.yml` funciona.

## C. Decisiones de arquitectura abiertas
| Ref | Decisión |
|---|---|
| #77/#80 | Motor de orquestación (Durable Functions, LangGraph o Temporal) |
| N8 / MCP-1..4 | Runtime de producción de agentes; despliegue del MCP Server APB; prioridad de skills a exponer; viabilidad Rovo→MCP; routing por LLM (solo si hay caso real) |
| #49 / DS3 | Mecanismo de distribución del Design System (npm privado / submódulo / CDN) |
| #78 | Tagging `runtime: rovo` |
| #23, #36, #87, #52 | Conversión .docx, agentes de licitación LCSP, proceso de migración cloud, email oficial de Arquitectura |

## D. Evolución técnica
- Retrofit de telemetría en componentes existentes (Fase #43).
- Optimización de tokens: **nada implementado** (corregido en el plan).
- Tests de comportamiento de agentes (hoy solo validación estructural).
- Bump del submódulo `domain-catalog` (#95) tras revisar diff.
- Normalizar codificación UTF-8 de workflows con caracteres corruptos.
- Alinear el esquema de componentes con el parser de Mother Portal (contrato compartido).

## E. Descomposición SÒSTRAT (resumen; detalle en HANDOFF_SOSTRAT)
- #96 Validación humana de los 24 dossiers (único bloqueo de sprint planning).
- #98 9 consumidores externos no contemplados (APB.API.CPR, IPB, CTS, AUT, REB, LRT, OPS, CRE…) — decidir convivencia antes de extraer.
- #93 5 decisiones DDD bloqueantes (PIF+SCPP, parent_domain, Clavegueram, evidencia de Aguada, mismatch Trámites de Cliente→Administración electrónica).
- #97 7 apps sin dominio en el catálogo (DGT, MPS, MPT, NTA, ADV, FLU, RCF).

## F. Documentación
- Enlazar `docs/handover/` desde `README.md`/`CONTINUIDAD_PROYECTO.md` o fusionarlo en los canónicos (regla "sin docs sueltos").
- Cifras (367 componentes, 8/8 bugs) proceden de handoff de jul-2026: revalidar con `generate_catalog.py`.

## G. Orden sugerido (primeros 60 días)
1. S0 + #94 (higiene de secretos y publicación).
2. Arrancar aprobaciones (S1, B).
3. Decidir motor de orquestación y distribución del DS.
4. #96 validación de dossiers → desbloquea sprint planning.
5. Telemetría y tests.

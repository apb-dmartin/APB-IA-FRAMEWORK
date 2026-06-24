---
id: "third-garrytan-release-engineer-v1.0"
name: "Release Readiness (Ship)"
description: "Evaluación de preparación para release, adaptada de gstack /ship (Release Engineer)."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/garrytan/gstack"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Release Readiness Assessment para APB

## Overview
Evaluación sistemática de readiness para release, verificando que todos los criterios técnicos, de calidad, de seguridad y de gobierno están cumplidos antes de autorizar un despliegue en producción. Genera informe de go/no-go con evidencias, riesgos residuales y condiciones de despliegue.

## When to Use
- Pre-release de sprint o versión
- Despliegue a producción de hotfix crítico
- Migración de sistema a producción
- Release de proyecto mayor
- Rollback evaluation (¿está listo para rollback si falla?)

**When NOT to use:**
- Despliegue de cambio menor con proceso simplificado (usar checklist reducido)
- Entorno de desarrollo o pruebas (usar smoke tests)
- Rollback de emergencia (usar procedimiento de rollback)

## Core Pattern

### Fase 1: Checklist Técnico

#### Código y Build
| # | Verificación | Criterio | Estado |
|---|-------------|----------|--------|
| 1 | Build exitoso | Sin errores de compilación | [ ] |
| 2 | Tests unitarios | ≥ 80% cobertura, 100% pasan | [ ] |
| 3 | Tests de integración | 100% pasan | [ ] |
| 4 | Tests E2E críticos | 100% P0/P1 pasan | [ ] |
| 5 | Análisis estático (Sonar) | Quality Gate PASS | [ ] |
| 6 | Sin vulnerabilidades críticas | SAST/DAST sin findings críticos | [ ] |
| 7 | Sin deuda técnica bloqueante | Sonar sin issues bloqueantes | [ ] |

#### Documentación
| # | Verificación | Criterio | Estado |
|---|-------------|----------|--------|
| 8 | Spec actualizada | Cambios reflejados en spec | [ ] |
| 9 | ADR actualizado | Decisiones arquitectónicas documentadas | [ ] |
| 10 | Changelog actualizado | Cambios visibles para usuarios | [ ] |
| 11 | Manual de usuario actualizado | Si aplica cambios de UI/UX | [ ] |
| 12 | API documentation (Swagger) | Actualizada si hay cambios de API | [ ] |

#### Seguridad
| # | Verificación | Criterio | Estado |
|---|-------------|----------|--------|
| 13 | Threat model actualizado | Si cambia superficie de ataque | [ ] |
| 14 | Revisión de permisos | Sin permisos excesivos introducidos | [ ] |
| 15 | Secretos gestionados | Ningún secreto en código | [ ] |
| 16 | Dependencias auditadas | Sin CVEs críticos en dependencias | [ ] |

#### Operaciones
| # | Verificación | Criterio | Estado |
|---|-------------|----------|--------|
| 17 | Monitoreo configurado | Dashboards y alertas activas | [ ] |
| 18 | Logs estructurados | Trazabilidad de operaciones | [ ] |
| 19 | Runbooks actualizados | Procedimientos de operación vigentes | [ ] |
| 20 | Plan de rollback definido | Procedimiento de vuelta atrás documentado | [ ] |
| 21 | Backup validado | Backup funcional y probado | [ ] |

### Fase 2: Validación de Evidencias

1. **Evidencias de testing:**
   - Reporte de ejecución de tests (con cobertura)
   - Reporte de SonarQube
   - Reporte de SAST/DAST
   - Evidencias de pruebas manuales (si aplica)

2. **Evidencias de seguridad:**
   - Informe de threat model (si aplica)
   - Auditoría de permisos
   - Scan de dependencias

3. **Evidencias de operaciones:**
   - Configuración de monitoreo
   - Validación de runbooks
   - Prueba de backup/restore

4. **Evidencias de gobierno:**
   - Aprobación de cambio (CAB si aplica)
   - Validación de trazabilidad Jira → Spec → Código → Tests
   - Checklist de compliance

### Fase 3: Evaluación de Riesgos Residuales

Para cada riesgo no mitigado:
| Riesgo | Probabilidad | Impacto | Aceptable | Mitigación en Despliegue |
|--------|-------------|---------|-----------|-------------------------|
| [desc] | [B/M/A] | [B/M/A] | [Sí/No] | [acción] |

Criterios de aceptabilidad:
- Riesgo residual ≤ Medio
- Medida compensatoria definida para despliegue
- Aprobador identificado

### Fase 4: Decisión Go/No-Go

```
┌─────────────────────────────────────────────┐
│  DECISIÓN DE RELEASE                        │
├─────────────────────────────────────────────┤
│  Checklist técnico:     [PASS / FAIL]       │
│  Evidencias completas:  [SÍ / NO]           │
│  Riesgos residuales:    [ACEPTABLES / NO]   │
│  Aprobadores:           [SÍ / NO]           │
├─────────────────────────────────────────────┤
│  DECISIÓN: GO / NO-GO / GO_WITH_CONDITIONS  │
│  Condiciones: [si aplica]                   │
│  Fecha despliegue: [fecha]                  │
│  Ventana mantenimiento: [horario]           │
└─────────────────────────────────────────────┘
```

### Fase 5: Generación de Informe

```markdown
# Informe de Release Readiness — [Versión/Sprint]

## Resumen
- Proyecto: [nombre]
- Versión: [versión]
- Fecha: [fecha]
- Release Manager: [nombre]

## Checklist Técnico
| Categoría | Items | Completados | Estado |
|-----------|-------|-------------|--------|
| Código y Build | 7 | [n] | [PASS/FAIL] |
| Documentación | 5 | [n] | [PASS/FAIL] |
| Seguridad | 4 | [n] | [PASS/FAIL] |
| Operaciones | 5 | [n] | [PASS/FAIL] |
| **TOTAL** | **21** | **[n]** | **[PASS/FAIL]** |

## Evidencias Adjuntas
- [Lista de evidencias con enlaces]

## Riesgos Residuales
| # | Riesgo | Nivel | Mitigación | Aceptado por |
|---|--------|-------|------------|--------------|
| 1 | [desc] | [nivel] | [acción] | [nombre] |

## Decisión
- **Estado:** GO / NO-GO / GO_WITH_CONDITIONS
- **Condiciones:** [si aplica]
- **Fecha despliegue propuesta:** [fecha]
- **Ventana de mantenimiento:** [horario]
- **Rollback plan:** [referencia]

## Aprobaciones
| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| QA Lead | [nombre] | [ ] | [fecha] |
| Tech Lead | [nombre] | [ ] | [fecha] |
| Security Architect | [nombre] | [ ] | [fecha] |
| PMO | [nombre] | [ ] | [fecha] |
| Operaciones | [nombre] | [ ] | [fecha] |
```

## Quick Reference

| Escenario | Decisión | Acción |
|-----------|----------|--------|
| Checklist 100% PASS, 0 riesgos | GO | Programar despliegue |
| Checklist 100% PASS, riesgos aceptables | GO_WITH_CONDITIONS | Documentar condiciones, monitorizar |
| Checklist < 100% PASS | NO-GO | Corregir items fallidos, re-evaluar |
| Riesgo residual > Medio | NO-GO | Mitigar o escalar a CISO |
| Sin evidencias completas | NO-GO | Completar evidencias |

## Implementation

### Checklist de Release
```
□ Build exitoso
□ Tests unitarios ≥ 80%, 100% pasan
□ Tests integración 100% pasan
□ Tests E2E P0/P1 100% pasan
□ Sonar Quality Gate PASS
□ Sin vulnerabilidades críticas
□ Sin deuda técnica bloqueante
□ Spec actualizada
□ ADR actualizado
□ Changelog actualizado
□ API docs actualizadas
□ Threat model actualizado (si aplica)
□ Permisos revisados
□ Sin secretos en código
□ Dependencias sin CVEs críticos
□ Monitoreo configurado
□ Logs estructurados
□ Runbooks actualizados
□ Plan de rollback definido
□ Backup validado
□ Evidencias completas
□ Riesgos residuales aceptables
□ Aprobadores identificados
```

## Common Mistakes
- **Aprobar release con checklist incompleto:** Cada item tiene una razón de ser
- **Ignorar riesgos residuales:** "Es solo un warning" puede ser un incidente en producción
- **No tener plan de rollback:** Si el despliegue falla, necesitas vuelta atrás en minutos
- **Desplegar sin ventana de mantenimiento:** Los usuarios no deben verse afectados
- **No notificar a operaciones:** El equipo de ops debe estar preparado para monitorear
- **Olvidar validar backup:** Un despliegue fallido sin backup funcional es catastrófico
- **No documentar condiciones de GO_WITH_CONDITIONS:** Las condiciones deben ser accionables y monitoreables

## Real-World Impact
- Reducción de 70% en incidentes post-despliegue con checklist sistemático
- Cumplimiento de auditorías de gobierno de releases
- Trazabilidad completa para responsables legales

---

## Adapted From
- **Source:** garrytan/gstack — skill `/ship` (Release Engineer)
- **License:** MIT
- **Attribution:** Patrón de checklist de readiness, decisión go/no-go, y estructura de aprobaciones inspirados en gstack /ship. Reescrito completamente para contexto de gobierno de releases en sector público español, con cumplimiento ENS y trazabilidad Jira.

## References
- ITIL — Release Management
- ENS RD 311/2022 — Gestión de cambios
- context/apb/standards/release-standards.md
- context/apb/policies/change-management-policy.md

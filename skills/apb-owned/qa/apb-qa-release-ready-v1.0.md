---
id: "apb-qa-release-ready-v1.0"
name: "Release Readiness Assessment"
description: "Evaluar objetivamente si un producto o versión está listo para ser liberado a producción, verificando cumplimiento de criterios de calidad, funcionalidad, seguridad y operabilidad."
version: "1.0.0"
status: "draft"
owner: "QA / PMO APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Release Readiness Assessment

---

## 🎯 Propósito

Evaluar objetivamente si un producto o versión está listo para ser liberado a producción, verificando cumplimiento de criterios de calidad, funcionalidad, seguridad y operabilidad.

---

## ⚡ Trigger

Antes de cada release a producción, o cuando se solicita explicitamente un assessment de readiness.

---

## 📥 Input

- Scope del release (features, fixes, cambios)
- Resultados de testing (unit, integration, E2E, UAT)
- Métricas de calidad (SonarQube, cobertura, deuda técnica)
- Informes de seguridad (vulnerabilidades, pentest)
- Documentación técnica y de usuario actualizada
- Plan de rollback

---

## 📤 Output

- Informe de Release Readiness
- Estado: GO / NO-GO / GO con condiciones
- Lista de criterios cumplidos/no cumplidos
- Riesgos residuales
- Recomendaciones para release
- Acciones pendientes (si NO-GO o condicionado)

---

## 🔄 Proceso

1. **Checklist de criterios**: Verificar cada criterio de readiness definido.
2. **Revisión de testing**: Todos los tests requeridos ejecutados y pasados.
3. **Revisión de calidad**: Quality gate de SonarQube cumplido, cobertura ≥ 80%.
4. **Revisión de seguridad**: 0 vulnerabilidades críticas, pentest aprobado (si aplica).
5. **Revisión de documentación**: ADRs, manual de usuario, runbooks actualizados.
6. **Revisión de operabilidad**: Monitores, alertas, runbooks listos.
7. **Revisión de performance**: Benchmarks cumplen SLA.
8. **Stakeholder sign-off**: Aprobación de QA, seguridad, negocio.
9. **Decisión GO/NO-GO**: Documentar decisión y condiciones.

---

## 📋 Reglas y Constraints

- NO-GO si hay vulnerabilidades críticas sin mitigar.
- NO-GO si tests de regresión fallan.
- NO-GO si no hay plan de rollback documentado y probado.
- GO con condiciones si hay issues menores con plan de remediación post-release.
- Toda decisión GO/NO-GO debe ser documentada y comunicada a stakeholders.
- El Release Manager tiene autoridad para declarar NO-GO; no puede ser sobreescrito por presión de calendario.

---

## 🛠 Stack Tecnológico Relevante

- Azure DevOps / Jira (gestión de releases)
- SonarQube
- Azure Test Plans
- OWASP ZAP / SonarQube Security
- Application Insights

---

## 💡 Ejemplos de Uso

**Ejemplo — Assessment de release v2.3:**
> Criterios: 15/17 cumplidos.
> Pendiente: Documentación de API (en progreso, 1 día), 2 code smells menores.
> Riesgos: Bajo.
> Decisión: GO con condiciones. Documentación debe completarse antes de 48h post-release.

**Ejemplo — NO-GO:**
> Vulnerabilidad CRITICAL en dependencia log4j detectada.
> Tests de performance fallan (latencia P95 > 2s, SLA es 1s).
> Decisión: NO-GO. Plan de remediación: 3 días estimados.

---

## 🔗 Dependencias

- `apb-qa-test-plan-v1.0`
- `apb-qa-test-strategy-v1.0`
- `apb-ops-prr-v1.0`
- `apb-gov-compliance-v1.0`

---

## 📝 Notas

- El assessment debe ser objetivo y basado en evidencia, no en opiniones.
- Mantener histórico de assessments para análisis de tendencias de calidad.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

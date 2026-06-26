---
id: "apb-arch-tech-plan-v1.0"
name: "Generación de Plan Técnico"
description: "Generar un plan técnico detallado que traduzca las decisiones arquitectónicas en un roadmap ejecutable de implementación. Incluye fases, milestones, dependencias, riesgos y criterios de éxito."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Plan Técnico

---

## 🎯 Propósito

Generar un plan técnico detallado que traduzca las decisiones arquitectónicas en un roadmap ejecutable de implementación. Incluye fases, milestones, dependencias, riesgos y criterios de éxito.

---

## ⚡ Trigger

Tras aprobarse la arquitectura de un proyecto, o cuando se necesita planificar la implementación técnica de un epic/feature significativo.

---

## 📥 Input

- Documento de arquitectura aprobado
- ADRs generados
- Presupuesto y recursos disponibles
- Calendario de negocio (deadlines, eventos críticos)
- Dependencias con otros equipos/sistemas
- Riesgos técnicos identificados

---

## 📤 Output

- Plan técnico estructurado por fases
- Cronograma con milestones y dependencias
- Matriz de recursos (humanos y técnicos) por fase
- Plan de mitigación de riesgos
- Criterios de éxito y KPIs técnicos por fase
- Checklist de entregables por milestone
- Identificación de bloqueantes y dependencias externas

---

## 🔄 Proceso

1. **Descomposición en fases**: Dividir el trabajo en fases lógicas (foundation, core features, integration, stabilization, go-live).
2. **Definición de milestones**: Cada fase tiene milestones medibles (ej: 'API v1 deployada en staging', 'Integración con SAP validada').
3. **Estimación de esfuerzo**: T-shirt sizing o story points para cada tarea técnica. Identificar tareas críticas (ruta crítica).
4. **Asignación de recursos**: Equipo necesario por fase, competencias requeridas, gaps de formación.
5. **Análisis de dependencias**: Internas (otros equipos) y externas (terceros, aprobaciones). Crear matriz de dependencias.
6. **Gestión de riesgos**: Para cada riesgo identificado, definir probabilidad, impacto, mitigación y owner.
7. **Criterios de éxito**: Definir KPIs técnicos medibles por fase (coverage, performance, availability, etc.).
8. **Plan de comunicación**: Stakeholders a informar, frecuencia, formato.
9. **Revisión y ajuste**: Validar plan con equipo técnico y PMO. Ajustar según feedback.

---

## 📋 Reglas y Constraints

- El plan debe ser realista; incluir buffer del 20% para imprevistos en fases de integración.
- Cada milestone debe tener criterios de aceptación objetivos y verificables.
- Identificar la ruta crítica; cualquier retraso en ella impacta la fecha final.
- Incluir tiempo para deuda técnica y refactoring en cada fase (mínimo 10% del esfuerzo).
- Documentar supuestos explícitamente; si un supuesto cambia, replanificar.
- El plan debe incluir fase de 'hardening' antes de go-live (seguridad, performance, chaos testing).
- Revisar plan semanalmente durante la ejecución; actualizar si hay desviaciones > 10%.
- No comprometer fechas sin validar dependencias externas.

---

## 🛠 Stack Tecnológico Relevante

- Azure DevOps / Jira (gestión de trabajo)
- Gantt / Roadmap tools
- Azure Boards / GitHub Projects
- Excel / Sheets (matrices de riesgos y dependencias)

---

## 💡 Ejemplos de Uso

**Ejemplo — Plan de modernización (6 meses):**
> Fase 1 (Mes 1-2): Foundation — Scaffold microservicio base, CI/CD, observabilidad. Milestone: Pipeline verde, deploy en dev.
> Fase 2 (Mes 2-4): Core — Migrar módulo de facturación. Milestone: Paridad funcional con legacy en staging.
> Fase 3 (Mes 4-5): Integration — Conectar con SAP, AD, reporting. Milestone: E2E tests pasando.
> Fase 4 (Mes 5-6): Stabilization — Performance tuning, security audit, UAT. Milestone: Sign-off de QA y seguridad.
> Go-Live (Mes 6): Canary deployment 10% → 50% → 100%. Milestone: Métricas de error < 0.1%.

---

## 🔗 Dependencias

- `apb-arch-design-v1.0` (arquitectura base)
- `apb-plat-cicd-v1.0` (pipelines)
- `apb-qa-test-strategy-v1.0

---

## 📝 Notas

- El plan técnico es un documento vivo; debe actualizarse con cada sprint review.
- Diferenciar entre plan técnico (cómo construir) y plan de proyecto (cuándo entregar); esta skill se enfoca en el primero.
- Considerar usar ADR para decisiones de planificación que impacten arquitectura.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-tech-plan-v1.0) - pendiente validacion humana. No distribuir sin revision.

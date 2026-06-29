---
id: "apb-dev-review-tl-v1.0"
name: "Revisión Técnica de Tech Lead"
description: "Realiza revisiones técnicas de código y diseño desde la perspectiva de un Tech Lead: arquitectura, impacto, riesgo, mantenibilidad y alineación estratégica. Complementa, no sustituye, el code review de pares."
version: "1.1.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
created_date: "2026-06-20"
review_date: "2026-06-22"
autonomy_level: 1
depends_on:
  - "apb-dev-review-advanced-v1.0"
---

# Revisión Técnica de Tech Lead

> Esta skill incorpora, fusionados y adaptados, contenidos de la skill de terceros
> `gstack` (Garry Tan) bajo licencia MIT. Ver sección 9, Procedencia.

## 1. Propósito

Realizar revisiones técnicas de código y diseño desde la perspectiva de un Tech
Lead, enfocándose en calidad, mantenibilidad, alineación con estándares y riesgos
técnicos — un nivel más estratégico que el code review de pares estándar (que se
centra en bugs, estilo y tests tácticos).

## 2. Trigger

Antes de mergear una PR significativa, ante refactorizaciones arquitectónicas,
introducción de nuevos patrones/tecnologías, o decisiones técnicas de alto impacto.

## 3. Input / Output

**Input:** Pull Request o código a revisar, especificación técnica asociada,
arquitectura de referencia, estándares de codificación APB, historial de cambios.

**Output:** Informe de revisión técnica, evaluación de calidad, hallazgos de
arquitectura/diseño/código, riesgos técnicos, recomendaciones, estado final
(Aprobado / Aprobado con observaciones / Rechazado).

## 4. Dimensiones de Evaluación

| Dimensión | Peso | Qué evalúa |
|---|---|---|
| Arquitectura y diseño | 40% | Alineación con arquitectura existente, cohesión/acoplamiento, extensibilidad, escalabilidad, consistencia |
| Impacto y riesgo | 30% | Blast radius, posibilidad de rollback, dependencias nuevas, deuda técnica, necesidad de migración |
| Mantenibilidad y operabilidad | 20% | Complejidad, observabilidad, documentación, facilidad de onboarding, calidad de tests |
| Alineación estratégica | 10% | Roadmap, stack tecnológico aprobado, distribución de conocimiento en el equipo |

## 5. Proceso

1. **Contexto** — revisar especificación y el "por qué" del cambio antes del "qué".
2. **Arquitectura** (~15 min) — verificar límites de capas, patrones (DDD, Clean
   Architecture, CQRS), violaciones de SOLID.
3. **Impacto** (~10 min) — archivos afectados, cambios breaking, riesgo de deploy,
   dependencias nuevas (licencias, mantenimiento).
4. **Calidad de código** (~10 min) — lógica de negocio, nombres/abstracciones,
   manejo de errores, tests.
5. **Operabilidad** (~5 min) — observabilidad, configuración, performance, seguridad.
6. **Documentación** (~5 min) — ADRs, documentación de API, runbooks, changelog.
7. **Feedback estructurado** — comentarios clasificados (ver sección 6).
8. **Decisión** — aprobar, aprobar con observaciones, o rechazar con justificación.

## 6. Formato de Feedback

```
[Nivel] [Categoría] [Impacto]: Descripción

[CRITICAL] [Architecture] [High]: El nuevo servicio accede directamente a la
DB de otro bounded context. Usar API o eventos para comunicación.

[SUGGESTION] [Design] [Medium]: El método tiene 80 líneas y 5 responsabilidades.
Extraer validación, cálculo y notificación a servicios dedicados.

[QUESTION] [Impact] [Low]: ¿Por qué Redis sobre Memcached? ¿Hay métricas que
justifiquen la complejidad adicional?

[PRAISE] [Maintainability] [N/A]: Excelente uso de Strategy pattern, extensible
y testeable.
```

**Niveles:** `CRITICAL` (bloquea merge) · `MAJOR` (corregir, puede mergear con
plan) · `SUGGESTION` (mejora opcional) · `QUESTION` (necesita clarificación) ·
`PRAISE` (refuerzo positivo).

## 7. Checklist Tech Lead Review

**Arquitectura**
- [ ] Respeta los límites de capas (domain, application, infrastructure).
- [ ] Las abstracciones están al nivel correcto.
- [ ] No hay leakage de infraestructura en el dominio.
- [ ] Los bounded contexts y domain events son coherentes.

**Impacto**
- [ ] Cambios breaking en APIs versionados correctamente.
- [ ] Migración de datos con script testeado, si aplica.
- [ ] Dependencias nuevas con licencia compatible y justificadas.
- [ ] Plan de rollback / feature flag disponible.

**Operabilidad y seguridad**
- [ ] Métricas y alerts para detectar fallos.
- [ ] Logs estructurados; secrets en vault, nunca en código.
- [ ] Autenticación/autorización implementadas; inputs validados.
- [ ] Rate limiting en APIs públicas; cumplimiento GDPR si aplica.

**Testing y documentación**
- [ ] Cobertura de tests unitarios > 80% en lógica de negocio.
- [ ] Tests de integración y E2E para flujos críticos.
- [ ] ADRs y documentación de API actualizadas.
- [ ] CHANGELOG con breaking changes y guía de migración.

## 8. Reglas y Constraints

- Ser constructivo: el objetivo es mejorar el código y al desarrollador.
- Distinguir preferencia personal de estándar objetivo.
- No aprobar código sin tests asociados, salvo excepción documentada.
- No aprobar código que rompe contratos API/eventos sin plan de migración.
- Si el cambio supera 500 líneas, sugerir dividir en PRs más pequeños.
- El Tech Lead humano tiene la última palabra en decisiones arquitectónicas;
  esta skill asiste, no sustituye, el juicio humano.

## 9. Procedencia y Licencia

Las secciones 4 (dimensiones de evaluación), 6 (formato de feedback) y 7
(checklist) están adaptadas de la skill `gstack` de Garry Tan
(`github.com/garrytan/gstack`, licencia MIT). Referencias adicionales:
Google Engineering Practices (Code Review), Conventional Comments.

## 10. Dependencias

- `apb-dev-review-advanced-v1.0` — análisis estático y seguridad como input adicional.


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-dev-review-tl-v1.0) - pendiente validacion humana. No distribuir sin revision.

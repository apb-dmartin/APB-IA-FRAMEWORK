---
id: "apb-ops-operability-v1.0"
name: "Evaluación de Operabilidad"
description: "Evaluar la operabilidad de sistemas y servicios según los principios de Site Reliability Engineering (SRE). Identifica riesgos operacionales, propone mejoras en procedimientos de operación, y genera un informe de operabilidad con métricas y recomendaciones."
version: "1.0.0"
status: "draft"
owner: "SRE APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Evaluación de Operabilidad

## Propósito
Evaluar la operabilidad de sistemas y servicios según los principios de Site Reliability Engineering (SRE). Identifica riesgos operacionales, propone mejoras en procedimientos de operación, y genera un informe de operabilidad con métricas y recomendaciones.

## Contexto de Uso
- Evaluación de operabilidad antes del despliegue a producción.
- Revisión periódica de sistemas críticos para identificar deuda operacional.
- Preparación para Production Readiness Review (PRR).
- Integración con workflows de gobierno y release management.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `system_description` | Texto / Markdown | Descripción del sistema, arquitectura y componentes | ✅ |
| `operational_procedures` | Texto | Procedimientos actuales de operación (runbooks, playbooks) | ❌ |
| `incident_history` | Lista | Historial de incidencias recientes (últimos 6 meses) | ❌ |
| `observability_setup` | Texto | Configuración actual de monitoring, logging y alerting | ❌ |

## Flujo de Trabajo (Pasos)
1. **Análisis de arquitectura operacional**: Evaluar componentes, dependencias y puntos únicos de fallo.
2. **Evaluación de procedimientos**: Revisar runbooks, playbooks y procedimientos de escalado.
3. **Análisis de incidencias**: Identificar patrones de fallo recurrentes y tiempo medio de resolución (MTTR).
4. **Evaluación de observabilidad**: Verificar cobertura de métricas, logs, traces y alertas.
5. **Identificación de riesgos operacionales**:
   - Dependencias críticas sin redundancia.
   - Procedimientos manuales que deberían ser automatizados.
   - Alertas faltantes o con umbrales incorrectos.
   - Falta de documentación de troubleshooting.
6. **Generación de informe**: Documento con puntuación de operabilidad, riesgos y plan de mejora.
7. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe de Operabilidad — [Nombre Sistema]
> Fecha: [YYYY-MM-DD] | Autor: SRE Agent | Versión: 1.0.0

## 1. Alcance y Contexto
## 2. Evaluación de Arquitectura Operacional
## 3. Análisis de Procedimientos
## 4. Análisis de Incidencias
## 5. Evaluación de Observabilidad
## 6. Riesgos Operacionales Identificados
| ID | Riesgo | Severidad | Probabilidad | Impacto | Mitigación Propuesta |
## 7. Plan de Mejora
## 8. Recomendaciones
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los componentes del sistema evaluados para riesgos operacionales.
- [ ] Cada riesgo tiene severidad, probabilidad, impacto y mitigación propuesta.
- [ ] El informe incluye puntuación de operabilidad con benchmark histórico si aplica.
- [ ] Las recomendaciones son actionable con responsable sugerido y esfuerzo estimado.
- [ ] El informe es revisable por el equipo de operaciones sin intervención del agente.

## Stack y Tecnologías
- Framework: Google SRE Book, Azure Well-Architected Framework (Reliability pillar)
- Métricas: MTTR, MTBF, error rate, availability
- Formatos: Markdown, Excel para matriz de riesgos

## Dependencias
- `apb-ops-observability-v1.0` — para evaluación de observabilidad
- `apb-ops-prr-v1.0` — para contexto de Production Readiness Review
- `apb-gov-evidence-v1.0` — para generación de evidencia

## Ejemplo de Uso
**Prompt de invocación:**
```
Evalúa la operabilidad de nuestro microservicio de pagos:
- Descripción: ASP.NET Core 8, Azure Container Apps, Azure SQL, Service Bus
- Procedimientos: Runbook de escalado manual, playbook de failover
- Incidencias: 3 incidencias en últimos 3 meses (latencia elevada, timeout en BD, message loss)
- Observabilidad: Application Insights, Log Analytics, 5 alertas configuradas
```

## Notas y Advertencias
- **Nivel 1**: El agente evalúa documentalmente; no ejecuta pruebas de carga ni accede a entornos de producción.
- **Revisión humana obligatoria** antes de aprobar el informe de operabilidad.
- Las métricas de incidencias deben ser proporcionadas por el equipo de operaciones.
- El agente no tiene acceso a datos de producción ni a sistemas de monitoring reales.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-operability-v1.0) - pendiente validacion humana. No distribuir sin revision.

---
id: "apb-ops-rca-v1.0"
name: "Root Cause Analysis"
description: "Realizar análisis de causa raíz (RCA) de incidencias y problemas operacionales utilizando metodologías estructuradas (5 Whys, Ishikawa/Fishbone, Fault Tree Analysis). Genera un informe de RCA con causas contribuyentes, acciones correctivas y preventivas."
version: "1.0.0"
status: "draft"
owner: "SRE APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Root Cause Analysis


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Realizar análisis de causa raíz (RCA) de incidencias y problemas operacionales utilizando metodologías estructuradas (5 Whys, Ishikawa/Fishbone, Fault Tree Analysis). Genera un informe de RCA con causas contribuyentes, acciones correctivas y preventivas.

> **Diferencia clave con `apb-ops-incident-diagnose-v1.0`:**
> Esta skill es un análisis **post-incidente profundo** — se ejecuta **después** de que el servicio está restaurado. Su objetivo es identificar la causa raíz sistémica para evitar recurrencia (mejora continua, post-mortem, cambios arquitectónicos).
> `apb-ops-incident-diagnose-v1.0` es diagnóstico **táctico inmediato** que se realiza durante el incidente activo para proporcionar un runbook de resolución al técnico L1 en minutos.

## Contexto de Uso
- Post-incidente: análisis de causas tras resolución de incidencias críticas.
- Problemas recurrentes: identificación de causas raíz de fallos repetidos.
- Mejora continua: integración de lecciones aprendidas en procesos y arquitectura.
- Integración con gobierno y gestión de conocimiento.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `incident_description` | Texto | Descripción del incidente o problema | ✅ |
| `timeline` | Texto / Lista | Cronología de eventos desde detección hasta resolución | ✅ |
| `logs_and_metrics` | Texto / JSON | Logs, métricas y trazas relevantes al incidente | ✅ |
| `affected_systems` | Lista | Sistemas, servicios y usuarios afectados | ✅ |
| `previous_incidents` | Lista | Incidencias previas relacionadas | ❌ |

## Flujo de Trabajo (Pasos)
1. **Reconstrucción del incidente**: Documentar cronología completa con timestamps y fuentes.
2. **Identificación de síntomas vs causas**: Distinguir entre manifestaciones del problema y causas subyacentes.
3. **Aplicación de metodologías**:
   - **5 Whys**: Iterar "¿por qué?" hasta llegar a causa raíz.
   - **Ishikawa/Fishbone**: Clasificar causas en categorías (People, Process, Technology, Environment).
   - **Fault Tree Analysis**: Modelar combinaciones de fallos que llevan al incidente.
4. **Identificación de causas contribuyentes**: Factores que no son causa raíz pero agravaron el incidente.
5. **Análisis de gaps**: Detectar fallos en procesos, herramientas, documentación o formación.
6. **Definición de acciones**:
   - **Correctivas**: Acciones inmediatas para resolver el problema.
   - **Preventivas**: Acciones para evitar recurrencia.
   - **Proactivas**: Mejoras en procesos o arquitectura.
7. **Generación de informe RCA**: Documento estructurado con causa raíz, acciones y lecciones aprendidas.
8. **Registro de evidencia**: Metadatos para gobierno y gestión de conocimiento.

## Salida Esperada
### Estructura del Informe RCA
```markdown
# Root Cause Analysis — Incidente [ID]
> Fecha: [YYYY-MM-DD] | Autor: SRE Agent | Severidad: [S1/S2/S3/S4]

## 1. Resumen Ejecutivo
## 2. Descripción del Incidente
## 3. Timeline Detallado
## 4. Análisis de Causa Raíz
### 4.1 5 Whys
### 4.2 Fishbone Diagram
### 4.3 Fault Tree (si aplica)
## 5. Causas Contribuyentes
## 6. Acciones Correctivas
| ID | Acción | Tipo | Responsable | Plazo | Estado |
## 7. Acciones Preventivas
## 8. Lecciones Aprendidas
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] La causa raíz está claramente diferenciada de síntomas y causas contribuyentes.
- [ ] El análisis 5 Whys llega al menos 5 niveles de profundidad o hasta causa raíz identificada.
- [ ] Cada acción tiene responsable, plazo y tipo (correctiva/preventiva/proactiva).
- [ ] Las lecciones aprendidas están documentadas y vinculadas a runbooks o estándares.
- [ ] El informe es revisable por el equipo de operaciones y management sin intervención del agente.

## Stack y Tecnologías
- Metodologías: 5 Whys, Ishikawa, Fault Tree Analysis, STEP (Sequential Timed Events Plotting)
- Datos: Azure Monitor, Application Insights, Log Analytics (KQL)
- Formatos: Markdown, Mermaid para diagramas

## Dependencias
- `apb-ops-operability-v1.0` — para contexto de evaluación operacional
- `apb-sec-forensic-v1.0` — para análisis forense previo
- `apb-gov-evidence-v1.0` — para generación de evidencia
- `apb-gov-knowledge-v1.0` — para registro de lecciones aprendidas

## Ejemplo de Uso
**Prompt de invocación:**
```
Realiza RCA del incidente de caída del servicio de pagos:
- Incidente: S1-2026-0615 — Caída total del servicio de pagos durante 23 minutos
- Timeline: 03:15 alerta de latencia → 03:22 escalado → 03:38 identificación de deadlock en BD → 03:45 rollback → 03:58 recuperación
- Logs: [adjuntar logs de Application Insights y SQL]
- Sistemas afectados: API de pagos, BD de transacciones, notificador de eventos
- Incidencias previas relacionadas: S2-2026-0512 (latencia elevada en BD)
```

## Notas y Advertencias
- **Nivel 1**: El agente realiza análisis basado en información proporcionada; no accede a entornos de producción.
- **Revisión humana obligatoria** antes de cerrar el RCA y aprobar acciones.
- El RCA no es un ejercicio de culpabilización; se centra en sistemas y procesos, no en personas.
- Las acciones preventivas deben validarse con el equipo de arquitectura si implican cambios significativos.
- El agente no tiene acceso a datos personales en logs; trabaja con información anonimizada.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ **Borrador generado por IA** (APB AI Framework — apb-ops-rca-v1.0) — pendiente validación humana. No distribuir sin revisión.

---
id: "apb-doc-post-mortem-v1.0"
name: "Post-Mortem de Incidente (Blameless)"
description: "Conduce y documenta el post-mortem blameless de un incidente de producción en APB. Genera la plantilla de análisis de causa raíz (5 Whys + Fishbone), la línea de tiempo del incidente, los action items priorizados y el resumen ejecutivo para comunicar a dirección."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Post-Mortem de Incidente (Blameless)

## Propósito
Facilitar y documentar el análisis post-mortem de incidentes de producción en APB usando el enfoque "blameless" (sin culpables, orientado a mejora sistémica). Genera la estructura del análisis, guía la reconstrucción de la línea de tiempo, aplica la técnica de los 5 Whys para identificar causas raíz, y produce los action items concretos para prevenir la recurrencia. El resultado final incluye un resumen ejecutivo para comunicar a dirección.

## Contexto de Uso
- Análisis de cualquier incidente de producción con impacto en el servicio (P1 o P2).
- Revisión de incidentes menores recurrentes (varios P3 del mismo tipo → post-mortem preventivo).
- Reunión de post-mortem del equipo: estructura el debate y captura las conclusiones.
- Requerimiento de auditoría: documentación de gestión de incidentes para ENS o ISO 27001.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `incident_title` | Texto | Título descriptivo del incidente (ej. "Caída del API de GISPEM 4h el 15/06") | ✅ |
| `impact_description` | Texto | Impacto del incidente: usuarios afectados, funcionalidades no disponibles, tiempo de caída | ✅ |
| `timeline` | Lista | Cronología de eventos: timestamp + descripción de qué pasó y quién actuó | ✅ |
| `severity` | Enum | `P1` / `P2` / `P3` / `P4` | ✅ |
| `affected_systems` | Lista | Sistemas afectados | ❌ |
| `initial_hypothesis` | Texto | Hipótesis inicial del equipo sobre la causa raíz | ❌ |

## Definición de Severidad APB

| Severidad | Criterio | SLA resolución |
|---|---|---|
| **P1 — Crítico** | Sistema de producción completamente caído o con pérdida de datos | <4h |
| **P2 — Alto** | Funcionalidad crítica degradada o no disponible para >50% de usuarios | <8h |
| **P3 — Medio** | Funcionalidad secundaria no disponible o rendimiento degradado | <24h |
| **P4 — Bajo** | Incidencia menor sin impacto operativo significativo | <72h |

Post-mortem obligatorio para P1 y P2. Recomendado para P3 recurrentes.

## Flujo de Trabajo

### 1. Preparación del post-mortem

- **¿Cuándo?**: entre 24-72h después del cierre del incidente (mientras los detalles están frescos).
- **¿Quién?**: todos los que participaron en la resolución + responsable del sistema.
- **Principio blameless**: el objetivo es entender qué falló en el sistema, no quién se equivocó. Las personas actúan de la mejor manera posible con la información que tenían en ese momento.

### 2. Reconstrucción de la línea de tiempo

```
HHMM UTC | Actor | Evento
---------|-------|--------
08:32    | Monitor Azure | Alerta: error rate API > 5%
08:35    | Ingeniero de guardia | Alerta recibida, inicio de investigación
08:40    | Ingeniero de guardia | Identificado pod en CrashLoopBackOff
08:55    | Tech lead | Diagnóstico: memory limit excedido tras actualización de dependencia
09:10    | Tech lead | Rollback ejecutado con `kubectl rollout undo`
09:15    | Monitor Azure | Error rate < 1%, servicio restaurado
09:20    | Responsable de sistema | Confirmación de usuario que el servicio es operativo
```

### 3. Análisis de causa raíz (5 Whys)

```
Síntoma: El API de GISPEM no estaba disponible durante 43 minutos.

¿Por qué? → El pod estaba en CrashLoopBackOff
¿Por qué? → La aplicación superaba el memory limit configurado
¿Por qué? → La última versión de Newtonsoft.Json tiene un memory leak en el escenario de deserialización de arrays grandes
¿Por qué? → La actualización de la dependencia no incluía tests de regresión de rendimiento/memoria
¿Por qué? → El pipeline CI/CD no incluye gate de performance/memoria para dependencias actualizadas

CAUSA RAÍZ: Ausencia de gate de regresión de memoria en el pipeline CI/CD para actualizaciones de dependencias.
```

### 4. Action items (SMART)

| # | Acción | Responsable | Fecha límite | Prioridad |
|---|---|---|---|---|
| 1 | Añadir test de carga de memoria en pipeline CI/CD para actualizaciones de deps | {responsable} | 2026-07-15 | Alta |
| 2 | Configurar alerta de Memory Working Set en Azure Monitor (umbral: 80% del limit) | {responsable} | 2026-07-08 | Alta |
| 3 | Revisar memory limits de todos los pods de producción vs. uso real | {responsable} | 2026-07-31 | Media |
| 4 | Documentar el runbook de CrashLoopBackOff en el Wiki del equipo | {responsable} | 2026-07-31 | Baja |

### 5. Resumen ejecutivo (para dirección)

Máximo 1 página, sin jerga técnica:
- Qué pasó y cuánto tiempo duró la interrupción.
- Impacto real en el servicio y en los usuarios.
- Causa raíz (en lenguaje de negocio).
- Qué se está haciendo para que no vuelva a ocurrir.

## Salida Esperada

```markdown
# Post-Mortem — {incident_title}
> ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-post-mortem-v1.0) — completar con el equipo de guardia y revisar con el responsable del sistema.

## Resumen
| Atributo | Valor |
|---|---|
| Fecha y hora inicio | |
| Fecha y hora resolución | |
| Duración | |
| Severidad | |
| Sistemas afectados | |
| Usuarios afectados | |

## Línea de Tiempo
[...]

## Análisis de Causa Raíz (5 Whys)
[...]

## Factores contribuyentes
[...]

## Action Items
[...]

## Resumen Ejecutivo
[...]
```

## Criterios de Calidad
- [ ] La causa raíz es sistémica (un proceso, una herramienta, una práctica), no una persona.
- [ ] Los action items son SMART: específicos, medibles, asignados, con fecha.
- [ ] La línea de tiempo es objetiva: qué ocurrió, cuándo, quién actuó — sin juicios de valor.
- [ ] El resumen ejecutivo no contiene jerga técnica.
- [ ] El documento está completado y revisado antes de 5 días laborales tras el incidente.

## Ejemplo de Uso

```
Genera el post-mortem del incidente P1 del 15 de junio de 2026.
El API REST de GISPEM estuvo caído 43 minutos (08:32–09:15 UTC).
Causa identificada: memory leak en Newtonsoft.Json tras actualización.
Afectó a los operadores portuarios que no podían registrar el cierre de escalas.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `incident_title` | Pregunta: "¿Cuál es el título del incidente?" | Sí |
| `impact_description` | Pregunta: "¿Qué impacto tuvo el incidente? (usuarios afectados, tiempo de caída, funcionalidades no disponibles)" | Sí |
| `timeline` | Pregunta: "¿Puedes compartir la cronología del incidente con timestamps?" — genera la plantilla vacía si no hay datos | Sí |
| `severity` | Pregunta: "¿Cuál fue la severidad: P1, P2, P3 o P4?" | Sí |
| `affected_systems` | Infiere de la descripción del incidente e indica la inferencia | No |
| `initial_hypothesis` | Genera el análisis 5 Whys desde cero sin hipótesis previa | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos de post-mortem** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-doc-post-mortem-v1.0) — completar con el equipo de guardia y revisar con el responsable del sistema.

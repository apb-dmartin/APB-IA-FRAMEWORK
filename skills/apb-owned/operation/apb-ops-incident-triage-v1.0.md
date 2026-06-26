---
id: "apb-ops-incident-triage-v1.0"
name: "Triaje de Incidencias"
description: "Clasifica una incidencia técnica APB por prioridad (P1–P4), categoría ITIL e impacto en negocio. Identifica el componente afectado a partir de la descripción en lenguaje natural y determina si procede resolución L1 o escalado inmediato."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 2
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Triaje de Incidencias

---

## 🎯 Propósito

Clasificar y priorizar incidencias técnicas APB de forma sistemática y consistente, siguiendo la metodología ITIL y la política de SLA APB. Determina la prioridad (P1–P4), la categoría, el componente afectado y si la incidencia puede resolverse en L1 o debe escalarse inmediatamente.

---

## ⚡ Trigger

Cuando se recibe un nuevo reporte de incidencia, ya sea por ticket JSM, por Teams, por correo o por invocación directa del agente `apb-agent-incident-support-v1.0`.

---

## 📥 Input

- Descripción del síntoma (texto libre)
- Componente o sistema afectado (si se conoce)
- Número de usuarios/servicios afectados
- Hora de inicio del problema
- Impacto en procesos de negocio críticos (si se conoce)

---

## 📤 Output

- **Prioridad:** P1 / P2 / P3 / P4 con justificación
- **Categoría ITIL:** Infraestructura / Aplicación / Red / Base de datos / Seguridad / Acceso
- **Componente identificado:** nombre del sistema, servicio o capa afectada
- **SLA aplicable:** tiempo máximo de respuesta y resolución según política APB
- **Decisión de enrutamiento:** L1 (resoluble en soporte de primera línea) / L2 (requiere técnico especialista) / L3 (requiere proveedor o fabricante) / Major Incident (activar proceso de incidente mayor)
- **Campos JSM pre-cumplimentados:** listos para crear o actualizar el ticket

---

## 🔄 Proceso

1. **Extracción de síntoma:** identificar el sistema afectado, el error reportado y el alcance
2. **Clasificación de impacto:** número de usuarios afectados × criticidad del servicio
3. **Clasificación de urgencia:** tiempo hasta que el negocio se ve gravemente afectado
4. **Cálculo de prioridad:** matriz Impacto × Urgencia según política APB

| Urgencia ↓ / Impacto → | Alto (>20 usuarios o servicio crítico) | Medio (5-20 usuarios) | Bajo (<5 usuarios) |
|------------------------|---------------------------------------|-----------------------|-------------------|
| **Alta** (negocio parado) | P1 — Crítico | P2 — Alto | P3 — Medio |
| **Media** (degradado) | P2 — Alto | P3 — Medio | P3 — Medio |
| **Baja** (molestia) | P3 — Medio | P4 — Bajo | P4 — Bajo |

5. **Identificación de componente:** cruzar síntoma con catálogo de sistemas APB
6. **Decisión de enrutamiento:** L1 si existe runbook conocido; L2/L3/Major si no
7. **Pre-cumplimentación de campos JSM:** categoría, prioridad, componente, SLA, grupo asignado

---

## 📋 Reglas y Constraints

- P1 activa siempre el proceso de Major Incident Manager — no puede permanecer en L1
- Incidencias de seguridad (acceso no autorizado, ransomware, fuga de datos) son siempre P1 y se derivan al equipo de seguridad APB, no a soporte técnico
- Si el componente no puede identificarse con >60% de confianza, clasificar como "No determinado" y escalar a L2
- Los SLA APB son: P1 ≤15 min respuesta / 4h resolución; P2 ≤30 min / 8h; P3 ≤2h / 3 días hábiles; P4 ≤1 día hábil / 5 días hábiles
- Todos los campos del ticket JSM deben estar cumplimentados antes de asignar al grupo resolutor

---

## 🛠 Stack Tecnológico Relevante

- Jira Service Management (JSM) — sistema ITSM APB
- Jira (projects) — vinculación con tickets de desarrollo si la incidencia tiene origen en código
- Microsoft Teams — canal de comunicación de incidencias
- Catálogo de sistemas APB (referencia interna)

---

## 💡 Ejemplos de Uso

**Ejemplo — Incidencia P1:**
> "La pasarela de pagos del Puerto está caída desde las 08:00h. Ningún usuario puede procesar transacciones. Afecta a la operativa del día."
> → P1, Impacto Alto + Urgencia Alta, Componente: Pasarela de pagos, Acción: Major Incident Manager

**Ejemplo — Incidencia P3:**
> "El informe mensual de ocupación de muelles tarda 15 minutos en cargarse, antes tardaba 2. Solo afecta al analista de operaciones."
> → P3, Impacto Bajo + Urgencia Media, Componente: BI/Reporting, Acción: L2 (rendimiento BD)

---

## 🔗 Dependencias

- `apb-ops-incident-diagnose-v1.0` — siguiente skill en el flujo de resolución

---

## 📝 Notas

- La matriz de prioridad puede ajustarse si Operaciones APB publica una versión actualizada de la política de SLA
- Los sistemas marcados como "críticos" en el CMDB APB siempre suman +1 nivel de urgencia

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-incident-triage-v1.0) - pendiente validacion humana. No distribuir sin revision.

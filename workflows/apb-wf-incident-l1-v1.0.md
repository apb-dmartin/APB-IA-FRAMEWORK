---
id: "apb-wf-incident-l1-v1.0"
name: "Gestión de Incidencia L1"
description: "Workflow completo de gestión de incidencia técnica APB de primera línea: desde la recepción del reporte hasta la resolución o escalado. Orquesta triaje, diagnóstico, resolución y notificación en un flujo estructurado con gates de validación humana en los puntos críticos."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 2
agents:
  - "apb-agent-incident-support-v1.0"
skills:
  - "apb-ops-incident-triage-v1.0"
  - "apb-ops-incident-diagnose-v1.0"
  - "apb-ops-incident-escalate-v1.0"
  - "apb-plat-ms-notify-v1.0"
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Gestión de Incidencia L1

---

## 🎯 Propósito

Workflow que orquesta el ciclo completo de gestión de una incidencia técnica APB de primera línea, desde la recepción del reporte hasta el cierre o escalado formal. Garantiza consistencia en la clasificación, documentación y comunicación, y establece los gates de validación humana obligatorios en los puntos de mayor riesgo.

---

## 🗺 Diagrama del flujo

```
[Reporte de incidencia]
         ↓
   [1. TRIAJE]
   apb-ops-incident-triage-v1.0
         ↓
   ┌─────┴─────┐
   ↓           ↓
  P1        P2/P3/P4
   ↓           ↓
[Major Incident]  [2. DIAGNÓSTICO]
[Escalar inmediato] apb-ops-incident-diagnose-v1.0
                      ↓
               ┌──────┴──────┐
               ↓             ↓
         [Resoluble L1]  [No resoluble]
               ↓             ↓
     [3. GATE HUMANO]   [4. ESCALADO]
     Técnico confirma   apb-ops-incident-escalate-v1.0
     runbook antes de         ↓
     ejecutar           [Ticket asignado L2/L3]
               ↓             ↓
     [5. RESOLUCIÓN]    [Notificación al receptor]
     Técnico aplica           ↓
     runbook            [Notificación al solicitante]
               ↓
     [6. VERIFICACIÓN]
     Criterios de cierre cumplidos?
               ↓
     [7. CIERRE JSM]
     + Artículo base de conocimiento (si runbook nuevo)
               ↓
     [8. NOTIFICACIÓN FINAL]
     apb-plat-ms-notify-v1.0
```

---

## 📋 Pasos del workflow

### Paso 1 — Triaje (`apb-ops-incident-triage-v1.0`)

**Entrada:** descripción del síntoma, sistema afectado, impacto estimado  
**Salida:** prioridad P1–P4, categoría, componente, SLA, decisión de enrutamiento  
**Duración objetivo:** ≤5 min  
**Gate humano:** NO (el triaje es automático para P2–P4; P1 activa proceso manual de Major Incident)

### Paso 2 — Diagnóstico (`apb-ops-incident-diagnose-v1.0`)

**Entrada:** clasificación del triaje + logs y evidencias  
**Salida:** árbol de causa raíz, runbook, criterios de resolución  
**Duración objetivo:** ≤15 min  
**Delegación:** si el componente es Oracle/IIS/Red/Azure, el agente delega en el subagente especializado  
**Gate humano:** NO (el diagnóstico es propuesta del agente — el técnico decide si ejecutar)

### Paso 3 — Gate de validación humana ⚠️

**Obligatorio antes de ejecutar cualquier paso del runbook.**  
El técnico L1 responsable revisa:
- ¿El diagnóstico es coherente con el síntoma?
- ¿Los pasos de riesgo Medio/Alto han sido evaluados?
- ¿Hay impacto en otros sistemas no detectado?

Si el técnico no está disponible o la incidencia supera su capacidad → ir a Paso 4.

### Paso 4 — Escalado (`apb-ops-incident-escalate-v1.0`)

**Entrada:** diagnóstico completo + razón del escalado  
**Salida:** ticket JSM actualizado, resumen para L2/L3, notificaciones  
**Gate humano:** SÍ — el técnico L1 debe confirmar el escalado antes de ejecutarlo  
**Post-escalado:** el workflow se transfiere al grupo L2/L3 receptor

### Paso 5 — Resolución (ejecución humana)

El técnico L1 aplica el runbook propuesto. El agente no ejecuta acciones sobre sistemas de producción.  
El técnico registra en el ticket JSM cada paso ejecutado y su resultado.

### Paso 6 — Verificación de cierre

El técnico verifica los criterios de resolución definidos en el diagnóstico:
- El servicio responde correctamente
- Los usuarios afectados confirman la normalidad
- Las métricas de monitorización vuelven a niveles normales
- No hay alertas activas relacionadas en Azure Monitor / Zabbix / Grafana

### Paso 7 — Cierre del ticket JSM

- Estado: **Resuelto**
- Causa raíz documentada en el campo "Causa raíz"
- Solución aplicada documentada en "Resolución"
- Si el runbook era nuevo → crear artículo en la base de conocimiento JSM

### Paso 8 — Notificación final (`apb-plat-ms-notify-v1.0`)

- Notificación Teams al solicitante: "La incidencia INC-XXXX ha sido resuelta."
- Si era P1/P2: notificación al responsable del servicio con resumen ejecutivo

---

## 📥 Input del workflow

- Reporte de incidencia (texto libre del solicitante o ticket JSM existente)
- Sistema afectado (si se conoce)
- Impacto estimado
- Logs y evidencias (opcional, mejora la calidad del diagnóstico)

---

## 📤 Output del workflow

- Ticket JSM cerrado con causa raíz, resolución y SLA cumplido/incumplido documentado
- Notificación de resolución al solicitante
- Artículo de base de conocimiento (si el runbook era nuevo)
- Propuesta de ticket de Problema (si la incidencia es recurrente)

---

## 🚫 Límites del workflow

- NO se ejecuta para incidencias de seguridad (ciberincidentes) — derivar al proceso de respuesta a incidentes de seguridad APB
- NO gestiona cambios planificados — usar el proceso de change management APB
- NO puede cerrar incidencias P1 sin validación del Major Incident Manager

---

## 📊 Métricas del workflow

| Métrica | Objetivo APB |
|---------|-------------|
| Tiempo medio de triaje | ≤5 min |
| Tiempo medio de diagnóstico L1 | ≤20 min |
| Tasa de resolución en L1 (sin escalado) | ≥60% |
| Cumplimiento de SLA P1 | 100% |
| Cumplimiento de SLA P2 | ≥95% |
| Artículos de KB generados / incidencias resueltas | ≥30% |

---

## 🔄 Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-26 | Arquitectura APB | Versión inicial — Sesión 21 |

---

*Documento generado por el APB AI Framework. Requiere revisión humana antes de aprobación.*

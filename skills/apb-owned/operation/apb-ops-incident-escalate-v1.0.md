---
id: "apb-ops-incident-escalate-v1.0"
name: "Escalado de Incidencias L2/L3"
description: "Genera el resumen técnico estructurado para el escalado de una incidencia APB de L1 a L2, L3 o Major Incident. Actualiza el ticket JSM con toda la información recopilada, asigna el grupo resolutor correcto y notifica al técnico receptor con el contexto completo."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-26"
review_date: "2026-06-26"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Escalado de Incidencias L2/L3


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Formalizar el escalado de una incidencia cuando L1 no puede resolverla. Genera un resumen técnico completo para el receptor (L2/L3), actualiza el ticket JSM con el histórico de diagnóstico y acciones realizadas, y asigna el ticket al grupo especialista correcto. Minimiza el tiempo perdido por el técnico receptor en recopilar contexto.

---

## ⚡ Trigger

Cuando `apb-ops-incident-diagnose-v1.0` determina que la causa raíz supera la capacidad de L1, o cuando la prioridad es P1 (Major Incident automático).

---

## 📥 Input

- Ticket JSM con triaje y diagnóstico completos
- Razón del escalado (no resoluble en L1 / P1 / tiempo SLA L1 superado)
- Acciones ya realizadas en L1 (si las hay)
- Logs y evidencias recopiladas

---

## 📤 Output

- **Resumen de escalado:** documento técnico estructurado para el técnico receptor
- **Ticket JSM actualizado:** campos de escalado cumplimentados, grupo asignado, SLA reiniciado
- **Notificación al receptor:** Teams + correo con el resumen y enlace al ticket
- **Comunicación al solicitante:** actualización de estado (sin detalles técnicos)
- **Apertura de Major Incident bridge** (solo P1): instrucciones para convocar el puente de crisis

---

## 🔄 Proceso

1. **Validación del escalado:** verificar que se han agotado las opciones L1 antes de escalar
2. **Selección del grupo resolutor:**

| Componente | Grupo L2 | Grupo L3 |
|------------|----------|----------|
| Oracle DB | DBA APB | Soporte Oracle (proveedor) |
| IIS / aplicaciones web | Desarrollo APB | Proveedor de la aplicación |
| Apache / Tomcat | Plataforma APB | Proveedor / comunidad |
| DNS | Infraestructura APB | Operador de red / ISP |
| Firewall | Seguridad APB | Proveedor (Fortinet/Cisco) |
| Azure | Plataforma Cloud APB | Microsoft Support |
| On-Premise Linux/Windows | Sistemas APB | Proveedor hardware |
| Aplicaciones de negocio | Proveedor de la aplicación | — |

3. **Generación del resumen de escalado** con la siguiente estructura:
   - Descripción del síntoma (original)
   - Clasificación: prioridad, categoría, SLA restante
   - Componente afectado y entorno (producción/preproducción)
   - Timeline: hora de inicio, hora de detección, hora de apertura de ticket
   - Diagnóstico L1: causa probable, confianza, árbol de causas descartadas
   - Acciones realizadas en L1 y resultado
   - Logs y evidencias adjuntas
   - Próximos pasos sugeridos
4. **Actualización del ticket JSM:** campo "Escalado a", grupo asignado, nota de escalado
5. **Notificaciones:** Teams al técnico L2/L3 asignado + correo al solicitante

---

## 📋 Reglas y Constraints

- Autonomía nivel 1: el escalado debe ser confirmado por el técnico L1 responsable antes de ejecutarse
- P1 activa el proceso de Major Incident: notificar al Major Incident Manager APB y convocar el puente de crisis
- El ticket JSM no puede cerrarse durante el escalado — solo puede cerrarlo el grupo resolutor
- La comunicación al solicitante nunca incluye detalles técnicos internos (logs, nombres de servidor, IPs internas)
- El SLA del nivel receptor comienza en el momento de la asignación del ticket al nuevo grupo

---

## 🛠 Stack Tecnológico Relevante

- Jira Service Management (JSM) — gestión de tickets ITSM
- Microsoft Teams — notificaciones de escalado
- Outlook / Exchange — correo al solicitante
- Directorio de grupos resolutores APB (referencia interna)

---

## 💡 Ejemplos de Uso

**Ejemplo — Escalado a DBA:**
> Incidencia: Oracle ORA-00060 recurrente, no resuelta con kill session en L1.
> → Escalado a grupo "DBA APB", resumen incluye: sesiones involucradas, transacción bloqueante, queries ejecutadas, historial de los últimos 3 deadlocks en 24h.

**Ejemplo — Major Incident P1:**
> Incidencia: pasarela de pagos caída, 0 transacciones procesándose.
> → P1 automático: notificación al Major Incident Manager, apertura de bridge Teams, ticket asignado a Plataforma APB + Proveedor pasarela, comunicación al solicitante en ≤15 min.

---

## 🔗 Dependencias

- `apb-ops-incident-triage-v1.0` — clasificación previa
- `apb-ops-incident-diagnose-v1.0` — diagnóstico previo
- `apb-plat-ms-notify-v1.0` — notificaciones Teams/correo

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Ticket JSM con triaje y diagnóstico completos` | Pregunta: "¿Puedes proporcionar ticket jsm con triaje y diagnóstico completos?" | Sí |
| `Razón del escalado` | Pregunta: "¿Puedes proporcionar razón del escalado?" | Sí |
| `Acciones ya realizadas en L1` | Pregunta: "¿Puedes proporcionar acciones ya realizadas en l1?" | Sí |
| `Logs y evidencias recopiladas` | Pregunta: "¿Puedes proporcionar logs y evidencias recopiladas?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Footer obligatorio** (última línea del cuerpo del mensaje/correo):
  `⚠️ Generado por IA (APB AI Framework — apb-ops-incident-escalate-v1.0) — revisado y enviado por [nombre].`

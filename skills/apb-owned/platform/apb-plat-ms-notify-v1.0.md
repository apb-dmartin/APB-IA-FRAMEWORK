---
id: "apb-plat-ms-notify-v1.0"
name: "Microsoft 365 Notification Skill"
description: "Skill de plataforma para enviar notificaciones a Microsoft Teams y correo Outlook en los puntos de revisión humana del framework (human_review_points) y cuando un agente genera una entrega. Cubre los dos canales (canal Teams + persona por correo), incluye el contenido del artefacto o un resumen ejecutivo, y puede leer respuestas de aprobación/rechazo para registrarlas."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
inputs:
  - "Tipo de evento: revisión humana pendiente | entrega disponible | aprobación recibida | rechazo recibido"
  - "Identificador del agente/skill que genera el evento"
  - "Artefacto generado o resumen ejecutivo del mismo (Markdown o texto)"
  - "Destinatarios: canal Teams (ID) y/o persona (UPN de correo)"
  - "Prioridad: normal | urgente"
outputs:
  - "Confirmación de envío a cada canal (Teams y/o mail)"
  - "ID de mensaje Teams para seguimiento"
  - "ID de correo enviado para auditoría"
  - "Estado de lectura de respuesta (si se invoca en modo polling)"
depends_on:
  - "prov-ms365-v1.0"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Microsoft 365 Notification Skill

## Propósito

Cubre el canal de comunicación humana del framework: cada vez que un agente alcanza un `human_review_point` o genera una entrega, esta skill garantiza que la persona correcta recibe la notificación en el canal correcto (Teams y/o correo), con el contexto suficiente para tomar una decisión sin tener que buscar el artefacto manualmente.

También escucha respuestas: si el revisor responde al canal Teams o al correo, la skill lee esa respuesta y la registra para que el agente pueda reanudar el flujo (aprobado → siguiente paso; rechazado → motivo y vuelta a corrección).

---

## Tipos de Evento

| Tipo | Cuándo se dispara | Canal por defecto |
|------|-------------------|-------------------|
| `human_review_required` | El agente necesita aprobación humana antes de continuar | Teams (canal del equipo) + mail (responsable) |
| `delivery_available` | El agente ha generado un artefacto listo para usar | Teams (canal del equipo) |
| `approval_received` | El revisor ha aprobado el artefacto | Registro interno (no notifica de nuevo al equipo) |
| `rejection_received` | El revisor ha rechazado con motivo | Teams (canal) + mail (persona que generó el artefacto) |

---

## Prompt de Sistema

```
Eres la skill de notificaciones Microsoft 365 del APB AI Framework.

Tu función es comunicar a las personas correctas que hay algo pendiente de revisión
o que una entrega está disponible, de forma que puedan actuar sin tener que buscar
el artefacto en ningún otro sistema.

### Al enviar una notificación de revisión humana (human_review_required)

1. Identifica quién debe revisar: usa el campo `human_review_points` del agente que
   dispara el evento. Si hay persona asignada, notifica por correo. Siempre notifica
   también al canal Teams del equipo responsable.

2. Construye el mensaje con esta estructura:
   - **Qué necesita revisión**: nombre del agente y tipo de artefacto generado
   - **Contexto mínimo**: propósito del artefacto en 2-3 frases
   - **Resumen del artefacto**: los primeros 300-500 caracteres del output, o la
     tabla de componentes si es un mockup, o los hallazgos principales si es un
     informe de riesgos
   - **Acción requerida**: qué debe hacer el revisor (aprobar / rechazar / comentar)
   - **Aviso corporativo**: "Generado por IA (APB AI Framework) — requiere validación
     humana antes de cualquier uso productivo"

3. En Teams, usa una tarjeta adaptable (Adaptive Card) si el runtime lo permite,
   con botones "✅ Aprobar" y "❌ Rechazar con comentario". Si no es posible,
   usa mensaje de texto con instrucciones claras.

4. En correo, incluye el artefacto completo como adjunto `.md` si su tamaño lo
   permite (< 5 MB), o un enlace a SharePoint si el artefacto ya ha sido subido.

### Al enviar una notificación de entrega (delivery_available)

1. Notifica solo al canal Teams (no mail, salvo que la prioridad sea "urgente").
2. Incluye un enlace directo al artefacto en SharePoint o en el PR de GitHub.
3. Menciona el agente que generó la entrega y el tiempo estimado de revisión.

### Al leer respuestas (polling mode)

1. Usa prov-ms365-v1.0 para leer los últimos mensajes del canal Teams o los correos
   de respuesta en la bandeja del agente/alias de notificaciones.
2. Detecta palabras clave de aprobación ("aprobado", "ok", "adelante", "approved") y
   de rechazo ("rechazado", "no", "cambios", "rejected", "revisar").
3. Si hay ambigüedad, no registres como aprobación — marca como "pendiente de
   clarificación" y notifica de nuevo pidiendo confirmación explícita.
4. Registra la respuesta con: quién respondió, cuándo, y el texto exacto de la respuesta.

### Límites
- No tomes decisiones de negocio basadas en el contenido de la respuesta — solo la
  registras y la pasas al agente que invocó esta skill.
- No reenvíes el mismo evento dos veces al mismo destinatario en menos de 1 hora.
- No incluyas datos clasificados como RESERVADOS en mensajes Teams o correo sin
  confirmación de Ciberseguridad APB.
- Siempre incluye el aviso "Generado por IA" en mensajes sobre artefactos del framework.
```

---

## Plantillas de mensaje

### Teams — Revisión humana pendiente

```
📋 **Revisión requerida — [Nombre del agente]**

**Artefacto:** [tipo] — [nombre/identificador]
**Generado por:** [agent-id] el [fecha]
**Acción requerida:** validar y aprobar o rechazar antes de [fecha límite si aplica]

---
**Resumen:**
[Primeras 300-500 chars del output o tabla de componentes]

---
⚠️ *Generado por IA (APB AI Framework) — requiere validación humana antes de cualquier uso productivo.*

Responde con ✅ para aprobar o ❌ + motivo para rechazar.
```

### Correo — Revisión humana pendiente (asunto)

```
[APB AI Framework] Revisión pendiente: [tipo de artefacto] — [nombre] — [fecha]
```

---

## Configuración de destinatarios por tipo de agente

| Agente origen | Canal Teams | Destinatario correo |
|---------------|-------------|---------------------|
| `apb-agent-ux-mockup-v1.0` | `#arquitectura-frontend` | Perfil funcional asignado (UPN) |
| `apb-agent-risk-exception-v1.0` | `#arquitectura-gobernanza` | Responsable de Arquitectura (UPN) |
| `apb-agent-security-architect-v1.0` | `#ciberseguridad` | CISO APB (UPN) |
| `apb-agent-release-manager-v1.0` | `#releases` | Release Manager (UPN) |
| Resto de agentes | `#arquitectura-general` | Arquitectura APB (alias de equipo) |

Los UPNs y IDs de canal concretos se configuran en `context/apb/config/ms365-routing.yaml` (fichero no incluido en este repo — gestionado en Azure Key Vault / configuración de despliegue APB).

---

## Capacidades

- Notificación a canal Teams con tarjeta adaptable o mensaje de texto
- Notificación por correo con adjunto del artefacto o enlace a SharePoint
- Modo polling: lectura de respuestas y clasificación aprobación/rechazo/pendiente
- Deduplicación: no reenvía el mismo evento al mismo destinatario en < 1 hora
- Trazabilidad: registra todos los envíos con ID de mensaje y timestamp

---

## Dependencias

| Componente | Rol |
|-----------|-----|
| `prov-ms365-v1.0` | Provider que ejecuta las llamadas a Graph API |
| `apb-gov-ai-risk-gate-v1.0` | Verificación de riesgos antes de incluir contenido sensible |

---

## Restricciones

- No contiene lógica de negocio — solo comunica; las decisiones las toma siempre un humano
- No almacena credenciales — las gestiona `prov-ms365-v1.0` vía Azure Key Vault
- El polling de respuestas no se activa automáticamente — debe invocarse explícitamente por el workflow o agente
- No reemplaza el proceso formal de aprobación en Jira (`apb-gov-jira-evidence-v1.0`) — lo complementa

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 15 del plan APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo mensaje generado por esta skill debe incluir marca de origen IA:

- **Footer en cuerpo del mensaje** (ultima linea):
  `Generado por IA (APB AI Framework - apb-plat-ms-notify-v1.0) - revisado y enviado por [nombre].`

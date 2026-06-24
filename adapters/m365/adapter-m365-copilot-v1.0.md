---
id: "adapter-m365-copilot-v1.0"
name: "Microsoft 365 Copilot Adapter"
description: "Adaptador de doble sentido entre el APB AI Framework y Microsoft 365 Copilot: (1) expone skills y agentes del framework como plugins de M365 Copilot para que los usuarios los invoquen desde Teams, Word, Outlook o SharePoint; (2) permite que el framework invoque capacidades de M365 Copilot (resumen de reuniones Teams, borradores de correo, análisis de documentos) como herramientas dentro de un workflow. Compatible con Microsoft 365 Copilot extensibility (API plugins y Copilot connectors)."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "orchestration"
runtime_target: "m365-copilot"
adapted_components:
  - "apb-agent-ux-mockup-v1.0"
  - "apb-agent-spec-engineer-v1.0"
  - "apb-agent-documentation-v1.0"
  - "apb-agent-risk-exception-v1.0"
  - "apb-agent-tech-debt-v1.0"
  - "apb-plat-ms-notify-v1.0"
  - "apb-plat-sharepoint-io-v1.0"
  - "prov-ms365-v1.0"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Microsoft 365 Copilot Adapter

---

## Propósito

M365 Copilot es el asistente de IA integrado en las aplicaciones Microsoft 365 (Teams,
Word, Outlook, SharePoint, Excel). Este adaptador define cómo el APB AI Framework se
relaciona con él en ambas direcciones:

- **Dirección A (framework → M365 Copilot):** el framework invoca capacidades de M365
  Copilot como herramientas dentro de sus workflows (ej. pedir a Copilot que resuma
  una reunión de Teams y usar ese resumen como input para `apb-agent-spec-engineer-v1.0`).

- **Dirección B (M365 Copilot → framework):** los usuarios de APB pueden invocar agentes
  del framework directamente desde la interfaz de M365 Copilot en Teams o SharePoint,
  sin necesidad de abrir Claude ni otra herramienta separada.

---

## Arquitectura de integración

### Dirección A — Framework invoca M365 Copilot

El framework llama a las APIs de Graph que exponen datos ya procesados por M365 Copilot:

| Capacidad M365 Copilot | API Graph | Uso en el framework |
|-----------------------|-----------|---------------------|
| Resumen de reunión Teams | `GET /me/onlineMeetings/{id}/transcripts` + Copilot summary | Input para agentes de spec/discovery |
| Borrador de correo | `POST /me/messages` con `body` generado por Copilot | Notificaciones enriquecidas de `apb-plat-ms-notify-v1.0` |
| Análisis de documento SharePoint | Copilot en SharePoint vía connector | Pre-procesamiento de documentos antes de `apb-plat-sharepoint-io-v1.0` |
| Resumen de hilo de Teams | `GET /teams/{id}/channels/{id}/messages` + Copilot summary | Extracción de decisiones para evidencias Jira |

Todas las llamadas pasan por `prov-ms365-v1.0` con el token Graph de APB.

### Dirección B — M365 Copilot invoca el framework

Los agentes APB se exponen como **API Plugins de M365 Copilot** (especificación OpenAPI 3.0
declarada en `.well-known/ai-plugin.json`). El usuario los invoca desde el chat de
M365 Copilot con lenguaje natural.

```
Arquitectura:
[Usuario en Teams/SharePoint/Word]
    → [M365 Copilot — interpreta la intención]
    → [API Plugin APB — endpoint REST en Azure API Management APB]
    → [Framework skill/agent correspondiente]
    → [Respuesta devuelta a M365 Copilot]
    → [M365 Copilot muestra resultado al usuario]
```

---

## Plugins expuestos en M365 Copilot

### Plugin: APB Mockup

Permite al usuario pedir un mockup de pantalla desde Teams o SharePoint sin salir de M365.

```yaml
plugin_id: "apb-mockup-plugin"
display_name: "APB — Generador de Mockups"
description: "Genera un mockup funcional y prototipo HTML de una pantalla APB a partir de una descripción en lenguaje natural."
agent_mapped: "apb-agent-ux-mockup-v1.0"
trigger_examples:
  - "Genera un mockup de pantalla de gestión de buques con filtros por muelle"
  - "Necesito un prototipo de formulario de alta de expediente"
  - "Diseña la pantalla de dashboard de operaciones portuarias"
output_delivery:
  - "Respuesta en el chat de M365 Copilot (especificación Markdown)"
  - "Fichero HTML subido a SharePoint (Arquitectura/Artefactos-IA/) via apb-plat-sharepoint-io-v1.0"
  - "Notificación al canal Teams del equipo (apb-plat-ms-notify-v1.0)"
```

### Plugin: APB Spec

Genera o enriquece especificaciones funcionales desde documentos SharePoint o historial de Jira.

```yaml
plugin_id: "apb-spec-plugin"
display_name: "APB — Generador de Specs"
description: "Genera especificaciones funcionales desde documentos existentes en SharePoint o exportaciones de Jira."
agent_mapped: "apb-agent-spec-engineer-v1.0"
trigger_examples:
  - "Genera la spec de la pantalla de gestión de atraques a partir del manual de GISPEM en SharePoint"
  - "Extrae los requisitos del histórico de Jira del proyecto Portal Docks"
```

### Plugin: APB Risk Gate

Evalúa el riesgo de IA de un artefacto antes de aprobarlo.

```yaml
plugin_id: "apb-risk-plugin"
display_name: "APB — Evaluación de Riesgos IA"
description: "Evalúa si un artefacto generado por IA cumple las políticas APB antes de aprobarlo."
skill_mapped: "apb-gov-ai-risk-gate-v1.0"
trigger_examples:
  - "Evalúa el riesgo de este mockup antes de enviarlo al equipo de desarrollo"
  - "¿Cumple este código generado con las políticas de seguridad APB?"
```

---

## Configuración del plugin (ai-plugin.json)

```json
{
  "schema_version": "v2.1",
  "name_for_human": "APB AI Framework",
  "name_for_model": "apb_ai_framework",
  "description_for_human": "Accede a los agentes y skills del APB AI Framework desde M365 Copilot.",
  "description_for_model": "Invoca agentes del APB AI Framework para generar mockups, specs, evaluaciones de riesgo y documentación. Siempre incluye aviso de generación por IA en los outputs. Requiere validación humana antes de usar en producción.",
  "auth": {
    "type": "oauth",
    "client_url": "https://apim.portdebarcelona.cat/ai-framework/oauth/authorize",
    "scope": "framework.read framework.execute",
    "authorization_url": "https://apim.portdebarcelona.cat/ai-framework/oauth/token",
    "authorization_content_type": "application/json",
    "verification_tokens": {
      "openai": "AKV://apb-copilot-plugin-token"
    }
  },
  "api": {
    "type": "openapi",
    "url": "https://apim.portdebarcelona.cat/ai-framework/openapi.yaml"
  },
  "logo_url": "https://apim.portdebarcelona.cat/ai-framework/logo.png",
  "contact_email": "arquitectura@portdebarcelona.cat",
  "legal_info_url": "https://intranet.portdebarcelona.cat/politica-ia"
}
```

El endpoint REST del framework se expone via **Azure API Management APB** — el mismo gateway ya usado para otras APIs internas. No se expone directamente el modelo ni las credenciales de Claude.

---

## Limitaciones del runtime M365 Copilot

| Limitación | Implicación para el framework |
|-----------|-------------------------------|
| Ventana de contexto limitada (~32K tokens en M365 Copilot) | Los artefactos grandes se entregan como fichero SharePoint, no como respuesta inline |
| No accede directamente a Claude API | El plugin hace de proxy: M365 Copilot → APIM → Claude → respuesta |
| Los plugins de M365 Copilot requieren aprobación del administrador Microsoft 365 | Arquitectura APB debe publicar y aprobar el plugin en el tenant antes de que los usuarios lo vean |
| No soporta ejecución de código Python/JS directamente | Las skills que requieren ejecución de código usan el runtime de Claude, no el de Copilot |
| Las respuestas de plugin tienen formato limitado (texto, tablas básicas) | El prototipo HTML siempre se entrega como fichero SharePoint, nunca inline en Copilot |

---

## Pasos de activación (pendiente de Arquitectura APB)

1. **Registrar app en Azure AD APB** con los scopes de Graph API requeridos por `prov-ms365-v1.0`
2. **Publicar el endpoint OpenAPI** en Azure API Management APB con autenticación OAuth
3. **Subir el `ai-plugin.json`** al dominio `apim.portdebarcelona.cat/.well-known/`
4. **Aprobar el plugin** en el centro de administración de Microsoft 365 del tenant APB
5. **Publicar para los usuarios** — inicialmente solo equipo de Arquitectura, luego por rol

---

## Restricciones

- El plugin nunca expone credenciales de Azure Key Vault ni tokens de Claude al runtime de M365 Copilot
- Todo artefacto generado via este adaptador lleva el aviso `Generado por IA (APB AI Framework)` visible para el usuario final en M365 Copilot
- El principio de no auto-aprobación del framework (`SYSTEM.md §2.1`) se mantiene íntegro — M365 Copilot no puede aprobar sus propios artefactos generados; la aprobación siempre requiere acción humana explícita
- La compatibilidad de M365 Copilot con API plugins es una feature en evolución (Microsoft la lanza progresivamente en 2025-2026) — verificar disponibilidad en el tenant APB antes de activar

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 15 del plan APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._

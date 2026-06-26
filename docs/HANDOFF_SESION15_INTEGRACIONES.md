# Handoff Sesión 15 — Integraciones Microsoft y plataformas IA

> **Para:** equipo de Plataforma APB, equipo de Desarrollo APB, Administrador Microsoft 365 APB, Administrador Atlassian APB  
> **De:** Arquitectura APB  
> **Fecha:** 2026-06-26  
> **Contexto:** el APB AI Framework tiene los agentes y skills construidos. Esta sesión ha generado
> los artefactos de integración. Este documento describe exactamente qué queda pendiente y quién lo hace.

---

## Lo que ya está hecho (no requiere acción de tu equipo)

| Artefacto | Ubicación en el repo | Estado |
|---|---|---|
| Adapter Rovo completo | `adapters/rovo/adapter-rovo-v1.0.md` | ✅ Listo |
| Adapter M365 Copilot completo | `adapters/m365/adapter-m365-copilot-v1.0.md` | ✅ Listo |
| Provider MS365 (Teams/mail/SharePoint vía Graph API) | `providers/prov-ms365-v1.0.md` | ✅ Listo |
| Skill notificaciones Teams/mail | `skills/apb-owned/platform/apb-plat-ms-notify-v1.0.md` | ✅ Listo |
| Skill lectura/escritura SharePoint | `skills/apb-owned/platform/apb-plat-sharepoint-io-v1.0.md` | ✅ Listo |
| **Spec OpenAPI 3.0 del framework** | `openapi/apb-framework-api.yaml` | ✅ Generado en esta sesión |
| **Manifest plugin M365 Copilot** | `openapi/ai-plugin.json` | ✅ Generado en esta sesión |
| **Forge App skeleton Rovo** | `forge/manifest.yml` + `forge/src/` | ✅ Generado en esta sesión |
| **Guía de activación Rovo** | `docs/rovo-getting-started.md` | ✅ Generado en esta sesión |

---

## Pendiente — por equipo

### PLATAFORMA APB (bloqueante para todo lo demás)

> Sin esto, ninguna integración funciona. Es el mayor esfuerzo y el prerequisito de todos los demás pasos.

**Acción 1 — Desplegar el backend del APB AI Framework**

El framework necesita un endpoint REST real en Azure. La especificación exacta de ese
endpoint está en `openapi/apb-framework-api.yaml`.

Lo que necesita Plataforma:
- Elegir el runtime: **Azure Function** (recomendado para empezar, coste bajo) o Azure Container Apps
- El backend debe recibir las solicitudes REST del `openapi/apb-framework-api.yaml` y llamar internamente
  a la API de Claude (Anthropic) con el agente/skill correspondiente
- Credenciales de Claude API en Azure Key Vault APB (clave `apb-claude-api-key`)
- URL objetivo de producción: `https://apim.portdebarcelona.cat/ai-framework/v1`

**Acción 2 — Publicar en Azure API Management**

- Importar `openapi/apb-framework-api.yaml` en el portal APIM APB
- Configurar autenticación OAuth 2.0 (Client Credentials)
- Verificar que `/health` responde 200 desde fuera de la red APB

**Acción 3 — Registrar dos apps en Azure Active Directory APB**

| App AD | Para qué | Scopes |
|---|---|---|
| `apb-ai-framework-api` | El backend del framework (la API que se llama) | `framework.read`, `framework.execute` |
| `apb-forge-rovo-client` | La Forge App de Rovo (el cliente que llama) | `framework.execute` sobre la app anterior |

**Acción 4 — Registrar app Azure AD para M365 Copilot plugin**

- Nombre: `apb-m365-copilot-plugin`
- Tipo: Authorization Code + Client Credentials
- Scopes: los mismos (`framework.read`, `framework.execute`)
- Anotar `client-id` para el paso de publicación del plugin

**Acción 5 — Publicar el ai-plugin.json**

Una vez el backend esté activo:
- Subir `openapi/ai-plugin.json` a `https://apim.portdebarcelona.cat/.well-known/ai-plugin.json`
- Verificar acceso público (o al menos desde el tenant APB)

---

### DESARROLLO APB

**Acción 1 — Implementar `getFrameworkToken()` en la Forge App**

El fichero `forge/src/functions/invokeFramework.js` tiene la función marcada como pendiente.
El equipo de Desarrollo debe implementar el flujo OAuth 2.0 Client Credentials contra Azure AD.
La implementación de referencia está en `docs/rovo-getting-started.md` §Paso 5.

**Acción 2 — Gestionar el ciclo de vida del token**

La implementación básica obtiene un token por llamada. En producción añadir:
- Caché del token (válido ~1h) para evitar llamadas extra a Azure AD
- Renovación automática cuando faltan <5 min para expirar

**Acción 3 — Implementar polling robusto o webhook**

El polling actual en `invokeFramework.js` bloquea el hilo de la Forge Function (máx 60s).
Para agentes que tardan más (specs largas, análisis complejos), implementar:
- Webhook desde el backend del framework que notifique a la Forge App cuando el job termine, o
- Respuesta inmediata a Rovo con "estoy procesando..." y notificación posterior via Confluence/Teams

**Acción 4 — Desplegar la Forge App** (requiere Acción 1 de Plataforma completada)

```bash
cd forge/
npm install
forge variables set APB_FRAMEWORK_API_URL https://apim.portdebarcelona.cat/ai-framework/v1
forge variables set APB_FRAMEWORK_CLIENT_ID <client-id-apb-forge-rovo-client>
forge variables set --encrypt APB_FRAMEWORK_CLIENT_SECRET <secret>
forge deploy --environment development
forge install --product jira --site <tenant>.atlassian.net
```

---

### ADMINISTRADOR MICROSOFT 365 APB

**Acción 1 — Aprobar el plugin M365 Copilot**

Una vez Plataforma haya publicado el `ai-plugin.json` y el backend esté activo:
- Ir a **Microsoft 365 Admin Center > Integrated Apps > Upload custom app**
- Cargar el manifest o apuntar a `https://apim.portdebarcelona.cat/.well-known/ai-plugin.json`
- Aprobar para el grupo piloto: equipo de Arquitectura APB

**Acción 2 — Verificar que M365 Copilot está licenciado en el tenant APB**

El plugin requiere que los usuarios tengan licencia de **Microsoft 365 Copilot** (no solo M365).
Verificar cuántas licencias hay disponibles antes del roll-out.

---

### ADMINISTRADOR ATLASSIAN APB

**Acción 1 — Confirmar disponibilidad de Rovo** (julio 2026)

- Verificar con Atlassian que el tenant APB tiene Rovo incluido en el plan
- Si no está activo, solicitar activación o upgrade del plan

**Acción 2 — Aprobar la Forge App**

Una vez Desarrollo haya desplegado la Forge App:
- Ir a **Atlassian Admin > Marketplace > Apps privadas**
- Aprobar `APB AI Framework — Rovo Agents`
- Verificar que los permisos coinciden con los de `forge/manifest.yml`
- Activar inicialmente solo para el grupo de Arquitectura APB

---

## Orden de ejecución recomendado

```
Plataforma (backend + APIM + Azure AD)  ← todo lo demás depende de esto
        ↓
Desarrollo (OAuth en Forge App + test)
        ↓
Admin Atlassian (aprobar Forge App en sandbox)
        ↓  en paralelo:
Admin M365 (aprobar plugin M365 Copilot)
        ↓
Piloto con equipo de Arquitectura APB (1-2 semanas)
        ↓
Roll-out a analistas y desarrolladores
```

---

## Qué NO tiene que hacer tu equipo

- **No tocar** los archivos `.md` del framework (agents/, skills/, providers/, adapters/) — son los artefactos del framework, no código desplegable
- **No reescribir** la spec OpenAPI — está generada desde el diseño real del framework
- **No construir un segundo framework** — el objetivo es que el plugin/Forge App llame al endpoint del framework, no que reimplemente la lógica de los agentes

---

## Preguntas frecuentes

**¿Puedo probar algo antes de que Plataforma despliegue el backend?**

Sí. Puedes usar el framework hoy adjuntando el `.md` del agente directamente en el chat de Claude
(web o Claude Code). Eso no requiere ninguna infraestructura. La integración con M365 Copilot y
Rovo es la que necesita el backend.

**¿Qué pasa si el tenant no tiene Rovo en julio?**

La integración con M365 Copilot (plugin) no depende de Rovo — puede activarse independientemente.
Atlassian Rovo puede postponerse si el plan no lo incluye.

**¿El framework llama a Claude directamente o pasa por APIM?**

La arquitectura objetivo es: M365 Copilot / Rovo → APIM APB → backend framework → Claude API.
El backend es el único componente que tiene la clave de Claude API — nunca se expone al plugin ni a la Forge App.

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 15 del plan APB-IA-FRAMEWORK.  
> **Validado por humano:** _pendiente — Debora Martín, Arquitectura APB._

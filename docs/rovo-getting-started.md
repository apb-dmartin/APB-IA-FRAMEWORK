# Guía de activación — APB AI Framework en Rovo

> **Audiencia:** equipo de Arquitectura APB + administrador Atlassian APB  
> **Prerequisito:** tenant Atlassian con Rovo activado (previsto julio 2026)  
> **Tiempo estimado de activación:** 2–4 horas (primera vez), 30 min (actualizaciones)

---

## Qué consigue esta integración

Una vez activada, los usuarios del tenant Atlassian APB pueden invocar los agentes
del APB AI Framework directamente desde el **chat de Rovo** en Jira o Confluence,
sin abrir Claude ni ninguna otra herramienta:

| Agente Rovo | Qué hace |
|---|---|
| **APB — Spec desde historial Jira** | Analiza tickets de un proyecto y genera la spec funcional en Confluence |
| **APB — Discovery Técnico** | Informe de deuda técnica, arquitectura y vulnerabilidades de un proyecto |
| **APB — Generador de Documentación** | Manuales, ADRs, documentación de arquitectura publicados en Confluence |
| **APB — Evaluación de Riesgos IA** | Semáforo de cumplimiento de la política de IA APB para cualquier artefacto |

---

## Arquitectura de la integración

```
[Usuario en Jira / Confluence]
       ↓  chat natural ("Genera la spec de...")
[Rovo — interpreta intención]
       ↓  invoca Rovo Agent personalizado APB
[Forge App "apb-rovo-agents" — forge/]
       ↓  POST /agents/{agentId}/invoke  (OAuth 2.0)
[Azure API Management APB]
       ↓
[APB AI Framework API — backend]
       ↓  resultado
[Forge App — devuelve a Rovo]
       ↓
[Rovo muestra resultado al usuario en Jira/Confluence]
```

---

## Pasos de activación

### Paso 1 — Verificar prerequisites (Plataforma APB)

- [ ] Confirmar que el tenant Atlassian APB tiene **Rovo activado y licenciado**
- [ ] Confirmar que el equipo de Arquitectura tiene rol de **administrador Forge** en el tenant
- [ ] Instalar Forge CLI: `npm install -g @forge/cli` (Node.js ≥ 18 requerido)
- [ ] Autenticarse en Forge: `forge login` con las credenciales de administrador Atlassian APB

### Paso 2 — Desplegar el backend del framework (Plataforma APB)

> Este paso es el más costoso y es **requisito bloqueante** para todo lo demás.
> El APB AI Framework necesita un endpoint REST real que la Forge App pueda llamar.

- [ ] **Registrar una Azure AD App** en el tenant Azure APB:
  - Nombre: `apb-ai-framework-api`
  - Tipo: aplicación web / API
  - Scopes a exponer: `framework.read`, `framework.execute`
  - Anotar: `tenant-id`, `client-id`
- [ ] **Desplegar el backend del framework** en Azure (Azure Function o Azure Container Apps):
  - El backend debe implementar los endpoints de `openapi/apb-framework-api.yaml`
  - Debe llamar internamente a la API de Claude (Anthropic) o al runtime configurado
  - URL de producción objetivo: `https://apim.portdebarcelona.cat/ai-framework/v1`
- [ ] **Publicar la OpenAPI spec** en Azure APIM:
  - Importar `openapi/apb-framework-api.yaml` en el portal de Azure APIM APB
  - Configurar la política de autenticación OAuth 2.0 (Client Credentials)
  - Verificar que `https://apim.portdebarcelona.cat/ai-framework/v1/health` devuelve 200
- [ ] **Subir el `ai-plugin.json`** al dominio:
  - Ubicación: `https://apim.portdebarcelona.cat/.well-known/ai-plugin.json`
  - Contenido: `openapi/ai-plugin.json` de este repo
- [ ] Guardar credenciales en **Azure Key Vault APB**:
  - `apb-m365-tenant-id`
  - `apb-m365-client-id`
  - `apb-m365-client-secret` (para Graph API si se integra Teams/mail/SharePoint)

### Paso 3 — Registrar la app Azure AD para la Forge App (Plataforma APB)

La Forge App necesita su propia app Azure AD para obtener tokens y llamar al framework:

- [ ] Crear una segunda Azure AD App: `apb-forge-rovo-client`
- [ ] Configurar Client Credentials grant (sin usuario)
- [ ] Asignar permiso sobre `apb-ai-framework-api` con scope `framework.execute`
- [ ] Anotar `client-id` y generar `client-secret`

### Paso 4 — Configurar y desplegar la Forge App (Arquitectura APB)

```bash
# Desde la carpeta forge/ de este repo
cd forge/
npm install

# Configurar las variables de entorno de Forge (una sola vez por entorno)
forge variables set APB_FRAMEWORK_API_URL https://apim.portdebarcelona.cat/ai-framework/v1
forge variables set APB_FRAMEWORK_CLIENT_ID <client-id-del-paso-3>
forge variables set --encrypt APB_FRAMEWORK_CLIENT_SECRET <client-secret-del-paso-3>

# Desplegar en entorno de desarrollo primero
forge deploy --environment development

# Verificar que la app aparece en el panel Atlassian Developer
forge open

# Instalar en el tenant APB (sandbox primero)
forge install --product jira --site <your-tenant>.atlassian.net
```

### Paso 5 — Implementar la autenticación OAuth en el código (Desarrollo APB)

El fichero `forge/src/functions/invokeFramework.js` tiene la función `getFrameworkToken()`
marcada como **PENDIENTE**. El equipo de desarrollo debe implementarla:

```javascript
// Implementación de referencia (Client Credentials flow)
async function getFrameworkToken() {
  const tokenEndpoint = `https://login.microsoftonline.com/${TENANT_ID}/oauth2/v2.0/token`;
  const response = await fetch(tokenEndpoint, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "client_credentials",
      client_id: process.env.APB_FRAMEWORK_CLIENT_ID,
      client_secret: process.env.APB_FRAMEWORK_CLIENT_SECRET,
      scope: "https://apim.portdebarcelona.cat/ai-framework/.default",
    }),
  });
  const data = await response.json();
  return data.access_token;
}
```

### Paso 6 — Aprobar la Forge App como administrador Atlassian (Administrador APB)

- [ ] Ir a **Atlassian Admin > Marketplace > Apps privadas**
- [ ] Localizar `APB AI Framework — Rovo Agents`
- [ ] Aprobar los permisos solicitados (lista en `forge/manifest.yml > permissions`)
- [ ] Activar para el grupo piloto: equipo de Arquitectura APB

### Paso 7 — Piloto y roll-out

- [ ] Prueba con el equipo de Arquitectura APB (1–2 semanas)
- [ ] Validar que los 4 agentes Rovo responden correctamente
- [ ] Verificar que `human_review_required` se comunica al usuario en todos los casos
- [ ] Roll-out a analistas y desarrolladores APB

---

## Verificación rápida post-activación

Desde Jira o Confluence, abrir el chat de Rovo y escribir:

```
¿Qué agentes APB tengo disponibles?
```

Debería responder listando los 4 agentes. Si no aparecen, verificar:
1. Que la Forge App está instalada y aprobada
2. Que el endpoint `https://apim.portdebarcelona.cat/ai-framework/v1/health` responde 200
3. Los logs de la Forge App: `forge logs --environment production`

---

## Permisos Atlassian requeridos por la Forge App

| Permiso | Para qué |
|---|---|
| `read:jira-work` | Leer tickets de proyectos Jira como input de agentes |
| `write:jira-work` | Crear tickets de revisión humana tras generación |
| `read:confluence-content.all` | Leer documentación existente como contexto |
| `write:confluence-content` | Publicar specs y documentación generadas |
| `read:confluence-space.summary` | Ver el estado de un espacio para detectar gaps |
| `read:rovo:user` | Obtener identidad del usuario para auditoría |
| `fetch: apim.portdebarcelona.cat` | Llamar al APB AI Framework API |

---

## Restricciones y política de uso

- Los Rovo Agents APB **no pueden aprobar sus propios artefactos** — toda validación requiere acción humana explícita (coherente con `SYSTEM.md §2.1`)
- Todo artefacto generado incluye el aviso `Generado por APB AI Framework` visible en Confluence/Jira
- Los datos personales procesados se rigen por la política RGPD APB (`context/apb/policies/compliance/`)
- En caso de duda sobre si un artefacto puede usarse en producción, consultar con Arquitectura APB antes de distribuirlo

---

## Contacto y soporte

- **Propietario:** Arquitectura APB — `arquitectura@portdebarcelona.cat`
- **Incidencias técnicas de la Forge App:** crear ticket en Jira proyecto `ARQAPB` con etiqueta `rovo-agents`
- **Incidencias del backend del framework:** crear ticket con etiqueta `ai-framework-api`

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 15 del plan APB-IA-FRAMEWORK.  
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de distribuir._

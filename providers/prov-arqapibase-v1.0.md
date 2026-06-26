---
id: "prov-arqapibase-v1.0"
name: "Provider: APB.ARQ.APIBASE"
description: "Proveedor de acceso al repositorio GitHub portdebarcelona/ArqApiBase — paquete base de arquitectura .NET para APIs REST APB. Fuente de verdad para el estándar ApbControllerBase, autenticación JWT, ApbDbContext (auditoría), Swagger, versionado y Application Insights. Los agentes deben leer este repo antes de generar código .NET de tipo API REST."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
provider_type: "knowledge"
access_mode: "read"
source_repo: "https://github.com/portdebarcelona/ArqApiBase"
source_branch: "master"
access: "privado — organización portdebarcelona, acceso configurado en APB AI Framework"
current_package_version: "1.0.21"
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Provider: APB.ARQ.APIBASE

---

## Descripción

Proveedor de acceso al repositorio GitHub privado `portdebarcelona/ArqApiBase`. Contiene el paquete NuGet `APB.ARQ.APIBASE` que Arquitectura APB distribuye a todos los equipos de desarrollo como base obligatoria para APIs REST .NET en el Port de Barcelona.

**Este provider es la fuente de verdad.** Los agentes no deben usar conocimiento estático del paquete — deben leer el estado actual del repo al generar código .NET de tipo API.

---

## Acceso

- **Repositorio:** `https://github.com/portdebarcelona/ArqApiBase`
- **Visibilidad:** Privado — organización `portdebarcelona`
- **Rama principal:** `master`
- **Acceso desde el framework:** Configurado en la organización GitHub APB

---

## Ficheros clave a leer

| Fichero | Qué contiene |
|---------|-------------|
| `src/APB.ARQ.APIBASE/ApbControllerBase.cs` | Clase base para controladores API: APP, USUARI, ACTOR, LANG, ACTUACIO, IDENTITAT, Load/LoadAsync |
| `src/APB.ARQ.APIBASE/ApbStartup.cs` | JWT Bearer, API versioning, Swagger, Application Insights, CORS, localización |
| `src/APB.ARQ.APIBASE/ApbDbContext.cs` | DbContext con auditoría automática en SaveChanges: APB_CREADOR, APB_MODIFICADOR, AUDIT_* |
| `src/APB.ARQ.APIBASE/ApbHealthCheck.cs` | Health check estándar APB (`/ping`, `/health`) |
| `src/APB.ARQ.APIBASE/ApbExceptionHandlingMiddleware.cs` | Middleware de gestión centralizada de excepciones |
| `src/APB.ARQ.APIBASE/APB.ARQ.APIBASE.csproj` | Versión del paquete y dependencias (DevExtreme, JWT, Swagger, Application Insights) |
| `src/PublishPackage.txt` | Versión actual del paquete NuGet publicado |

---

## Cuándo invocar este provider

Un agente debe leer este provider antes de:
- Generar un nuevo controlador para una API REST APB
- Revisar código .NET de tipo API (verificar herencia, claims, auditoría)
- Generar un `DbContext` en un proyecto APB
- Configurar autenticación JWT en un proyecto .NET APB
- Responder preguntas sobre entornos (des/pre/pro), URLs de issuer/audience

---

## Proceso de actualización del skill asociado

Cuando se publique una nueva versión de `APB.ARQ.APIBASE`:

1. Arquitectura APB actualiza `current_package_version` en este provider
2. Arquitectura APB revisa cambios de contrato en `ApbControllerBase`, `ApbDbContext` o `ApbStartup`
3. Si hay cambios de contrato → actualizar `apb-arch-dotnet-base-v1.0` con las nuevas reglas
4. Si solo hay cambios internos → actualizar `current_package_version` es suficiente
5. Commit y push al APB-IA-FRAMEWORK: `chore: actualizar prov-arqapibase a vX.Y.Z`

**Responsable:** Arquitectura APB — acción manual al recibir notificación de nueva release de ArqApiBase.

---

*Provider generado por el APB AI Framework — Sesión 13. Requiere revisión humana antes de aprobación.*

---
id: "prov-arqbase-v1.0"
name: "Provider: APB.ARQ.BASE"
description: "Proveedor de acceso al repositorio GitHub portdebarcelona/ArqBase — paquete base de arquitectura .NET para aplicaciones web MVC APB. Fuente de verdad para el estándar ApbController, autenticación TGT, gestión de usuario y localización. Los agentes deben leer este repo antes de generar código .NET de tipo MVC."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
provider_type: "knowledge"
access_mode: "read"
source_repo: "https://github.com/portdebarcelona/ArqBase"
source_branch: "master"
access: "privado — organización portdebarcelona, acceso configurado en APB AI Framework"
current_package_version: "ver PublishPackage.txt en el repo"
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Provider: APB.ARQ.BASE

---

## Descripción

Proveedor de acceso al repositorio GitHub privado `portdebarcelona/ArqBase`. Contiene el paquete NuGet `APB.ARQ.BASE` que Arquitectura APB distribuye a todos los equipos de desarrollo como base obligatoria para aplicaciones web MVC .NET en el Port de Barcelona.

**Este provider es la fuente de verdad.** Los agentes no deben usar conocimiento estático del paquete — deben leer el estado actual del repo al generar código .NET de tipo aplicación web.

---

## Acceso

- **Repositorio:** `https://github.com/portdebarcelona/ArqBase`
- **Visibilidad:** Privado — organización `portdebarcelona`
- **Rama principal:** `master`
- **Acceso desde el framework:** Configurado en la organización GitHub APB

---

## Ficheros clave a leer

| Fichero | Qué contiene |
|---------|-------------|
| `src/APB.ARQ.BASE/ApbStartup.cs` | Configuración automática: localización, DataProtection Redis, HttpClient, gestión de errores |
| `src/APB.ARQ.BASE/ApbController.cs` | Clase base para controladores MVC: USUARI, LANG, APP, TePermis, SetCulture, SetUser |
| `src/APB.ARQ.BASE/ApbCookieAuthenticationEvents.cs` | Gestión de eventos de autenticación por cookie |
| `src/APB.ARQ.BASE/ApbCrypto.cs` | Utilidades de cifrado APB (RSA con certificado) |
| `src/PublishPackage.txt` | Versión actual del paquete NuGet publicado |

---

## Cuándo invocar este provider

Un agente debe leer este provider antes de:
- Generar un nuevo controlador para una aplicación web MVC APB
- Revisar código .NET de tipo web app (verificar herencia correcta)
- Responder preguntas sobre el modelo de usuario, permisos o localización APB
- Documentar integraciones con el sistema TGT de autenticación

---

## Proceso de actualización del skill asociado

Cuando se publique una nueva versión de `APB.ARQ.BASE`:

1. Arquitectura APB actualiza `current_package_version` en este provider
2. Arquitectura APB revisa si hay cambios de contrato en `ApbController` o `ApbStartup`
3. Si hay cambios de contrato → actualizar `apb-arch-dotnet-base-v1.0` con las nuevas reglas
4. Si solo hay cambios internos → actualizar `current_package_version` es suficiente
5. Commit y push al APB-IA-FRAMEWORK con el mensaje: `chore: actualizar prov-arqbase a vX.Y.Z`

**Responsable:** Arquitectura APB — acción manual al recibir notificación de nueva release de ArqBase.

---

*Provider generado por el APB AI Framework — Sesión 13. Requiere revisión humana antes de aprobación.*

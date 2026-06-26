---
id: "apb-arch-dotnet-base-v1.0"
name: "Estándares de Arquitectura Base .NET APB"
description: "Define las reglas obligatorias para proyectos .NET APB: cuándo usar APB.ARQ.BASE vs APB.ARQ.APIBASE, anti-patrones prohibidos y checklist de cumplimiento. El contenido técnico detallado (clases, métodos, configuración) se obtiene siempre en tiempo de invocación desde los providers prov-arqbase-v1.0 y prov-arqapibase-v1.0 — no de este skill."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
providers:
  - "prov-arqbase-v1.0"
  - "prov-arqapibase-v1.0"
consumed_by:
  - "apb-agent-implementer-v1.0"
  - "apb-agent-code-reviewer-v1.0"
  - "apb-agent-technical-architect-v1.0"
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Estándares de Arquitectura Base .NET APB

---

## ⚠️ Importante — Fuente de verdad dinámica

Este skill define las **reglas de uso**. El contenido técnico actual (clases, métodos, propiedades, configuración, dependencias) debe obtenerse **siempre** leyendo los repos en el momento de la invocación:

- **Apps MVC:** leer `prov-arqbase-v1.0` → `https://github.com/portdebarcelona/ArqBase`
- **APIs REST:** leer `prov-arqapibase-v1.0` → `https://github.com/portdebarcelona/ArqApiBase`

**Nunca usar conocimiento estático sobre estos paquetes.** Las versiones evolucionan y el skill refleja la política, no la implementación.

---

## 🎯 Propósito

Todo proyecto .NET desarrollado en APB debe usar los paquetes base de Arquitectura como punto de partida obligatorio. Estos paquetes encapsulan los estándares transversales APB que no deben reimplementarse en cada proyecto.

---

## 📦 Cuándo usar cada paquete

| Tipo de proyecto | Paquete base | Clase a heredar |
|-----------------|-------------|----------------|
| Aplicación web MVC con sesión de usuario, vistas Razor, autenticación TGT | `APB.ARQ.BASE` | `ApbController` |
| API REST consumida por otras apps o por el frontend, autenticada con JWT | `APB.ARQ.APIBASE` | `ApbControllerBase` |

**Si hay duda:** las APIs no tienen vistas — usan `ControllerBase`. Las apps web tienen vistas — usan `Controller`. En APB, siempre con el prefijo `Apb`.

---

## 📋 Acción del agente al generar código .NET

```
1. Determinar el tipo de proyecto (MVC / API REST)
2. Leer el repo correspondiente via el provider
3. Identificar la versión actual del paquete (PublishPackage.txt)
4. Generar código heredando de la clase base correcta
5. Verificar checklist de cumplimiento antes de entregar
```

---

## ✅ Checklist de cumplimiento (aplicar siempre en revisión de código)

### APIs REST (APB.ARQ.APIBASE)
- [ ] Controladores heredan de `ApbControllerBase`, no de `ControllerBase`
- [ ] DbContext hereda de `ApbDbContext`, no de `DbContext`
- [ ] Claims leídos desde propiedades del controller base (`APP`, `USUARI`, `ACTOR`, `LANG`), no con `User.FindFirst` manual
- [ ] Health checks registrados (`/ping` y `/health`)
- [ ] `UseApbSwaggerUI` para Swagger multi-versión
- [ ] `UseApbHealthChecks` en el pipeline
- [ ] `UseApbExceptionHandling` para gestión centralizada de errores
- [ ] `APPINSIGHTS_CONNECTIONSTRING` configurado en todos los entornos
- [ ] JWT Bearer no configurado manualmente — lo gestiona `ApbStartup`
- [ ] Endpoints con DevExtreme DataGrid usan `Load<T>` / `LoadAsync<T>`

### Apps web MVC (APB.ARQ.BASE)
- [ ] Controladores heredan de `ApbController`, no de `Controller`
- [ ] Control de acceso usa `USUARI.TePermis("PERMISO")`, no roles/claims directos
- [ ] `error.html` en `wwwroot/` para la gestión de errores corporativa
- [ ] `PathBase` configurado si la app no está en la raíz del dominio
- [ ] No hay implementación propia de gestión de sesión ni autenticación

---

## 🚫 Anti-patrones prohibidos

| Anti-patrón | Motivo |
|-------------|--------|
| Heredar de `Controller` o `ControllerBase` directamente | Omite autenticación, auditoría y estándares APB |
| Leer claims JWT con `User.FindFirst(...)` | El base controller ya los expone tipados |
| Implementar auditoría de BD propia | Duplica lógica, queda inconsistente con Application Insights |
| Hardcodear URLs de servicios APB (`tgtdes.portdebarcelona.cat`, etc.) | Rompe al cambiar entorno — usar `Arq:Services:*` en config |
| Omitir health checks | Sin observabilidad de salud del servicio |
| Configurar JWT Bearer manualmente | Parámetros de issuer/audience pueden desincronizarse del estándar APB |
| Usar versión desactualizada del paquete base | Puede omitir fixes de seguridad o cambios de estándar |

---

## 🔄 Política de actualización

Cuando Arquitectura APB publique una nueva versión de `APB.ARQ.BASE` o `APB.ARQ.APIBASE`:

1. Actualizar `current_package_version` en el provider correspondiente
2. Si hay cambios de contrato en las clases base → actualizar este skill
3. Commit al APB-IA-FRAMEWORK: `chore: actualizar prov-arq{base|apibase} a vX.Y.Z`

**Referencia:** `context/apb/policies/POLICY_ARCHITECTURE_BASE.md`

---

## 🔄 Historial de cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-26 | Arquitectura APB | Versión inicial — Sesión 13 (#48). Modelo de provider dinámico. |

---

*Skill generada por el APB AI Framework. Requiere revisión humana antes de aprobación.*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-dotnet-base-v1.0) - pendiente validacion humana. No distribuir sin revision.

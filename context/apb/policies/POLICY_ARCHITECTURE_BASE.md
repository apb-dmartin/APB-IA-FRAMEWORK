---
id: "policy-architecture-base-v1.0"
name: "Política de Paquetes Base de Arquitectura .NET APB"
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
scope: "Todos los proyectos .NET desarrollados en o para el Port de Barcelona"
created_date: "2026-06-26"
review_date: "2027-06-26"
---

# Política de Paquetes Base de Arquitectura .NET APB

---

## 1. Propósito

Establecer el uso obligatorio de los paquetes base de arquitectura APB en todos los proyectos .NET, definir el mecanismo de actualización y garantizar que los agentes de IA del APB AI Framework siempre trabajan con la versión vigente de los estándares.

---

## 2. Alcance

Esta política aplica a:
- Todos los equipos internos APB que desarrollen aplicaciones .NET
- Equipos externos (proveedores) que desarrollen software para APB bajo contrato
- Agentes de IA del APB AI Framework cuando generen o revisen código .NET

---

## 3. Paquetes base obligatorios

| Paquete | Repo fuente | Para |
|---------|------------|------|
| `APB.ARQ.BASE` | `https://github.com/portdebarcelona/ArqBase` (privado) | Aplicaciones web MVC con sesión |
| `APB.ARQ.APIBASE` | `https://github.com/portdebarcelona/ArqApiBase` (privado) | APIs REST autenticadas con JWT |

**Regla:** Todo proyecto .NET nuevo en APB debe usar uno de estos paquetes como base. No se admite reimplementación de los estándares que estos paquetes ya cubren (autenticación, auditoría, localización, health checks, Swagger).

---

## 4. Fuente de verdad

Los repos GitHub `portdebarcelona/ArqBase` y `portdebarcelona/ArqApiBase` son la **única fuente de verdad** sobre el estándar técnico vigente.

**Implicación para agentes de IA:** Los agentes del APB AI Framework deben leer el estado actual del repo en el momento de la invocación (via `prov-arqbase-v1.0` o `prov-arqapibase-v1.0`), no usar conocimiento estático cacheado en el skill. El skill `apb-arch-dotnet-base-v1.0` define las reglas de uso — el repo define la implementación.

---

## 5. Proceso de actualización del framework cuando cambia un paquete base

### Trigger
Nueva release publicada en `portdebarcelona/ArqBase` o `portdebarcelona/ArqApiBase`.

### Responsable
Arquitectura APB — la misma persona/equipo que publica la release.

### Pasos (mecanismo manual — fase actual)

| Paso | Acción | Responsable |
|------|--------|------------|
| 1 | Revisar el CHANGELOG de la nueva versión — identificar cambios de contrato | Arquitectura APB |
| 2 | Actualizar `current_package_version` en `prov-arqbase-v1.0` o `prov-arqapibase-v1.0` | Arquitectura APB |
| 3 | Si hay cambios de contrato en clases base → actualizar checklist y anti-patrones en `apb-arch-dotnet-base-v1.0` | Arquitectura APB |
| 4 | Commit al APB-IA-FRAMEWORK: `chore: actualizar prov-arq{base\|apibase} a vX.Y.Z` | Arquitectura APB |
| 5 | Si el cambio es breaking → notificar a equipos de desarrollo APB | Arquitectura APB |

### Criterio de cambio de contrato (paso 3)
Se considera cambio de contrato cuando:
- Se añade, renombra o elimina una propiedad pública en `ApbController`, `ApbControllerBase` o `ApbDbContext`
- Cambia el comportamiento de `ApbStartup` (nuevos servicios, nuevas configuraciones obligatorias)
- Se añade o elimina un método de extensión de middleware

### Futura automatización (fase posterior — tras integraciones P1-P7)
Cuando las integraciones del framework estén desplegadas, migrar a CI automático:
- GitHub Action en `ArqBase`/`ArqApiBase` que abre PR en `APB-IA-FRAMEWORK` actualizando el provider
- El PR incluye diff del contrato para revisión de Arquitectura APB antes de merge

---

## 6. Acceso a los repos para agentes de IA

- Los repos `portdebarcelona/ArqBase` y `portdebarcelona/ArqApiBase` son **privados**
- El APB AI Framework tiene acceso configurado en la organización GitHub `portdebarcelona`
- Los agentes leen via el provider `prov-github-v1.0` con las credenciales configuradas
- **Nunca** almacenar tokens de GitHub en el código o en ficheros del framework

---

## 7. Excepciones

Un proyecto .NET puede no usar los paquetes base únicamente si:
- Es un proyecto de prueba de concepto (PoC) temporal, no destinado a producción
- Hay una incompatibilidad técnica documentada y aprobada por Arquitectura APB
- El proyecto usa una tecnología .NET no soportada por los paquetes base (p.ej., Blazor WASM puro)

Toda excepción debe documentarse en el ADR del proyecto y aprobarse por Arquitectura APB.

---

## 8. Incumplimiento

El agente `apb-agent-code-reviewer-v1.0` marcará como defecto **Crítico** cualquier controlador que no herede de `ApbController` o `ApbControllerBase`. El PR no podrá mergearse sin corrección.

---

*Política generada por el APB AI Framework — Sesión 13. Requiere aprobación formal de Arquitectura APB antes de publicación.*

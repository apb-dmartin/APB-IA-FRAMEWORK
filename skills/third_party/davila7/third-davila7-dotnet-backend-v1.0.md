---
id: "third-davila7-dotnet-backend-v1.0"
name: "Skill: .NET Backend Patterns (davila7/claude-code-templates)"
description: "Patrones de referencia para construir y optimizar servicios backend ASP.NET Core 8+ (Minimal APIs, EF Core, autenticación, background workers), adaptados del repositorio público davila7/claude-code-templates al stack .NET 8/C# de APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
source_repo: "https://github.com/davila7/claude-code-templates"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: .NET Backend Patterns (davila7/claude-code-templates)

---

## Descripción
Adaptación de la skill `dotnet-backend` del repositorio público
`davila7/claude-code-templates` (MIT). El contenido original es una guía de
referencia para construir APIs ASP.NET Core 8+ (controller-based o Minimal
APIs) con EF Core, autenticación, background workers y patrones de
rendimiento. Se incorpora como complemento técnico de implementación a
`apb-dev-code-base-v1.0` y `apb-dev-implement-v1.0`, que cubren el flujo de
generación de código pero no el catálogo detallado de patrones .NET 8
específicos (Minimal API vs controladores, EF Core, background services).

> **Nota de gobernanza:** identificada en la Sesión 9 (revisión de terceros,
> `proyecto.md` §8) dentro de un mega-repositorio agregador de cientos de
> skills (`davila7/claude-code-templates`, antes registrado en §8 solo como
> "plantillas"). Este descriptor cubre únicamente la skill puntual
> `dotnet-backend`; el resto del agregador no se incorpora.

## Capacidades
- Diseño de APIs ASP.NET Core 8+ (Minimal APIs y controladores)
- Configuración de EF Core: migraciones code-first, `Include`/`ThenInclude`,
  `AsNoTracking` para consultas de solo lectura
- Patrones de autenticación/autorización: JWT, ASP.NET Core Identity,
  autorización basada en políticas y claims
- Background workers (`IHostedService`, `BackgroundService`) para tareas de
  larga duración o programadas
- Patrones de rendimiento: async/await consistente, output caching (.NET 8+)

## Inputs
- `tipo_servicio`: API REST, servicio en background, o ambos
- `modelo_datos`: entidades y relaciones a mapear con EF Core
- `requisitos_auth`: estrategia de autenticación/autorización requerida

## Outputs
- `codigo_api`: endpoints o controladores ASP.NET Core generados
- `configuracion_efcore`: `DbContext` y migraciones
- `patron_auth`: implementación de autenticación/autorización aplicada

## Restricciones
- El contenido original usa PostgreSQL como ejemplo de almacén relacional;
  en APB el almacén por defecto es **Azure SQL** (Oracle solo on-premise,
  Cosmos DB solo con justificación arquitectónica) — los ejemplos deben
  adaptarse al proveedor real antes de su uso
- El original sugiere Hangfire/Quartz.NET para jobs programados; en APB la
  mensajería/orquestación corporativa estándar es **Azure Service Bus** —
  evaluar caso por caso si Hangfire/Quartz.NET es necesario además, o si
  Azure Service Bus/Azure Functions con triggers de tiempo cubre el caso
- No sustituye `apb-dev-code-base-v1.0` (generación de código base APB) ni
  `apb-arch-api-contract-v1.0` (diseño de contratos API): esta skill aporta
  el catálogo de patrones de implementación .NET, no la decisión
  arquitectónica previa

## Adaptaciones APB
- Sustituir ejemplos de PostgreSQL por Azure SQL (`UseSqlServer` en lugar de
  `UseNpgsql`) en cualquier código generado a partir de esta skill
- Sustituir Hangfire/Quartz.NET por Azure Service Bus + Azure Functions con
  trigger de tiempo cuando el caso de uso sea programación de tareas
  corporativas, salvo justificación explícita en contrario
- Conectar con `apb-sub-dev-net-v1.0` (subagente .NET) como consumidor
  natural de esta skill

## Ejemplo de Uso
```
Invocar: third-davila7-dotnet-backend-v1.0
Input: { tipo_servicio: "API REST", modelo_datos: "Escala portuaria, Buque",
         requisitos_auth: "JWT + autorización por política (rol operador)" }
Output: Estructura de Minimal API con EF Core sobre Azure SQL, autenticación
        JWT y autorización por política, lista para revisión técnica
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

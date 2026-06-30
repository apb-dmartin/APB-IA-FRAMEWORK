---
id: "apb-dev-micro-base-v1.0"
name: "Microservice Base Scaffold"
description: "Diseña arquitecturas de microservicios (DDD estratégico, patrones de comunicación e integración) y genera el scaffold base de un microservicio .NET/C# siguiendo los estándares corporativos APB: arquitectura limpia/hexagonal, DDD, logging, health checks y Dockerfile."
version: "1.1.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "apb-arch-ddd-v1.0"
  - "apb-dev-api-standard-v1.0"
  - "apb-plat-docker-v1.0"
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB
---

# Microservice Base Scaffold

> Las secciones 1–6 (diseño estratégico de microservicios) incorporan,
> fusionados y adaptados, contenidos de la skill de terceros
> `NeoLabHQ/context-engineering-kit` (plugins `ddd` y `sdd`) bajo licencia
> MIT. Ver sección 12, Procedencia. Las secciones 7+ (scaffold .NET) son
> contenido propio de APB.

## 1. Propósito y Alcance

Esta skill cubre dos fases relacionadas: el **diseño estratégico** de una
arquitectura de microservicios (bounded contexts, patrones de comunicación e
integración, estrategia de datos) y la **generación del scaffold base** de un
microservicio .NET/C# concreto siguiendo los estándares APB.

## 2. Diseño Estratégico: DDD para Microservicios

### 2.1 Bounded Contexts como Líneas de Corte

Cada bounded context es candidato a microservicio (regla guía, no rígida).
Criterios de descomposición: cohesión funcional (un subdomain completo por
servicio), autonomía de datos (database per service), independencia de
despliegue, y equipo independiente (1–3 servicios por equipo).

**Anti-patrón:** microservicio por entidad — demasiado granular, overhead de
comunicación excesivo.

### 2.2 Patrones de Relación entre Contexts (Context Mapping)

`Partnership` (colaboración mutua) · `Shared Kernel` (modelo mínimo
compartido) · `Customer-Supplier` (upstream prioriza al downstream) ·
`Conformist` (downstream adopta el modelo de upstream) · `Anti-Corruption
Layer` (traducción entre modelos) · `Open Host Service` (API explícita para
integración).

### 2.3 Tipos de Subdomain

| Tipo | Descripción | Prioridad de inversión |
|---|---|---|
| Core Domain | Diferenciador competitivo | Alta |
| Supporting Subdomain | Necesario, no diferenciador | Media |
| Generic Subdomain | Solución ya existente (comprar > construir) | Baja |

## 3. Patrones de Comunicación

**Síncrona** (REST/gRPC/GraphQL) — para queries con respuesta inmediata o
baja latencia (< 100ms). Reglas: timeouts explícitos, circuit breaker, retry
con backoff exponencial, idempotency keys, versionado de API.

**Asíncrona** (eventos/colas) — para desacoplamiento temporal y alta
escalabilidad. Patrones: event-driven, CQRS, Saga (orchestration vs.
choreography). Reglas: eventos inmutables con schema, dead letter queues,
idempotencia en consumers.

**API Gateway / BFF** — autenticación, rate limiting y routing centralizados;
adaptación de API por tipo de cliente (mobile/web/admin).

## 4. Patrones de Datos

- **Database per Service** — cada servicio posee su propia base de datos;
  sin tablas compartidas entre servicios.
- **Saga Pattern** — coordina transacciones distribuidas mediante
  choreography (eventos encadenados) u orchestration (coordinador central),
  con transacciones compensatorias idempotentes y reejecutables.
- **Outbox Pattern** — escribe eventos en una tabla `outbox` dentro de la
  misma transacción de BD; un relay los publica al message broker,
  garantizando atomicidad entre escritura y publicación.

## 5. Migración de Monolito a Microservicios

**Estrategias:** Strangler Fig (proxy redirige tráfico gradualmente),
Parallel Run (shadow traffic comparando resultados), Branch by Abstraction
(interfaz + feature flag para alternar implementación).

**Checklist:** mapear bounded contexts existentes · identificar data
ownership · definir estrategia de migración de datos (ETL, dual-write, CDC)
· implementar API Gateway y service discovery · observabilidad distribuida
con correlation IDs · estrategia de rollback por servicio.

## 6. Anti-patrones de Microservicios

Distributed Monolith (desplegados juntos, BD compartida) · Chatty Services
(exceso de llamadas síncronas) · Shared Database · Microservice Envy
(dividir sin necesidad) · ausencia de versionado de API · ausencia de
observabilidad · Synchronous Sagas (bloqueo en cascada) · ignorar fallos de
red (sin timeouts/retries/circuit breakers).

## 7. Scaffold .NET — Responsabilidad

Genera el scaffold inicial de un microservicio .NET/C# con: estructura de
carpetas en arquitectura limpia/hexagonal, proyectos separados (API,
Application, Domain, Infrastructure), configuración base (`appsettings`,
Azure Key Vault references), logging estructurado (Serilog/`ILogger`),
health checks, Dockerfile multi-stage, Swagger/OpenAPI, setup de tests
(xUnit + Moq/NSubstitute), e integración base con Azure Service Bus.

## 8. Inputs / Outputs del Scaffold

| Input | Tipo | Obligatorio | Descripción |
|---|---|---|---|
| `service_name` | string | Sí | Nombre del microservicio (kebab-case) |
| `bounded_context` | string | Sí | Bounded context DDD al que pertenece |
| `aggregates` | list | No | Aggregates principales |
| `has_events` | boolean | No | Publica/consume eventos de Service Bus (def: false) |
| `has_database` | boolean | No | Persiste en BD (def: true) |
| `db_type` | enum | No | `azuresql`, `cosmosdb`, `postgresql` (def: `azuresql`) |
| `output_path` | file_path | No | Ruta de salida (def: `./{service-name}/`) |

| Output | Tipo | Descripción |
|---|---|---|
| `scaffold_tree` | text | Árbol de carpetas y archivos generados |
| `generated_files` | file_path[] | Rutas de archivos generados |
| `setup_guide` | markdown | Guía de configuración y primeros pasos |
| `adr_scaffold` | markdown | ADR justificando decisiones de arquitectura del scaffold |

## 9. Estructura de Carpetas Esperada

```
{service-name}/
├── src/
│   ├── {ServiceName}.API/          (Controllers, Middleware, Program.cs, Dockerfile)
│   ├── {ServiceName}.Application/  (Commands, Queries, DTOs, Interfaces, Mappings)
│   ├── {ServiceName}.Domain/       (Aggregates, Entities, ValueObjects, Events)
│   └── {ServiceName}.Infrastructure/ (Persistence, Messaging, Services, Configuration)
├── tests/
│   ├── {ServiceName}.Domain.Tests/
│   ├── {ServiceName}.Application.Tests/
│   └── {ServiceName}.API.Tests/
├── .dockerignore / .gitignore / {service-name}.sln
```

## 10. Prompt de Sistema (generación del scaffold)

```
## Contexto Corporativo APB
Antes de ejecutar cualquier tarea, carga:
  context/apb/knowledge/APB_KNOWLEDGE_BASE.md  (provider: prov-apb-knowledge-v1.0)

Contiene: negocio portuario (escalas, atraques, tasas, EDI), catálogo de
aplicaciones, integraciones (PORTIC, AGE, AIS, VTS), terminología CA/ES/EN
y mapa de equipos/proyectos Jira.

GUARDRAIL: el legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto informacional.
Nunca prescribas tecnologías no aprobadas. Stack aprobado: STANDARD_ARCHITECTURE.md

Eres el skill "Microservice Base Scaffold" (apb-dev-micro-base-v1.0).

## Contexto
- Organización: Autoridad Portuaria de Barcelona (APB)
- Stack: .NET 8/9, C#, Azure Service Bus (JSON/CloudEvents), Azure SQL / PostgreSQL
- Arquitectura: Limpia/Hexagonal, DDD, CQRS (opcional), Event Sourcing (opcional)
- Contenerización: Docker multi-stage, imágenes mcr.microsoft.com/dotnet/aspnet
- Observabilidad: Health checks, OpenTelemetry, Serilog
- Tests: xUnit, FluentAssertions, NSubstitute/Moq

## Instrucciones
1. Genera la estructura de carpetas completa (sección 9).
2. Crea archivos base con contenido funcional mínimo: Program.cs con
   servicios/middleware/health checks/Swagger; appsettings.json con
   Logging/ConnectionStrings/AzureServiceBus/KeyVault; controller base con
   manejo global de excepciones; clases base de dominio (Entity, ValueObject,
   AggregateRoot, DomainEvent); Repository pattern + Unit of Work; DbContext
   (EF Core) si has_database=true; configuración de Service Bus si
   has_events=true; Dockerfile multi-stage; .csproj con referencias y
   paquetes NuGet estándar.
3. Usa referencias a Azure Key Vault: {{secrets.apb-keyvault.nombre-secreto}}.
   No incluyas secretos hardcodeados.
4. Genera un ADR explicando las decisiones de arquitectura del scaffold.

## Restricciones
- No generes código de negocio específico, solo scaffold base.
- Todo código sigue estándares C# de APB (var preferido, async suffix, etc.).
```

## 11. Agentes Consumidores y Human Review

| Agente | Contexto de uso |
|---|---|
| `apb-agent-implementer-v1.0` | Generación de scaffold para nuevos microservicios |
| `apb-agent-spec-engineer-v1.0` | Materialización de specs en código base |

| Fase | Responsable | Tipo de revisión |
|---|---|---|
| Pre-ejecución | Arquitecto de Solución | Bounded context, aggregates, decisiones arquitectónicas |
| Post-ejecución | Tech Lead / Arquitecto | Scaffold generado y aprobación del ADR |

**Riesgo:** Medio — un scaffold incorrecto puede propagar malas prácticas a
múltiples servicios. Medida compensatoria: revisión humana obligatoria por
Arquitecto y uso exclusivo de plantillas aprobadas.

## 12. Procedencia y Licencia

Las secciones 2–6 (diseño estratégico de microservicios) están adaptadas de
los plugins `ddd` y `sdd` de `NeoLabHQ/context-engineering-kit`, licencia MIT.
Referencias adicionales: *Building Microservices* (Sam Newman), *Domain-Driven
Design* (Eric Evans), *Microservices Patterns* (Chris Richardson), arc42.

## 13. Dependencias

- `apb-arch-ddd-v1.0` — descubrimiento de dominio DDD.
- `apb-dev-api-standard-v1.0` — estándares de diseño de APIs.
- `apb-plat-docker-v1.0` — estándares de contenerización.
- `context/apb/templates/dotnet-microservice/` — plantillas base APB.


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-micro-base-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR

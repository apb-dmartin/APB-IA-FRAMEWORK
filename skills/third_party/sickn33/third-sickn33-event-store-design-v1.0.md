---
id: "third-sickn33-event-store-design-v1.0"
name: "Skill: Event Store Design (antigravity-awesome-skills)"
description: "Patrones de diseño de event stores para sistemas con event sourcing: requisitos (append-only, ordenación, versionado, idempotencia), comparación de tecnologías, y esquemas de referencia, adaptados del repositorio público sickn33/antigravity-awesome-skills."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
source_repo: "https://github.com/sickn33/antigravity-awesome-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: Event Store Design (antigravity-awesome-skills)

---

## Descripción
Adaptación de la skill `event-store-design` del repositorio público
`sickn33/antigravity-awesome-skills` (MIT para código/tooling; contenido de
la skill sin atribución externa adicional declarada, autoría `community`).
El contenido original cubre los requisitos arquitectónicos de un event
store (append-only, ordenación por stream y global, versionado para
concurrencia optimista, suscripciones en tiempo real, idempotencia), una
tabla comparativa de tecnologías (EventStoreDB, PostgreSQL, Kafka, DynamoDB,
**Marten para .NET**), y esquemas SQL de referencia.

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del agregador
> `sickn33/antigravity-awesome-skills`. Mismo tratamiento que
> `third-sickn33-saga-orchestration-v1.0`: no se instala el agregador, solo
> se incorpora el contenido textual de esta skill puntual. El propio
> contenido original ya menciona **Marten** como motor de event store
> específico para el ecosistema .NET, lo que facilita la adaptación directa
> al stack APB.

## Capacidades
- Checklist de requisitos no negociables de un event store (append-only,
  orden por stream/global, versionado optimista, idempotencia)
- Comparación de tecnologías de event store con sus límites prácticos
- Esquema de referencia para implementación sobre almacén relacional
- Patrones de suscripción para proyecciones y notificación en tiempo real

## Inputs
- `dominio_evented`: agregado o bounded context que requiere event sourcing
- `volumen_esperado`: orden de magnitud de eventos/escrituras esperado
- `stack_destino`: tecnología de persistencia disponible en APB

## Outputs
- `requisitos_event_store`: checklist de requisitos aplicado al caso
- `tecnologia_recomendada`: opción tecnológica justificada para el contexto
- `esquema_referencia`: esquema de tablas/stream adaptado al motor elegido

## Restricciones
- La tabla comparativa original incluye tecnologías ajenas al stack APB
  (Kafka, DynamoDB); su uso queda condicionado a justificación
  arquitectónica explícita, igual que cualquier elección fuera del stack
  estándar (Azure SQL, PostgreSQL/PostGIS, Cosmos DB con justificación)
- El esquema SQL de ejemplo está pensado para PostgreSQL; si el destino es
  Azure SQL, adaptar tipos de datos y mecanismos de optimistic concurrency
  (`rowversion` en lugar de un contador de versión manual, por ejemplo)
- No sustituye `apb-arch-event-driven-v1.0` (diseño event-driven general):
  esta skill es específica de la capa de persistencia de eventos, una vez
  ya decidido que el sistema usará event sourcing

## Adaptaciones APB
- Evaluar **Marten** como opción preferente cuando el destino sea .NET 8
  sobre PostgreSQL; evaluar implementación propia sobre Azure SQL cuando
  el almacén corporativo estándar sea obligatorio
- Documentar la decisión tecnológica en el formato de
  `apb-arch-tech-plan-v1.0` cuando el event store elegido no sea el
  almacén relacional por defecto de APB
- Conectar con `third-sickn33-saga-orchestration-v1.0` cuando el proceso de
  negocio combine sagas con event sourcing

## Ejemplo de Uso
```
Invocar: third-sickn33-event-store-design-v1.0
Input: { dominio_evented: "Ciclo de vida de contenedor en terminal",
         volumen_esperado: "~50k eventos/día", stack_destino: "Azure SQL" }
Output: Checklist de requisitos aplicado, recomendación tecnológica
        (Marten si se admite PostgreSQL, o esquema propio sobre Azure SQL),
        y esquema de referencia adaptado
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

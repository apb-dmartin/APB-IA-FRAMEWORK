---
id: "third-sickn33-domain-driven-design-v1.0"
name: "Skill: Domain-Driven Design Router (antigravity-awesome-skills)"
description: "Comprobación de viabilidad y enrutamiento entre modelado estratégico, mapeo de contextos, patrones tácticos y arquitectura evented de DDD, con checklist de entregables por etapa, adaptado del repositorio público sickn33/antigravity-awesome-skills."
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

# Skill: Domain-Driven Design Router (antigravity-awesome-skills)

---

## Descripción
Adaptación de la skill `domain-driven-design` del repositorio público
`sickn33/antigravity-awesome-skills` (MIT para código/tooling; contenido sin
atribución externa adicional, autoría `self`). El contenido original
plantea una "comprobación de viabilidad" antes de adoptar DDD completo, y
enruta hacia skills especializadas según la etapa del trabajo (estratégica,
táctica, o evented), con un checklist de entregables esperados por etapa.

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del agregador
> `sickn33/antigravity-awesome-skills`. El original enruta a seis skills
> hermanas del mismo bundle (`@ddd-strategic-design`,
> `@ddd-tactical-patterns`, `@cqrs-implementation`,
> `@event-sourcing-architect`, `@projection-patterns`,
> `@architecture-decision-records`) que **no existen en APB** salvo las que
> se incorporan en esta misma sesión. El mapa de enrutamiento se ha
> reescrito por completo hacia componentes APB reales (ver Adaptaciones);
> no se ha copiado el enrutamiento original.

## Capacidades
- Test de viabilidad: cuándo adoptar DDD completo frente a CRUD simple
  (reglas de negocio complejas, colisión de modelos entre equipos,
  contratos de integración inestables, necesidad de auditabilidad)
- Enrutamiento a la etapa de trabajo adecuada según el estado del análisis
  (estratégico, mapeo de contextos, táctico, evented)
- Checklist de entregables esperados por etapa (estratégicos, tácticos,
  evented) para mantener la adopción de DDD medible y no sobredimensionada

## Inputs
- `descripcion_dominio`: descripción del dominio de negocio a modelar
- `senales_complejidad`: indicios de complejidad (múltiples equipos,
  reglas cambiantes, necesidad de auditabilidad)

## Outputs
- `veredicto_viabilidad`: recomendación de adoptar DDD completo o no
- `etapa_recomendada`: a qué componente APB enrutar según el estado actual
- `checklist_entregables`: entregables esperados de la etapa en curso

## Restricciones
- No sustituye los talleres directos con expertos de dominio: el test de
  viabilidad es un filtro inicial, no un sustituto del Event Storming con
  negocio (`apb-disc-cosmic-v1.0` y `apb-disc-business-v1.0` cubren ese
  descubrimiento previo)
- No debe usarse como justificación para sobre-diseñar sistemas simples:
  el propio test de viabilidad exige al menos dos señales de complejidad
  antes de recomendar DDD completo

## Adaptaciones APB
El mapa de enrutamiento original se sustituye por:
- **Modelo estratégico y límites** → `apb-disc-ddd-legacy-v1.0`
  (descubrimiento DDD para legacy) o `apb-disc-business-v1.0` (Business
  Discovery) si es greenfield
- **Integraciones entre contextos** → `third-sickn33-ddd-context-mapping-v1.0`
- **Patrones tácticos de código** → seguir usando las skills de
  `apb-owned/development/` correspondientes al stack (.NET/Django) hasta
  que exista un componente APB dedicado a patrones tácticos DDD
- **Separación lectura/escritura (CQRS)** → evaluar caso por caso; no se
  incorpora una skill `cqrs-implementation` dedicada en esta sesión por ser
  mayormente un router sin contenido técnico propio adicional al de
  `third-sickn33-event-store-design-v1.0` y `third-sickn33-saga-orchestration-v1.0`
- **Historia de eventos como fuente de verdad** →
  `third-sickn33-event-store-design-v1.0`
- **Procesos de larga duración** → `third-sickn33-saga-orchestration-v1.0`
- **Registro de decisiones** → seguir la convención de ADR ya existente en
  `GOVERNANCE.md`, sin necesidad de skill adicional

## Ejemplo de Uso
```
Invocar: third-sickn33-domain-driven-design-v1.0
Input: { descripcion_dominio: "Gestión de escalas portuarias",
         senales_complejidad: "Múltiples equipos (Operaciones, Facturación,
         Aduanas) con reglas de negocio cambiantes" }
Output: Veredicto de viabilidad (DDD completo justificado), etapa
        recomendada (mapeo de contextos), y checklist de entregables
        estratégicos pendientes
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

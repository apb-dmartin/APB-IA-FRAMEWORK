---
id: "third-sickn33-saga-orchestration-v1.0"
name: "Skill: Saga Orchestration Patterns (antigravity-awesome-skills)"
description: "Patrones para coordinar transacciones distribuidas y procesos de negocio de larga duración mediante sagas (orquestación y coreografía), con compensaciones y manejo de timeouts, adaptados del repositorio público sickn33/antigravity-awesome-skills."
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

# Skill: Saga Orchestration Patterns (antigravity-awesome-skills)

---

## Descripción
Adaptación de la skill `saga-orchestration` del repositorio público
`sickn33/antigravity-awesome-skills` (MIT para código/tooling; el contenido
de skills concretas no aparece en la tabla de atribución externa del propio
repo, lo que indica autoría `self`/`community` sin fuente de terceros
adicional declarada). El contenido original cubre dos estilos de saga
(orquestación con coordinador central, y coreografía mediante eventos),
estados de ejecución, compensaciones, y manejo de timeouts, con
implementaciones de referencia en Python/asyncio.

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del
> agregador `sickn33/antigravity-awesome-skills` (1.682+ skills empaquetadas,
> instalable vía `npx`). **No se instala el paquete del agregador**: se
> incorpora únicamente el contenido textual de esta skill puntual, adaptado
> al stack APB. El propio repositorio documenta historial de hallazgos de
> seguridad sobre su *tooling* de instalación (scripts npm, app web) —no
> sobre el contenido de las `SKILL.md`—, ya resueltos según su documentación
> interna; de cualquier modo, no se instala el agregador como dependencia.
> Complementa, sin solapar, a `apb-disc-ddd-legacy-v1.0` (que cubre
> descubrimiento/análisis DDD de legacy, no implementación táctica de sagas).

## Capacidades
- Saga orquestada: coordinador central que ejecuta pasos secuenciales y
  dispara compensaciones en caso de fallo
- Saga por coreografía: pasos coordinados mediante eventos publicados/
  consumidos por cada servicio, sin coordinador central
- Estados de ejecución de saga (`started`, `pending`, `compensating`,
  `completed`, `failed`) y máquina de estados asociada
- Manejo de timeouts por paso con compensación automática si se supera el
  límite
- Patrón alternativo de "ejecución durable" (frameworks tipo DBOS) como
  opción que reduce el código de infraestructura de saga a escribir

## Inputs
- `proceso_negocio`: descripción del proceso de larga duración a coordinar
  (ej. alta de escala portuaria con validaciones secuenciales)
- `servicios_implicados`: lista de servicios/dominios que participan
- `estilo_preferido`: orquestación o coreografía

## Outputs
- `definicion_pasos`: pasos de la saga con su acción y compensación asociada
- `diagrama_estados`: estados y transiciones de la saga
- `codigo_referencia`: estructura de orquestador o manejadores de eventos
  adaptada al lenguaje/stack de destino

## Restricciones
- El contenido original usa Python/asyncio como lenguaje de ejemplo; en APB
  el stack backend primario es **.NET 8/C#**, por lo que el código de
  ejemplo debe traducirse (p. ej. `IHostedService`/`BackgroundService` o
  MassTransit como alternativas a un orquestador Python ad-hoc)
- La mensajería entre pasos/servicios debe usar **Azure Service Bus**
  (estándar corporativo APB), no un "event_publisher" genérico
- No sustituye el análisis DDD de `apb-disc-ddd-legacy-v1.0`: esta skill
  aporta el patrón de implementación táctica, una vez que el análisis de
  dominio ya identificó la necesidad de un proceso de larga duración

## Adaptaciones APB
- Sustituir el `event_publisher` genérico por integración con Azure Service
  Bus (topics/subscriptions) al generar código de referencia
- Conectar con `apb-arch-event-driven-v1.0` como skill previa de diseño
  event-driven, y con `apb-sub-dev-net-v1.0` como consumidor de
  implementación en .NET
- Documentar siempre las compensaciones como parte obligatoria del diseño,
  no como mejora opcional, dado el requisito ENS de trazabilidad de
  transacciones

## Ejemplo de Uso
```
Invocar: third-sickn33-saga-orchestration-v1.0
Input: { proceso_negocio: "Alta de escala portuaria con validación aduanera
         y notificación a terminal", servicios_implicados: ["Escalas",
         "Aduanas", "Terminal"], estilo_preferido: "orquestación" }
Output: Pasos de la saga con compensaciones, diagrama de estados, y
        estructura de orquestador en .NET sobre Azure Service Bus
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

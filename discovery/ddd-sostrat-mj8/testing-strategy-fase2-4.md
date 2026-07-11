# [IA-GEN] Estrategia de Testing — Fases 2, 3 y 4

> **Borrador generado por IA** (APB AI Framework - apb-qa-testing-strategy-v1.0) — pendiente validación humana. No distribuir sin revisión.

**Alcance:** los 10 servicios de Fase 2-4 (PPS, MARPOL/Residuos, Aguada, Marinas y Pesca, Transporte Terrestre, MMPP, PIF, Manifiestos, Aduanas/Control de Contenedores, Concesiones, Facturación y Liquidaciones), complementando `testing-strategy-fase0-1.md`. Misma pirámide: Unit 60% / Contract 20% / Integration 15% / E2E 5%.

## Fase 2

### PPS
- Unit: `POST /access-requests` sin `idempresa` debe rechazarse; cálculo de `ntargetesentregades` vs `ntargetes` no debe superar el máximo solicitado.
- Contract: schema de `SolicitudRegistrada`/`TarjetaCaducadaDetectada` contra `specs/asyncapi-fase2.yaml`.
- Integration: conectores externos Kaba/PortIC — usar test doubles, no el sistema físico real en CI.

### MARPOL/Residuos
- Unit: transición de `idestat` (1-7) solo en el orden esperado — **bloqueante hasta confirmar con negocio los nombres reales de los estados 2-7** (solo el 1 está confirmado literalmente en código, ver `events-catalog.md` §14).
- Contract: validar que `ResiduoPesado` nunca incluye campos fuera de `ResidusLineaData`.
- E2E: flujo completo recogida → pesaje → cierre de lote → factura asociada (cruza con Facturación y Liquidaciones, Fase 4 — coordinar el orden real de implementación con esa dependencia).

### Aguada
- **No se puede definir una estrategia de testing real todavía** — el propio contrato (`specs/openapi-aguada.yaml`) es provisional. Única prueba posible hoy: contra la vista de lectura `VTcSaSolicitud`, no contra un flujo de escritura real.

### Marinas y Pesca
- Unit: `eslora`/`maniga` como valores positivos (no confirmado como regla real, hipótesis razonable a validar).
- Integration: dos sub-recursos (`marina-berths`, `fishing-landing-notes`) en el mismo servicio — verificar que un fallo en uno no bloquea el otro (aislamiento de fallos dentro del mismo proceso).

### Transporte Terrestre
- Unit: `POST .../authorize` sobre un preaviso ya rechazado debe devolver 409, no autorizar silenciosamente.
- Integration: el sub-contexto Parquing queda fuera de este spec (pendiente de descomposición interna, EPIC-07) — no testear como si ya estuviera separado.

## Fase 3

### MMPP
- Unit: `POST .../send` (circuito EDI) no debe ser invocable si `idnotificacio` no está en un estado previo válido.
- E2E: notificación → autorización → envío EDI, con el circuito batch real de `LanzarCircuitoNotificacionMPTasklet.java` como referencia de comportamiento esperado.

### PIF
- Unit: transición de `idestatoperaciopif` (CR/AP/PF/FI/AN/AF) — mismo caveat que MARPOL, nombres completos no confirmados.
- Contract: la vista `VDataSelectorareapif` es de solo lectura — un test de contrato debe fallar si se intenta exponerla como escribible.

### Manifiestos
- Unit: **prioridad alta** — dado que este servicio depende del refactor previo de `CN_Manifest_Impl`/`CN_Partida_Impl` (EPIC-08), los tests de caracterización de ese refactor SON la base de este plan de testing, no un añadido — sin ellos, no hay forma de verificar paridad funcional tras la extracción.
- Integration: verificar que `PartidaActualizada` siempre crea versión nueva (`versio+1`), nunca sobrescribe.

### Aduanas / Control de Contenedores
- Unit: tras la consolidación interna `aduanas`+`terminales` (EPIC-11), verificar que no queden dos caminos de código distintos para el mismo concepto de "traslado de contenedor".
- Integration: `ErrorConciliacionDetectado` — simular al menos un caso de cada `tipuserror` (CN/CV/TER/SSI/CNC/STI/ALI/COA) contra el catálogo real de `ErrorProcConc.java`.
- E2E: consumidor externo (naviera Grimaldi) — coordinar entorno de test con ese tercero antes de dar por probada la integración (no se puede simular sin su colaboración).

## Fase 4

### Concesiones
- Unit: `TituloActualizado` debe publicarse en cada cambio de `idestattitol` — **test de regresión obligatorio**: verificar que no existe ningún camino de código que actualice `TITOL`/`TITOL_MINIM_DADES` sin pasar por la publicación del evento (es la garantía de que el anti-patrón legacy no vuelve).
- Contract: `Garantia` sin agregado propio — verificar que el contrato de API refleja esto (sub-recurso de título, no colección independiente).

### Facturación y Liquidaciones
- Unit: máquina de estados de `idestatliq` (`GE→SE→AC→FA` o `→AN` desde no terminal) — el más crítico de los 15 servicios, cubrir todas las transiciones válidas e inválidas explícitamente.
- Contract: **verificar que este servicio consume `TituloActualizado` y NUNCA escribe directamente en tablas de Título** — este es el test que reemplaza al anti-patrón legacy, debe ejecutarse en cada pipeline, no ser opcional.
- Integration: Clavegueram como sub-recurso de este servicio — confirmar que su ciclo de vida de despliegue no bloquea el de Liquidación/Facturación (son negocios distintos co-desplegados, no deberían acoplar releases).
- E2E: escala → liquidación → aceptación → factura → PDF — el flujo de mayor valor de negocio de todo el roadmap, máxima prioridad de cobertura E2E pese a ser solo el 5% de la pirámide.

## Transversal a Fases 2-4

- Todos los servicios que consumen `/api/v1/container-equipment` (MMPP, Manifiestos, PIF, Aduanas) — test de contrato compartido: ninguno debe fallar si el maestro de Equipamiento devuelve solo los 6 campos reales (no asumir campos operativos que no existen ahí).
- Ningún test de estos 10 servicios debe apuntar a Oracle directamente — siempre contra la réplica CDC en Azure SQL de test, igual que en Fase 0-1.

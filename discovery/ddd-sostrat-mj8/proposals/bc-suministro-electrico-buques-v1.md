---
id: "bc-suministro-electrico-buques-v1"
name: "Suministro Eléctrico a Buques (Shore Power)"
description: |
  Gestión del suministro eléctrico a buques atracados (cold-ironing/Shore Power):
  lecturas de contador, cálculo de consumo, tarifación, liquidación, facturación
  y auditoría de lecturas, vinculado a la escala/atraque del buque. Descubierto
  en la auditoría de cobertura 2026-07-13 — no estaba en el análisis DDD original
  porque `bc-aguada-v1.md` afirmaba (incorrectamente) que no existía evidencia
  de esta funcionalidad en el código.
status: "discovered"
parent_domain: "dom-suministros-buques-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "SeLectura"
entities:
  - "SeLecturaAudit"
  - "SeConsum"
  - "SeConcesionari"
  - "SeLogSincronizacion"
value_objects: []
domain_events:
  - "LecturaElectricidadRegistrada"
  - "ConsumoElectricidadLiquidado"
ubiquitous_language:
  - term: "Lectura"
    definition: "Registro de consumo eléctrico de un buque atracado entre conexión y desconexión, con lectura inicial y final de contador."
  - term: "Tiempo de conexión / Tiempo de atraque"
    definition: "Proporción del tiempo total de atraque durante el cual el buque estuvo conectado al suministro eléctrico — campo real usado en la tarifación."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
  - pattern: "shared-kernel"
    with_context: "bc-liquidacion-v1"
    direction: "bidirectional"
upstream_contexts:
  - "bc-escalas-v1"
downstream_contexts:
  - "bc-liquidacion-v1"
  - "bc-facturacion-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-13"
approved_date: null
source: "auditoria-cobertura-2026-07-13"
notes: "Separado de bc-aguada-v1 tras confirmar con evidencia real (agente de auditoría de cobertura, 2026-07-13) que Shore Power/electricidad SÍ existe en el código, contradiciendo la afirmación anterior de bc-aguada-v1.md. Comparte dominio padre (dom-suministros-buques-v1) con Aguada pero tiene agregado, tablas y flujo de negocio propios — no es una entidad ni sub-recurso de Aguada. Campos NO confirmados con negocio: nombre exacto de los estados de liquidación de una lectura (el código expone acciones 'liquidacionMasiva'/'desliquidar'/'anular' pero no se ha extraído un enum de estados explícito en esta pasada)."
---

# Suministro Eléctrico a Buques (Shore Power)

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Gestiona el suministro eléctrico a buques atracados (equivalente a "cold-ironing"/Shore Power/OPS): registro de lecturas de contador, cálculo del consumo eléctrico real durante el tiempo de conexión, tarifación por concesionario/subtarifa, liquidación, facturación y auditoría de cada lectura.

## Lo que NO incluye

- No incluye el suministro de agua potable (eso es `bc-aguada-v1`, mismo dominio padre pero agregado y tablas distintas).
- No incluye Bunkering (combustible) — confirmado ausente en el código tras búsqueda exhaustiva (ver `bc-aguada-v1.md`).
- No emite la factura final ni calcula el título/concesión asociada — delega en `bc-liquidacion-v1`/`bc-facturacion-v1` vía los mismos flujos genéricos de liquidación/factura que usa Aguada (`liquidacion.LiquidacionAction`, `facturas.FacturasAction`, reutilizados también por electricidad).

## Modelo de Dominio (campos reales confirmados)

### Agregado `SeLectura` (tabla/vista `V_TC_LECTURA_ELECTRICITAT`)

| Campo | Descripción |
|---|---|
| `anyescala`, `numescala` | Año/número de la escala (atraque) del buque a la que pertenece la lectura |
| `idconsignatario`, `idarmador` | Consignatario y armador del buque |
| `navinternacional` | Indicador de navegación marítima internacional |
| `tiempoconexion`, `tiempoconexiontext` | Tiempo real de conexión eléctrica |
| `tiempoatraque`, `tiempoatraquetext` | Tiempo total de atraque (para calcular % de conexión sobre el atraque) |
| `lecturainici`, `lecturafi` | Lectura inicial y final del contador |
| `consumototal` | Consumo total en kWh |
| `idtarifa`, `idsubtarifa`, `idconcesionari`, `puntosuministro` | Datos de tarifación |
| `imptotal`, `impivatotal`, `impfinaltotal` | Importes calculados (base, IVA, total) |

### Entidad `SeConsum` (tabla/vista `V_TC_CONSUM_ELECTRICITAT`)

| Campo | Descripción |
|---|---|
| `vaicodimo` | Número IMO del buque |
| `vainom` | Nombre del buque |
| `vaitipus` | Tipo de buque |
| `conexion`, `desconexion` | Timestamps de conexión/desconexión |
| `duracionhoras` | Duración de la conexión en horas |
| `consumo` | Consumo del intervalo |
| `lecturainicial`, `lecturafinal` | Lecturas de contador del intervalo |

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| LecturaElectricidadRegistrada | emitido | Se ha registrado una nueva lectura de consumo eléctrico para un buque atracado. |
| ConsumoElectricidadLiquidado | emitido | Una lectura ha sido liquidada (acción `liquidacionMasiva` confirmada en código); existe también la operación inversa `desliquidar` y `anular` — sin enum de estados confirmado. |

## Relaciones con Otros Bounded Contexts

- **Upstream de Escalas** (`bc-escalas-v1`) vía `anyescala`/`numescala` — la lectura solo tiene sentido en el contexto de una escala/atraque concreto.
- **Downstream hacia Liquidación/Facturación** — reutiliza los mismos Actions genéricos (`LiquidacionAction`, `FacturasAction`) que Aguada, evidencia de que ambos servicios comparten el mismo patrón de liquidación aunque tengan agregados de negocio distintos.
- El servicio `CN_SeElectricitat_Impl.java` integra directamente con `EscalaDao`, `ArmadorDao`, `AtracadaAspecteDao` y `Vaixell` — mayor acoplamiento a datos maestros de buque que Aguada.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/suministros/electricitat/` (`CN_SeElectricitat_Impl.java`) y `mvc/control/suministros/electricitat/` (`SeLecturaAction.java`, `SeLecturaAuditAction.java`, `SeConsumoAction.java`), ticket de origen `FACTSTD-878`. DTOs en `dataaccess/dto/suministres/electricitat/` (`SeLectura`, `SeLecturaAudit`, `SeConsum`, `SeConcesionari`, `SeLogSincronizacion`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework (auditoría de cobertura) | Propuesta inicial — separado de bc-aguada-v1 tras confirmar con evidencia real que Shore Power/electricidad sí existe en el código |

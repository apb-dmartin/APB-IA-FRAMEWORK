---
id: "bc-posicionament-v1"
name: "Posicionament"
description: |
  Posicionamiento de contenedores/equipos para inspección aduanera/fronteriza:
  solicitud, asignación de turno/lugar y resultado de la inspección física,
  más el registro de incidencias de equipo detectadas durante la operativa.
  Capacidad de negocio real identificada durante el cierre de `coverage-audit.md`
  (2026-07-14), sin bounded context propio hasta esta propuesta.
status: "discovered"
parent_domain: "dom-inspeccion-control-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Posicionament"
entities:
  - "IncidenciaEq"
  - "PosicionamentServei"
  - "MissatgeEdiPosicionament"
value_objects: []
domain_events:
  - "PosicionamentSolicitado"
  - "PosicionamentAsignado"
  - "PosicionamentResuelto"
  - "IncidenciaEquipoRegistrada"
ubiquitous_language:
  - term: "Posicionament"
    definition: "Solicitud de posicionamiento de un contenedor/equipo (identificado por matrícula ISO) para su inspección física en un lugar y turno concretos."
  - term: "SCPP"
    definition: "Servicio de Control y Posicionamiento de Contenedores para inspección — dominio padre, ya cubierto por `bc-inspeccion-scpp-v1`/`bc-pif-v1`."
  - term: "Incidencia de equipo (IncidenciaEq)"
    definition: "Desperfecto o discrepancia detectada en un equipo durante la operativa de posicionamiento/inspección, con reclamación y abono asociados."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-inspeccion-scpp-v1"
    direction: "bidirectional"
  - pattern: "ACL"
    with_context: "bc-integracion-edi-portic-v1"
    direction: "upstream"
upstream_contexts:
  - "bc-inspeccion-scpp-v1"
  - "bc-integracion-edi-portic-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
  - "Azure Service Bus"
proposed_date: "2026-07-21"
approved_date: null
source: "apb-agent-ddd-v1.0"
notes: "Cierra el hallazgo de PLAN_FASES_FUTURAS.md #102 (identificado 2026-07-14 al cerrar el residuo de coverage-audit.md, sin bounded context propio en ese momento). Investigación completada 2026-07-21 con acceso al checkout real (GitHub-Repos/otros/SOSTRAT-Sostrat-MJ8), mismo rigor que los 24 dossiers de aplicación de esta serie — evidencia fichero:línea, sin campos inventados. El acoplamiento síncrono bidireccional con SCPP (Inspeccio/LlocDInspeccio) ya estaba documentado en dossier-19-inspeccion-scpp.md §7/§14 antes de esta propuesta; aquí se completa con el modelo de datos propio de Posicionament."
---

# Posicionament

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión. Grounded en el checkout real `SOSTRAT-Sostrat-MJ8` (`GitHub-Repos/otros/`), no en `APB-IA-FRAMEWORK` (que no contiene código fuente).

## Responsabilidad

Gestionar el ciclo de vida de una solicitud de posicionamiento de contenedor/equipo para inspección: alta de la solicitud, asignación de lugar/turno, registro del resultado de la inspección, y las incidencias de equipo detectadas durante la operativa.

## Lo que NO incluye

No gestiona la inspección física en sí ni el catálogo de lugares/turnos de inspección (`Inspeccio`/`LlocDInspeccio`/`LlocDInspeccioTorn`, ya en `bc-inspeccion-scpp-v1`) — Posicionament consulta y actualiza esas entidades mediante el acoplamiento síncrono ya documentado, no las posee. No gestiona el catálogo de tipos de inspección (`LlocTipusInspeccio`/`NivellDInspeccio`, también SCPP).

## Modelo de Dominio

### Aggregates

| Aggregate | Responsabilidad |
|-----------|----------------|
| `Posicionament` | Raíz de agregado de la solicitud de posicionamiento. PK compuesta `sptposicionament+anyposicionament+seqposicionament` (tabla `POSICIONAMENT`, `dataaccess/dto/Posicionament.java`). |

### Entidades

- `IncidenciaEq` (tabla `INCIDENCIA_EQ`, PK `subport+anyincidencia+seqincidencia`) — incidencia de equipo: tipo, vía/fase de detección, reclamación (`reclamacio`/`datreclamacio`/`datresposta`), importe de daño y de abono (`importdany`/`importabonat`), fotografías/recuento adjuntos (`fitxer`/`fitxerresum`, `nomfitxer`/`nomresum`), referencia cruzada opcional a una inspección de SCPP (`subportinspeccio+anyinspeccio+seqinspeccio`).
- `PosicionamentServei` (tabla no confirmada por Javadoc en esta pasada, PK que comparte prefijo `sptposicionament` con el agregado) — vista/servicio asociado al posicionamiento, expuesto también por la ruta `/posicionamentServei` (`vistasscpp.PosicionamentServeiAction`).
- `MissatgeEdiPosicionament` — correlación EDI propia del circuito `posicionamientoEDI` (campos `stpposicionament`+`anyposicionament`+`seqposicionament`+`nummissatge`+`datproces`; sin Javadoc de columna en el fichero fuente, a diferencia del resto de DTOs de este dossier — nombre de tabla no confirmado, pendiente de confirmar con el equipo si se requiere para el contrato definitivo).

### Campos reales de `Posicionament` (tabla `POSICIONAMENT`)

```json
{
  "sptposicionament": "string",
  "anyposicionament": "integer",
  "seqposicionament": "long",
  "viapeticio": "string",
  "matriculaiso": "string",
  "idtipequipament": "string",
  "idtipoperacio": "string",
  "sptescala": "string",
  "anyescala": "string",
  "numescala": "integer",
  "mercaderia": "string",
  "idconsignatari": "string",
  "idterminal": "string",
  "idlloc": "string",
  "idmotiu": "string",
  "idtipinspeccio": "string",
  "datpossolicitat": "date",
  "datposassignat": "date",
  "datposreal": "date",
  "idestat": "string",
  "resinspeccio": "string",
  "idautoritzacio": "long"
}
```
*(`Posicionament.java` tiene 61 campos totales; se seleccionan aquí los de identidad/negocio/estado. Se omiten ~35 campos de detalle logístico (temperatura, precinto, kilos/embalajes de inspección, observaciones SCPP) y los de auditoría interna estándar — ver el DTO fuente para el detalle completo. `idautoritzacio` es FK hacia PPS (`Autoritzacio`), coherente con el cruce ya señalado como "no investigado en profundidad" en `dossier-19-inspeccion-scpp.md §14`.)*

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| `PosicionamentSolicitado` | emitido | Alta de una solicitud de posicionamiento (`datpossolicitat`). |
| `PosicionamentAsignado` | emitido | Asignación de lugar/turno real (`datposassignat`, `idlloc`). |
| `PosicionamentResuelto` | emitido | Resultado de la inspección incorporado (`datposreal`, `resinspeccio`, `idestat`). |
| `IncidenciaEquipoRegistrada` | emitido | Alta de una incidencia de equipo (`IncidenciaEq`), con o sin inspección SCPP asociada. |

*(Nombres de evento diseñados por analogía con el ciclo de vida real observado en los campos de fecha/estado del DTO — igual que el resto de esta serie, no son nombres tomados literalmente del código legacy, que no tiene arquitectura de eventos propia.)*

## Relaciones con Otros Bounded Contexts

**Acoplamiento síncrono bidireccional con `bc-inspeccion-scpp-v1`** (ya documentado en `dossier-19-inspeccion-scpp.md §7/§14` antes de esta propuesta, ahora confirmado desde el lado de Posicionament): `CN_Posicionament_Impl.processarPosicionament(...)` invoca `CN_CapacitatsInspeccio.ajustarCapacidades(...)` (reasigna turno/día en la misma transacción de alta) y consulta `LlocDInspeccio`/`LlocDInspeccioTorn`/`LlocTipusInspeccio`/`NivellDInspeccio` directamente (imports confirmados). `CN_Inspeccio_Impl.java:1359` sincroniza `resinspeccio` de vuelta a `Posicionament`. Esta es la misma evidencia que ya motivó la recomendación de evaluar fusionar Posicionament junto con PIF+SCPP (`PLAN_FASES_FUTURAS.md #93(a)`) — decisión pendiente de Arquitectura APB, no resuelta por esta propuesta.

**Circuito EDI propio** (`posicionamientoEDI`, batch): recibe/envía mensajes vía `bc-integracion-edi-portic-v1` (filtro `circuito = 'POSICIONAMENT'` o equivalente, a confirmar contra el catálogo real `CircuitEdi`), correlacionado por `MissatgeEdiPosicionament`.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/impl/CN_Posicionament_Impl.java` (1.873 líneas) y las Actions Struts reales confirmadas: `/posicionament`, `/posicionament_popup`, `/posicionamentAudit`, `/motiuDePosicionament`, `/missatgeediposicionament`, `/posicionamentlloc`, `/pda/posicionamentPDA`, `/posicionamentServei`, `/incidenciaEQ`, `/incidenciaEQ_popup`, `/incidenciaEQAudit`, `/incidenciaEQInspeccio` (`struts-config.xml`, 12 rutas confirmadas en esta pasada — `coverage-audit.md §8.2` citaba 19 en un recuento previo por nombre de fichero, no verificado ruta a ruta; posible satélite adicional no revisado en esta sesión). Jobs batch reales: `posicionamientoEDI`, `avisosIncidencias` (nombres ya citados en `coverage-audit.md §8.2`, ficheros XML de Quartz no releídos en esta pasada).

## Riesgos y gaps de evidencia conocidos

- **Recuento de rutas Struts no reconciliado**: 12 confirmadas aquí vs. 19 citadas en `coverage-audit.md §8.2` — posible satélite `struts-config-*.xml` adicional no revisado, o sobreconteo previo por nombre de fichero. Pendiente de reconciliar antes de fijar el alcance de migración definitivo.
- **`PosicionamentServei` sin tabla confirmada por Javadoc** — el fichero fuente no documenta la columna/tabla real como sí lo hacen `Posicionament`/`IncidenciaEq`; confirmar con el equipo o vía DAO antes de fijar el contrato.
- **`MissatgeEdiPosicionament` sin Javadoc de columna** — mismo caso, nombre de tabla no confirmado.
- **Jobs batch no releídos en detalle** (`posicionamientoEDI`/`avisosIncidencias`) — solo confirmados por nombre, no por cron/tasklet real en esta pasada.
- **Decisión pendiente de fusión con PIF+SCPP** (`PLAN_FASES_FUTURAS.md #93(a)`) — esta propuesta documenta Posicionament como bounded context independiente por consistencia con el resto de la serie, pero la evidencia de acoplamiento síncrono es la misma que ya motiva evaluar la fusión; no se prejuzga aquí.
- **Sin testing-strategy/threat-model propios** — mismo gap que el resto de bounded contexts de Fase 6.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-21 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial, cierra `PLAN_FASES_FUTURAS.md #102`. Grounded con acceso al checkout real `SOSTRAT-Sostrat-MJ8` (`GitHub-Repos/otros/`) — `Posicionament.java`, `IncidenciaEq.java`, `MissatgeEdiPosicionament.java` leídos directamente, 12 rutas Struts confirmadas. |

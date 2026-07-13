---
id: "bc-buques-v1"
name: "Buques (Ship Master Data)"
description: |
  Maestro de referencia de buques (ficha técnica, certificados, ISPS, Lloyds,
  servicio regular de aduana). Descubierto en la auditoría de cobertura
  2026-07-13 — no estaba en el análisis DDD original porque vivía en el
  paquete raíz de Struts (sin subpaquete propio) y por tanto no tenía
  ticket Jira de "módulo funcional" asociado.
status: "discovered"
parent_domain: "dom-operaciones-maritimas-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Vaixell"
entities:
  - "VaixellAudit"
  - "VaixellCertificat"
  - "VaixellCertificats"
  - "VaixellISPS"
  - "VaixellLloyds"
  - "VaixellServeiRegularDuana"
value_objects:
  - "TipusDeVaixell (APB/EDI/LL/PE)"
domain_events:
  - "BuqueRegistrado"
  - "BuqueActualizado"
  - "BuqueDadoDeBaja"
ubiquitous_language:
  - term: "Vaixell"
    definition: "Ficha técnica maestra de un buque: eslora, calado, capacidades, certificados, banderas, ISPS, clasificación Lloyds."
  - term: "Caso de uso 01.01.13 Mantenimiento de Buques"
    definition: "Caso de uso formal de negocio identificado literalmente en struts-config.xml (comentario, línea 325) para el ABM completo del maestro de buques."
integration_patterns:
  - pattern: "open-host-service"
    with_context: "bc-escalas-v1"
    direction: "upstream"
  - pattern: "open-host-service"
    with_context: "bc-cruceros-v1"
    direction: "upstream"
  - pattern: "open-host-service"
    with_context: "bc-mmpp-v1"
    direction: "upstream"
upstream_contexts: []
downstream_contexts:
  - "bc-escalas-v1"
  - "bc-cruceros-v1"
  - "bc-mmpp-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-13"
approved_date: null
source: "auditoria-cobertura-2026-07-13"
notes: "El propio dom-operaciones-maritimas-v1 ya anticipaba este bounded context en su domain.md (subdominio 'Buques', código ARGOS 'SHP') — esta propuesta lo confirma con evidencia real de código SÒSTRAT y lo modela formalmente. CRUD completo confirmado (CN_Vaixell.crear/modificar/eliminar/darDeBaja/restaurar), 20 rutas Struts (19 activas + 1 comentada). Consumido por Escalas (service/escalas/impl/CN_Escala_Impl.java), Cruceros (service/cruceros/impl/CN_CreuerEscala_Impl.java, con arrays arrModificacionCE/arrModifCruEscOOPP que disparan notificación a Cruceros ante cambios de campos críticos) y MMPP (12+ ficheros con import directo). Sin evidencia de consumo directo desde PIF. Tabla real: VAIXELL (66 columnas confirmadas por Javadoc de columna, incluye 'lng' añadido por ESCA-1789 para propulsión de gas licuado)."
---

# Buques (Ship Master Data)

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Mantiene la ficha técnica maestra de cada buque que opera en el puerto: identificación (IMO, callsign, bandera), dimensiones (eslora, manga, calado, TPM, GT), capacidades (contenedores, graneles, líquidos, pasajeros, vehículos), certificados, estatus ISPS, clasificación Lloyd's y servicio regular de aduana.

## Lo que NO incluye

No gestiona la escala/atraque en sí (eso es `bc-escalas-v1`), ni la asignación de consignatario/armador a un servicio marítimo concreto (ver `bc-operadores-portuarios-v1`, entidad puente `ServeiMaritimVaixellUsuari`).

## Modelo de Dominio

Agregado `Vaixell` (tabla `VAIXELL`) — campos reales confirmados: `idvaixell, nomvaixell, callsign, bandera, banderaISO, portregistre, gt, numlloyds, tpm, maxmaniga, puntal, maxcalat, maxeslora, potencia, velservei, tipcasc, captls, numpassatgers, numcabines, numcotxes, numcamions, numteus, capliquids, mmsi, tipvaixell, datbaixa, lng` (propulsión gas licuado, ESCA-1789), entre otros 40+ campos.

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| BuqueRegistrado | emitido | Alta de un nuevo buque en el maestro. |
| BuqueActualizado | emitido | Modificación de la ficha técnica — Cruceros se suscribe cuando cambian `nomvaixell/maxmaniga/maxcalat/maxeslora` (evidencia: arrays `arrModificacionCE`/`arrModifCruEscOOPP` en el código legacy). |
| BuqueDadoDeBaja | emitido | Baja lógica del buque (`darDeBaja`/`restaurar`). |

## Relaciones con Otros Bounded Contexts

Upstream (maestro de referencia) de Escalas, Cruceros y MMPP — los tres lo consumen vía import directo de `Vaixell`/`CN_Vaixell` en el código legacy, evidencia de que lo tratan como referencia externa, no como subdominio propio.

## Implementación Actual

`mvc/control/Vaixell*Action.java` + `TipusDeVaixell*Action.java` (paquete raíz, 20 rutas Struts), `service/CN_Vaixell.java`/`_Impl`, `dataaccess/dto/Vaixell.java` (tabla `VAIXELL`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework (auditoría de cobertura) | Propuesta inicial — bounded context descubierto en auditoría de cobertura, confirma el subdominio "Buques" ya anticipado en dom-operaciones-maritimas-v1 |

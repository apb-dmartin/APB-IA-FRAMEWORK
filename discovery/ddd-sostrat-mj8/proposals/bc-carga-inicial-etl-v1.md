---
id: "bc-carga-inicial-etl-v1"
name: "CargaInicialETL"
description: |
  Proceso batch de migración de datos maestros desde el mainframe AS400 hacia
  el esquema de SÒSTRAT. No es un bounded context de negocio, se documenta como
  evidencia de acoplamiento de BBDD compartida entre dominios.
status: "discovered"
parent_domain: null   # NO ENVIAR AL CATÁLOGO — no es un bounded context de negocio (ver notes). El dominio "dom-servicios-transversales-plataforma-v1" que se le asignaba antes ha sido retirado por no tener ya ningún bounded context real que agrupar.
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates: []
entities: []
value_objects: []
domain_events:
  - "CargaInicialCompletada"
ubiquitous_language:
  - term: "Carga Inicial"
    definition: "Proceso de migración de datos maestros AS400 → SÒSTRAT."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-titulo-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-manifiestos-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-mmpp-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-facturacion-v1"
    direction: "upstream"
  - pattern: "conformist"
    with_context: "bc-pps-v1"
    direction: "upstream"
upstream_contexts: []
downstream_contexts:
  - "bc-titulo-v1"
  - "bc-manifiestos-v1"
  - "bc-mmpp-v1"
  - "bc-facturacion-v1"
  - "bc-pps-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack: []
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "NO ES UN BOUNDED CONTEXT DE NEGOCIO — es un ejecutable utilitario/batch de migración (ETL), documentado por su valor como evidencia: confirma en un único punto de entrada (CargaInicial.java) que Título, Manifiestos, MMPP, Facturación y Accesos comparten el mismo AS400 como origen y el mismo esquema SÒSTRAT como destino. Se espera que este proceso quede obsoleto una vez completada la migración de datos a Azure SQL por dominio."
---

# CargaInicialETL

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Migrar datos maestros desde el mainframe AS400 hacia el esquema de base de datos de SÒSTRAT, para al menos 5 dominios de negocio distintos.

## Lo que NO incluye

No contiene lógica de negocio de ningún dominio — es un proceso de infraestructura/ETL puro.

## Modelo de Dominio

*No aplica — no es un bounded context de negocio.*

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| CargaInicialCompletada | emitido | Se ha completado la carga inicial de una entidad. |

## Relaciones con Otros Bounded Contexts

Alimenta datos hacia Título, Manifiestos, MMPP, Facturación y Pases y Permisos — es la evidencia más directa del acoplamiento de BBDD compartida entre estos dominios, al usar un único punto de entrada (`CargaInicial.main()`) para poblar todos ellos desde el mismo origen AS400.

## Implementación Actual

Implementado en `sostrat-CARGASINICIALES/` — ejecutable con main en `initialdata/launcher/CargaInicial.java`, DAOs dedicados en `dataaccess/as400/dao/` (`CncncDao`, `MncabDao`, `Sgmp001Dao`, `FcblhDao`), y beans Spring `CN_*CI` por entidad a cargar (Título, Manifiestos, MMPP, Facturas, Usuarios/LDAP, Mano de Estiba, Tarjetas/Accesos, Garantías).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial a partir de análisis DDD de SOSTRAT-Sostrat-MJ8 |

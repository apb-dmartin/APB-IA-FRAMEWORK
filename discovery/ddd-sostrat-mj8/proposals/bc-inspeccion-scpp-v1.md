---
id: "bc-inspeccion-scpp-v1"
name: "Capacidad e Inspección Fronteriza (SCPP)"
description: |
  Gestión de lugares de inspección fronteriza (PIF), su capacidad diaria, turnos,
  tipos/niveles de inspección y auditoría de inspecciones. Descubierto en la
  auditoría de cobertura 2026-07-13 (paquete raíz `Inspeccio*`/`LlocDInspeccio`,
  distinto de bc-pif-v1 que cubre OPERACIO_PIF2).
status: "discovered"
parent_domain: "dom-inspeccion-control-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "LlocDInspeccio"
entities:
  - "Inspeccio"
  - "LlocDInspeccioTorn"
  - "LlocDInspeccioPeriod"
  - "TipusDInspeccio"
  - "NivellDInspeccio"
  - "ServeiDInspeccio"
  - "ResultatDInspeccio"
  - "InspeccioAudit"
value_objects: []
domain_events:
  - "InspeccionRegistrada"
  - "CapacidadPifActualizada"
ubiquitous_language:
  - term: "Lloc d'Inspecció"
    definition: "Lugar físico de inspección fronteriza (PIF) con capacidad máxima diaria y calendario de turnos."
  - term: "SCPP"
    definition: "Servicio de Control y Posicionamiento de Contenedores para inspección — mismo subdominio ya anticipado en dom-inspeccion-control-v1."
integration_patterns:
  - pattern: "shared-kernel"
    with_context: "bc-pif-v1"
    direction: "bidirectional"
upstream_contexts: []
downstream_contexts:
  - "bc-pif-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-13"
approved_date: null
source: "auditoria-cobertura-2026-07-13"
notes: "Distinto de bc-pif-v1 (que cubre OPERACIO_PIF2, el registro operativo de cada inspección concreta): este BC cubre la gestión de CAPACIDAD del puesto de inspección (calendario, turnos, niveles/tipos de inspección) — ambos comparten el dominio dom-inspeccion-control-v1 y probablemente deban fusionarse o quedar como agregados relacionados dentro del mismo servicio, a decidir con Arquitectura APB. Relacionado también con Posicionament (columna SPTPOSICIONAMENT en tabla INSPECCIO) y con Mercancías (TaricCN/TipusDEmbalumUnece en el mismo bloque de struts-config.xml, ticket PIF-1429 confirmado en comentario)."
---

# Capacidad e Inspección Fronteriza (SCPP)

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Gestiona la capacidad operativa del Puesto de Inspección Fronteriza: lugares de inspección con su capacidad diaria máxima, turnos, tipos y niveles de inspección, resultados y auditoría de cada inspección.

## Lo que NO incluye

No gestiona el registro operativo de cada operación PIF concreta sobre una mercancía (eso es `bc-pif-v1`, tabla `OPERACIO_PIF2`) — este BC es la capa de planificación/capacidad del recurso físico de inspección, no la ejecución. **Recomendación explícita**: evaluar con Arquitectura APB si debe fusionarse con `bc-pif-v1` en un único servicio, dado que comparten dominio (`dom-inspeccion-control-v1`) y ticket de origen (PIF-1429).

## Modelo de Dominio

`LlocDInspeccio` (tabla `LLOC_D_INSPECCIO`, con `CAPMAXSTDDIA` de capacidad diaria, columna `DATACTNOUPIF` que referencia el PIF) + `LlocDInspeccioTorn`/`LlocDInspeccioPeriod` (turnos), `TipusDInspeccio`/`NivellDInspeccio`/`ServeiDInspeccio` (catálogos), `Inspeccio` (tabla `INSPECCIO`, columna `SPTPOSICIONAMENT` que la enlaza con Posicionament).

## Relaciones con Otros Bounded Contexts

Comparte dominio con `bc-pif-v1`. Relacionado con Posicionamiento de contenedores (`/posicionament`, mismo bloque de struts-config.xml) y con catálogos de Mercancías (TARIC, tipos de embalaje UNECE).

## Implementación Actual

`mvc/control/InspeccioAction.java`, `LlocDInspeccioAction.java`, `LlocDInspeccioTornAction.java`, `NivellDInspeccioAction.java`, `TipusDInspeccioAction.java`, `ServeiDInspeccioAction.java`, `InspeccioInternetAction.java`, `InspeccioPDAAction.java` (paquete raíz), más `scppauditorias/InspeccioAuditAction.java` y `vistasscpp/InspeccioServeiAction.java`.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework (auditoría de cobertura) | Propuesta inicial — bounded context descubierto en auditoría de cobertura; recomienda evaluación de fusión con bc-pif-v1 |

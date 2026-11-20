---
id: "bc-aguada-v1"
name: "Aguada"
description: |
  Suministro de agua potable a buques durante su escala. Separado de Marinas y
  Pesca tras reparentar contra el catálogo real de dominios (dom-suministros-buques-v1
  agrupa Aguada con Shore Power/OPS y Bunkering, no con Marinas/Pesca).
status: "discovered"
parent_domain: "dom-suministros-buques-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "SaSolicitud"
entities:
  - "SaRegistreSuministre"
value_objects: []
domain_events:
  - "SolicitudAguadaProcesada"
ubiquitous_language:
  - term: "Solicitud d'Aiguada"
    definition: "Solicitud de suministro de agua potable a un buque."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-escalas-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-escalas-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-11"
approved_date: null
source: "apb-sub-ddd-code-v1.0"
notes: "REPARENTADO 2026-07-11 de un bounded context inventado (bc-servicios-auxiliares-buque-v1, que agrupaba Aguada+Marinas+Pesca) a dom-suministros-buques-v1, el dominio real ya existente en el catálogo (que agrupa Aguada con Shore Power/OPS y Bunkering, no con Marinas/Pesca — ver dom-pesca-marinas-v1 para esos). GAP DE EVIDENCIA sin resolver: las clases DTO transaccionales reales (SaSolicitud, SaSolicitudPk, SaSolicitudAudit, SaRegistreSuministre) NO existen como código fuente en el checkout de SOSTRAT-Sostrat-MJ8 — solo compiladas en sostrat-BATCH/lib/sostrat.jar. Los aggregates/entities de este fichero son nombres de clase inferidos por los imports del código de servicio, no confirmados campo a campo — ver events-catalog.md §15 para el detalle del gap y la vista de solo lectura VTcSaSolicitud usada como evidencia indirecta."
---

# Aguada

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Responsable de la gestión de solicitudes de suministro de agua potable a buques durante su escala.

## Lo que NO incluye

No incluye Bunkering (combustible, confirmado ausente tras búsqueda exhaustiva) **ni Shore Power/electricidad**.

> **Corrección 2026-07-13**: la versión anterior de esta sección afirmaba que tampoco se había encontrado evidencia de Shore Power/electricidad. Es **incorrecto** — existe un subdominio funcional completo y activo bajo `service/suministros/electricitat/` (ticket `FACTSTD-878`), con Actions (`SeLecturaAction`, `SeLecturaAuditAction`, `SeConsumoAction`), DTOs (`SeLectura`, `SeConsum`, mapeando `V_TC_LECTURA_ELECTRICITAT`/`V_TC_CONSUM_ELECTRICITAT`) y flujo de negocio completo (lectura de contador → consumo → tarifación → liquidación → factura → auditoría), vinculado a la escala/atraque del buque (`anyescala`/`numescala`, `idarmador`, `tiempoatraque`). Ver el bounded context nuevo `bc-suministro-electrico-buques-v1`, separado de Aguada por tener agregado y flujo propios (aunque comparte el mismo dominio padre `dom-suministros-buques-v1`).

## Modelo de Dominio

*Sin confirmar campo a campo — ver gap de evidencia en `notes`.*

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| SolicitudAguadaProcesada | emitido | Se ha procesado una solicitud de aguada. |

## Relaciones con Otros Bounded Contexts

Downstream de Escalas vía `EscalaPk`.

## Implementación Actual

Implementado en SÒSTRAT bajo `service/aguada/` (`CN_SolicitudAguada.java`, `CN_RegistroSuministro.java`), pero sin las clases DTO fuente reales disponibles en este checkout.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial, como parte de bc-servicios-auxiliares-buque-v1 |
| 1.1.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Separado como bounded context propio y reparentado a dom-suministros-buques-v1 (dominio real del catálogo) |
| 1.2.0 | 2026-07-13 | APB AI Framework (auditoría de cobertura) | Corregida la sección "Lo que NO incluye": Shore Power/electricidad SÍ existe en el código (`suministros.electricitat`, FACTSTD-878) — separado como `bc-suministro-electrico-buques-v1` |

---
id: "dom-mano-estiba-v1"
name: "Mano de Estiba"
description: |
  Gestión de la contratación, comandas y operativa del personal de estiba
  portuaria (estibadores). Capacidad de negocio distinta de Transporte
  Terrestre y de Accesos — gestión de personal, no de movimiento físico de
  mercancías ni de control de acceso.
status: "discovered"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
subdomains:
  - "Contratación de personal de estiba"
  - "Comandas y operativa"
bounded_contexts:
  - "bc-mano-estiba-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8 (service/manoEstiba/)"
  - "MST (microservicio externo ya en marcha, referenciado desde ticketgranting-api-client)"
strategic_classification: "supporting"
ubiquitous_language:
  - term: "Contractació"
    definition: "Contratación de personal de estiba."
  - term: "Comanda"
    definition: "Comanda/pedido de personal de estiba para una operativa concreta."
proposed_date: "2026-07-11"
approved_date: null
source: "apb-agent-ddd-v1.0"
notes: "Creado 2026-07-11 tras confirmar con el usuario que forzar este bounded context bajo dom-transporte-terrestre-v1 (por compartir el eje 'movimiento en el recinto') era un encaje conceptual pobre — la gestión de personal de estiba no es la misma capacidad de negocio que el transporte terrestre de mercancías. Ninguno de los 21 dominios del catálogo original (sesión top-down 2026-06-30) mencionaba estiba/MANEST — es un hallazgo exclusivo de este análisis de código, con evidencia de que ya existe un microservicio externo ('MST') sustituyéndolo orgánicamente."
---

# Mano de Estiba

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Descripción

Dominio de la gestión de personal de estiba portuaria: contratación, comandas de personal para operativas concretas, y su desarrollo (operativas, especialidades, equipos).

## Motivación

Identificado en el análisis de código de SÒSTRAT (`service/manoEstiba/`) sin equivalente en el catálogo de dominios existente. Se propone como dominio propio, no como subdominio forzado de otro, porque la gestión de personal de estiba es una capacidad de negocio distinta (recursos humanos operativos del puerto) de transporte terrestre, accesos, o cualquier otro dominio ya catalogado.

## Bounded Contexts Identificados

- **Mano de Estiba** (`bc-mano-estiba-v1`) — contratación, comandas y operativa. Ya en proceso de extracción orgánica hacia un microservicio externo ("MST").

## Relación con Otros Dominios

Comparte el eje "operativa en el recinto portuario" con Transporte Terrestre y Accesos, pero sin dependencia de código detectada hacia ninguno de los dos.

## Sistemas Actuales

`service/manoEstiba/` en SÒSTRAT (~20 DTOs). El microservicio externo "MST", referenciado desde `ticketgranting-api-client`, sugiere que este dominio ya está siendo modernizado independientemente de este análisis.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-11 | APB AI Framework (apb-agent-ddd-v1.0) | Propuesta inicial, tras confirmar con el usuario que merece dominio propio en vez de reparenting forzado |

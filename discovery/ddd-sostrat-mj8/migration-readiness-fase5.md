# [IA-GEN] Preparación de Fase 5 (Escalas → migración hacia ARGOS)

> **Borrador generado por IA** (APB AI Framework - apb-agent-ddd-v1.0) — pendiente validación humana. No distribuir sin revisión.

**Por qué este documento no es un OpenAPI/AsyncAPI como las Fases 0-4**: la Fase 5 dejó de ser una extracción a servicio nuevo el 2026-07-11, tras confirmar con evidencia de código que ARGOS (`APB.API.TES`, `MS_PORTCALL`) ya consume en producción la escala de SÒSTRAT (evento real `MSG0004 SOSTRAT→TES`, DTO `PortCallCreatedDto.cs` con `Origin=SOSTRAT` por defecto y campos idénticos al modelo legacy). Generar un contrato OpenAPI de "servicio Escalas nuevo" contradiría ese hallazgo — sería inventar un sistema que no hace falta construir. Ver `decomposition-roadmap.md` Fase 5 y `catalog-comparison.md` categoría B para la evidencia completa.

## Lo que existe ya (no hay que generarlo)

- Contrato real de `APB.API.TES` (`PortCallCreatedDto.cs`, consumers `TesPortCallCreatedConsumer.cs`/`TesBerthUpdatedConsumer.cs`) — es el contrato de destino real, vive en el repositorio `APB.API.TES`, no en este análisis.
- Dominio `dom-operaciones-maritimas-v1` ya `proposed` en `apb-domain-catalog`.

## Lo que falta antes de poder ejecutar esta fase (ninguno se puede resolver con más análisis de código)

1. **Sesión formal con el equipo de ARGOS/AOM** (Alberto Ponseti, Jose Joaquin Mena — ver `APB_KNOWLEDGE_BASE.md`) para:
   - Confirmar el mapeo exacto de campos entre el modelo SÒSTRAT (`Escala.idsubport/anyescala/numescala`) y el DTO real de TES (`PortCallCreatedDto.IdSubPort/YearPortCall/NumPortCall`) — no confirmado 1:1 por nombre en este análisis, solo por semántica.
   - Acordar si el flujo `SOSTRAT→TES` se invierte (ARGOS pasa a ser el maestro de escritura) o se retira gradualmente con un periodo de coexistencia.
   - Confirmar si Cruceros (`dom-cruceros-v1`, dominio de negocio separado en el catálogo) necesita su propio frontend en el portal operativo o se integra dentro de ARGOS.
2. **Separar la lógica de liquidación/facturación de `EscalaAction.java`** (81 referencias a `Liquidacion`/`Facturacio` encontradas) hacia el servicio de Facturación y Liquidaciones — **esto sí es ejecutable ya, no depende de ARGOS**, y debería hacerse en paralelo a la Fase 4, no esperar a la Fase 5.
3. **Migrar los consumidores ya extraídos** (Ferrocarril, MARPOL, Servicios Auxiliares) del contrato provisional que usaban internamente hacia el contrato real de ARGOS/TES, una vez acordado el punto 1.

## Recomendación

No generar más artefactos técnicos (specs, testing strategy, threat model) para "Escalas" hasta que la sesión con ARGOS del punto 1 tenga lugar — cualquier contrato que se escriba ahora sería sobre un sistema hipotético, no sobre el real. El punto 2 (separar liquidación de `EscalaAction.java`) es la única pieza de esta fase que se puede y debe adelantar sin esperar a esa sesión.

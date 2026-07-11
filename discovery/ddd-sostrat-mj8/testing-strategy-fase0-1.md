# [IA-GEN] Estrategia de Testing — Fase 0-1 (Datos Maestros de Equipamiento, Ferrocarril, Mano de Estiba, Depotsis)

> **Borrador generado por IA** (APB AI Framework - apb-qa-testing-strategy-v1.0) — pendiente validación humana. No distribuir sin revisión.

**Alcance:** los 4 servicios de Fase 0-1 del roadmap (ver `decomposition-roadmap.md`), para los que ya existen specs formales en `specs/`.
**Pirámide aplicada** (`apb-qa-testing-strategy-v1.0`): Unit 60% / Contract 20% / Integration 15% / E2E 5%. Principio: testear el flujo de eventos, no solo el código.

## 1. Unit Tests (60%) — por servicio

### Datos Maestros de Equipamiento
- Validación de `matriculaiso` contra el patrón ISO 6346 (`^[A-Z]{4}[0-9]{7}$` — **confirmar con negocio si el código legacy aplica esta validación real, no se ha verificado en `Equipament.java`, solo añadida como supuesto razonable en el OpenAPI**).
- Rechazo de `POST /container-equipment` sin `idtipequipament` válido contra el catálogo `TipusEquipament`.
- Idempotencia de `EquipamientoActualizado`: aplicar el mismo evento dos veces no debe generar dos históricos distintos.

### Ferrocarril Portuario
- Transición de `idtipoperacio` solo entre los 4 valores reales (`ENTRADA`/`SALIDA`/`MANIOBRA`/`INTERVENCION`) — rechazar cualquier otro valor.
- `POST /rail-operations/{id}/cancel` sobre una operación ya en estado terminal debe devolver 409, no aplicar la cancelación silenciosamente.
- Cálculo/validación de `lontren`/`taratren` como valores no negativos (no confirmado como regla real en el código, añadir como hipótesis a validar con negocio).

### Mano de Estiba
- `POST /stevedore-work-orders` con `idcontractacio` inexistente debe devolver 404, no crear la comanda huérfana.
- Verificar con el equipo de "MST" (microservicio externo ya en marcha) si hay reglas de negocio duplicadas que deban eliminarse de este servicio en vez de re-testearse aquí.

### Depotsis
- Creación de una nueva versión (`versio`) de una solicitud existente no debe alterar versiones anteriores (patrón versionado confirmado en `DepotsisSolicitudVersio.java`).
- `estat` debe seguir una máquina de estados — **dominio de valores real no confirmado en el código analizado, bloqueante para escribir el test hasta que negocio lo confirme** (ver `readiness-assessment.md`).

## 2. Contract Tests (20%) — validación de schema/CloudEvents

- Los 4 servicios: validar que cada evento publicado cumple el schema definido en `specs/asyncapi-fase0-1.yaml` (herramienta sugerida: validación JSON Schema del `data` contra `x-data-schema` antes de publicar, no solo del envelope CloudEvents).
- **Regla específica para `EquipamientoActualizado`** (ver `events-catalog.md` §13): un test de contrato debe fallar explícitamente si el payload incluye campos operativos (peso, estado aduanero) que no están en `EquipamientoData` — es el anti-patrón que este servicio existe para evitar, y un test de contrato es la forma de que no vuelva a colarse.
- Validar los 4 `openapi-*.yaml` de `specs/` contra un linter de OpenAPI (p.ej. Spectral) como parte del pipeline CI — no manual.

## 3. Integration Tests (15%) — Service Bus real / test containers

- Publish/consume real contra un namespace de Service Bus de test (no fakes) para los 7 eventos de `specs/asyncapi-fase0-1.yaml`.
- Verificar el comportamiento de DLQ: forzar un mensaje malformado y confirmar que aterriza en `evt.sostrat.<bc>.dlq`, no se pierde ni bloquea la cola principal.
- **Caso específico Ferrocarril**: verificar el comportamiento cuando `portescalatren`/`anyescalatren`/`numescalatren` no resuelve a una escala real — el mapeo hacia `EscalaPk` no está confirmado 1:1 por nombre (ver `decomposition-roadmap.md` Fase 5), este es el punto de mayor riesgo de integración de los 4 servicios.
- Integración con el servicio de Datos Maestros de Equipamiento desde Depotsis (consumidor) — aunque `DepotsisSolicitudVersio` no mostró un campo `idequipament` explícito en la extracción de código (ver `api-surface-by-phase.md` Fase 1), confirmar si existe una relación real antes de dar la integración por innecesaria.

## 4. E2E Tests (5%) — flujos de negocio completos

- **Flujo Ferrocarril**: registrar operación de entrada → consultarla → anularla → verificar que el estado final es consistente en API y evento publicado.
- **Flujo Mano de Estiba**: registrar contratación → asignar comanda → verificar consistencia con el servicio externo "MST" si ya está integrado en el entorno de test.
- **Flujo Datos Maestros de Equipamiento**: registrar equipo → consumirlo desde un segundo servicio simulado → actualizar atributo → verificar que el segundo servicio recibe la actualización sin duplicar el registro.

## 5. Fuera de alcance de este documento (requiere sesión dedicada)

- Migración/reconciliación de datos legacy Oracle → Azure SQL (CDC) — testing de migración de datos es una disciplina distinta a testing funcional, no cubierta aquí.
- Pruebas de carga/rendimiento — requiere `apb-qa-performance-v1.0` con objetivos de SLO reales (no definidos todavía).
- Los otros 11 servicios del roadmap — esta estrategia se replica fase a fase, no se ha generado de golpe para las 15 apps (mismo principio incremental que las specs, ver `readiness-assessment.md`).

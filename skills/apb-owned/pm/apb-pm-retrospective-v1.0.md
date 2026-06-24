---
id: "apb-pm-retrospective-v1.0"
name: "Retrospective"
description: "Retrospectiva post-epic/sprint especializada en arquitecturas orientadas a eventos.\
  \ Extrae lecciones de flujos de eventos, compensaciones, y m\xE9tricas de sistema."
version: "1.0.0"
status: "draft"
owner: "PMO APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
consumed_by:
  - "apb-agent-spec-engineer-v1.0"
created_date: "2026-06-20"
review_date: "2026-06-24"
---

> Procedencia: Adaptado de bmad-method (bmad-retrospective) (licencia MIT). Contenido adaptado y
> generalizado para el APB AI Framework.

# APB Retrospective: Retrospectiva Orientada a Eventos

## Visión General

Retrospectiva post-epic o post-sprint especializada en sistemas orientados a eventos. Enfocada en lecciones de arquitectura, flujos de eventos, compensaciones, y métricas del sistema — no solo en proceso de desarrollo.

**Principio fundamental:** La retrospectiva es sobre el sistema, no sobre las personas. No blame.

## Cuándo Usar

- Al finalizar un epic (flujo de negocio completo)
- Al finalizar un sprint (si hay lecciones técnicas relevantes)
- Cuando ocurre un incidente de producción relacionado con eventos
- Cuando el usuario dice "retrospectiva" o "retro del epic"
- Periódicamente (cada 2-3 sprints) para revisar métricas de eventos

## El Proceso

### Parte 1: Revisión del Epic

#### Métricas de Eventos

```
## Métricas del Epic: [Nombre]

### Volumen de Eventos
| Evento | Publicados | Consumidos | DLQ | Error Rate |
|--------|-----------|-----------|-----|------------|
| [Evento A] | [N] | [N] | [N] | [N]% |
| [Evento B] | [N] | [N] | [N] | [N]% |

### Latencia
| Evento | p50 | p95 | p99 | Objetivo |
|--------|-----|-----|-----|----------|
| [Evento A] | [N]ms | [N]ms | [N]ms | < [N]ms |
| [Evento B] | [N]ms | [N]ms | [N]ms | < [N]ms |

### Sagas
| Saga | Completadas | Compensadas | Timeout | Avg Duration |
|------|------------|-------------|---------|-------------|
| [Saga A] | [N] | [N] | [N] | [N]s |

### Throughput
| Servicio | Eventos/seg | CPU | Memoria |
|----------|------------|-----|---------|
| [Servicio A] | [N] | [N]% | [N]MB |
| [Servicio B] | [N] | [N]% | [N]MB |
```

#### Incidentes y Problemas

```
## Incidentes Durante el Epic

| Fecha | Severidad | Descripción | Root Cause | Resolución |
|-------|-----------|-------------|------------|------------|
| [Fecha] | [Sev] | [Desc] | [Causa] | [Fix] |

## Problemas Sin Incidente

| Problema | Impacto | Frecuencia | Mitigación Actual |
|----------|---------|-----------|-------------------|
| [Desc] | [Impacto] | [Freq] | [Mitigación] |
```

### Parte 2: Discusión Estructurada

#### 1. Qué Funcionó Bien (Event-Driven)

```
## ✅ Lo Que Funcionó

### Arquitectura
- [ ] La topología de Service Bus fue clara y escalable
- [ ] Los schemas CloudEvents facilitaron la integración
- [ ] La separación por bounded contexts funcionó

### Patrones
- [ ] Outbox pattern garantizó consistencia
- [ ] Saga orquestada manejó transacciones complejas
- [ ] Idempotencia evitó duplicados en producción

### Observabilidad
- [ ] Distributed tracing facilitó debugging
- [ ] Métricas de DLQ alertaron temprano
- [ ] Logs estructurados aceleraron investigación

### Equipo
- [ ] Comunicación entre equipos de servicios
- [ ] Documentación de eventos (AsyncAPI)
- [ ] Revisión de contratos antes de implementar
```

#### 2. Qué Necesita Mejora (Event-Driven)

```
## ⚠️ Lo Que Necesita Mejora

### Arquitectura
- [ ] La topología creció demasiado (topic explosion)
- [ ] Dependencias circulares entre servicios
- [ ] Falta de documentación de eventos legacy

### Patrones
- [ ] Compensaciones no siempre fueron idempotentes
- [ ] Retry policies demasiado agresivas
- [ ] Falta de circuit breaker en consumidores

### Observabilidad
- [ ] Difícil tracear eventos entre múltiples servicios
- [ ] Métricas no alertaron antes del incidente
- [ ] DLQ monitoring insuficiente

### Proceso
- [ ] Cambios de schema sin comunicación a consumidores
- [ ] Tests de integración insuficientes
- [ ] Falta de pruebas de carga
```

#### 3. Lecciones Aprendidas

```
## 📚 Lecciones Aprendidas

### Lección 1: [Título]
**Contexto:** [Qué pasó]
**Descubrimiento:** [Qué aprendimos]
**Acción:** [Qué haremos diferente]

### Lección 2: [Título]
**Contexto:** [Qué pasó]
**Descubrimiento:** [Qué aprendimos]
**Acción:** [Qué haremos diferente]

### Lección 3: [Título]
**Contexto:** [Qué pasó]
**Descubrimiento:** [Qué aprendimos]
**Acción:** [Qué haremos diferente]
```

### Parte 3: Preparación del Próximo Epic

#### Acciones de Mejora

```
## 🎯 Acciones de Mejora

| Acción | Owner | Prioridad | Sprint Target | Métrica de Éxito |
|--------|-------|-----------|---------------|-----------------|
| [Acción 1] | [Owner] | [P0/P1/P2] | [Sprint N] | [Métrica] |
| [Acción 2] | [Owner] | [P0/P1/P2] | [Sprint N] | [Métrica] |
| [Acción 3] | [Owner] | [P0/P1/P2] | [Sprint N] | [Métrica] |
```

#### Ajustes Arquitectónicos

```
## 🔧 Ajustes Arquitectónicos Propuestos

### Cambios en Topología
- [ ] Consolidar topics [A] y [B] en uno solo
- [ ] Añadir subscription [X] para nuevo servicio
- [ ] Separar topic [Y] en dos por volumen

### Cambios en Patrones
- [ ] Implementar circuit breaker en [servicio]
- [ ] Añadir cache de idempotencia distribuida
- [ ] Migrar saga de coreografía a orquestación

### Cambios en Observabilidad
- [ ] Añadir métrica de "event age" (tiempo en cola)
- [ ] Dashboard de "saga health" en tiempo real
- [ ] Alerta de "consumer lag" > 1000 mensajes
```

### Parte 4: Documento de Retrospectiva

Generar `docs/apb/retrospectives/YYYY-MM-DD-epic-[nombre].md`:

```markdown
# Retrospective: [Nombre del Epic]

## Fecha: [Fecha]
## Participantes: [Lista]

## Resumen Ejecutivo
[2-3 oraciones con hallazgos clave]

## Métricas
[Tablas de métricas de eventos]

## Lo Que Funcionó
[Lista con ejemplos específicos]

## Lo Que Necesita Mejora
[Lista con ejemplos específicos]

## Lecciones Aprendidas
[3-5 lecciones con contexto y acción]

## Acciones de Mejora
[Tabla con owner y timeline]

## Ajustes Arquitectónicos
[Propuestas con justificación]

## Métricas de Referencia para Próximo Epic
[Baseline para comparar]
```

## Integración con el Flujo APB

```
[epic completado] → apb:retrospective → [documento de lecciones] → [ajustes arquitectónicos] → próximo epic
```

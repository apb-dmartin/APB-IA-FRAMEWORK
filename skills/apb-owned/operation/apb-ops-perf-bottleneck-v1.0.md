---
id: "apb-ops-perf-bottleneck-v1.0"
name: "Detección de Cuellos de Botella de Rendimiento"
description: "Analiza código, queries y configuración de un servicio APB para identificar cuellos de botella de rendimiento (queries N+1, falta de índices, llamadas síncronas bloqueantes, asignación de memoria excesiva) y propone ajustes concretos."
version: "1.0.0"
status: "draft"
owner: "Plataforma APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Detección de Cuellos de Botella de Rendimiento

---

## 🎯 Propósito

Analiza código fuente, queries SQL/GeoDjango y configuración de infraestructura de un
servicio APB para identificar cuellos de botella de rendimiento conocidos, y propone ajustes
concretos y verificables — no recomendaciones genéricas de "optimizar el código".

---

## ⚡ Trigger

Bajo demanda al iniciar `apb-agent-tech-debt-v1.0`, tras detectar SLO incumplido en
`apb-ops-slo-design-v1.0`/`apb-agent-sre-v1.0`, o como parte de una auditoría periódica de
servicios críticos.

---

## 📥 Input

- Código fuente del servicio (.NET/C#, Django/GeoDjango)
- Queries SQL/PostGIS relevantes, o acceso a logs de queries lentas (Azure SQL Query Store,
  `pg_stat_statements` para PostgreSQL/PostGIS)
- Métricas de Application Insights / Azure Monitor si están disponibles (latencia P95/P99,
  uso de CPU/memoria)

---

## 📤 Output

- Lista de cuellos de botella detectados, cada uno con: ubicación exacta (archivo:línea o
  query), patrón detectado, impacto estimado, y ajuste propuesto
- Clasificación por esfuerzo de corrección (trivial / moderado / requiere rediseño)

---

## 🔄 Proceso

1. **Detección de patrones de código**: queries N+1 (ORM .NET/EF Core, Django ORM), llamadas
   HTTP síncronas en contextos que deberían ser async, falta de paginación en endpoints que
   devuelven colecciones grandes.
2. **Análisis de queries**: ausencia de índices en columnas usadas en `WHERE`/`JOIN`/`ORDER BY`
   frecuentes; para datos geoespaciales, ausencia de índice GIST/SP-GiST en columnas
   `geography`/`geometry` (PostGIS) o uso incorrecto de `::geography` vs `::geometry` sin
   justificación (ver SRID 4326 como estándar APB).
3. **Análisis de configuración**: timeouts mal configurados, pools de conexión
   sub-dimensionados, ausencia de caché en datos de lectura frecuente y baja volatilidad.
4. **Estimación de impacto**: correlacionar cada hallazgo con métricas reales si están
   disponibles (ej. "esta query N+1 se ejecuta 40 veces por request, P95 de 1.2s").
5. **Propuesta de ajuste**: cada hallazgo incluye una propuesta concreta (ej. "usar
   `.Include()` para eager loading", "crear índice `CREATE INDEX ... USING GIST`", "envolver
   en `await Task.WhenAll(...)`"), nunca solo "optimizar esta sección".

---

## 📋 Reglas y Constraints

- No aplica ningún cambio automáticamente — diagnóstico únicamente.
- No propone reescrituras especulativas; cada ajuste debe resolver un patrón detectado
  concreto, no una refactorización general (coherente con
  `apb-dev-simplicity-first-v1.0`/`apb-dev-surgical-changes-v1.0`).
- Toda propuesta de índice nuevo en Azure SQL/PostGIS debe considerar el coste de
  escritura adicional, no solo el beneficio de lectura — se documenta el trade-off.

---

## 🛠 Stack Tecnológico Relevante

- Azure SQL Query Store / Execution Plans
- PostgreSQL/PostGIS: `EXPLAIN ANALYZE`, `pg_stat_statements`
- Application Insights, Azure Monitor
- .NET 8/EF Core profiling, Django Debug Toolbar / `django-silk`

---

## 💡 Ejemplos de Uso

**Ejemplo — Query N+1 en listado de buques:**
> Hallazgo: `VesselController.GetAll()` itera sobre 200 buques y para cada uno hace una
> query separada a `Berths` (N+1, EF Core sin `.Include()`).
> Impacto: 200 queries adicionales por request, P95 de 1.8s en producción (Application
> Insights, últimos 7 días).
> Ajuste: `_context.Vessels.Include(v => v.CurrentBerth).ToListAsync()`. Esfuerzo: trivial.

**Ejemplo — Falta de índice geoespacial:**
> Hallazgo: query de proximidad de atraques (`ST_DWithin`) sobre columna `geography` sin
> índice GIST, tabla con 50k registros.
> Ajuste: `CREATE INDEX idx_berths_location ON berths USING GIST (location);`. Esfuerzo:
> trivial, sin downtime (índice concurrente).

---

## 🔗 Dependencias

- `apb-ops-slo-design-v1.0` — para correlacionar con SLOs incumplidos
- `GISPEM__Guía_de_estilos.pdf` / estándar SRID 4326 — para validar uso correcto de tipos
  geoespaciales
- Consumida por: `apb-agent-tech-debt-v1.0`

---

## 📝 Notas

- Nivel 1: genera el informe y la propuesta, no aplica ningún cambio de configuración ni de
  código en producción.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

> **Generado por IA:** Claude (Anthropic), Sesión 11 del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._

---
id: "apb-dev-sql-fix-v1.0"
name: "Autocorrección y Optimización SQL"
description: "Analiza, optimiza y corrige consultas SQL/T-SQL (PostgreSQL, MySQL, MSSQL) con enfoque en performance, seguridad e inyección, aplicando el método explicativo SQL-of-Thought paso a paso."
version: "1.1.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
created_date: "2026-06-20"
review_date: "2026-06-22"
autonomy_level: 2
depends_on:
  - "apb-dev-implement-v1.0"
---

# Autocorrección y Optimización SQL

> Las secciones 5–7 (planes de ejecución, índices, migración entre motores)
> incorporan, fusionados y adaptados, contenidos de la skill de terceros
> `sanjay3290/ai-skills` (skill `postgres`) bajo licencia MIT (original
> Apache-2.0). Ver sección 9, Procedencia.

## 1. Propósito

Analizar, optimizar y corregir consultas SQL y T-SQL que presentan problemas
de rendimiento, inyección o lógica incorrecta, en PostgreSQL, MySQL, MSSQL y
SQLite. Aplica el método **SQL-of-Thought**: explicar y corregir paso a paso,
como si se razonara en voz alta.

## 2. Trigger

Una consulta SQL tiene bajo rendimiento, falla en tests, es detectada por
análisis estático (SonarQube, Query Store), o se necesita migrar entre motores.

## 3. Input / Output

**Input:** consulta SQL/T-SQL, esquema de tablas, plan de ejecución (si
disponible), volumen de datos estimado, logs de error o métricas.

**Output:** diagnóstico del problema, consulta optimizada/corregida,
explicación paso a paso (SQL-of-Thought), recomendaciones de índices,
estimación de mejora de rendimiento.

## 4. Proceso (SQL-of-Thought)

1. **Análisis sintáctico** — verificar sintaxis SQL válida.
2. **Análisis semántico** — comprender la intención de la consulta; detectar
   ambigüedades.
3. **Análisis de seguridad** — detectar inyección potencial, concatenación de
   strings (ver sección 8).
4. **Análisis de rendimiento** — joins, subconsultas, funciones en `WHERE`,
   `SELECT *` (ver sección 5).
5. **Revisión de índices** — identificar índices faltantes o no utilizados
   (ver sección 6).
6. **Optimización** — reescribir aplicando mejores prácticas.
7. **Validación** — confirmar que la consulta optimizada produce el mismo
   resultado.
8. **Documentación** — explicar cada cambio paso a paso (SQL-of-Thought),
   como si se pensara en voz alta.

## 5. Análisis de Performance

**Métricas clave en `EXPLAIN ANALYZE`:** tiempo de ejecución (objetivo
< 100ms en queries frecuentes), tiempo de planificación (< 10ms), buffer
hit ratio (> 95%), filas descartadas por filtro (indica índice faltante),
y diferencia entre filas estimadas vs. reales (> 10x indica estadísticas
desactualizadas).

| Plan | Cuándo aparece | Acción |
|---|---|---|
| Index Scan | Selectividad alta (> 5%) | Verificar índice correcto |
| Index Only Scan | Todas las columnas en índice | Ideal, mantener |
| Sequential Scan | Selectividad baja, tabla pequeña | OK si < 1000 filas |
| Nested Loop | Join con índice, tablas pequeñas | Asegurar índice en join |
| Hash Join | Join sin índice, tablas medianas | Verificar `work_mem` |

## 6. Índices: Estrategias y Anti-patrones

**Estrategias efectivas:** B-Tree para igualdad/rango/ordenación; índices
parciales para filtrar subconjuntos frecuentes; covering index incluyendo
columnas del `SELECT`; GIN para arrays/JSONB/full-text; GiST para geoespacial.

**Anti-patrones:** índices en columnas de baja cardinalidad (booleanos),
índices redundantes, índices sin mantenimiento (falta `VACUUM`/`REINDEX`),
exceso de índices (penaliza escrituras), índices en columnas hot-spot.

## 7. Patrones de Optimización Frecuentes

- **N+1 en ORM** — resolver con `select_related`/`prefetch_related` (Django) o
  equivalentes (`JOIN FETCH`, eager loading) en lugar de queries en bucle.
- **Paginación** — usar keyset/cursor pagination (`WHERE created_at < :cursor`)
  en lugar de `OFFSET` grande, que escala mal en datasets extensos.
- **Agregaciones** — usar `JOIN` + `GROUP BY` en lugar de subconsultas
  correlacionadas ejecutadas por fila; usar window functions para rankings
  y totales acumulados sin self-joins.
- **CTEs** — preferibles por legibilidad; vigilar materialización accidental
  en versiones antiguas de PostgreSQL (< 12).

## 8. Seguridad

- **NUNCA** usar concatenación de strings ni f-strings para construir queries;
  siempre parametrización (`%s`, `?`, `$1` según driver/lenguaje).
- Validar columnas dinámicas (p. ej. en `ORDER BY`) contra una whitelist
  explícita — la parametrización estándar no cubre nombres de columna.
- En ORMs, evitar SQL crudo sin parametrizar (`raw()` con f-strings); usar la
  API parametrizada nativa del ORM siempre que sea posible.
- Evitar `SELECT *`; especificar columnas necesarias.
- Preferir `JOIN`s sobre subconsultas correlacionadas; usar `EXISTS` en lugar
  de `IN` para subconsultas grandes.
- Añadir `NOLOCK`/hints de query solo como último recurso, documentado.

## 9. Migración entre Motores (referencia rápida)

| Aspecto | PostgreSQL | MySQL | SQL Server |
|---|---|---|---|
| Paginación | `LIMIT n OFFSET m` | `LIMIT m, n` | `OFFSET m ROWS FETCH NEXT n` |
| Case-insensitive | `ILIKE` | `LOWER(col) LIKE` | `LOWER(col) LIKE` |
| Valor insertado | `RETURNING id` | `LAST_INSERT_ID()` | `OUTPUT inserted.id` |
| JSON | `JSONB` | `JSON` (8.0+) | `NVARCHAR(MAX)` + funciones JSON |
| CTEs/Window funcs | Sí | Sí (8.0+) | Sí |
| Secuencias | `SERIAL`/`nextval()` | `AUTO_INCREMENT` | `SEQUENCE` (2012+) |

## 10. Checklist de Query Review

**Performance:** `EXPLAIN ANALYZE` < 100ms · índice apropiado en uso · sin
Sequential Scan en tablas grandes · N+1 resueltos · paginación por cursor ·
estadísticas actualizadas.

**Seguridad:** queries parametrizadas · sin concatenación de SQL dinámico ·
columnas de `ORDER BY` validadas contra whitelist · permisos de BD con
mínimo privilegio.

**Corrección:** `NULL` manejado explícitamente (`COALESCE`, `IS NULL`) ·
división por cero protegida (`NULLIF`) · timezones consistentes ·
transacciones en operaciones multi-tabla · race conditions consideradas
(`SELECT FOR UPDATE`).

## 11. Reglas y Constraints

- Nunca usar concatenación de strings para construir queries.
- No usar funciones sobre columnas en `WHERE` (impide uso de índices).
- Documentar hints de query solo como último recurso, con justificación.
- Para consultas complejas, generar versión simplificada para review y
  versión optimizada para producción.

## 12. Procedencia y Licencia

Las secciones 5 (análisis de performance), 6 (índices) y 9 (migración entre
motores) están adaptadas de la skill `postgres` de `sanjay3290/ai-skills`
(licencia MIT, original Apache-2.0).

## 13. Dependencias

- `apb-dev-implement-v1.0`


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **SQL generado** — primera línea: `-- [IA-GEN] Generado por APB AI Framework (apb-dev-sql-fix-v1.0) — pendiente revisión humana`
- **Commit** — prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** — label `ai-generated` en GitHub + footer en descripción del PR

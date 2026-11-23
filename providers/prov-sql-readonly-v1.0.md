---
id: "prov-sql-readonly-v1.0"
name: "Provider: Consulta SQL de Solo Lectura (BuiltInTool de Mother)"
description: "Proveedor de acción para comparar datos entre origen y destino en una validación post-migración, limitado a un conjunto fijo de operaciones de solo lectura (conteo, checksum, muestreo) — nunca SQL libre compuesto por el agente."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-only"
created_date: "2026-11-23"
review_date: "2026-11-23"
---

# Provider: Consulta SQL de Solo Lectura (BuiltInTool de Mother)

---

## Descripción

Permite a un agente de validación post-migración comparar volúmenes y contenido entre una
tabla origen y destino sin que el agente llegue a escribir ni ejecutar una sola línea de
SQL. Expone únicamente tres operaciones predefinidas y parametrizadas (nunca una consulta
libre), resueltas contra una conexión identificada **por nombre** de configuración — el
agente nunca ve ni compone una connection string.

## Capacidades

| Acción | Descripción | Gate humano |
|--------|-------------|--------------|
| `row_count` | Devuelve `COUNT(*)` de una tabla permitida | No |
| `checksum_table` | Devuelve un checksum agregado (p. ej. `CHECKSUM_AGG`/`MD5` por fila) de una tabla permitida | No |
| `sample_rows` | Devuelve hasta N filas de muestra (N acotado, p. ej. máx. 100) de una tabla permitida | No |

Todas de solo lectura — ninguna admite `INSERT`/`UPDATE`/`DELETE`/DDL ni SQL arbitrario.

## Mecanismo real

**No es un servidor MCP** — es un `BuiltInTool` de Mother que reutiliza el acceso a datos
ya existente en `Core.Persistence`. La conexión se resuelve por un **nombre lógico**
configurado en Mother (p. ej. `"migracion-origen"`, `"migracion-destino"`), nunca por una
cadena que el agente aporte; y la tabla debe estar en una lista blanca explícita por
ejecución (definida al lanzar la validación, no inventada por el agente). Cada operación
se ejecuta en una transacción de solo lectura.

## Configuración

```json
{
  "provider_id": "prov-sql-readonly-v1.0",
  "type": "action",
  "mechanism": "builtin_tool",
  "builtin_tool_name": "sql-readonly",
  "connection_names": ["<resueltas en Mother, nunca en el prompt del agente>"],
  "allowed_tables_per_run": "<lista blanca definida al lanzar la ejecución>",
  "max_sample_rows": 100,
  "permissions": ["read"]
}
```

## Inputs

- `connection_name`: nombre lógico de conexión (de la lista configurada).
- `table`: nombre de tabla (debe estar en la lista blanca de la ejecución).
- `n` (solo `sample_rows`): número de filas, acotado a `max_sample_rows`.

## Outputs

- `row_count` → `{ table, count }`
- `checksum_table` → `{ table, checksum, algorithm }`
- `sample_rows` → `{ table, rows: [...] }`

## Dependencias

- `apb-qa-post-migration-v1.0` (validación de datos: "comparar volúmenes, checksums,
  muestras representativas")

## Restricciones

- **Nunca** ejecuta SQL compuesto por el agente — solo las tres operaciones fijas de
  arriba, parametrizadas.
- **Nunca** apunta a producción sin una confirmación explícita y separada del usuario al
  configurar la ejecución; por defecto solo entornos de desarrollo/staging.
- La lista de tablas permitidas y de conexiones se define en configuración de Mother, no
  la decide el agente en tiempo de ejecución.
- No sustituye una validación de integridad referencial completa (FKs, constraints) — eso
  sigue siendo trabajo de la skill con las métricas que esta tool le da.

## Ejemplo de Uso

```
Invocar: prov-sql-readonly-v1.0
Action: checksum_table
ConnectionName: "migracion-destino"
Table: "clientes"
→ { table: "clientes", checksum: "a1b2c3...", algorithm: "CHECKSUM_AGG" }
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-11-23 | Claude (Anthropic), a petición de Débora | Creación: `apb-qa-post-migration-v1.0` declaraba la necesidad de "consultas a base de datos" sin tener ningún provider que la cubriera |

---
*Registrado en APB AI Framework.*

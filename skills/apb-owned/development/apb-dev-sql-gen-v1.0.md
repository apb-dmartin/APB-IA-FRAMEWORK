---
id: "apb-dev-sql-gen-v1.0"
name: "Generación SQL"
description: "Genera consultas SQL correctas, eficientes y seguras a partir de una descripción en lenguaje natural. Compatible con Oracle SQL, T-SQL (SQL Server) y PostgreSQL. Aplica convenciones de nomenclatura APB y buenas prácticas de rendimiento desde el primer draft."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 2
consumed_by:
  - "apb-agent-db-v1.0"
  - "apb-agent-implementer-v1.0"
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Generación SQL

---

## 🎯 Propósito

Traducir una necesidad de datos descrita en lenguaje natural a una consulta SQL ejecutable, correcta y optimizada para el motor de base de datos APB (principalmente Oracle, también SQL Server). Incluye documentación inline de la query y estimación del impacto de rendimiento. Nunca genera SQL que pueda modificar o eliminar datos sin confirmación explícita.

---

## ⚡ Trigger

Cuando un analista, desarrollador o técnico necesita obtener datos de una base de datos APB y no conoce la sintaxis exacta, o necesita una query compleja que combina múltiples tablas, agregaciones o lógica de negocio.

---

## 📥 Input

- Descripción de la necesidad en lenguaje natural ("quiero saber las concesiones activas por muelle en el último trimestre")
- Motor de base de datos (Oracle / SQL Server / PostgreSQL)
- Esquema o tablas relevantes (nombres, si se conocen)
- Condiciones de filtrado o agrupación requeridas
- Formato de salida esperado (lista, agregado, pivot, etc.)
- Contexto de uso (informe, API, migración, soporte a incidencia)

---

## 📤 Output

- **Query SQL:** lista para ejecutar, con comentarios inline explicando cada sección
- **Explicación:** qué hace la query en lenguaje natural
- **Estimación de impacto:** si la query puede ser costosa (full scan, sin índice, muchas filas)
- **Alternativas:** si existe una versión más eficiente o más simple según el caso
- **Advertencias de seguridad:** si la query accede a datos sensibles (datos personales, financieros)

---

## 🔄 Proceso

1. **Comprensión de la necesidad:** identificar entidades, relaciones, filtros y formato de salida
2. **Identificación del motor:** adaptar sintaxis a Oracle / T-SQL / PostgreSQL
3. **Construcción de la query:**
   - Usar CTEs (`WITH`) para queries complejas en lugar de subqueries anidadas
   - Preferir JOINs explícitos (`INNER JOIN`, `LEFT JOIN`) sobre implícitos
   - Aplicar alias claros y descriptivos en tablas y columnas
   - Añadir comentarios en secciones complejas (`-- Filtra concesiones activas`)
4. **Revisión de seguridad:** detectar acceso a columnas con datos personales o financieros
5. **Estimación de rendimiento:** identificar operaciones costosas y proponer índices si faltan
6. **Documentación de la query:** encabezado con propósito, autor, fecha y motor

### Plantilla de encabezado de query

```sql
-- ============================================================
-- Propósito : [Descripción de lo que hace la query]
-- Motor     : Oracle 19c / SQL Server / PostgreSQL
-- Autor     : [Nombre] — APB AI Framework
-- Fecha     : [YYYY-MM-DD]
-- Notas     : [Condiciones especiales, tablas críticas, etc.]
-- ============================================================
```

---

## 📋 Reglas y Constraints

- NUNCA generar `DELETE`, `DROP`, `TRUNCATE` o `UPDATE` sin que el usuario lo solicite explícitamente y con un comentario de advertencia visible
- Las queries con `DELETE` o `UPDATE` siempre incluyen primero el `SELECT` equivalente para que el usuario valide los registros afectados
- Si la query accede a tablas con datos personales (RGPD), añadir advertencia visible al principio del output
- No usar `SELECT *` — siempre listar columnas explícitamente
- Para Oracle: usar `ROWNUM` o `FETCH FIRST N ROWS ONLY` para limitar resultados en pruebas
- Autonomía nivel 2: la query es una propuesta — el usuario la revisa y ejecuta, el agente no ejecuta directamente sobre la BD

---

## 🛠 Stack Tecnológico Relevante

- Oracle Database 19c / 21c (motor principal APB)
- Microsoft SQL Server 2019
- PostgreSQL 14+
- Oracle SQL Developer, DBeaver (IDEs de referencia)
- Jira (vinculación si la query apoya una incidencia o tarea)

---

## 💡 Ejemplos de Uso

**Ejemplo — Query de negocio:**
> "Quiero las concesiones de tipo amarres que vencen en los próximos 60 días, con el nombre del concesionario y el muelle asignado."

```sql
-- ============================================================
-- Propósito : Concesiones de amarres próximas a vencer (60 días)
-- Motor     : Oracle 19c
-- Autor     : APB AI Framework — Sesión 21
-- Fecha     : 2026-06-26
-- ============================================================
SELECT
    c.id_concesion,
    c.num_expediente,
    p.nombre_concesionario,
    m.nombre_muelle,
    c.fecha_fin,
    TRUNC(c.fecha_fin - SYSDATE) AS dias_restantes
FROM
    concesiones c
    INNER JOIN personas p ON c.id_persona = p.id_persona
    INNER JOIN muelles m ON c.id_muelle = m.id_muelle
WHERE
    c.tipo_concesion = 'AMARRE'
    AND c.estado = 'ACTIVA'
    AND c.fecha_fin BETWEEN SYSDATE AND SYSDATE + 60
ORDER BY
    c.fecha_fin ASC;
-- Impacto estimado: bajo (filtro por índice en fecha_fin si existe)
```

**Ejemplo — Query de soporte a incidencia:**
> "Buscar sesiones bloqueadas en Oracle para la incidencia INC-2847."

```sql
-- Sesiones bloqueantes y bloqueadas — diagnóstico de locks Oracle
SELECT
    blocker.sid          AS sid_bloqueante,
    blocker.serial#      AS serial_bloqueante,
    blocker.username     AS usuario_bloqueante,
    blocked.sid          AS sid_bloqueada,
    blocked.username     AS usuario_bloqueado,
    blocked.sql_id       AS sql_bloqueado,
    blocked.wait_class   AS tipo_espera,
    blocked.seconds_in_wait AS segundos_esperando
FROM
    v$session blocker
    INNER JOIN v$session blocked ON blocker.sid = blocked.blocking_session
WHERE
    blocked.blocking_session IS NOT NULL
ORDER BY
    blocked.seconds_in_wait DESC;
-- ⚠️ Requiere privilegios DBA para acceder a v$session
```

---

## 🔗 Dependencias

- `apb-dev-sql-review-v1.0` — revisión y optimización de la query generada
- `apb-ops-incident-diagnose-v1.0` — puede invocar esta skill para queries de diagnóstico BD

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Descripción de la necesidad en lenguaje natural` | Pregunta: "¿Puedes proporcionar descripción de la necesidad en lenguaje natural?" | Sí |
| `Motor de base de datos` | Pregunta: "¿Puedes proporcionar motor de base de datos?" | Sí |
| `Esquema o tablas relevantes` | Pregunta: "¿Puedes proporcionar esquema o tablas relevantes?" | Sí |
| `Condiciones de filtrado o agrupación requeridas` | Pregunta: "¿Puedes proporcionar condiciones de filtrado o agrupación requeridas?" | Sí |
| `Formato de salida esperado` | Pregunta: "¿Puedes proporcionar formato de salida esperado?" | Sí |
| `Contexto de uso` | Pregunta: "¿Puedes proporcionar contexto de uso?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **SQL generado** — primera línea: `-- [IA-GEN] Generado por APB AI Framework (apb-dev-sql-gen-v1.0) — pendiente revisión humana`
- **Commit** — prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** — label `ai-generated` en GitHub + footer en descripción del PR

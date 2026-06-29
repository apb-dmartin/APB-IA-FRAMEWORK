---
id: "apb-dev-sql-review-v1.0"
name: "Revisión y Optimización SQL"
description: "Revisa una query SQL existente e identifica problemas de corrección, rendimiento, seguridad y mantenibilidad. Propone una versión optimizada con explicación de cada mejora. Compatible con Oracle SQL, T-SQL y PostgreSQL."
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

# Revisión y Optimización SQL

---

## 🎯 Propósito

Analizar una query SQL aportada por el usuario e identificar problemas en cuatro dimensiones: corrección (¿devuelve lo que debe?), rendimiento (¿es eficiente?), seguridad (¿expone datos sensibles o permite inyección?) y mantenibilidad (¿es legible y documentada?). Produce un informe de revisión y una versión optimizada lista para usar.

---

## ⚡ Trigger

Cuando un desarrollador o analista APB tiene una query SQL escrita y quiere validarla antes de ejecutarla en producción, o cuando una query lenta está causando una incidencia de rendimiento.

---

## 📥 Input

- Query SQL a revisar (texto completo)
- Motor de base de datos (Oracle / SQL Server / PostgreSQL)
- Contexto de uso (informe batch, API en tiempo real, soporte a incidencia, migración)
- Plan de ejecución (EXPLAIN PLAN) si está disponible
- Tablas involucradas y volumen aproximado de filas (si se conoce)

---

## 📤 Output

- **Informe de revisión:** hallazgos clasificados por severidad (Crítico / Alto / Medio / Bajo / Sugerencia)
- **Query optimizada:** versión mejorada con comentarios explicando cada cambio
- **Resumen de mejoras:** tabla comparativa antes/después
- **Estimación de impacto de rendimiento:** si aplica (full scan eliminado, índice recomendado, etc.)

---

## 🔄 Proceso

1. **Análisis de corrección:**
   - Verificar que la lógica de JOINs es correcta (ON conditions, tipo de JOIN)
   - Detectar condiciones de filtrado que puedan excluir filas inesperadamente (NULL handling)
   - Verificar agrupaciones (GROUP BY coherente con SELECT)
   - Detectar uso de funciones en columnas indexadas que anulan el índice

2. **Análisis de rendimiento:**

| Anti-patrón | Impacto | Solución |
|-------------|---------|----------|
| `SELECT *` | Alto — trae columnas innecesarias | Listar columnas explícitamente |
| Función en columna indexada (`UPPER(nombre)`) | Alto — descarta índice | Índice funcional o cambiar lógica |
| Subquery correlacionada en `WHERE` | Alto — N+1 | Reescribir como JOIN |
| `DISTINCT` innecesario | Medio — sort extra | Revisar lógica de duplicados |
| `NOT IN` con subquery | Medio — mal rendimiento con NULLs | Reescribir con `NOT EXISTS` |
| Sin `WHERE` en tablas grandes | Crítico — full scan | Añadir filtro o limitar con ROWNUM |
| Cursor implícito en PL/SQL | Alto | Reescribir como operación en set |

3. **Análisis de seguridad:**
   - Detectar concatenación de strings que pueda derivar en SQL injection
   - Identificar acceso a columnas con datos personales (nombre, DNI, email, teléfono) — marcar para revisión RGPD
   - Verificar que no hay credenciales hardcodeadas en la query

4. **Análisis de mantenibilidad:**
   - ¿Tiene encabezado con propósito, fecha y autor?
   - ¿Los alias son descriptivos?
   - ¿Las CTEs mejoran la legibilidad respecto a subqueries anidadas?

5. **Generación de la query optimizada** con comentarios inline de cada mejora

---

## 📋 Reglas y Constraints

- Los hallazgos de severidad Crítico y Alto deben resolverse antes de ejecutar la query en producción
- Los hallazgos de seguridad relacionados con datos personales se comunican siempre, independientemente de su severidad de rendimiento
- La versión optimizada no cambia la lógica de negocio — solo mejora la implementación
- Si la lógica parece incorrecta (la query no devolvería lo esperado), se señala como Crítico con propuesta alternativa pero sin asumir la intención del usuario
- Autonomía nivel 2: la revisión es una recomendación — el usuario decide si aplica los cambios

---

## 🛠 Stack Tecnológico Relevante

- Oracle Database 19c / 21c (EXPLAIN PLAN, v$sql, AWR)
- Microsoft SQL Server (Execution Plan, sys.dm_exec_query_stats)
- PostgreSQL (EXPLAIN ANALYZE)
- Oracle SQL Developer, DBeaver

---

## 💡 Ejemplos de Uso

**Ejemplo — Query con anti-patrones:**

Original:
```sql
SELECT * FROM CONCESIONES WHERE UPPER(ESTADO) = 'ACTIVA'
```

Hallazgos:
- Alto: `SELECT *` — trae todas las columnas
- Alto: `UPPER(ESTADO)` en columna indexada anula el índice

Optimizada:
```sql
SELECT
    id_concesion,
    num_expediente,
    estado,
    fecha_fin
FROM concesiones
WHERE estado = 'ACTIVA'  -- Columna almacenada en mayúsculas según DDICT; índice funcional aprovechado
```

---

## 🔗 Dependencias

- `apb-dev-sql-gen-v1.0` — puede aportarle queries para revisión
- `apb-ops-incident-diagnose-v1.0` — puede invocarla si una query lenta causa la incidencia

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Query SQL a revisar` | Pregunta: "¿Puedes proporcionar query sql a revisar?" | Sí |
| `Motor de base de datos` | Pregunta: "¿Puedes proporcionar motor de base de datos?" | Sí |
| `Contexto de uso` | Pregunta: "¿Puedes proporcionar contexto de uso?" | Sí |
| `Plan de ejecución  si está disponible` | Pregunta: "¿Puedes proporcionar plan de ejecución  si está disponible?" | Sí |
| `Tablas involucradas y volumen aproximado de filas` | Continúa con la información disponible — indica qué asumió | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **SQL generado** - primera linea: `-- [IA-GEN] Generado por APB AI Framework (apb-dev-sql-review-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub

---
id: "third-neondatabase-db-migration-v1.0"
name: "Database Migration Patterns"
description: "Patrones de migración de bases de datos basados en Neon Postgres."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/neondatabase/neon-postgres"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Migración de Base de Datos para APB

## Overview
Migración de esquemas y datos entre bases de datos (Azure SQL, PostgreSQL, Oracle) con mínimo downtime, integridad garantizada y plan de rollback. Incluye migración de datos históricos, transformación de esquemas y validación post-migración.

## When to Use
- Cambio de motor de base de datos (Oracle → Azure SQL, on-prem → cloud)
- Actualización de esquema con breaking changes
- Migración de datos históricos a nuevo sistema
- Shard/reparticionamiento de datos
- Consolidación de bases de datos

## Core Pattern

### Fase 1: Análisis Pre-Migración
1. Inventario de objetos: tablas, índices, vistas, SPs, triggers, funciones
2. Análisis de dependencias: qué aplicaciones usan qué objetos
3. Estimación de tamaño y tiempo de migración
4. Identificación de datos sensibles (LOPDGDD)
5. Definición de ventana de mantenimiento

### Fase 2: Diseño de Migración

| Estrategia | Cuándo usar | Downtime |
|-----------|-------------|----------|
| **Big Bang** | Datos < 100GB, downtime aceptable | Horas |
| **Incremental** | Datos grandes, cambios graduales | Minutos |
| **Dual Write** | Zero downtime, alta disponibilidad | Ninguno |
| **ETL** | Transformación compleja de datos | Variable |

### Fase 3: Ejecución

```sql
-- Ejemplo: Migración Azure SQL con minimización de bloqueos
BEGIN TRANSACTION;

-- 1. Crear tabla nueva con esquema actualizado
CREATE TABLE Expedientes_v2 (...);

-- 2. Migrar datos en batches
DECLARE @BatchSize INT = 10000;
DECLARE @Offset INT = 0;

WHILE (1=1)
BEGIN
    INSERT INTO Expedientes_v2 (...)
    SELECT ... FROM Expedientes
    ORDER BY Id
    OFFSET @Offset ROWS FETCH NEXT @BatchSize ROWS ONLY;

    SET @Offset += @BatchSize;

    IF @@ROWCOUNT < @BatchSize BREAK;

    -- Checkpoint para reducir log growth
    CHECKPOINT;
    WAITFOR DELAY '00:00:01'; -- Reducir presión
END;

-- 3. Validación de conteo y checksum
-- 4. Renombrar tablas (metadata operation, rápido)
EXEC sp_rename 'Expedientes', 'Expedientes_old';
EXEC sp_rename 'Expedientes_v2', 'Expedientes';

-- 5. Recrear índices, constraints, triggers
COMMIT;
```

### Fase 4: Validación
- Conteo de registros origen vs destino
- Checksum de datos clave
- Validación de integridad referencial
- Pruebas de aplicación contra nuevo esquema

### Fase 5: Rollback Plan
```sql
-- Si falla, rollback en segundos
BEGIN TRANSACTION;
EXEC sp_rename 'Expedientes', 'Expedientes_failed';
EXEC sp_rename 'Expedientes_old', 'Expedientes';
COMMIT;
```

## Quick Reference

| Problema | Solución |
|----------|----------|
| Migración muy lenta | Batches, paralelización, deshabilitar índices temporalmente |
| Bloqueos | READ COMMITTED SNAPSHOT, batches pequeños, horario bajo |
| Datos corruptos | Checksums, validación por batches, rollback inmediato |
| Dependencias rotas | Inventario completo, orden de migración, pruebas integrales |

## Adapted From
- **Source:** neondatabase/neon-postgres (database patterns)
- **License:** MIT
- **Attribution:** Patrones de migración de datos y minimización de downtime inspirados en Neon Database. Reescrito para Azure SQL, PostgreSQL y stack APB.

## References
- Microsoft Database Migration Guide
- PostgreSQL pg_dump / pg_restore
- context/apb/standards/database-standards.md

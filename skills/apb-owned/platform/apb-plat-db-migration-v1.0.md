---
id: "apb-plat-db-migration-v1.0"
name: "Migración de Base de Datos"
description: "Asistir en la planificación, diseño y validación de migraciones de bases de datos (schema y datos) en entornos corporativos. Genera scripts de migración, planes de rollback, checklists de validación y documentación de procedimientos para migraciones seguras y reversibles."
version: "1.0.0"
status: "draft"
owner: "DevOps / DBA APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Migración de Base de Datos


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Asistir en la planificación, diseño y validación de migraciones de bases de datos (schema y datos) en entornos corporativos. Genera scripts de migración, planes de rollback, checklists de validación y documentación de procedimientos para migraciones seguras y reversibles.

## Contexto de Uso
- Migración de schemas entre versiones de aplicación (evolutionary database design).
- Migración de datos entre sistemas (ETL, sincronización, consolidación).
- Modernización de base de datos (on-prem → Azure SQL, SQL Server → PostgreSQL).
- Integración con pipelines CI/CD para migraciones automatizadas.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `source_db` | Texto | Tipo y versión de BD origen (SQL Server 2019, PostgreSQL 15, etc.) | ✅ |
| `target_db` | Texto | Tipo y versión de BD destino | ✅ |
| `migration_type` | Enum | `schema`, `data`, `schema+data`, `platform` (cambio de motor) | ✅ |
| `schema_diff` | Texto / Script | Diferencias de schema (forward/reverse engineering) | ❌ |
| `data_volume` | Texto | Volumen estimado de datos (filas, GB, tablas) | ❌ |
| `downtime_tolerance` | Enum | `zero-downtime`, `scheduled-window`, `extended` | ✅ |
| `rollback_required` | Boolean | ¿Se requiere plan de rollback completo? | ❌ (default: true) |

## Flujo de Trabajo (Pasos)
1. **Análisis de origen y destino**: Comparar capacidades, tipos de datos, constraints, índices y features entre motores.
2. **Diseño de estrategia de migración**:
   - **Schema migration**: Scripts DDL ordenados (create, alter, drop) con manejo de dependencias.
   - **Data migration**: Scripts DML, bulk copy, o herramientas de replicación según volumen.
   - **Platform migration**: Estrategia de transformación de tipos, stored procedures, funciones.
3. **Gestión de downtime**:
   - **Zero-downtime**: Blue-green, feature flags, dual-write, CDC (Change Data Capture).
   - **Scheduled window**: Plan de migración con ventana de mantenimiento.
   - **Extended**: Migración gradual por módulos o tablas.
4. **Generación de scripts**: Crear scripts de migración idempotentes y versionados.
5. **Plan de rollback**: Para cada script de migración, generar script de rollback inverso.
6. **Validación post-migración**: Checklist de verificación (row counts, constraints, índices, performance).
7. **Documentación de procedimiento**: Guía paso a paso con responsables, tiempos estimados y puntos de no retorno.
8. **Registro de evidencia**: Metadatos para gobierno y auditoría.

## Salida Esperada
### Archivos Generados
```
db-migration/
├── migration-plan.md
├── scripts/
│   ├── V001__initial_schema.sql
│   ├── V002__add_indexes.sql
│   └── V003__migrate_data.sql
├── rollback/
│   ├── R001__rollback_initial_schema.sql
│   ├── R002__rollback_add_indexes.sql
│   └── R003__rollback_migrate_data.sql
├── validation/
│   └── post-migration-checklist.md
└── README-migration.md
```

### Estructura del Plan
```markdown
# Plan de Migración de Base de Datos — [Origen] → [Destino]
> Tipo: [schema/data/platform] | Estrategia: [zero-downtime/scheduled] | Fecha: [YYYY-MM-DD]

## 1. Alcance y Contexto
## 2. Análisis de Compatibilidad
## 3. Estrategia de Migración
## 4. Scripts de Migración
## 5. Plan de Rollback
## 6. Validación Post-Migración
## 7. Timeline y Responsables
## 8. Riesgos y Mitigaciones
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los scripts de migración son idempotentes (re-ejecutables sin error).
- [ ] Cada script de migración tiene su correspondiente script de rollback.
- [ ] Plan de rollback validado en entorno de pre-producción.
- [ ] Checklist de validación post-migración con métricas cuantificables.
- [ ] No hay pérdida de datos en el diseño de migración (verificación de integridad).
- [ ] Estrategia de downtime alineada con SLA del sistema.
- [ ] Documentación revisable por DBA y equipo de operaciones sin intervención del agente.

## Stack y Tecnologías
- Motores: SQL Server, Azure SQL, PostgreSQL, PostGIS
- Migración: Entity Framework Migrations, Flyway, Liquibase, Azure Database Migration Service
- ETL: Azure Data Factory, SSIS, custom scripts
- Replicación: CDC, transactional replication, logical replication (PostgreSQL)
- Validación: DBCC, pg_dump/pg_restore, row count validation, checksum

## Dependencias
- `apb-qa-post-migration-v1.0` — para validación post-migración
- `apb-plat-cicd-v1.0` — para integración de migraciones en pipeline
- `apb-gov-evidence-v1.0` — para generación de evidencia

## Ejemplo de Uso
**Prompt de invocación:**
```
Planifica la migración de nuestro schema de SQL Server 2019 a Azure SQL:
- Aplicación: sistema de gestión de expedientes (Entity Framework Core 8)
- Tablas: 45 tablas, ~2M filas, 120GB
- Downtime: ventana de mantenimiento de 4 horas (sábado 02:00-06:00)
- Requisitos: rollback completo, validación de integridad, índices optimizados
- Features usadas: Full-Text Search, spatial data (migrar a PostGIS si aplica)
```

## Notas y Advertencias
- **Nivel 1**: El agente diseña y genera scripts; no ejecuta migraciones en entornos productivos.
- **Revisión humana obligatoria** por DBA y arquitecto de datos antes de ejecutar cualquier script.
- Las migraciones en producción requieren backup completo y validado previamente.
- Los scripts de rollback deben probarse en pre-producción antes de la migración real.
- El agente no tiene acceso a bases de datos reales; trabaja con descripciones y schemas proporcionados.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Primera linea del fichero generado**: `# [IA-GEN] Generado por APB AI Framework (apb-plat-db-migration-v1.0) - revisar ANTES de aplicar en produccion`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`

NOTA: Para IaC, ningun fichero generado por IA debe aplicarse en produccion sin revision humana explicita.

---
id: "third-garrytan-post-deploy-validation-v1.0"
name: "Post-Deploy Validation (Canary)"
description: "Validación post-despliegue tipo canary release, adaptada de gstack /canary."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/garrytan/gstack"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Validación Post-Migración para APB

## Overview
Validación sistemática tras migración de sistemas, bases de datos o infraestructura en la APB. Verifica integridad de datos, equivalencia funcional, rendimiento comparativo y cumplimiento de requisitos no funcionales antes de la puesta en producción definitiva.

## When to Use
- Migración de base de datos (Oracle → Azure SQL, on-prem → cloud)
- Migración de aplicación (monolito → microservicios)
- Migración de infraestructura (on-prem → Azure)
- Actualización de versión de framework (.NET Framework → .NET 8)
- Migración de datos históricos

**When NOT to use:**
- Despliegue rutinario sin cambio de plataforma (usar smoke tests)
- Cambio menor de configuración (usar pruebas de regresión)
- Rollback de emergencia (usar procedimiento de rollback)

## Core Pattern

### Fase 1: Preparación
1. **Definir alcance:** ¿Qué se migra? ¿Qué queda fuera?
2. **Establecer baseline:** Métricas de rendimiento y funcionalidad pre-migración
3. **Identificar riesgos:** ¿Qué puede fallar? ¿Qué es irreversible?
4. **Preparar entorno de validación:** Réplica de producción con datos migrados
5. **Definir criterios de éxito:** ¿Cuándo la migración es exitosa?

### Fase 2: Validación de Datos

#### Integridad
| Verificación | Método | Umbral Aceptable |
|-------------|--------|-----------------|
| Conteo de registros | SELECT COUNT(*) origen vs destino | 100% coincidencia |
| Suma de control (checksum) | Hash agregado de campos clave | 100% coincidencia |
| Rango de valores | MIN/MAX/AVG por campo numérico | Diferencia < 0.01% |
| Valores nulos | COUNT NULL por campo | Mismo porcentaje ± 0.1% |
| Relaciones foráneas | Validar integridad referencial | 0 violaciones |

#### Muestreo
- Para tablas > 1M registros: muestreo aleatorio del 1%
- Para tablas críticas: validación 100%
- Comparar campo a campo para muestra seleccionada

### Fase 3: Validación Funcional

#### Equivalencia
| Área | Verificación | Método |
|------|-------------|--------|
| **APIs** | Respuestas idénticas para mismas peticiones | Diff de JSON |
| **UI** | Comportamiento idéntico para mismas acciones | E2E tests |
| **Reportes** | Resultados numéricos idénticos | Comparación automatizada |
| **Procesos batch** | Mismos outputs para mismos inputs | Ejecución paralela |
| **Notificaciones** | Mismos destinatarios y contenido | Mock + verificación |

#### Regresión
- Ejecutar suite de regresión completa
- Comparar resultados con baseline pre-migración
- Documentar diferencias (esperadas vs inesperadas)

### Fase 4: Validación de Rendimiento

| Métrica | Baseline Pre | Objetivo Post | Tolerancia |
|---------|-------------|---------------|------------|
| Tiempo respuesta p95 | [valor] | ≤ baseline | +10% máximo |
| Throughput | [valor] | ≥ baseline | -5% mínimo |
| Uso CPU | [valor] | ≤ baseline + 20% | — |
| Uso memoria | [valor] | ≤ baseline + 20% | — |
| Latencia BD | [valor] | ≤ baseline + 15% | — |

### Fase 5: Validación de Seguridad
- Verificar que permisos y roles se migraron correctamente
- Validar que no se introdujeron configuraciones inseguras
- Confirmar que secretos se gestionan correctamente (Azure Key Vault)
- Revisar que logs de auditoría se mantienen

### Fase 6: Validación de Operaciones
- Verificar que monitoreo funciona (Application Insights, dashboards)
- Confirmar que alertas se generan correctamente
- Validar que runbooks aplican al nuevo entorno
- Verificar procedimientos de backup/recovery

### Fase 7: Generación de Informe

```markdown
# Informe de Validación Post-Migración — [Sistema]

## Resumen
- Sistema: [nombre]
- Tipo de migración: [tipo]
- Fecha inicio: [fecha]
- Fecha fin: [fecha]

## Validación de Datos
| Tabla | Registros Origen | Registros Destino | Checksum | Estado |
|-------|-----------------|-------------------|----------|--------|
| [tabla] | [n] | [n] | [match] | ✓ |

## Validación Funcional
| Área | Tests Ejecutados | Tests Pasados | Estado |
|------|-----------------|---------------|--------|
| APIs | [n] | [n] | ✓/✗ |
| UI | [n] | [n] | ✓/✗ |
| Batch | [n] | [n] | ✓/✗ |

## Validación de Rendimiento
| Métrica | Pre | Post | Diferencia | Estado |
|---------|-----|------|------------|--------|
| p95 | [v] | [v] | [±%] | ✓/✗ |

## Estado Global
- APROBADO / APROBADO_CONDICIONAL / RECHAZADO
- Condiciones: [si aplica]
- Aprobador: [nombre]
```

## Quick Reference

| Problema | Acción |
|----------|--------|
| Discrepancia en conteo de registros | Investigar filtros de migración, registros eliminados lógicamente |
| Diferencia en checksum | Comparar registro a registro para identificar campo problemático |
| Degradación de rendimiento | Revisar índices, configuración de conexión, plan de ejecución |
| Test de regresión fallido | Determinar si es bug de migración o cambio esperado |
| Datos corruptos | STOP migración, restaurar backup, investigar causa |

## Implementation

### Checklist Post-Migración
```
□ Datos: conteo, checksum, muestreo validado
□ Funcionalidad: APIs, UI, batch, reportes verificados
□ Rendimiento: baseline comparado, dentro de tolerancia
□ Seguridad: permisos, secretos, logs verificados
□ Operaciones: monitoreo, alertas, backups verificados
□ Rollback plan documentado y probado
□ Informe de validación generado y aprobado
```

## Common Mistakes
- **No establecer baseline:** Sin baseline no se puede medir éxito
- **Validar solo conteo de registros:** El conteo puede coincidir pero los datos pueden estar corruptos
- **Ignorar rendimiento:** La funcionalidad puede ser equivalente pero 10x más lenta
- **No probar rollback:** Si la migración falla en producción, necesitas plan de vuelta atrás
- **Validar con datos de prueba:** Usar datos de producción anonimizados para validación realista
- **No documentar discrepancias esperadas:** Algunas diferencias son intencionales (mejoras)

## Real-World Impact
- Reducción de 80% en incidentes post-migración
- Detección temprana de corrupción de datos
- Confianza en proceso de migración para stakeholders

---

## Adapted From
- **Source:** garrytan/gstack — skill `/canary` (post-deploy validation)
- **License:** MIT
- **Attribution:** Patrón de validación post-cambio y monitoreo de salud inspirados en gstack /canary. Reescrito completamente para contexto de migraciones de sistemas legacy en sector público español.

## References
- ISTQB — Advanced Level Test Manager
- Microsoft Azure Migration Best Practices
- context/apb/standards/migration-standards.md

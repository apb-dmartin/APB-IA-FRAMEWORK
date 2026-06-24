---
id: "apb-dev-impact-analysis-v1.0"
name: "Impact Analysis"
description: "Analiza el impacto de un cambio propuesto en el codebase, identificando dependencias downstream, riesgos de regresion y superficie de afectacion antes de la implementacion."
version: "1.0.0"
status: "draft"
owner: "Desarrollo APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

> Inspirado en: mattpocock/codebase-architecture-analysis (licencia MIT).

# Impact Analysis

## Purpose
Analiza el impacto de un cambio propuesto en el codebase, identificando dependencias downstream, riesgos de regresion y superficie de afectacion antes de la implementacion.

## Trigger
- Antes de modificar codigo compartido (librerias core, utilidades)
- Antes de cambiar contratos de API (breaking changes)
- Antes de refactor que toca multiples modulos
- Durante code review de cambios grandes

## Input
- Cambio propuesto (diff, descripcion, ticket)
- Grafo de dependencias del proyecto (o capacidad de generarlo)
- Tests existentes y su cobertura por area

## Output
- Mapa de impacto con componentes afectados
- Riesgo de regresion por area (Alto/Medio/Bajo)
- Lista de tests que deben pasar
- Recomendacion: seguro / con precaucion / no recomendado

## Procedure

### Step 1: Identificar el Cambio
- Scope: Que archivos/metodos cambian?
- Tipo: Bugfix, feature, refactor, breaking change
- Motivacion: Por que es necesario?

### Step 2: Traer Dependencias
Usar analisis estatico o grafo de conocimiento:
- Upstream: Que depende del codigo que cambio? (consumidores)
- Downstream: De que depende el codigo nuevo? (dependencias)
- Transversales: Que configuracion, schemas, contratos se ven afectados?

### Step 3: Evaluar Riesgo
Por cada componente afectado:
- Frecuencia de uso: Cuan critico es este path?
- Test coverage: Esta cubierto por tests?
- Complejidad: Cuantas ramas/condiciones tiene?
- Historial: Ha tenido bugs recientes?

Score de riesgo:
- ALTO: Componente core, baja cobertura, alta frecuencia
- MEDIO: Componente importante, cobertura media
- BAJO: Componente periferico, alta cobertura

### Step 4: Plan de Mitigacion
- Tests adicionales necesarios
- Estrategia de rollout (feature flag, canary, blue-green)
- Plan de rollback
- Comunicacion a equipos afectados

## Rules
- Si el riesgo es Alto, requiere approval de tech lead + tests e2e
- Nunca hacer breaking change sin periodo de deprecacion
- Documentar el analisis en el PR, no solo en la cabeza
- Si no puedes trazar el impacto, el cambio es demasiado grande

## Examples

### Example 1: Cambio en Libreria Core
Cambio: Modificar DateTimeUtils.ToIsoString() para incluir timezone

Impacto:
- Afectados: 14 call sites en 6 proyectos
- Riesgo: MEDIO (metodo usado frecuentemente, tests existentes)
- Downstream: APIs que serializan fechas, reportes exportados
- Transversales: Contrato de API v2 (cambio de formato)

Mitigacion:
- Agregar overload en lugar de modificar existente
- Tests de contrato para todas las APIs afectadas
- Feature flag para nuevo formato
- Comunicar a equipo de integraciones

### Example 2: Refactor de Base de Datos
Cambio: Normalizar tabla Orders (split en Orders + OrderDetails)

Impacto:
- Afectados: 8 repositories, 12 queries, 3 reports
- Riesgo: ALTO (data layer, multiples consumidores)
- Downstream: Caching, indices de busqueda, backups
- Transversales: ETL, data warehouse, BI

Mitigacion:
- Script de migracion con rollback testeado
- Tests de integracion para cada repository
- Validacion de datos post-migracion (checksums)
- Ventana de mantenimiento, comunicacion a stakeholders

## Integration
- Usa: `third-mattpocock-codebase-architecture-analysis-v1.0` (wrapper) — ⚠️ **PENDIENTE**: fuente citada (mattpocock/codebase-architecture-analysis) sin descriptor formal creado todavía. Ver Sesión 5.
- Relacionado con: apb-dev-grill-before-code-v1.0 (evaluar si el cambio vale la pena)

## Tags
#impact-analysis #dependencies #regression #risk #architecture #development

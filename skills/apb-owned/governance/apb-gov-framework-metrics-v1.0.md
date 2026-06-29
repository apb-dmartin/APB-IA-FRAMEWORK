---
id: "apb-gov-framework-metrics-v1.0"
name: "Métricas y Dashboard del APB AI Framework"
description: "Genera el dashboard de uso y KPIs del APB AI Framework: componentes activos por dominio, agentes más usados, tasa de adopción por equipo, calidad del catálogo (% en draft vs. candidate vs. approved), y evolución de la deuda técnica del framework."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Métricas y Dashboard del APB AI Framework

## Propósito
Proporcionar visibilidad sobre el estado, adopción y calidad del APB AI Framework. Permite a Arquitectura APB medir el retorno de la inversión en el framework, identificar áreas de bajo uso, detectar componentes en estado draft que deberían promoverse, y planificar la siguiente fase de enriquecimiento basada en datos reales de uso.

## Contexto de Uso
- Preparación del informe trimestral de Arquitectura APB.
- Comité de seguimiento del framework IA.
- Decisión de qué skills/agentes priorizar en la siguiente sesión de enriquecimiento.
- Onboarding de un equipo nuevo: ¿qué está disponible en el framework para su dominio?
- Revisión de calidad del catálogo: ¿cuántos componentes siguen en draft?

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `report_type` | Enum | `dashboard` / `adopcion` / `calidad-catalogo` / `deuda-tecnica` | ✅ |
| `catalog_data` | JSON | Output de `python scripts/generate_catalog.py` o catálogo en formato JSON | ❌ |
| `usage_data` | JSON | Logs de uso de agentes y skills (si el equipo lleva registro) | ❌ |
| `period` | Texto | Período del informe: ej. "Q2 2026", "Junio 2026" | ❌ |

## Flujo de Trabajo

### Dashboard general

1. **Inventario de componentes** (desde catálogo o listado de archivos del repo):
   - Total de componentes por tipo (skills, agentes, subagentes, providers, wrappers).
   - Distribución por dominio: architecture, development, qa, platform, governance...
   - Distribución por estado: draft / candidate / approved.
   - Componentes creados en el último trimestre.

2. **Cobertura por stack tecnológico APB**:
   - ¿Qué tecnologías del stack tienen skills asociadas?
   - Gaps identificados: tecnologías sin cobertura o con cobertura mínima (<2 skills).

3. **Estado de calidad del catálogo**:
   - % de componentes con todos los campos obligatorios del frontmatter.
   - % de skills con sección "Comportamiento ante inputs incompletos".
   - % de componentes con sección "Marcado IA obligatorio".
   - Componentes con fecha review_date vencida (> 12 meses desde created_date).

4. **Deuda técnica del framework**:
   - Skills en draft desde hace >6 meses sin movimiento.
   - Componentes sin ejemplo de uso documentado.
   - Agentes con skills referenciadas que no existen en el repo.

5. **Señales de la siguiente fase**:
   - Dominios con <5 skills (subcobertura).
   - Gaps identificados en las sesiones anteriores no cubiertos aún.
   - Propuesta de prioridades para la siguiente sesión de enriquecimiento.

### Dashboard de adopción (si hay datos de uso)

1. Top 10 skills más invocadas.
2. Top 5 agentes más activos.
3. Equipos que usan el framework vs. equipos que no lo han adoptado.
4. Tendencia de uso mensual (si hay histórico).

### ⚠️ CHECKPOINT HUMANO
Los datos de adopción requieren fuentes verificadas (logs del sistema, encuestas de equipo) — el modelo solo procesa los datos que se le proporcionan, no tiene acceso a sistemas de monitorización en tiempo real.

## Salida Esperada

```markdown
# Dashboard APB AI Framework — [Período]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-framework-metrics-v1.0) — datos pendientes validación por Arquitectura APB.

## Resumen Ejecutivo
| KPI | Valor | Tendencia |
|---|---|---|
| Total componentes | | |
| Componentes en "approved" | | |
| Cobertura de dominios activos | | |
| Skills con review_date vencida | | |

## Distribución por Tipo
| Tipo | Total | Draft | Candidate | Approved |
|---|---|---|---|---|
| Skills | | | | |
| Agentes | | | | |
| Subagentes | | | | |
| Providers | | | | |

## Distribución por Dominio
| Dominio | Nº componentes | % del total |
|---|---|---|

## Estado de Calidad del Catálogo
| Check | % componentes OK | Acción requerida |
|---|---|---|

## Gaps y Prioridades para Siguiente Fase
1. [Gap 1] — dominio afectado — componentes que faltan
2. [Gap 2] ...

## Deuda Técnica del Framework
| Componente | Tipo de deuda | Antigüedad | Prioridad |
|---|---|---|---|
```

## Criterios de Calidad
- [ ] Los conteos de componentes son consistentes con el estado real del repositorio.
- [ ] Los gaps identificados tienen propuesta de acción concreta.
- [ ] Los componentes con review_date vencida están listados y asignados a un responsable.

## Dependencias
- `scripts/generate_catalog.py` — fuente de verdad para el inventario de componentes
- `scripts/validate_repo.py --strict` — fuente de verdad para el estado de calidad

## Ejemplo de Uso

```
Genera el dashboard del framework para el informe de Q2 2026.
Tengo el catálogo actualizado (adjunto). No tengo datos de uso todavía.
Quiero saber el estado de calidad y qué priorizar en la siguiente sesión.
```

## Notas y Advertencias
- Sin datos de uso reales, el dashboard de adopción es estimativo — recomendar al equipo instrumentalizar las invocaciones de agentes para obtener métricas reales.
- El catálogo debe generarse con `python scripts/generate_catalog.py` justo antes de invocar esta skill para tener datos frescos.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `report_type` | Pregunta: "¿Qué tipo de informe necesitas: dashboard general, adopción, calidad del catálogo o deuda técnica?" | Sí |
| `catalog_data` | Genera instrucciones para obtener el catálogo con `python scripts/generate_catalog.py` e indica que sin él solo puede hacer análisis estructural | No |
| `usage_data` | Genera informe sin sección de adopción, indicando que faltan datos de uso | No |
| `period` | Usa la fecha actual e indica el período asumido explícitamente | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-framework-metrics-v1.0) — datos pendientes validación por Arquitectura APB.

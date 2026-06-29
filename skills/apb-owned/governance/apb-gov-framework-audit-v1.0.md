---
id: "apb-gov-framework-audit-v1.0"
name: "Auditoría de Consistencia del Framework APB"
description: "Audita la consistencia interna del APB AI Framework: detecta skills huérfanos sin agente que los use, referencias rotas entre componentes, componentes obsoletos sin sucesor declarado, violaciones del estándar de marcado IA y gaps de cobertura por dominio. Genera el informe de salud del framework."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Auditoría de Consistencia del Framework APB

## Propósito
Mantener la coherencia y calidad del APB AI Framework a medida que crece. Sin auditoría sistemática, el framework acumula skills huérfanos que nadie usa, referencias rotas entre componentes, componentes obsoletos que confunden a los agentes y gaps de dominio donde no hay cobertura. Este skill ejecuta una auditoría completa del repositorio y produce un informe accionable para el equipo de arquitectura.

## Contexto de Uso
- Revisión trimestral de la salud del framework (proceso GovernanceReview).
- Antes de una sesión de enriquecimiento: identificar qué necesita el framework antes de añadir más componentes.
- Tras una migración o reestructuración del repositorio: verificar que no se rompieron referencias.
- Incorporación de un nuevo dominio al framework: auditar el estado de partida.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `repo_root` | Path | Ruta raíz del repositorio APB AI Framework | ✅ |
| `index_file` | Path | Ruta a `INDEX.md` o `CATALOG.md` para contrastar | ❌ |
| `schema_file` | Path | Ruta a `SCHEMA.md` para validar estructura de frontmatter | ❌ |
| `audit_scope` | Lista | Dominios a auditar; por defecto todos: `all` | ❌ |
| `strict_mode` | Boolean | Si `true`, los warnings se tratan como errores | ❌ |

## Flujo de Trabajo

1. **Inventario del repositorio**:
   - Escanear todos los ficheros `.md` en `skills/`, `agents/`, `subagents/`, `workflows/`, `context/`.
   - Extraer frontmatter YAML de cada componente: id, name, domain, status, version, owner, autonomy_level.
   - Construir el grafo de referencias: qué skills usa cada agente, qué subagents orquesta cada agente.

2. **Detección de skills huérfanos**:
   - Identificar skills que no son referenciados por ningún agente en su sección `skills_used` o en workflows.
   - Clasificar: huérfano puro (nunca referenciado) vs. huérfano reciente (referencias eliminadas).
   - Excluir skills marcados como `standalone: true` en su frontmatter.

3. **Verificación de referencias**:
   - Para cada referencia en la sección `Dependencias` de skills/agentes: verificar que el fichero destino existe.
   - Para cada `skill_id` referenciado en agentes: verificar que el skill existe en `skills/`.
   - Para cada subagent referenciado en agentes: verificar que el subagent existe en `subagents/`.
   - Detectar referencias circulares: A depende de B que depende de A.

4. **Identificación de componentes obsoletos**:
   - Componentes con `status: deprecated` sin `successor` declarado en frontmatter.
   - Componentes con `status: draft` creados hace >90 días sin actualización (fecha de `review_date`).
   - Versiones duplicadas del mismo componente activas simultáneamente (ej. `v1.0` y `v2.0` ambas en status `active`).

5. **Validación de estándar de marcado IA**:
   - Verificar que cada skill/agente/subagent contiene la sección `## Marcado IA obligatorio (POLICY_AI_USAGE §6)`.
   - Comprobar que el frontmatter incluye `autonomy_level` con valor válido (1-5).
   - Detectar skills sin `owner` o con owner en formato incorrecto (debe ser email @portdebarcelona.cat).

6. **Análisis de cobertura por dominio**:
   - Contar componentes activos por dominio: `operation`, `security`, `governance`, `development`, `architecture`, etc.
   - Identificar dominios con cobertura mínima (<3 skills activos).
   - Identificar gaps funcionales: dominios presentes en el plan de fases futuras pero sin implementación.

7. **Análisis de calidad del INDEX y CATALOG**:
   - Comparar componentes en INDEX.md vs. componentes encontrados en el escaneo del repositorio.
   - Detectar componentes presentes en ficheros pero ausentes del índice (sin registrar).
   - Detectar entradas del índice que apuntan a ficheros inexistentes.

8. **⚠️ CHECKPOINT HUMANO**: El equipo de arquitectura debe revisar la lista de componentes marcados para deprecación o eliminación antes de ejecutar cualquier limpieza.

## Salida Esperada

```markdown
# Informe de Auditoría del Framework APB — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-framework-audit-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Resumen de Salud
| Componentes totales | Skills | Agentes | Subagents | Workflows | Score salud (0-100) |

## Errores Críticos (bloquean validate_repo.py)
| Componente | Tipo error | Descripción | Acción requerida |
|---|---|---|---|

## Skills Huérfanos
| Skill ID | Dominio | Creado | Último uso conocido | Recomendación |
|---|---|---|---|---|

## Referencias Rotas
| Componente origen | Referencia rota | Tipo | Acción sugerida |
|---|---|---|---|

## Componentes Obsoletos
| Componente | Status | Problema | Acción sugerida |
|---|---|---|---|

## Violaciones de Marcado IA
| Componente | Violación | Severidad |
|---|---|---|

## Cobertura por Dominio
| Dominio | Skills activos | Agentes | Subagents | Estado | Gaps detectados |
|---|---|---|---|---|---|

## Inconsistencias INDEX/CATALOG
| Tipo | Componente | Descripción |
|---|---|---|

## Recomendaciones Prioritarias
1. [Acción más urgente]
2. ...
```

## Criterios de Calidad
- [ ] El escaneo cubrió el 100% de los ficheros `.md` en los directorios objetivo.
- [ ] Todos los errores críticos tienen acción recomendada concreta.
- [ ] La cobertura por dominio está completa y comparada con el plan de fases futuras.
- [ ] Los componentes marcados para deprecación tienen propuesta de sucesor o eliminación justificada.
- [ ] El score de salud (0-100) está calculado con criterios documentados y reproducibles.
- [ ] El informe puede ejecutarse de forma incremental (solo cambios desde última auditoría).

## Stack y Tecnologías
- Ejecución: `validate_repo.py --strict` (checks automatizables), auditoría manual para checks semánticos
- Análisis de grafo de referencias: Python (networkx) o análisis manual con Grep
- Formatos de salida: Markdown (informe), JSON (datos para dashboard futuro Power BI)

## Dependencias
- `context/apb/standards/AI_MARKING_STANDARD.md` — estándar de marcado verificado
- `context/apb/schemas/SCHEMA.md` — esquema de frontmatter validado
- `INDEX.md`, `CATALOG.md` — índices contra los que se compara el escaneo

## Ejemplo de Uso

```
Ejecuta una auditoría completa del APB AI Framework.
Scope: todos los dominios.
Necesito identificar skills sin usar, referencias rotas y gaps de cobertura
para planificar la sesión de enriquecimiento del próximo trimestre.
```

## Notas y Advertencias
- **Nivel 1**: Las decisiones de deprecación y eliminación de componentes requieren aprobación del equipo de arquitectura.
- La auditoría es una foto fija del momento de ejecución: programar ejecuciones periódicas (trimestral mínimo).
- Un skill "huérfano" no significa que sea inútil: puede ser un skill standalone de uso directo por usuarios. Revisar antes de deprecar.
- El score de salud (0-100) es una métrica relativa: lo relevante es la tendencia entre auditorías, no el valor absoluto.
- Integrar esta skill en el workflow de `GovernanceReview` para automatizar la auditoría periódica.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B, Bloque 2 |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > **Borrador generado por IA** (APB AI Framework - apb-gov-framework-audit-v1.0) — pendiente validación humana. No distribuir sin revisión.

---
id: "apb-gov-catalog-v1.0"
name: "Gestión del Catálogo de IA"
description: "Mantener el catálogo centralizado de componentes de IA del framework APB (skills, agentes, workflows, providers, wrappers). Detecta inconsistencias, propone actualizaciones de versionado, y genera métricas de gobierno del ecosistema de IA."
version: "1.0.0"
status: "draft"
owner: "Gobierno TI APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Gestión del Catálogo de IA


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Mantener el catálogo centralizado de componentes de IA del framework APB (skills, agentes, workflows, providers, wrappers). Detecta inconsistencias, propone actualizaciones de versionado, y genera métricas de gobierno del ecosistema de IA.

## Contexto de Uso
- Registro de nuevos componentes en el catálogo.
- Actualización de estado de componentes (draft → candidate → approved).
- Detección de dependencias rotas o versiones incompatibles.
- Generación de reportes de gobierno para el Comité de IA.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `action` | Enum | `register`, `update`, `validate`, `deprecate`, `report` | ✅ |
| `component` | Texto | ID del componente a gestionar | ✅ (excepto report) |
| `new_status` | Enum | `draft`, `candidate`, `under_review`, `approved`, `deprecated`, `retired` | ❌ |
| `component_metadata` | JSON | Metadatos del componente (versión, owner, dependencias) | ❌ |

## Flujo de Trabajo (Pasos)
1. **Validación de acción**: Verificar que la acción solicitada es válida para el componente.
2. **Registro** (`register`): Añadir nuevo componente al catálogo con metadatos completos.
3. **Actualización** (`update`): Modificar metadatos, estado o versión del componente.
4. **Validación** (`validate`): Verificar consistencia del catálogo:
   - Todos los componentes tienen ID único.
   - Las dependencias referenciadas existen en el catálogo.
   - No hay ciclos de dependencia.
   - Las versiones siguen SemVer.
5. **Deprecación** (`deprecate`): Marcar componente como obsoleto, indicar reemplazo y plazo de soporte.
6. **Generación de reporte** (`report`): Métricas de gobierno:
   - Total de componentes por tipo y estado.
   - Componentes sin descriptor.
   - Dependencias huérfanas.
   - Tiempo medio en cada estado.
7. **Registro de evidencia**: Metadatos de cambios en el catálogo.

## Salida Esperada
### Estructura del Reporte
```markdown
# Reporte de Catálogo de IA — [Período]
> Fecha: [YYYY-MM-DD] | Autor: AI Catalog Manager Agent

## 1. Resumen Ejecutivo
## 2. Métricas de Gobierno
| Indicador | Valor | Objetivo | Estado |
## 3. Componentes por Tipo y Estado
## 4. Dependencias y Grafo
## 5. Inconsistencias Detectadas
## 6. Componentes sin Descriptor
## 7. Roadmap de Aprobación
## 8. Recomendaciones
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] 100% de componentes tienen ID único y metadatos completos.
- [ ] No hay dependencias a componentes inexistentes.
- [ ] No hay ciclos de dependencia en el grafo.
- [ ] Las versiones siguen SemVer consistentemente.
- [ ] El reporte de gobierno incluye KPIs medibles y tendencias.
- [ ] El catálogo es validable por `scripts/validate_repo.py` sin errores.

## Stack y Tecnologías
- Catálogo: `catalog/CATALOG.md` (fuente de verdad)
- Validación: `scripts/validate_repo.py`
- Versionado: SemVer
- Grafo de dependencias: Mermaid, Graphviz
- Formatos: Markdown, JSON para metadatos

## Dependencias
- `apb-gov-evidence-v1.0` — para evidencia de cambios
- `apb-gov-standards-v1.0` — para estándares de nomenclatura
- `scripts/validate_repo.py` — para validación de consistencia

## Ejemplo de Uso
**Prompt de invocación:**
```
Registra el nuevo skill en el catálogo:
- Acción: register
- Componente: apb-sec-forensic-v1.0
- Metadatos: dominio=Security, owner=Ciberseguridad, agente=Security Architect Agent, prioridad=Media
- Dependencias: apb-ops-rca-v1.0, apb-gov-evidence-v1.0
```

## Notas y Advertencias
- **Nivel 1**: El agente gestiona metadatos del catálogo; no modifica el código de los componentes.
- **Revisión humana obligatoria** para cambios de estado a `approved` o `retired`.
- El catálogo `CATALOG.md` es la fuente de verdad; cualquier cambio requiere PR.
- Los componentes en `watchlist` no pueden avanzar de estado hasta evaluación de seguridad y licencia.

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

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-gov-catalog-v1.0) - pendiente validacion humana. No distribuir sin revision.

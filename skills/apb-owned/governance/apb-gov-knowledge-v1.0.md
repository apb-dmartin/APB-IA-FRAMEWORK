---
id: "apb-gov-knowledge-v1.0"
name: "Gestión de Conocimiento"
description: "Estructurar, indexar y mantener el conocimiento técnico y funcional de APB en un sistema de gestión de conocimiento accesible. Incluye categorización, búsqueda semántica, detección de duplicados y mantenimiento de la frescura del contenido."
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

# Gestión de Conocimiento


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Estructurar, indexar y mantener el conocimiento técnico y funcional de APB en un sistema de gestión de conocimiento accesible. Incluye categorización, búsqueda semántica, detección de duplicados y mantenimiento de la frescura del contenido.

## Contexto de Uso
- Onboarding de nuevo personal técnico con acceso a conocimiento estructurado.
- Resolución de problemas mediante búsqueda en base de conocimiento.
- Prevención de pérdida de conocimiento por rotación de equipo.
- Integración con skills de discovery y documentación.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `knowledge_source` | Texto / Archivo | Documento, wiki, conversación o código fuente a indexar | ✅ |
| `category` | Enum | `architecture`, `development`, `qa`, `security`, `operation`, `business` | ✅ |
| `tags` | Lista | Etiquetas para clasificación | ❌ |
| `freshness_review` | Boolean | ¿Requiere revisión de frescura del contenido existente? | ❌ (default: false) |

## Flujo de Trabajo (Pasos)
1. **Ingesta de conocimiento**: Cargar y parsear fuente (markdown, wiki, código comentado).
2. **Extracción de entidades**: Identificar conceptos clave: tecnologías, patrones, decisiones, problemas, soluciones.
3. **Categorización**: Asignar a taxonomía corporativa de conocimiento.
4. **Deduplicación**: Verificar si el conocimiento ya existe en la base; sugerir merge si es duplicado.
5. **Enriquecimiento**: Añadir metadatos, enlaces relacionados, y contexto.
6. **Indexación**: Generar entradas en el sistema de conocimiento con campos estructurados.
7. **Revisión de frescura** (si aplica): Identificar contenido obsoleto (> 1 año sin revisión) y marcar para actualización.
8. **Generación de resumen**: Crear abstracto y keywords para facilitar búsqueda.
9. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Estructura de Entrada de Conocimiento
```markdown
# [Título del Conocimiento]
> ID: KNOW-[YYYY]-[NNNN] | Categoría: [category] | Fecha: [YYYY-MM-DD]
> Autor: [fuente] | Tags: [tags] | Relacionado: [IDs conocimiento relacionado]

## Resumen
## Contexto
## Detalle
## Decisiones y Justificaciones
## Problemas Conocidos y Soluciones
## Referencias
## Estado: [vigente / obsoleto / en revisión]
## Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Cada entrada tiene ID único, categoría y tags consistentes.
- [ ] No hay duplicados sin justificación; los duplicados detectados están marcados para merge.
- [ ] El contenido obsoleto está marcado con fecha de última revisión y estado.
- [ ] Las entradas son searchable por título, tags, categoría y contenido.
- [ ] Trazabilidad a fuentes originales (commits, tickets, documentos).
- [ ] El conocimiento es accesible y comprensible para perfiles junior.

## Stack y Tecnologías
- Sistema de conocimiento: Confluence, SharePoint, o base de conocimiento custom (LightRAG, GraphRAG)
- Indexación: Elasticsearch, Azure AI Search
- NLP: extracción de entidades, resumen automático
- Formatos: Markdown, JSON para metadatos

## Dependencias
- `apb-gov-evidence-v1.0` — para evidencia documental
- `apb-gov-catalog-v1.0` — para tracking en catálogo
- `third-lightrag-knowledge-v1.0` — para RAG de conocimiento (watchlist)

## Ejemplo de Uso
**Prompt de invocación:**
```
Indexa el siguiente conocimiento sobre patrones de integración con Azure Service Bus:
- Fuente: ADR-0042 (decisión de arquitectura)
- Categoría: architecture
- Tags: azure, service-bus, event-driven, integration, patterns
- Relacionado: KNOW-2026-0012, KNOW-2026-0034
```

## Notas y Advertencias
- **Nivel 1**: El agente estructura e indexa conocimiento; no modifica sistemas de producción sin confirmación.
- **Revisión humana recomendada** para contenido marcado como obsoleto o duplicado.
- La base de conocimiento debe respaldarse periódicamente.
- El agente no tiene acceso a información confidencial sin los permisos adecuados.

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
  > **Borrador generado por IA** (APB AI Framework - apb-gov-knowledge-v1.0) - pendiente validacion humana. No distribuir sin revision.

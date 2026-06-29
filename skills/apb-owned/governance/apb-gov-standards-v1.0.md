---
id: "apb-gov-standards-v1.0"
name: "Mantenimiento de Estándares Corporativos"
description: "Mantener actualizado el repositorio de estándares corporativos de APB (arquitectura, desarrollo, QA, seguridad, operación). Detecta obsolescencia, propone actualizaciones basadas en evolución tecnológica, y valida que nuevos estándares no entren en conflicto con existentes."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Mantenimiento de Estándares Corporativos

## Propósito
Mantener actualizado el repositorio de estándares corporativos de APB (arquitectura, desarrollo, QA, seguridad, operación). Detecta obsolescencia, propone actualizaciones basadas en evolución tecnológica, y valida que nuevos estándares no entren en conflicto con existentes.

## Contexto de Uso
- Revisión periódica de estándares (trimestral/semestral).
- Propuesta de nuevos estándares ante introducción de nuevas tecnologías.
- Validación de consistencia entre estándares de diferentes dominios.
- Integración con workflows de gobierno y arquitectura de referencia.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `standards_scope` | Enum | `architecture`, `development`, `qa`, `security`, `operation`, `all` | ✅ |
| `review_trigger` | Enum | `scheduled`, `technology_change`, `audit_finding`, `incident` | ✅ |
| `current_standards` | Lista | Lista de estándares actuales con versión y fecha | ✅ |
| `new_technologies` | Lista | Nuevas tecnologías o prácticas a evaluar | ❌ |
| `audit_findings` | Lista | Hallazgos de auditoría que requieren actualización de estándar | ❌ |

## Flujo de Trabajo (Pasos)
1. **Inventario de estándares**: Cargar estándares vigentes desde `context/apb/standards/`.
2. **Evaluación de obsolescencia**: Para cada estándar, verificar:
   - Fecha de última revisión (> 1 año = revisión obligatoria).
   - Tecnologías referenciadas aún soportadas.
   - Compatibilidad con stack tecnológico actual de APB.
3. **Análisis de nuevas tecnologías**: Evaluar impacto de nuevas tecnologías en estándares existentes.
4. **Detección de conflictos**: Identificar estándares contradictorios entre dominios.
5. **Propuesta de actualizaciones**:
   - **Amendment** — Cambio menor (versión patch).
   - **Revision** — Cambio significativo (versión minor).
   - **New Standard** — Nuevo estándar (versión 1.0.0).
   - **Deprecation** — Estándar obsoleto, reemplazado por otro.
6. **Generación de changelog**: Documentar cambios propuestos con justificación.
7. **Validación de consistencia**: Verificar que estándares actualizados son coherentes entre sí.
8. **Generación de informe**: Documento con estado de estándares, propuestas y roadmap de revisión.
9. **Registro de evidencia**: Metadatos para gobierno y aprobación del Comité de Arquitectura.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe de Mantenimiento de Estándares — [Período]
> Fecha: [YYYY-MM-DD] | Autor: Governance Agent | Scope: [standards_scope]

## 1. Inventario de Estándares
| ID | Nombre | Versión | Última Revisión | Estado | Próxima Revisión |
## 2. Estándares Obsoletos
## 3. Propuestas de Actualización
| ID | Tipo de Cambio | Justificación | Impacto | Riesgo |
## 4. Conflictos Detectados
## 5. Nuevos Estándares Propuestos
## 6. Roadmap de Revisión
## 7. Recomendaciones al Comité de Arquitectura
## 8. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] 100% de estándares del scope evaluados para obsolescencia.
- [ ] Cada propuesta de cambio tiene justificación técnica y análisis de impacto.
- [ ] Conflictos entre estándares identificados y resueltos o escalados.
- [ ] Roadmap de revisión con fechas y responsables sugeridos.
- [ ] El informe es presentable al Comité de Arquitectura sin edición adicional.
- [ ] Trazabilidad entre estándares, tecnologías y decisiones de arquitectura.

## Stack y Tecnologías
- Repositorio: `context/apb/standards/` en Git
- Control de versiones: SemVer para estándares
- Formatos: Markdown, YAML para metadatos de estándares
- Tracking: Jira epics para aprobación de estándares

## Dependencias
- `apb-gov-evidence-v1.0` — para evidencia de revisión
- `apb-gov-catalog-v1.0` — para tracking de estándares en catálogo
- `apb-gov-arch-ref-v1.0` — para validación contra arquitectura de referencia
- `apb-agent-tech-discovery-v1.0` — para evaluación de nuevas tecnologías

## Ejemplo de Uso
**Prompt de invocación:**
```
Revisa los estándares de desarrollo de APB:
- Scope: development
- Trigger: technology_change (migración a .NET 8)
- Estándares actuales: STD-DEV-001 a STD-DEV-024
- Nuevas tecnologías: .NET 8, Minimal APIs, Native AOT
- Hallazgos de auditoría: STD-DEV-012 requiere actualización por obsolescencia de .NET Framework 4.8
```

## Notas y Advertencias
- **Nivel 1**: El agente propone actualizaciones; no modifica estándares aprobados directamente.
- **Revisión humana obligatoria** por el Comité de Arquitectura para cualquier cambio de estándar.
- Los estándares deprecados deben mantenerse visibles durante 1 año con marca de obsolescencia.
- Las propuestas de nuevos estándares requieren análisis de alternativas (discovery obligatorio).
- El agente no tiene acceso de escritura al repo de estándares sin aprobación de PR.

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
  > **Borrador generado por IA** (APB AI Framework - apb-gov-standards-v1.0) - pendiente validacion humana. No distribuir sin revision.

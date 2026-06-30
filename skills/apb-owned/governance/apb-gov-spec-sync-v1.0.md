---
id: "apb-gov-spec-sync-v1.0"
name: "Sincronización Automática del Spec"
description: "Mantener sincronizados los documentos de especificación (system-spec.md, api-spec.md, etc.) con el código fuente, los tests y la documentación de arquitectura. Detecta desviaciones entre spec y implementación, genera alertas de drift y propone actualizaciones."
version: "1.0.0"
status: "draft"
owner: "Gobierno TI APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 2
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Sincronización Automática del Spec


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Mantener sincronizados los documentos de especificación (system-spec.md, api-spec.md, etc.) con el código fuente, los tests y la documentación de arquitectura. Detecta desviaciones entre spec y implementación, genera alertas de drift y propone actualizaciones.

## Contexto de Uso
- Detección de spec drift en proyectos en desarrollo activo.
- Actualización automática de specs tras cambios en la arquitectura o API.
- Validación de que el código implementado cumple con la especificación vigente.
- Integración con pipelines CI/CD para validación continua de specs.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `spec_file` | Texto | Ruta o contenido del documento de especificación | ✅ |
| `source_code` | Texto / Código | Código fuente a comparar con el spec | ✅ |
| `test_code` | Texto / Código | Tests que validan el spec | ❌ |
| `sync_mode` | Enum | `detect-only`, `propose-update`, `auto-update` | ❌ (default: detect-only) |
| `notification_channel` | Enum | `pr-comment`, `jira-comment`, `slack`, `email` | ❌ |

## Flujo de Trabajo (Pasos)
1. **Parseo del spec**: Extraer requisitos funcionales, endpoints, modelos de datos, reglas de negocio.
2. **Análisis de código**: Extraer implementación actual (controllers, servicios, modelos, DTOs).
3. **Comparación semántica**: Identificar discrepancias:
   - Endpoints no documentados o documentados pero no implementados.
   - Campos de modelo que difieren entre spec y código.
   - Reglas de negocio no reflejadas en tests.
   - Cambios de versión de API no sincronizados.
4. **Clasificación de drift**:
   - `breaking` — Cambio incompatible (requiere versión major).
   - `feature` — Nueva funcionalidad no documentada.
   - `fix` — Corrección de documentación.
   - `cosmetic` — Formato, typos, ejemplos.
5. **Generación de reporte de drift**: Listado de discrepancias con severidad y ubicación.
6. **Propuesta de actualización** (si `sync_mode` = `propose-update`): Generar diff sugerido para el spec.
7. **Notificación**: Enviar alerta por canal configurado con resumen de drift.
8. **Registro de evidencia**: Metadatos para gobierno y tracking de specs.

## Salida Esperada
### Estructura del Reporte de Drift
```markdown
# Spec Drift Report — [Nombre Proyecto]
> Fecha: [YYYY-MM-DD] | Spec: [ruta] | Commit: [SHA] | Autor: Documentation Agent

## 1. Resumen de Drift
| Tipo | Count | Severidad |
## 2. Detalle de Discrepancias
| ID | Categoría | Ubicación Spec | Ubicación Código | Descripción | Severidad | Acción Propuesta |
## 3. Endpoints Orphan
## 4. Modelos Desincronizados
## 5. Tests Faltantes
## 6. Propuesta de Actualización (si aplica)
## 7. Recomendaciones
## 8. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] 100% de endpoints del spec están verificados contra código.
- [ ] Cada discrepancia tiene categoría, severidad y ubicación precisa.
- [ ] El reporte de drift es actionable (indica archivo y línea cuando es posible).
- [ ] Las propuestas de actualización preservan la estructura y formato del spec original.
- [ ] No se realizan cambios automáticos en specs aprobados sin confirmación humana.
- [ ] El reporte es revisable por el equipo de desarrollo sin intervención del agente.

## Stack y Tecnologías
- Parseo de specs: Markdown AST, OpenAPI parser, custom regex
- Análisis de código: Roslyn (C#), AST parsers
- Comparación: diff semántico, tree comparison
- Notificación: GitHub PR comments, Jira REST API, Slack webhooks
- Formatos: Markdown, JSON para metadatos

## Dependencias
- `apb-disc-spec-gen-v1.0` — para generación de specs
- `apb-gov-evidence-v1.0` — para evidencia de sincronización
- `apb-gov-jira-evidence-v1.0` — para registro en Jira
- `apb-dev-code-base-v1.0` — para análisis de codebase

## Ejemplo de Uso
**Prompt de invocación:**
```
Detecta drift entre nuestro spec y la implementación actual:
- Spec: docs/system-spec.md (versión 2.3.0)
- Código: src/ (ASP.NET Core 8)
- Tests: tests/ (xUnit)
- Modo: propose-update
- Notificar: PR comment en rama feature/payments-v3
```

## Notas y Advertencias
- **Nivel 2**: En modo `auto-update`, el agente puede proponer PRs con cambios; requieren aprobación humana.
- **Revisión humana obligatoria** para cualquier cambio en specs aprobados.
- El modo `detect-only` es el default seguro; `auto-update` solo en entornos de desarrollo.
- Los cambios breaking requieren versión major del spec y aprobación de arquitectura.
- El agente no tiene acceso a repositorios privados sin autenticación configurada.

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
  > **Borrador generado por IA** (APB AI Framework - apb-gov-spec-sync-v1.0) - pendiente validacion humana. No distribuir sin revision.

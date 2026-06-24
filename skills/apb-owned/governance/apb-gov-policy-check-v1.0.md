---
id: "apb-gov-policy-check-v1.0"
name: "Validación de Políticas APB"
description: "Validar que decisiones, diseños, implementaciones y operaciones cumplen con las políticas corporativas de APB. Detecta violaciones, propone excepciones formalizadas cuando sea necesario, y mantiene un registro de compliance de políticas."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Validación de Políticas APB

## Propósito
Validar que decisiones, diseños, implementaciones y operaciones cumplen con las políticas corporativas de APB. Detecta violaciones, propone excepciones formalizadas cuando sea necesario, y mantiene un registro de compliance de políticas.

## Contexto de Uso
- Validación de políticas en gates de arquitectura, desarrollo y despliegue.
- Verificación de cumplimiento de políticas de seguridad, IA, calidad y operación.
- Gestión de excepciones a políticas con trazabilidad y aprobación.
- Integración con workflows de gobierno y riesgo.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `subject` | Texto / Markdown | Documento, código o decisión a validar | ✅ |
| `policy_scope` | Lista | Políticas a validar: `security`, `ai-usage`, `data-privacy`, `operation`, `all` | ✅ |
| `subject_type` | Enum | `architecture`, `code`, `process`, `decision`, `deployment` | ✅ |
| `exception_context` | Texto | Contexto si se solicita excepción | ❌ |

## Flujo de Trabajo (Pasos)
1. **Carga de políticas**: Obtener políticas vigentes desde `context/apb/policies/`.
2. **Análisis del sujeto**: Parsear el documento, código o decisión a validar.
3. **Validación por política**: Para cada política aplicable, verificar cumplimiento:
   - **POL-SEC-XXX**: Seguridad (cifrado, autenticación, secretos).
   - **POL-AI-XXX**: Uso de IA (transparencia, no decisiones autónomas críticas, revisión humana).
   - **POL-DATA-XXX**: Privacidad y protección de datos (GDPR, LOPD, minimización).
   - **POL-OPS-XXX**: Operación (observabilidad, backup, recuperación).
4. **Identificación de violaciones**: Documentar política violada, severidad y impacto.
5. **Evaluación de excepciones**: Si el contexto justifica una excepción, generar:
   - Justificación de negocio.
   - Riesgo residual.
   - Controles compensatorios.
   - Plazo de validez.
   - Aprobador requerido.
6. **Generación de informe**: Documento con estado de compliance, violaciones y excepciones.
7. **Registro de evidencia**: Metadatos para gobierno y auditoría.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe de Validación de Políticas — [Sujeto]
> Fecha: [YYYY-MM-DD] | Autor: Governance Agent | Scope: [policy_scope]

## 1. Alcance y Contexto
## 2. Políticas Evaluadas
## 3. Resumen de Compliance
| Política | Estado | Severidad | Hallazgo | Excepción |
## 4. Violaciones Detalladas
## 5. Excepciones Propuestas
## 6. Plan de Remediación
## 7. Recomendaciones
## 8. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todas las políticas del scope están evaluadas.
- [ ] Cada violación tiene severidad, impacto y referencia a política.
- [ ] Las excepciones incluyen justificación, riesgo residual, controles compensatorios y plazo.
- [ ] El informe es presentable al Comité de Seguridad y Gobierno sin edición adicional.
- [ ] No se incluyen secretos ni datos sensibles en el informe.

## Stack y Tecnologías
- Políticas: `context/apb/policies/`
- Parseo: Markdown, AST de código
- Formatos: Markdown, Jira para tracking de excepciones

## Dependencias
- `apb-gov-evidence-v1.0` — para evidencia de validación
- `apb-gov-standards-v1.0` — para estándares relacionados
- `apb-sec-risk-policies-v1.0` — para análisis de riesgo de excepciones
- `apb-wf-risk-exception-v1.0` — para workflow de excepciones

## Ejemplo de Uso
**Prompt de invocación:**
```
Valida políticas para la siguiente decisión de arquitectura:
- Sujeto: Uso de LLM (GPT-4) para generación automática de respuestas a ciudadanos
- Scope: ai-usage, data-privacy, security
- Contexto: El sistema procesa solicitudes de información pública; el LLM genera borradores que son revisados por humanos antes de envío
- Preocupación: ¿Cumple POL-AI-003 (revisión humana obligatoria para decisiones que afectan a ciudadanos)?
```

## Notas y Advertencias
- **Nivel 1**: El agente valida y propone; no aprueba excepciones ni modifica políticas.
- **Revisión humana obligatoria** para todas las excepciones a políticas.
- Las políticas de IA son especialmente sensibles; cualquier excepción requiere aprobación del Comité de Ética de IA.
- El agente no tiene acceso a datos personales para validar políticas de privacidad; trabaja con descripciones.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |

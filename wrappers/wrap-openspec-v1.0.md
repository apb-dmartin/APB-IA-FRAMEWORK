---
id: "wrap-openspec-v1.0"
name: "OpenSpec Kit"
description: "Wrapper para adaptar el OpenSpec Kit al formato de plantillas APB. Valida estructura, adapta salidas y garantiza consistencia con el estándar de especificaciones del framework."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
wraps: "OpenSpec Kit"
source_repo: "https://github.com/Fission-AI/OpenSpec"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# OpenSpec Kit

## Descripción
Wrapper para adaptar el OpenSpec Kit al formato de plantillas APB. Valida estructura, adapta salidas y garantiza consistencia con el estándar de especificaciones del framework.

## Funciones del Wrapper

### 1. Adaptación a Plantillas APB
- Conversión de specs OpenSpec → formato APB
- Aplicación de plantilla `system-spec.md`
- Inclusión de metadatos ENS y gobierno

### 2. Validación de Estructura
- Verificación de campos obligatorios
- Validación de referencias cruzadas
- Chequeo de consistencia

### 3. Mapeo de Componentes
- Mapeo de entidades OpenSpec → dominios APB
- Identificación de bounded contexts
- Generación de diagramas compatibles

### 4. Integración con Workflows
- Conexión a `apb-wf-spec-from-legacy-v1.0`
- Generación de backlog desde specs
- Vinculación a ADRs

## Skills Cubiertos
| Skill Tercero | Skill APB Relacionada | Estado |
|---------------|----------------------|--------|
| `third-openspec-spec-gen-v1.0` | `apb-disc-spec-gen-v1.0` | draft |

## Configuración
```json
{
  "wrapper_id": "wrap-openspec-v1.0",
  "source": "OpenSpec Kit",
  "license": "MIT",
  "template_mapping": {
    "openspec_template": "context/apb/templates/SPEC.md",
    "adr_template": "context/apb/templates/ADR.md"
  },
  "validation_rules": [
    "required_fields",
    "cross_references",
    "ens_metadata"
  ],
  "runtimes": ["copilot", "claude"]
}
```

## Inputs
- `openspec_output`: salida del OpenSpec Kit
- `project_context`: contexto del proyecto APB
- `template_version`: versión de plantilla APB

## Outputs
- `apb_spec`: especificación en formato APB
- `validation_report`: informe de validación
- `component_mapping`: mapeo de componentes

## Restricciones
- Plantilla APB obligatoria
- Metadatos ENS requeridos
- Validación humana antes de aprobación
- No modifica lógica de generación OpenSpec

## Ejemplo de Uso
```
Invocar: wrap-openspec-v1.0
Input: { openspec_output: "...", project_context: "APB.LegacyApp" }
Output: system-spec.md en formato APB con validación
```

---
*Wrapper APB AI Framework.*

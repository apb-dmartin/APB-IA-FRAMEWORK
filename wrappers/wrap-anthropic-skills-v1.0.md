---
id: "wrap-anthropic-skills-v1.0"
name: "Anthropic Skills"
description: "Wrapper para adaptar skills de Anthropic al formato y estándares del APB AI Framework. Gestiona la validación de licencia MIT, filtra capacidades no corporativas y normaliza inputs/outputs."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
wraps: "Anthropic Skills"
source_repo: "https://github.com/anthropics/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Anthropic Skills

## Descripción
Wrapper para adaptar skills de Anthropic al formato y estándares del APB AI Framework. Gestiona la validación de licencia MIT, filtra capacidades no corporativas y normaliza inputs/outputs.

## Funciones del Wrapper

### 1. Adaptación de Formato
- Conversión de prompts Anthropic → formato APB
- Normalización de metadatos (ID, versión, estado)
- Mapeo de capacidades a skills APB existentes

### 2. Validación de Licencia
- Verificación de licencia MIT
- Registro de atribución
- Cumplimiento de requisitos de licencia

### 3. Filtrado de Capacidades
- Identificación de capacidades no corporativas
- Aplicación de políticas de seguridad APB
- Restricción de acceso a datos sensibles

### 4. Integración con Runtime
- Adaptación para GitHub Copilot
- Adaptación para Claude (Anthropic)
- Mapeo de capabilities a runtime específico

## Skills Cubiertos
| Skill Tercero | Skill APB Relacionada | Estado |
|---------------|----------------------|--------|
| `third-anthropic-business-discovery-v1.0` | `apb-disc-business-v1.0` | draft |

## Configuración
```json
{
  "wrapper_id": "wrap-anthropic-skills-v1.0",
  "source": "Anthropic Skills",
  "license": "MIT",
  "validation_rules": [
    "check_license",
    "filter_capabilities",
    "normalize_format"
  ],
  "runtimes": ["copilot", "claude"]
}
```

## Inputs
- `raw_skill`: skill de terceros en formato original
- `target_runtime`: runtime objetivo (copilot/claude)
- `security_policy`: política de seguridad a aplicar

## Outputs
- `adapted_skill`: skill adaptado al formato APB
- `validation_report`: informe de validación
- `capability_mapping`: mapeo de capacidades

## Restricciones
- Solo skills con licencia MIT o compatible
- No modifica la lógica interna del skill
- Requiere aprobación de AI Catalog Manager

## Ejemplo de Uso
```
Invocar: wrap-anthropic-skills-v1.0
Input: { raw_skill: "anthropic-business-discovery", target_runtime: "claude" }
Output: Skill adaptado con metadatos APB y validación
```

---
*Wrapper APB AI Framework.*

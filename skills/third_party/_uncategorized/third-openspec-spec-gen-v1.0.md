---
id: "third-openspec-spec-gen-v1.0"
name: "Skill: Spec Generation (OpenSpec Kit)"
description: "Generación automática de especificaciones técnicas desde código fuente, documentación y requisitos. Soporta múltiples formatos de salida."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
source_repo: "https://github.com/Fission-AI/OpenSpec"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Skill: Spec Generation (OpenSpec Kit)

---

## Descripción
Generación automática de especificaciones técnicas desde código fuente, documentación y requisitos. Soporta múltiples formatos de salida.

## Capacidades
- Generación de specs desde código (.NET, Python, JS)
- Extracción de contratos API desde implementación
- Generación de diagramas de secuencia
- Validación de consistencia spec-código

## Inputs
- `source_code_path`: ruta al código fuente
- `existing_docs`: documentación existente (opcional)
- `output_format`: formato de salida deseado

## Outputs
- `system_spec.md`
- `api_contracts.md`
- `sequence_diagrams.md`

## Restricciones
- Requiere acceso al repositorio fuente
- No modifica código existente
- Validación humana obligatoria

## Adaptaciones APB
- Formato de salida adaptado a plantilla APB
- Integración con `apb-disc-spec-gen-v1.0`
- Workflow `apb-wf-spec-from-legacy-v1.0`

## Ejemplo de Uso
```
Invocar: third-openspec-spec-gen-v1.0
Input: { source_code_path: "/repos/legacy-app", output_format: "APB" }
Output: system_spec.md en formato APB estándar
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

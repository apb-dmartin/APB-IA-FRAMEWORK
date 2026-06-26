---
id: "third-mattpocock-grill-prd-issues-v1.0"
name: "Skill: Grill → PRD → Issues (mattpocock/skills)"
description: "Flujo de clarificación de requisitos mediante interrogatorio estructurado (grilling), seguido de generación de PRD y descomposición en issues independientes, adaptado del repositorio público mattpocock/skills."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
source_repo: "https://github.com/mattpocock/skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: Grill → PRD → Issues (mattpocock/skills)

---

## Descripción
Adaptación del flujo `grill-me` / `to-prd` / `to-issues` del repositorio público
`mattpocock/skills` (MIT, Matt Pocock). El patrón original interroga al usuario
recorriendo cada rama del "árbol de diseño" hasta alcanzar un entendimiento
compartido antes de escribir código, sintetiza la conversación en un PRD, y
descompone el PRD en issues independientes ("vertical slices") listos para
asignar.

> **Nota de gobernanza:** este descriptor cubre un gap de catálogo identificado
> en la Sesión 7. Citado desde `apb-dev-grill-before-code-v1.0` antes de existir
> como componente formal. El repositorio de origen es un monorepo de ~21 skills;
> este descriptor cubre específicamente la cadena `grill-me → to-prd → to-issues`,
> no la totalidad del repositorio.

## Capacidades
- Interrogatorio estructurado de requisitos antes de implementar (`/grill-me`)
- Síntesis de la conversación en un PRD sin necesidad de re-entrevista (`/to-prd`)
- Descomposición del PRD en issues de tamaño manejable y con dependencias
  explícitas entre tareas (`/to-issues`)

## Inputs
- `feature_description`: descripción inicial de la necesidad o cambio
- `conversation_context`: contexto de la sesión de grilling (si ya se realizó)

## Outputs
- `clarifying_questions`: preguntas generadas durante el grilling
- `prd_document`: PRD sintetizado
- `issues_list`: lista de issues con relaciones de bloqueo entre ellos

## Restricciones
- El flujo original asume convenciones de stack TypeScript/Node y GitHub Issues;
  en APB se adapta el *patrón* (interrogatorio → PRD → issues), no las
  integraciones técnicas específicas del repo origen
- No sustituye la skill `apb-disc-enrich-req-v1.0` (enriquecimiento de
  requisitos) cuando ya existe una especificación formal: este flujo es previo,
  para cuando la necesidad aún no está formalizada

## Adaptaciones APB
- Integración con Jira como sistema de tickets en lugar de GitHub Issues nativo
- Las preguntas de clarificación deben registrarse para trazabilidad
  (Gobernanza §3.4 del proyecto)

## Ejemplo de Uso
```
Invocar: third-mattpocock-grill-prd-issues-v1.0
Input: { feature_description: "Nuevo módulo de facturación de escalas portuarias" }
Output: PRD sintetizado + lista de issues con dependencias, listos para Jira
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

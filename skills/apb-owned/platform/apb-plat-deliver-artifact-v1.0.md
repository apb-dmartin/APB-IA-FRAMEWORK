---
id: "apb-plat-deliver-artifact-v1.0"
name: "Artifact Delivery Skill"
description: "Skill transversal de plataforma para la entrega de cualquier artefacto generado por el framework (specs, informes, mockups, documentación, informes de riesgo, planes, código). Implementa el flujo estándar de entrega: (1) presenta el artefacto en el chat en formato nativo para revisión del usuario, (2) solicita aprobación antes de cualquier envío externo, (3) pregunta el formato de exportación deseado (Word, HTML, PDF, ZIP), (4) pregunta el destino de entrega (Jira, Confluence, SharePoint, correo, descarga directa). Todos los agentes que generan entregables finales invocan esta skill como último paso antes de cerrar su ciclo."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
inputs:
  - "artifact_content: contenido del artefacto (Markdown, HTML o texto estructurado)"
  - "artifact_type: spec | mockup | report | documentation | risk-report | plan | code | iac | ansible | helm | pipeline | script | sql | config | mixed | other"
  - "artifact_name: nombre base del fichero sin extensión (ej. spec-gispem-v1)"
  - "agent_id: ID del agente que genera el artefacto (para trazabilidad)"
  - "human_review_required: booleano — si true, el artefacto debe pasar por human_review_point antes de la entrega externa"
  - "suggested_formats: lista de formatos recomendados por el agente según el tipo de artefacto (opcional)"
outputs:
  - "Artefacto presentado en el chat en formato nativo para revisión"
  - "Artefacto exportado en el/los formatos que el usuario elige"
  - "Artefacto depositado en el/los destinos que el usuario elige"
  - "Confirmación de entrega con URLs, IDs y destinatarios"
depends_on:
  - "prov-ms365-v1.0"
  - "prov-atlassian-v1.0"
  - "apb-plat-sharepoint-io-v1.0"
  - "apb-plat-doc-to-markdown-v1.0"
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Artifact Delivery Skill

## Propósito

Centraliza el flujo de entrega de todos los artefactos del framework en una sola skill
reutilizable. Ningún agente gestiona su propia lógica de entrega — todos invocan esta
skill cuando tienen un artefacto listo para el usuario.

Garantiza que:
- El usuario siempre revisa y aprueba antes de que salga cualquier cosa al exterior
- El formato y destino son siempre elección del usuario, no decisión del agente
- Todos los artefactos llevan metadatos de trazabilidad obligatorios
- El patrón es idéntico en todos los agentes del framework

---

## Prompt de Sistema

```
Eres el skill "Artifact Delivery Skill" (apb-plat-deliver-artifact-v1.0)
del APB AI Framework, operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Antes de ejecutar cualquier tarea, carga:
  context/apb/knowledge/APB_KNOWLEDGE_BASE.md  (provider: prov-apb-knowledge-v1.0)

Contiene: negocio portuario, catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS),
integraciones, terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

## Misión
Gestionar la entrega de cualquier artefacto generado por el framework (specs, informes,
mockups, documentación, informes de riesgo, planes, código). Implementas el flujo estándar:
presentar el artefacto en el chat para revisión, solicitar aprobación, preguntar formato
de exportación y destino de entrega. Todos los agentes que generan entregables finales
te invocan como último paso antes de cerrar su ciclo.

## Inputs Esperados
- artifact_content: contenido del artefacto (Markdown, HTML o texto estructurado)
- artifact_type: spec | mockup | report | documentation | risk-report | plan | code | iac | sql | other
- artifact_name: nombre base del fichero sin extensión
- agent_id: ID del agente que genera el artefacto (para trazabilidad)
- human_review_required: booleano — si true, pasa por human_review_point antes de entrega externa
- suggested_formats: lista de formatos recomendados (opcional)

## Instrucciones
1. Presenta el artefacto en el chat en formato nativo (Markdown renderizado) para revisión.
2. Si human_review_required=true, invoca apb-orch-human-checkpoint-v1.0 antes de continuar.
3. Solicita aprobación explícita del usuario antes de cualquier envío externo.
4. Pregunta el formato de exportación: Word | HTML | PDF | ZIP.
5. Pregunta el destino: Jira | Confluence | SharePoint | correo | descarga directa.
6. Entrega al destino usando los providers correspondientes (prov-ms365-v1.0, prov-atlassian-v1.0).
7. Confirma la entrega con URLs, IDs y destinatarios.

## Restricciones
- Nunca envíes externamente sin aprobación humana explícita.
- Autonomía nivel 1: todas las acciones de entrega requieren confirmación del usuario.
- No generes el contenido del artefacto: eres el paso de entrega, no de generación.

## Formato de Salida
Confirmación de entrega: canal usado, URL/ID del artefacto publicado, destinatarios y timestamp.
```

---

## Tipos de artefacto soportados

### Familia Documento

| artifact_type | Descripción | Formatos disponibles | Ruta SharePoint por defecto |
|--------------|-------------|---------------------|----------------------------|
| `spec` | Especificación funcional o técnica | Word, HTML, PDF, ZIP | `Proyectos/[X]/Documentacion/` |
| `mockup` | Prototipo HTML + especificación | HTML, ZIP | `Arquitectura/Artefactos-IA/Mockups/` |
| `report` | Informe técnico, de discovery, de deuda | Word, HTML, PDF, ZIP | `Arquitectura/Artefactos-IA/` |
| `risk-report` | Informe de análisis de riesgos | Word, HTML, PDF, ZIP | `Arquitectura/Artefactos-IA/Informes-Riesgo/` |
| `documentation` | Documentación funcional o técnica | Word, HTML, PDF, ZIP | `Proyectos/[X]/Documentacion/` |
| `plan` | Plan de remediación, plan de proyecto | Word, HTML, PDF, ZIP | `Arquitectura/Artefactos-IA/Planes/` |

### Familia Código

| artifact_type | Descripción | Formatos disponibles | Ruta SharePoint por defecto |
|--------------|-------------|---------------------|----------------------------|
| `code` | Código de aplicación generado o scaffolding | ZIP | `Proyectos/[X]/Codigo/` |
| `iac` | Infraestructura como código (Terraform, Bicep, CloudFormation) | ZIP | `Arquitectura/Artefactos-IA/IaC/` |
| `ansible` | Playbooks y roles Ansible | ZIP | `Arquitectura/Artefactos-IA/IaC/` |
| `helm` | Charts Helm / manifiestos Kubernetes | ZIP | `Arquitectura/Artefactos-IA/IaC/` |
| `pipeline` | Pipelines CI/CD (YAML Azure DevOps, GitHub Actions, etc.) | ZIP | `Arquitectura/Artefactos-IA/Pipelines/` |
| `script` | Scripts de automatización (PowerShell, Bash, Python) | ZIP | `Arquitectura/Artefactos-IA/Scripts/` |
| `sql` | Scripts SQL, migraciones, stored procedures | ZIP | `Proyectos/[X]/BaseDatos/` |
| `config` | Ficheros de configuración (appsettings, .env, variables) | ZIP | `Proyectos/[X]/Configuracion/` |

### Mixta

| artifact_type | Descripción | Formatos disponibles | Ruta SharePoint por defecto |
|--------------|-------------|---------------------|----------------------------|
| `mixed` | Combinación de documento + código en el mismo entregable | Word/PDF para docs, ZIP para el conjunto | Según subtipo dominante |
| `other` | Cualquier artefacto no clasificable | ZIP | `Arquitectura/Artefactos-IA/` |

---

## Agentes que invocan esta skill

Todos los agentes que generan entregables finales deben invocar esta skill
como último paso de su flujo, pasando:
- `artifact_content`: el artefacto generado (Markdown o HTML)
- `artifact_type`: según la tabla anterior
- `artifact_name`: nombre base sin extensión
- `agent_id`: su propio ID
- `human_review_required`: true si el artefacto está en un `human_review_point`

| Agente | artifact_type | Nota |
|--------|--------------|------|
| `apb-agent-ux-mockup-v1.0` | `mockup` | Spec (Markdown) + prototipo (HTML) — los dos artefactos |
| `apb-agent-spec-engineer-v1.0` | `spec` | Especificación funcional/técnica |
| `apb-agent-documentation-v1.0` | `documentation` | Documentación por audiencia |
| `apb-agent-tech-discovery-v1.0` | `report` | Informe de discovery técnico |
| `apb-agent-tech-debt-v1.0` | `report` | Informe de deuda técnica |
| `apb-agent-compliance-audit-v1.0` | `risk-report` | Informe de riesgos organizativo |
| `apb-agent-risk-exception-v1.0` | `risk-report` | Informe de excepción de riesgo |
| `apb-agent-business-analyst-v1.0` | `spec` | Especificación funcional / user stories |
| `apb-agent-cloud-architect-v1.0` | `report` | Informe de arquitectura cloud |
| `apb-agent-security-architect-v1.0` | `report` | Informe de seguridad |
| `apb-agent-domain-architect-v1.0` | `report` | Informe de dominio / ADR |
| `apb-agent-technical-architect-v1.0` | `report` | Decisiones arquitectónicas / ADR |
| `apb-agent-modernization-v1.0` | `plan` | Plan de modernización |
| `apb-agent-finops-v1.0` | `report` | Informe de costes cloud |
| `apb-agent-release-manager-v1.0` | `report` | Release notes / plan de despliegue |
| `apb-agent-qa-auto-v1.0` | `report` | Informe de cobertura / plan de tests |
| `apb-agent-implementer-v1.0` | `code` o `mixed` | Código generado + spec técnica (si produce spec aparte → `mixed`) |
| `apb-agent-platform-engineer-v1.0` | `iac` o `pipeline` | Terraform, Bicep, pipelines CI/CD |
| `apb-agent-sre-v1.0` | `script` o `mixed` | Scripts de automatización, runbooks Markdown, IaC de observabilidad |

---

## Metadatos obligatorios en todos los formatos

Todo artefacto exportado o depositado por esta skill lleva obligatoriamente:

| Metadato | Valor |
|---------|-------|
| `Generado_Por_IA` | `Sí` |
| `Agente_Origen` | ID del agente que generó el contenido |
| `Estado_Revision` | `Pendiente de validación humana` |
| `Fecha_Generacion` | Fecha ISO del momento de generación |

En documentos Word: en las propiedades personalizadas del documento.
En HTML: en `<meta>` tags del `<head>` y en banner visible en el cuerpo.
En SharePoint: en columnas de lista de la biblioteca.
En Jira: en el campo personalizado del ticket adjunto.
En Confluence: en el bloque de aviso de la página.

---

## Restricciones

- No omite la presentación en chat bajo ninguna circunstancia — ni con urgencia declarada por el agente invocador
- No envía a destinos externos si el usuario no ha aprobado el contenido primero
- No asume un destino por defecto — siempre pregunta
- Si el usuario no quiere ningún destino externo, entrega solo por descarga directa y no insiste
- El aviso `Generado_Por_IA` no es eliminable ni ocultable en ningún formato de salida

---

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-24 | Arquitectura APB | Creación — patrón de entrega transversal unificado para todos los agentes del framework |

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 16 del plan APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), esta skill es la responsable de la entrega de artefactos del framework. Aplica marcado completo segun el tipo de cada artefacto entregado: comentario `[IA-GEN]` en codigo/IaC, callout en documentos Markdown, label `ai-generated` en PRs, label `ia-generado` en Jira, footer en emails. Ver estandar completo en AI_MARKING_STANDARD.md.

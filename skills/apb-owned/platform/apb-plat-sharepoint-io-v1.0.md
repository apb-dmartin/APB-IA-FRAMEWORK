---
id: "apb-plat-sharepoint-io-v1.0"
name: "SharePoint Document I/O Skill"
description: "Skill de plataforma para leer documentos de entrada desde SharePoint APB (guías de estilos, políticas, specs funcionales, documentación técnica existente, histórico exportado de Jira) y escribir artefactos de salida generados por el framework (mockups aprobados, informes de riesgos, documentación Word, planes de remediación). Normaliza documentos Office/PDF a Markdown antes de pasarlos a otros agentes/skills."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
inputs:
  - "Operación: leer | escribir | listar | actualizar-metadatos"
  - "Sitio y biblioteca SharePoint (URL relativa o ID de sitio Graph)"
  - "Ruta o nombre del documento dentro de la biblioteca"
  - "Contenido a escribir (Markdown, HTML, o bytes de fichero Office) — solo en operación escribir"
  - "Metadatos a establecer (columnas de lista SharePoint) — opcional"
outputs:
  - "Contenido del documento en Markdown (lectura) — listo para consumir por otros agentes"
  - "Contenido original en bytes si se solicita formato nativo"
  - "URL de acceso directo al documento en SharePoint"
  - "Metadatos del ítem (autor, fecha modificación, versión, columnas personalizadas)"
  - "Confirmación de escritura con ID de ítem y URL"
depends_on:
  - "prov-ms365-v1.0"
  - "apb-plat-doc-to-markdown-v1.0"
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# SharePoint Document I/O Skill

## Propósito

Hace que SharePoint sea un canal bidireccional para el framework: los agentes leen desde
ahí los documentos corporativos que necesitan como input (guías de estilos, políticas,
specs existentes), y depositan en SharePoint los artefactos que generan para que los
equipos puedan acceder a ellos desde su entorno habitual sin necesidad de buscarlos en
el repo de GitHub ni en el chat del agente.

La normalización a Markdown es automática: cualquier documento Word, PDF o Excel que se
lea se convierte a Markdown via `apb-plat-doc-to-markdown-v1.0` antes de pasarse al
agente consumidor. Esto garantiza que todos los componentes del framework trabajen
internamente en texto plano, independientemente del formato de origen.

---

## Bibliotecas SharePoint estándar APB

| Biblioteca | Contenido típico | Operación principal |
|-----------|------------------|---------------------|
| `Arquitectura/Guias-Estilos` | Guía de estilos UI/UX, manual de widgets DevExpress | Lectura |
| `Arquitectura/Politicas` | Políticas corporativas APB (ENS, RGPD, LCSP) | Lectura |
| `Arquitectura/Specs` | Especificaciones funcionales y técnicas de proyectos | Lectura/Escritura |
| `Arquitectura/Artefactos-IA` | Mockups aprobados, informes de riesgos, planes de remediación | Escritura |
| `Proyectos/[Proyecto]/Documentacion` | Documentación funcional y técnica de cada proyecto | Lectura/Escritura |
| `Proyectos/[Proyecto]/Jira-Export` | Exportaciones históricas de Jira para reconstrucción de specs | Lectura |

---

## Prompt de Sistema

```
Eres el skill "SharePoint Document I/O Skill" (apb-plat-sharepoint-io-v1.0)
del APB AI Framework, operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Antes de ejecutar cualquier tarea, carga:
  context/apb/knowledge/APB_KNOWLEDGE_BASE.md  (provider: prov-apb-knowledge-v1.0)

Contiene: negocio portuario, catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS),
integraciones, terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

## Misión
Leer documentos de entrada desde SharePoint APB (guías de estilos, políticas, specs
funcionales, documentación técnica existente, histórico exportado de Jira) y escribir
artefactos de salida generados por el framework (mockups aprobados, informes de riesgos,
documentación Word, planes de remediación). Normalizas documentos Office/PDF a Markdown
antes de pasarlos a otros agentes/skills.

## Inputs Esperados
- Operación: leer | escribir | listar | actualizar-metadatos
- Sitio y biblioteca SharePoint (URL relativa o ID de sitio Graph)
- Ruta o nombre del documento dentro de la biblioteca
- Contenido a escribir (Markdown, HTML, o bytes de fichero Office) — solo en operación escribir
- Metadatos a establecer (columnas de lista SharePoint) — opcional

## Instrucciones
1. Autentica via prov-ms365-v1.0 usando Graph API.
2. Para leer: descarga el fichero, convierte a Markdown con apb-plat-doc-to-markdown-v1.0 si es Office/PDF.
3. Para escribir: convierte el Markdown/HTML al formato de destino y sube al sitio/biblioteca indicados.
4. Para listar: devuelve metadatos de ítems (nombre, autor, fecha, versión, columnas).
5. Para actualizar-metadatos: modifica las columnas de lista sin tocar el contenido del fichero.
6. Devuelve siempre URL directa al documento y metadatos del ítem.

## Restricciones
- Nunca sobreescribas un documento sin confirmar con el agente orquestador.
- Autonomía nivel 1: las escrituras requieren confirmación explícita del flujo.
- No incluyas credenciales: usa siempre prov-ms365-v1.0 para autenticación.

## Formato de Salida
Markdown normalizado (lectura) o confirmación de escritura con URL y ID de ítem (escritura).
```

---

## Flujos de uso típicos

### Flujo 1 — Agente de mockup leyendo guía de estilos

```
[apb-agent-ux-mockup-v1.0]
    → apb-plat-sharepoint-io-v1.0 (leer: Arquitectura/Guias-Estilos/GuiaEstilos_APB_2022.pdf)
    → [normalizado a Markdown via apb-plat-doc-to-markdown-v1.0]
    → [agente usa el Markdown como contexto de estilos corporativos]
    → [genera mockup + prototipo HTML]
    → apb-plat-sharepoint-io-v1.0 (escribir: Arquitectura/Artefactos-IA/mockup-[pantalla]-[fecha].md)
    → apb-plat-ms-notify-v1.0 (notificar: URL del mockup en SharePoint al revisor)
```

### Flujo 2 — Agente de spec leyendo histórico Jira

```
[apb-agent-spec-engineer-v1.0]
    → apb-plat-sharepoint-io-v1.0 (leer: Proyectos/GISPEM/Jira-Export/jira-history-2024.xlsx)
    → [normalizado a Markdown tabla de tickets]
    → [agente genera spec funcional desde el histórico]
    → apb-plat-sharepoint-io-v1.0 (escribir: Proyectos/GISPEM/Documentacion/spec-gispem-v1.md)
```

### Flujo 3 — Agente de documentación escribiendo Word

```
[apb-agent-documentation-v1.0]
    → [genera documentación en Markdown]
    → apb-plat-sharepoint-io-v1.0 (escribir: Proyectos/[X]/Documentacion/manual-[nombre].docx)
    → [metadatos: Generado_Por_IA=Sí, Estado_Revision=Pendiente]
    → apb-plat-ms-notify-v1.0 (entrega disponible al equipo del proyecto)
```

---

## Capacidades

- Lectura de documentos Office/PDF/Markdown desde cualquier biblioteca SharePoint APB autorizada
- Normalización automática a Markdown via `apb-plat-doc-to-markdown-v1.0`
- Escritura de artefactos con metadatos obligatorios de trazabilidad de IA
- Listado y búsqueda de documentos en bibliotecas
- Gestión de versiones: crea nueva versión, no sobreescribe
- Control de tamaño: avisa si el documento supera el umbral de tokens estimados

---

## Dependencias

| Componente | Rol |
|-----------|-----|
| `prov-ms365-v1.0` | Ejecuta las operaciones de lectura/escritura sobre Graph API |
| `apb-plat-doc-to-markdown-v1.0` | Normaliza documentos Office/PDF a Markdown |
| `apb-plat-ms-notify-v1.0` | Notifica la disponibilidad de artefactos escritos |

---

## Restricciones

- Solo opera sobre bibliotecas en el tenant Microsoft 365 APB (`portdebarcelona.cat`)
- No accede a OneDrive personal de usuarios — solo a SharePoint de sitio
- Las operaciones de escritura en producción requieren que el artefacto haya pasado por un `human_review_point` — no escribe borradores no revisados en carpetas de producción
- No elimina documentos — como máximo mueve a carpeta de archivo o crea nueva versión

---

> **Generado por IA:** Claude (Anthropic/Claude Code), Sesión 15 del plan APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Primera linea del fichero generado**: `# [IA-GEN] Generado por APB AI Framework (apb-plat-sharepoint-io-v1.0) - revisar ANTES de aplicar en produccion`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`

NOTA: Para IaC, ningun fichero generado por IA debe aplicarse en produccion sin revision humana explicita.

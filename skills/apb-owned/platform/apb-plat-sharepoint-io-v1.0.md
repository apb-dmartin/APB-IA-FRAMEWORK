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
Eres la skill de I/O de SharePoint del APB AI Framework.

Tu función es ser el puente documental entre SharePoint APB y los agentes del framework:
lees los documentos que los agentes necesitan como input, y escribes los artefactos que
los agentes generan para que los equipos puedan acceder a ellos.

### Al leer un documento (operación: leer)

1. Usa prov-ms365-v1.0 con operación `download_as_bytes` para obtener el fichero.
2. Detecta el formato por extensión: .docx, .pdf, .xlsx, .pptx, .md, .txt.
3. Para ficheros Office/PDF, invoca apb-plat-doc-to-markdown-v1.0 para normalizar a Markdown.
4. Para ficheros .md o .txt, devuelve el contenido directamente sin transformación.
5. Adjunta los metadatos del ítem (autor, fecha, versión de SharePoint) al output,
   para que el agente consumidor pueda citar correctamente la fuente.
6. Si el documento tiene más de 50.000 tokens estimados, avisa al agente invocador
   y ofrece dividir por secciones o devolver solo la tabla de contenidos primero.

### Al escribir un artefacto (operación: escribir)

1. Recibe el contenido en Markdown o en bytes de fichero Office.
2. Si el contenido es Markdown y el destino es una biblioteca configurada para .docx,
   convierte a Word antes de subir (via apb-plat-doc-to-markdown-v1.0 en modo inverso
   si está disponible, o sube el .md directamente con nota de conversión pendiente).
3. Usa prov-ms365-v1.0 con operación `upload_document`.
4. Establece los metadatos mínimos obligatorios:
   - `Generado_Por_IA`: "Sí"
   - `Agente_Origen`: ID del agente que generó el artefacto
   - `Estado_Revision`: "Pendiente de validación humana"
   - `Fecha_Generacion`: fecha ISO actual
5. Devuelve la URL directa al documento subido para incluirla en la notificación
   de entrega (apb-plat-ms-notify-v1.0).

### Al listar documentos (operación: listar)

1. Devuelve nombre, URL, autor, fecha de modificación y metadatos clave de cada ítem.
2. Filtra por extensión si se especifica en los parámetros.
3. Ordena por fecha de modificación descendente por defecto.

### Límites
- No leas ni escribas en bibliotecas fuera de las rutas autorizadas sin confirmación
  explícita del agente invocador y de Arquitectura APB.
- No subas contenido clasificado como RESERVADO sin confirmación de Ciberseguridad APB.
- Si el documento tiene control de versiones activo en SharePoint, no sobreescribas
  la versión actual — crea una versión nueva con el contenido actualizado.
- Siempre establece el metadato `Generado_Por_IA: Sí` en todo documento que suba
  el framework, sin excepción.
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

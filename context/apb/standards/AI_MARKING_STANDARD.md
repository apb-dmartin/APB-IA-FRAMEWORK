---
id: "std-ai-marking-v1.0"
name: "Estándar de Marcado de Artefactos Generados por IA"
version: "1.0.0"
status: "active"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
policy_ref: "POLICY_AI_USAGE_v1.0 §6"
created_date: "2026-06-26"
review_date: "2027-06-26"
---

# Estándar de Marcado de Artefactos Generados por IA

## Propósito

Define el marcado obligatorio que debe incluir **todo artefacto generado o asistido por IA** antes de salir del agente y llegar a su destino (repositorio, Jira, correo, documento). Implementa el §6 de la Política de Uso de IA (`POLICY_AI_USAGE_v1.0`).

**Regla general**: Si la IA lo produce, se marca. Siempre. Sin excepciones.

---

## Tipos de artefacto y marcado requerido

### 1. Código fuente (.cs, .py, .js, .ts, .vb…)

**Comentario en la primera línea del bloque generado:**

```csharp
// [IA-GEN] Generado por APB AI Framework ({skill_id}) — pendiente revisión humana
```

Equivalentes por lenguaje:
- SQL: `-- [IA-GEN] Generado por APB AI Framework ({skill_id}) — pendiente revisión humana`
- YAML / HCL / Dockerfile: `# [IA-GEN] Generado por APB AI Framework ({skill_id}) — pendiente revisión humana`
- HTML/XML: `<!-- [IA-GEN] Generado por APB AI Framework ({skill_id}) — pendiente revisión humana -->`

**Commit asociado:**

El mensaje de commit debe incluir la etiqueta `[ai-gen]` y la línea de co-autoría:

```
[ai-gen] <descripción del cambio>

Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>
```

---

### 2. Pull Requests (GitHub / Azure DevOps)

**Label**: `ai-generated` — añadir al crear el PR.

**Footer obligatorio en la descripción del PR** (antes de cerrar el texto):

```markdown
---
> ⚠️ **Generado por IA** (APB AI Framework — {skill_id}) — revisado y validado por [nombre del revisor] antes de publicar este PR.
```

---

### 3. Tickets Jira (Stories, Tasks, Sub-tasks, Bugs, Epics)

**Label Jira**: `ia-generado` — campo _Labels_ del ticket.

**Footer en descripción del ticket:**

```
---
_Generado por IA (APB AI Framework — {skill_id}). Requiere validación humana antes de ejecutar._
```

---

### 4. Documentos (Markdown, Word, PDF, PPT, OpenAPI/Swagger)

**Documentos Markdown** — callout al inicio del contenido (inmediatamente después del título H1):

```markdown
> ⚠️ **Borrador generado por IA** (APB AI Framework — {skill_id}) — pendiente validación humana. No distribuir sin revisión previa.
```

**Documentos Word / PPT** — pie de página en todas las páginas:

```
[IA-GEN] Generado por APB AI Framework — pendiente validación humana
```

**OpenAPI / Swagger YAML** — campo `info.x-ai-generated` y comentario de cabecera:

```yaml
# [IA-GEN] Generado por APB AI Framework ({skill_id}) — pendiente revisión humana
info:
  x-ai-generated: true
  x-ai-skill: "{skill_id}"
  x-human-reviewer: ""   # rellenar antes de publicar
```

---

### 5. Correos electrónicos y mensajes Teams / Slack

**Footer obligatorio** en el cuerpo del mensaje (última línea):

```
⚠️ Generado por IA (APB AI Framework — {skill_id}) — revisado y enviado por [nombre].
```

---

### 6. Infraestructura como código (Terraform, Bicep, Helm, Docker, CI/CD YAML)

**Comentario en la primera línea del fichero:**

```hcl
# [IA-GEN] Generado por APB AI Framework ({skill_id}) — revisar ANTES de aplicar en producción
```

**Commit:**

```
[ai-gen] <descripción>

Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>
```

> ⚠️ Para IaC el marcado es especialmente crítico: un `terraform apply` sin revisión sobre un fichero IA puede alterar infraestructura en producción.

---

## Resumen rápido de referencia

| Tipo de artefacto | Dónde marcar | Qué añadir |
|-------------------|-------------|-----------|
| Código fuente | Primera línea del bloque generado | Comentario `[IA-GEN]` |
| Commit | Mensaje de commit | `[ai-gen]` + `Co-Authored-By` |
| Pull Request | Descripción + metadata | Footer + label `ai-generated` |
| Ticket Jira | Descripción + metadata | Footer + label `ia-generado` |
| Documento Markdown | Tras el título H1 | Callout ⚠️ |
| Documento Word/PPT | Pie de página | `[IA-GEN]` |
| OpenAPI/Swagger | Cabecera YAML + `info` | `# [IA-GEN]` + `x-ai-generated` |
| Email / Teams | Última línea del cuerpo | Footer ⚠️ |
| IaC (Terraform, Docker…) | Primera línea del fichero | Comentario `[IA-GEN]` |

---

## Cuándo se retira la marca

La marca **no se retira**. Documenta el origen del artefacto de forma permanente para auditoría (POLICY_AI_USAGE §10).

Una vez validado por un técnico senior, el campo `x-human-reviewer` (OpenAPI) o el footer pueden actualizarse con el nombre del revisor y la fecha:

```
✅ Revisado por [nombre] el [fecha] — conforme a POLICY_AI_USAGE_v1.0
```

---

## Skills que implementan este estándar

Todas las skills APB que generan artefactos externos incluyen una sección `## Marcado IA obligatorio` que referencia este documento. Ver también: `apb-plat-deliver-artifact-v1.0` (entrega de artefactos con marcado completo).

---

*Estándar generado por IA (APB AI Framework) — Sesión 23. Requiere aprobación de Arquitectura APB antes de publicación oficial.*

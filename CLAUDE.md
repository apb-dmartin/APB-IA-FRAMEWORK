# APB AI Framework — Instrucciones para agentes IA

> Este fichero es leído automáticamente por Claude Code al abrir el repositorio.
> Su contenido son reglas permanentes que cualquier instancia de IA debe seguir
> al trabajar sobre este repositorio.

---

## Reglas obligatorias

### 1. Marcado de artefactos (POLICY_AI_USAGE §6)

**Toda skill, agente o componente nuevo que genere artefactos de output debe incluir
la sección `## Marcado IA obligatorio (POLICY_AI_USAGE §6)`.**

El estándar completo está en:
`context/apb/standards/AI_MARKING_STANDARD.md`

Resumen rápido de marcado por tipo:

| Artefacto | Marca obligatoria |
|-----------|------------------|
| Código (.cs, .py…) | `// [IA-GEN] Generado por APB AI Framework ({skill_id}) — pendiente revisión humana` |
| SQL | `-- [IA-GEN] ...` |
| YAML / HCL / Dockerfile | `# [IA-GEN] ...` |
| OpenAPI/Swagger | `# [IA-GEN]` + `info.x-ai-generated: true` |
| Commit | Prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>` |
| Pull Request | Label `ai-generated` + footer en descripción |
| Ticket Jira | Label `ia-generado` + footer en descripción |
| Documento Markdown | Callout `> ⚠️ Borrador generado por IA...` tras el título H1 |
| Word / PPT | Pie de página `[IA-GEN] Generado por APB AI Framework` |
| Email / Teams | Footer en última línea del cuerpo |

**Si creas una skill nueva sin esta sección, el validador `validate_repo.py` fallará con ERROR.**

### 2. Autonomía máxima: nivel 1

Ningún agente del framework puede auto-aprobarse ni auto-mergearse.
Toda salida de estado `draft` requiere aprobación humana explícita.

### 3. Sin secretos en ningún fichero

No incluir tokens, passwords, API keys, ni credenciales en ningún fichero del repo.
Usar referencias a Azure Key Vault o variables de entorno.

### 4. Antes de crear una skill nueva

Usar el template `context/apb/templates/SKILL_APB.md`.
Ejecutar `validate_repo.py` antes del commit.

### 5. Commits

Formato: `[tipo]: descripción corta`
- Tipos: `feat`, `fix`, `chore`, `docs`, `refactor`
- Si el commit incluye artefacto generado por IA: añadir prefijo `[ai-gen]`
  y línea `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`

---

*Este fichero es específico de Claude Code. Los mecanismos duraderos de cumplimiento
son `validate_repo.py` (check #13) y los templates en `context/apb/templates/`.*

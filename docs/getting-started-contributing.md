# Guía de Contribución al APB AI Framework

> ⚠️ Borrador generado por IA (APB AI Framework — E-DX1) — pendiente validación humana. No distribuir sin revisión.

Esta guía explica cómo crear un componente nuevo (skill o agente) siguiendo el protocolo
oficial del framework. El proceso es el mismo que sigue `apb-agent-meta-builder-v1.0`
internamente.

---

## 1. Prerrequisitos

- Python 3.10 o superior
- PyYAML instalado: `pip install pyyaml`
- Acceso de escritura al repositorio `APB-IA-FRAMEWORK`
- Git configurado con identidad APB

---

## 2. Antes de crear — discovery obligatorio

**Regla fundamental:** no crear un componente sin verificar primero que no existe ya.

```bash
# Buscar en el catálogo por nombre o dominio
grep -i "nombre-clave" catalog/CATALOG.md

# Buscar en el índice
grep -i "nombre-clave" INDEX.md
```

Si encuentras algo similar, evalúa si es mejor **extender** el componente existente
(cambio de versión minor/patch) o crear uno nuevo con diferenciación clara de responsabilidad.

**Herramienta automatizada:** `apb-agent-meta-builder-v1.0` hace este discovery automáticamente
si lo invocas con el contexto de lo que quieres construir.

---

## 3. Crear una skill nueva

### 3.1 Copiar la plantilla

```bash
cp context/apb/templates/SKILL_APB.md \
   skills/apb-owned/{dominio}/apb-{dominio}-{nombre}-v1.0.md
```

Dominios disponibles: `architecture`, `development`, `qa`, `platform`, `pm`,
`security`, `governance`, `orchestration`, `operation`, `discovery`, `design`,
`documentation`.

### 3.2 Rellenar el frontmatter obligatorio

```yaml
---
id: "apb-{dominio}-{nombre}-v1.0"
name: "Nombre Descriptivo"
description: "Una frase clara que describe QUÉ hace y CUÁNDO se usa."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "{dominio}"
autonomy_level: 1
consumed_by: []          # se rellena cuando un agente la adopte
created_date: "YYYY-MM-DD"
review_date: "YYYY-MM-DD"   # máximo 6 meses desde created_date
---
```

### 3.3 Secciones obligatorias del cuerpo

El validador (`validate_repo.py`) rechazará la skill si faltan:

```markdown
## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| ...   | ...                   | Sí / No           |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al `AI_MARKING_STANDARD`, todo artefacto generado por esta skill debe incluir:

- **Documentos Markdown**: callout inmediatamente tras el título H1:
  > **Borrador generado por IA** (APB AI Framework - apb-{dominio}-{nombre}-v1.0)
- **Código (.cs, .py…)**: `// [IA-GEN] Generado por APB AI Framework ({id}) — pendiente revisión humana`
- **Commits**: prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
```

---

## 4. Crear un agente nuevo

### 4.1 Copiar la plantilla

```bash
cp context/apb/templates/AGENT.md \
   agents/apb-agent-{nombre}-v1.0.md
```

### 4.2 Frontmatter obligatorio

```yaml
---
id: "apb-agent-{nombre}-v1.0"
name: "Nombre del Agente"
description: "Rol y responsabilidad principal del agente."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "{dominio}"
autonomy_level: 1
skills:
  - "apb-skill-a-v1.0"    # IDs exactos de skills que usa
  - "apb-skill-b-v1.0"
subagents: []              # IDs de subagentes si delega trabajo
runtime:
  - "claude"
  - "copilot"
human_review_points:
  - "Revisión de output antes de uso"
created_date: "YYYY-MM-DD"
review_date: "YYYY-MM-DD"
---
```

### 4.3 Sección obligatoria del cuerpo

```markdown
## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al `AI_MARKING_STANDARD`, todo artefacto generado por este agente debe incluir
la marca de origen IA apropiada según el tipo de artefacto.
```

### 4.4 Actualizar el wiring bidireccional

Si el agente usa skills existentes, **también hay que actualizar esas skills**:

```yaml
# En cada skill que el agente usará — añadir el ID del agente en consumed_by:
consumed_by:
  - "apb-agent-{nombre}-v1.0"
```

El validador rechazará wiring unidireccional (skill declara consumidor que no la lista,
o viceversa).

---

## 5. Ejecutar el validador

```bash
PYTHONIOENCODING=utf-8 python scripts/validate_repo.py --strict
```

Criterio de éxito: `exit 0`, `0 errores`. Los 60 warnings de `source_commit: unverified`
en skills de terceros son deliberados y están exentos en modo `--strict`.

Errores comunes y su solución:

| Error | Causa | Solución |
|---|---|---|
| `Falta la sección '## Marcado IA obligatorio'` | Sección ausente | Añadirla conforme a `AI_MARKING_STANDARD.md` |
| `Falta la sección '## ⚠️ Comportamiento ante inputs incompletos'` | Sección ausente | Añadirla con tabla de comportamiento |
| `Referencia rota en 'skills': 'apb-foo-v1.0' no existe` | ID de skill incorrecto | Verificar el ID exacto en `CATALOG.md` |
| `Wiring unidireccional: skill declara 'consumed_by: X'` | Skill y agente no sincronizados | Actualizar `consumed_by` en la skill O `skills` en el agente |

---

## 6. Regenerar el catálogo

```bash
python scripts/generate_catalog.py
```

Actualiza `catalog/CATALOG.md`, `INDEX.md` y `DOMAIN_REGISTRY.md`. El CI bloqueará el PR
si el catálogo no está actualizado.

---

## 7. Abrir el Pull Request

### Formato del commit

```
[ai-gen] feat: añadir apb-{dominio}-{nombre}-v1.0

Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>
```

Tipos de commit: `feat` (nuevo componente), `fix` (corrección), `refactor` (restructuración),
`docs` (solo documentación), `chore` (mantenimiento).

### Checklist antes de crear el PR

- [ ] `validate_repo.py --strict` en verde (exit 0)
- [ ] `generate_catalog.py` ejecutado (sin cambios o con el nuevo componente)
- [ ] Sección `## Marcado IA obligatorio` presente
- [ ] Sección `## ⚠️ Comportamiento ante inputs incompletos` presente
- [ ] Wiring bidireccional correcto (skill y agente sincronizados)
- [ ] `review_date` como máximo 6 meses desde hoy

### Proceso de aprobación

El PR requiere revisión humana explícita. Ningún agente puede auto-aprobarse (`SYSTEM.md §2.1`).
Los componentes salen de `draft` solo tras aprobación documentada en el PR.

---

## 8. Checklist de cierre de sesión

Al terminar cualquier sesión de trabajo en el repo, ejecutar siempre:

```bash
python scripts/generate_catalog.py
PYTHONIOENCODING=utf-8 python scripts/validate_repo.py --strict
python -m unittest tests.test_validate_repo tests.test_behavior_coverage -v
```

Y actualizar `discovery/PLAN_FASES_FUTURAS.md` §J con el estado actual.

Ver protocolo completo en `discovery/PLAN_FASES_FUTURAS.md §J`.

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../context/apb/standards/AI_MARKING_STANDARD.md),
este documento fue generado por el APB AI Framework (E-DX1) y está pendiente de validación
humana por Arquitectura APB antes de ser distribuido.

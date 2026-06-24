# Guía de Contribución al APB AI Framework

> **Versión:** 1.0.0-draft
> **Estado:** draft

---

## Antes de Contribuir

### 1. Revisa el estado del framework

- Consulta `SYSTEM.md` para entender las reglas globales.
- Consulta `GOVERNANCE.md` para entender estados y aprobadores.
- Consulta `catalog/CATALOG.md` para evitar duplicados.

### 2. Discovery de alternativas (OBLIGATORIO para skills APB)

Antes de crear una skill propia (`apb-owned`), debe existir evidencia en `discovery/` de que se han revisado alternativas:

- **MCP oficiales:** GitHub, Azure, Microsoft Learn, DevExpress, Playwright, Sonar, Atlassian, k6.
- **Skills oficiales:** Anthropic Skills, OpenSpec.
- **Comunidad:** skills.sh, Composio, SuperClaude, Mukul Cybersecurity Skills, LightRAG, Graphify, Rowboat, LIDR, UI UX Pro Max.

Plantilla de discovery: `context/apb/templates/DISCOVERY.md`.

### 3. Esquema de metadatos obligatorio

Todo componente debe declarar su frontmatter YAML según `context/apb/SCHEMA.md`.
Ejecuta `python scripts/validate_repo.py` antes de abrir PR; el validador
comprueba el cumplimiento de este esquema, IDs únicos y referencias cruzadas.

---

## Checklist de Pull Request

Todo PR debe cumplir los siguientes criterios:

### Metadatos

- [ ] **ID único** en catálogo (formato: `apb-{dominio}-{nombre}-v{major}.{minor}`).
- [ ] **Nombre** descriptivo y consistente con la convención de nomenclatura.
- [ ] **Descripción** clara del objetivo.
- [ ] **Versión** semántica (ej: 1.0.0-draft).
- [ ] **Propietario** identificado (nombre + email).
- [ ] **Estado:** `draft` salvo aprobación explícita.
- [ ] **Fecha de creación** y **fecha de revisión**.

### Skills

- [ ] **Inputs** definidos (tipo, descripción, obligatoriedad).
- [ ] **Outputs** definidos (tipo, descripción).
- [ ] **Dominio funcional** declarado.
- [ ] **Agentes consumidores** identificados.
- [ ] **Dependencias** declaradas (otras skills, providers, wrappers).
- [ ] **Nivel de autonomía** declarado.
- [ ] **Human review** declarado (quién valida, en qué fase).

### Agentes

- [ ] **Responsabilidad principal** definida.
- [ ] **Skills disponibles** listadas (con referencias al catálogo).
- [ ] **Límites de actuación** documentados.
- [ ] **Puntos de validación humana** asociados y documentados.
- [ ] **Runtime soportado** (Copilot, Claude, ambos).

### Workflows

- [ ] **Objetivo de negocio** definido.
- [ ] **Agentes involucrados** listados.
- [ ] **Secuencia de ejecución** documentada.
- [ ] **Puntos de control humano** identificados.
- [ ] **Nivel de autonomía** del workflow declarado.

### Seguridad y Calidad

- [ ] **Sin secretos ni credenciales** en archivos.
- [ ] **Sin información sensible** (datos personales, IPs internas).
- [ ] **Licencia** declarada (para componentes de terceros).
- [ ] **Análisis de riesgo** (para componentes High/Critical).

### Validación

- [ ] Script de validación ejecutado: `python scripts/validate_repo.py`.
- [ ] Sin errores de estructura.
- [ ] Sin IDs duplicados en catálogo.
- [ ] Sin referencias rotas.

---

## Convenciones de Nomenclatura

### IDs de Skills

```
apb-{dominio}-{nombre}-v{major}.{minor}
```

Ejemplos:
- `apb-dev-code-review-v1.0`
- `apb-qa-test-plan-v1.0`
- `apb-arch-ddd-discovery-v1.0`

### IDs de Agentes

```
apb-agent-{nombre}-v{major}.{minor}
```

Ejemplos:
- `apb-agent-code-reviewer-v1.0`
- `apb-agent-spec-engineer-v1.0`

### IDs de Workflows

```
apb-wf-{nombre}-v{major}.{minor}
```

Ejemplos:
- `apb-wf-legacy-onboarding-v1.0`
- `apb-wf-sdd-full-v1.0`

---

## Proceso de Contribución

1. **Fork/branch** desde `main`.
2. **Crear** el componente siguiendo las plantillas en `templates/`.
3. **Documentar** discovery si es skill APB nueva.
4. **Ejecutar** `python scripts/validate_repo.py`.
5. **Abrir PR** con checklist completo.
6. **Revisión** por pares y aprobadores correspondientes.
7. **Merge** tras aprobación.

---

## Plantillas Disponibles

| Plantilla | Ubicación | Uso |
|-----------|-----------|-----|
| Skill APB | `templates/SKILL_APB.md` | Nueva skill propia |
| Skill Terceros | `templates/SKILL_THIRD_PARTY.md` | Descriptor de skill externa |
| Agente | `templates/AGENT.md` | Nuevo agente |
| Workflow | `templates/WORKFLOW.md` | Nuevo workflow |
| Discovery | `templates/DISCOVERY.md` | Evidencia de revisión de alternativas |

---

## Contacto

- **Dudas técnicas:** arquitectura@portdebarcelona.cat
- **Dudas de gobierno:** arquitectura@portdebarcelona.cat
- **Dudas de seguridad:** albert.prats@portdebarcelona.cat

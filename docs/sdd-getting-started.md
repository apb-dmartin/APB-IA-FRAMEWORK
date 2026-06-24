# Getting Started — Spec Driven Development con el APB AI Framework

> Referenciado desde `README.md` ("Para nuevos proyectos (SDD-Ready)"). Esta
> guía cierra esa referencia, creada en la Sesión 7 del plan de remediación.
> Para la jerarquía completa de conceptos (Capability → Provider → Wrapper →
> Skill → Subagent → Agent → Workflow), ver `README.md` y `SYSTEM.md`.

## 1. Antes de empezar

- Confirma que el repo pasa la validación local:
  ```bash
  pip install pyyaml --break-system-packages
  python3 scripts/validate_repo.py
  ```
  Debe dar `0 errores`. Los warnings restantes están documentados y son
  esperados (ver `discovery/CONTINUIDAD_PROYECTO.md`).
- Lee `context/apb/SCHEMA.md` si vas a crear o editar un componente: es la
  única fuente de verdad sobre el formato de frontmatter YAML.
- Lee `GOVERNANCE.md` si tu cambio afecta a un componente ya `approved` —
  el ciclo de vida y los aprobadores están definidos ahí, no aquí.

## 2. Arrancar un proyecto nuevo (SDD-Ready)

```bash
# 1. Copiar el scaffold SDD-ready a tu nuevo repositorio
cp -r repo-scaffold/sdd-ready/* /ruta/al/nuevo-repo/

# 2. Revisar la estructura propuesta
cat repo-scaffold/sdd-ready/SCAFFOLD_SDD.md
```

El scaffold incluye `docs/system-spec.md` como punto de partida: es el
documento que formaliza la necesidad de negocio antes de generar backlog,
diseño técnico o código (principio de Spec Driven Development, ver
`proyecto.md` §1). No se debe generar código sin que exista primero esta
especificación, un plan técnico o un issue Jira con criterios de aceptación
— es la regla "no vibe coding" (Principio Fundamental #8 del framework).

## 3. El ciclo SDD en la práctica

```
Necesidad de negocio
   │
   ▼  apb-agent-business-analyst-v1.0 / apb-agent-spec-engineer-v1.0
Especificación formal (spec, historias, criterios de aceptación)
   │
   ▼  apb-disc-adversarial-v1.0  (validación adversaria — uso obligatorio)
Especificación robustecida
   │
   ▼  apb-agent-domain-architect-v1.0 / apb-agent-technical-architect-v1.0
Diseño técnico (DDD, APIs, eventos)
   │
   ▼  apb-agent-implementer-v1.0
Código implementado + tests
   │
   ▼  apb-agent-code-reviewer-v1.0          ← segunda línea, independiente del autor
Code review (cumplimiento, seguridad, deuda técnica)
   │
   ▼  Validación humana (Tech Lead / Desarrollador) — obligatoria, Nivel 1 mínimo
Merge
```

Nota la diferencia entre **`apb-agent-implementer-v1.0`** (genera e implementa,
se auto-revisa) y **`apb-agent-code-reviewer-v1.0`** (revisa código ya escrito,
de forma independiente, antes del merge). Ningún agente aprueba sus propios
resultados — ver `GOVERNANCE.md` y `proyecto.md` §3.6 (Supervisión Humana).

## 4. Invocar un agente de forma independiente

No siempre necesitas el ciclo completo. Para listar y consultar agentes
disponibles sin pasar por un workflow:

```bash
# Listar todos los agentes con sus skills y runtimes soportados
python3 scripts/invoke_agent.py --list

# Listar workflows disponibles
python3 scripts/invoke_agent.py --list-workflows

# Ver cómo se invocaría un agente concreto con un input dado
python3 scripts/invoke_agent.py \
  --agent apb-agent-implementer-v1.0 \
  --runtime claude \
  --input '{"spec_reference": "APB-EXP-001"}'
```

`invoke_agent.py` lee el frontmatter real de `agents/` y `workflows/` en cada
ejecución — nunca hay un catálogo hardcodeado que pueda desincronizarse del
repo (ver `scripts/generate_catalog.py` para el mismo principio aplicado a
`catalog/CATALOG.md` e `INDEX.md`).

## 5. Después de implementar: mantener el catálogo sincronizado

Cualquier componente nuevo o modificado (skill, agente, subagente, workflow,
provider, wrapper, adapter) requiere regenerar el catálogo antes de abrir PR:

```bash
python3 scripts/generate_catalog.py          # regenera CATALOG.md, INDEX.md, DOMAIN_REGISTRY.md
python3 scripts/validate_repo.py --strict    # validación completa antes de PR
```

La CI (`.github/workflows/validate.yml`) **bloquea el PR si el catálogo está
desincronizado** — no hay auto-commit. Si el chequeo de drift falla, ejecuta
`generate_catalog.py` localmente y sube el resultado (decisión de gobernanza
registrada en `discovery/CONTINUIDAD_PROYECTO.md`).

## 6. Validar tu propio cambio antes de abrir PR

```bash
python3 scripts/validate_repo.py --strict
python3 -m unittest tests.test_validate_repo -v   # solo si modificaste el propio validador
```

`tests/test_validate_repo.py` no valida el repo real — usa fixtures aislados
en un directorio temporal para comprobar que el validador detecta lo que debe
detectar (parseo de frontmatter, secretos embebidos, referencias rotas,
dependencias circulares). Si tu cambio afecta a `scripts/validate_repo.py`,
estos tests deben seguir pasando.

## 7. Dónde seguir leyendo

| Pregunta | Documento |
|---|---|
| ¿Qué campos lleva el frontmatter de cada tipo de componente? | `context/apb/SCHEMA.md` |
| ¿Quién aprueba qué, y en qué estado puede estar un componente? | `GOVERNANCE.md` |
| ¿Qué es el framework, principios y jerarquía completa? | `README.md`, `SYSTEM.md` |
| ¿Qué dominios funcionales existen y qué skills caen en cada uno? | `DOMAIN_REGISTRY.md` |
| ¿Qué se decidió ya y qué queda pendiente del plan de sesiones? | `discovery/CONTINUIDAD_PROYECTO.md` |
| ¿Cómo creo un componente nuevo paso a paso? | *(pendiente — ver `discovery/PLAN_FASES_FUTURAS.md`, punto 8)* |

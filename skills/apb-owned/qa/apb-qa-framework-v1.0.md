---
id: "apb-qa-framework-v1.0"
name: "QA del APB AI Framework"
description: "Valida la corrección, completitud y coherencia de los componentes del APB AI Framework (agentes, skills, providers, workflows). Verifica que cada componente cumple el SCHEMA.md, que los IDs son únicos, que las dependencias existen y que los campos obligatorios están presentes."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 2
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# QA del APB AI Framework

---

## 🎯 Propósito

Ejecutar la validación de calidad interna del APB AI Framework: verificar que los componentes (agentes, skills, subagentes, providers, workflows) son coherentes entre sí, cumplen el esquema definido en `SCHEMA.md`, no tienen dependencias rotas y están correctamente registrados en el índice `INDEX.md` y el catálogo `CATALOG.md`. Complementa el script de validación automatizado (`scripts/validate.py`) con análisis semántico que no puede automatizarse.

---

## ⚡ Trigger

Cuando se añade un componente nuevo al framework, cuando se modifica uno existente, antes de un release del framework, o periódicamente como auditoría de calidad.

---

## 📥 Input

- Componente o lista de componentes a validar (ficheros `.md` con frontmatter YAML)
- Tipo de validación: individual / batch / pre-release completo
- Contexto: nuevo componente, modificación de existente, auditoría periódica

---

## 📤 Output

- **Informe de validación:** resultado por componente (✅ Válido / ⚠️ Advertencias / ❌ Errores)
- **Lista de errores:** bloqueantes que impiden pasar a estado `candidate`
- **Lista de advertencias:** no bloqueantes pero recomendadas antes de `approved`
- **Componentes con dependencias rotas:** referencias a IDs que no existen en el framework
- **Propuesta de corrección:** texto exacto a modificar en el fichero para cada error

---

## 🔄 Proceso

### Validaciones de esquema (errores bloqueantes)

| Campo | Regla |
|-------|-------|
| `id` | Debe coincidir con el nombre del fichero (sin `.md`). Patrón: `apb-{type}-{name}-v{X}.{Y}` |
| `name` | Presente, no vacío, en español |
| `description` | Presente, 1–3 frases, no vacío |
| `version` | Semver: `X.Y.Z` o `X.Y.Z-draft` |
| `status` | Uno de: `draft`, `candidate`, `under_review`, `approved`, `deprecated`, `retired`, `watchlist`, `rejected` |
| `owner` | Formato `Nombre <email>` |
| `domain` | Debe existir en `DOMAIN_REGISTRY.md` |
| `autonomy_level` | Entero 0–4 |
| `created_date` | Formato `YYYY-MM-DD` |
| `review_date` | Formato `YYYY-MM-DD`, no anterior a `created_date` |

### Validaciones de coherencia (errores bloqueantes)

- Las skills referenciadas en `skills:` de un agente deben existir como ficheros en `skills/`
- Los subagentes referenciados en `subagents:` deben existir en `subagents/`
- Las dependencias en `depends_on:` deben existir en el framework
- Los workflows referenciados deben existir en `workflows/`
- El `id` debe ser único en todo el framework (sin duplicados)
- El runtime declarado debe ser uno de: `copilot`, `claude`

### Validaciones de calidad (advertencias)

- `human_review_points` vacío en agentes con `autonomy_level` ≥ 2 → advertencia
- `status: draft` con `review_date` > 30 días → advertencia (componente estancado)
- Ausencia de sección `## 💡 Ejemplos de Uso` en skills → advertencia
- Ausencia de `## 🔄 Historial de Cambios` en agentes → advertencia
- Descripción < 20 caracteres o > 500 caracteres → advertencia
- Componente no registrado en `INDEX.md` → advertencia (requiere regenerar índice)

### Validaciones semánticas (advertencias de calidad)

- La descripción del componente coincide con su contenido real
- Los `human_review_points` son específicos (no genéricos como "revisión antes de usar")
- Los ejemplos de uso incluyen inputs y outputs concretos, no genéricos
- Los límites y restricciones son precisos y accionables

---

## 📋 Reglas y Constraints

- Los errores bloqueantes impiden que el componente avance a estado `candidate` o superior
- Las advertencias no impiden la promoción pero deben resolverse antes de `approved`
- El script automatizado `scripts/validate.py` cubre las validaciones de esquema y algunas de coherencia; esta skill añade las semánticas
- Autonomía nivel 2: el informe es una propuesta — un miembro de Arquitectura APB revisa y aprueba las correcciones

---

## 🛠 Stack Tecnológico Relevante

- Python (`scripts/validate.py`) — validación automática de esquema
- GitHub Actions (`.github/workflows/validate.yml`) — CI/CD del framework
- `SCHEMA.md` — referencia de esquema
- `DOMAIN_REGISTRY.md` — registro de dominios válidos
- `INDEX.md` — índice auto-generado de componentes

---

## 💡 Ejemplos de Uso

**Ejemplo — Validación de componente nuevo:**
> Nuevo fichero: `agents/apb-agent-incident-support-v1.0.md`

Resultado:
- ✅ `id` coincide con filename
- ✅ `domain: operation` existe en DOMAIN_REGISTRY.md
- ✅ `autonomy_level: 2` con `human_review_points` presentes y específicos
- ⚠️ Skill `apb-sub-ops-oracle-v1.0` referenciada como subagente pero fichero aún no creado → crear o actualizar referencia

**Ejemplo — Auditoría pre-release:**
> 226 componentes validados. Resultado:
> - 0 errores bloqueantes
> - 59 advertencias (todas exentas según política — componentes de terceros sin ejemplos propios)
> - 3 componentes con `review_date` > 60 días → propuesta de revisión

---

## 🔗 Dependencias

- `apb-qa-pipeline-v1.0` — validación del pipeline CI/CD que ejecuta esta skill automáticamente
- `scripts/validate.py` — herramienta de validación automática del framework

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

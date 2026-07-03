# APB AI Framework — Instrucciones para GitHub Copilot

> Este fichero es leído automáticamente por GitHub Copilot (VS Code, Visual
> Studio, JetBrains) al abrir el repositorio. **Es un punto de entrada delgado**:
> las reglas permanentes viven en [`AGENTS.md`](../AGENTS.md), la fuente única
> agnóstica de LLM y de herramienta (`SYSTEM.md §4.3` y `§10.1`). Este fichero
> no debe duplicar ni contradecir `AGENTS.md` — si necesitas cambiar una regla,
> cámbiala allí.

---

**Lee [`AGENTS.md`](../AGENTS.md) antes de trabajar en este repositorio.** Contiene,
entre otras: el estándar de marcado IA obligatorio, el nivel de autonomía por
defecto, la prohibición de secretos en ficheros, el proceso para crear una skill
nueva, la obligación de leer `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` antes
de generar artefactos de negocio, y el formato de commits.

## Específico de GitHub Copilot

- Runtime inicial de referencia del framework (`SYSTEM.md §4.1`): modo por
  defecto **ReadOnly** para providers de acción.
- Contexto de repositorio vía `@workspace` / `@file` / `@terminal`.
- Antes de proponer un commit, verificar `python scripts/validate_repo.py --strict`
  y la suite de tests (`python -m unittest discover tests`).
- Ver `adapters/copilot/adapter-copilot-v1.0.md` para el mapeo detallado de
  capacidades del framework a comandos de chat de Copilot.

---

*Los mecanismos duraderos de cumplimiento son `validate_repo.py` (checks #13 y #22,
este último verifica que este fichero no diverja de `AGENTS.md`) y los templates
en `context/apb/templates/`.*

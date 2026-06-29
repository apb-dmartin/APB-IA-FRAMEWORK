# Template: Skill APB (Propia)

> **Uso:** Crear una nueva skill propia del APB AI Framework.
> **Ubicación:** `skills/apb-owned/{dominio}/`
> **Convención de nombre:** `apb-{dominio}-{nombre}-v{major}.{minor}.md`

---

## 1. Metadatos (Frontmatter Obligatorio)

```yaml
---
id: "apb-{dominio}-{nombre}-v{major}.{minor}"
name: "{Nombre Descriptivo de la Skill}"
description: "Descripción clara y concisa del objetivo de esta skill."
version: "1.0.0-draft"
status: "draft"
owner: "Nombre Apellido <arquitectura@portdebarcelona.cat>"
domain: "{architecture | development | qa | platform | pm | security | governance | orchestration}"
autonomy_level: 1  # 0=Asistencia, 1=Generación con revisión (default), 2=Ejecución supervisada, 3=Automatización controlada, 4=Autorización explícita
created_date: "YYYY-MM-DD"
review_date: "YYYY-MM-DD"
---
```

## 2. Responsabilidad

Describir qué hace esta skill, qué problema resuelve y en qué contexto se aplica.

> **Ejemplo:** Esta skill analiza código C#/.NET para detectar violaciones de estándares corporativos APB, sugerir refactorizaciones y generar un informe estructurado.

## 3. Inputs

| Nombre | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `input_1` | string | Sí | Descripción del input 1 |
| `input_2` | text | No | Descripción del input 2 |
| `input_3` | file_path | Sí | Ruta al archivo o directorio |
| `input_4` | enum | No | Valores permitidos: `A`, `B`, `C` |

## 4. Outputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `output_1` | markdown | Descripción del output 1 |
| `output_2` | json | Descripción del output 2 |
| `output_3` | file_path | Ruta al artefacto generado |

## 5. Dependencias

| Tipo | ID | Descripción |
|------|-----|-------------|
| skill | `apb-{dominio}-{nombre}-v{major}.{minor}` | Skill requerida |
| provider | `{nombre}-provider` | Provider de conocimiento/acción |
| wrapper | `{nombre}-wrapper` | Wrapper APB sobre tercero |

## 6. Prompt del Sistema (System Prompt)

```
Eres el skill "{NOMBRE_SKILL}" del APB AI Framework.

## Contexto
{Descripción del contexto corporativo, estándares aplicables, stack tecnológico.}

## Instrucciones
1. {Instrucción 1}
2. {Instrucción 2}
3. {Instrucción 3}

## Restricciones
- No generes código sin una spec o issue Jira de referencia.
- No incluyas secretos ni credenciales en ningún output.
- Respeta los estándares corporativos APB sobre recomendaciones del modelo.
- Todo output debe ser trazable: agente, skill, prompt, usuario, fecha.

## Formato de Salida
{Especificar formato esperado: markdown estructurado, JSON, tabla, etc.}

## Ejemplos
### Ejemplo 1: {Caso típico}
Input: ...
Output: ...

### Ejemplo 2: {Caso límite}
Input: ...
Output: ...
```

## 7. Agentes Consumidores

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-{nombre}-v{major}.{minor}` | {Cuándo y cómo usa este agente la skill} |

## 8. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | {Rol} | {Validación de inputs, aprobación de scope} |
| Post-ejecución | {Rol} | {Revisión de outputs, aprobación de entregables} |

## 9. Riesgo y Clasificación

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `Low` / `Medium` / `High` / `Critical` |
| Impacto en producción | {Descripción} |
| Medidas compensatorias | {Si aplica} |

## 10. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | YYYY-MM-DD | @autor | Creación inicial |

---

## ⚠️ Comportamiento ante inputs incompletos

> Documentar el comportamiento para CADA input declarado en la sección 3.
> El agente NUNCA debe continuar con inputs obligatorios vacíos o contradictorios sin indicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `{input_obligatorio_1}` | Pregunta: "{pregunta concreta al usuario}" | Sí |
| `{input_obligatorio_2}` | Pregunta: "{pregunta concreta al usuario}" | Sí |
| `{input_opcional_1}` | Asume valor por defecto `{valor}` — lo indica explícitamente | No |
| `{input_ambiguo}` | Presenta las interpretaciones posibles y solicita confirmación | Según caso |

---

## 11. Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA.

<!-- INSTRUCCIÓN: sustituir {tipo} y {sid} por los valores de esta skill -->
<!-- Tipos disponibles: code | sql | openapi | pr | jira | doc | doc_word | email | iac -->

**Tipo de artefacto principal:** {tipo}

- **{Formato de marcado}** — {descripción según AI_MARKING_STANDARD para el tipo elegido}
- **Commit** — prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>` _(si aplica)_

> Ver ejemplos completos en `context/apb/standards/AI_MARKING_STANDARD.md`.

---

## Checklist de Creación

- [ ] Metadatos completos en frontmatter.
- [ ] Inputs y outputs definidos con tipos.
- [ ] Prompt del sistema claro y contextualizado.
- [ ] Dependencias declaradas.
- [ ] Agentes consumidores identificados.
- [ ] Puntos de human review documentados.
- [ ] Nivel de autonomía declarado.
- [ ] Sin secretos ni información sensible.
- [ ] Discovery de alternativas documentado (si es skill APB nueva).
- [ ] **Sección `## Marcado IA obligatorio` completada** (POLICY_AI_USAGE §6).
- [ ] **Sección `## ⚠️ Comportamiento ante inputs incompletos` completada** con tabla para CADA input obligatorio.
- [ ] Script `validate_repo.py` ejecutado sin errores.

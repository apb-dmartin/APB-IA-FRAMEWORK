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
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB — obligatorio en todas las skills
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
| provider | `prov-apb-knowledge-v1.0` | **Obligatorio.** Contexto corporativo APB: negocio portuario, aplicaciones, integraciones, terminología. Leer al inicio de cada ejecución. |
| skill | `apb-{dominio}-{nombre}-v{major}.{minor}` | Skill requerida (eliminar si no aplica) |
| provider | `{nombre}-provider` | Provider adicional (eliminar si no aplica) |
| wrapper | `{nombre}-wrapper` | Wrapper APB sobre tercero (eliminar si no aplica) |

## 6. Prompt de Sistema

> **Obligatorio.** Este bloque es lo que el LLM recibe al ejecutar la skill.
> Debe funcionar con cualquier modelo (Claude, Copilot, GPT-4, etc.).
> Estructura fija: Identidad → Contexto APB → Misión → Inputs → Instrucciones → Restricciones → Formato.

```
Eres el skill "{NOMBRE_SKILL}" ({ID_SKILL}) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md

## Misión
{Descripción concisa de qué hace esta skill y cuándo se usa.
Una o dos frases directas. Sin redundar con la identidad.}

## Inputs Esperados
{Lista los inputs obligatorios y opcionales con su propósito.
Ejemplo:
- repo_path (obligatorio): ruta al repositorio a analizar
- scope (opcional, default "full"): "full" | "changed-files" | "single-file"}

## Instrucciones
1. {Paso 1 — acción concreta}
2. {Paso 2}
3. {Paso 3}
...
N. Emitir TELEMETRY_BLOCK al finalizar (skill_id, user, timestamp, resultado).

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Sin código sin spec o issue Jira de referencia.
- Autonomy Level {N}: todo output es borrador — el humano aprueba antes de aplicar.
- Trazabilidad: skill_id + usuario + fecha en todo output.

## Formato de Salida
{Especificar: markdown estructurado / JSON / tabla / código / fichero.
Ejemplo: "Markdown con secciones H2: Resumen, Hallazgos (tabla), Recomendaciones, Próximos pasos."}
```

## 7. Comportamiento ante Inputs Incompletos

> El LLM NUNCA debe continuar con inputs obligatorios vacíos. Documentar aquí la respuesta para cada input.

| Input | Si falta o es ambiguo | Bloquea |
|-------|----------------------|---------|
| `{input_obligatorio_1}` | Pregunta: "{pregunta concreta al usuario}" | Sí |
| `{input_obligatorio_2}` | Pregunta: "{pregunta concreta al usuario}" | Sí |
| `{input_opcional_1}` | Asume `{valor_default}` — lo indica explícitamente | No |

## 8. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | {Rol} | Validación de inputs, aprobación de scope |
| Post-ejecución | {Rol} | Revisión de outputs, aprobación antes de aplicar |

## 9. Riesgo

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `Low` / `Medium` / `High` / `Critical` |
| Impacto en producción | {Descripción} |
| Medidas compensatorias | {Si aplica} |

## 10. Agentes que Usan esta Skill

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-{nombre}-v{major}.{minor}` | {Cuándo y cómo} |

## 11. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | YYYY-MM-DD | @autor | Creación inicial |

---

## ⚠️ Marcado IA Obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA.

**Tipo de artefacto principal:** {code | sql | openapi | pr | jira | doc | doc_word | email | iac}

- **{Formato de marcado}** — {descripción según AI_MARKING_STANDARD para el tipo elegido}
- **Commit** — prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>` _(si aplica)_

---

## Checklist de Creación

- [ ] Frontmatter completo con `depends_on: prov-apb-knowledge-v1.0`.
- [ ] Secciones 2–4 (Responsabilidad, Inputs, Outputs) completas.
- [ ] **Sección 6 Prompt de Sistema completa** — las 7 subsecciones: Identidad, Contexto APB, Misión, Inputs, Instrucciones, Restricciones, Formato.
- [ ] Sección 7 (Comportamiento ante inputs incompletos) con tabla para CADA input obligatorio.
- [ ] Sección 8 (Human Review) con al menos punto de revisión post-ejecución.
- [ ] Sin secretos ni información sensible en ninguna sección.
- [ ] **Sección Marcado IA completada** (POLICY_AI_USAGE §6).
- [ ] Script `validate_repo.py` ejecutado sin errores.

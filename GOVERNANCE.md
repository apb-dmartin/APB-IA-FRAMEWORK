# Gobierno del APB AI Framework

> **Versión:** 1.0.0-draft
> **Estado:** draft
> **Propietario:** Arquitectura APB / Gobierno TI
> **Fecha revisión:** 2026-06-21

---

## 1. Estados de Componentes

El estado de todo componente (capability, provider, wrapper, skill, subagent, agent, workflow) se declara **exclusivamente como metadato** en frontmatter, catálogo o descriptor. **Nunca como carpeta o ruta de archivo.**

### 1.1 Estados Permitidos

| Estado | Código | Significado | Transiciones permitidas |
|--------|--------|-------------|------------------------|
| **Draft** | `draft` | Definido, no aprobado. Estado por defecto. | → candidate, → rejected |
| **Candidate** | `candidate` | Apto para piloto controlado. | → under_review, → draft |
| **Under Review** | `under_review` | En revisión formal por aprobadores. | → approved, → draft, → rejected |
| **Approved** | `approved` | Aprobado por responsables humanos. | → deprecated, → draft |
| **Deprecated** | `deprecated` | Sustituido, no recomendado para nuevos usos. | → retired, → draft |
| **Retired** | `retired` | Retirado, no disponible. | — |
| **Watchlist** | `watchlist` | Observado, no consumible hasta nueva evaluación. | → draft, → rejected |
| **Rejected** | `rejected` | Descartado tras evaluación. | — |

### 1.2 Diagrama de Transiciones

```
 ┌─────────────┐
 │ draft │ ←── Estado inicial
 └──────┬──────┘
 │
 ┌───────────────┼───────────────┐
 ▼ ▼ ▼
 ┌─────────────┐ ┌─────────────┐ ┌──────────┐
 │ candidate │ │ watchlist │ │ rejected │
 └──────┬──────┘ └──────┬──────┘ └──────────┘
 │ │
 ▼ ▼
 ┌─────────────┐ (a draft)
 │under_review │
 └──────┬──────┘
 │
 ┌─────┴─────┐
 ▼ ▼
┌─────────┐ ┌─────────┐
│approved │ │ rejected│
└────┬────┘ └─────────┘
 │
 ▼
┌───────────┐
│ deprecated│
└─────┬─────┘
 │
 ▼
┌─────────┐
│ retired │
└─────────┘
```

---

## 2. Aprobadores Humanos

### 2.1 Matriz de Responsabilidades

| Ámbito | Responsable de Validación | Escalado |
|--------|---------------------------|----------|
| **Arquitectura** | Arquitecto de Solución / Arquitecto de Referencia | Arquitecto Enterprise |
| **Docks / Plantillas** | Arquitecto de Referencia | Arquitectura |
| **Cloud / Infraestructura** | Arquitecto Cloud | Arquitectura Enterprise |
| **APIs / Eventos** | Arquitecto de Integración | Arquitectura |
| **DDD / Dominios** | Arquitecto de Solución | Arquitectura Enterprise |
| **QA / Calidad** | QA Lead / Gobierno QA | Dirección QA |
| **Ciberseguridad** | Security Architect / CISO | CISO |
| **Funcional / Negocio** | Product Owner / Analista Funcional | Responsable de Producto |
| **Operaciones / SRE** | SRE Lead / Responsable de Operaciones | Dirección de Operaciones |
| **Despliegue / Release** | PMO / Operaciones / Arquitectura | Dirección de Proyecto |

### 2.2 Reglas de Aprobación

1. **Ningún agente puede aprobar** un componente o excepción.
2. **Dos ojos:** Para componentes `approved`, se requiere al menos dos aprobadores de ámbitos distintos.
3. **Escalado automático:** Si un aprobador no responde en 5 días hábiles, el componente pasa a `watchlist` y se escala.
4. **Revisión periódica:** Los componentes `approved` se revisan cada 6 meses.

---

## 3. Ciclo de Vida de Componentes

### 3.1 Alta

1. El autor crea el componente en estado `draft`.
2. Completa metadatos: ID único, nombre, descripción, versión, propietario, inputs/outputs (skills), responsabilidades (agentes).
3. **Aplica los Principios Fundamentales #11 (disciplina de codificación agéntica) y #12 (normalización a Markdown)** del `README.md` — obligatorio para todo componente nuevo, generado tanto por humanos como por `apb-agent-meta-builder-v1.0` (Sesión 10).
4. **Incluye telemetría de invocación (Principio #13 — Sesión 17):** todo componente nuevo (skill, agente, subagente, workflow) debe:
   - Declarar `apb-ops-telemetry-emit-v1.0` en su campo `depends_on` (skills) o `skills` (agentes).
   - Producir un bloque `TELEMETRY_BLOCK` al final de su output siguiendo el esquema de `apb-ops-telemetry-emit-v1.0`.
   - Los ~226 componentes anteriores a la Sesión 17 recibirán este requisito retroactivamente en la Fase #43 (última fase del plan).
5. Ejecuta `python scripts/validate_repo.py`.
6. Abre PR con checklist de `CONTRIBUTING.md`.

### 3.2 Modificación

1. Todo cambio en un componente `approved` genera una nueva versión y pasa a `under_review`.
2. Los cambios menores (typos, clarificaciones) pueden pasar directamente con un solo aprobador.
3. Los cambios mayores (nueva funcionalidad, cambio de inputs/outputs) requieren revisión completa.

### 3.3 Validación

1. Revisión técnica por pares.
2. Revisión de arquitectura (si aplica).
3. Revisión de QA (si aplica).
4. Revisión de ciberseguridad (si aplica).
5. Pruebas de funcionamiento (para skills y agentes).

### 3.4 Publicación

1. El componente pasa a `approved`.
2. Se registra en `catalog/CATALOG.md`.
3. Se notifica a los equipos consumidores.

### 3.5 Retirada

1. Un componente se marca como `deprecated` cuando existe alternativa aprobada.
2. Tras 3 meses en `deprecated`, pasa a `retired`.
3. Los componentes `retired` se mantienen en el catálogo con referencia histórica pero no son consumibles.

---

## 4. Componentes de Terceros

### 4.1 Principios

- **No se copia** código ni prompts propietarios de terceros.
- **No se modifica** código de terceros salvo autorización legal expresa.
- Se registran mediante **descriptor** (`SKILL.md`, `PROVIDER.md`, `FRAMEWORK.md`).
- Se documenta: versión/commit, licencia, fuente, wrapper APB.

### 4.2 Checklist de Integración

- [ ] Licencia compatible con uso interno APB.
- [ ] Análisis de seguridad del componente.
- [ ] Pin de versión o commit específico.
- [ ] Wrapper APB creado (si aplica).
- [ ] Documentación de uso en `discovery/`.
- [ ] Registro en catálogo.

**Pin sin acceso verificado:** si en el momento de la integración no se
dispone de acceso de red al repositorio de origen para confirmar el SHA
exacto, se admite `source_commit: "unverified"` junto con
`verified_date: "YYYY-MM-DD"` (fecha de la revisión manual del contenido).
Este estado es **temporal**: debe refinarse a un commit/tag real en cuanto
se disponga de acceso (`git ls-remote <repo> HEAD` o `git log -1`), y
`scripts/validate_repo.py` lo señala como pendiente hasta entonces.

**Efecto en `validate_repo.py --strict` (decisión Sesión 7):** el warning de
`source_commit: "unverified"` está explícitamente **exento** del modo
estricto — no bloquea el merge en CI. Cualquier otro warning (carpeta
ausente, referencia rota en el cuerpo del documento, drift de catálogo) sí
bloquea sin excepción. Razón: exigir SHA real sin acceso de red bloquearía
la integración de terceros indefinidamente por una causa ajena al autor del
PR, lo que en la práctica empujaría a inventar SHAs falsos — el riesgo que
esta misma política busca evitar.

---

## 5. Gestión de Secretos

### 5.1 Secret Provider Corporativo

**Azure Key Vault** es la única fuente maestra de secretos.

### 5.2 Reglas

- **Prohibido:** Almacenar secretos en repositorios, prompts, skills, catálogos o documentación.
- **Permitido:** Referencias a Azure Key Vault (ej: `{{secrets.apb-keyvault.nombre-secreto}}`).
- **GitHub Secrets** puede cachear referencias para CI/CD, pero no es fuente maestra.
- Los adaptadores de runtime deben resolver secretos mediante el Secret Provider, nunca hardcodeados.

### 5.3 Rotación

- Los secretos se rotan cada 90 días.
- El framework no gestiona la rotación, solo consume secretos mediante referencias.

---

## 6. Métricas y Seguimiento

### 6.1 Indicadores de Gobierno

| Indicador | Objetivo | Frecuencia |
|-----------|----------|------------|
| Componentes en `draft` | < 30% del total | Mensual |
| Tiempo medio de aprobación | < 10 días hábiles | Mensual |
| Excepciones activas | < 5% de proyectos | Trimestral |
| Reutilización de skills | > 50% skills corporativas | Trimestral |
| Incidencias atribuibles a IA | < 2% del total | Mensual |

### 6.2 Auditoría

- Toda actividad de agentes se registra con: agente, skill, prompt, usuario, resultado, validaciones.
- Los logs se almacenan en el repositorio de evidencias del proyecto.
- Revisión trimestral por Gobierno TI.

---

## 7. Proceso de Deprecación

Cuando un componente (skill, agente, subagente, workflow o provider) queda obsoleto,
duplicado o es reemplazado por uno mejor, se sigue este proceso formal:

### 7.1 Quién puede proponer

Cualquier miembro del equipo de Arquitectura APB o propietario declarado en `owner:`.

### 7.2 Quién aprueba

Arquitectura APB — mínimo 1 revisor humano con acceso de escritura al repositorio.
La aprobación debe quedar documentada en el Pull Request.

### 7.3 Plazos de aviso

| Situación | Plazo mínimo de aviso |
|---|---|
| Skill con `consumed_by` activo (agentes consumidores) | 30 días antes de deprecar |
| Consolidación urgente aprobada explícitamente por Arquitectura | Sin plazo mínimo — documentar en `deprecated_reason` |
| Skill sin consumidores (`consumed_by: []`) | Sin plazo mínimo |

### 7.4 Pasos técnicos obligatorios

1. Cambiar `status: deprecated` en el frontmatter YAML.
2. Añadir `deprecated_reason:` con la motivación y fecha: `"Reemplazado por X (decisión Arquitectura APB YYYY-MM-DD)"`.
3. Limpiar `consumed_by: []` — los agentes consumidores deben actualizarse antes o en el mismo commit.
4. Actualizar el wiring de todos los agentes que la listaban en `skills:` para referenciar el sucesor.
5. Ejecutar `python scripts/validate_repo.py --strict` — debe salir con código 0 antes del commit.

### 7.5 Paso a `retired`

Un componente pasa de `deprecated` a `retired` cuando:
- Han transcurrido ≥ 90 días desde la deprecación sin incidencias asociadas.
- El equipo propietario confirma que ningún proyecto activo la referencia.

El cambio a `retired` se ejecuta mediante PR con el mismo proceso de aprobación.

### 7.6 Referencia de marcado

Los artefactos generados por el componente sucesor deben incluir el marcado de IA
conforme a `context/apb/standards/AI_MARKING_STANDARD.md`.

---

## 8. Disciplina operacional del harness

> Complementa `SYSTEM.md §10` (Harness Engineering). Agnóstico de LLM y de
> herramienta: estas reglas gobiernan la *infraestructura*, no el modelo.

### 8.1 Pass-State Gating

- Toda tarea/funcionalidad gestionada como Feature List tiene un **comando de
  verificación** declarado.
- **Solo el harness** (tras ejecutar ese comando con éxito) marca el estado
  `passing`. **El agente no puede declarar victoria por sí mismo.**
- Coherente con `SYSTEM.md §6` (Human Review) y con la prohibición #5 del
  `PROMPTING_STANDARD` ("no declares completado sin verificación").

### 8.2 Validación de 3 capas

| Capa | Qué detecta | En este repo |
|---|---|---|
| 1. Sintaxis / estático | Errores de forma, tipos, esquema | `validate_repo.py --strict` (frontmatter, IDs, wiring) |
| 2. Comportamiento | Errores de lógica unitaria | `tests/` (unittest) + Golden Output Tests |
| 3. Sistema / E2E | Defectos en los límites entre componentes | Verificación end-to-end de cierre de sesión (plan de fases §J) |

Los mensajes de error deben ser **"bolígrafo rojo"**: no genéricos, con
instrucción de corrección concreta (qué archivo, qué sección, cómo arreglarlo).

### 8.3 Clean State Handoff (cierre de sesión)

Al final de cada sesión de trabajo se garantizan las **5 dimensiones**:

1. **Build:** el repo valida sin errores (`--strict` exit 0).
2. **Tests:** todos pasan — nuevos y antiguos.
3. **Progreso:** el estado persistente está actualizado **con evidencia**
   (CONTINUIDAD / PROGRESS / plan de fases).
4. **Artefactos:** sin logs de debug ni ficheros temporales.
5. **Inicio:** la ruta de inicialización estándar funciona para la siguiente sesión.

**Bucle de limpieza periódico:** sesiones rutinarias para reducir deuda del
harness y **eliminar componentes ya innecesarios** por mejoras del modelo.

### 8.4 Separación de roles (insumo para orquestación, punto #77)

La arquitectura de 3 agentes — **Planner** (coordina), **Generator** (trabaja),
**Evaluator** (verifica) — se adopta como principio: quien genera nunca es quien
verifica. Su implementación ejecutable queda para la sesión de Orquestación (#77).

---

## 9. Referencias

- `SYSTEM.md` — Reglas globales y comportamiento del framework (incl. §10 Harness).
- `CONTRIBUTING.md` — Guía de contribución y checklist de PR.
- `catalog/CATALOG.md` — Catálogo centralizado de componentes.
- `context/apb/policies/` — Políticas corporativas aplicables.
- `context/apb/SCHEMA.md` — Esquema de metadatos YAML obligatorio para todo componente.
- `context/apb/standards/PROMPTING_STANDARD.md` — Estándar de estructura de prompt de componentes.

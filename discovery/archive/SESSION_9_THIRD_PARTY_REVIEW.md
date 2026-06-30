# Sesión 9 — Terceros: Patrón de Listas Curadas + Revisión `proyecto.md` §8

> Estado: EJECUTADO. Alcance acotado al cruce de las 34 URLs de §8 de
> `proyecto.md` contra los `source_repo` reales de los descriptores
> existentes, definición de patrón para listas curadas, e incorporación de
> 8 skills concretas de valor confirmado para el stack APB.

## 1. Punto de partida

Al inicio de esta sesión, el repositorio (zip de Sesión 8) tenía **44
skills de terceros** repartidas en 18 carpetas de ecosistema bajo
`skills/third_party/`. `proyecto.md` §8 lista 34 URLs de repositorios de
referencia como insumo para evaluación de terceros, sin que existiera
hasta ahora un cruce sistemático entre ambas listas.

## 2. Cruce de cobertura (34 URLs de §8)

| Categoría | Cantidad | Tratamiento |
|---|---|---|
| Ya incorporadas antes de Sesión 9 | 10 | — |
| Listas curadas puras (sin contenido propio) | 4 (`ComposioHQ/awesome-claude-plugins`, `ComposioHQ/awesome-claude-skills`, `hesreallyhim/awesome-claude-code`, `skills.sh/.../find-skills`) | **Patrón A**: documentadas en este informe, sin componente de catálogo |
| Mega-agregadores con contenido real (no listas) | 2 (`sickn33/antigravity-awesome-skills`, `davila7/claude-code-templates`) | Evaluación puntual de skills, sin instalar el agregador — ver §4 |
| Guía/producto sin skill instalable | 2 (`anthropics/claude-code`, `Piebald-AI/claude-code-system-prompts`) | Sin incorporación — referencia, no contenido de catálogo |
| Guía con valor de gobernanza (no skill) | 1 (`FlorianBruniaux/claude-code-ultimate-guide`) | Anotado como candidato a insumo de `POLICY_VULNERABILITY_MANAGEMENT_v1.1.md` — no incorporado, pendiente decisión Debora |
| Sin evaluar a fondo en esta sesión | 4 (`ComposioHQ/agent-orchestrator` vía `AgentWrapper`, `ruvnet/ruflo`, `affaan-m/ecc`, `nexu-io/open-design`) | Pendiente — anotado en `PLAN_FASES_FUTURAS.md` #27 |
| Otros (producto Anthropic, herramienta de uso) | 11 | Sin acción — no son repos de skills a incorporar (`anthropics/claude-code` como producto, `ryoppippi/ccusage` ya cubierto, etc.) |

## 3. Patrón confirmado por Debora para listas curadas (meta-repos)

**Decisión:** las listas curadas que únicamente enlazan a otros repos de
skills, sin contenido ejecutable propio, se documentan como fuente de
descubrimiento para búsquedas futuras (este documento), sin crear ningún
descriptor `third-*.md` ni wrapper. Razón: crear un descriptor de skill
para un índice de enlaces no aporta nada invocable — sería un componente
de catálogo sin lógica funcional propia.

Listas confirmadas bajo este patrón:
- `ComposioHQ/awesome-claude-plugins`
- `ComposioHQ/awesome-claude-skills`
- `hesreallyhim/awesome-claude-code`
- `skills.sh/vercel-labs/skills/find-skills` (herramienta de búsqueda, no
  lista estática, pero mismo tratamiento: sin contenido ejecutable propio)

**Reversibilidad:** si en el futuro se decide que alguna de estas listas
merece visibilidad directa en el catálogo (p. ej. como wrapper de
descubrimiento), es una ampliación trivial sobre este documento — no hay
trabajo perdido al optar por no incorporarlas ahora.

## 4. Hallazgo: dos repos mal clasificados inicialmente como "lista curada"

Durante la inspección directa (no solo lectura de README), se detectó que
dos repos de §8 **no son listas de enlaces** sino agregadores instalables
con contenido real embebido:

### `sickn33/antigravity-awesome-skills`
- 1.682+ skills empaquetadas, organizadas en `plugins/` por categoría
  (bundles temáticos: Azure/IA, DDD/evented architecture, secure app
  builder, QA/test automation, entre otros).
- Instalable vía `npx antigravity-awesome-skills`.
- El repo documenta en `docs/maintainers/security-findings-triage-*.md`
  hallazgos de seguridad históricos ya resueltos — **sobre el tooling de
  instalación** (scripts npm, app web), no sobre el contenido de las
  `SKILL.md` individuales.
- `docs/SOURCES.md` / `docs/sources/sources.md` documentan atribución
  externa solo para un subconjunto de skills; las evaluadas en esta sesión
  no aparecen en esa tabla (autoría `self`/`community` sin fuente de
  terceros adicional declarada más allá de la licencia MIT del repo
  contenedor).
- **Decisión aplicada:** no se instala el paquete npm como dependencia del
  framework APB. Se evalúa y adapta únicamente el contenido textual de
  skills puntuales con valor confirmado para el stack APB.

### `davila7/claude-code-templates`
- Pese al nombre ("templates"), contiene un agregador de skills bajo
  `cli-tool/components/skills/`, con categorías por dominio técnico
  (incluye `development/dotnet-backend`, `development/csharp-pro`,
  relevantes para el stack .NET 8/C# de APB).
- Mismo tratamiento: no se instala como dependencia, se evalúa contenido
  puntual.

## 5. Las 8 skills incorporadas

Decisión de Debora: "incorpora todas las de C" (bloque C = skills
concretas detectadas dentro de los agregadores, propuestas en el análisis
previo de esta misma sesión).

| ID del descriptor | Origen | Dominio | Relevancia confirmada para APB |
|---|---|---|---|
| `third-davila7-dotnet-backend-v1.0` | davila7/claude-code-templates | development | Alta — único contenido de terceros específico de ASP.NET Core 8+/EF Core hasta ahora |
| `third-davila7-csharp-pro-v1.0` | davila7/claude-code-templates | development | Media — checklist genérico de C# moderno, complemento de revisión |
| `third-sickn33-saga-orchestration-v1.0` | sickn33/antigravity-awesome-skills | architecture | Media-alta — patrón táctico no cubierto por skills propias de DDD |
| `third-sickn33-event-store-design-v1.0` | sickn33/antigravity-awesome-skills | architecture | Media-alta — menciona Marten (.NET) explícitamente en el original |
| `third-sickn33-ddd-context-mapping-v1.0` | sickn33/antigravity-awesome-skills | architecture | Media — complementa `apb-disc-ddd-legacy-v1.0` sin solapar |
| `third-sickn33-domain-driven-design-v1.0` | sickn33/antigravity-awesome-skills | architecture | Media — útil como test de viabilidad DDD, reenrutado a componentes APB reales |
| `third-sickn33-auth-implementation-patterns-v1.0` | sickn33/antigravity-awesome-skills | security | Media — catálogo de patrones auth, requiere traducción TypeScript→.NET |
| `third-sickn33-django-access-review-v1.0` | sickn33/antigravity-awesome-skills | qa | **Alta** — directamente aplicable al stack GIS Django/DRF/GeoDjango de APB |
| `third-sickn33-screen-reader-testing-v1.0` | sickn33/antigravity-awesome-skills | qa | **Alta** — cubre gap real: WCAG 2.1 AA es requisito explícito sin skill previa dedicada |

### 5.1 Adaptaciones aplicadas (no copia literal)

- **`dotnet-backend`**: ejemplos originales en PostgreSQL/Hangfire
  sustituidos conceptualmente por Azure SQL/Azure Service Bus (estándares
  corporativos APB) en la sección "Adaptaciones APB" de cada descriptor.
- **`saga-orchestration`**, **`auth-implementation-patterns`**: código de
  ejemplo original en Python/TypeScript; descriptor señala explícitamente
  que requiere traducción a .NET antes de uso directo, sin reescribir el
  código completo en esta sesión (alcance de un descriptor es documentar
  el patrón adaptado, no generar la librería .NET completa).
- **`ddd-context-mapping`**, **`domain-driven-design`**: el original
  referenciaba 6 skills hermanas del mismo bundle (`@ddd-strategic-design`,
  `@projection-patterns`, `@cqrs-implementation`, etc.) inexistentes en
  APB. El mapa de enrutamiento se **reescribió por completo** hacia
  componentes APB reales (`apb-disc-ddd-legacy-v1.0`, las propias skills
  `sickn33` incorporadas hoy, `apb-arch-api-contract-v1.0`) en vez de
  copiar referencias rotas.
- **`django-access-review`**: única skill con doble atribución — MIT
  (repo contenedor) + OWASP Cheat Sheet Series CC BY-SA 4.0 (citado
  explícitamente en el fichero de origen). Ambas licencias declaradas en
  el descriptor.

## 6. Correcciones de validación durante la sesión

Tras la creación inicial de los 8 descriptores, `validate_repo.py --strict`
detectó 4 referencias a IDs de subagentes/workflows con nomenclatura
obsoleta (anterior al renombrado de Sesión 8), introducidas por error de
redacción propio al citar consumidores naturales de cada skill:

| Referencia incorrecta escrita | ID real corregido | Fichero afectado |
|---|---|---|
| `apb-sub-django-v1.0` | `apb-sub-dev-django-v1.0` | `third-sickn33-django-access-review-v1.0.md` |
| `apb-sub-security-v1.0` | `apb-sub-qa-security-v1.0` | `third-sickn33-auth-implementation-patterns-v1.0.md`, `third-sickn33-django-access-review-v1.0.md` |
| `apb-sub-e2e-v1.0` | `apb-sub-qa-e2e-v1.0` | `third-sickn33-screen-reader-testing-v1.0.md` |
| `apb-wf-qa-v1.0` | `apb-wf-qa-evidence-v1.0` | `third-sickn33-screen-reader-testing-v1.0.md` |

No son gaps de catálogo reales — los componentes correctos sí existen,
simplemente se citaron con el nombre histórico. Corregidos antes del
cierre de sesión; validación re-ejecutada limpia tras cada corrección.

## 7. Corrección retroactiva de un error de cómputo de Sesión 8

Al iniciar la verificación de esta sesión se detectó que
`CONTINUIDAD_PROYECTO.md` (sección 8, cierre de Sesión 8) reportaba "43
skills terceros", mientras que el cómputo real verificado mediante
`find skills/third_party -name "*.md" | wc -l` y confirmado por
`generate_catalog.py` era **44** ya en el estado de cierre de Sesión 8.
Es un error de conteo manual al redactar el resumen de aquella sesión, no
un cambio de contenido — no se creó ni eliminó ningún componente
retroactivamente. Corregido en `CONTINUIDAD_PROYECTO.md` §8 con nota
explicativa.

## 8. Resultado de validación final de Sesión 9

```
0 errores, 59 warnings (exentos: source_commit unverified, GOVERNANCE.md §4.2)
generate_catalog.py --check: sin drift
tests.test_validate_repo: 19/19 OK
```

**Inventario tras Sesión 9: 217 componentes** (antes 208, +9 = 8 skills
nuevas + 1 corrección de cómputo retroactivo de Sesión 8 que no representa
trabajo nuevo de catálogo):
- 107 skills APB (sin cambio)
- **52 skills terceros** (antes 44, +8)
- 19 agentes, 13 subagentes, 7 workflows, 10 providers, 7 wrappers, 2
  adapters (sin cambio en ninguno de estos)

## 9. Pendiente explícito para una futura sesión de terceros

Ver `PLAN_FASES_FUTURAS.md` punto #27 para el listado completo de repos
adicionales mencionados por Debora tras el cierre de esta sesión, varios
de los cuales requieren que aporte la URL/organización exacta antes de
poder evaluarse (no se buscan por nombre solo, por riesgo de identificar
el repositorio equivocado).

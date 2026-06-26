---
id: "apb-dev-code-base-v1.0"
name: "Code Base Analysis"
description: "Analiza la base de código completa de un repositorio para generar un mapa de arquitectura, identificar dependencias, deuda técnica, patrones usados y oportunidades de mejora. Orientado a legacy onboarding y auditorías."
version: "1.0.0-draft"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-20"
---

# SKILL: Code Base Analysis

## 1. Responsabilidad

Esta skill analiza una base de código completa para:
- Generar un mapa de arquitectura visual (dependencias entre proyectos, capas).
- Identificar patrones arquitectónicos utilizados (MVC, N-Tier, DDD, etc.).
- Detectar deuda técnica: código duplicado, dependencias obsoletas, complejidad.
- Inventariar tecnologías, frameworks y librerías utilizadas.
- Identificar puntos de acoplamiento y violaciones de arquitectura.
- Proponer plan de modernización priorizado.
- Generar `system-spec.md` y `domain-spec.md` iniciales para repos sin specs.

## 2. Inputs

| Nombre | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `repo_path` | file_path | Sí | Ruta al repositorio a analizar |
| `analysis_depth` | enum | No | `surface`, `deep`, `full`. Default: `deep` |
| `focus_areas` | list | No | Áreas de foco: `architecture`, `security`, `performance`, `dependencies`, `tests`. Default: all |
| `output_format` | enum | No | `markdown`, `json`, `mermaid`. Default: `markdown` |
| `language` | enum | No | Idioma del informe: `es`, `ca`, `en`. Default: `es` |

## 3. Outputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `architecture_map` | markdown/mermaid | Mapa de arquitectura con dependencias |
| `tech_inventory` | json | Inventario de tecnologías, versiones, licencias |
| `tech_debt_report` | markdown | Informe de deuda técnica con severidad y estimación |
| `modernization_plan` | markdown | Plan de modernización priorizado con roadmap |
| `system_spec` | markdown | Especificación del sistema generada (`system-spec.md`) |
| `domain_spec` | markdown | Especificación del dominio generada (`domain-spec.md`) |

## 4. Dependencias

| Tipo | ID | Descripción |
|------|-----|-------------|
| skill | `apb-dev-code-review-v1.0` | Análisis detallado de código |
| skill | `apb-sec-owasp-v1.0` | Análisis de seguridad |
| skill | `apb-arch-ddd-v1.0` | Descubrimiento de dominio DDD |
| workflow | `apb-wf-legacy-onboarding-v1.0` | Workflow de onboarding legacy |

## 5. Prompt del Sistema

```
Eres el skill "Code Base Analysis" (apb-dev-code-base-v1.0) del APB AI Framework.

## Contexto
- Organización: Autoridad Portuaria de Barcelona (APB)
- Stack típico legacy: .NET Framework / .NET Core, WebForms, MVC, WCF, SQL Server
- Stack objetivo: .NET 8/9, microservicios, Azure, DDD, event-driven
- Repositorios legacy: ~550 repos existentes
- Objetivo: Generar specs y plan de modernización para onboarding al framework

## Instrucciones
1. Analiza la estructura del repositorio:
   - Archivos de solución (.sln), proyectos (.csproj)
   - Estructura de carpetas y convenciones de nombres
   - Archivos de configuración (web.config, appsettings, Dockerfile, etc.)

2. Inventaría tecnologías:
   - Frameworks (.NET version, ASP.NET, Entity Framework)
   - Librerías NuGet con versiones
   - Bases de datos y ORMs
   - Servicios externos integrados
   - Front-end (DevExpress, ASP.NET MVC, Blazor, etc.)

3. Genera mapa de arquitectura:
   - Diagrama de dependencias entre proyectos (Mermaid)
   - Identificación de capas y patrones
   - Puntos de acoplamiento fuerte
   - Servicios compartidos y librerías comunes

4. Detecta deuda técnica:
   - Dependencias obsoletas o con vulnerabilidades conocidas
   - Código duplicado (heurístico)
   - Complejidad ciclomática alta (>10)
   - Falta de tests o baja cobertura
   - Uso de APIs obsoletas o deprecated
   - Violaciones de arquitectura (acceso directo a DB desde UI, etc.)

5. Analiza seguridad:
   - Secretos hardcodeados
   - Configuraciones inseguras
   - Vulnerabilidades OWASP comunes
   - Autenticación/autorización

6. Genera specs:
   - `system-spec.md`: Visión general, contexto, restricciones, calidad
   - `domain-spec.md`: Bounded contexts, entidades, eventos, reglas de negocio

7. Genera plan de modernización:
   - Fases priorizadas por impacto/esfuerzo
   - Riesgos y mitigaciones
   - Dependencias entre fases
   - Estimación de esfuerzo (t-shirt sizing)

## Restricciones
- No modifiques el código fuente del repositorio.
- No ejecutes código del repositorio.
- No incluyas secretos en los outputs.
- Respeta los estándares corporativos APB.

## Formato de Salida
### Análisis de Base de Código: {repo_name}

**Ruta:** `{repo_path}`
**Fecha:** `{fecha}`
**Agente:** `{agente}`
**Skill:** `apb-dev-code-base-v1.0`
**Depth:** `{analysis_depth}`

---

#### 1. Resumen Ejecutivo
{resumen en 5-10 líneas}

---

#### 2. Inventario de Tecnologías
| Tecnología | Versión | Estado | Riesgo |
|------------|---------|--------|--------|
| {tech} | {version} | {current/obsolete} | {low/medium/high} |

---

#### 3. Mapa de Arquitectura
```mermaid
{diagrama de dependencias}
```

---

#### 4. Deuda Técnica
| Categoría | Severidad | Hallazgos | Esfuerzo Est. |
|-----------|-----------|-----------|---------------|
| {cat} | {sev} | {count} | {t-shirt} |

---

#### 5. Análisis de Seguridad
{hallazgos de seguridad}

---

#### 6. system-spec.md
```markdown
{contenido}
```

---

#### 7. domain-spec.md
```markdown
{contenido}
```

---

#### 8. Plan de Modernización
| Fase | Objetivo | Esfuerzo | Dependencias | Riesgo |
|------|----------|----------|--------------|--------|
| 1 | {obj} | {size} | {deps} | {risk} |
```

## 6. Agentes Consumidores

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-spec-engineer-v1.0` | Generación de specs para repos legacy |
| `apb-agent-governance-v1.0` | Auditoría de cumplimiento y deuda técnica |
| Workflow `apb-wf-legacy-onboarding-v1.0` | Paso 1 del onboarding legacy |

## 7. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | Arquitecto de Solución | Aprobación del scope del análisis |
| Post-ejecución | Arquitecto / Tech Lead | Validación de specs, aprobación del plan de modernización |

## 8. Riesgo y Clasificación

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `Medium` |
| Impacto en producción | Análisis incompleto podría omitir dependencias críticas o deuda técnica oculta |
| Medidas compensatorias | Revisión humana obligatoria. Análisis incremental en repos grandes. |

## 9. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Codigo generado** - primera linea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-code-base-v1.0) - pendiente revision humana`
- **Commit** - prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** - label `ai-generated` en GitHub + footer en descripcion del PR

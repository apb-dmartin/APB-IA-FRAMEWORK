---
id: "apb-sec-sast-v1.0"
name: "Análisis SAST — Interpretación de Resultados"
description: "Interpreta los resultados de herramientas SAST (SonarQube, Semgrep, Checkmarx) en el contexto APB: prioriza hallazgos según impacto real, descarta falsos positivos, genera plan de remediación ordenado y valida cumplimiento OWASP Top 10 y ENS."
version: "1.0.0"
status: "draft"
owner: "Seguridad APB <seguridad@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Análisis SAST — Interpretación de Resultados


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Transformar el output bruto de una herramienta SAST en un plan de remediación accionable, priorizando los hallazgos según su impacto real en los sistemas APB. No todos los findings SAST son iguales: este skill contextualiza severidades genéricas de la herramienta con el stack tecnológico APB (.NET, Java, Python), la exposición del servicio (interno vs. ciudadanos) y los requisitos ENS.

## Contexto de Uso
- Revisión de código antes de merge a rama principal (pipeline CI/CD).
- Auditoría de seguridad periódica de aplicaciones en producción.
- Onboarding de una aplicación existente al framework de seguridad APB.
- Preparación de evidencias de cumplimiento ENS o auditoría externa.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `sast_report` | JSON / XML / CSV | Informe exportado de SonarQube, Semgrep o Checkmarx | ✅ |
| `service_name` | Texto | Nombre del servicio o aplicación analizada | ✅ |
| `tech_stack` | Lista | Lenguajes y frameworks: .NET 8, Java 17, Python 3.11, etc. | ✅ |
| `exposure_level` | Enum | `internal` / `external-staff` / `external-citizens` | ✅ |
| `ens_category` | Enum | Categoría ENS del sistema: `basic` / `medium` / `high` | ❌ |
| `previous_findings` | JSON | Findings de análisis anteriores para comparar regresiones | ❌ |

## Flujo de Trabajo

1. **Parsing y normalización del informe**:
   - Extraer todos los findings con: regla disparada, severidad original, fichero, línea, descripción.
   - Normalizar severidades al esquema APB: Critical / High / Medium / Low / Info.
   - Agrupar por categoría OWASP Top 10 cuando aplique.

2. **Contextualización APB**:
   - Ajustar severidad según `exposure_level`: un SQL Injection en servicio interno → High; en servicio ciudadanos → Critical.
   - Filtrar reglas no aplicables al stack declarado (ej. reglas PHP en proyecto .NET).
   - Identificar falsos positivos conocidos: sanitización en capa anterior, datos no controlados por el usuario, código de test.

3. **Detección de falsos positivos**:
   - Marcar como FP candidato si: el dato tainted no llega a sink por control flow, la regla es experimental en la herramienta, o el patrón está en código generado (scaffolding, migrations).
   - Los FP candidatos requieren confirmación humana antes de suprimir.

4. **Priorización de remediación**:
   - **P0 — Inmediato** (bloquear merge): Critical, o cualquier OWASP A01-A03 en exposición externa.
   - **P1 — Sprint actual**: High sin mitigación compensatoria.
   - **P2 — Backlog priorizado**: Medium con plan de remediación en <30 días.
   - **P3 — Backlog técnico**: Low e Info, sin SLA urgente.

5. **Generación del plan de remediación**:
   - Por cada finding P0/P1: descripción del problema, línea exacta, fragmento de código vulnerable, corrección recomendada con ejemplo.
   - Para P2/P3: descripción breve + referencia a OWASP/CWE correspondiente.

6. **Verificación de cobertura OWASP y ENS**:
   - Mapear findings a las 10 categorías OWASP Top 10 (2021).
   - Si `ens_category` es `medium` o `high`: verificar cobertura de controles de seguridad en código (autenticación, cifrado, auditoría).

7. **⚠️ CHECKPOINT HUMANO**: El equipo de seguridad APB debe validar la lista de falsos positivos y la priorización antes de cerrar findings en la herramienta SAST.

## Salida Esperada

```markdown
# Informe SAST — [Servicio] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-sec-sast-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Resumen Ejecutivo
| Herramienta | Versión | Fecha análisis | Total findings | Critical | High | Medium | Low | FP candidatos |
|---|---|---|---|---|---|---|---|---|

## Cobertura OWASP Top 10
| Categoría | Findings | Severidad máxima | Estado |
|---|---|---|---|
| A01 Broken Access Control | ... | | |

## Plan de Remediación

### P0 — Bloquear merge (acción inmediata)
| ID | Regla | Fichero:Línea | Descripción | Corrección |
|---|---|---|---|---|

### P1 — Sprint actual
...

### P2 — Backlog priorizado (<30 días)
...

### P3 — Backlog técnico
...

## Falsos Positivos Candidatos (requieren confirmación humana)
| ID | Regla | Motivo FP | Decisión |
|---|---|---|---|

## Comparativa con análisis anterior
| Categoría | Anterior | Actual | Variación |
```

## Criterios de Calidad
- [ ] Todos los findings Critical y High tienen corrección recomendada con ejemplo de código.
- [ ] Los falsos positivos candidatos están documentados con justificación técnica.
- [ ] La priorización P0/P1/P2/P3 está alineada con el nivel de exposición declarado.
- [ ] El mapeo OWASP Top 10 está completo.
- [ ] Si ENS medium/high: los controles de seguridad en código están verificados.
- [ ] No se suprime ningún finding sin revisión humana explícita.

## Stack y Tecnologías
- SAST: SonarQube (instancia APB en Azure DevOps), Semgrep OSS, Checkmarx (si disponible)
- Lenguajes cubiertos: C# / .NET 8, Java 17, Python 3.11, TypeScript/JavaScript
- Referencias: OWASP Top 10 2021, CWE/SANS Top 25, ENS Guía CCN-STIC-807

## Dependencias
- `apb-sec-patch-management-v1.0` — los findings pueden generar tareas de actualización de dependencias
- `apb-dev-code-review-v1.0` — el informe SAST complementa la revisión de código manual

## Ejemplo de Uso

```
Analiza el informe SAST adjunto de SonarQube para el servicio APB-Portal-Ciudadanos.
Stack: .NET 8 + React. Exposición: external-citizens. ENS: medium.
Necesito la lista priorizada de findings y el plan de remediación para el sprint.
```

## Notas y Advertencias
- **Nivel 1**: Los falsos positivos y la priorización final requieren validación del equipo de seguridad.
- No suprimir findings con `// NOSONAR` o equivalente sin ticket de seguimiento en Jira.
- Las reglas experimentales de Semgrep tienen mayor tasa de FP: tratarlas siempre como FP candidatos.
- En servicios ciudadanos, aplicar el principio de mínima tolerancia: ante la duda, escalar severidad.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Seguridad APB / Claude Code | Creación inicial — Sesión Enriquecimiento B, Bloque 2 |

## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-sast-v1.0) — pendiente validación humana. No distribuir sin revisión.

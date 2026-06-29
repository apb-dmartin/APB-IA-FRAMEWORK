---
id: "apb-sec-patch-management-v1.0"
name: "Gestión de Parches — Priorización CVE × Impacto APB"
description: "Prioriza los parches de seguridad pendientes en sistemas APB cruzando la severidad CVSS del CVE con el impacto operativo real, la exposición del sistema, la disponibilidad de parche y la ventana de cambio permitida. Genera el plan de parcheo ordenado y los RFC necesarios."
version: "1.0.0"
status: "draft"
owner: "Seguridad APB <seguridad@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Gestión de Parches — Priorización CVE × Impacto APB

## Propósito
Determinar en qué orden y con qué urgencia se aplican los parches de seguridad en los sistemas APB. La puntuación CVSS por sí sola no es suficiente: un CVE de CVSS 9.0 en un sistema interno sin exposición externa puede ser menos urgente que un CVE de CVSS 7.5 en el portal ciudadanos. Este skill cruza cuatro dimensiones — severidad, exposición, explotabilidad y criticidad del sistema — para producir un plan de parcheo realista alineado con las ventanas de cambio APB.

## Contexto de Uso
- Evaluación mensual del backlog de CVE pendientes de parcheo.
- Respuesta a un CVE publicado de alta severidad (0-day o exploit público).
- Preparación del plan de parcheo para el CAB (Change Advisory Board) mensual.
- Auditoría ENS: demostrar que los sistemas tienen un proceso documentado de gestión de vulnerabilidades.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `cve_list` | Lista / JSON | CVEs pendientes con CVSS, descripción y sistemas afectados | ✅ |
| `affected_systems` | Lista | Sistemas APB afectados con metadatos: exposición, ENS, criticidad operativa | ✅ |
| `change_windows` | Lista | Ventanas de mantenimiento disponibles (fechas, duración, restricciones) | ✅ |
| `patch_availability` | Mapa | Para cada CVE: si existe parche, versión que lo resuelve, workaround disponible | ❌ |
| `exploit_intel` | Lista | CVEs con exploit público o activamente explotados (fuentes: CISA KEV, NVD) | ❌ |

## Flujo de Trabajo

1. **Enriquecimiento de CVEs**:
   - Para cada CVE: obtener CVSS base score, vector de ataque (Network/Adjacent/Local/Physical), complejidad de ataque, privilegios requeridos.
   - Verificar si el CVE está en el catálogo CISA KEV (Known Exploited Vulnerabilities) — estos tienen SLA mandatorio de 15 días.
   - Verificar disponibilidad de exploit público (Exploit-DB, Metasploit, PoC en GitHub).

2. **Evaluación de exposición APB**:
   - Para cada sistema afectado:
     - **Exposición**: `internet-facing` (ciudadanos, socios) / `staff-only` / `internal-only`
     - **Criticidad**: `critical` (operaciones portuarias, facturación) / `high` / `medium` / `low`
     - **ENS**: `basic` / `medium` / `high`

3. **Cálculo de prioridad APB**:
   Combinar CVSS + exposición + explotabilidad + criticidad en una puntuación APB:

   | Factor | Peso | Valores |
   |---|---|---|
   | CVSS base score | 40% | 0-10 normalizado |
   | Exposición | 25% | internet=10, staff=6, internal=3 |
   | Exploit público/KEV | 20% | KEV=10, exploit=8, PoC=5, ninguno=0 |
   | Criticidad sistema | 15% | critical=10, high=7, medium=4, low=1 |

   - **APB-P0** (≥8.5): Parche en <72h. Requiere RFC de emergencia.
   - **APB-P1** (7.0-8.4): Parche en <7 días. Requiere RFC urgente.
   - **APB-P2** (5.0-6.9): Parche en <30 días. RFC en próximo CAB mensual.
   - **APB-P3** (<5.0): Parche en <90 días. Backlog de seguridad.

4. **Identificación de workarounds**:
   - Para CVEs sin parche disponible: documentar mitigación temporal (deshabilitar feature, WAF rule, restricción de red, actualización de configuración).
   - Los workarounds son temporales y deben tener fecha de revisión.

5. **Planificación de ventanas de cambio**:
   - Asignar cada parche a la ventana de cambio más próxima compatible con su SLA.
   - Respetar restricciones APB: no parchear sistemas críticos en temporada alta de cruceros sin aprobación CAB.
   - Identificar parches que requieren reinicio de servicio → coordinar con SRE y NOC.
   - Agrupar parches del mismo sistema en una sola ventana cuando sea posible (reducir interrupciones).

6. **Generación de RFC**:
   - P0/P1: RFC de emergencia con justificación de urgencia, evidencia del CVE, plan de rollback.
   - P2: RFC estándar para próximo CAB con plan de parcheo y pruebas previas en staging.

7. **⚠️ CHECKPOINT HUMANO**: El plan de priorización APB-P0/P1 debe ser aprobado por el responsable de seguridad y el Change Manager antes de iniciar el parcheo.

## Salida Esperada

```markdown
# Plan de Gestión de Parches — [Fecha] — [Periodo]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-sec-patch-management-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Resumen Ejecutivo
| Total CVEs | APB-P0 | APB-P1 | APB-P2 | APB-P3 | En CISA KEV | Sin parche |

## CVEs APB-P0 — Acción en <72h

| CVE | CVSS | Puntuación APB | Sistema | Parche | Workaround | RFC requerido |
|---|---|---|---|---|---|---|

## CVEs APB-P1 — Acción en <7 días
...

## CVEs APB-P2 — Próximo CAB (<30 días)
...

## Plan de Ventanas de Cambio

| Fecha ventana | Sistemas | CVEs a parchear | Requiere reinicio | Duración estimada |
|---|---|---|---|---|

## CVEs sin Parche Disponible — Workarounds Activos
| CVE | Sistema | Workaround | Fecha revisión |

## RFCs a Generar
| Tipo RFC | CVEs | Sistema | Urgencia | Responsable |
```

## Criterios de Calidad
- [ ] Todos los CVEs en CISA KEV tienen SLA ≤15 días asignado.
- [ ] Los CVEs APB-P0 tienen RFC de emergencia generado o en proceso.
- [ ] Todos los CVEs sin parche tienen workaround documentado con fecha de revisión.
- [ ] El plan respeta las restricciones de ventanas de cambio APB declaradas.
- [ ] Los parches de sistemas críticos tienen plan de rollback documentado.
- [ ] El plan cubre los próximos 90 días con fechas concretas por ventana de cambio.

## Stack y Tecnologías
- CVE intelligence: NVD API, CISA KEV, osv.dev, Microsoft MSRC, Red Hat Security Advisories
- Gestión de cambios: Azure DevOps (RFC como Work Items), proceso CAB APB
- Parcheo OS: Azure Update Manager (VMs), AKS node auto-upgrade
- Parcheo aplicaciones: pipeline de actualización de dependencias, Azure Container Registry

## Dependencias
- `apb-sec-supply-chain-v1.0` — fuente de CVEs en dependencias de aplicaciones
- `apb-ops-change-management-v1.0` — los RFC de parcheo siguen el proceso de gestión de cambios APB
- `apb-ops-service-continuity-v1.0` — el parcheo de sistemas críticos requiere coordinación con continuidad

## Ejemplo de Uso

```
Tengo 23 CVEs pendientes de parcheo en los sistemas APB.
Adjunto la lista con CVSS y sistemas afectados.
Las próximas ventanas de cambio son el 15 y el 28 de julio.
No podemos afectar el portal ciudadanos hasta el 20 de julio por temporada de cruceros.
Genera el plan de priorización y los RFC necesarios para el CAB del jueves.
```

## Notas y Advertencias
- **Nivel 1**: La priorización APB-P0/P1 y los RFC de emergencia requieren aprobación humana.
- La puntuación CVSS base no incluye información de explotabilidad real — siempre cruzar con CISA KEV y exploit intel.
- Un CVE puede afectar a múltiples sistemas con prioridades distintas: cada instancia se evalúa independientemente.
- El parcheo de sistemas en alta disponibilidad (HA) requiere estrategia rolling update para evitar downtime.
- Registrar en Jira todos los CVEs aceptados como riesgo temporal con justificación y fecha de revisión.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Seguridad APB / Claude Code | Creación inicial — Sesión Enriquecimiento B, Bloque 2 |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-patch-management-v1.0) — pendiente validación humana. No distribuir sin revisión.

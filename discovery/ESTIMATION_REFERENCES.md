# Catálogo de Referencias de Valoraciones — Jira APB

> **Borrador generado por IA** (APB AI Framework - apb-pm-jira-estimation-review-v1.0) - pendiente validación humana. No distribuir sin revisión.

## Propósito

Catálogo acumulativo de valoraciones reales de tickets Jira APB, sembrado con un
análisis real de 12 meses (aportado por Débora, 2026-07-08) y alimentado
incrementalmente por las skills
[`apb-pm-jira-estimation-review-v1.0`](../skills/apb-owned/pm/apb-pm-jira-estimation-review-v1.0.md)
(sistema Horas/Perfil) y, en el futuro, por el uso de
[`apb-disc-cosmic-v1.0`](../skills/apb-owned/discovery/apb-disc-cosmic-v1.0.md)
(sistema COSMIC) a través de `apb-agent-valoracion-tecnica-v1.0`. Sirve como
**complemento** a la consulta en vivo a Jira (`prov-atlassian-v1.0`,
`search_issues`/JQL) — no como sustituto.

**Regla de uso (fijada por Débora, 2026-07-06):** mientras una categoría tenga
**menos de 20 entradas**, la skill debe seguir tratando Jira en vivo como fuente de
verdad para precedentes de esa categoría. A partir de 20 entradas, el catálogo puede
citarse como referencia rápida de primera mano, sin que eso impida seguir consultando
Jira si el usuario lo pide o los datos disponibles parecen insuficientes.

**Nota sobre el sistema aplicable (2026-07-08):** el sistema de valoración
(COSMIC vs Horas/Perfil) depende del **contrato del proveedor concreto**, no de si
el trabajo es funcional o técnico — confirmado por el caso real de los proyectos
Java/Sòstrat, que valoran desarrollo funcional en horas. Por eso la columna
"Sistema" de este catálogo refleja cómo se factura **en la práctica**, no una
clasificación teórica.

## Tabla A — Desarrollo por stack/concepto (semilla real, 12 meses, aportada 2026-07-08)

| # | Concepto | Sistema | Stack | Media | Mediana | Rango | Nº tickets | Confianza |
|---|---|---|---|---|---|---|---|---|
| 1 | Desarrollo funcional (merged) | Horas | Java (Sòstrat) | 26,7h | ~14h | 2–177h | 119 | ✅ ≥50 |
| 2 | Pantalla/UI (grid+formulario+TCON+filtro) | Horas | .NET/DevExtreme | 21,7h | ~12h | 2–102h | 56 | ✅ ≥50 |
| 3 | WS/API/endpoint | Horas | .NET | 22,0h | ~15h | 2–90h | 41 | ⚠️ <50 |
| 4 | Integración API REST/eventos/EntraID | Horas | Cross | 34,5h | ~28h | 12–69h | 22 | ❌ <25 |
| 5 | Trazabilidad/auditoría/alertas/logs | Horas | Cross | 20,8h | ~11h | 2–102h | 52 | ✅ ≥50 |
| 6 | Informe/dashboard/report/exportación | Horas | Cross | 21,7h | ~11h | 3,5–92h | 19 | ❌ <25 |
| 7 | Ref. global desarrollo .NET (todas categorías) | Horas | .NET | 19,8h | ~13h | 2–185h | 200+ | ✅ ≥50 |

**Detalle categoría 1 (Java/Sòstrat, 119 tickets):**

| Proyecto | Tickets | Horas totales | Media | Rango |
|---|---|---|---|---|
| EK (EMSWe) | 47 | 1.764h | 37,5h | 3–146h |
| ESCA (Escalas core) | 28 | 600h | 21,4h | 2–117h |
| MARPOL | 34 | 475h | 14,0h | 4–71h |
| PAXLST | 4 | 292h | 73,1h | 6–177h |
| SOSO | 5 | 44h | 8,8h | 4–21h |

## Tabla B — Tareas técnicas puras (semilla real, unidad normalizada)

| # | Concepto | Sistema | Unidad | Valor referencia | Fuente | Confianza |
|---|---|---|---|---|---|---|
| 8 | Cambio de plantilla .NET | Horas | h/app-API | 8h (simple) · 15-24h (con migración .NET mayor) | 10 tickets | ❌ <25 |
| 9 | Monorepo → multirepo | Horas | h/componente separado | 4-5h/componente | 8 tickets | ❌ <25 |
| 10 | Sonar — issue simple | Horas | h/issue | 1-2h | derivado de epics | ⚠️ indicativo |
| 11 | Sonar — issue medio | Horas | h/issue | 3-5h | derivado de epics | ⚠️ indicativo |
| 12 | Sonar — actualización APIBASE completa | Horas | h/API | 6-8h | ARQ-3628 (255h/42 APIs) | ⚠️ indicativo |
| 13 | Script BBDD — ALTER simple | Horas | h/script | 1-4h | 5 tickets EK | ❌ <25 |
| 14 | Script BBDD — tabla nueva + lógica | Horas | h/script | 20-55h | EK-247, PIF-1653 | ❌ <25 |

> ⚠️ **Discrepancia conocida:** el catálogo `Catálogo de coste de tareas técnicas
> APB — v1.xlsx` valora "Corrección de vulnerabilidades" en 8-24h — sobreestima
> frente al dato real por issue individual (fila 10-12 de arriba: 1-8h según tipo).
> Usar siempre el dato real de esta tabla como fuente primaria ante esa categoría.

## Categorías

| Categoría | Nº de entradas | Rango de horas típico | ¿Usable como referencia rápida? (≥20) |
|---|---|---|---|
| Desarrollo funcional Java (Sòstrat) | 119 | 2–177h | Sí |
| Pantalla/UI .NET/DevExtreme | 56 | 2–102h | Sí |
| WS/API/endpoint .NET | 41 | 2–90h | No (cerca del umbral) |
| Integración API REST/eventos/EntraID | 22 | 12–69h | No |
| Trazabilidad/auditoría/alertas/logs | 52 | 2–102h | Sí |
| Informe/dashboard/report/exportación | 19 | 3,5–92h | No |
| Tareas técnicas puras (plantilla/monorepo/Sonar/BBDD) | 40 (agregado) | 1-55h según concepto | No (cada subcategoría <25) |

### Categorías del Catálogo USM/UEC/UTA sin dato real (pendientes de acumular)

> Débora confirmó (2026-07-08) que no tiene datos reales para estas 8 categorías.
> `apb-agent-valoracion-tecnica-v1.0` estima puntualmente con criterio técnico
> cuando surge un caso real (nunca con benchmarks de mercado — ver
> `apb-pm-catalogo-servicios-v1.0` §4) y registra el resultado real de cierre
> aquí como primer precedente. Estas filas pasan a la tabla principal de arriba
> en cuanto acumulen entradas reales.

| Categoría (Catálogo USM/UEC/UTA) | Nº de entradas | Estado |
|---|---|---|
| Gobierno Técnico, Cloud y de Arquitectura | 0 | Pendiente de acumular vía uso real del agente |
| Gobierno Integral de CMDB y Documentación Operativa Automatizada | 0 | Pendiente de acumular vía uso real del agente |
| FinOps — Gobierno y Optimización | 0 | Pendiente de acumular vía uso real del agente |
| Operación Técnica de Infraestructura, Plataformas y Redes | 0 | Pendiente de acumular vía uso real del agente |
| Continuidad Técnica: Backup, Recuperación, HA y DR | 0 | Pendiente de acumular vía uso real del agente |
| Guardias Técnicas Automatizadas y Respuesta Automática | 0 | Pendiente de acumular vía uso real del agente |
| Administración de Plataformas y Productos (Terceros) | 0 | Pendiente de acumular vía uso real del agente |
| QA — Oficina de Gobierno y Calidad | 0 | Pendiente de acumular vía uso real del agente |
| IaC/CaC — Automatizaciones reutilizables bajo demanda (UTA) | 0 | Pendiente de acumular vía uso real del agente |
| IaC/CaC — Prestación continua de capacidades (USM) | 0 | Pendiente de acumular vía uso real del agente |

## Entradas individuales

> A partir de aquí, cada fila la añade la skill tras un análisis nuevo (no incluido
> en las Tablas A/B de semilla). Formato: ticket de origen del análisis (no
> necesariamente el precedente), categoría, horas/CFP reales del precedente citado,
> sistema y enlace al análisis si se generó como comentario en Jira.

| Fecha | Ticket precedente | Categoría | Sistema | Valor real | Complejidad | Fuente |
|---|---|---|---|---|---|---|
| *(sin entradas nuevas todavía — ver Tablas A/B para la semilla)* | | | | | | |

---
*Fichero mantenido automáticamente por `apb-pm-jira-estimation-review-v1.0` y
`apb-agent-valoracion-tecnica-v1.0`. Semilla real aportada por Débora (2026-07-08,
extracción de 12 meses de Jira). Revisión humana recomendada antes de tratar los
rangos de confianza ⚠️/❌ como referencia definitiva.*

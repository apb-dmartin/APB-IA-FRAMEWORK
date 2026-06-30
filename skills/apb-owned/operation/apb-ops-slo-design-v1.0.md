---
id: "apb-ops-slo-design-v1.0"
name: "Diseño de SLO y Error Budget"
description: "Diseñar Service Level Objectives (SLOs) y error budgets para servicios y sistemas, alineados con las expectativas de negocio y las capacidades técnicas. Genera definiciones de SLOs, SLIs (indicadores), alertas basadas en burn rate y políticas de error budget."
version: "1.0.0"
status: "draft"
owner: "SRE APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Diseño de SLO y Error Budget


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Diseñar Service Level Objectives (SLOs) y error budgets para servicios y sistemas, alineados con las expectativas de negocio y las capacidades técnicas. Genera definiciones de SLOs, SLIs (indicadores), alertas basadas en burn rate y políticas de error budget.

## Contexto de Uso
- Definición de SLOs para nuevos servicios en producción.
- Revisión y ajuste de SLOs existentes basado en datos de rendimiento.
- Negociación de SLOs entre equipos técnicos y de negocio.
- Integración con workflows de release y operación.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `service_description` | Texto / Markdown | Descripción del servicio, usuarios y criticidad | ✅ |
| `historical_metrics` | JSON / CSV | Métricas históricas de disponibilidad, latencia, throughput | ❌ |
| `business_requirements` | Texto | Requisitos de negocio: ventanas de servicio, penalizaciones | ❌ |
| `slo_time_window` | Enum | `28d`, `30d`, `90d` | ❌ (default: 30d) |

## Flujo de Trabajo (Pasos)
1. **Análisis de criticidad**: Determinar nivel de servicio esperado basado en impacto de negocio.
2. **Definición de SLIs**: Identificar indicadores clave:
   - **Availability**: % de requests exitosas.
   - **Latency**: percentil p99 de tiempo de respuesta.
   - **Throughput**: requests por segundo sostenibles.
   - **Error rate**: % de errores 5xx.
3. **Propuesta de SLOs**: Definir objetivos realistas basados en percentiles históricos.
4. **Cálculo de error budget**: Para cada SLO, calcular el budget de errores permitido en la ventana temporal.
5. **Diseño de alertas basadas en burn rate**: Configurar alertas proactivas cuando el consumo de error budget excede umbrales:
   - **Fast burn**: 2% del budget en 1 hora → página inmediata.
   - **Slow burn**: 5% del budget en 6 horas → ticket de alta prioridad.
6. **Documentación de políticas**: Definir acciones cuando se agota el error budget (freeze de releases, revisión de arquitectura).
7. **Generación de informe**: Documento con SLOs, SLIs, alertas y políticas de error budget.
8. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Estructura del Informe
```markdown
# SLO y Error Budget — [Nombre Servicio]
> Fecha: [YYYY-MM-DD] | Autor: SRE Agent | Ventana: [slo_time_window]

## 1. Alcance y Contexto
## 2. SLIs Definidos
| SLI | Descripción | Fuente de Datos |
## 3. SLOs Propuestos
| SLO | Objetivo | SLI Asociado | Justificación |
## 4. Error Budget
| SLO | Budget Total | Consumo Actual | % Restante |
## 5. Alertas de Burn Rate
| Condición | Ventana | Umbral | Acción | Severidad |
## 6. Políticas de Error Budget Agotado
## 7. Recomendaciones
## 8. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Cada SLO tiene SLI medible, fuente de datos y justificación de negocio.
- [ ] Los SLOs son realistas (basados en percentiles históricos, no aspiracionales).
- [ ] Las alertas de burn rate cubren fast burn y slow burn.
- [ ] Las políticas de error budget agotado son claras y actionable.
- [ ] El informe es revisable por el equipo de SRE y negocio sin intervención del agente.

## Stack y Tecnologías
- Framework: Google SRE Book, Azure Monitor SLOs
- Métricas: Application Insights, Azure Monitor, Prometheus/Grafana
- Formatos: Markdown, JSON para configuración de alertas

## Dependencias
- `apb-ops-observability-v1.0` — para diseño de observabilidad
- `apb-ops-prr-v1.0` — para contexto de PRR
- `apb-gov-evidence-v1.0` — para generación de evidencia

## Ejemplo de Uso
**Prompt de invocación:**
```
Diseña SLOs para nuestro API de gestión de usuarios:
- Servicio: ASP.NET Core 8, Azure Container Apps, Azure SQL
- Usuarios: 5.000 usuarios concurrentes, crítico para operación diaria
- Métricas históricas: disponibilidad 99.5%, p99 latencia 450ms, error rate 0.3%
- Ventana: 30 días
- Requisito de negocio: Disponibilidad mínima 99.9% en horario laboral
```

## Notas y Advertencias
- **Nivel 1**: El agente diseña SLOs basados en datos proporcionados; no configura alertas en Azure Monitor directamente.
- **Revisión humana obligatoria** antes de aprobar SLOs; requieren acuerdo con negocio.
- Los SLOs aspiracionales (> 99.99%) deben justificarse con análisis de coste/beneficio.
- El agente no tiene acceso a datos de producción; trabaja con métricas proporcionadas.


## Prompt de Sistema

```
Eres el skill "Diseño de SLO y Error Budget" (apb-ops-slo-design-v1.0) del APB AI Framework,
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
Diseñar Service Level Objectives (SLOs) y error budgets para servicios y sistemas, alineados con las expectativas de negocio y las capacidades técnicas. Genera definiciones de SLOs, SLIs (indicadores), alertas basadas en burn rate y políticas de error budget.

## Inputs Esperados
(no especificado)

## Instrucciones
(no especificado)

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level 1: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output.

## Formato de Salida
(no especificado)
```

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-slo-design-v1.0) - pendiente validacion humana. No distribuir sin revision.

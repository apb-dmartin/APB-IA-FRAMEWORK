---
id: "apb-plat-cloud-ready-v1.0"
name: "Análisis de Ready to Cloud"
description: "Evaluar la preparación de aplicaciones y sistemas legacy para su migración a la nube (Azure). Genera un informe de readiness que identifica bloqueadores, recomendaciones de refactorización, estimación de esfuerzo y plan de migración phased."
version: "1.0.0"
status: "draft"
owner: "Arquitectura Cloud APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Análisis de Ready to Cloud

## Propósito
Evaluar la preparación de aplicaciones y sistemas legacy para su migración a la nube (Azure). Genera un informe de readiness que identifica bloqueadores, recomendaciones de refactorización, estimación de esfuerzo y plan de migración phased.

## Contexto de Uso
- Evaluación previa a la migración de sistemas on-premise a Azure.
- Assessment de aplicaciones legacy para modernización cloud-native.
- Identificación de dependencias, deuda técnica y requisitos de refactorización.
- Integración con workflows de migración a cloud y arquitectura de referencia.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `application_inventory` | Lista | Lista de aplicaciones/sistemas a evaluar con descripción | ✅ |
| `current_architecture` | Texto / Diagrama | Arquitectura actual (on-prem, VMs, servidores físicos) | ✅ |
| `cloud_target` | Enum | `azure-iaas`, `azure-paas`, `azure-container`, `azure-serverless` | ✅ |
| `constraints` | Lista | Restricciones: compliance, latencia, licencias, integración legacy | ❌ |
| `business_priority` | Enum | `critical`, `high`, `medium`, `low` | ❌ |

## Flujo de Trabajo (Pasos)
1. **Inventario y catalogación**: Documentar cada aplicación con sus dependencias, tecnologías, datos y usuarios.
2. **Evaluación de 12 factores cloud-ready** (adaptado a Azure):
   - Codebase, Dependencies, Config, Backing services, Build/release/run, Processes, Port binding, Concurrency, Disposability, Dev/prod parity, Logs, Admin processes.
3. **Análisis de bloqueadores**: Identificar impedimentos técnicos para la migración:
   - Dependencias de hardware específico.
   - Licencias no compatibles con cloud.
   - Protocolos de comunicación legacy.
   - Requisitos de latencia que no cumplen con cloud.
   - Datos que no pueden salir de jurisdicción.
4. **Evaluación de target**: Recomendar servicio Azure más adecuado por aplicación:
   - VMs (IaaS) — lift-and-shift mínimo.
   - App Service (PaaS) — apps web/API sin estado.
   - Container Apps / AKS — microservicios containerizados.
   - Functions — event-driven, serverless.
   - SQL Database / PostgreSQL — datos managed.
5. **Estimación de esfuerzo**: T-shirt sizing (S/M/L/XL) por aplicación con factores de complejidad.
6. **Plan de migración phased**: Orden de migración por prioridad de negocio y dependencias técnicas.
7. **Generación de informe**: Documento estructurado con matriz de readiness, roadmap y riesgos.
8. **Registro de evidencia**: Metadatos para gobierno y tracking.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe Ready to Cloud — [Nombre del Programa]
> Fecha: [YYYY-MM-DD] | Autor: Cloud Architect Agent | Target: Azure

## 1. Alcance y Inventario
## 2. Evaluación por Aplicación
| Aplicación | Tecnología | 12-Factor Score | Bloqueadores | Target Azure | Esfuerzo | Prioridad |
## 3. Matriz de Readiness
## 4. Bloqueadores y Mitigaciones
## 5. Roadmap de Migración
## 6. Estimación de Costes (orientativa)
## 7. Riesgos y Dependencias
## 8. Recomendaciones
## 9. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] 100% de aplicaciones del inventario evaluadas con puntuación por factor.
- [ ] Todos los bloqueadores identificados tienen mitigación propuesta o plan de contingencia.
- [ ] Roadmap con dependencias cruzadas validado (no migrar B antes que A si B depende de A).
- [ ] Estimación de esfuerzo con factores de riesgo y complejidad documentados.
- [ ] Recomendaciones de target Azure justificadas técnicamente.
- [ ] El informe es revisable por el equipo de cloud y arquitectura sin intervención del agente.

## Stack y Tecnologías
- Framework: 12-Factor App, Azure Well-Architected Framework
- Servicios Azure: App Service, AKS, Container Apps, Functions, SQL Database, PostgreSQL, VM, Virtual Network
- Assessment: Azure Migrate, Microsoft Assessment and Planning Toolkit
- Formatos: Markdown, Excel para matriz detallada

## Dependencias
- `apb-arch-cloud-infra-v1.0` — para diseño de infraestructura cloud
- `apb-arch-decompose-v1.0` — para descomposición de monolitos
- `apb-plat-terraform-v1.0` — para generación de infraestructura target
- `apb-wf-cloud-migration-v1.0` — para workflow de migración

## Ejemplo de Uso
**Prompt de invocación:**
```
Evalúa la readiness para cloud de nuestro portfolio de aplicaciones:
- App 1: Sistema de gestión financiera (ASP.NET Web Forms, SQL Server 2016, on-prem)
- App 2: Portal de clientes (ASP.NET Core 6, Angular, VMs on-prem)
- App 3: Servicio de notificaciones (Windows Service .NET Framework 4.8, on-prem)
- Target preferido: Azure PaaS donde sea posible
- Restricciones: datos financieros en España (soberanía), latencia < 100ms
```

## Notas y Advertencias
- **Nivel 1**: El agente realiza análisis basado en información proporcionada; no ejecuta scans ni accede a entornos reales.
- **Revisión humana obligatoria** antes de aprobar el roadmap de migración.
- Las estimaciones de coste son orientativas; requieren validación con calculadora de precios de Azure.
- Los bloqueadores de compliance (soberanía de datos) deben validarse con el equipo legal y de seguridad.
- El agente no tiene acceso a suscripciones de Azure ni a datos de costing reales.

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

- **Primera linea del fichero generado**: `# [IA-GEN] Generado por APB AI Framework (apb-plat-cloud-ready-v1.0) - revisar ANTES de aplicar en produccion`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`

NOTA: Para IaC, ningun fichero generado por IA debe aplicarse en produccion sin revision humana explicita.

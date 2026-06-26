---
id: "apb-arch-design-v1.0"
name: "Diseño de Arquitectura"
description: "Generar propuestas de arquitectura de software basadas en requisitos funcionales y no funcionales, alineadas con los estándares corporativos de APB. Incluye selección de patrones, estilos arquitectónicos y justificación técnica."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Diseño de Arquitectura

---

## 🎯 Propósito

Generar propuestas de arquitectura de software basadas en requisitos funcionales y no funcionales, alineadas con los estándares corporativos de APB. Incluye selección de patrones, estilos arquitectónicos y justificación técnica.

---

## ⚡ Trigger

Cuando se requiere definir o revisar la arquitectura de un sistema, módulo o microservicio nuevo o existente. También tras cambios significativos en requisitos no funcionales (escalabilidad, seguridad, rendimiento).

---

## 📥 Input

- Requisitos funcionales y no funcionales documentados
- Contexto de negocio y dominio
- Restricciones tecnológicas y presupuestarias
- Arquitectura actual (si aplica)
- Estándares corporativos APB vigentes

---

## 📤 Output

- Documento de arquitectura (formato estándar APB)
- Diagramas C4 (nivel 1, 2 y 3 según necesidad)
- Matriz de decisiones arquitectónicas (ADRs preliminares)
- Lista de riesgos técnicos identificados
- Recomendaciones de implementación

---

## 🔄 Proceso

1. **Análisis de requisitos**: Revisar requisitos funcionales y no funcionales. Identificar constraints críticos.
2. **Evaluación de contexto**: Analizar arquitectura existente, deuda técnica y dependencias.
3. **Selección de estilo arquitectónico**: Evaluar opciones (monolito modular, microservicios, serverless, event-driven, CQRS, etc.) con matriz de decisión.
4. **Diseño de componentes**: Definir componentes principales, sus responsabilidades e interfaces.
5. **Diseño de datos**: Modelo de datos, estrategia de persistencia, caching y replicación.
6. **Diseño de comunicación**: Protocolos, brokers, APIs, patrones de integración.
7. **Validación contra estándares**: Verificar cumplimiento de estándares APB (seguridad, observabilidad, operabilidad).
8. **Generación de artefactos**: Documento, diagramas y ADRs preliminares.
9. **Revisión de riesgos**: Identificar y documentar riesgos técnicos con mitigaciones propuestas.

---

## 📋 Reglas y Constraints

- Todo diseño debe justificar la elección del estilo arquitectónico con criterios cuantificables (coste, complejidad, time-to-market, escalabilidad).
- No se permite diseñar sistemas sin considerar observabilidad (logs, métricas, trazas) desde el inicio.
- Las comunicaciones entre microservicios deben preferir eventos asíncronos (Azure Service Bus + CloudEvents) sobre llamadas síncronas, salvo justificación explícita.
- Todo componente debe tener un owner técnico definido.
- Se debe evaluar siempre la opción de reutilizar componentes existentes antes de crear nuevos.
- Los diagramas deben seguir el estándar C4 model.
- No se almacenan secretos en configuración; siempre referenciar Azure Key Vault.

---

## 🛠 Stack Tecnológico Relevante

- .NET 8/9, ASP.NET Core
- Azure Service Bus (eventos)
- Azure API Management
- Azure Application Insights
- Terraform / Bicep
- Docker / Kubernetes (AKS)
- CloudEvents 1.0
- PostgreSQL / Azure SQL
- Redis

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Nuevo microservicio de facturación:**
> Input: Requisitos de facturación electrónica, 10K transacciones/día, integración con Hacienda.
> Output: Arquitectura basada en microservicio .NET 9, Azure Service Bus para eventos de factura generada, PostgreSQL con particionamiento, API REST con versioning, ADR sobre elección de PostgreSQL vs Azure SQL.

**Ejemplo 2 — Modernización de módulo legacy:**
> Input: Módulo de nómina en VB6, 50 usuarios concurrentes, alta criticidad.
> Output: Propuesta de strangler fig pattern, microservicio .NET 9 con CQRS, migración gradual con anti-corruption layer, manteniendo BBDD legacy temporalmente.

---

## 🔗 Dependencias

- `apb-arch-validate-v1.0` (validación posterior)
- `apb-arch-tech-plan-v1.0` (plan técnico de implementación)
- `apb-doc-adr-v1.0` (formalización de decisiones)
- `apb-sec-threat-model-v1.0` (seguridad)
- `prov-azure-v1.0` (referencia a servicios cloud)

---

## 📝 Notas

- Esta skill no genera código; produce artefactos de diseño.
- Para arquitecturas complejas, recomendar la activación del workflow `apb-wf-sdd-full-v1.0`.
- En caso de duda entre estilos arquitectónicos, proponer PoC (proof of concept) como mitigación de riesgo.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-design-v1.0) - pendiente validacion humana. No distribuir sin revision.

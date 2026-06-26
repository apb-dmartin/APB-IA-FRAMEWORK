---
id: "apb-arch-event-driven-v1.0"
name: "Diseño Event-Driven"
description: "Diseñar arquitecturas basadas en eventos que permitan desacoplamiento, escalabilidad y resiliencia. Define patrones de publicación/suscripción, esquemas de eventos, manejo de fallos y garantías de entrega."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Diseño Event-Driven

---

## 🎯 Propósito

Diseñar arquitecturas basadas en eventos que permitan desacoplamiento, escalabilidad y resiliencia. Define patrones de publicación/suscripción, esquemas de eventos, manejo de fallos y garantías de entrega.

---

## ⚡ Trigger

Cuando un sistema requiere comunicación asíncrona entre componentes, procesamiento de streams, reacción a cambios de estado, o desacoplamiento de productores y consumidores.

---

## 📥 Input

- Diagrama de contexto del sistema
- Lista de eventos de negocio identificados
- Requisitos de latencia y throughput
- Requisitos de consistencia (eventual vs fuerte)
- Topología de red y restricciones de seguridad
- Stack tecnológico actual (Azure Service Bus ya definido como broker corporativo)

---

## 📤 Output

- Diseño de topología de eventos (diagrama)
- Catálogo de eventos con esquemas CloudEvents 1.0
- Definición de topics/queues y suscripciones
- Estrategia de manejo de errores (dead letter, retry, circuit breaker)
- Política de idempotencia y ordenamiento
- Matriz de productores/consumidores

---

## 🔄 Proceso

1. **Identificación de eventos de negocio**: Workshop con stakeholders para identificar eventos relevantes (Event Storming recomendado).
2. **Clasificación de eventos**: Categorizar en eventos de dominio, integración, notificación. Definir granularidad.
3. **Diseño de esquemas**: Definir esquemas JSON con CloudEvents 1.0 (specversion, type, source, id, time, datacontenttype, data).
4. **Diseño de topología**: Definir Service Bus topics/queues, subscriptions, filtros. Decidir entre Standard vs Premium tier.
5. **Patrones de consumo**: Evaluar competing consumers, fan-out, event sourcing, CQRS, saga pattern.
6. **Estrategia de resiliencia**: Dead letter queues, exponential backoff, circuit breaker, bulkhead.
7. **Seguridad**: Autenticación MSI, RBAC, encriptación en tránsito (TLS 1.2+) y en reposo.
8. **Observabilidad**: Correlación de trazas mediante trace-id en atributos CloudEvents.
9. **Documentación**: Generar catálogo de eventos y diagrama de flujo.

---

## 📋 Reglas y Constraints

- Todos los eventos DEBEN seguir el estándar CloudEvents 1.0 con esquema JSON.
- NO usar Avro ni Protobuf para schemas de eventos en el stack APB (salvo excepción aprobada por Arquitectura).
- Cada evento debe tener un identificador único (UUID v4) para trazabilidad.
- Los consumidores deben ser idempotentes; documentar estrategia de deduplicación.
- El ordenamiento de eventos solo se garantiza dentro de una session/partition; documentar si el negocio requiere ordenamiento global.
- Los dead letter messages deben alertar al equipo mediante Azure Monitor + Logic Apps.
- No exponer información sensible (PII) en payloads de eventos; usar referencias seguras.
- Latencia objetivo: < 500ms para eventos críticos, < 5s para eventos batch.

---

## 🛠 Stack Tecnológico Relevante

- Azure Service Bus (broker corporativo)
- CloudEvents 1.0
- .NET 8/9 (Azure.Messaging.ServiceBus)
- Azure Event Grid (para eventos de infraestructura)
- Azure Monitor / Application Insights
- Redis (para deduplicación/idempotencia)

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Pedido creado:**
> Evento: `com.apb.orders.order-created.v1`
> Schema CloudEvents con datos: orderId, customerId, items[], totalAmount, timestamp.
> Flujo: API REST publica evento → Service Bus Topic → Suscriptores: Inventario (reserva stock), Facturación (genera factura), Notificaciones (envía email).

**Ejemplo 2 — Saga de compensación:**
> Flujo de reserva de viaje: Vuelo reservado → Hotel reservado → Coche reservado.
> Si falla coche, emitir eventos de compensación para revertir vuelo y hotel.
> Patrón Saga orquestado mediante Azure Durable Functions + Service Bus.

---

## 🔗 Dependencias

- `apb-arch-event-storming-v1.0` (identificación de eventos)
- `apb-arch-api-contract-v1.0` (contratos de API que disparan eventos)
- `apb-ops-observability-v1.0` (diseño de observabilidad)
- `apb-sec-threat-model-v1.0` (seguridad de eventos)
- `prov-azure-v1.0`

---

## 📝 Notas

- Azure Service Bus Premium es obligatorio para workloads de producción con > 1000 msg/s o requisitos de baja latencia.
- Para Event Sourcing completo, evaluar Azure Cosmos DB como event store (no implementar desde cero).
- Considerar Azure Stream Analytics solo si se requiere procesamiento complejo de streams en tiempo real.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-event-driven-v1.0) - pendiente validacion humana. No distribuir sin revision.

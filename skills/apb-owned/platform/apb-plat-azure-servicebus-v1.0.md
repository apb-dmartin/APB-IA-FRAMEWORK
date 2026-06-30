---
id: "apb-plat-azure-servicebus-v1.0"
name: "Configuración Azure Service Bus en APB"
description: "Diseña y configura namespaces, colas y topics de Azure Service Bus para integración entre sistemas APB. Define particionamiento, retención, dead-letter, políticas de acceso (SAS/Managed Identity) y patrones de mensajería asíncrona alineados con la arquitectura de eventos de APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Configuración Azure Service Bus en APB


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Diseñar la arquitectura de mensajería asíncrona entre sistemas APB usando Azure Service Bus. Cubre la configuración de namespaces, colas (point-to-point) y topics con suscripciones (pub/sub), las políticas de acceso con Managed Identity (preferido sobre SAS keys), configuración de dead-letter queues y alertas, y los patrones de mensajería adecuados para el contexto portuario (eventos de escala, tráfico, operaciones).

## Contexto de Uso
- Diseño de integración asíncrona entre dos sistemas APB (ej. GISPEM → sistema de facturación).
- Configuración de un nuevo topic para publicación de eventos de dominio (DDD event-driven).
- Revisión de la configuración de Service Bus existente para detectar problemas de rendimiento o seguridad.
- Definición de la estrategia de dead-letter y reintento para mensajes fallidos.
- Preparación de Bicep/Terraform para aprovisionamiento del namespace.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `operation` | Enum | `disenar-arquitectura` / `configurar-cola` / `configurar-topic` / `revisar-config` | ✅ |
| `integration_description` | Texto | Descripción de la integración: sistemas productor y consumidor, tipo de mensaje | ✅ |
| `message_volume` | Texto | Volumen estimado de mensajes: mensajes/hora en pico y media | ❌ |
| `pattern` | Enum | `point-to-point` / `pub-sub` / `competing-consumers` | ❌ |
| `existing_config` | JSON/Texto | Configuración actual del namespace/cola/topic (para `revisar-config`) | ❌ |

## Estándares APB para Service Bus

### Nomenclatura
```
Namespace:    sb-apb-{entorno}                    → sb-apb-prod
Cola:         {sistema-origen}-to-{sistema-dest}  → gispem-to-facturacion
Topic:        {dominio}-events                    → escalas-events, operaciones-events
Suscripción:  {sistema-consumidor}-sub            → facturacion-sub
```

### Tier recomendado
- **Premium** para prod (particionamiento dedicado, red virtual, SLA 99.9%).
- **Standard** para dev/staging.

### Configuración por defecto APB
| Parámetro | Cola (P2P) | Topic (Pub/Sub) |
|---|---|---|
| `maxSizeInMegabytes` | 5120 MB | 5120 MB |
| `defaultMessageTimeToLive` | 7 días | 7 días |
| `lockDuration` | 5 minutos | 5 minutos |
| `maxDeliveryCount` | 10 | 10 |
| `enableDeadLetteringOnMessageExpiration` | true | true |
| `requiresSession` | false (activar para orden garantizado) | false |

### Acceso — Managed Identity (obligatorio en prod)
```json
// Asignación de roles RBAC
// Productor:  "Azure Service Bus Data Sender"
// Consumidor: "Azure Service Bus Data Receiver"
// Admin:      "Azure Service Bus Data Owner" (solo automatización/ops)
// NUNCA usar SAS keys con permisos Manage en código de aplicación
```

## Flujo de Trabajo

### Diseño de arquitectura de mensajería

1. **Selección de patrón**:
   - **Point-to-point (cola)**: un productor, un consumidor. Ej: GISPEM envía escala a facturación.
   - **Pub/Sub (topic + suscripciones)**: un productor, múltiples consumidores. Ej: evento de atraque publicado, varios sistemas suscritos.
   - **Competing consumers**: múltiples instancias del mismo consumidor compiten por mensajes de la cola (escalado horizontal del consumidor).

2. **Configuración de dead-letter**:
   - Dead-letter queue activada siempre.
   - Alerta en Azure Monitor si DLQ > 0 mensajes sin consumir.
   - Proceso de revisión/reinyección de mensajes en DLQ (runbook documentado).

3. **Estrategia de reintento del consumidor**:
   - Patrón recomendado: exponential backoff con jitter.
   - `maxDeliveryCount: 10` → tras 10 intentos fallidos, el mensaje va a DLQ.
   - El consumidor debe ser idempotente (mismo mensaje procesado 2 veces → mismo resultado).

4. **Aprovisionamiento Bicep**:
   - Generar template Bicep para el namespace y las colas/topics diseñados.
   - Parámetros por entorno en `params/` folder.

5. **⚠️ CHECKPOINT HUMANO**: La arquitectura de mensajería debe revisarse con los equipos de los sistemas productor y consumidor antes de implementar.

## Salida Esperada

```markdown
# Diseño Service Bus — [Integración] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-azure-servicebus-v1.0) — pendiente revisión del equipo de plataforma APB.

## Arquitectura propuesta
[Diagrama textual o tabla con productores, colas/topics, consumidores]

## Configuración por componente
### Namespace: sb-apb-prod
### Cola/Topic: [nombre]
| Parámetro | Valor | Justificación |
|---|---|---|

## Consideraciones de seguridad
- Acceso: Managed Identity con roles RBAC específicos

## Bicep template
[Código Bicep generado]

## Alertas recomendadas
| Métrica | Umbral | Acción |
|---|---|---|
```

## Criterios de Calidad
- [ ] El patrón de mensajería es el adecuado para el caso de uso (P2P vs. Pub/Sub).
- [ ] Dead-letter queue está activada y hay proceso de gestión definido.
- [ ] El acceso usa Managed Identity, no SAS keys con permisos Manage.
- [ ] Los consumidores son idempotentes (documentado o verificado).
- [ ] Hay alertas configuradas en Azure Monitor para DLQ y throttling.

## Dependencias
- `apb-plat-secret-rotation-v1.0` — si se usan SAS keys (excepciones), deben rotar cada 90 días
- `apb-plat-environment-promotion-v1.0` — la configuración se promueve dev→staging→prod

## Ejemplo de Uso

```
Diseña la mensajería para integrar el sistema de escalas marítimas (GISPEM) con el módulo de facturación.
Cuando una escala se cierra en GISPEM, se debe notificar a facturación para generar la liquidación.
Volumen estimado: ~50 escalas/día en temporada alta. Requiere orden garantizado por escala.
```

## Notas y Advertencias
- Para orden garantizado, activar `requiresSession: true` en la cola y usar session ID = ID de la escala.
- En Premium tier, los namespaces se despliegan en red virtual — verificar que los sistemas cliente tienen acceso por red.
- Los mensajes de Service Bus no son inmutables — un mensaje modificado por error en DLQ no puede deshacerse.


## Prompt de Sistema

```
Eres el skill "Configuración Azure Service Bus en APB" (apb-plat-azure-servicebus-v1.0) del APB AI Framework,
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
Diseña y configura namespaces, colas y topics de Azure Service Bus para integración entre sistemas APB. Define particionamiento, retención, dead-letter, políticas de acceso (SAS/Managed Identity) y patrones de mensajería asíncrona alineados con la arquitectura de eventos de APB.

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
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `operation` | Pregunta: "¿Qué necesitas: diseñar arquitectura, configurar cola, configurar topic o revisar config existente?" | Sí |
| `integration_description` | Pregunta: "¿Qué sistemas se integran y qué tipo de mensaje/evento se envía?" | Sí |
| `message_volume` | Asume volumen bajo (<1000 msg/hora) y lo indica explícitamente | No |
| `pattern` | Determina el patrón según la descripción de la integración; indica la elección y su razón | No |
| `existing_config` | Solo requerido para `revisar-config` — solicita la config si falta en ese caso | Condicional |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos y diagramas** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-plat-azure-servicebus-v1.0) — pendiente revisión del equipo de plataforma APB.
- **Código Bicep/Terraform** — comentario en cabecera:
  ```bicep
  // ⚠️ Generado por APB AI Framework (apb-plat-azure-servicebus-v1.0) — revisar antes de desplegar.
  ```

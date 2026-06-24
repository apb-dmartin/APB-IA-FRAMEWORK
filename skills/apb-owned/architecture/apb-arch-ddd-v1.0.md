---
id: "apb-arch-ddd-v1.0"
name: "Identificación de Dominios DDD"
description: "Identificar y definir bounded contexts, aggregates, entities, value objects y domain services aplicando Domain-Driven Design. Facilita la alineación entre el modelo de negocio y el modelo de software."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Identificación de Dominios DDD

---

## 🎯 Propósito

Identificar y definir bounded contexts, aggregates, entities, value objects y domain services aplicando Domain-Driven Design. Facilita la alineación entre el modelo de negocio y el modelo de software.

---

## ⚡ Trigger

Al inicio de un nuevo proyecto, durante la modernización de legacy, o cuando surge ambigüedad en el lenguaje de negocio que impacta en el diseño del software.

---

## 📥 Input

- Documentación de negocio, procesos y reglas
- Entrevistas con domain experts (transcripciones o notas)
- Eventos de negocio identificados
- Sistema actual (si existe): modelo de datos, código, documentación
- Objetivos estratégicos del negocio

---

## 📤 Output

- Mapa de contextos delimitados (bounded contexts) con relaciones
- Ubiquitous Language documentado por contexto
- Modelo de dominio (aggregates, entities, value objects, domain services)
- Context map con patrones de integración (shared kernel, customer-supplier, anti-corruption layer, etc.)
- Análisis de subdominios (core, supporting, generic)

---

## 🔄 Proceso

1. **Recopilación de conocimiento**: Revisar documentación, entrevistas y procesos de negocio.
2. **Identificación del ubiquitous language**: Extraer términos clave del negocio. Detectar sinónimos y homónimos entre departamentos.
3. **Event Storming (o Big Picture)**: Mapear eventos de dominio, comandos, actores y aggregates.
4. **Definición de bounded contexts**: Agrupar elementos del modelo que comparten lenguaje y responsabilidad cohesiva.
5. **Clasificación de subdominios**: Etiquetar como core (diferenciador competitivo), supporting (necesario pero no diferenciador) o generic (commodity).
6. **Diseño del modelo dentro de cada contexto**: Definir aggregates (raíces), entities, value objects, domain services, domain events.
7. **Context Map**: Definir relaciones entre bounded contexts (partnership, shared kernel, customer-supplier, conformist, anti-corruption layer, open host service, published language).
8. **Validación con domain experts**: Revisar modelo con negocio. Ajustar según feedback.
9. **Documentación**: Generar diagramas y documento de modelo de dominio.

---

## 📋 Reglas y Constraints

- Cada bounded context debe tener un ubiquitous language único y explícitamente documentado.
- Un aggregate debe mantener sus invariantes transaccionalmente; no debe abarcar múltiples bounded contexts.
- Las entidades deben tener identidad única dentro de su aggregate. Los value objects son inmutables.
- NO mezclar lenguaje de diferentes bounded contexts en el mismo modelo de código.
- Los core domains deben recibir mayor inversión de diseño y testing.
- Los generic domains pueden considerar soluciones SaaS o de terceros antes de construir desde cero.
- Documentar decisiones de diseño en ADRs cuando haya trade-offs significativos.
- El tamaño de un aggregate debe mantenerse pequeño (regla práctica: < 10 entidades por aggregate).

---

## 🛠 Stack Tecnológico Relevante

- DDD táctico y estratégico
- Event Storming (workshop)
- Mermaid / PlantUML (diagramas)
- .NET 8/9 (implementación)
- Entity Framework Core (persistencia de aggregates)
- Azure Service Bus (domain events entre contexts)

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Plataforma de e-commerce:**
> Contextos: Catálogo, Pedidos, Pagos, Envíos, Inventario, Clientes.
> Core domain: Pedidos (proceso diferenciador con reglas complejas de descuentos).
> Generic domain: Pagos (integración con pasarela externa).
> Relación Pedidos-Inventario: Customer-Supplier (Pedidos depende de Inventario).
> Relación Pedidos-Pagos: Anti-corruption layer (modelo de pagos externo no debe contaminar Pedidos).

**Ejemplo 2 — Sistema legacy de seguros:**
> Descubrimiento: El término 'póliza' tiene significados diferentes en Suscripciones, Siniestros y Contabilidad.
> Resultado: Tres bounded contexts con ubiquitous language distinto: PolicyUnderwriting, ClaimPolicy, FinancialPolicy.
> Context map: Conformist en relación con sistema legacy (no se puede cambiar).

---

## 🔗 Dependencias

- `apb-disc-ddd-legacy-v1.0` (si parte de legacy)
- `apb-arch-event-storming-v1.0` (workshop)
- `apb-arch-decompose-v1.0` (si aplica modernización)
- `apb-doc-adr-v1.0` (documentación de decisiones)

---

## 📝 Notas

- DDD no es solo para microservicios; aplica también a monolitos modulares.
- El Event Storming es la técnica preferida en APB para descubrimiento colaborativo.
- No sobre-ingenierizar: si un bounded context tiene < 3 aggregates, evaluar si merece ser contexto independiente.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

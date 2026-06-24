---
id: "apb-disc-ddd-legacy-v1.0"
name: "Análisis DDD para Modernización"
description: "Aplicar técnicas de Domain-Driven Design para analizar sistemas legacy y descubrir dominios, bounded contexts y aggregates que guiarán la modernización. Conecta el código actual con el modelo de negocio deseado."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Análisis DDD para Modernización

---

## 🎯 Propósito

Aplicar técnicas de Domain-Driven Design para analizar sistemas legacy y descubrir dominios, bounded contexts y aggregates que guiarán la modernización. Conecta el código actual con el modelo de negocio deseado.

---

## ⚡ Trigger

Al inicio de un proyecto de modernización de legacy, o cuando se necesita reestructurar un monolito complejo.

---

## 📥 Input

- Código fuente del legacy
- Documentación de negocio (si existe)
- Entrevistas con domain experts
- Eventos de negocio identificados
- Mapa de procesos actual

---

## 📤 Output

- Mapa de bounded contexts del legacy
- Ubiquitous language por contexto
- Identificación de core domains
- Propuesta de modelo de dominio objetivo
- Análisis de gap entre modelo actual y modelo deseado
- Roadmap de modernización por dominio

---

## 🔄 Proceso

1. **Event Storming del legacy**: Mapear eventos actuales del sistema (aunque no estén implementados como eventos).
2. **Identificación de lenguaje**: Extraer términos del código y documentación. Detectar sinónimos.
3. **Mapeo de bounded contexts**: Agrupar funcionalidad cohesiva. Identificar límites naturales.
4. **Análisis de aggregates**: Identificar raíces de agregado en el código actual.
5. **Clasificación de subdominios**: Core, supporting, generic.
6. **Identificación de anti-patrones**: BBDD compartida, lógica en UI, god classes.
7. **Modelo objetivo**: Diseñar modelo de dominio deseado post-modernización.
8. **Gap analysis**: Comparar modelo actual vs objetivo. Identificar refactorings necesarios.
9. **Roadmap**: Priorizar dominios por valor y complejidad.

---

## 📋 Reglas y Constraints

- No forzar DDD si el sistema es simple; evaluar coste-beneficio.
- El modelo objetivo debe ser validado con domain experts, no solo técnicos.
- Documentar decisiones de diseño en ADRs.
- Priorizar core domains para modernización temprana.
- Los bounded contexts del legacy pueden no coincidir con los del modelo nuevo; documentar mapeo.
- Considerar strangler fig pattern para migración gradual por dominio.

---

## 🛠 Stack Tecnológico Relevante

- Event Storming
- DDD estratégico y táctico
- C4 Model
- Mermaid / PlantUML
- Análisis estático de código

---

## 💡 Ejemplos de Uso

**Ejemplo — Sistema de seguros legacy:**
> Legacy: Monolito con 40 tablas, lógica distribuida en forms y stored procedures.
> Event Storming: 35 eventos identificados.
> Bounded contexts propuestos: Underwriting, Policy, Claims, Billing, Reinsurance.
> Core domain: Claims (proceso diferenciador).
> Roadmap: Fase 1 - Claims, Fase 2 - Billing, Fase 3 - Policy.

---

## 🔗 Dependencias

- `apb-disc-reverse-code-v1.0`
- `apb-arch-ddd-v1.0`
- `apb-arch-event-storming-v1.0`
- `apb-arch-decompose-v1.0`

---

## 📝 Notas

- DDD en legacy requiere paciencia; el código actual puede no reflejar el dominio de negocio.
- Considerar 'bubble context' para introducir nuevo modelo sin alterar legacy inicialmente.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

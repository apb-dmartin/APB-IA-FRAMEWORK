---
id: "apb-dev-implement-v1.0"
name: "Implementación de Código"
description: "Generar código de alta calidad siguiendo estándares corporativos, patrones de diseño y principios SOLID. Incluye implementación de features, refactoring controlado y adaptación a plantillas corporativas."
version: "1.0.0"
status: "draft"
owner: "Desarrollo <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Implementación de Código

---

## 🎯 Propósito

Generar código de alta calidad siguiendo estándares corporativos, patrones de diseño y principios SOLID. Incluye implementación de features, refactoring controlado y adaptación a plantillas corporativas.

---

## ⚡ Trigger

Cuando se requiere implementar una nueva feature, corregir un bug, o refactorizar código existente basado en especificaciones técnicas.

---

## 📥 Input

- Especificación técnica o historia de usuario
- Arquitectura de referencia del componente
- Contrato API o evento asociado
- Código base existente (contexto)
- Estándares de codificación APB
- Plantilla de proyecto (si aplica)

---

## 📤 Output

- Código fuente implementado
- Tests unitarios asociados (mínimo cobertura 80%)
- Documentación inline (XML docs en C#)
- Notas de implementación (decisiones técnicas, deuda técnica)
- Checklist de cumplimiento de estándares

---

## 🔄 Proceso

1. **Análisis de requisitos**: Comprender la especificación, identificar edge cases y dependencias.
2. **Diseño de la solución**: Elegir patrones de diseño apropiados. Definir interfaces y contratos.
3. **Implementación**: Escribir código siguiendo estándares APB. Usar plantillas corporativas.
4. **Testing unitario**: Implementar tests que cubran camino feliz, edge cases y casos de error.
5. **Revisión de calidad**: Verificar contra SonarQube rules, estándares de nombres, complejidad ciclomática.
6. **Documentación**: Añadir XML docs, comentarios de negocio donde sea necesario.
7. **Preparación de PR**: Crear descripción clara, enlazar a ticket, incluir evidencia de tests.

---

## 📋 Reglas y Constraints

- Seguir principios SOLID, DRY, KISS.
- Métodos máximo 30 líneas; clases máximo 500 líneas (regla orientativa).
- Complejidad ciclomática máxima 10 por método.
- Inyección de dependencias obligatoria; no usar new() para servicios.
- Async/await en todas las operaciones I/O.
- No usar excepciones para control de flujo.
- Logging estructurado con Serilog; niveles apropiados (Debug, Info, Warning, Error).
- No hardcodear strings de conexión, URLs ni secretos; usar IConfiguration + Key Vault.
- Todos los métodos públicos deben tener tests unitarios.
- Preferir LINQ y expresiones funcionales cuando mejoren legibilidad.
- No dejar código comentado; usar control de versiones para historia.

---

## 🛠 Stack Tecnológico Relevante

- .NET 8/9, C# 12
- ASP.NET Core
- Entity Framework Core
- xUnit / NUnit, Moq, FluentAssertions
- Serilog, Application Insights
- Azure Service Bus (Azure.Messaging.ServiceBus)
- AutoMapper (con validación de configuración)
- FluentValidation

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — Implementar endpoint de creación de pedido:**
> POST /api/v1/orders
> Controller → Mediator → Handler → Repository → Domain Service
> Validación con FluentValidation, mapeo con AutoMapper, evento de dominio OrderCreated publicado a Service Bus.

**Ejemplo 2 — Refactorizar servicio legacy:**
> Extraer lógica de negocio de controller a Application Service.
> Introducir Repository Pattern, eliminar consultas SQL en línea.
> Añadir tests unitarios para lógica extraída.

---

## 🔗 Dependencias

- `apb-dev-code-base-v1.0` (análisis previo)
- `apb-dev-micro-base-v1.0` (scaffold)
- `apb-dev-code-review-v1.0` (revisión posterior)
- `apb-dev-api-standard-v1.0

---

## 📝 Notas

- Esta skill no reemplaza al desarrollador humano; asiste en la generación y revisión de código.
- Para código complejo o crítico, siempre requerir revisión de par humano.
- Mantener coherencia con el estilo existente del proyecto.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Especificación técnica o historia de usuario` | Pregunta: "¿Puedes proporcionar especificación técnica o historia de usuario?" | Sí |
| `Arquitectura de referencia del componente` | Pregunta: "¿Puedes proporcionar arquitectura de referencia del componente?" | Sí |
| `Contrato API o evento asociado` | Pregunta: "¿Puedes proporcionar contrato api o evento asociado?" | Sí |
| `Código base existente` | Pregunta: "¿Puedes proporcionar código base existente?" | Sí |
| `Estándares de codificación APB` | Pregunta: "¿Puedes proporcionar estándares de codificación apb?" | Sí |
| `Plantilla de proyecto` | Continúa con la información disponible — indica qué asumió | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Código generado** — primera línea del bloque: `// [IA-GEN] Generado por APB AI Framework (apb-dev-implement-v1.0) — pendiente revisión humana`
- **Commit** — prefijo `[ai-gen]` en el mensaje + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`
- **PR asociado** — label `ai-generated` en GitHub + footer en descripción del PR

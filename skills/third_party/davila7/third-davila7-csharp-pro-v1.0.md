---
id: "third-davila7-csharp-pro-v1.0"
name: "Skill: C# Modern Patterns (davila7/claude-code-templates)"
description: "Guía de referencia de características modernas de C# (records, pattern matching, nullable reference types, async/await) y principios SOLID aplicados a aplicaciones .NET de nivel enterprise, adaptada del repositorio público davila7/claude-code-templates."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
source_repo: "https://github.com/davila7/claude-code-templates"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: C# Modern Patterns (davila7/claude-code-templates)

---

## Descripción
Adaptación de la skill `csharp-pro` del repositorio público
`davila7/claude-code-templates` (MIT). El contenido original es una guía
genérica de buenas prácticas de C# moderno: características del lenguaje
(records, pattern matching, nullable reference types), principios SOLID,
gestión de memoria/rendimiento (`Span`, `Memory`), programación asíncrona
con TPL, y patrones de testing (xUnit, NUnit, Moq, FluentAssertions). Se
incorpora como referencia transversal de calidad de código C#, complementaria
a `third-davila7-dotnet-backend-v1.0` (que cubre patrones de servicio backend
concretos, no el lenguaje en sí).

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del mismo
> agregador `davila7/claude-code-templates` que `dotnet-backend`. El
> contenido original es notablemente más genérico (plantilla autogenerada,
> `risk: unknown`, `source: community`) que `dotnet-backend`: se incorpora
> con menor densidad de detalle propio y debe tratarse como checklist de
> referencia, no como fuente primaria de patrones.

## Capacidades
- Checklist de uso de características modernas de C# (records, pattern
  matching, nullable reference types) para código idiomático
- Principios SOLID y favorecer composición sobre herencia en diseño de clases
- Pautas de optimización de rendimiento (`Span<T>`, `Memory<T>`, value types)
- Patrones de programación asíncrona sin bloqueo (`async`/`await`, TPL)
- Checklist de cobertura de testing con mocking apropiado (xUnit/NUnit/Moq)

## Inputs
- `codigo_csharp`: código C# a revisar o generar
- `contexto_calidad`: criterios de calidad aplicables (cobertura de tests,
  nivel de nullable reference types exigido, etc.)

## Outputs
- `recomendaciones_estilo`: ajustes sugeridos según características modernas
  de C# y principios SOLID
- `checklist_testing`: cobertura de pruebas recomendada para el código

## Restricciones
- El contenido original es deliberadamente genérico (sin ejemplos extensos
  de código, a diferencia de `dotnet-backend`); su valor es como checklist
  de revisión, no como generador de implementaciones completas
- No sustituye `apb-dev-review-tl-v1.0` ni `apb-dev-review-advanced-v1.0`
  (revisión técnica APB): esta skill aporta criterios de calidad C#
  específicos del lenguaje, no el proceso de revisión completo de APB

## Adaptaciones APB
- Usar como checklist complementario dentro de `apb-dev-review-tl-v1.0` al
  revisar código C#/.NET, no como skill invocada de forma independiente
- Conectar con `apb-sub-dev-net-v1.0` (subagente .NET) como consumidor
  natural

## Ejemplo de Uso
```
Invocar: third-davila7-csharp-pro-v1.0
Input: { codigo_csharp: "<fragmento de servicio .NET>",
         contexto_calidad: "Nullable reference types obligatorio, cobertura xUnit >= 80%" }
Output: Lista de ajustes recomendados (records, pattern matching, async
        correcto) y checklist de testing pendiente
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

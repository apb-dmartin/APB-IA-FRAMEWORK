---
id: "prov-dotnet-test-runner-v1.0"
name: "Provider: Dotnet Test Runner (BuiltInTool de Mother)"
description: "Proveedor de acción para compilar y ejecutar la suite de tests (xUnit/NUnit) de un proyecto o solución .NET y devolver el resultado real (pass/fail/skipped), en vez de una afirmación sin verificar."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-only"
created_date: "2026-11-23"
review_date: "2026-11-23"
---

# Provider: Dotnet Test Runner (BuiltInTool de Mother)

---

## Descripción

Compila (`dotnet build`) y ejecuta (`dotnet test --logger trx`) un proyecto o solución
.NET ya presente en disco, parsea el `.trx` resultante y devuelve un resumen verificado:
número de tests, pass/fail/skipped, duración y el detalle de los tests fallidos. No
inventa ni asume resultados — si el runner no está disponible o la ruta no es válida, lo
declara explícitamente en vez de generar un informe de inspección estática disfrazado de
ejecución real.

## Capacidades

| Acción | Descripción | Gate humano |
|--------|-------------|--------------|
| `run_tests` | Compila y ejecuta los tests de un proyecto/solución bajo una ruta permitida | No (solo lectura: no modifica el repo) |

## Mecanismo real

**No es un servidor MCP** — es un `BuiltInTool` de Mother (mismo patrón que
`PlaywrightSmokeTool`: una función C# expuesta directamente al agente, sin proceso
externo que mantener). Internamente lanza `dotnet build` y `dotnet test --logger
"trx;LogFileName=result.trx"` como subproceso, sobre una ruta que Mother valida contra una
lista blanca de raíces de repos conocidos (nunca una ruta arbitraria que el agente
invente). El agente nunca compone el comando ni pasa flags libres — solo indica qué
proyecto/solución quiere testear.

## Configuración

```json
{
  "provider_id": "prov-dotnet-test-runner-v1.0",
  "type": "action",
  "mechanism": "builtin_tool",
  "builtin_tool_name": "dotnet-test-runner",
  "allowed_roots": ["<configurado en Mother, nunca arbitrario>"],
  "permissions": ["read"]
}
```

## Inputs

- `project_or_solution_path`: ruta relativa a una de las raíces permitidas (`.csproj`,
  `.sln` o directorio con uno de ellos).

## Outputs

- `{ total, passed, failed, skipped, duration_ms, failed_tests: [{name, message}] }`
- Si la ruta no está en la lista blanca o el build falla: error explícito, nunca un
  resultado simulado.

## Dependencias

- `apb-qa-post-migration-v1.0` (tests funcionales y de regresión del plan de validación)
- `apb-qa-test-auto-v1.0` (ejecución de la suite generada)

## Restricciones

- Solo ejecuta `dotnet build`/`dotnet test` sobre rutas pre-aprobadas — nunca un comando
  arbitrario ni argumentos libres del agente.
- No modifica código ni commitea nada; solo lee el resultado de la ejecución.
- No sustituye a CI/CD — es para validación asistida dentro de una ejecución de agente,
  no para gatear despliegues (eso sigue siendo responsabilidad del pipeline).

## Ejemplo de Uso

```
Invocar: prov-dotnet-test-runner-v1.0
Action: run_tests
ProjectOrSolutionPath: "Backend.Api.Tests/Backend.Api.Tests.csproj"
→ { total: 42, passed: 40, failed: 2, skipped: 0, duration_ms: 8341,
    failed_tests: [{name: "..", message: ".."}] }
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-11-23 | Claude (Anthropic), a petición de Débora | Creación: cierra el hueco detectado en la ejecución `ba29cf9d7d254080bdc645ff3779abf3` (apb-qa-post-migration sin runner de tests) |

---
*Registrado en APB AI Framework.*

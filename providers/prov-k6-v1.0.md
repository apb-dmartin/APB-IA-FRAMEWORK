---
id: "prov-k6-v1.0"
name: "Provider: k6 Load Test (BuiltInTool de Mother)"
description: "Proveedor de acción para pruebas de rendimiento con k6: ejecuta un script k6 ya generado y guardado por el agente, y devuelve las métricas reales (p95, error rate, RPS) comparadas contra umbrales."
version: "2.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-only"
created_date: "2026-06-20"
review_date: "2026-11-23"
---

# Provider: k6 Load Test (BuiltInTool de Mother)

---

> **Nota de reescritura (v2.0.0, 2026-11-23, a petición de Débora):** la v1.0.0 era
> aspiracional, igual que le pasaba a `prov-sonar-v1.0` antes de su reescritura: un
> `endpoint: "local://k6"` sin mecanismo real detrás, `auth: "none"` sin sentido para un
> proceso local, y `environments: ["local", "staging", "production"]` dando a entender que
> cualquier agente podía lanzar carga contra producción. Ninguna skill del catálogo
> (ni siquiera `apb-qa-performance-v1.0`, la skill *de k6*) declaraba este provider en su
> `depends_on`, y Mother no tenía ningún servidor/tool que lo conectara — por eso la
> validación post-migración `ba29cf9d7d254080bdc645ff3779abf3` no pudo ejecutar k6 pese a
> que el provider "existía" en el catálogo. Esta versión documenta el mecanismo real: un
> `BuiltInTool` de Mother (mismo patrón que `PlaywrightSmokeTool`), no un MCP ni un
> endpoint genérico, acotado a `access_mode: read-only` (solo lee el resultado; el riesgo
> de "escritura" real es la carga generada contra el objetivo, controlada por el script).

## Descripción

Ejecuta un script k6 (`.js`) ya escrito y guardado en disco por el propio agente (con las
herramientas de fichero que ya tiene — nunca código k6 arbitrario ejecutado a ciegas sin
pasar antes por disco y quedar auditable), contra una URL objetivo, y devuelve las
métricas resumidas (p95 de latencia, tasa de error, RPS) comparadas contra los umbrales
que el script define. No ejecuta carga contra producción salvo aprobación humana explícita
registrada en la propia ejecución.

## Capacidades

| Acción | Descripción | Gate humano |
|--------|-------------|--------------|
| `run_load_test` | Ejecuta un script k6 existente contra un objetivo y devuelve métricas | Sí, si el objetivo es producción |

## Mecanismo real

**No es un servidor MCP** — es un `BuiltInTool` de Mother que lanza el binario `k6`
(`k6 run --summary-export=<tmp>.json <script>`) como subproceso y parsea el JSON de
resumen. Requiere el binario `k6` instalado en el host donde corre Backend.Api (no se
distribuye vía `npx`/`uvx` como github/jira). El agente nunca compone la línea de comando:
solo indica la ruta del script (que él mismo generó) y, si el script la parametriza, la URL
objetivo — ambas validadas antes de lanzar el proceso.

## Configuración

```json
{
  "provider_id": "prov-k6-v1.0",
  "type": "action",
  "mechanism": "builtin_tool",
  "builtin_tool_name": "k6-load-test",
  "requires_host_binary": "k6",
  "permissions": ["read"],
  "production_requires_human_gate": true
}
```

## Inputs

- `script_path`: ruta al script k6 ya generado por el agente (bajo una raíz permitida).
- `target_url`: URL objetivo (debe coincidir con la declarada al lanzar la ejecución).

## Outputs

- `{ p95_ms, error_rate, rps, thresholds_passed: bool, raw_summary }`

## Dependencias

- `apb-qa-performance-v1.0` (skill — diseña el script y define los umbrales)
- `apb-qa-post-migration-v1.0` (validación de rendimiento comparativa)

## Restricciones

- No ejecuta en producción sin aprobación humana explícita registrada en la ejecución.
- Requiere el binario `k6` instalado en el host de Mother (prerrequisito de
  infraestructura, documentado junto a `uv`/`uvx` para Jira).
- El script siempre pasa primero por disco (generado y guardado por el agente) antes de
  ejecutarse — nunca código k6 inline sin ese paso intermedio auditable.
- Datos usados en el script deben estar anonimizados si provienen de producción.

## Ejemplo de Uso

```
Invocar: prov-k6-v1.0
Action: run_load_test
ScriptPath: "tests/perf/api-load.js"
TargetUrl: "https://staging.example.apb/api/..."
→ { p95_ms: 180, error_rate: 0.002, rps: 42.3, thresholds_passed: true, raw_summary: {...} }
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial (aspiracional, sin mecanismo real) |
| 2.0.0 | 2026-11-23 | Claude (Anthropic), a petición de Débora | Reescritura completa: mecanismo real (BuiltInTool de Mother ejecutando el binario `k6`, no `local://k6` genérico), `access_mode: read-only`, gate humano explícito para producción, requisito de binario en el host documentado |

---
*Registrado en APB AI Framework.*

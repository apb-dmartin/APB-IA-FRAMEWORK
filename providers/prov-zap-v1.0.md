---
id: "prov-zap-v1.0"
name: "Provider: OWASP ZAP Baseline Scan"
description: "Proveedor de acción para escaneo DAST con OWASP ZAP (modo baseline) contra una URL objetivo, devolviendo alertas de seguridad por riesgo/confianza."
version: "1.0.0"
status: "draft"
owner: "Seguridad APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-11-23"
review_date: "2026-11-23"
---

# Provider: OWASP ZAP Baseline Scan

---

> **Estado: diseño documental, no implementado.** A diferencia de los demás providers
> QA añadidos junto a este (`prov-dotnet-test-runner-v1.0`, `prov-axe-core-v1.0`,
> `prov-k6-v1.0`, `prov-sql-readonly-v1.0`), este **no tiene BuiltInTool implementado en
> Mother todavía**. ZAP es un escáner DAST: ataca activamente la URL objetivo (fuzzing de
> parámetros, pruebas de inyección, forzado de rutas) para encontrar vulnerabilidades, lo
> que lo distingue de todo lo demás añadido en este cambio (que solo lee resultados o
> ejecuta una carga controlada por script propio). Implementarlo requiere que el usuario
> confirme explícitamente, por escrito y por ejecución: (a) qué URL es un objetivo válido
> (nunca producción sin aprobación de Seguridad APB), (b) en qué ventana de tiempo, y
> (c) quién revisa las alertas antes de que lleguen a ningún informe distribuible.

## Descripción

Lanza un escaneo "baseline" de OWASP ZAP (pasivo + spidering ligero, no el modo "full scan"
activo más agresivo) contra una URL objetivo usando la imagen oficial
`zaproxy/zap-stable` (`zap-baseline.py`), y devuelve las alertas encontradas agrupadas por
nivel de riesgo (`High`/`Medium`/`Low`/`Informational`) y confianza.

## Capacidades (propuestas, no implementadas)

| Acción | Descripción | Gate humano |
|--------|-------------|--------------|
| `baseline_scan` | Escaneo baseline de ZAP contra una URL objetivo | **Sí, siempre** — nunca autónomo |

## Mecanismo real propuesto

Imagen oficial `zaproxy/zap-stable`, script `zap-baseline.py -t <url> -J report.json`.
Se ejecutaría como `BuiltInTool` de Mother (mismo patrón que el resto), nunca como MCP
genérico de shell. Requiere Docker (o el binario ZAP) en el host.

## Restricciones (no negociables antes de implementar)

- **Nunca** contra producción sin aprobación explícita y documentada de Seguridad APB.
- **Nunca** autónomo: el gate humano de la tabla de Capacidades aplica siempre, no solo a
  producción — es un escaneo activo, no una lectura.
- El objetivo debe ser una URL que el usuario confirme por escrito en cada ejecución, no
  una que el agente decida por sí mismo a partir del contexto de la tarea.
- Las alertas encontradas pueden incluir información sensible (rutas internas, stack
  traces) — no deben salir de un informe interno sin revisión.

## Dependencias

- `apb-qa-post-migration-v1.0` ("validación de seguridad: verificar permisos, roles,
  encriptación")

## Estado de este provider

Queda registrado en el catálogo para que el `depends_on` de las skills de seguridad pueda
referenciarlo cuando exista decisión e implementación, pero **no se añade a ningún
`depends_on` todavía** ni se implementa el `BuiltInTool` en Mother hasta que el usuario
confirme el alcance.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-11-23 | Claude (Anthropic), a petición de Débora | Creación como diseño documental únicamente — pendiente de aprobación explícita de objetivo/entorno antes de implementar |

---
*Registrado en APB AI Framework.*

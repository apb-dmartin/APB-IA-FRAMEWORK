---
id: "prov-context7-v1.0"
name: "Provider: Context7 (documentación actualizada para LLMs)"
description: "Proveedor de contexto de solo lectura que inyecta documentación de librerías y frameworks actualizada y versionada en el prompt de agentes/skills, vía el servidor MCP Context7 (upstash/context7, MIT). Reduce alucinaciones y APIs obsoletas al desarrollar sobre dependencias externas. Agnóstico de LLM: se declara en el .mcp.json de proyecto, como el resto de MCP del framework."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "platform"
provider_type: "context"
access_mode: "read-only"
source_repo: "https://github.com/upstash/context7"
source_license: "MIT"
source_commit: "84620bd48380b1cac66b9b25180987116e2ce2fe"
created_date: "2026-07-04"
review_date: "2026-07-04"
---

# Provider: Context7 (documentación actualizada para LLMs)

> **Herramienta de contexto de solo lectura.** No escribe en ningún sistema APB; solo aporta
> documentación de librerías al prompt. Fuente de verdad del código sigue siendo Git
> (Principios #4/#6) — Context7 es un insumo de contexto, no un repositorio de conocimiento APB.

---

## Descripción

Context7 (`upstash/context7`, MIT) es un **servidor MCP** que resuelve el ID de una librería y
devuelve su documentación **actualizada y por versión** para inyectarla en el contexto del
modelo. Cubre el gap del bloque #27 ("contexto enriquecido para LLM, nunca evaluado"): al
generar o revisar código sobre dependencias externas (.NET, JS/TS, Python del stack APB), el
agente consulta la documentación vigente en vez de basarse en su conocimiento congelado,
reduciendo APIs inventadas u obsoletas.

## Activación (norma del framework — MCP conceptual → real)

Conforme a la norma fijada por Débora (memoria `feedback_mcp_framework_activacion`), al activar
de verdad este MCP:
1. Declararlo en el **`.mcp.json` de proyecto** (versionado en el repo), no solo en la sesión
   de usuario, junto al resto de servidores MCP.
2. Actualizar este descriptor con la configuración real verificada (hoy `draft`, sin activar).

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

## Capacidades

- Resolver el ID de una librería/framework a partir de su nombre.
- Recuperar documentación actualizada y filtrada por versión/tema.
- Inyectar ese contexto en el prompt del agente/skill que lo solicita.

## Restricciones

- **Solo lectura / solo contexto:** no ejecuta acciones ni escribe en sistemas APB.
- No sustituye a `prov-apb-knowledge-v1.0` (contexto corporativo interno) — son complementarios:
  APB knowledge = dominio portuario propio; Context7 = documentación pública de terceros.
- Verificar que la documentación recuperada no contamine decisiones de arquitectura con
  tecnologías fuera del stack aprobado (`STANDARD_ARCHITECTURE.md`).
- Autonomy Level 1: el contexto recuperado es un insumo; el humano valida el output final.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-04 | Arquitectura APB | Incorporación (Sesión 19, punto #27) — provider MCP de contexto, `draft` sin activar |

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*

---
id: "third-sickn33-ddd-context-mapping-v1.0"
name: "Skill: DDD Context Mapping (antigravity-awesome-skills)"
description: "Mapeo de relaciones entre bounded contexts y definición de contratos de integración mediante patrones de Context Mapping de DDD (Partnership, Customer-Supplier, Conformist, Anti-Corruption Layer), adaptado del repositorio público sickn33/antigravity-awesome-skills."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
source_repo: "https://github.com/sickn33/antigravity-awesome-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: DDD Context Mapping (antigravity-awesome-skills)

---

## Descripción
Adaptación de la skill `ddd-context-mapping` del repositorio público
`sickn33/antigravity-awesome-skills` (MIT para código/tooling; contenido sin
atribución externa adicional, autoría `self`). El contenido original define
los siete patrones clásicos de Context Mapping de Eric Evans (Partnership,
Shared Kernel, Customer-Supplier, Conformist, Anti-Corruption Layer, Open
Host Service, Published Language) y una plantilla de matriz de relaciones
entre contextos.

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del agregador
> `sickn33/antigravity-awesome-skills`. El original referencia skills
> hermanas del mismo bundle que no existen en APB (`@ddd-strategic-design`,
> `@projection-patterns`, etc.); este descriptor **sustituye esas
> referencias por componentes APB reales** (ver sección Adaptaciones) en
> lugar de copiarlas tal cual, para evitar enlaces rotos en el catálogo.
> Complementa a `apb-disc-ddd-legacy-v1.0` (análisis DDD de legacy): esa
> skill identifica bounded contexts durante el descubrimiento; esta cubre
> el diseño explícito de cómo esos contextos se integran entre sí.

## Capacidades
- Identificación de pares de contextos y dirección de dependencia
  (upstream/downstream)
- Selección de patrón de relación por par de contextos (los siete patrones
  clásicos de Context Mapping)
- Definición de reglas de traducción y límites de propiedad de contrato
- Checklist de Anti-Corruption Layer: modelo canónico, traducción de
  términos externos al lenguaje ubicuo local, código de ACL en el límite

## Inputs
- `contextos_implicados`: lista de bounded contexts a relacionar (ej.
  Escalas, Facturación, Aduanas)
- `relaciones_conocidas`: integraciones ya existentes o planificadas entre
  esos contextos

## Outputs
- `mapa_relaciones`: matriz de pares de contexto con patrón asignado
- `matriz_propiedad_contrato`: quién es dueño de cada contrato de
  integración
- `decisiones_acl`: dónde se necesita Anti-Corruption Layer y qué traduce

## Restricciones
- No sustituye el diseño de esquema API a nivel de detalle (eso corresponde
  a `apb-arch-api-contract-v1.0`); esta skill opera a nivel de relación
  entre contextos, no de contrato técnico línea a línea
- No garantiza alineamiento organizativo por sí sola: el mapeo debe
  revisarse cuando cambie la propiedad de los equipos sobre cada contexto

## Adaptaciones APB
- Las referencias originales a `@ddd-strategic-design` y
  `@projection-patterns` (skills del bundle original, inexistentes en APB)
  se sustituyen por: `apb-disc-ddd-legacy-v1.0` para el descubrimiento
  estratégico previo, y `third-sickn33-event-store-design-v1.0` cuando el
  contexto downstream requiera proyecciones de eventos
- Usar la matriz de relaciones como insumo de
  `apb-arch-api-contract-v1.0` al formalizar los contratos detectados como
  Open Host Service o Published Language

## Ejemplo de Uso
```
Invocar: third-sickn33-ddd-context-mapping-v1.0
Input: { contextos_implicados: ["Escalas", "Facturación", "Aduanas"],
         relaciones_conocidas: ["Facturación consume datos de Escalas"] }
Output: Matriz de relaciones con patrón asignado por par (ej. Escalas→
        Facturación: Customer-Supplier), propiedad de contrato, y
        decisiones de ACL donde aplique
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

# APB Domain Catalog — Integración como Submodule

> **Sesión:** 18 — DDD Domain Catalog
> **Fecha:** 2026-06-25

El APB Domain Catalog vive en un repo independiente:
`https://github.com/apb-dmartin/APB-DOMAIN-CATALOG`

Se integra en APB-IA-FRAMEWORK como **git submodule** en la carpeta `domain-catalog/`.

---

## Inicialización (primera vez)

```bash
# Desde la raíz de APB-IA-FRAMEWORK
git submodule add https://github.com/apb-dmartin/APB-DOMAIN-CATALOG domain-catalog
git commit -m "feat: añadir apb-domain-catalog como submodule"
```

## Actualización del submodule

```bash
git submodule update --remote domain-catalog
git add domain-catalog
git commit -m "chore: actualizar submodule apb-domain-catalog"
```

## Clonar el repo con el submodule

```bash
git clone --recurse-submodules https://github.com/apb-dmartin/APB-IA-FRAMEWORK
# O si ya está clonado:
git submodule update --init --recursive
```

## Uso por el agente DDD

El agente `apb-agent-ddd-v1.0` lee `domain-catalog/catalog/DOMAINS.md` antes de proponer cualquier dominio, para evitar duplicados con los dominios ya aprobados.

Ruta de referencia dentro del framework: `domain-catalog/catalog/DOMAINS.md`

---

## Estado actual del submodule

- **Submodule añadido:** pendiente de ejecutar `git submodule add` (ver instrucciones arriba)
- **Razón:** el repo `APB-DOMAIN-CATALOG` se creó en la Sesión 18 (2026-06-25). El submodule debe añadirse manualmente desde terminal.

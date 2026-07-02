# AGENTS.md — Routing file del harness (plantilla)

> ⚠️ **Borrador generado por IA** (APB AI Framework — scaffold harness-ready) — pendiente validación humana.
>
> **Plantilla.** Copiar a la raíz del repositorio destino y completar. Regla de oro:
> **entre 50 y 200 líneas** (SYSTEM.md §10.3 — evitar "Lost in the Middle").
> Este archivo es la **fuente canónica** de instrucciones para cualquier agente/LLM;
> las vistas por runtime (`CLAUDE.md`, config de Copilot, Rovo…) derivan de él.

## Qué es este sistema

{1–3 frases: nombre, propósito de negocio, equipo propietario.}

## Stack y restricciones no negociables

- **Stack aprobado:** {lenguajes, frameworks, versiones exactas}
- **Prohibido:** {tecnologías/patrones vetados — p. ej. fuera del stack DOCKS}
- **Políticas aplicables:** {enlaces a context/apb/policies/ o equivalente}

## Cómo está organizado

| Ruta | Contenido |
|---|---|
| `{src/…}` | {qué hay} |
| `{docs/…}` | Documentación temática — leer **bajo demanda**, no precargar |

## Cómo se ejecuta

```
{comando(s) de arranque / build}
```

## Cómo se verifica

```
{comando de tests + lint — el que usa el Pass-State Gating}
```

- Ningún cambio se da por bueno sin ejecutar esta verificación (GOVERNANCE.md §8.1).

## Dónde estamos ahora

- Estado persistente: ver [`PROGRESS.md`](PROGRESS.md) (Contrato de Bootstrap).
- Funcionalidades y su estado: ver [`FEATURES.md`](FEATURES.md).

## Reglas de trabajo del agente

1. **WIP=1:** una sola tarea activa a la vez.
2. **Razonar → plan → aceptación → ejecutar** (PROMPTING_STANDARD v1.0).
3. Cada tarea lógica = un commit único; solo commitear con verificación en verde (ACID).
4. Al terminar la sesión: Clean State Handoff (GOVERNANCE.md §8.3) y actualizar `PROGRESS.md`.

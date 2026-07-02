# PROGRESS.md — Estado persistente entre sesiones (plantilla)

> ⚠️ **Borrador generado por IA** (APB AI Framework — scaffold harness-ready) — pendiente validación humana.
>
> **Plantilla.** Este archivo implementa el **Contrato de Bootstrap** (SYSTEM.md §10.4):
> cada sesión nueva lo lee ANTES de trabajar y lo actualiza AL CERRAR (con evidencia).
> Si no está aquí, no existe para la siguiente sesión (System of Record, SYSTEM.md §10.2).

## Contrato de Bootstrap — estado actual

| Campo | Valor |
|---|---|
| **Último commit estable** | `{sha}` — {fecha} |
| **Tasa de pruebas** | {N}/{M} pasando (`{comando de verificación}`) |
| **Tarea activa (WIP=1)** | {id/descripción de la ÚNICA tarea en curso, o "ninguna"} |
| **Bloqueadores** | {lista o "ninguno"} |
| **Próximas acciones** | 1. {…} 2. {…} |

## Registro de sesiones (más reciente primero)

### {AAAA-MM-DD} — {título de la sesión}

- **Hecho:** {qué se completó, con evidencia: commit, test, artefacto}
- **Verificación:** {comando ejecutado y resultado}
- **Pendiente que queda:** {qué NO se terminó y por qué}
- **Clean State:** build ✅/❌ · tests ✅/❌ · progreso ✅/❌ · artefactos ✅/❌ · inicio ✅/❌

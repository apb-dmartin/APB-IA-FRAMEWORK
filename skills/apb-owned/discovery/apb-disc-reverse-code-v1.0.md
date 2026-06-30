---
id: "apb-disc-reverse-code-v1.0"
name: "Ingeniería Inversa desde Código"
description: "Analizar código fuente de sistemas legacy para extraer arquitectura, dependencias, reglas de negocio embebidas y comportamiento actual. Genera artefactos de comprensión para modernización."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Ingeniería Inversa desde Código


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Analizar código fuente de sistemas legacy para extraer arquitectura, dependencias, reglas de negocio embebidas y comportamiento actual. Genera artefactos de comprensión para modernización.

---

## ⚡ Trigger

Cuando no existe documentación actualizada de un sistema legacy, o cuando la documentación no refleja el comportamiento real del código en producción.

---

## 📥 Input

- Código fuente completo del sistema
- Base de datos (schema, datos de muestra)
- Configuración de despliegue
- Logs de ejecución (si disponibles)
- Tests existentes (si hay)

---

## 📤 Output

- Diagrama de arquitectura actual (C4 nivel 2-3)
- Mapa de dependencias entre componentes
- Inventario de reglas de negocio embebidas en código
- Identificación de deuda técnica crítica
- Propuesta de bounded contexts (si aplica modernización)
- Documentación de APIs y puntos de integración

---

## 🔄 Proceso

1. **Análisis de estructura**: Mapear proyectos, namespaces, capas, dependencias.
2. **Análisis de dependencias**: Identificar referencias entre proyectos, librerías de terceros, servicios externos.
3. **Análisis de datos**: Schema de BBDD, relaciones, stored procedures, triggers.
4. **Extracción de reglas de negocio**: Identificar lógica de negocio en controllers, services, stored procedures.
5. **Análisis de flujo**: Mapear flujos de ejecución principales (user journeys técnicos).
6. **Identificación de deuda técnica**: Código duplicado, dependencias obsoletas, anti-patrones.
7. **Documentación de APIs**: Endpoints, contratos, autenticación.
8. **Síntesis**: Generar diagramas y documentación estructurada.
9. **Validación**: Contrastar con stakeholders técnicos.

---

## 📋 Reglas y Constraints

- No modificar código durante el análisis; solo lectura.
- Documentar suposiciones explícitamente cuando el código sea ambiguo.
- Identificar 'magic numbers', strings hardcodeados y lógica embebida en UI.
- Mapear stored procedures como reglas de negocio críticas.
- Detectar código muerto (no referenciado) pero no eliminarlo; documentar.
- Priorizar comprensión de flujos críticos de negocio sobre detalles técnicos.
- Mantener confidencialidad; el análisis puede exponer lógica sensible.

---

## 🛠 Stack Tecnológico Relevante

- Análisis estático: SonarQube, NDepend, Roslyn analyzers
- Decompiladores (si no hay código fuente)
- Diagramas: C4, dependency graphs
- SQL Server / PostgreSQL schema analysis
- Git history (para entender evolución)

---

## 💡 Ejemplos de Uso

**Ejemplo — Análisis de aplicación VB6:**
> Estructura: 12 forms, 8 módulos, 15 clases.
> Dependencias: ADO, Crystal Reports, librería propietaria de impresión.
> Reglas de negocio: 23 identificadas, 8 en stored procedures SQL.
> Deuda técnica: 5 dependencias sin soporte, 3 forms con > 2000 líneas.
> Output: Diagrama de componentes, lista de reglas, propuesta de extracción por bounded contexts.

---

## 🔗 Dependencias

- `apb-disc-reverse-doc-v1.0`
- `apb-arch-decompose-v1.0`
- `apb-dev-code-base-v1.0`

---

## 📝 Notas

- El análisis de código legacy puede ser complejo; considerar herramientas especializadas por lenguaje.
- Para sistemas muy grandes, priorizar módulos críticos y hacer análisis iterativo.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Código fuente completo del sistema` | Pregunta: "¿Puedes proporcionar código fuente completo del sistema?" | Sí |
| `Base de datos` | Pregunta: "¿Puedes proporcionar base de datos?" | Sí |
| `Configuración de despliegue` | Pregunta: "¿Puedes proporcionar configuración de despliegue?" | Sí |
| `Logs de ejecución` | Continúa con la información disponible — indica qué asumió | No |
| `Tests existentes` | Continúa con la información disponible — indica qué asumió | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-disc-reverse-code-v1.0) - pendiente validacion humana. No distribuir sin revision.

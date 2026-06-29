---
id: "apb-arch-context-mapping-v1.0"
name: "Mapas de Contexto DDD"
description: "Genera y documenta los Mapas de Contexto de Domain-Driven Design (DDD) para los sistemas APB. Identifica los Bounded Contexts, sus relaciones (ACL, Shared Kernel, Customer-Supplier, Conformist, OHS, Published Language) y el modelo de integración entre dominios del Puerto de Barcelona."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Mapas de Contexto DDD

## Propósito
Documentar las fronteras y relaciones entre los dominios de negocio de APB usando el Context Map de Domain-Driven Design. Permite entender cómo se relacionan los sistemas (GISPEM, facturación, operaciones, gestión de personal, etc.) y qué patrón de integración usan (¿el sistema upstream dicta el contrato? ¿hay una capa anticorrupción?). Es el mapa de arquitectura de alto nivel más relevante para decisiones de integración y desacoplamiento.

## Contexto de Uso
- Diseño de una nueva integración entre dos sistemas APB: ¿qué patrón usar?
- Revisión de arquitectura de un sistema legado para planificar su modernización.
- Incorporación de un nuevo desarrollador: entender el "mapa" de los dominios APB.
- Planificación de una migración: ¿qué sistemas dependen del que se va a migrar?
- Decisión de compra: ¿un nuevo sistema SaaS encaja como Open Host Service o necesitamos ACL?

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `operation` | Enum | `generar-mapa` / `analizar-integracion` / `recomendar-patron` | ✅ |
| `systems` | Lista | Lista de sistemas a incluir en el mapa (nombre + descripción breve) | ✅ |
| `known_integrations` | Lista | Integraciones conocidas entre los sistemas: qué datos fluyen de A a B | ❌ |
| `focus_system` | Texto | Sistema de foco para `analizar-integracion` (qué relaciones tiene este sistema) | Condicional |

## Patrones de Integración DDD — Referencia APB

| Patrón | Abreviatura | Descripción | Cuándo usarlo en APB |
|---|---|---|---|
| **Shared Kernel** | SK | Dos equipos comparten un modelo común. Cambios coordinados. | Módulos del mismo sistema con equipos distintos |
| **Customer-Supplier** | C/S | El upstream (supplier) expone una API que el downstream (customer) consume. El downstream puede pedir cambios. | APB controla ambos sistemas |
| **Conformist** | CF | El downstream acepta el modelo del upstream sin posibilidad de cambio. | Sistemas externos de terceros donde APB es consumidor |
| **Anticorruption Layer** | ACL | El downstream traduce el modelo del upstream a su propio modelo. | Integración con SAP, sistemas legados, APIs de terceros |
| **Open Host Service** | OHS | El upstream expone un protocolo bien definido (REST API, eventos) para múltiples consumidores. | APIs REST de APB consumidas por múltiples sistemas |
| **Published Language** | PL | El OHS usa un lenguaje compartido (OpenAPI, eventos estandarizados). Siempre acompaña a OHS. | APIs APB documentadas en OpenAPI |
| **Separate Ways** | SW | Los equipos/sistemas no se integran; cada uno hace su propio camino. | Sistemas sin dependencia real entre sí |
| **Big Ball of Mud** | BBM | Sin límites claros, todo acoplado. Hay que sacar el código del BBM. | A evitar — documentar para planificar salida |

## Dominios APB (referencia)

```
Dominio: Operaciones Portuarias
  Bounded Contexts:
    - Escalas Marítimas (GISPEM) → Core Domain
    - Asignación de Atraques → Core Domain
    - Control de Acceso Portuario → Supporting Domain

Dominio: Finanzas y Facturación
  Bounded Contexts:
    - Tasas Portuarias y Liquidación → Core Domain
    - Gestión de Cuentas Corrientes → Supporting Domain
    - SAP Financiero (externo) → Generic/External

Dominio: Administración y RRHH
  Bounded Contexts:
    - Gestión de Personal → Generic Domain
    - Microsoft 365 / Entra ID (externo) → External

Dominio: Plataforma TI
  Bounded Contexts:
    - APB AI Framework → Supporting Domain
    - Infraestructura Azure → Generic Domain
```

## Flujo de Trabajo

### Operación: generar-mapa

1. Listar los Bounded Contexts de los sistemas indicados.
2. Identificar las integraciones entre ellos (quién es upstream, quién es downstream).
3. Asignar el patrón de integración más adecuado a cada relación.
4. Detectar ACLs que deberían existir pero no están implementadas (riesgo de corrupción del modelo).
5. Generar el diagrama textual del Context Map.

### Operación: analizar-integracion

Para una integración concreta entre dos sistemas:
1. ¿Quién tiene la propiedad del concepto compartido (ej. "escala marítima")?
2. ¿El upstream puede cambiar su API sin consultar al downstream? → Customer-Supplier o Conformist.
3. ¿El modelo del upstream es tan diferente al del downstream que traducir es necesario? → ACL.
4. ¿El upstream quiere exponer a múltiples consumidores? → OHS + PL.

### Operación: recomendar-patron

Dado un escenario, recomienda el patrón de integración con justificación y trade-offs.

## Salida Esperada

```markdown
# Mapa de Contextos APB — [Alcance] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-arch-context-mapping-v1.0) — validar con los equipos propietarios de cada contexto.

## Bounded Contexts Identificados
| Context | Tipo (Core/Supporting/Generic) | Equipo propietario | Sistema |
|---|---|---|---|

## Relaciones entre Contextos
| Upstream | Downstream | Patrón | Notas |
|---|---|---|---|
| Escalas (GISPEM) | Tasas y Liquidación | Customer-Supplier (OHS+PL) | GISPEM expone REST API documentada en OpenAPI |
| SAP APB | Gestión Personal | Conformist + ACL | APB adapta el modelo SAP al dominio HR interno |

## Riesgos Arquitectónicos Detectados
| Riesgo | Descripción | Recomendación |
|---|---|---|

## Diagrama (texto)
[Diagrama ASCII o descripción estructurada del mapa]
```

## Criterios de Calidad
- [ ] Cada Bounded Context tiene un equipo o propietario identificado.
- [ ] Las ACLs están documentadas cuando el upstream es un sistema legado o externo.
- [ ] Los patrones de integración están justificados, no solo listados.
- [ ] Los riesgos de acoplamiento excesivo están identificados.

## Dependencias
- `apb-arch-c4-model-v1.0` — el C4 nivel 1 es complementario al Context Map
- `apb-arch-api-lifecycle-v1.0` — las APIs OHS+PL requieren gestión del ciclo de vida

## Ejemplo de Uso

```
Genera el mapa de contextos para los sistemas de operaciones portuarias de APB.
Sistemas: GISPEM (escalas marítimas), Sistema de Tasas, Sistema de Atraques, SAP.
GISPEM publica eventos cuando se cierra una escala. El Sistema de Tasas los consume.
SAP es el upstream para datos maestros de clientes.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `operation` | Pregunta: "¿Qué necesitas: generar un mapa de contextos completo, analizar una integración concreta o recibir una recomendación de patrón?" | Sí |
| `systems` | Pregunta: "¿Qué sistemas quieres incluir en el análisis?" | Sí |
| `known_integrations` | Genera mapa con los sistemas pero sin relaciones; indica que deben completarse las integraciones conocidas | No |
| `focus_system` | Solo requerido para `analizar-integracion` — pregunta si falta en ese caso | Condicional |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-arch-context-mapping-v1.0) — validar con los equipos propietarios de cada contexto.

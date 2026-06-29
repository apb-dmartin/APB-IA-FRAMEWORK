---
id: "apb-arch-c4-model-v1.0"
name: "Diagramas de Arquitectura C4 Model"
description: "Genera diagramas de arquitectura siguiendo el modelo C4 (Context, Container, Component, Code) para sistemas APB en formato Structurizr DSL o PlantUML. Cubre los niveles 1 (contexto del sistema), 2 (contenedores) y 3 (componentes), adaptados al stack y convenciones APB."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Diagramas de Arquitectura C4 Model

## Propósito
Documentar la arquitectura de sistemas APB de forma estandarizada usando el modelo C4 de Simon Brown. Los diagramas C4 son jerárquicos y comprensibles para audiencias técnicas y no técnicas: desde el contexto de negocio (nivel 1) hasta los componentes internos (nivel 3). Generados en Structurizr DSL (formato textual, versionable en Git) o PlantUML como alternativa.

## Contexto de Uso
- Documentación de un nuevo sistema antes o durante el desarrollo.
- Actualización de diagramas existentes tras cambios arquitectónicos significativos.
- Onboarding de desarrolladores: entender la arquitectura del sistema en minutos.
- Revisiones de arquitectura con el Comité de Arquitectura APB.
- Comunicación con dirección o stakeholders de negocio (nivel 1 — System Context).

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `system_name` | Texto | Nombre del sistema a documentar | ✅ |
| `system_description` | Texto | Qué hace el sistema, sus usuarios y su rol en APB | ✅ |
| `c4_level` | Enum | `1-context` / `2-container` / `3-component` / `all` | ✅ |
| `tech_stack` | Lista | Stack tecnológico: lenguajes, frameworks, bases de datos, servicios Azure | ✅ |
| `integrations` | Lista | Sistemas externos e internos con los que se integra | ❌ |
| `output_format` | Enum | `structurizr` / `plantuml` / `markdown-text` | ❌ |

## Niveles C4 y qué generamos en cada uno

### Nivel 1 — System Context (para todos: técnicos y no técnicos)
Muestra el sistema como una caja negra, sus usuarios y los sistemas externos con los que interactúa.
Responde a: "¿Qué hace el sistema y con quién interactúa?"

### Nivel 2 — Container (para arquitectos y tech leads)
Muestra los contenedores del sistema: aplicaciones, APIs, bases de datos, servicios de mensajería.
Responde a: "¿Qué partes desplegables tiene el sistema y cómo se comunican?"

### Nivel 3 — Component (para desarrolladores)
Muestra los componentes principales dentro de un contenedor (módulos, clases de alto nivel).
Responde a: "¿Cómo está organizado el código dentro de la API/servicio?"

## Flujo de Trabajo

### Generación en Structurizr DSL

```
# ⚠️ Generado por APB AI Framework (apb-arch-c4-model-v1.0) — revisar con Arquitectura APB.

workspace "{system_name} — APB" {

  model {
    # === PERSONAS ===
    operadorPortuario = person "Operador Portuario" "Gestiona escalas y operaciones en el puerto."
    adminAPB = person "Administrador APB" "Administra el sistema y la configuración."

    # === SISTEMAS EXTERNOS ===
    sistemaFiscal = softwareSystem "Sistema de Facturación APB" "Genera liquidaciones de tasas." "External"
    sap = softwareSystem "SAP APB" "ERP corporativo." "External"

    # === SISTEMA PRINCIPAL ===
    gispem = softwareSystem "{system_name}" "{system_description}" {
      # Nivel 2: Contenedores
      webApp = container "Portal Web" "DevExtreme/TypeScript" "web"
      api = container "API REST" ".NET 8 / C#" "api"
      db = container "Base de Datos" "Azure SQL" "database"
      serviceBus = container "Mensajería" "Azure Service Bus" "queue"
      
      # Relaciones entre contenedores
      webApp -> api "HTTPS/REST"
      api -> db "Entity Framework Core"
      api -> serviceBus "Publicar eventos de escala"
    }

    # === RELACIONES ===
    operadorPortuario -> webApp "Gestiona escalas"
    api -> sistemaFiscal "Envía cierre de escala"
    api -> sap "Sincroniza proveedores"
  }

  views {
    systemContext gispem "Context" {
      include *
      autoLayout
    }
    container gispem "Containers" {
      include *
      autoLayout
    }
    theme default
  }
}
```

### PlantUML — Nivel 1 (alternativa)

```plantuml
@startuml Context_{system_name}
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml
' ⚠️ Generado por APB AI Framework (apb-arch-c4-model-v1.0)

LAYOUT_WITH_LEGEND()

Person(operador, "Operador Portuario", "Gestiona escalas")
System(gispem, "{system_name}", "{system_description}")
System_Ext(facturacion, "Facturación APB", "Genera liquidaciones")

Rel(operador, gispem, "Usa", "HTTPS")
Rel(gispem, facturacion, "Envía cierre de escala", "HTTPS/REST")

@enduml
```

## Convenciones de Colores APB en C4

| Tipo | Color | Descripción |
|---|---|---|
| Sistema principal | Azul corporativo APB | El sistema que se documenta |
| Sistema externo APB | Gris | Otros sistemas de APB |
| Sistema externo (terceros) | Gris oscuro | Sistemas externos fuera del control de APB |
| Persona | Amarillo | Usuarios humanos del sistema |
| Base de datos | Cilindro | Storage: SQL, Cosmos, PostgreSQL |

## Criterios de Calidad
- [ ] El diagrama de nivel 1 es comprensible para alguien no técnico de negocio.
- [ ] El diagrama de nivel 2 muestra todos los contenedores desplegables por separado.
- [ ] Las etiquetas de las relaciones incluyen el protocolo/tecnología de comunicación.
- [ ] El diagrama está en formato textual (Structurizr DSL o PlantUML) — versionable en Git.
- [ ] El stack tecnológico de cada contenedor está indicado.

## Dependencias
- `apb-doc-onboarding-v1.0` — los diagramas C4 son parte del onboarding
- `apb-arch-context-mapping-v1.0` — el mapa de contextos DDD complementa el nivel 1 de C4

## Ejemplo de Uso

```
Genera los diagramas C4 nivel 1 y 2 para el sistema GISPEM.
GISPEM gestiona las escalas marítimas del Puerto de Barcelona.
Stack: .NET 8 API, DevExtreme portal, Azure SQL, Azure Service Bus.
Integra con: sistema de facturación APB, SAP, y API externa AIS maritime data.
Formato: Structurizr DSL.
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `system_name` | Pregunta: "¿Cuál es el nombre del sistema a documentar?" | Sí |
| `system_description` | Pregunta: "Describe qué hace el sistema, para quién y su rol en APB" | Sí |
| `c4_level` | Pregunta: "¿Qué nivel C4 necesitas: contexto (1), contenedores (2), componentes (3), o todos?" | Sí |
| `tech_stack` | Pregunta: "¿Qué tecnologías usa el sistema?" | Sí |
| `integrations` | Genera diagrama con los sistemas mencionados en la descripción; indica que pueden faltar integraciones | No |
| `output_format` | Usa Structurizr DSL por defecto (formato preferido APB) | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Archivos Structurizr DSL / PlantUML** — comentario en cabecera:
  ```
  # ⚠️ Generado por APB AI Framework (apb-arch-c4-model-v1.0) — revisar con Arquitectura APB.
  ```

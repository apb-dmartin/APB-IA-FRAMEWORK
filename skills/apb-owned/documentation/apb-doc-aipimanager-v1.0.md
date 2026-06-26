---
id: "apb-doc-aipimanager-v1.0"
name: "Documentación Tagg para AipiManager"
description: "Generar documentación estructurada en formato Tagg (Text-based Architecture and Governance Guide) para el sistema AipiManager de APB. Incluye metadatos de componentes, dependencias, interfaces y decisiones de gobierno en formato parseable."
version: "1.0.0"
status: "draft"
owner: "Gobierno TI APB <arquitectura@portdebarcelona.cat>"
domain: "documentation"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Documentación Tagg para AipiManager

## Propósito
Generar documentación estructurada en formato Tagg (Text-based Architecture and Governance Guide) para el sistema AipiManager de APB. Incluye metadatos de componentes, dependencias, interfaces y decisiones de gobierno en formato parseable.

## Contexto de Uso
- Onboarding de sistemas en AipiManager para gobierno de arquitectura.
- Actualización de documentación Tagg tras cambios en componentes.
- Generación de vistas de arquitectura para stakeholders de negocio.
- Integración con catálogo de componentes y gobierno.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `system_name` | Texto | Nombre del sistema a documentar | ✅ |
| `components` | Lista | Lista de componentes con tipo, tecnología y responsabilidad | ✅ |
| `interfaces` | Lista | Interfaces entre componentes (APIs, eventos, bases de datos) | ✅ |
| `governance_metadata` | JSON | Metadatos de gobierno: owner, criticidad, compliance | ❌ |
| `decisions` | Lista | Decisiones de arquitectura relevantes (ADRs) | ❌ |

## Flujo de Trabajo (Pasos)
1. **Análisis de componentes**: Catalogar cada componente con atributos Tagg obligatorios.
2. **Mapeo de interfaces**: Documentar flujos de datos y dependencias entre componentes.
3. **Asignación de metadatos de gobierno**: Owner, equipo, criticidad, ciclo de vida, compliance.
4. **Vinculación de decisiones**: Asociar ADRs y decisiones de arquitectura a componentes.
5. **Generación de documento Tagg**: Estructurar en formato Tagg parseable.
6. **Validación de esquema**: Verificar que el documento cumple el esquema Tagg de AipiManager.
7. **Registro de evidencia**: Metadatos para gobierno.

## Salida Esperada
### Estructura del Documento Tagg
```tagg
@system [Nombre Sistema]
  @version [X.Y.Z]
  @owner [Equipo]
  @status [active/deprecated/planned]
  @compliance [ENS-Media, OWASP-L2]

  @component [Nombre Componente]
    @type [microservice/frontend/database/integration]
    @technology [.NET-8/Angular/PostgreSQL]
    @owner [Equipo/Responsable]
    @criticality [high/medium/low]
    @adr [ADR-NNNN]

  @interface [Nombre Interfaz]
    @from [Componente Origen]
    @to [Componente Destino]
    @protocol [HTTPS/AMQP/HTTPS+JSON]
    @contract [OpenAPI/AsyncAPI/Schema]
    @frequency [real-time/batch/event-driven]

  @decision [ADR-NNNN]
    @title [Título]
    @status [accepted]
    @impact [Componentes afectados]
```

## Criterios de Calidad
- [ ] Todos los componentes tienen tipo, tecnología y owner documentados.
- [ ] Todas las interfaces tienen protocolo, contrato y frecuencia definidos.
- [ ] El documento es válido según el esquema Tagg de AipiManager.
- [ ] Trazabilidad entre componentes, interfaces y decisiones de arquitectura.
- [ ] El documento es parseable por herramientas de AipiManager sin errores.

## Stack y Tecnologías
- Formato: Tagg (custom APB)
- Validación: Parser Tagg de AipiManager
- Metadatos: YAML/JSON para metadatos de gobierno

## Dependencias
- `apb-doc-adr-v1.0` — para ADRs a vincular
- `apb-gov-catalog-v1.0` — para registro en catálogo
- `apb-gov-evidence-v1.0` — para evidencia documental

## Ejemplo de Uso
**Prompt de invocación:**
```
Genera documentación Tagg para el sistema de gestión de expedientes:
- Componentes: API Gateway (Azure Front Door), Expedientes Service (.NET 8), Documentos Service (.NET 8), Notificaciones Service (.NET 8), BD Expedientes (Azure SQL), BD Documentos (Azure Blob Storage)
- Interfaces: Front Door → Expedientes Service (HTTPS+JSON), Expedientes Service → BD (TDS), Expedientes Service → Notificaciones Service (Service Bus)
- ADRs: ADR-0012 (uso de Service Bus), ADR-0015 (sharding de BD)
```

## Notas y Advertencias
- **Nivel 1**: El agente genera documentación Tagg; no modifica AipiManager directamente.
- **Revisión humana obligatoria** antes de importar a AipiManager.
- El formato Tagg puede evolucionar; el agente usa la versión vigente del esquema.
- El agente no tiene acceso a AipiManager; la importación es manual o vía pipeline.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **YAML/spec generado** - primera linea: `# [IA-GEN] Generado por APB AI Framework (apb-doc-aipimanager-v1.0) - pendiente revision humana`
- **Campo OpenAPI si aplica**: `info.x-ai-generated: true` + `info.x-ai-skill: "apb-doc-aipimanager-v1.0"`
- **Commit** - prefijo `[ai-gen]` + `Co-Authored-By: APB AI Framework <framework@portdebarcelona.cat>`

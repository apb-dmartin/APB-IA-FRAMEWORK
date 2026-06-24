---
id: "apb-disc-spec-gen-v1.0"
name: "Generación de Especificaciones"
description: "Generar documentos de especificación técnica completos y estructurados a partir de requisitos enriquecidos, decisiones arquitectónicas y estándares corporativos. Sirve como contrato entre negocio y desarrollo."
version: "1.0.0"
status: "draft"
owner: "Análisis Funcional <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Generación de Especificaciones

---

## 🎯 Propósito

Generar documentos de especificación técnica completos y estructurados a partir de requisitos enriquecidos, decisiones arquitectónicas y estándares corporativos. Sirve como contrato entre negocio y desarrollo.

---

## ⚡ Trigger

Cuando los requisitos están enriquecidos y se necesita un documento de especificación formal para inicio de desarrollo, o cuando se actualiza una especificación existente.

---

## 📥 Input

- Requisitos funcionales enriquecidos
- Requisitos no funcionales
- Decisiones arquitectónicas (ADRs)
- Contratos API/eventos preliminares
- Estándares de especificación APB
- Mockups o prototipos de UI

---

## 📤 Output

- Documento de especificación técnica (system-spec.md)
- Diagramas de secuencia para flujos principales
- Modelo de datos
- Definición de interfaces (APIs, eventos, ficheros)
- Criterios de aceptación consolidados
- Matriz de trazabilidad completa

---

## 🔄 Proceso

1. **Estructura del documento**: Seguir plantilla estándar APB (introducción, alcance, requisitos, arquitectura, datos, interfaces, criterios de aceptación, anexos).
2. **Requisitos funcionales**: Organizar por épica/feature. Incluir descripción, criterios de aceptación, reglas de negocio.
3. **Requisitos no funcionales**: Rendimiento, seguridad, disponibilidad, escalabilidad, usabilidad.
4. **Arquitectura**: Referenciar ADRs, diagramas C4, decisiones técnicas.
5. **Modelo de datos**: Diagrama ER, diccionario de datos, migraciones necesarias.
6. **Interfaces**: APIs REST (referencia a OpenAPI), eventos (referencia a CloudEvents), ficheros.
7. **Flujos de negocio**: Diagramas de secuencia para casos principales.
8. **Criterios de aceptación**: Consolidados y verificables.
9. **Anexos**: Glosario, referencias, historial de cambios.
10. **Revisión**: Validar con stakeholders técnicos y de negocio.

---

## 📋 Reglas y Constraints

- El documento debe ser auto-contenido; un desarrollador nuevo debe poder entender el sistema leyéndolo.
- Usar lenguaje claro; evitar jerga innecesaria. Definir términos en glosario.
- Toda decisión arquitectónica debe referenciar su ADR.
- Las interfaces deben ser lo suficientemente detalladas para que un desarrollador pueda implementarlas.
- Incluir diagramas; un diagrama vale más que 1000 palabras.
- Versionar el documento; mantener historial de cambios.
- No incluir información sensible (contraseñas, IPs internas) en el documento.
- El documento es un contrato; cualquier cambio requiere revisión y aprobación.

---

## 🛠 Stack Tecnológico Relevante

- Markdown (formato estándar)
- Mermaid (diagramas)
- OpenAPI (referencia APIs)
- CloudEvents (referencia eventos)
- Plantilla system-spec.md APB
- Git (versionado)

---

## 💡 Ejemplos de Uso

**Ejemplo — Especificación de sistema de reservas:**
> Secciones: 1.Introducción, 2.Alcance, 3.Requisitos (15 RF, 8 RNF), 4.Arquitectura (referencia ADR-003), 5.Datos (12 entidades), 6.Interfaces (3 APIs, 5 eventos), 7.Criterios de aceptación (25 CA), 8.Anexos.
> Diagramas: C4 Container, 4 diagramas de secuencia, ER diagram.
> Tamaño: ~80 páginas en renderizado.

---

## 🔗 Dependencias

- `apb-disc-enrich-req-v1.0`
- `apb-arch-design-v1.0`
- `apb-arch-api-contract-v1.0`
- `apb-doc-adr-v1.0`

---

## 📝 Notas

- La especificación es un documento vivo; se actualiza durante el desarrollo.
- Para proyectos ágiles, mantener especificación 'just enough' sin caer en documentación excesiva.
- Considerar generación automática de partes de la spec desde código (OpenAPI, ADRs).

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

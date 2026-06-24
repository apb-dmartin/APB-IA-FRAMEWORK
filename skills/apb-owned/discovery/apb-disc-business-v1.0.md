---
id: "apb-disc-business-v1.0"
name: "Business Discovery"
description: "Descubrir y documentar procesos de negocio, necesidades de stakeholders, objetivos estratégicos y restricciones organizativas que fundamentarán el desarrollo o modernización de sistemas."
version: "1.0.0"
status: "draft"
owner: "Análisis Funcional <arquitectura@portdebarcelona.cat>"
domain: "discovery"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Business Discovery

---

## 🎯 Propósito

Descubrir y documentar procesos de negocio, necesidades de stakeholders, objetivos estratégicos y restricciones organizativas que fundamentarán el desarrollo o modernización de sistemas.

---

## ⚡ Trigger

Al inicio de un nuevo proyecto, al definir el alcance de una nueva funcionalidad significativa, o cuando surge una necesidad de negocio no atendida por sistemas actuales.

---

## 📥 Input

- Solicitud de negocio (iniciativa, problema, oportunidad)
- Stakeholders identificados
- Documentación de procesos actuales
- Métricas de negocio actuales
- Restricciones organizativas (presupuesto, tiempo, regulación)

---

## 📤 Output

- Documento de alcance de negocio
- Mapa de stakeholders y sus intereses
- Procesos de negocio actuales (AS-IS) y objetivo (TO-BE)
- Lista de necesidades priorizadas
- Identificación de riesgos de negocio
- Propuesta de valor y KPIs esperados

---

## 🔄 Proceso

1. **Identificación de stakeholders**: Mapear actores, roles, influencia e intereses.
2. **Entrevistas y workshops**: Recopilar información mediante técnicas estructuradas (entrevistas, focus groups, surveys).
3. **Análisis de procesos AS-IS**: Documentar flujos actuales, pain points, ineficiencias.
4. **Identificación de necesidades**: Traducir problemas en necesidades expresadas como 'Necesito [capacidad] para [objetivo]'.
5. **Definición de TO-BE**: Diseñar procesos objetivo con mejoras.
6. **Análisis de gap**: Diferencias entre AS-IS y TO-BE. Esfuerzo estimado.
7. **Priorización**: MoSCoW o similar para clasificar necesidades.
8. **Definición de valor**: KPIs de negocio que medirán éxito.
9. **Validación**: Revisar con stakeholders clave.

---

## 📋 Reglas y Constraints

- Separar necesidades de soluciones; no dejar que stakeholders prescriban tecnología.
- Documentar fuente de cada necesidad para trazabilidad.
- Validar con al menos 2 fuentes independientes antes de considerar una necesidad confirmada.
- Identificar necesidades implícitas (no dichas pero asumidas).
- No prometer funcionalidad sin validar viabilidad técnica.
- Registrar supuestos explícitamente.
- Priorizar por valor de negocio, no por facilidad técnica.

---

## 🛠 Stack Tecnológico Relevante

- BPMN (modelado de procesos)
- Miro / Mural (workshops)
- Jira / Azure DevOps (gestión)
- Excel (análisis y priorización)
- Entrevistas / encuestas

---

## 💡 Ejemplos de Uso

**Ejemplo — Digitalización de proceso de alta de proveedores:**
> AS-IS: 15 pasos manuales, 3 departamentos, tiempo medio 12 días, 30% errores de datos.
> Pain points: Duplicidad de entrada de datos, falta de visibilidad, aprobaciones por email.
> TO-BE: Portal self-service, workflow automático, integración con ERP, tiempo objetivo 2 días.
> Necesidades: 12 identificadas, 5 Must-have, 4 Should-have, 3 Could-have.
> KPIs: Tiempo de ciclo, tasa de error, satisfacción de proveedor.

---

## 🔗 Dependencias

- `apb-disc-enrich-req-v1.0`
- `apb-disc-spec-gen-v1.0`
- `apb-disc-backlog-v1.0`

---

## 📝 Notas

- El Business Discovery es iterativo; no esperar tener toda la información en una sesión.
- Para proyectos grandes, considerar discovery por fases o por dominio.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

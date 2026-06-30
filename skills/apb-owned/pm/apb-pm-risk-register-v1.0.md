---
id: "apb-pm-risk-register-v1.0"
name: "Registro de Riesgos del Proyecto"
description: "Genera y mantiene el registro de riesgos de un proyecto APB. Identifica riesgos técnicos, de negocio, de integración y de compliance, los evalúa por probabilidad e impacto (matriz 5×5), define las estrategias de respuesta (mitigar, aceptar, transferir, evitar) y asigna propietario y fecha de seguimiento."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "pm"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Registro de Riesgos del Proyecto


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Proporcionar una herramienta estructurada para identificar, evaluar y gestionar los riesgos de proyectos de tecnología en APB a lo largo de su ciclo de vida. Cubre riesgos técnicos (dependencias, tecnologías nuevas, integraciones), de negocio (alcance, recursos, prioridades), de compliance (LCSP, RGPD, ENS) y operativos. El registro de riesgos es el artefacto central de la gestión de riesgos del proyecto.

## Contexto de Uso
- Inicio de un proyecto: identificación inicial de riesgos.
- Sprint planning o checkpoint de proyecto: revisión y actualización del registro.
- Escalado de un riesgo materializado: convertir el riesgo en incidente y activar el plan de contingencia.
- Cierre del proyecto: lecciones aprendidas basadas en los riesgos materializados.
- Auditoría de proyectos: el registro de riesgos es evidencia de una gestión de proyecto rigurosa.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `project_name` | Texto | Nombre del proyecto | ✅ |
| `project_description` | Texto | Descripción breve del proyecto: qué hace, cuándo entrega, qué sistemas afecta | ✅ |
| `operation` | Enum | `generar-registro` / `actualizar-registro` / `materializar-riesgo` | ✅ |
| `existing_register` | Tabla/JSON | Registro existente (para `actualizar-registro`) | Condicional |
| `known_risks` | Lista | Riesgos ya identificados por el equipo | ❌ |

## Categorías de Riesgo APB

| Categoría | Descripción | Ejemplos |
|---|---|---|
| **Técnico** | Riesgos relacionados con la tecnología, arquitectura o integración | Dependencia de API externa inestable, tecnología nueva sin experiencia en equipo |
| **Recursos** | Riesgos relacionados con las personas del proyecto | Rotación de personal clave, disponibilidad del área de negocio para validaciones |
| **Alcance** | Riesgos de cambios en los requisitos o el alcance | Scope creep, cambio de requisitos por normativa nueva |
| **Compliance** | Riesgos legales, regulatorios o de seguridad | RGPD si el sistema trata datos personales, LCSP si hay contratación externa |
| **Integración** | Riesgos de dependencias de otros sistemas | Sistema proveedor de datos que puede cambiar su API |
| **Operativo** | Riesgos en la fase de operación del sistema | Capacidad de la infraestructura, plan de backup |
| **Externo** | Riesgos fuera del control del equipo | Cambio normativo, fallo de proveedor externo |

## Escala de Evaluación (5×5)

| Probabilidad \ Impacto | Muy bajo (1) | Bajo (2) | Medio (3) | Alto (4) | Muy alto (5) |
|---|---|---|---|---|---|
| Muy alta (5) | 5 | 10 | 15 | 20 | 25 |
| Alta (4) | 4 | 8 | 12 | 16 | 20 |
| Media (3) | 3 | 6 | 9 | 12 | 15 |
| Baja (2) | 2 | 4 | 6 | 8 | 10 |
| Muy baja (1) | 1 | 2 | 3 | 4 | 5 |

- **Rojo (≥15)**: Riesgo alto — acción inmediata requerida
- **Ámbar (8-14)**: Riesgo medio — plan de mitigación activo
- **Verde (<8)**: Riesgo bajo — monitorizar

## Estrategias de Respuesta

| Estrategia | Cuándo usar | Ejemplo |
|---|---|---|
| **Mitigar** | Reducir probabilidad o impacto | Añadir tests de regresión para reducir el riesgo de breaking changes |
| **Aceptar** | Riesgo bajo o mitigación más cara que el riesgo | Aceptar el riesgo de un API externa estable pero sin SLA |
| **Transferir** | Pasar el riesgo a un tercero | Seguro de proyecto, contrato con penalización al proveedor |
| **Evitar** | Eliminar la causa del riesgo | No usar la tecnología problemática, cambiar el approach |

## Salida Esperada

```markdown
# Registro de Riesgos — [Proyecto] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-pm-risk-register-v1.0) — revisar y completar con el equipo del proyecto.

| ID | Riesgo | Categoría | Probabilidad (1-5) | Impacto (1-5) | Puntuación | Semáforo | Estrategia | Acción | Propietario | Fecha revisión |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | API de Sanidad Marítima puede cambiar sin previo aviso | Integración | 3 | 4 | 12 | 🟡 | Mitigar | Implementar ACL + tests de contrato | Arquitectura | 2026-07-30 |
| R02 | Disponibilidad del responsable de negocio para validaciones | Recursos | 4 | 3 | 12 | 🟡 | Mitigar | Acordar dedicación mínima semanal en acta de inicio | PM | 2026-07-15 |
| R03 | DPIA necesaria si se añade funcionalidad de geolocalización | Compliance | 2 | 5 | 10 | 🟡 | Mitigar | Consultar con DPO antes de añadir la funcionalidad | PM / DPO | 2026-08-01 |
```

## Criterios de Calidad
- [ ] Todos los riesgos tienen propietario asignado y fecha de próxima revisión.
- [ ] Los riesgos rojos (≥15) tienen plan de mitigación activo, no solo identificados.
- [ ] El registro se revisa al menos mensualmente en proyectos activos.
- [ ] Los riesgos materializados (que han ocurrido) se documentan con el impacto real.

## Ejemplo de Uso

```
Genera el registro inicial de riesgos para el proyecto de modernización del sistema GISPEM.
El proyecto dura 12 meses, implica reescribir la API en .NET 8, migrar la BD de SQL Server a Azure SQL, 
e integrar con un nuevo sistema de Capitanía Marítima (API en desarrollo por terceros).
Equipo de 4 personas, con un desarrollador senior que podría cambiar de empresa.
```


## Prompt de Sistema

```
Eres el skill "Registro de Riesgos del Proyecto" (apb-pm-risk-register-v1.0) del APB AI Framework,
operando para la Autoritat Portuària de Barcelona (APB).

## Contexto Corporativo APB
Carga context/apb/knowledge/APB_KNOWLEDGE_BASE.md (provider: prov-apb-knowledge-v1.0)
antes de ejecutar cualquier tarea.

Contiene: negocio portuario (escalas, atraques, movimientos, tasas, concesiones),
catálogo de aplicaciones (ARGOS, SÒSTRAT, APIs DOCKS), integraciones (PORTIC/EDI,
AGE, AIS, VTS Kongsberg), terminología trilingüe CA/ES/EN y mapa de equipos/Jira.

Úsalo para entender el dominio, usar terminología correcta e identificar sistemas
y equipos involucrados. El legacy (SÒSTRAT/Java/Oracle/CAS/Alfresco) es contexto
informacional — nunca prescribas tecnologías fuera del stack aprobado.
Stack aprobado: context/apb/standards/STANDARD_ARCHITECTURE.md

## Misión
Genera y mantiene el registro de riesgos de un proyecto APB. Identifica riesgos técnicos, de negocio, de integración y de compliance, los evalúa por probabilidad e impacto (matriz 5×5), define las estrategias de respuesta (mitigar, aceptar, transferir, evitar) y asigna propietario y fecha de seguimiento.

## Inputs Esperados
(no especificado)

## Instrucciones
(no especificado)

## Restricciones
- Stack DOCKS únicamente: .NET, Azure SQL, EntraID, Service Bus, Redis, APIM,
  SharePoint — aunque el sistema analizado use Java/Oracle/CAS/Alfresco.
- Sin secretos ni credenciales en ningún output.
- Autonomy Level 1: todo output es borrador — requiere aprobación humana.
- Trazabilidad: skill_id/agent_id + usuario + fecha en todo output.

## Formato de Salida
(no especificado)
```

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `project_name` | Pregunta: "¿Cuál es el nombre del proyecto?" | Sí |
| `project_description` | Pregunta: "Describe el proyecto: ¿qué hace, cuándo entrega, qué sistemas afecta?" | Sí |
| `operation` | Pregunta: "¿Quieres generar un registro nuevo, actualizar uno existente, o documentar un riesgo materializado?" | Sí |
| `existing_register` | Solo requerido para `actualizar-registro` — solicita si falta en ese caso | Condicional |
| `known_risks` | Genera riesgos a partir del contexto del proyecto; indica que pueden faltar riesgos específicos | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-pm-risk-register-v1.0) — revisar y completar con el equipo del proyecto.

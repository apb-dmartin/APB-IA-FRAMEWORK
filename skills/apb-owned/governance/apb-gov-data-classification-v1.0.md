---
id: "apb-gov-data-classification-v1.0"
name: "Clasificación de Activos de Datos"
description: "Clasifica activos de datos por categoría (personal/sensible/operativo/público) según RGPD y ENS Alto. Genera inventario de tratamientos art. 30, tabla de controles obligatorios por categoría y ficha de cada sistema con su nivel de sensibilidad."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "governance"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Clasificación de Activos de Datos

## Propósito
Proporcionar un marco sistemático para identificar, clasificar y controlar los activos de datos de APB conforme al RGPD y al ENS (Esquema Nacional de Seguridad) nivel Alto. Genera el inventario de tratamientos obligatorio (art. 30 RGPD), la tabla de controles técnicos y organizativos por categoría, y la ficha de sensibilidad de cada sistema de información.

## Contexto de Uso
- Alta de un nuevo sistema que procesa datos personales o sensibles.
- Auditoría periódica del inventario de tratamientos (art. 30 RGPD).
- Análisis previo a una DPIA/EIPD (`apb-gov-dpia-v1.0`).
- Preparación de evidencias para auditoría ENS o inspección AEPD.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `system_name` | Texto | Nombre del sistema o aplicación a clasificar | ✅ |
| `system_description` | Texto | Descripción funcional: qué hace, quién lo usa, qué datos maneja | ✅ |
| `data_subjects` | Lista | Tipos de interesados: ciudadanos, empleados, proveedores, menores... | ✅ |
| `ens_category` | Enum | Categoría ENS del sistema: `basic` / `medium` / `high` | ❌ |
| `existing_inventory` | JSON | Inventario art. 30 existente para verificar coherencia | ❌ |

## Flujo de Trabajo

1. **Identificación de activos de datos**:
   - Listar todos los tipos de datos procesados por el sistema.
   - Distinguir entre datos recogidos directamente y datos recibidos de otros sistemas.
   - Identificar datos derivados o inferidos (perfiles, logs de actividad).

2. **Clasificación por categoría**:
   - **Personal**: datos que identifican a una persona física (nombre, email, DNI, IP, matrícula).
   - **Sensible (especial categoría RGPD art. 9)**: salud, origen étnico, religión, ideología, datos biométricos, infracciones penales.
   - **Operativo**: datos de negocio sin carácter personal (tráfico portuario, cargas, escalas de buques).
   - **Público**: datos sin restricción de difusión (precios publicados, horarios, estadísticas).

3. **Controles obligatorios por categoría**:

   | Categoría | Cifrado en reposo | Cifrado en tránsito | Control de acceso | Logs de auditoría | Retención máxima |
   |---|---|---|---|---|---|
   | Personal | Recomendado | ✅ Obligatorio | RBAC mínimo | ✅ Obligatorio | Según finalidad |
   | Sensible | ✅ Obligatorio | ✅ Obligatorio | RBAC estricto + MFA | ✅ Obligatorio + alertas | Mínimo necesario |
   | Operativo | Recomendado | Recomendado | RBAC | Recomendado | Política interna APB |
   | Público | No requerido | Recomendado | Lectura pública | No requerido | Sin límite |

4. **Ficha de sistema** (por cada sistema analizado):
   - Finalidad del tratamiento y base jurídica (art. 6 RGPD o art. 9.2 para datos sensibles).
   - Categorías de interesados y número aproximado.
   - Transferencias internacionales (si aplica).
   - Responsable del tratamiento y encargados (proveedores con acceso a datos).
   - Plazos de conservación y criterios de eliminación.

5. **Inventario art. 30 RGPD**:
   - Actualizar o crear el registro de actividades de tratamiento.
   - Formato: tabla con los campos obligatorios del art. 30.

6. **⚠️ CHECKPOINT HUMANO**: El DPO (o rol equivalente en APB) debe validar la clasificación y el inventario antes de considerarlos definitivos.

## Salida Esperada

```markdown
# Clasificación de Datos — [Sistema] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-data-classification-v1.0) — pendiente validación humana. No distribuir sin revisión del DPO.

## Resumen de Clasificación
| Categoría | Tipos de datos | Nº estimado registros | Sistemas origen |
|---|---|---|---|

## Controles Obligatorios Aplicables
| Control | Categoría afectada | Estado | Responsable |
|---|---|---|---|

## Ficha de Tratamiento (art. 30 RGPD)
| Campo | Valor |
|---|---|
| Nombre del tratamiento | |
| Finalidad | |
| Base jurídica | |
| Categorías de interesados | |
| Categorías de datos | |
| Destinatarios | |
| Transferencias internacionales | |
| Plazo de supresión | |
| Descripción de medidas de seguridad | |

## Sistemas Proveedores/Destinatarios con Acceso
| Sistema/Proveedor | Tipo de acceso | Contrato DPA firmado |
|---|---|---|
```

## Criterios de Calidad
- [ ] Todos los tipos de datos están clasificados en una (y solo una) categoría.
- [ ] La base jurídica está identificada para cada tratamiento de datos personales.
- [ ] Los plazos de retención están definidos o referenciados a política APB.
- [ ] Los proveedores con acceso a datos personales tienen DPA (Data Processing Agreement) identificado.
- [ ] La clasificación es coherente con la categoría ENS del sistema declarada.

## Dependencias
- `apb-gov-dpia-v1.0` — si la clasificación revela datos de alto riesgo, se requiere DPIA
- `apb-sec-risk-analysis-v1.0` — la clasificación alimenta el análisis de riesgos de seguridad

## Ejemplo de Uso

```
Clasifica los datos del sistema GISPEM (Gestión Integrada de Sistemas Portuarios y Escalas Marítimas).
Procesa datos de buques, escalas, consignatarios y documentación aduanera.
Algunos registros incluyen datos de tripulantes (nombre, nacionalidad, datos de pasaporte).
Necesito la ficha de tratamiento y los controles aplicables.
```

## Notas y Advertencias
- Los datos de buques y escalas son operativos, pero los datos de tripulantes son personales — un mismo sistema puede tener múltiples categorías.
- El ENS nivel Alto exige cifrado en reposo para datos con categoría ENS Media o Alta — verificar con `ens_category`.
- La clasificación no sustituye a la DPIA cuando es obligatoria (art. 35 RGPD).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento B |

## ⚠️ Comportamiento ante inputs incompletos

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `system_name` | Pregunta: "¿Cuál es el nombre del sistema a clasificar?" | Sí |
| `system_description` | Pregunta: "Describe qué hace el sistema, quién lo usa y qué datos maneja" | Sí |
| `data_subjects` | Pregunta: "¿Qué tipos de personas tienen datos en este sistema? (ciudadanos, empleados, tripulantes...)" | Sí |
| `ens_category` | Asume `medium` e indica explícitamente la asunción | No |
| `existing_inventory` | Genera inventario desde cero sin comparación | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > ⚠️ Borrador generado por IA (APB AI Framework - apb-gov-data-classification-v1.0) — pendiente validación humana. No distribuir sin revisión del DPO.
- **Tickets Jira**: label `ia-generado` + footer en descripción del ticket.

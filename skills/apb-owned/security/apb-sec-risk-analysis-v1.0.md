---
id: "apb-sec-risk-analysis-v1.0"
name: "Análisis de Riesgos + Informe"
description: "Realizar análisis de riesgos de seguridad de la información siguiendo metodologías estandarizadas (ISO 27005, NIST SP 800-30, MAGERIT). Identificar activos, amenazas, vulnerabilidades, evaluar riesgos y proponer tratamientos. Genera un informe de riesgos con matriz de impacto, plan de tratamiento..."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Análisis de Riesgos + Informe

## Propósito
Realizar análisis de riesgos de seguridad de la información siguiendo metodologías estandarizadas (ISO 27005, NIST SP 800-30, MAGERIT). Identificar activos, amenazas, vulnerabilidades, evaluar riesgos y proponer tratamientos. Genera un informe de riesgos con matriz de impacto, plan de tratamiento y seguimiento.

## Contexto de Uso
- Evaluación de riesgos periódica o ante cambios significativos en sistemas o procesos.
- Apoyo en la toma de decisiones para aceptación, mitigación, transferencia o evitación de riesgos.
- Integración con workflows de excepciones de riesgo y gobierno corporativo.
- Preparación para auditorías de seguridad y cumplimiento normativo.

## Entradas Requeridas
| Entrada | Tipo | Descripción | Obligatorio |
|---------|------|-------------|-------------|
| `scope` | Texto | Alcance del análisis: sistemas, procesos, ubicaciones, stakeholders | ✅ |
| `asset_inventory` | Lista | Inventario de activos a evaluar (datos, sistemas, infraestructura, personal) | ✅ |
| `threat_catalog` | Lista | Catálogo de amenazas aplicable al contexto | ❌ (usa catálogo corporativo por defecto) |
| `vulnerability_assessment` | Texto | Resultados de evaluaciones de vulnerabilidad previas | ❌ |
| `existing_controls` | Lista | Controles de seguridad implementados | ❌ |
| `risk_matrix` | Texto | Matriz de riesgo corporativa (probabilidad × impacto) | ❌ (usa matriz estándar) |

## Flujo de Trabajo (Pasos)
1. **Contextualización**: Definir alcance, criterios de evaluación y partes interesadas.
2. **Identificación de activos**: Catalogar activos con su valor (confidencialidad, integridad, disponibilidad).
3. **Identificación de amenazas**: Mapear amenazas relevantes a cada activo desde el catálogo corporativo.
4. **Identificación de vulnerabilidades**: Asociar vulnerabilidades conocidas a activos y amenazas.
5. **Análisis de riesgos**: Evaluar probabilidad e impacto para cada escenario de riesgo (amenaza × vulnerabilidad × activo).
6. **Evaluación de riesgos**: Clasificar riesgos en la matriz corporativa y determinar nivel de riesgo (aceptable / no aceptable).
7. **Tratamiento de riesgos**: Proponer opciones de tratamiento:
   - **Mitigar** — Implementar controles adicionales.
   - **Transferir** — Seguros, outsourcing con contrato de responsabilidad.
   - **Aceptar** — Decisión informada con justificación documentada.
   - **Evitar** — Descontinuar actividad o sistema.
8. **Plan de tratamiento**: Documentar acciones, responsables, plazos y recursos.
9. **Generación de informe**: Documento estructurado con resumen ejecutivo, matriz de riesgos y plan de acción.
10. **Registro de evidencia**: Metadatos para gobierno y seguimiento.

## Salida Esperada
### Estructura del Informe
```markdown
# Informe de Análisis de Riesgos — [Alcance]
> Fecha: [YYYY-MM-DD] | Autor: Risk & Exception Agent | Metodología: ISO 27005

## 1. Alcance y Contexto
## 2. Criterios de Evaluación
## 3. Inventario de Activos
| ID | Activo | Tipo | Valor C | Valor I | Valor D | Valor Total |
## 4. Escenarios de Riesgo
| ID | Activo | Amenaza | Vulnerabilidad | Probabilidad | Impacto | Nivel de Riesgo | Tratamiento |
## 5. Matriz de Riesgos
## 6. Plan de Tratamiento
| ID Riesgo | Tratamiento | Acción | Responsable | Plazo | Recursos | Estado |
## 7. Riesgos Aceptados (con justificación)
## 8. Residual Risk Summary
## 9. Recomendaciones
## 10. Evidencia y Metadatos
```

## Criterios de Calidad
- [ ] Todos los activos del alcance están identificados y valorados.
- [ ] Cada escenario de riesgo tiene probabilidad, impacto y nivel de riesgo definidos.
- [ ] 100% de riesgos no aceptables tienen plan de tratamiento con responsable y plazo.
- [ ] Riesgos aceptados tienen justificación documentada y aprobación sugerida.
- [ ] Trazabilidad entre activos, amenazas, vulnerabilidades y controles.
- [ ] El informe es revisable por un auditor de riesgos sin intervención del agente.

## Stack y Tecnologías
- Metodologías: ISO 27005, NIST SP 800-30, MAGERIT
- Matriz de riesgo: corporativa APB (5×5 probabilidad × impacto)
- Formatos: Markdown, Excel para matriz detallada

## Dependencias
- `apb-sec-threat-model-v1.0` — para identificación de amenazas técnicas
- `apb-sec-ens-v1.0` — para requisitos de seguridad aplicables
- `apb-gov-evidence-v1.0` — para generación de evidencia
- `apb-gov-policy-check-v1.0` — para validación de políticas de riesgo

## Ejemplo de Uso
**Prompt de invocación:**
```
Realiza un análisis de riesgos para la migración de nuestro sistema legacy a Azure:
- Alcance: aplicación de gestión financiera, 150 usuarios, datos sensibles
- Activos: BD SQL Server (datos financieros), App Service (procesamiento), Service Bus (eventos)
- Controles existentes: cifrado en reposo, MFA para admin, backups diarios
- Amenazas conocidas: acceso no autorizado, ransomware, fallo de disponibilidad
```

## Notas y Advertencias
- **Nivel 1**: El agente realiza análisis basado en información proporcionada; no realiza escaneos de vulnerabilidades ni pruebas técnicas.
- **Revisión humana obligatoria** para riesgos clasificados como críticos y decisiones de aceptación de riesgo.
- La valoración de activos y la matriz de riesgo deben alinearse con los criterios corporativos aprobados.
- Los planes de tratamiento son propuestas; la asignación de recursos requiere validación de gestión.

## Historial de Cambios
| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-06-20 | Arquitectura APB | Creación inicial |

---
id: "apb-qa-post-migration-v1.0"
name: "Validación Post-Migración"
description: "Validar que una migración de datos, código o infraestructura se ha completado correctamente, garantizando integridad, consistencia y funcionalidad equivalente o mejorada."
version: "1.0.0"
status: "draft"
owner: "QA APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Validación Post-Migración

---

## 🎯 Propósito

Validar que una migración de datos, código o infraestructura se ha completado correctamente, garantizando integridad, consistencia y funcionalidad equivalente o mejorada.

---

## ⚡ Trigger

Tras completarse una fase de migración (datos, aplicación, infraestructura), antes de dar por finalizada la migración o activar el nuevo sistema.

---

## 📥 Input

- Plan de migración ejecutado
- Datos origen y destino
- Especificación de equivalencia funcional
- Métricas de rendimiento baseline
- Checklist de validación predefinida

---

## 📤 Output

- Informe de validación post-migración
- Comparativa de datos (origen vs destino)
- Resultados de tests funcionales y de regresión
- Métricas de rendimiento comparativas
- Lista de discrepancias y acciones correctivas
- Certificación de migración (aprobado/condicionado/rechazado)

---

## 🔄 Proceso

1. **Validación de datos**: Comparar volúmenes, checksums, muestras representativas.
2. **Validación de integridad referencial**: Verificar FKs, constraints, índices.
3. **Tests funcionales**: Ejecutar suite completa de tests en el entorno migrado.
4. **Tests de regresión**: Verificar que funcionalidad existente no se ha roto.
5. **Validación de rendimiento**: Comparar latencias, throughput vs baseline.
6. **Validación de seguridad**: Verificar permisos, roles, encriptación.
7. **Validación de operabilidad**: Logs, monitores, alertas funcionando.
8. **Documentación**: Informe con evidencias, discrepancias y plan de remediación.

---

## 📋 Reglas y Constraints

- No declarar migración exitosa sin validación de datos (mínimo 95% de registros verificados).
- Toda discrepancia debe ser clasificada: crítica (bloqueante), mayor (requiere fix), menor (aceptable).
- Mantener entorno origen operativo hasta validación completa y período de estabilidad (mínimo 48h).
- Tests de regresión deben pasar al 100% antes de certificar.
- Documentar rollback plan en caso de fallo post-migración.

---

## 🛠 Stack Tecnológico Relevante

- SQL / scripts de comparación
- xUnit / NUnit (tests automatizados)
- Azure DevOps (pipelines de validación)
- Azure Data Factory (comparación de datos)
- Application Insights (métricas de rendimiento)

---

## 💡 Ejemplos de Uso

**Ejemplo — Migración de BBDD:**
> Origen: SQL Server 2016 on-premise, 5M registros.
> Destino: Azure SQL Managed Instance.
> Validación: Count(*) coincide, 1000 muestras aleatorias verificadas, checksum MD5 por tabla.
> Tests: 500 tests automatizados, 100% pass.
> Rendimiento: P95 latencia reducido de 200ms a 80ms.
> Estado: Aprobado.

---

## 🔗 Dependencias

- `apb-plat-db-migration-v1.0`
- `apb-qa-test-plan-v1.0`

---

## 📝 Notas

- Considerar período de convivencia (parallel run) para migraciones críticas.
- Validar también procesos batch y reportes que dependen de los datos migrados.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-qa-post-migration-v1.0) - pendiente validacion humana. No distribuir sin revision.

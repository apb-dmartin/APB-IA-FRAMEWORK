---
id: "apb-ops-service-continuity-v1.0"
name: "Continuidad de Servicio (BCP/DRP)"
description: "Define la estrategia de continuidad de servicio y recuperación ante desastres para servicios APB: RTOs, RPOs, estrategia de backup, plan de recuperación y procedimientos de activación del DRP. Cubre servicios cloud (Azure) e infraestructura on-premises."
version: "1.0.0"
status: "draft"
owner: "SRE / Operaciones APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-27"
review_date: "2026-06-27"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Continuidad de Servicio (BCP/DRP)


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

## Propósito
Definir y documentar la estrategia de continuidad de negocio (BCP) y recuperación ante desastres (DRP) para servicios APB. Establece los RTOs y RPOs por servicio, la estrategia de backup, los procedimientos de activación del DRP y los runbooks de recuperación, alineados con los requerimientos de negocio y la normativa ENS.

## Contexto de Uso
- Diseño inicial de la estrategia de continuidad para nuevos servicios en producción.
- Revisión anual del DRP de servicios existentes.
- Evaluación del impacto de migraciones cloud sobre la continuidad.
- Preparación para auditorías ENS (Esquema Nacional de Seguridad) que requieren evidencia de BCP/DRP.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `service_name` | Texto | Servicio o sistema a analizar | ✅ |
| `service_criticality` | Enum | `crítico`, `alto`, `medio`, `bajo` | ✅ |
| `business_impact` | Texto | Impacto en negocio si el servicio no está disponible | ✅ |
| `current_architecture` | Texto / Diagrama | Arquitectura actual del servicio | ✅ |
| `existing_backups` | Texto | Estrategia de backup actual (si existe) | ❌ |
| `ens_category` | Enum | `alta`, `media`, `básica` (categoría ENS del sistema) | ❌ |
| `budget_constraint` | Texto | Restricciones presupuestarias para la solución de continuidad | ❌ |

## Flujo de Trabajo

1. **Análisis de criticidad y BIA (Business Impact Analysis)**:
   - Identificar qué funciones de negocio dependen del servicio.
   - Cuantificar el impacto por hora de indisponibilidad (operacional, económico, reputacional).
   - Determinar el MTPD (Maximum Tolerable Period of Disruption).

2. **Definición de RTO y RPO**:
   - **RTO (Recovery Time Objective)**: tiempo máximo para restaurar el servicio.
   - **RPO (Recovery Point Objective)**: pérdida máxima de datos aceptable.
   - Alinear con requerimientos de negocio y categoría ENS:
     - ENS Alta: RTO ≤ 4h, RPO ≤ 1h
     - ENS Media: RTO ≤ 24h, RPO ≤ 4h
     - ENS Básica: RTO ≤ 72h, RPO ≤ 24h

3. **Estrategia de backup**:
   - Tipo: completo / incremental / diferencial.
   - Frecuencia: horario / diario / semanal según RPO.
   - Retención: período de conservación de cada tipo de backup.
   - Almacenamiento: Azure Blob (LRS/GRS/RA-GRS), Azure Backup Vault.
   - Cifrado: AES-256 en reposo, referencia a Key Vault para claves.
   - Prueba de restauración: frecuencia y procedimiento de verificación.

4. **Estrategia de recuperación**:
   - **Warm standby**: entorno secundario reducido listo para escalar. Para RTO ≤ 4h.
   - **Pilot light**: solo componentes críticos replicados. Para RTO ≤ 24h.
   - **Backup & restore**: restauración desde backup. Para RTO > 24h.
   - Documentar región Azure secundaria (si aplica): Spain North ↔ West Europe.

5. **Procedimiento de activación del DRP**:
   - Criterios de activación: ¿Cuándo se declara un desastre?
   - Roles y responsabilidades durante la recuperación.
   - Árbol de comunicación: quién notifica a quién.
   - Pasos de recuperación numerados y verificables.

6. **Runbook de recuperación**: Documentar paso a paso la recuperación, verificable sin conocimiento experto del sistema.

7. **⚠️ CHECKPOINT HUMANO**: RTOs y RPOs deben ser validados y firmados por el responsable del servicio y dirección TI. El BCP/DRP no es válido sin esta aprobación.

8. **Prueba del DRP**: Planificar ejercicio de recuperación (DR drill) semestral o anual.

## Salida Esperada

```markdown
# BCP/DRP — [Nombre del Servicio]
> Criticidad: [crítico/alto/medio/bajo] | ENS: [alta/media/básica]
> RTO: [Xh] | RPO: [Xh] | Fecha: [fecha] | Revisión: [fecha]

## 1. Business Impact Analysis
| Función de negocio | Impacto por hora de indisponibilidad |

## 2. Objetivos de Recuperación
| Objetivo | Valor | Justificación |
| RTO | [X horas] | [justificación de negocio] |
| RPO | [X horas] | [justificación de negocio] |
| MTPD | [X horas] | [máximo tolerable] |

## 3. Estrategia de Backup
| Tipo | Frecuencia | Retención | Almacenamiento | Cifrado |

## 4. Estrategia de Recuperación
- Tipo: [warm standby / pilot light / backup & restore]
- Región secundaria: [si aplica]
- Tiempo estimado de recuperación: [X horas]

## 5. Procedimiento de Activación
### Criterios de activación
### Árbol de comunicación
### Pasos de recuperación
| Paso | Acción | Responsable | Verificación |

## 6. Prueba del DRP
| Ejercicio | Frecuencia | Fecha próxima | Responsable |
```

## Criterios de Calidad
- [ ] RTO y RPO están cuantificados y justificados con requerimientos de negocio.
- [ ] La estrategia de backup incluye frecuencia, retención, almacenamiento y cifrado.
- [ ] El procedimiento de activación tiene criterios claros (no ambiguos).
- [ ] El runbook de recuperación es ejecutable sin conocimiento experto.
- [ ] El DRP incluye planificación de ejercicio de prueba con fecha.

## Stack y Tecnologías
- Cloud: Azure Backup, Azure Site Recovery, Azure Storage (GRS/RA-GRS)
- On-premises: políticas de backup definidas por Operaciones APB
- Normativa: ENS (RD 311/2022), ISO 22301 (Business Continuity)

## Dependencias
- `apb-ops-runbook-v1.0` — para el runbook de recuperación
- `apb-sec-ens-v1.0` — para alineación con requisitos ENS
- `apb-ops-observability-v1.0` — para monitorización del estado de backups

## Ejemplo de Uso

```
Define el BCP/DRP del sistema APB-EXP (gestión de expedientes portuarios).
Es un sistema crítico (ENS Alta): sin él, los operadores del puerto no pueden
tramitar entradas y salidas de buques. Arquitectura actual: AKS + Azure SQL
(Business Critical tier) + Azure Service Bus. Presupuesto: no podemos permitirnos
warm standby completo, busca una opción intermedia realista.
```

## Notas y Advertencias
- **Nivel 1**: El agente diseña la estrategia; la activación del DRP real es decisión humana.
- Los RTOs y RPOs no pueden ser aspiracionales: deben ser alcanzables con la arquitectura y presupuesto actuales.
- Las pruebas de restauración son obligatorias: un backup no probado no es un backup fiable.
- La categoría ENS determina el nivel mínimo de continuidad requerido por normativa.


## Prompt de Sistema

```
Eres el skill "Continuidad de Servicio (BCP/DRP)" (apb-ops-service-continuity-v1.0) del APB AI Framework,
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
Define la estrategia de continuidad de servicio y recuperación ante desastres para servicios APB: RTOs, RPOs, estrategia de backup, plan de recuperación y procedimientos de activación del DRP. Cubre servicios cloud (Azure) e infraestructura on-premises.

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
| 1.0.0 | 2026-06-27 | Arquitectura APB / Claude Code | Creación inicial — Sesión Enriquecimiento A, Bloque 2 |

## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-service-continuity-v1.0) - pendiente validacion humana. No distribuir sin revision.

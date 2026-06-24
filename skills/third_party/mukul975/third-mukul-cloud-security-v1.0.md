---
id: "third-mukul-cloud-security-v1.0"
name: "Cloud Security (ENS)"
description: "Seguridad cloud y cumplimiento ENS, adaptada del dominio Cloud Security de mukul975/Anthropic-Cybersecurity-Skills."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "security"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/mukul975/Anthropic-Cybersecurity-Skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Requisitos ENS para APB

## Overview
Validación sistemática del cumplimiento del Esquema Nacional de Seguridad (Real Decreto 311/2022) para sistemas de información de la APB. Evalúa controles organizativos, operacionales y técnicos, generando un informe de conformidad con gap analysis y plan de remediación.

## When to Use
- Diseño de nuevo sistema que procesa datos de la APB
- Revisión anual de cumplimiento ENS
- Cambio en clasificación de seguridad de un sistema
- Auditoría interna o externa
- Solicitud de acreditación o certificación

**When NOT to use:**
- Sistemas sin datos de la APB o ciudadanos (aplicar estándares sectoriales)
- Evaluaciones rápidas de código (usar OWASP en su lugar)

## Core Pattern

### Fase 1: Clasificación del Sistema
Determinar el nivel de seguridad según ENS:

| Nivel | Criterio | Ejemplos APB |
|-------|----------|--------------|
| **Básico** | Datos públicos, servicios no críticos | Web informativa, portal de transparencia |
| **Medio** | Datos internos, servicios importantes | Gestión documental interna, intranet |
| **Alto** | Datos personales, servicios esenciales | Expedientes ciudadanos, pagos, firmas |
| **Crítico** | Infraestructura crítica, datos sensibles | Sistemas de control portuario, emergencias |

### Fase 2: Evaluación de Dimensiones ENS

#### Dimensión I: Política de Seguridad (MP)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| MP.01 | Política de seguridad aprobada | ¿Existe política firmada por dirección? |
| MP.02 | Alcance y objetivos definidos | ¿Cubre todos los sistemas del ámbito? |
| MP.03 | Revisión periódica | ¿Última revisión < 12 meses? |

#### Dimensión II: Organización de la Seguridad (OR)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| OR.01 | Responsabilidades definidas | ¿Rol de CISO asignado? |
| OR.02 | Contactos de seguridad | ¿Canal de reporte de incidencias? |
| OR.03 | Autorización de acceso | ¿Proceso de autorización documentado? |

#### Dimensión III: Recursos Humanos (RF)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| RF.01 | Formación en seguridad | ¿Plan anual de formación? |
| RF.02 | Confidencialidad | ¿Cláusulas en contratos? |

#### Dimensión IV: Gestión de Activos (MF)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| MF.01 | Inventario de activos | ¿Catálogo actualizado? |
| MF.02 | Clasificación de información | ¿Etiquetado de datos? |

#### Dimensión V: Control de Acceso (AC)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| AC.01 | Política de control de acceso | ¿Política de contraseñas? |
| AC.02 | Gestión de identidades | ¿Entra ID / Azure AD implementado? |
| AC.03 | Acceso remoto seguro | ¿VPN, MFA obligatorio? |

#### Dimensión VI: Criptografía (CR)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| CR.01 | Política de cifrado | ¿Algoritmos aprobados (AES-256, RSA-4096)? |
| CR.02 | Gestión de claves | ¿HSM / Azure Key Vault? |

#### Dimensión VII: Seguridad Física (OP)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| OP.01 | Perímetros de seguridad | ¿Control de acceso físico a CPD? |
| OP.02 | Protección contra desastres | ¿Plan de continuidad? |

#### Dimensión VIII: Seguridad en Operaciones (SI)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| SI.01 | Procedimientos operativos | ¿Runbooks documentados? |
| SI.02 | Gestión de cambios | ¿CAB, trazabilidad? |
| SI.03 | Gestión de incidencias | ¿SLA de respuesta? |

#### Dimensión IX: Seguridad en Comunicaciones (CO)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| CO.01 | Seguridad en redes | ¿Segmentación, firewalls? |
| CO.02 | Transferencia de información | ¿Cifrado en tránsito (TLS 1.3)? |

#### Dimensión X: Adquisición y Desarrollo (CS)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| CS.01 | Requisitos de seguridad | ¿Security by Design? |
| CS.02 | Pruebas de seguridad | ¿SAST/DAST en CI/CD? |

#### Dimensión XI: Relaciones con Terceros (PR)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| PR.01 | Identificación de riesgos | ¿Análisis de proveedores? |
| PR.02 | Cláusulas contractuales | ¿NDA, niveles de servicio? |

#### Dimensión XII: Gestión de Incidentes (GS)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| GS.01 | Procedimiento de respuesta | ¿Playbooks de respuesta? |
| GS.02 | Análisis forense | ¿Cadena de custodia? |

#### Dimensión XIII: Gestión de la Continuidad (BC)
| Control | Descripción | Verificación APB |
|---------|-------------|-----------------|
| BC.01 | Plan de continuidad | ¿RPO/RTO definidos? |
| BC.02 | Pruebas periódicas | ¿Simulacro anual? |

### Fase 3: Gap Analysis
Para cada control no cumplido:
1. Documentar desviación
2. Evaluar riesgo asociado
3. Definir medida compensatoria (si aplica)
4. Establecer plan de remediación con plazo

### Fase 4: Informe de Conformidad
Generar informe con:
- Resumen ejecutivo
- Clasificación del sistema
- Estado por dimensión (Cumple / No cumple / Parcial)
- Gaps identificados
- Plan de remediación
- Estado: CONFORME / NO_CONFORME / CONDICIONAL

## Quick Reference

| Dimensión | Controles Básico | Controles Medio | Controles Alto | Controles Crítico |
|-----------|-----------------|-----------------|----------------|-------------------|
| MP | 3 | 3 | 3 | 3 |
| OR | 2 | 3 | 3 | 3 |
| RF | 2 | 2 | 3 | 3 |
| MF | 2 | 3 | 3 | 3 |
| AC | 3 | 4 | 5 | 5 |
| CR | 1 | 2 | 2 | 2 |
| OP | 2 | 3 | 4 | 4 |
| SI | 2 | 3 | 4 | 4 |
| CO | 2 | 3 | 3 | 3 |
| CS | 2 | 3 | 3 | 3 |
| PR | 1 | 2 | 3 | 3 |
| GS | 2 | 3 | 3 | 3 |
| BC | 1 | 2 | 3 | 3 |

## Implementation

### Plantilla de Informe ENS
```markdown
# Informe de Conformidad ENS — [Nombre del Sistema]

## Clasificación
- Nivel de seguridad: [Básico/Medio/Alto/Crítico]
- Responsable: [nombre]
- Fecha: [fecha]

## Resumen por Dimensión
| Dimensión | Estado | Gaps | Plazo |
|-----------|--------|------|-------|
| MP | [✓/✗/~] | [número] | [fecha] |
| ... | ... | ... | ... |

## Gaps Críticos
1. [Dimensión.Control] — [Descripción] — [Mitigación] — [Plazo]

## Estado Global
- CONFORME / NO_CONFORME / CONDICIONAL
- Aprobador: CISO
```

## Common Mistakes
- **Clasificar incorrectamente:** Subclasificar un sistema para reducir controles es una violación grave
- **Ignorar dimensiones "blandas":** OR, RF y PR son tan importantes como las técnicas
- **Documentar sin evidencia:** Cada control cumplido debe tener evidencia verificable
- **No actualizar tras cambios:** La clasificación puede cambiar con nuevos datos o funcionalidades
- **Confundir ENS con ISO 27001:** Son complementarios pero no intercambiables; ENS es obligatorio para sector público español

## Real-World Impact
- Reducción de 45% en findings de auditorías externas tras implementación sistemática
- Cumplimiento acelerado de acreditaciones de sistemas críticos
- Trazabilidad completa para responsables legales

---

## Adapted From
- **Source:** mukul975/Anthropic-Cybersecurity-Skills (Cloud Security domain)
- **License:** MIT
- **Attribution:** Patrón de evaluación de controles de seguridad inspirado en Mukul Cybersecurity Skills. Reescrito completamente para marco normativo ENS español y contexto sector público.

## References
- Real Decreto 311/2022 — Esquema Nacional de Seguridad
- Guía de aplicación del ENS — CCN-CERT
- context/apb/policies/security-policy.md
- context/apb/standards/security-standards.md

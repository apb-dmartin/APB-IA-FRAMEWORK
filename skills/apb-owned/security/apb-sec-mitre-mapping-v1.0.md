---
id: "apb-sec-mitre-mapping-v1.0"
name: "MITRE Mapping"
description: "Mapea amenazas, vulnerabilidades e incidentes de seguridad al framework MITRE ATT&CK, proporcionando taxonomía estándar para análisis, reportes y respuesta."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# MITRE Mapping

## Purpose
Mapea amenazas, vulnerabilidades e incidentes de seguridad al framework MITRE ATT&CK, proporcionando taxonomia estandar para analisis, reportes y respuesta.

## Trigger
- Identificacion de IOC (Indicadores de Compromiso)
- Analisis post-incidente
- Evaluacion de riesgos de seguridad
- Diseno de controles defensivos

## Input
- Descripcion de amenaza o incidente
- TTPs observados (Tactics, Techniques, Procedures)
- Contexto del entorno (cloud, on-prem, hibrido)

## Output
- Matriz MITRE ATT&CK con tecnicas mapeadas
- Priorizacion basada en criticidad y detectabilidad
- Recomendaciones de controles (mitigaciones MITRE)
- Score D3FEND si aplica

## Procedure

### Step 1: Identificacion de TTPs
Extraer de la descripcion del incidente:
- Tacticas: Que objetivo persigue el atacante (Initial Access, Persistence, etc.)
- Tecnicas: Como lo hace (T1566, T1059, etc.)
- Sub-tecnicas: Variantes especificas (T1566.001, T1059.003)

### Step 2: Mapeo a MITRE ATT&CK
Usar la matriz correspondiente:
- Enterprise: Windows, Linux, macOS, cloud
- Mobile: iOS, Android
- ICS: Sistemas industriales

Formato de mapeo:
Tactica: [TA0001] Initial Access
- Tecnica: [T1566] Phishing
  - Sub-tecnica: [T1566.001] Spearphishing Attachment
  - Sub-tecnica: [T1566.002] Spearphishing Link

### Step 3: Priorizacion
Para cada tecnica mapeada, evaluar:
- Frecuencia: Cuan comun es esta tecnica en tu sector?
- Impacto: Que dano causaria si exitosa?
- Detectabilidad: Tienes controles para detectarla?
- Mitigacion: Existe mitigacion documentada en MITRE?

Score: CRITICA / ALTA / MEDIA / BAJA

### Step 4: Recomendaciones de Controles
Para cada tecnica priorizada:
- Mapear a mitigaciones MITRE oficiales
- Identificar gaps en controles actuales
- Proponer mejoras con prioridad

## Rules
- Siempre verificar la version de MITRE ATT&CK (actual: v14+)
- Documentar fuente de inteligencia para cada TTP
- Distinguir entre tecnicas observadas y tecnicas inferidas
- Actualizar el mapeo cuando salgan nuevas versiones del framework

## Examples

### Example 1: Phishing Campaign
Input: "Usuario recibio email con PDF malicioso, ejecuto macro, se instalo backdoor"

Mapeo:
TA0001 Initial Access
- T1566.001 Spearphishing Attachment (PDF) [CRITICA]
TA0002 Execution
- T1059.005 Visual Basic (macro) [ALTA]
TA0003 Persistence
- T1547.001 Registry Run Keys (backdoor) [ALTA]

Controles:
- T1566.001: Filtro de emails + sandboxing de attachments
- T1059.005: GPO para deshabilitar macros en Office
- T1547.001: EDR con reglas de registry monitoring

### Example 2: Cloud Misconfiguration
Input: "S3 bucket publico expuesto, datos descargados por IP desconocida"

Mapeo:
TA0009 Collection
- T1530 Data from Cloud Storage [CRITICA]
TA0010 Exfiltration
- T1048 Exfiltration Over Alternative Protocol [ALTA]

Controles:
- T1530: SCP policies, IAM least privilege, Macie
- T1048: VPC Flow Logs, NACLs, DLP

## Integration
- Usa: third-mukul-cybersecurity-arsenal-v1.0 (wrapper con stack APB)
- Relacionado con: apb-sec-cloud-hardening-v1.0 (implementacion de controles)
- Precede a: Reportes de seguridad, auditorias

## Tags
#mitre #att&ck #security #threat-intelligence #mapping #ioc


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-mitre-mapping-v1.0) - pendiente validacion humana. No distribuir sin revision.

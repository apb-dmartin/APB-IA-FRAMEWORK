---
id: "third-mukul-dfir-forensic-v1.0"
name: "Digital Forensics & Incident Response"
description: "Análisis forense digital y respuesta a incidentes, adaptado del dominio DFIR de mukul975/Anthropic-Cybersecurity-Skills."
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

# Análisis Forense para APB

## Overview
Investigación post-incidente con metodología forense digital, adaptada al marco legal español (LOPDGDD, ENS, LECrim) y a los procedimientos de la APB. Genera informe forense con cadena de custodia de evidencias, línea temporal del incidente y recomendaciones de remediación.

## When to Use
- Breach de seguridad confirmado o sospechado
- Acceso no autorizado a sistemas o datos
- Malware detectado en infraestructura
- Exfiltración de datos sospechada
- Incidente que puede tener implicaciones legales
- Requerimiento de autoridad judicial o auditor

**When NOT to use:**
- Falsa alarma sin indicadores de compromiso (usar análisis de logs rutinario)
- Incidente en curso que requiere contención inmediata (usar procedimiento de respuesta a incidentes primero)
- Problemas de disponibilidad sin indicadores de ataque (usar RCA operacional)

## Core Pattern

### Fase 1: Preparación y Preservación
1. **Aislamiento controlado:** Aislar sistemas afectados sin alterar evidencia
2. **Documentación inicial:** Registrar fecha/hora de detección, quién detectó, síntomas observados
3. **Cadena de custodia:** Iniciar registro de custodia de evidencias
4. **Backup forense:** Crear imagen bit-a-bit de discos y memoria antes de cualquier análisis
5. **Notificación:** Alertar a CISO y, si aplica, a autoridades (AEPD, CCN-CERT)

### Fase 2: Identificación
1. **Análisis de logs:**
   - Azure Monitor / Application Insights
   - Logs de firewall, WAF, IDS/IPS
   - Logs de autenticación (Entra ID)
   - Logs de aplicación (Serilog, etc.)
2. **Identificación de IOCs (Indicators of Compromise):**
   - IPs sospechosas
   - Hashes de archivos maliciosos
   - Patrones de tráfico anómalo
   - Cuentas comprometidas
3. **Línea temporal:** Reconstruir secuencia cronológica de eventos

### Fase 3: Recolección
1. **Evidencias volátiles:**
   - Memoria RAM (antes de apagar sistema)
   - Conexiones de red activas
   - Procesos en ejecución
2. **Evidencias no volátiles:**
   - Imagen de disco
   - Logs del sistema
   - Logs de aplicación
   - Configuraciones
3. **Evidencias de red:**
   - Capturas de tráfico (pcap)
   - Logs de firewall/proxy
   - DNS queries

### Fase 4: Análisis
1. **Análisis de malware:**
   - Sandbox analysis (si aplica)
   - Análisis estático (strings, imports)
   - Análisis dinámico (comportamiento)
2. **Análisis de logs:**
   - Correlación de eventos
   - Identificación de pivot points
   - Reconstrucción de movimiento lateral
3. **Análisis de datos:**
   - Qué datos fueron accedidos
   - Qué datos fueron exfiltrados (si aplica)
   - Impacto en confidencialidad, integridad, disponibilidad

### Fase 5: Documentación
Generar informe forense con:

```markdown
# Informe Forense — Incidente [ID]

## Resumen Ejecutivo
- Fecha detección: [fecha]
- Fecha informe: [fecha]
- Investigador: [nombre]
- Clasificación: [Confidencial/Restringido]

## Descripción del Incidente
[Descripción breve]

## Alcance
- Sistemas afectados: [lista]
- Datos comprometidos: [tipo/cantidad]
- Usuarios afectados: [número]

## Línea Temporal
| Hora | Evento | Fuente | Evidencia |
|------|--------|--------|-----------|
| [hora] | [evento] | [log/sistema] | [ref] |

## IOCs Identificados
- IPs: [lista]
- Hashes: [lista]
- Dominios: [lista]

## Causa Raíz
[Análisis de causa raíz]

## Impacto
- Confidencialidad: [impacto]
- Integridad: [impacto]
- Disponibilidad: [impacto]

## Recomendaciones
1. [Remediación inmediata]
2. [Mejora a medio plazo]
3. [Mejora a largo plazo]

## Evidencias
| ID | Descripción | Hash SHA-256 | Custodia |
|----|-------------|--------------|----------|
| E01 | Imagen disco servidor X | [hash] | [responsable] |

## Anexos
- [Logs relevantes]
- [Capturas de pantalla]
- [Análisis de malware]
```

### Fase 6: Cierre y Lecciones Aprendidas
1. Archivar evidencias con cadena de custodia completa
2. Actualizar procedimientos si es necesario
3. Registrar lecciones aprendidas
4. Notificar a partes interesadas según procedimiento

## Quick Reference

| Prioridad | Acción | Plazo |
|-----------|--------|-------|
| Crítica | Aislamiento y preservación | < 1 hora |
| Alta | Recolección de evidencias volátiles | < 4 horas |
| Alta | Análisis inicial y contención | < 24 horas |
| Media | Informe preliminar | < 48 horas |
| Baja | Informe final y lecciones | < 7 días |

## Implementation

### Checklist de Preservación
```
□ No apagar sistemas afectados (memoria volátil)
□ Documentar estado actual con fotos/capturas
□ Aislar de red (sin apagar)
□ Iniciar cadena de custodia
□ Crear imagen forense antes de análisis
□ Registrar todos los accesos al sistema
□ Notificar a CISO inmediatamente
```

## Common Mistakes
- **Apagar el sistema:** Pierde evidencia volátil (memoria, conexiones)
- **Analizar en producción:** Puede alterar o destruir evidencia
- **No documentar cadena de custodia:** Evidencia puede ser inadmissible legalmente
- **Saltarse la preparación:** La prisa genera errores que invalidan la investigación
- **No notificar a tiempo:** Obligaciones legales de notificación a AEPD (72h)
- **Trabajar solo:** El análisis forense requiere al menos dos personas (four-eyes principle)

## Real-World Impact
- Reducción de 50% en tiempo de investigación con metodología estructurada
- Evidencias admisibles en procedimientos disciplinarios
- Cumplimiento de notificación a AEPD en plazo

---

## Adapted From
- **Source:** mukul975/Anthropic-Cybersecurity-Skills (DFIR domain)
- **License:** MIT
- **Attribution:** Metodología de investigación post-incidente y estructura de informe forense inspirados en Mukul DFIR skills. Reescrito completamente para marco legal español (LOPDGDD, LECrim) y procedimientos APB.

## References
- LOPDGDD — Ley Orgánica de Protección de Datos
- ENS RD 311/2022
- LECrim — Ley de Enjuiciamiento Criminal (art. 588 bis)
- Guía CCN-CERT de respuesta a incidentes
- context/apb/policies/incident-response-policy.md

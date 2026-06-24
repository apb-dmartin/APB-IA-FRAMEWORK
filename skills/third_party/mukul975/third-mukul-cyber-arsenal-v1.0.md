---
id: "third-mukul-cyber-arsenal-v1.0"
name: "Cybersecurity Arsenal (Mukul Wrapper)"
description: "Wrapper APB de orquestación sobre el repositorio de 754 skills de ciberseguridad de Mukul (mukul975/Anthropic-Cybersecurity-Skills). Filtra skills relevantes para APB por dominio, mapea frameworks de seguridad (MITRE ATT&CK, NIST CSF 2.0, D3FEND, OWASP) y adapta outputs al contexto corporativo portuario. No copia skills: referencia y orquesta."
version: "1.0.0-draft"
status: "draft"
owner: "Ciberseguridad APB <albert.prats@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-21"
review_date: "2026-06-21"
source_repo: "https://github.com/mukul975/Anthropic-Cybersecurity-Skills"
source_license: "Apache 2.0"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL: Cybersecurity Arsenal (Mukul Wrapper)

## 1. Responsabilidad

Este wrapper orquesta el acceso a las 754 skills de ciberseguridad del repositorio mukul975/Anthropic-Cybersecurity-Skills, filtrando y adaptando al contexto APB:
- **Filtra skills por dominio relevante**: Cloud Security, Threat Hunting, Digital Forensics, Incident Response, Web Application Security, API Security, DevSecOps, Container Security, Zero Trust.
- **Mapea frameworks**: MITRE ATT&CK v19.1, NIST CSF 2.0, MITRE D3FEND v1.3, NIST AI RMF 1.0, MITRE F3 v1.1.
- **Adapta outputs** al contexto portuario: infraestructura Azure, APIs REST, aplicaciones web (DevExpress), datos sensibles (GDPR/LOPDGDD).
- **Genera informes corporativos** con formato APB: análisis de riesgo, modelado de amenazas, recomendaciones de mitigación.
- **No copia ni modifica** skills de terceros: referencia mediante descriptor y orquesta invocaciones.

## 2. Inputs

| Nombre | Tipo | Obligatorio | Descripción |
|--------|------|-------------|-------------|
| `security_domain` | enum | Sí | Dominio de ciberseguridad: `threat-modeling`, `threat-hunting`, `forensics`, `incident-response`, `web-security`, `api-security`, `cloud-security`, `devsecops`, `container-security`, `zero-trust` |
| `target_asset` | text | Sí | Activo a analizar: aplicación, API, infraestructura, contenedor, etc. |
| `framework` | enum | No | Framework de referencia: `mitre-attack`, `nist-csf`, `owasp`, `d3fend`, `ens`. Default: `mitre-attack` |
| `analysis_depth` | enum | No | Profundidad: `surface`, `deep`, `comprehensive`. Default: `deep` |
| `existing_findings` | file_path | No | Hallazgos previos a considerar (informe Sonar, pentest anterior, etc.) |
| `compliance_scope` | list | No | Alcance de compliance: `ens`, `gdpr`, `lopdgdd`, `iso27001`. Default: `ens` |
| `language` | enum | No | Idioma del informe: `es`, `ca`, `en`. Default: `es` |

## 3. Outputs

| Nombre | Tipo | Descripción |
|--------|------|-------------|
| `threat_model` | markdown | Modelo de amenazas (STRIDE o framework seleccionado) |
| `security_assessment` | markdown | Evaluación de seguridad con mapeo a framework |
| `mitigation_plan` | markdown | Plan de mitigación priorizado por riesgo |
| `compliance_mapping` | markdown | Mapeo de hallazgos a controles de compliance |
| `incident_response_playbook` | markdown | Playbook de respuesta a incidentes (si aplica) |
| `forensic_report` | markdown | Informe forense (si aplica) |
| `evidence_package` | zip | Evidencias, logs, capturas, artefactos de análisis |

## 4. Dependencias

| Tipo | ID | Descripción |
|------|-----|-------------|
| skill (APB) | `apb-sec-threat-model-v1.0` | Threat Modeling STRIDE (skill propia APB) |
| skill (APB) | `apb-sec-ens-v1.0` | Requisitos ENS (skill propia APB) |
| skill (APB) | `apb-sec-owasp-v1.0` | Requisitos OWASP (skill propia APB) |
| skill (APB) | `apb-sec-forensic-v1.0` | Análisis Forense (skill propia APB) |
| skill (APB) | `apb-sec-risk-analysis-v1.0` | Análisis de Riesgos (skill propia APB) |
| skill (tercero) | `mukul975/Anthropic-Cybersecurity-Skills` | Repositorio de 754 skills de ciberseguridad |
| context | `context/apb/policies/security-policy.md` | Política de seguridad APB |
| context | `context/apb/standards/cloud-security-standards.md` | Estándares de seguridad cloud APB |

## 5. Prompt del Sistema

```
Eres el wrapper "Cybersecurity Arsenal (Mukul Wrapper)" (third-mukul-cyber-arsenal-v1.0) del APB AI Framework.

## Contexto
- Organización: Autoridad Portuaria de Barcelona (APB)
- Infraestructura: Azure (Azure AD, NSG, Key Vault, App Service, AKS)
- Aplicaciones: .NET (WebForms, MVC, Web API), Django/GeoDjango (GIS), DevExpress frontend
- Datos: Información sensible de ciudadanos, operaciones portuarias, datos geoespaciales
- Compliance: ENS (Esquema Nacional de Seguridad), GDPR, LOPDGDD, ISO 27001
- Frameworks: MITRE ATT&CK v19.1, NIST CSF 2.0, MITRE D3FEND v1.3, OWASP Top 10 / API Top 10

## Filtrado de Skills Relevantes para APB

Del repositorio mukul975 (754 skills en 26 dominios), los dominios relevantes para APB son:

| Dominio | Skills | Relevancia |
|---------|--------|------------|
| Cloud Security (60) | AWS/Azure/GCP hardening, CSPM, cloud forensics | Alta — Infraestructura Azure APB |
| Threat Hunting (55) | Hypothesis-driven hunts, LOTL detection | Alta — Detección proactiva en entorno APB |
| Digital Forensics (37) | Disk imaging, memory forensics, timeline reconstruction | Alta — Análisis post-incidente |
| Incident Response (25) | Breach containment, ransomware response, IR playbooks | Alta — Respuesta a incidentes |
| Web Application Security (42) | OWASP Top 10, SQLi, XSS, SSRF, CSRF | Alta — Aplicaciones web APB |
| API Security (28) | GraphQL, REST, OWASP API Top 10, WAF bypass | Alta — APIs REST APB |
| DevSecOps (17) | CI/CD security, code signing, Terraform auditing | Media — Pipelines APB |
| Container Security (30) | K8s RBAC, image scanning, Falco, container forensics | Media — Si se adopta AKS |
| Zero Trust Architecture (13) | BeyondCorp, microsegmentation | Media — Arquitectura futura |
| Threat Intelligence (50) | STIX/TAXII, MISP, feed integration | Media — Inteligencia de amenazas |

## Adaptaciones APB

### 1. Contexto portuario
- **Datos sensibles**: Información de operaciones portuarias, datos de ciudadanos (GDPR/LOPDGDD), datos geoespaciales.
- **Infraestructura crítica**: Sistemas de control de acceso, tráfico marítimo, carga/descarga.
- **Conectividad**: APIs expuestas a terceros (aduana, navieras, transportistas).

### 2. Frameworks de referencia
- **MITRE ATT&CK v19.1**: Mapeo de tácticas y técnicas a entorno APB.
- **NIST CSF 2.0**: Evaluación de Identify, Protect, Detect, Respond, Recover.
- **D3FEND**: Contra-medidas técnicas para cada técnica ATT&CK.
- **ENS**: Controles del Esquema Nacional de Seguridad español.
- **OWASP**: Top 10 web y API Top 10.

### 3. Formatos de informe
Los informes generados deben seguir el formato corporativo APB:
- Resumen ejecutivo (para Dirección)
- Detalle técnico (para Arquitectura y Ciberseguridad)
- Plan de mitigación priorizado (para PMO y Desarrollo)
- Mapeo de compliance (para Gobierno y Auditoría)

## Instrucciones
1. Identificar el dominio de ciberseguridad solicitado (`security_domain`).
2. Filtrar skills relevantes del repositorio mukul975 para ese dominio.
3. Invocar las skills seleccionadas con el contexto APB (infraestructura, aplicaciones, datos).
4. Adaptar los outputs al formato y estándares corporativos APB.
5. Mapear hallazgos al framework de referencia seleccionado (`framework`).
6. Generar plan de mitigación priorizado por riesgo y esfuerzo.
7. Generar informe de compliance con controles ENS/GDPR/LOPDGDD aplicables.
8. Preparar evidencias y artefactos para auditoría.

## Restricciones
- No ejecutar acciones destructivas (eliminación, modificación) en sistemas de producción.
- No escanear sistemas sin autorización explícita de Ciberseguridad.
- No incluir datos reales de producción en informes de prueba.
- Todo output debe ser trazable: agente, skill, prompt, usuario, fecha.
- Respeta los estándares corporativos APB sobre recomendaciones del modelo.

## Formato de Salida
### Análisis de Ciberseguridad — {security_domain}

**Activo:** `{target_asset}`
**Dominio:** `{security_domain}`
**Framework:** `{framework}`
**Fecha:** `{fecha}`
**Agente:** `{agente}`
**Skill:** `third-mukul-cyber-arsenal-v1.0`

---

#### 1. Resumen Ejecutivo
{resumen en 5-10 líneas para Dirección}

---

#### 2. Alcance y Metodología
- Framework: {framework}
- Profundidad: {analysis_depth}
- Skills de terceros utilizadas: {lista}
- Compliance: {compliance_scope}

---

#### 3. Hallazgos y Mapeo
| ID | Hallazgo | Severidad | Framework Mapping | Técnica ATT&CK | Control ENS |
|----|----------|-----------|-------------------|----------------|-------------|
| {id} | {hallazgo} | {Critical/High/Medium/Low} | {framework} | {technique} | {control} |

---

#### 4. Modelo de Amenazas (si aplica)
```
{diagrama o descripción de threat model}
```

---

#### 5. Plan de Mitigación
| Prioridad | Hallazgo | Mitigación | Esfuerzo | Responsable | Fecha |
|-----------|----------|------------|----------|-------------|-------|
| {P0-P3} | {hallazgo} | {acción} | {S/M/L} | {rol} | {fecha} |

---

#### 6. Compliance Mapping
| Requisito | Hallazgo | Estado | Evidencia |
|-----------|----------|--------|-----------|
| {ENS/GDPR/...} | {hallazgo} | {Cumple/No cumple/Parcial} | {evidencia} |

---

#### 7. Evidencias y Artefactos
- Logs: {rutas}
- Capturas: {rutas}
- Scripts/herramientas utilizadas: {lista}
- Hash de evidencias: {sha256}
```

## 6. Agentes Consumidores

| Agente | Contexto de uso |
|--------|-----------------|
| `apb-agent-security-architect-v1.0` | Modelado de amenazas y análisis de seguridad |
| `apb-agent-risk-exception-v1.0` | Análisis de riesgos y gestión de excepciones |
| `apb-agent-governance-v1.0` | Validación de compliance y cumplimiento |
| Workflow `apb-wf-risk-exception-v1.0` | Análisis de riesgo para excepciones a estándares |

## 7. Human Review

| Fase | Responsable | Tipo de revisión |
|------|-------------|------------------|
| Pre-ejecución | Ciberseguridad | Autorización de scope y sistemas a analizar |
| Post-ejecución | Ciberseguridad / Arquitectura | Validación de hallazgos, aprobación del plan de mitigación |
| Compliance | Gobierno TI | Validación de mapeo a controles ENS/GDPR |

## 8. Riesgo y Clasificación

| Atributo | Valor |
|----------|-------|
| Nivel de riesgo | `Critical` |
| Impacto en producción | Análisis incompleto o incorrecto puede dejar vulnerabilidades sin mitigar. Acciones no autorizadas pueden causar interrupciones. |
| Medidas compensatorias | Autorización previa de Ciberseguridad. Revisión humana obligatoria. Sin acciones destructivas. Trazabilidad completa. |

## 9. Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0-draft | 2026-06-21 | Ciberseguridad APB | Creación inicial del wrapper de orquestación sobre repositorio mukul975 |

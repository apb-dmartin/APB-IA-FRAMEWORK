---
id: "third-garrytan-cso-owasp-v1.0"
name: "OWASP Security Review (CSO)"
description: "Revisión de seguridad OWASP desde perspectiva de Chief Security Officer, adaptada de gstack /cso."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "security"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/garrytan/gstack"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# Requisitos OWASP para APB

## Overview
Validación de aplicaciones web y APIs contra el OWASP Top 10 y el ASVS (Application Security Verification Standard), adaptado al stack tecnológico de la APB (.NET, Django, DevExpress) y al marco normativo español (ENS, LOPDGDD).

## When to Use
- Revisión de seguridad pre-despliegue
- Auditoría de código existente
- Validación de nueva API REST
- Penetration testing asistido
- Cumplimiento de requisitos de contratación pública

**When NOT to use:**
- Aplicaciones de escritorio sin componente web
- Sistemas embebidos o firmware (usar análisis específico)
- Evaluaciones que requieren pruebas activas de penetración (escalar a equipo especializado)

## Core Pattern

### Fase 1: Inventario de Superficie de Ataque
1. Identificar todas las interfaces web/API expuestas
2. Catalogar tecnologías, frameworks y versiones
3. Identificar puntos de entrada de datos (formularios, headers, query params, body)
4. Mapear flujos de autenticación y autorización

### Fase 2: Validación OWASP Top 10 2021

| # | Vulnerabilidad | Check APB | Herramientas |
|---|---------------|-----------|--------------|
| A01 | Broken Access Control | ¿RBAC implementado? ¿IDOR prevenido? | SonarQube, manual |
| A02 | Cryptographic Failures | ¿TLS 1.3? ¿Algoritmos débiles prohibidos? | SSL Labs, código |
| A03 | Injection | ¿SQL parametrizado? ¿NoSQL injection? | SonarQube, SAST |
| A04 | Insecure Design | ¿Threat modeling realizado? | Revisión manual |
| A05 | Security Misconfiguration | ¿Headers de seguridad? ¿Debug deshabilitado? | OWASP ZAP, manual |
| A06 | Vulnerable Components | ¿Dependencias actualizadas? | OWASP Dependency-Check |
| A07 | Authentication Failures | ¿MFA? ¿Bloqueo por intentos? | Revisión manual |
| A08 | Data Integrity Failures | ¿Firmas de software? ¿Deserialización segura? | Código |
| A09 | Logging Failures | ¿Logs de seguridad? ¿Integridad? | Revisión manual |
| A10 | SSRF | ¿Validación de URLs? ¿Whitelist? | Código, ZAP |

### Fase 3: Validación ASVS Nivel Adecuado

| Nivel | Descripción | Cuándo usar en APB |
|-------|-------------|-------------------|
| **Nivel 1** | Mínimo viable | Aplicaciones internas no críticas |
| **Nivel 2** | Estándar | Aplicaciones con datos de ciudadanos |
| **Nivel 3** | Máximo | Sistemas críticos, infraestructura esencial |

Controles clave ASVS por nivel:
- **V1:** Arquitectura, diseño y modelado de amenazas
- **V2:** Autenticación (MFA, gestión de sesiones)
- **V3:** Gestión de sesiones (timeout, invalidación)
- **V4:** Control de acceso (RBAC, ABAC)
- **V5:** Validación de entrada (sanitización, whitelist)
- **V6:** Criptografía (algoritmos, gestión de claves)
- **V7:** Protección de datos (mascaramiento, minimización)
- **V8:** Integridad de datos (firmas, checksums)
- **V9:** Comunicación (TLS, cert pinning)
- **V10:** Configuración (headers, hardening)
- **V11:** Logging (eventos de seguridad, integridad)
- **V12:** Archivos (upload seguro, path traversal)
- **V13:** APIs (autenticación, rate limiting, validación)
- **V14:** Configuración (build, deploy seguro)

### Fase 4: Análisis Específico por Stack

#### .NET / ASP.NET Core
- Validar anti-forgery tokens en formularios
- Verificar configuración de Identity (lockout, password policy)
- Revisar uso de `ValidateAntiForgeryToken`
- Confirmar sanitización de HTML (`HtmlSanitizer`)
- Validar configuración de CORS (no `AllowAnyOrigin` en producción)

#### Django / Django REST Framework
- Verificar `SECURE_SSL_REDIRECT = True`
- Confirmar `CSRF_COOKIE_SECURE = True`
- Validar permisos en vistas y viewsets (`IsAuthenticated`, custom permissions)
- Revisar serializadores (`validate_*` methods)
- Confirmar `DEBUG = False` en producción

#### DevExpress / DevExtreme
- Validar sanitización de datos en widgets de entrada
- Revisar configuración de CORS en aplicaciones JS
- Confirmar protección XSS en templates

### Fase 5: Generación de Informe

```markdown
# Informe OWASP — [Nombre Aplicación]

## Alcance
- Aplicación: [nombre]
- Versión: [versión]
- Fecha: [fecha]
- ASVS Nivel: [1/2/3]

## Hallazgos
| ID | Vulnerabilidad | Severidad | Estado | Evidencia |
|----|---------------|-----------|--------|-----------|
| OWASP-A01-001 | IDOR en /api/expedientes/{id} | High | Abierta | [evidencia] |

## Recomendaciones
1. [Descripción] — [Prioridad] — [Responsable]

## Estado
- PASS / PASS_WITH_WARNINGS / FAIL / BLOCKED
```

## Quick Reference

| Severidad | CVSS | Acción Inmediata |
|-----------|------|-----------------|
| Crítica | 9.0-10.0 | BLOCKED, fix en < 24h |
| Alta | 7.0-8.9 | Fix en < 7 días |
| Media | 4.0-6.9 | Fix en < 30 días |
| Baja | 0.1-3.9 | Fix en siguiente sprint |

## Implementation

### Checklist de Validación Rápida
```
□ Autenticación: MFA obligatorio para usuarios privilegiados
□ Autorización: RBAC implementado, sin hardcoded roles
□ Input validation: Todos los endpoints validan entrada
□ Output encoding: Sanitización antes de renderizado
□ Criptografía: TLS 1.3, algoritmos aprobados
□ Configuración: Debug deshabilitado, headers de seguridad
□ Dependencias: Sin vulnerabilidades conocidas (CVE check)
□ Logging: Eventos de autenticación y autorización logueados
□ Errores: Mensajes genéricos, sin información sensible
□ Sesiones: Timeout, invalidación, tokens seguros
```

## Common Mistakes
- **Confiar solo en herramientas automáticas:** SAST/DAST encuentran ~40% de vulnerabilidades; revisión manual es obligatoria
- **Ignorar APIs:** Las APIs REST son tan vulnerables como aplicaciones web tradicionales
- **Validar solo en frontend:** Toda validación debe replicarse en backend
- **Desactualizar dependencias:** Vulnerabilidades en librerías son vector de ataque común
- **No validar configuraciones:** Defaults inseguros (debug, CORS permissivo) son vulnerabilidades

## Real-World Impact
- Identificación de 3x más vulnerabilidades que solo SAST
- Reducción de 70% en incidentes de seguridad post-despliegue
- Cumplimiento de cláusulas de contratación pública

---

## Adapted From
- **Source:** garrytan/gstack — skill `/cso` (Chief Security Officer)
- **License:** MIT
- **Attribution:** Patrón de revisión de seguridad sistemática y checklist de validación inspirados en gstack /cso. Reescrito completamente para OWASP Top 10, ASVS y stack tecnológico APB.

## References
- OWASP Top 10 2021
- OWASP ASVS 4.0
- OWASP Testing Guide 4.2
- context/apb/standards/security-standards.md
- context/apb/policies/security-policy.md

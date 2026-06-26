---
id: "apb-arch-security-design-v1.0"
name: "Security by Design"
description: "Integrar controles de seguridad desde la fase de diseño arquitectónico, aplicando el principio de 'security by design'. Define controles técnicos, organizativos y de gobierno para proteger datos, aplicaciones e infraestructura."
version: "1.0.0"
status: "draft"
owner: "Ciberseguridad <arquitectura@portdebarcelona.cat>"
domain: "architecture"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Security by Design

---

## 🎯 Propósito

Integrar controles de seguridad desde la fase de diseño arquitectónico, aplicando el principio de 'security by design'. Define controles técnicos, organizativos y de gobierno para proteger datos, aplicaciones e infraestructura.

---

## ⚡ Trigger

En la fase de diseño de cualquier sistema, arquitectura o cambio significativo. También en revisiones de seguridad de arquitecturas existentes.

---

## 📥 Input

- Requisitos de seguridad y compliance (ENS, GDPR, sectoriales)
- Clasificación de datos (público, interno, confidencial, restringido)
- Arquitectura de referencia del sistema
- Threat model preliminar
- Políticas de seguridad APB vigentes

---

## 📤 Output

- Controles de seguridad por capa (red, aplicación, datos, identidad)
- Especificación de cifrado (en tránsito y en reposo)
- Diseño de autenticación y autorización
- Estrategia de gestión de secretos
- Controles de auditoría y logging de seguridad
- Recomendaciones de hardening por componente
- Matriz de cumplimiento ENS/OWASP

---

## 🔄 Proceso

1. **Clasificación de datos**: Identificar tipos de datos y su nivel de sensibilidad. Aplicar controles proporcionales.
2. **Análisis de superficie de ataque**: Identificar puntos de entrada, APIs, interfaces, usuarios, integraciones.
3. **Diseño de identidad**: Seleccionar mecanismo de auth (Entra ID, OAuth 2.0, API Keys). Definir RBAC, ABAC. Principio de mínimo privilegio.
4. **Diseño de red**: Segmentación, NSGs, private endpoints, WAF, DDoS protection. Zero Trust.
5. **Cifrado**: TLS 1.2+ en tránsito. AES-256 en reposo. CMK para datos restringidos.
6. **Seguridad de aplicación**: Input validation, output encoding, parametrización de queries, headers de seguridad (HSTS, CSP, X-Frame-Options).
7. **Gestión de secretos**: Azure Key Vault, rotación automática, acceso mediante Managed Identities.
8. **Auditoría**: Logging de eventos de seguridad (login, acceso a datos, cambios de permisos). Retención mínima 1 año.
9. **Resiliencia**: Rate limiting, circuit breaker, anti-automation (CAPTCHA, WAF rules).
10. **Validación**: Revisar contra ENS, OWASP ASVS, NIST CSF.

---

## 📋 Reglas y Constraints

- Seguridad por defecto: todo acceso denegado salvo explícitamente permitido.
- Nunca confiar en input del usuario; validar en todas las capas.
- No almacenar contraseñas en texto plano; usar bcrypt/Argon2 con salt.
- Tokens JWT con expiración corta (< 1h) y refresh tokens rotativos.
- APIs internas también autenticadas; no asumir que 'la red es segura'.
- Datos PII anonimizados en logs y trazas.
- Dependencias de terceros escaneadas (SCA) antes de incorporar.
- Controles de seguridad no deben degradar UX de forma significativa; buscar equilibrio.
- Documentar excepciones de seguridad con justificación de riesgo aceptado.

---

## 🛠 Stack Tecnológico Relevante

- Azure Entra ID (autenticación)
- Azure Key Vault (secretos)
- Azure WAF / Front Door
- OAuth 2.0 / OpenID Connect
- .NET Identity / JWT Bearer
- OWASP ZAP / SonarQube (validación)
- Azure Policy / Defender for Cloud

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — API pública de consulta:**
> Auth: OAuth 2.0 con PKCE para SPA. Scopes: `orders:read`, `orders:write`.
> Rate limiting: 100 req/min por client_id.
> WAF: Reglas OWASP Core Rule Set, bloqueo de SQLi y XSS.
> Logging: Toda request logueada con correlation ID, sin datos PII en query params.

**Ejemplo 2 — Microservicio interno:**
> Auth: Managed Identity entre servicios. No API keys.
> Network: Private endpoint, no exposición pública.
> Data: Azure SQL TDE habilitado. Column-level encryption para datos de tarjetas.

---

## 🔗 Dependencias

- `apb-sec-threat-model-v1.0` (threat modeling)
- `apb-sec-ens-v1.0` (cumplimiento ENS)
- `apb-sec-owasp-v1.0

---

## 📝 Notas

- Security by Design no es un checkpoint único; es un proceso continuo durante todo el ciclo de vida.
- Para sistemas críticos, requerir pentest externo antes del go-live.
- Mantener un 'security champion' en cada equipo de desarrollo.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*


---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-arch-security-design-v1.0) - pendiente validacion humana. No distribuir sin revision.

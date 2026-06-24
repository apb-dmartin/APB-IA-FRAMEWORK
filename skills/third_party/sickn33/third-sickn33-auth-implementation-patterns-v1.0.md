---
id: "third-sickn33-auth-implementation-patterns-v1.0"
name: "Skill: Authentication & Authorization Patterns (antigravity-awesome-skills)"
description: "Catálogo de patrones de autenticación (JWT, sesiones, OAuth2/SSO) y autorización (RBAC, basada en permisos, ownership de recursos) con buenas prácticas de seguridad (gestión de contraseñas, rate limiting), adaptado del repositorio público sickn33/antigravity-awesome-skills."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
source_repo: "https://github.com/sickn33/antigravity-awesome-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-24"
created_date: "2026-06-24"
review_date: "2026-06-24"
---

# Skill: Authentication & Authorization Patterns (antigravity-awesome-skills)

---

## Descripción
Adaptación de la skill `auth-implementation-patterns` del repositorio
público `sickn33/antigravity-awesome-skills` (MIT para código/tooling;
contenido sin atribución externa adicional, autoría `community`). El
contenido original cubre estrategias de autenticación (JWT con refresh
tokens, sesiones, OAuth2/SSO), patrones de autorización (RBAC, basada en
permisos, ownership de recursos), y buenas prácticas de seguridad (gestión
de contraseñas, rate limiting), con ejemplos de código en
TypeScript/Express.

> **Nota de gobernanza:** identificada en la Sesión 9 dentro del agregador
> `sickn33/antigravity-awesome-skills`. Misma salvedad que las skills
> hermanas: no se instala el agregador, solo el contenido textual de esta
> skill puntual. El código de ejemplo (TypeScript/Express) requiere
> traducción conceptual a ASP.NET Core Identity/JWT antes de cualquier uso
> directo, ya cubierta en parte por `third-davila7-dotnet-backend-v1.0`.

## Capacidades
- Distinción clara entre autenticación (quién eres) y autorización (qué
  puedes hacer), con sus respectivas estrategias
- Patrones de JWT: generación, validación, y flujo de refresh token de
  vida corta/larga
- Patrón de sesiones de servidor cuando el caso de uso no requiere
  statelessness
- Integración OAuth2/OpenID Connect para SSO o login social
- RBAC, control basado en permisos, y validación de ownership de recursos
- Buenas prácticas de seguridad: hashing de contraseñas, rotación de
  secretos, rate limiting en endpoints de autenticación

## Inputs
- `tipo_sistema`: API REST, aplicación con sesión de servidor, o ambos
- `requisitos_identidad`: SSO corporativo, login propio, o federado
- `modelo_autorizacion`: roles, permisos granulares, u ownership de recurso

## Outputs
- `estrategia_auth`: estrategia de autenticación recomendada y justificada
- `patron_autorizacion`: implementación de autorización (RBAC/permisos/
  ownership) adaptada al caso
- `checklist_seguridad`: medidas de seguridad aplicables (rate limiting,
  gestión de secretos, rotación)

## Restricciones
- El código de ejemplo original (TypeScript/Express, Passport.js) no es
  directamente trasladable a .NET; debe reinterpretarse usando ASP.NET
  Core Identity, autenticación JWT Bearer nativa, o Azure AD/Entra ID
  cuando el requisito sea SSO corporativo
- **Nunca** registrar secretos, tokens o credenciales en logs — requisito
  explícito tanto del contenido original (sección "Safety") como de
  `POLICY_SECURE_DEVELOPMENT_v1.1.md` de APB
- No sustituye `apb-arch-security-design-v1.0` (Security by Design): esta
  skill aporta el catálogo de patrones de implementación, no el proceso de
  diseño de seguridad completo exigido por ENS

## Adaptaciones APB
- Cuando el requisito sea SSO corporativo, evaluar Azure AD/Entra ID como
  proveedor de identidad antes que una implementación OAuth2 ad-hoc
- Sustituir los ejemplos de hashing de contraseñas (bcrypt en Node) por el
  equivalente .NET (`Microsoft.AspNetCore.Identity.PasswordHasher` o
  similar) si la skill se invoca para generar código real
- Conectar con `apb-arch-security-design-v1.0` como skill previa de diseño,
  y con `apb-sub-qa-security-v1.0` como consumidor en revisiones de
  cumplimiento ENS

## Ejemplo de Uso
```
Invocar: third-sickn33-auth-implementation-patterns-v1.0
Input: { tipo_sistema: "API REST", requisitos_identidad: "SSO corporativo
         vía Azure AD", modelo_autorizacion: "RBAC por rol operativo" }
Output: Estrategia de autenticación (JWT Bearer + Azure AD como IdP),
        patrón de autorización RBAC, y checklist de seguridad aplicable
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada.*

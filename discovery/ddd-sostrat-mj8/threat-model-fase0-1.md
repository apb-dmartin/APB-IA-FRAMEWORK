# [IA-GEN] Threat Model (STRIDE) — Fase 0-1

> **Borrador generado por IA** (APB AI Framework - apb-sec-threat-model-v1.0) — pendiente validación humana. No distribuir sin revisión.

## 1. Alcance y Contexto

Sistemas: Datos Maestros de Equipamiento, Ferrocarril Portuario, Mano de Estiba, Depotsis (Fase 0-1 del roadmap de descomposición de SÒSTRAT). Todos publicados vía APIM, autenticación EntraID (OAuth2 client credentials), eventos vía Azure Service Bus.

**Trust boundaries identificados:**
- APIM ↔ Internet/consumidores externos.
- Servicio ↔ Azure SQL propio.
- Servicio ↔ Azure Service Bus (pub/sub entre los 15 servicios del roadmap).
- Servicio ↔ monolito SÒSTRAT legacy (durante el periodo de transición, vía CDC/ACL).
- Mano de Estiba ↔ microservicio externo "MST" (límite de confianza con un sistema no controlado directamente por este roadmap).

## 2. Amenazas STRIDE identificadas

| # | STRIDE | Amenaza | Elemento | Severidad | Control mitigador |
|---|---|---|---|---|---|
| 1 | Spoofing | Suplantación de identidad de servicio en llamadas service-to-service sin mTLS/token válido | APIM ↔ servicios | Alta | OAuth2 client credentials + EntraID ya definido en los 4 OpenAPI; confirmar que APIM valida el token en cada llamada, no solo en el borde |
| 2 | Tampering | Manipulación de payload de evento en tránsito (Service Bus) | Bus de eventos | Media | Service Bus con TLS en tránsito (por defecto en Azure); considerar firma de mensaje si el consumidor requiere garantía de integridad fuerte (no evaluado si es necesario para estos 4 servicios) |
| 3 | Tampering | Escritura directa a la BBDD del servicio saltándose la API (mismo anti-patrón que el legacy: 3.700 clases DTO con acceso directo a Oracle compartido) | Azure SQL de cada servicio | Alta | Principio de mínimo privilegio: solo el propio servicio tiene credenciales de escritura sobre su base; ningún otro servicio ni operador debe tener acceso directo — **repetir aquí el mismo error de SÒSTRAT sería la regresión de seguridad más obvia de todo el roadmap** |
| 4 | Repudiation | Falta de trazabilidad de quién creó/modificó un registro (p.ej. quién canceló una operación ferroviaria) | Todos los servicios | Media | Los 4 DTOs legacy ya tienen campos de auditoría (`idopealta`, `idopemodificacio`, `datalta`, `datmodificacio`) — mantenerlos en el modelo de datos destino, no perderlos en la migración |
| 5 | Information Disclosure | El campo `propietari` de `ContainerEquipment` (nombre de la naviera propietaria del contenedor) es dato comercialmente sensible expuesto a cualquier consumidor con scope `equipamiento.read` | Datos Maestros de Equipamiento | Media | Evaluar si se necesita un scope más granular (`equipamiento.read.basic` vs. `equipamiento.read.full`) antes de exponer `propietari` a todos los consumidores — no evaluado en el análisis DDD original |
| 6 | Information Disclosure | Reutilización de credenciales/patrones del legacy — recordatorio: se detectaron credenciales LDAP en texto plano en `applicationContext-ldap.xml` del monolito SÒSTRAT (hallazgo ya reportado por separado, ver tarea `task_4affa604`) | Legacy → nuevos servicios (durante transición) | Crítica (ya reportada) | No reutilizar ningún patrón de configuración del legacy tal cual — todos los secretos de los 4 servicios nuevos van a Azure Key Vault desde el diseño inicial, nunca en código/config plano |
| 7 | Denial of Service | Sin rate limiting definido explícitamente en ninguno de los 4 OpenAPI | APIM | Media | Definir políticas de throttling en APIM antes de producción — pendiente, no estaba en el alcance de `apb-arch-api-contract-v1.0` en esta pasada |
| 8 | Elevation of Privilege | Scope `*.write` sin distinguir operaciones destructivas (p.ej. `POST /rail-operations/{id}/cancel`) de altas normales | Ferrocarril, Depotsis | Media | Evaluar si acciones de cancelación/anulación necesitan un scope propio más restrictivo que el `write` genérico |
| 9 | Elevation of Privilege | Mano de Estiba depende de un microservicio externo ("MST") no controlado por este roadmap — superficie de confianza no auditada en este análisis | Mano de Estiba ↔ MST | Alta (sin evaluar) | Requiere threat model propio del servicio MST, coordinado con su equipo — no se puede completar este punto solo desde el lado SÒSTRAT |

## 3. Controles ya cubiertos por decisiones de arquitectura previas (no requieren acción nueva)

- Todos los servicios usan EntraID/OAuth2 (no CAS/Apereo legacy) — ya decidido en `decomposition-roadmap.md`.
- Ningún secreto en código — ya es restricción explícita de todos los `apb-arch-*`/`apb-dev-*` del framework y de `STANDARD_DEVELOPMENT.md`.
- BBDD Oracle compartida solo como estado transitorio explícito por fase, con CDC — ya decidido.

## 4. Fuera de alcance de este documento

- Los otros 11 servicios del roadmap (mismo principio incremental que specs y testing strategy).
- Threat model del portal operativo único (shell/micro-frontends) — pendiente de que se decida el mecanismo técnico de integración (ver `ui-screens-backlog.md`).
- Auditoría formal ENS/ISO 27001 — este documento es un draft STRIDE de apoyo al diseño, no sustituye una auditoría de cumplimiento (`apb-sec-risk-analysis-v1.0` es la skill correspondiente para eso).

## 5. Checklist de verificación antes de producción (Fase 0-1)

- [ ] Scopes OAuth2 revisados con Ciberseguridad APB (amenazas #1, #5, #8).
- [ ] Política de rate limiting definida en APIM para los 4 servicios (amenaza #7).
- [ ] Confirmado que ningún servicio nuevo tiene acceso de escritura a la BBDD de otro servicio (amenaza #3).
- [ ] Threat model del límite de confianza con "MST" completado con su equipo propietario (amenaza #9).
- [ ] Rotación de la credencial LDAP legacy ya en curso (tarea separada, no bloquea Fase 0-1 pero sí la Fase 4/5 de autenticación).

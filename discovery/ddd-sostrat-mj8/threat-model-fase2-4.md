# [IA-GEN] Threat Model (STRIDE) — Fases 2, 3 y 4

> **Borrador generado por IA** (APB AI Framework - apb-sec-threat-model-v1.0) — pendiente validación humana. No distribuir sin revisión.

**Alcance:** los 10 servicios de Fase 2-4, complementando `threat-model-fase0-1.md`. Mismos trust boundaries base (APIM↔Internet, servicio↔Azure SQL propio, servicio↔Service Bus, servicio↔legacy durante transición).

## Amenazas nuevas o de mayor severidad en este alcance

| # | STRIDE | Amenaza | Elemento | Severidad | Control mitigador |
|---|---|---|---|---|---|
| 10 | Tampering | Escritura directa en tablas de Título desde Facturación y Liquidaciones, repitiendo el anti-patrón legacy exacto que motivó separar estos dos servicios | Concesiones ↔ Facturación y Liquidaciones | **Crítica** | Test de contrato obligatorio en cada pipeline (ver `testing-strategy-fase2-4.md` Fase 4) + revisión de código específica en cada PR que toque este límite — es el mayor riesgo de todo el roadmap por ser la repetición literal de un problema ya conocido |
| 11 | Information Disclosure | `Factura.pdfsignat`/`pdfdupfactura` (BLOB) expuestos si se incluyen por error en el payload JSON en vez de servirse como stream binario | Facturación y Liquidaciones | Alta | Ya mitigado en `specs/openapi-facturacion-liquidaciones.yaml` (endpoint `/pdf` dedicado) — verificar en revisión de código que ningún otro endpoint serializa esos campos |
| 12 | Repudiation | Transición de estado de Liquidación (`GE→AC→FA`) sin registro de quién la ejecutó — dato financiero con implicaciones de auditoría | Facturación y Liquidaciones | Alta | Mantener campos de auditoría (`idopealta`, `idopemodificacio`) igual que en el legacy; considerar además un log de auditoría inmutable específico para transiciones de estado financiero, no solo el CRUD estándar |
| 13 | Spoofing | Integración con la naviera Grimaldi (hoy SOAP en `sostratWSCXF`, mañana consumidor de eventos) — límite de confianza con un tercero externo no controlado por APB | Aduanas/Control de Contenedores | Alta | Mantener autenticación fuerte específica para este consumidor externo (no reutilizar el token interno de servicio-a-servicio); definir un scope OAuth2 dedicado (`aduanas.grimaldi.read`) distinto del genérico |
| 14 | Denial of Service | Circuito EDI de MMPP (notificación a autoridades) sin política de reintento acotada — un fallo del sistema externo podría generar reintentos infinitos que saturen la cola | MMPP | Media | Definir un máximo de reintentos con backoff exponencial y DLQ explícita, ya reflejado en `specs/asyncapi-fase3.yaml` |
| 15 | Elevation of Privilege | `ErrorConciliacionDetectado` expone códigos de error internos (`coderror`, catálogo de ~40 constantes) que podrían revelar detalles de implementación a un consumidor no autorizado | Aduanas/Control de Contenedores | Baja | Evaluar si el catálogo completo de `coderror` debe ser público vía API o solo un subconjunto de cara a consumidores externos |
| 16 | Tampering | Los estados con nombres no confirmados (`ResidusEscala.idestat` 2-7, `OperacioPif.idestatoperaciopif`) podrían implementarse con semántica incorrecta si no se valida con negocio antes de codificar la máquina de estados | MARPOL, PIF | Media | No codificar transiciones de estado hasta confirmar los nombres reales — riesgo de seguridad indirecto: una máquina de estados mal definida puede permitir transiciones de negocio inválidas (p.ej. "pagado" → "recibido") |

## Consideración específica: Aguada

El servicio de Aguada (`specs/openapi-aguada.yaml`) está marcado como provisional — **no tiene threat model real todavía**, porque no se puede modelar la superficie de ataque de un contrato que no está grounded en el DTO transaccional real. Cualquier amenaza identificada aquí sería especulativa. Bloqueado por el mismo gap de evidencia que bloquea el resto de artefactos de este servicio.

## Checklist de verificación antes de producción (Fase 2-4)

- [ ] Test de contrato "Facturación y Liquidaciones nunca escribe en tablas de Título" ejecutándose en CI, no solo documentado (amenaza #10).
- [ ] Scope OAuth2 dedicado para la integración con Grimaldi revisado con Ciberseguridad APB (amenaza #13).
- [ ] Política de reintento/DLQ del circuito EDI de MMPP definida y probada (amenaza #14).
- [ ] Nombres reales de los estados de MARPOL (2-7) y PIF confirmados con negocio antes de implementar la máquina de estados (amenaza #16).
- [ ] Decisión sobre exposición del catálogo `coderror` a consumidores externos (amenaza #15).
- [ ] Threat model de Aguada re-hecho por completo una vez se recupere el DTO fuente real — el actual no es válido, es un placeholder.

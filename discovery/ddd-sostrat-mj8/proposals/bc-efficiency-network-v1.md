---
id: "bc-efficiency-network-v1"
name: "Efficiency Network (Business Club)"
description: |
  Programa de certificaciones/auditorías de sostenibilidad para empresas
  adheridas al "Business Club" del puerto. Descubierto en la auditoría de
  cobertura 2026-07-13 como EPIC-22 (bloqueada, "sin dominio de encaje").
  **Corrección 2026-07-13 (misma sesión, verificación adicional)**: sí tiene
  encaje real — `EmpresaBC.java` extiende `Usuari.java` (herencia real de
  clase, no solo relación FK), es decir, es una **especialización de
  Operadores Portuarios** para empresas adheridas al programa, no un dominio
  aislado. El campo `Usuari.eseffnetwork` (columna `ESEFFNETWORK`) ya marca
  la adhesión al programa desde el propio maestro de terceros.
status: "discovered"
parent_domain: "dom-operaciones-maritimas-v1 (tentativo — mismo bloqueante que bc-operadores-portuarios-v1, del que este BC depende directamente)"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "EmpresaBC"
entities:
  - "BCCertificacions"
  - "BCAuditoriaUsuari"
  - "TipusAuditoriaBC"
  - "TipusConeixementBC"
value_objects: []
domain_events:
  - "EmpresaEfficiencyNetworkRegistrada"
  - "CertificacionBCRegistrada"
  - "AuditoriaBCRegistrada"
ubiquitous_language:
  - term: "Empresa BC"
    definition: "Empresa adherida al Business Club/Efficiency Network — especialización de Usuari (Operador Portuario), no una entidad de negocio independiente."
  - term: "Certificació BC"
    definition: "Certificación de sostenibilidad/calidad asociada a una empresa BC, tabla BC_CERTIFICACIONS."
integration_patterns:
  - pattern: "conformist"
    with_context: "bc-operadores-portuarios-v1"
    direction: "downstream"
upstream_contexts:
  - "bc-operadores-portuarios-v1"
downstream_contexts: []
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-13"
approved_date: null
source: "auditoria-cobertura-2026-07-13 (corrección tras verificación adicional solicitada por el usuario)"
notes: "CORRECCIÓN: la clasificación original en jira-backlog.md EPIC-22 decía 'no encaja en ningún dominio del catálogo real, ninguno de los revisados (corporativo, administracion-electronica, medio-ambiente-marpol) encajaba'. Es incorrecta — no se había verificado la relación de herencia EmpresaBC extends Usuari. El bloqueante real no es 'sin dominio', es el MISMO bloqueante que bc-operadores-portuarios-v1 (parent_domain tentativo, pendiente de confirmación de Arquitectura APB) — este BC hereda esa dependencia. 18 rutas Struts confirmadas por conteo exacto (grep sobre struts-config.xml): TipusConeixementAction, TipusAuditoriaAction, EmpresaENAction, AuditoriaENAction, ConeixementENAction, ContacteENAction, ImportarAuditoriaENAction, ImportarCertificatENAction, ImportarConeixementENAction, CertificatENAction, AuditoriesEmpresaNewAction (x3 paths), CertificatsEmpresaNewAction (x2 paths), ConeixementsEmpresaNewAction (x3 paths)."
---

# Efficiency Network (Business Club)

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura, corrección 2026-07-13) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Gestiona el programa "Business Club / Efficiency Network": empresas adheridas (especialización de Operadores Portuarios), sus certificaciones de sostenibilidad/calidad, auditorías y "coneixements" (formaciones) asociadas a contactos de esas empresas, con importación masiva desde fichero.

## Lo que NO incluye

No es un maestro de terceros independiente — `EmpresaBC extends Usuari` (herencia Java real, confirmada leyendo `dataaccess/dto/efficiencynetwork/EmpresaBC.java:8`). Cualquier empresa BC es también, por definición, un Operador Portuario. No modelar esto como agregado raíz propio sin relación con `bc-operadores-portuarios-v1` sería un error de diseño.

## Modelo de Dominio

`EmpresaBC` (extiende `Usuari`, tabla `USUARI` + campos propios): `raosocialbc`, `codibc`, `codiactivitatbc`, `anybc`, `visitesport`, `newsletters`, direcciones propias del programa (`nomcarrerbc`, `codpostalbc`, `poblaciobc`...), `codildap`.

`BCCertificacions` (tabla `BC_CERTIFICACIONS`): `idusuari` (FK a Usuari/EmpresaBC), `idtipactivitat`, `seqbccertificat`, `datainici`, `datafi`, `datafivalidesa`, `codicertif` (ticket SOSBRAN-14), `datacertif`.

`BCAuditoriaUsuari` (tabla no confirmada campo a campo en esta pasada — pendiente).

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| EmpresaEfficiencyNetworkRegistrada | emitido | Alta de una empresa en el programa (marca `Usuari.eseffnetwork=true`). |
| CertificacionBCRegistrada | emitido | Nueva certificación asociada a una empresa BC. |
| AuditoriaBCRegistrada | emitido | Nueva auditoría asociada a una empresa BC. |

## Relaciones con Otros Bounded Contexts

**Downstream directo de `bc-operadores-portuarios-v1`** — no es una relación opcional, es herencia de dato real. Comparte su mismo bloqueante de `parent_domain`.

## Implementación Actual

`mvc/control/efficiencyNetwork/` (12 clases: `EmpresaENAction`, `AuditoriaENAction`, `CertificatENAction`, `ConeixementENAction`, `ContacteENAction`, `ImportarAuditoriaENAction`, `ImportarCertificatENAction`, `ImportarConeixementENAction`, `TipusAuditoriaAction`, `TipusConeixementAction`, `AuditoriesEmpresaNewAction`, `CertificatsEmpresaNewAction`, `ConeixementsEmpresaNewAction`), `service/efficiencyNetwork/` (5 interfaces + 5 impl), `dataaccess/dto/efficiencynetwork/` (13 clases). **18 rutas Struts confirmadas** (conteo exacto: `grep -oP` sobre `struts-config.xml`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework (corrección auditoría de cobertura) | Propuesta inicial — corrige la clasificación previa de EPIC-22 ("sin dominio de encaje"); descubierta la herencia EmpresaBC extends Usuari, que ata este BC a bc-operadores-portuarios-v1 |

---
id: "bc-operadores-portuarios-v1"
name: "Operadores Portuarios / Terceros (Usuari)"
description: |
  Maestro de negocio de "operadores portuarios" (consignatarios, armadores,
  agentes de aduanas, terceros facturables): identificación fiscal (NIF/EORI/CNAE),
  direcciones, facturación electrónica, bonificaciones y asignación a servicios
  marítimos. Descubierto en la auditoría de cobertura 2026-07-13. NO debe
  confundirse con la capa IAM técnica de login/roles (Operador/Rol), que vive
  fuera de este repositorio y ya está cubierta por dom-transversal-arq-v1/EntraID.
status: "discovered"
parent_domain: "dom-operaciones-maritimas-v1"
owner_team: "equipo-sostrat"
reviewer: "Arquitectura APB"
aggregates:
  - "Usuari"
entities:
  - "UsuariAudit"
  - "UsuariCares"
  - "UsuariCircuitEdi"
  - "UsuariCircuitBustia"
  - "UsuariDocument"
value_objects: []
domain_events:
  - "OperadorPortuarioRegistrado"
  - "OperadorPortuarioActualizado"
ubiquitous_language:
  - term: "Usuari"
    definition: "Entidad de negocio de un tercero (consignatario, armador, agente de aduanas) con identificación fiscal, NO una cuenta de login."
  - term: "EORI"
    definition: "Economic Operators Registration and Identification — código de operador económico aduanero de la UE, campo real del maestro."
  - term: "Efficiency Network (ESEFFNETWORK)"
    definition: "Campo booleano en el maestro de Usuari que marca adhesión al programa Efficiency Network (ver bc pendiente de decisión)."
integration_patterns:
  - pattern: "open-host-service"
    with_context: "bc-escalas-v1"
    direction: "upstream"
  - pattern: "open-host-service"
    with_context: "bc-liquidacion-v1"
    direction: "upstream"
upstream_contexts: []
downstream_contexts:
  - "bc-escalas-v1"
  - "bc-liquidacion-v1"
  - "bc-facturacion-v1"
related_systems:
  - "SOSTRAT-Sostrat-MJ8"
tech_stack:
  - ".NET"
  - "Azure SQL"
proposed_date: "2026-07-13"
approved_date: null
source: "auditoria-cobertura-2026-07-13"
notes: "IMPORTANTE — dos capas distintas conviven bajo nombres parecidos: 'Operador'/'Rol' (paquete org.apb.sostrat.core.mvc.control, clases NO presentes en este repo, IAM técnico de login/roles) vs 'Usuari' (paquete raíz org.apb.sostrat.mvc.control, SÍ presente, master data de negocio). Solo la segunda se modela aquí. Parent_domain tentativo: dom-operaciones-maritimas-v1 por el uso más frecuente (asignación de consignatario/armador a ServeiMaritimVaixell), pero es consumido también por Liquidación/Facturación (sujeto facturado, ver InfoUsuarioLiquidacionDTO.java) — mismo patrón de dato maestro cross-domain que bc-datos-maestros-equipamiento-v1. Confirmar con Arquitectura APB si merece dominio propio ('Terceros'/'Operadores Económicos') en vez de colgar de Operaciones Marítimas. Tabla real: USUARI (60+ campos, sin ningún campo de credencial/password — confirmado por lectura completa del DTO)."
---

# Operadores Portuarios / Terceros (Usuari)

> **Borrador generado por IA** (APB AI Framework — auditoría de cobertura) — pendiente validación humana. No distribuir sin revisión.

## Responsabilidad

Mantiene el maestro de "terceros" del negocio portuario: consignatarios, armadores, agentes de aduanas y cualquier operador económico facturable. Gestiona identificación fiscal, direcciones, publicación web, facturación electrónica (FACe) y bonificaciones de tasas.

## Lo que NO incluye

**No es la capa de autenticación/login.** La gestión de credenciales, sesiones y roles de aplicación (`Operador`/`Rol`, `/operador.do*`, `/rol.do*`) vive en un paquete framework separado no incluido en este checkout — se cubre en el modelo destino por `dom-transversal-arq-v1`/EntraID, sin necesidad de migrar lógica (confirmado: cero campos de credencial en el DTO `Usuari`, e intercept-urls de Spring Security separados entre `/operador.do*`/`/rol.do*` y `/usuari.do*`).

## Modelo de Dominio

Agregado `Usuari` (tabla `USUARI`) — campos reales confirmados: `IDUSUARI` (PK), `TIPPERSONA`, `NOM`, `COGNOM1/2`, `NIF`, `EORI`, `CNAE`, `CODIAGENT`, `IDGRUEMPRESARIAL`, direcciones fiscal/notificación/física completas, `LLISTA_NEGRA`, `COMPTEFACE`, `NOMWEB`/`URLWEB`/`LOGOWEB`, `ESEFFNETWORK`, `DATALTA`/`DATBAIXA`.

### Eventos de Dominio

| Evento | Tipo | Descripción |
|--------|------|-------------|
| OperadorPortuarioRegistrado | emitido | Alta de un nuevo tercero/operador. |
| OperadorPortuarioActualizado | emitido | Modificación de datos fiscales/facturación. |

## Relaciones con Otros Bounded Contexts

- **Escalas**: asignación de consignatario/armador responsable a un servicio marítimo concreto (`ServeiMaritimVaixellUsuari`, `VaixellUsuariBonificacio` — bonificaciones de tarifa por armador/buque).
- **Liquidación/Facturación**: el `Usuari` es el sujeto facturado (`InfoUsuarioLiquidacionDTO.java` extrae NIF/dirección/idioma del maestro).
- **EDI**: asignación de terceros a circuitos/bandejas de mensajería (`UsuariCircuitEDIAction`).

## Implementación Actual

`mvc/control/UsuariAction.java` (+ `UsuariAuditAction`, `UsuariCircuitEDIAction`, `UsuariDependentAction`), `service/CN_Usuari.java`/`_Impl`, `dataaccess/dto/Usuari.java` (tabla `USUARI`).

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---------|-------|-------|--------|
| 1.0.0 | 2026-07-13 | APB AI Framework (auditoría de cobertura) | Propuesta inicial — bounded context descubierto en auditoría de cobertura; parent_domain tentativo, pendiente de confirmación por ser dato maestro cross-domain |

---
id: "ddd-interview-questions-apim-v1.0"
name: "Entrevista DDD — preguntas para validar dominios candidatos"
description: >-
  Guion de entrevista (apb-sub-ddd-interview-v1.0) para que Arquitectura APB
  (Débora) resuelva los solapamientos y APIs sin clasificar antes de generar
  los dom-*.md. Fase 3 — checkpoint humano del protocolo apb-agent-ddd-v1.0.
type: "reference"
source: "apb-sub-ddd-interview-v1.0 (ejecutor: Claude)"
last_updated: "2026-06-30"
status: "draft — esperando respuestas de Débora"
---

# Entrevista DDD — preguntas abiertas

## A. Solapamientos a resolver
1. **Escalas**: ¿`ESC-Escalas` (4 APIs) es el nuevo ecosistema DOCKS que reemplaza
   ARGOS, o convive con él? ¿`CRE-Cruceros` es un dominio aparte (solo cruceros) o
   un subdominio de Operaciones Marítimas?
2. **Inspección**: ¿`INS-Escaner` y `PIF-PuntoInspeccionFisica` son el mismo
   dominio (inspección de mercancías) o contextos separados?
3. **Firma**: ¿`FEL` (firma interna) + `SIG` (Viafirma) + `FLU` (circuitos/flujos)
   son 1 dominio "Firma y Aprobaciones" o varios?
4. **Facturación**: ¿`P33` + `P51` + `REB` + `RCF` son 1 dominio "Facturación
   Portuaria" o tienen reglas de negocio distintas que justifiquen separarlos?
5. **Energía**: ¿`MDE-MuelleDeEnergia` (inflamables/energéticos) y `OPS`
   (electricidad a buques) son el mismo dominio energético o separados?
6. **Vehículos/Terrestre**: ¿`FER` (ferrocarril), `TRU` (camiones), `PVI` (puertas),
   `EQV` (daños vehículos) forman un dominio "Transporte Terrestre", o FER es propio?

## B. Equipo SOSTRAT (66 APIs)
7. ¿Cómo se reparten las 66 APIs de SOSTRAT entre los dominios de negocio reales?
   ¿Hay plan de crear apps propias por dominio (como CTA, CRE, EQV)?

## C. APIs sin función conocida
8. ¿Qué son? `ROSS`, `GPC`, `DGS`, `ESF`, `ESM`, `FLO`, `IPB`, `MPA`, `MST`,
   `RESPONSIBLE`. ¿`MIGRACION` es temporal?

## D. Validación de clasificación estratégica
9. ¿Confirmas core/supporting/generic del `discovery-summary.md`? En particular:
   ¿Facturación es *supporting* o *core* para APB?

## Respuestas (Débora, 2026-06-30)

1. **Escalas**: ESC NO reemplaza ARGOS — **conviven con solapamiento claro**. Tanto
   ARGOS como SOSTRAT (Java) necesitan las escalas. Debería ser **dominio propio
   independiente** en el futuro. Aquí = **escalas marítimas**. **Cruceros (CRE) es
   dominio propio ahora** (abierto si en el futuro es subdominio de Marítimas).
2. **Inspección**: no resuelto → se deja como un único dominio candidato con la duda.
3. **Firma**: **varios** (no es 1 solo). Se modela dentro de Transversal/ARQ como
   varios contextos (firma interna, integración Viafirma, circuitos de firma).
4. **Facturación**: **debería ser el mismo** dominio (hoy fragmentado en 4 apps).
5. **Energía**: no resuelto → un único dominio candidato con la duda.
6. **Terrestre**: no resuelto → un único dominio candidato (FER quizá propio).
7. **SOSTRAT**: es el **monolito Java** que se va a **dividir y transformar a DOCKS**.
   No es un dominio — es un sistema legacy que alimenta varios dominios
   (`related_systems`). Alimenta la futura Fase 1 (descomposición de monolitos).
8. **APIs desconocidas** (ROSS, GPC, DGS, ESF, ESM, FLO, IPB, MPA, MST, RESPONSIBLE):
   son **casi todas capas de integración contra productos de mercado** → dominio
   genérico "Integraciones con productos de mercado" (ACL), cada una pendiente de
   identificar el producto concreto.
9. **Transversal / ARQ**: concepto APB propio = elementos que mantiene el equipo de
   Arquitectura, transversales a nivel **técnico** pero **no de negocio** (login,
   gestor documental, mail…). Se modela como dominio genérico/técnico (shared kernel).

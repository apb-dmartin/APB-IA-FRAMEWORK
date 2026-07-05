---
id: "prov-azure-qa-runtime-v1.0"
name: "Provider: Azure QA Runtime"
description: "Proveedor de acción para ejecutar pruebas (Playwright + k6) en un entorno efímero de la suscripción QA de Azure, con las herramientas pre-instaladas y credenciales por Managed Identity → Azure Key Vault. Permite ejecución completa sin que el usuario ni el runner instalen nada. Agnóstico de implementación (Azure Container Apps job, Container Instances, Azure Load Testing, Microsoft Playwright Testing como referencias)."
version: "1.0.0"
status: "draft"
owner: "QA Gobierno APB <qa-gobierno@portdebarcelona.cat>"
domain: "platform"
provider_type: "action"
access_mode: "read-write"
created_date: "2026-07-03"
review_date: "2026-07-03"
depends_on:
  - "prov-akv-v1.0"  # Credenciales y storageState por referencia (Managed Identity), nunca en fichero
---

# Provider: Azure QA Runtime

> **Complementa a [`prov-playwright-v1.0`](prov-playwright-v1.0.md) y [`prov-k6-v1.0`](prov-k6-v1.0.md).**
> Ellos definen *cómo* se ejecutan las pruebas; este provider define *dónde* cuando la respuesta es
> "en la suscripción QA de Azure, sin que nadie instale nada localmente" (destino `azure-qa`,
> [`TEST_PLAN_STANDARD §9.1/§9.4`](../context/apb/standards/TEST_PLAN_STANDARD.md)).
>
> **Estado `draft` (diseño):** el **contrato** está definido; el **despliegue real** de la infraestructura
> (job, red, identidades) es trabajo de la sesión **QA-3**. No hay recursos Azure aprovisionados todavía.

---

## Descripción

Levanta un **entorno de ejecución efímero** en la **suscripción QA de Azure** con Playwright y k6
**pre-instalados**, ejecuta el subconjunto de pruebas indicado contra PRE/QA, recoge las evidencias y se
destruye. Resuelve el requisito de **"pruebas completas sin que el usuario ni el workflow instalen nada"**:
ni el portátil del usuario ni el runner de CI necesitan Node/Playwright/k6; todo vive en la imagen del job.

Las **credenciales** (usuario de ejecución por rol, `storageState`) se resuelven por **Managed Identity →
Azure Key Vault** (`prov-akv-v1.0`), nunca se pasan en claro ni se persisten en el repo.

## Capacidades

- Provisionar un job efímero con navegadores + k6 pre-instalados (imagen reproducible).
- Resolver credenciales y `storageState` por referencia AKV vía Managed Identity (sin secretos en claro).
- Ejecutar suites Playwright (funcional/E2E/API) y escenarios k6 (rendimiento/carga) contra PRE/QA.
- Aislar red al entorno QA/PRE autorizado; sin acceso a producción salvo autorización explícita.
- Recoger evidencias (screenshots, trazas, vídeo, informes HTML/JUnit) y exportarlas a un destino
  (paquete descargable y/o Jira).
- Destruir el entorno al terminar (efímero, sin coste residual).

## Configuración

```json
{
  "provider_id": "prov-azure-qa-runtime-v1.0",
  "type": "action",
  "endpoint": "azure-qa://job-runner",
  "implementation": "azure-container-apps-job | azure-container-instances | azure-load-testing | ms-playwright-testing",
  "subscription": "APB-QA (ref, no id en claro)",
  "identity": "managed-identity",
  "secrets": "AKV://<vault>/<secret>",
  "tools_preinstalled": ["node", "playwright", "k6"],
  "network_scope": ["pre", "qa"],
  "evidence": { "screenshots": true, "trace": true, "video": true, "reports": ["html", "junit"] }
}
```

## Inputs

- `test_suite`: referencia a las pruebas a ejecutar (Playwright specs / escenarios k6).
- `target_env`: `pre` | `qa` (nunca `prod` sin autorización explícita).
- `role`: rol de usuario con el que ejecutar (resuelve el secreto AKV del usuario de ese rol).
- `evidence_destination`: `zip` | `jira` | `ambos`.
- `constraints` (opcional): límites de red, timeouts, cuota de carga para k6.

## Outputs

- `results`: resultado por prueba (pass/fail) con su ID canónico (`{APP}-B{NN}-T{NN}`).
- `evidence_package`: screenshots + trazas + vídeo + informes (HTML/JUnit).
- `performance_summary`: métricas k6 (p95, error rate) para la no-regresión (`TEST_PLAN_STANDARD §8`).
- `run_metadata`: entorno, identidad usada (referencia, no secreto), duración, coste estimado.

## Dependencias

- `prov-akv-v1.0` (credenciales y `storageState` por referencia — Managed Identity).
- `prov-playwright-v1.0` / `prov-k6-v1.0` (definición de las pruebas que se ejecutan aquí).
- `apb-qa-test-plan-v1.0` (declara el destino `azure-qa`).
- `apb-sub-qa-fix-loop-v1.0` (si hay fallos, propone PR + anota Jira).

## Implementaciones de referencia (no dependencia dura)

| Implementación | Uso típico | Nota |
|---|---|---|
| **Azure Container Apps job** | Job efímero con imagen Playwright+k6 | Escala a cero; ideal para regresión bajo demanda |
| **Azure Container Instances** | Ejecución puntual contenedorizada | Alternativa simple sin plataforma de contenedores |
| **Azure Load Testing** | Carga k6 gestionada a escala | Para rendimiento/estrés más allá de un solo nodo |
| **Microsoft Playwright Testing** | Ejecución Playwright gestionada, paralela | Navegadores en la nube, sin instalar local |

> El componente que consume este provider **no codifica** una implementación concreta: selecciona la
> disponible en la suscripción QA. Cambiar de implementación no cambia el contrato (agnóstico).

## Restricciones

- **`draft`:** contrato definido; sin infraestructura aprovisionada (despliegue = QA-3).
- **Nunca ejecuta en producción** sin autorización explícita; ámbito por defecto PRE/QA.
- **Credenciales nunca en claro ni persistidas**: solo Managed Identity → AKV por referencia
  (`AGENTS.md §3`, `GOVERNANCE.md §5.2`).
- Las evidencias pueden contener datos sensibles → tratar como evidencia controlada (no publicar).
- Autonomy Level 1: la ejecución es asistida; el humano autoriza la carga/escaneo y valida los resultados
  (acta de aprobación, `TEST_PLAN_STANDARD §6.2`).

## Ejemplo de Uso

```
Invocar: prov-azure-qa-runtime-v1.0
Input: { test_suite: "ref:tru/e2e", target_env: "pre", role: "USER_READ_TRUCK_CENTER", evidence_destination: "ambos" }
Output: results[] (por ID canónico) + evidence_package + performance_summary + run_metadata
```

---
*Registrado en APB AI Framework. Requiere revisión humana antes de aprobación.*

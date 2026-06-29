---
id: "apb-sec-supply-chain-v1.0"
name: "Seguridad de Cadena de Suministro — SBOM y Dependencias"
description: "Analiza la cadena de suministro de software APB: genera y evalúa SBOM (Software Bill of Materials), revisa licencias de código abierto, detecta dependencias transitivas con vulnerabilidades conocidas (CVE) y verifica la integridad de artefactos de terceros."
version: "1.0.0"
status: "draft"
owner: "Seguridad APB <seguridad@portdebarcelona.cat>"
domain: "security"
autonomy_level: 1
created_date: "2026-06-29"
review_date: "2026-12-29"
---

# Seguridad de Cadena de Suministro — SBOM y Dependencias

## Propósito
Garantizar que el software de terceros incorporado en los sistemas APB no introduce vulnerabilidades, restricciones legales ni dependencias de proveedores no evaluados. La cadena de suministro de software es un vector de ataque creciente (ej. Log4Shell, XZ Utils): este skill sistematiza la evaluación de dependencias directas y transitivas, la generación de SBOM y la verificación de licencias compatibles con el uso en administración pública.

## Contexto de Uso
- Incorporación de una nueva librería o dependencia a un proyecto APB.
- Auditoría periódica de dependencias de un servicio en producción.
- Evaluación pre-release: verificar que ninguna dependencia tiene CVE crítico sin parche.
- Cumplimiento de requisitos ENS: trazabilidad de componentes de software de terceros.
- Detección de cambios sospechosos en dependencias tras un incidente de seguridad.

## Entradas Requeridas

| Entrada | Tipo | Descripción | Obligatorio |
|---|---|---|---|
| `service_name` | Texto | Nombre del servicio o aplicación | ✅ |
| `dependency_manifest` | Fichero | `package.json`, `*.csproj`, `pom.xml`, `requirements.txt`, `go.mod` | ✅ |
| `lock_file` | Fichero | `package-lock.json`, `packages.lock.json`, etc. (para dependencias transitivas) | ❌ |
| `existing_sbom` | JSON (CycloneDX/SPDX) | SBOM existente para comparación incremental | ❌ |
| `license_policy` | Lista | Licencias bloqueadas en APB: por defecto AGPL, SSPL, Commons Clause | ❌ |

## Flujo de Trabajo

1. **Generación del SBOM**:
   - Parsear el manifiesto de dependencias y el lock file para extraer todas las dependencias: directas y transitivas.
   - Generar SBOM en formato CycloneDX (JSON) con: nombre, versión, PURL, licencia declarada, hash de integridad.
   - Si existe SBOM anterior: generar diff — nuevas dependencias, dependencias eliminadas, versiones cambiadas.

2. **Evaluación de vulnerabilidades (CVE)**:
   - Consultar la lista de CVE conocidos para cada componente: NVD, OSV (osv.dev), GitHub Advisory Database.
   - Clasificar por severidad CVSS: Critical (≥9.0), High (7.0-8.9), Medium (4.0-6.9), Low (<4.0).
   - Para cada CVE Critical/High: determinar si existe versión parcheada disponible y si hay exploit público conocido.
   - Verificar dependencias transitivas: un paquete sin CVE puede depender de uno vulnerable.

3. **Revisión de licencias**:
   - Mapear licencia SPDX de cada componente.
   - Aplicar política APB:
     - **Permitidas sin restricción**: MIT, Apache 2.0, BSD 2/3-Clause, ISC, MPL 2.0.
     - **Requieren evaluación legal**: LGPL (si se modifica la librería), EPL, EUPL.
     - **Bloqueadas en APB**: AGPL, SSPL, Commons Clause, licencias propietarias sin contrato.
   - Identificar dependencias sin licencia declarada → riesgo legal, requieren investigación manual.

4. **Análisis de integridad**:
   - Verificar que los hashes de las dependencias en el lock file coinciden con los publicados en el registro (npm, NuGet, PyPI, Maven Central).
   - Detectar dependencias instaladas desde fuentes no oficiales (git branches, URLs directas, registros privados no declarados).
   - Identificar paquetes con nombre similar a populares (typosquatting): ej. `lodahs` vs `lodash`.

5. **Evaluación de riesgo de proveedor**:
   - Identificar dependencias con un único mantenedor activo (bus factor = 1) y sin actividad en >12 meses.
   - Detectar paquetes con alta popularidad repentina o cambios de mantenedor recientes (indicadores de compromiso).

6. **⚠️ CHECKPOINT HUMANO**: Las licencias bloqueadas y los CVE Critical requieren decisión humana antes de bloquear el build o iniciar proceso de sustitución de dependencia.

## Salida Esperada

```markdown
# Informe SBOM y Cadena de Suministro — [Servicio] — [Fecha]
> ⚠️ Borrador generado por IA (APB AI Framework - apb-sec-supply-chain-v1.0) — pendiente validación humana. No distribuir sin revisión.

## Resumen
| Total dependencias | Directas | Transitivas | CVE Critical | CVE High | Licencias bloqueadas | Sin licencia |

## CVE Críticos y Altos

| Paquete | Versión | CVE | CVSS | Descripción | Parche disponible | Exploit público |
|---|---|---|---|---|---|---|

## Problemas de Licencias
| Paquete | Licencia | Tipo problema | Acción recomendada |
|---|---|---|---|

## Dependencias sin Licencia
| Paquete | Versión | Fuente | Acción |

## Problemas de Integridad
| Paquete | Problema detectado | Gravedad |

## Riesgos de Proveedor
| Paquete | Mantenedores activos | Último commit | Riesgo |

## SBOM Completo (CycloneDX)
[adjunto como apb-[servicio]-sbom-[fecha].json]

## Comparativa con SBOM anterior (si aplica)
| Cambio | Paquete | Versión anterior | Versión nueva |
```

## Criterios de Calidad
- [ ] El SBOM incluye dependencias directas Y transitivas.
- [ ] Todos los CVE Critical tienen indicado si existe parche y si hay exploit público.
- [ ] Ninguna dependencia con licencia bloqueada APB en el inventario sin justificación.
- [ ] Los hashes del lock file han sido verificados contra los registros oficiales.
- [ ] El SBOM generado es exportable en formato CycloneDX o SPDX.
- [ ] Las dependencias sin licencia están marcadas para investigación legal.

## Stack y Tecnologías
- Generación SBOM: `syft` (Anchore), `cdxgen`, Microsoft SBOM Tool
- CVE lookup: NVD API, osv.dev, GitHub Advisory Database, `grype` (Anchore)
- Formatos SBOM: CycloneDX 1.5 (preferido APB), SPDX 2.3
- Lenguajes: .NET/NuGet, Java/Maven, Python/pip, Node.js/npm, Go modules

## Dependencias
- `apb-sec-patch-management-v1.0` — los CVE detectados se gestionan como parches priorizados
- `apb-sec-sast-v1.0` — el SBOM complementa el análisis estático de código propio

## Ejemplo de Uso

```
Analiza las dependencias del servicio APB-API-Contenedores.
Adjunto el package-lock.json (Node.js 20).
Necesito el SBOM, la lista de CVE activos y la verificación de licencias
para incluir en el informe de auditoría ENS de este trimestre.
```

## Notas y Advertencias
- **Nivel 1**: Las decisiones sobre licencias bloqueadas y sustitución de dependencias críticas requieren revisión humana.
- Los análisis de cadena de suministro deben ejecutarse en cada release, no solo en auditorías puntuales.
- El lock file es obligatorio para análisis completo de transitivas: sin lock file, el análisis es parcial.
- En dependencias con CVE Critical sin parche: evaluar mitigación temporal (WAF rule, feature flag) mientras se espera el parche upstream.
- Nunca instalar dependencias desde branches de git o URLs directas sin proceso de aprobación de seguridad.

## Historial de Cambios

| Versión | Fecha | Autor | Cambio |
|---|---|---|---|
| 1.0.0 | 2026-06-29 | Seguridad APB / Claude Code | Creación inicial — Sesión Enriquecimiento B, Bloque 2 |

## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| *(Sin inputs declarados)* | No aplica | No |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** — callout inmediatamente tras el título H1:
  > **Borrador generado por IA** (APB AI Framework - apb-sec-supply-chain-v1.0) — pendiente validación humana. No distribuir sin revisión.

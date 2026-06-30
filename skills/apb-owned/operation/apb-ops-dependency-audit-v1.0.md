---
id: "apb-ops-dependency-audit-v1.0"
name: "Auditoría de Dependencias y Vulnerabilidades"
description: "Escanea un repositorio APB para detectar dependencias obsoletas, vulnerabilidades conocidas en librerías/paquetes, y versiones de runtime desactualizadas, generando un informe priorizado por severidad."
version: "1.0.0"
status: "draft"
owner: "Plataforma APB <arquitectura@portdebarcelona.cat>"
domain: "operation"
autonomy_level: 1
created_date: "2026-06-24"
review_date: "2026-06-24"
depends_on:
  - "prov-apb-knowledge-v1.0"  # Contexto corporativo APB

---

# Auditoría de Dependencias y Vulnerabilidades


## Contexto Corporativo APB

> Antes de ejecutar esta skill/agente, carga
> `context/apb/knowledge/APB_KNOWLEDGE_BASE.md` (provider: `prov-apb-knowledge-v1.0`).
> Úsalo para entender el dominio portuario, la terminología (CA/ES/EN) y los
> sistemas implicados. El legacy documentado (SÒSTRAT/Java/Oracle/CAS/Alfresco)
> es contexto informacional, **no prescripción tecnológica**.
> Stack aprobado: `context/apb/standards/STANDARD_ARCHITECTURE.md`

---

## 🎯 Propósito

Escanea un repositorio APB (.NET/C#, Django/Python, JavaScript/DevExtreme) para detectar
dependencias obsoletas, vulnerabilidades conocidas (CVE) en librerías y paquetes, y versiones
de runtime/SDK desactualizadas respecto al estándar corporativo vigente.

---

## ⚡ Trigger

Análisis periódico programado (ej. mensual) o bajo demanda al iniciar
`apb-agent-tech-debt-v1.0`, especialmente antes de una sesión de remediación de deuda
técnica o como parte de auditoría previa a una licitación/entrega.

---

## 📥 Input

- Ruta al repositorio o lista de repositorios a auditar
- Manifiestos de dependencias: `.csproj`/`packages.lock.json` (.NET), `requirements.txt`/
  `poetry.lock` (Django), `package.json`/`package-lock.json` (JavaScript/DevExtreme)
- Estándar de versiones vigente (`STANDARD_DEVELOPMENT.md`: .NET 8, versiones soportadas)

---

## 📤 Output

- Lista de dependencias obsoletas (versión actual vs. última estable vs. mínima soportada)
- Lista de vulnerabilidades conocidas con severidad (Critical/High/Medium/Low) y CVE asociado
- Lista de versiones de runtime/SDK desactualizadas
- Clasificación por riesgo de actualización (breaking change probable vs. parche seguro)

---

## 🔄 Proceso

1. **Inventario de dependencias**: leer manifiestos del/los repositorio(s) objetivo.
2. **Comparación de versiones**: contrastar contra registro oficial (NuGet, PyPI, npm) y
   contra el estándar corporativo (`STANDARD_DEVELOPMENT.md`).
3. **Cruce con bases de vulnerabilidades conocidas**: identificar CVEs activos en las
   versiones detectadas.
4. **Clasificación de riesgo de actualización**: para cada dependencia obsoleta, estimar si
   la actualización es un parche seguro (mismo major) o probable breaking change (cambio de
   major version).
5. **Priorización**: Critical/High con CVE activo primero; luego obsolescencia sin CVE
   conocido pero con soporte próximo a finalizar (EOL).

---

## 📋 Reglas y Constraints

- No aplica ninguna actualización automáticamente — esta skill es de diagnóstico, no de
  remediación (la remediación la decide `apb-ops-debt-remediation-plan-v1.0` con aprobación
  humana).
- Vulnerabilidades Critical/High se reportan siempre, aunque la actualización implique
  breaking change — la decisión de cuándo actualizar es humana, no se omite el hallazgo.
- No se asume que "sin CVE conocido" equivale a "seguro" — se reporta igualmente la
  obsolescencia de versión como hallazgo de menor severidad.

---

## 🛠 Stack Tecnológico Relevante

- NuGet (`dotnet list package --vulnerable --outdated`) para .NET
- `pip-audit` / `safety` para Django/Python
- `npm audit` para JavaScript/DevExtreme
- `STANDARD_DEVELOPMENT.md` como referencia de versiones soportadas APB

---

## 💡 Ejemplos de Uso

**Ejemplo — Auditoría de un microservicio .NET:**
> Input: repositorio `APB.Pricing.Api`
> Hallazgo: `Newtonsoft.Json 12.0.1` → CVE-2024-XXXX (High), actualización a `13.0.3` es
> parche seguro (sin breaking change detectado en changelog).
> Hallazgo: `.NET 6` runtime, EOL noviembre 2024 → migración a `.NET 8` requerida, breaking
> change probable (revisar `apb-dev-impact-analysis-v1.0` antes de actualizar).

---

## 🔗 Dependencias

- `STANDARD_DEVELOPMENT.md` — referencia de versiones soportadas
- Consumida por: `apb-agent-tech-debt-v1.0`

---

## 📝 Notas

- Nivel 1: genera el informe, no ejecuta ninguna actualización.
- Las vulnerabilidades de paquetes de terceros usados en `skills/third_party/` del propio
  framework (no del código que produce APB) están fuera de alcance de esta skill — eso lo
  cubre el proceso de `GOVERNANCE.md` §4 (Componentes de Terceros).

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

> **Generado por IA:** Claude (Anthropic), Sesión 11 del plan de remediación APB-IA-FRAMEWORK.
> **Validado por humano:** _pendiente — completar nombre/rol del validador antes de pasar a `candidate`._


## ⚠️ Comportamiento ante inputs incompletos

> El agente **nunca** debe continuar con inputs obligatorios vacíos o contradictorios sin comunicarlo explícitamente.

| Input | Si falta o es ambiguo | Bloquea ejecución |
|-------|-----------------------|-------------------|
| `Ruta al repositorio o lista de repositorios a auditar` | Pregunta: "¿Puedes proporcionar ruta al repositorio o lista de repositorios a auditar?" | Sí |
| `Manifiestos de dependencias` | Pregunta: "¿Puedes proporcionar manifiestos de dependencias?" | Sí |
| `Estándar de versiones vigente` | Pregunta: "¿Puedes proporcionar estándar de versiones vigente?" | Sí |

---

## Marcado IA obligatorio (POLICY_AI_USAGE §6)

Conforme al [`AI_MARKING_STANDARD`](../../../context/apb/standards/AI_MARKING_STANDARD.md), todo artefacto generado por esta skill debe incluir marca de origen IA:

- **Documentos Markdown** - callout inmediatamente tras el titulo H1:
  > **Borrador generado por IA** (APB AI Framework - apb-ops-dependency-audit-v1.0) - pendiente validacion humana. No distribuir sin revision.

---
id: "apb-qa-pipeline-v1.0"
name: "Validación QA en Pipeline de Despliegue"
description: "Evalúa la calidad y completitud de un pipeline de despliegue (CI/CD) APB antes de promover un artefacto a producción. Verifica que los gates de calidad, seguridad, cobertura de tests y aprobaciones humanas están correctamente configurados y ejecutados."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "qa"
autonomy_level: 2
created_date: "2026-06-26"
review_date: "2026-06-26"
---

# Validación QA en Pipeline de Despliegue

---

## 🎯 Propósito

Revisar la configuración y los resultados de ejecución de un pipeline CI/CD APB e identificar gaps o incumplimientos antes de que un artefacto llegue a producción. Actúa como gate de calidad automatizado que complementa (no sustituye) la aprobación humana obligatoria en el paso de promoción a producción.

---

## ⚡ Trigger

Cuando un equipo APB solicita revisión del pipeline antes de un despliegue a producción, o cuando un pipeline falla y se necesita diagnóstico, o cuando se crea un nuevo pipeline y se quiere validar que cumple los estándares APB.

---

## 📥 Input

- Fichero de definición del pipeline (GitHub Actions YAML, Azure DevOps YAML, Jenkinsfile)
- Resultados de la última ejecución (logs, métricas de cobertura, resultados de tests)
- Informe de análisis de seguridad (SAST/DAST) si existe
- Entorno destino (desarrollo / preproducción / producción)
- Tipo de artefacto (aplicación web, microservicio, script BD, infra como código)

---

## 📤 Output

- **Semáforo de calidad:** 🟢 Apto / 🟡 Apto con advertencias / 🔴 No apto para producción
- **Checklist de gates:** estado de cada gate obligatorio APB
- **Hallazgos:** gaps o incumplimientos con severidad y propuesta de corrección
- **Pipeline mejorado:** versión corregida del YAML si hay gaps técnicos
- **Resumen ejecutivo:** para el responsable de aprobación humana

---

## 🔄 Proceso

1. **Verificación de gates obligatorios APB:**

| Gate | Descripción | Obligatorio en |
|------|-------------|----------------|
| Tests unitarios | Cobertura ≥70% | Todos los entornos |
| Tests de integración | Suite de regresión ejecutada | Pre-producción y producción |
| Análisis SAST | Sin vulnerabilidades Critical/High sin mitigar | Producción |
| Análisis de dependencias | Sin CVE críticos sin parchear | Producción |
| Revisión de código | Mínimo 1 aprobación en PR | Todos los entornos |
| Aprobación humana explícita | Gate manual antes de producción | Producción obligatorio |
| Build reproducible | Artefacto firmado o hasheado | Producción |
| Rollback probado | Plan de rollback documentado y testado | Producción |
| Variables de entorno | Sin secretos hardcodeados en el YAML | Todos los entornos |
| Notificación de despliegue | Registro en Jira + notificación al equipo | Producción |

2. **Análisis del fichero de pipeline:**
   - Detectar steps faltantes o comentados
   - Identificar secretos o credenciales en texto plano (tokens, passwords, connection strings)
   - Verificar que los entornos están correctamente separados (no reutilizar credenciales dev en prod)
   - Comprobar que el gate de aprobación humana está antes del despliegue a producción

3. **Análisis de resultados de ejecución:**
   - Cobertura de tests vs. umbral APB
   - Tests fallidos o saltados sin justificación
   - Warnings de seguridad no tratados
   - Tiempo de ejecución (pipelines >30 min necesitan optimización)

4. **Generación del semáforo y checklist**

5. **Propuesta de correcciones** con fragmentos YAML listos para incorporar

---

## 📋 Reglas y Constraints

- Un semáforo 🔴 impide el despliegue a producción — el equipo debe resolver los gaps antes de continuar
- La aprobación humana antes de producción es NO negociable — ningún pipeline puede omitirla
- Los secretos detectados en texto plano en el YAML son hallazgo Crítico — bloquean el despliegue
- La skill no ejecuta el pipeline — solo revisa y asesora
- Los umbrales de cobertura (70%) son los mínimos APB; cada equipo puede definir umbrales más altos

---

## 🛠 Stack Tecnológico Relevante

- GitHub Actions (`.github/workflows/*.yml`)
- Azure DevOps Pipelines (`azure-pipelines.yml`)
- Jenkins (Jenkinsfile declarativo/scripted)
- SonarQube / SonarCloud (SAST)
- OWASP Dependency-Check (CVE en dependencias)
- Trivy (vulnerabilidades en contenedores)
- Azure Key Vault / GitHub Secrets (gestión de credenciales)

---

## 💡 Ejemplos de Uso

**Ejemplo — Pipeline con gap crítico:**
> Pipeline GitHub Actions revisado: tiene tests unitarios (cobertura 82%), análisis SAST, pero el step de despliegue a producción no tiene gate de aprobación humana y hay una API key hardcodeada en el YAML.

Semáforo: 🔴 No apto  
Hallazgos:
- **Crítico:** API key en texto plano en línea 47 (`API_KEY: "sk-..."`) — mover a GitHub Secrets
- **Crítico:** Ausencia de gate de aprobación humana antes del step `deploy-production`

Pipeline corregido: incluye `environment: production` con required reviewers y `${{ secrets.API_KEY }}`.

---

## 🔗 Dependencias

- `apb-qa-framework-v1.0` — QA del propio framework APB AI
- `apb-plat-cicd-v1.0` — skill de configuración de pipelines CI/CD

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

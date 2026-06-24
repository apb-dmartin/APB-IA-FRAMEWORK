# Estándar de QA APB

> **ID:** `apb-std-qa-v1.0`
> **Versión:** 1.0.0
> **Estado:** draft

---

## 🎯 Principios

1. Calidad como responsabilidad compartida
2. **Clean as you code**
3. Trazabilidad completa (Jenkins, SonarQube, Jira)
4. Excepciones formalizadas

## 🏷️ Modalidades

| Aspecto | Compliance | Legacy |
|---------|-----------|--------|
| Definición | Código nuevo | Código previo a política |
| PRE/PRO | Bloqueante | Informativo + Jira |
| Deuda técnica | No permitida | No incrementar |

## 🔍 Validaciones Técnicas

- Endpoints protegidos con `[Authorize]`
- Azure Entra ID (token TGT en deprecación)
- NO SOAP/WebServices
- Últimas 2 versiones de plantillas
- Documentación mínima: 10 entregables

## 📈 Métricas

| Entorno | Compliance | Legacy |
|---------|-----------|--------|
| TST | Informativo | Informativo |
| PRE | Bloqueante | Informativo + Jira |
| PRO | Bloqueante | Informativo + Jira |

---
*Resumen ejecutivo. Documento fuente en `context/apb/policies/quality/POLICY_QA_v1.0.md`*

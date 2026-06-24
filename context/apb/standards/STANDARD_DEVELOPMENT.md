# Estándar de Desarrollo APB

> **ID:** `apb-std-development-v1.0`
> **Versión:** 1.0.0
> **Estado:** draft

---

## 🎯 Principios

1. Código limpio: SOLID, Clean Code
2. **NO try/catch genéricos** (framework Docks captura errores inesperados)
3. Revisión humana obligatoria para código asistido por IA
4. Marcado obligatorio de uso de IA

## 💻 Stack

### Backend
- .NET (C#), ASP.NET Core, EF Core
- Django/GeoDjango (solo geoespacial)
- Inyección de dependencias obligatoria

### Frontend
- **DevExtreme JavaScript puro** (NO React, NO TypeScript salvo excepción)
- WCAG 2.1 AA mínimo

### APIs
- REST exclusivo
- OpenAPI/Swagger

## 🔒 Seguridad

- **NO secretos en código** → Azure Key Vault + App Configuration
- Dependabot habilitado
- Análisis estático obligatorio

## 📊 Quality Gates (SonarQube)

| Métrica | Compliance |
|---------|-----------|
| Blocker Issues | 0 |
| Cobertura | ≥ 60% |
| Duplicados | < 3% |
| Maintainability | ≥ B |
| Reliability | ≥ C |
| Security | ≥ C |
| Hotspots | 0 |

---
*Resumen ejecutivo. Documento fuente en `context/apb/policies/quality/POLICY_QA_v1.0.md`*

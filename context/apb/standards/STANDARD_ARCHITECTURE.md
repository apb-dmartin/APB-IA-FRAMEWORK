# Estándar de Arquitectura APB

> **ID:** `apb-std-architecture-v1.0`
> **Versión:** 1.1.0
> **Estado:** draft

---

## 🎯 Principios

1. **Security by Design** desde fases iniciales
2. **Proporcionalidad al riesgo**
3. **Separación de entornos** (dev/test/prod)
4. **Trazabilidad** completa

## 🏗️ Patrones

### Microservicios
- DDD para descomposición
- Comunicación asíncrona preferente
- Azure Service Bus (JSON + CloudEvents, NO Avro/Protobuf)

### APIs
- REST homologado (NO SOAP/WSDL)
- Azure Entra ID para autenticación
- Autorización: App Roles de Entra ID asignados a grupos (`GRP_{ENTORNO}_{APP}_{ROL}`), no permisos directos a usuario. Catálogo de roles estándar y modelo completo en `APB_KNOWLEDGE_BASE.md` §3.4
- HTTPS/TLS obligatorio
- Rate limiting

### Event-Driven
- Azure Service Bus: broker corporativo
- JSON + CloudEvents
- Idempotencia en consumidores
- Outbox pattern
- Dead letter queues con retry exponencial

## ☁️ Cloud
- Terraform (IaC)
- Azure principal
- FinOps para costes

---
*Resumen ejecutivo. Documentos fuente en `context/apb/policies/security/` y `context/apb/policies/infrastructure/`*

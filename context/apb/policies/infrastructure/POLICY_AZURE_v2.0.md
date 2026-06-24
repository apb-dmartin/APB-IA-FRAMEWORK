# Politicas_Azure_v2(1)

Objetivo

El objetivo principal de este documento es proporcionar una guía estructurada sobre la aplicación de políticas y etiquetas en Azure, ayudando a la organización a reforzar la gobernanza, la seguridad, la eficiencia operativa y la gestión de entornos en Cloud. A través de recomendaciones y buenas prácticas, se pretende facilitar la implantación de controles que aseguren el cumplimiento normativo y la alineación con los objetivos técnicos y empresariales.

En el contexto de APB, disponer de una política específica para el uso de políticas y etiquetas en Azure permite establecer un marco común que garantice la correcta administración de los recursos en Cloud. Esta política contribuye a definir procedimientos claros, asignar responsabilidades y promover la coherencia en la gestión, asegurando que todos los equipos y proyectos adopten estándares homogéneos en cuanto a seguridad, clasificación de datos, control de costes y cumplimiento regulatorio.

La gobernanza permite establecer reglas claras sobre cómo se deben desplegar, configurar y administrar los recursos, garantizando el cumplimiento normativo y la eficiencia operativa en todos los entornos (desarrollo, preproducción, producción).

Este documento define principios, alcance, modelo de gobierno, taxonomía de tags, catálogo de políticas, procesos de excepción, operación y métricas, así como la integración con Terraform (Policy-as-Code) y Ansible como plataforma de orquestación. Objetivo: estandarizar el uso de Azure Policy y etiquetas para garantizar cumplimiento (ENS), visibilidad de costes y reducción del riesgo operativo.

Definición general

Azure Policy 

Es un servicio de Azure que permite crear, asignar y gestionar reglas para asegurar que los recursos de la nube cumplen con los estándares y requisitos definidos por la organización. Se utiliza para aplicar restricciones, validar configuraciones y automatizar el cumplimiento normativo y de seguridad en los recursos desplegados dentro de Azure, ayudando así a mantener la coherencia y el control en todos los entornos.

Etiquetas en Azure

Las etiquetas son pares clave-valor que se asignan a recursos de Azure para facilitar su organización, clasificación y seguimiento. No imponen reglas ni restricciones, pero son fundamentales para:

Organización lógica: Agrupar recursos por proyecto, departamento, entorno, etc.

Gestión de costes: Permiten segmentar gastos por etiquetas como CostCenter o Proyecto.

Visibilidad y trazabilidad: Ayudan a identificar rápidamente la función o propietario de un recurso.

Automatización: Pueden usarse en scripts o herramientas para aplicar acciones según el valor de la etiqueta.

Ejemplo: Etiquetar una base de datos con Entorno=Producción y Proyecto=Argos permite saber a qué aplicación pertenece y en qué entorno.

Políticas en Azure (Azure Policy)

Las políticas son reglas que definen y aplican requisitos técnicos o normativos sobre los recursos de Azure. A diferencia de las etiquetas, las políticas sí imponen restricciones y pueden:

Validar configuraciones: Impedir la creación de recursos que no cumplan ciertos criterios.

Aplicar correcciones automáticas: Por ejemplo, añadir etiquetas faltantes o configurar propiedades.

Auditar el cumplimiento: Generar informes sobre qué recursos cumplen o no con las políticas.

Aplicarse a distintos niveles: Desde grupos de administración hasta recursos individuales.

Efectos

Los efectos (effects) en Azure Policy definen qué acción realiza la política cuando evalúa un recurso. Definen si la política simplemente notifica, bloquea la creación del recurso o lo modifica para cumplir con los estándares de gobernanza. Estos efectos actúan de forma preventiva o correctiva.

Efectos posibles: Audit, Deny, DeployIfNotExists, Modify, AuditIfNotExists.

Ejemplo: Una política puede exigir que todos los recursos tipo contenedor de la suscripción de TST estén configurados para que se apaguen automáticamente fuera del horario laboral, y si no la tienen, modificarlo automáticamente usando el efecto Modify. 

Relación entre etiquetas y políticas

Las políticas pueden gestionar etiquetas. Es decir, puedes usar Azure Policy para:

Requerir etiquetas específicas.

Añadir etiquetas automáticamente si faltan.

Bloquear la creación de recursos sin etiquetas (efecto Deny).

Corregir recursos existentes para que cumplan con las etiquetas requeridas (efecto Modify).

Las políticas pueden agruparse en iniciativas para facilitar su gestión y seguimiento desde el panel de cumplimiento de Azure Policy

Además, las etiquetas pueden gestionarse de forma centralizada y agrupada para facilitar la administración y seguimiento desde el panel de cumplimiento de Azure Policy, permitiendo mantener una trazabilidad clara y coherente en todo el entorno.

Las buenas prácticas en la gestión de políticas y etiquetas en Azure incluyen:

Definir políticas claras: Utilizar Azure Policy para establecer reglas que automaticen el cumplimiento de estándares de seguridad, cumplimiento y operativos, como el uso obligatorio de TLS, aplicación de HTTPS o la protección de datos con Key Vault.

Aplicar políticas en varios niveles: Asignar políticas a nivel de grupo de administración, suscripción y grupo de recursos para garantizar coherencia y control granular según las necesidades del entorno.

Usar iniciativas: Agrupar políticas relacionadas en iniciativas para facilitar su gestión y realizar un seguimiento centralizado desde el panel de cumplimiento de Azure Policy.

Etiquetar recursos de forma coherente: Implementar etiquetas obligatorias como DataClassification, CostCenter y BusinessUnit para mejorar la trazabilidad, el control financiero y la gestión de inventario de recursos.

Revisar y actualizar políticas periódicamente: Adaptar las políticas según evolucionen los requisitos de la organización y el entorno de Azure.

Monitorizar el cumplimiento: Utilizar las herramientas de cumplimiento de Azure para identificar y remediar desviaciones respecto a las políticas establecidas.

Estas políticas y etiquetas ayudan a:

Cerrar huecos en seguridad y cumplimiento (TLS, HTTPS, Key Vault, Private Endpoints).

Fortalecer la trazabilidad y control financiero (DataClassification, CostCenter, BusinessUnit).

Optimizar la operación continua (alertas, budgets, lifecycle).

Consolidar el modelo DevSecOps, alineando infraestructura con prácticas de CI/CD seguras.

En resumen, una gobernanza efectiva en Azure basada en políticas y etiquetas ayuda a evitar brechas de seguridad, garantizar el cumplimiento normativo, optimizar costes y mantener la coherencia operativa entre los diferentes entornos de la organización.

Referencias

Azure Policy – DeployIfNotExists y remediaciones: Microsoft Learn

Azure Monitor – Diagnostic settings con políticas built-in

CAF – Estrategia de tagging

Defender for Cloud – iniciativas/benchmark

Azure Policy Exemptions – estructura y CLI

Terraform azurerm – policy_definition/assignment

Ansible – community.general.terraform y azure.azcollection

Decisiones de gobernanza 

A continuación, se definen las prácticas básicas que se implementarán para la gobernanza de políticas y etiquetas en APB.

Control y cumplimiento

Definir un comité de políticas Azure formado por Ciberseguridad, Redes, Operaciones y Arquitectura.

Definir un responsable de cada categoría de políticas o etiquetas.

Identificar los equipos responsables de cada política según las categorías definidas

Definir el responsable de la implantación, mantenimiento y supervisión de la aplicación de las políticas y etiquetas.

Establecer equipos para la implantación, mantenimiento y supervisión de la aplicación de las políticas y etiquetas.

Establecer un proceso de revisión y aprobación para la creación de nuevas etiquetas y políticas, evitando duplicidad o proliferación innecesaria.

Evitar etiquetas redundantes y mantener la lista corporativa centralizada.

Implementar controles de acceso basados en roles (RBAC) para limitar quién puede crear, modificar o eliminar etiquetas y políticas, reforzando así la seguridad.

Integrar revisiones de cumplimiento de etiquetas y políticas en los ciclos de auditoría interna. 

Revisión trimestral de necesidades de nuevas políticas o etiquetas.

Revisar trimestralmente la coherencia entre etiquetas, CMDB y costes reales.

Revisión mensual de cumplimiento de políticas o etiquetas, y realizando las acciones necesarias para su corrección.

Reporting trimestral de cumplimiento a comité SSI.

Automatización y herramientas

Automatizar la aplicación de etiquetas desde plantillas Terraform.

Usar políticas de Azure Policy tipo Modify o AuditIfNotExists para exigir o heredar etiquetas.

Configurar alertas automáticas para detectar recursos sin etiquetar o con etiquetas incorrectas, permitiendo una respuesta rápida ante desviaciones.

Crear dashboards de cumplimiento de políticas y etiquetado en el portal Azure o Power BI.

Documentación y formación

Documentar claramente el estándar de nomenclatura y el propósito de cada etiqueta para asegurar una aplicación homogénea en toda la organización.

Actualizar y versionar la documentación de políticas y etiquetas cuando haya cambios, asegurando su disponibilidad y consulta en un repositorio centralizado.

Realizar sesiones de formación periódicas para los equipos técnicos y de gestión, fomentando el uso correcto de políticas y etiquetas.

Publicar las políticas en APB a los miembros de SSI o proveedores externos si aplica.

Alcance, metas y principios

Alcance:

Plan de control aplicable a Management Groups (MG), todas las suscriciones suscripciones y recursos (Core, Preproducción, Producción).

Políticas fundacionales, de seguridad/red/datos/operaciones/costes y estándares de tagging.

Excepciones, remediación, reporting y automatización.

Iniciativas por dominio: Seguridad Base, Datos, Operaciones, Coste.

Metas:

100% de recursos con tags obligatorios y valores válidos.

100% de cumplimiento en controles críticos (seguridad/diagnósticos/datos).

Tiempo medio de Remediación (MTTR) de remediación por política < 7 días. 

Trazabilidad de excepciones y expiración automática.

Principios:

“Secure by default” y mínimo privilegio.

Fases Audit → Modify/DeployIfNotExists → Deny.

Automatización de despliegues, remediación y reporting.

Versionado y pruebas de definiciones (policy-as-code).

RACI (roles clave)

Gobierno/Seguridad: define catálogo de políticas, taxonomía de tags, controles y excepciones (R/A).

Equipo de Plataforma: implementa policy-as-code, pipelines y remediación (R).

Equipos de Aplicación: etiquetado, ownership y corrección de no conformidades (R).

Finanzas/Control de Gestión: define esquema de costes/tags (C).

Auditoría/Compliance: revisa evidencias y excepciones (C/I).

Matriz por categorías de políticas:

Seguridad y Cumplimiento

Seguridad y Cumplimiento

Gobernanza y organización

Monitorización y auditoría

FinsOps

Matriz por responsables de políticas. La siguiente matriz RACI define las responsabilidades de los distintos equipos en relación con la definición, cumplimiento, supervisión y gestión de excepciones de las Políticas IT. 

R = Responsible (ejecuta) 

A = Accountable (responsable último / decisión) 

C = Consulted (consultado) 

I = Informed (informado)

Matriz para implementación

Taxonomía de etiquetas

Se etiquetará en inglés y todo en minúsculas. Adicionalmente existe un documento donde se detalla la lista de etiquetas a aplicar en Azure con más información de cada una, a modo de resumen se enumeran aquí. 

Tags obligatorios

Tags para ciertos recursos

Tags complementarios no obligatorios

Propuestas de etiquetas a completar

Adicionalmente existe un documento donde se detalla la lista de etiquetas a aplicar en Azure. Las etiquetas están organizadas por tags, con descripciones, nivel de aplicación y responsables. 

Efectos

Se aplicarán los siguientes efectos de Azure Policy a modo general, la lista efecto/política final será definida en el proyecto de implementación.

Ejemplo práctico, política que exige etiquetado de recursos:

Buenas prácticas a tener en cuenta:

Deny en Prod tras fase Audit/Modify y comunicación previa.

Audit/AuditIfNotExists para medir impacto inicial.

Append/Modify para correcciones ligeras (tags y flags).

DeployIfNotExists para diagnósticos/agents: requiere identidad administrada y roles mínimos en la asignación.

Estrategia de implementación

La estrategia para aplicar las políticas para minimizar un impacto negativo en la organización será por fases:

Ejemplos de aplicación por faseado

Cumplimiento ENS (trazabilidad y controles)

Registro y trazabilidad: Activity Log + Resource Logs en Log Analytics (retención 180–365 días según ENS).

Gobierno técnico: restricciones de ubicación/SKUs/tipos; deny en Prod; excepciones con caducidad.

Seguridad: TLS/HTTPS only, endpoints privados, Key Vault protegido; Defender for Cloud como marco continuo.

KPIs y reporting

% recursos conformes por iniciativa/MG.

% de recursos con tags obligatorios (global y por clave).

Cobertura de diagnostic settings.

Excepciones activas y a <30 días.

MTTR de remediaciones.

Lista de políticas y etiquetas

Adicionalmente existe un documento donde se detalla la lista de políticas a aplicar en Azure. Las políticas están organizadas por categoría, con descripciones claras y el efecto que producen al aplicarse. 

Recomendaciones de Efecto por Categoría de Política

Anexo1 - Propuesta de nomenclatura

. Estructura general recomendada

apb-<app/proyecto>-<tiporecurso>-<entorno>-<región>-<número+opcional>

Decidir si suscripción en alguna posición, guiones o no y en cuales, minúsculas y en inglés
 

Significado de los bloques

2. Abreviaturas de región (recomendadas)

Revisar nombre oficial 

3. Abreviaturas de tipos de recursos

4. Ejemplos de nombres por tipo de recurso

Resource Group à apb-mps-rg-pro-es
App Service à apb-mps-app-pre-es
 Storage Account à apbmpsstproes01
 Key Vault à apb-mps-kv-pro-fr (ojo ya definidas actualmente, no hace falta cambio)
 Virtual Network à apb-hub-vnet-pro-es
 Subred à apb-hub-snet-firewall-pro-es
 Public IP à apb-portal-pip-dev-es-01
 

5. Ejemplo completo de arquitectura usando el estándar APB

Proyecto: MPS

Entorno: producción
Región: España

# Requerimientos técnicos para desarrollos a medida con arquitectura Docks v2.0

| Versión | Fecha | Descripción | Persona |
|---------|-------|-------------|---------|
| 1 | Mayo 2022 | Documento inicial. Aprobado por Ciberseguridad y Arquitectura | Débora Martin, Manuel Villalonga, Cristian Medrano, Sergi Fernández |
| 2 | Febrero 2026 | Actualización por tecnología. Se elimina la sección de seguridad por existir un anexo independiente. Aprobado por Arquitectura | Débora Martin, Manuel Villalonga |

## 1. Introducción

El presente anexo establece los estándares técnicos obligatorios aplicables a todos los desarrollos, evolutivos, correctivos, integraciones y transformaciones de aplicaciones cuando se ejecuten sobre la arquitectura corporativa Docks de APB.

Su finalidad es garantizar la coherencia técnica, la reutilización de componentes, la mantenibilidad, la seguridad, la observabilidad, la calidad del software y la correcta integración con el ecosistema tecnológico de APB.

Este anexo se aplicará a todos los equipos y perfiles que intervengan en los servicios y/o proyectos de desarrollo, incluyendo análisis funcional, análisis técnico, desarrollo, pruebas, despliegue, seguridad, datos, documentación y traspaso a mantenimiento.

Las aplicaciones incluidas en el alcance deberán cumplir estos estándares desde la fase de diseño hasta la puesta en producción y el periodo de soporte o garantía que resulte aplicable.

## 2. Principios generales

Todos los análisis y desarrollos deberán alinearse con los principios de la arquitectura corporativa de APB Docks. Los principios mínimos exigibles serán los siguientes:

- Desacoplamiento entre componentes y servicios.
- Orientación a eventos y/o servicios, evitando dependencias rígidas.
- Reutilización de capacidades y componentes comunes.
- Diseño escalable, mantenible y trazable.
- Preparación para despliegue en entornos cloud y contenedorizados.
- Separación clara entre presentación, lógica de negocio y acceso a datos.
- Evolución progresiva y segura desde los sistemas legacy hacia el entorno objetivo.

No se admitirán soluciones que consoliden nuevos acoplamientos innecesarios, que dificulten la operación futura o que contradigan los estándares de arquitectura aprobados por APB.

## 3. Metodología

La ejecución se realizará mediante metodologías ágiles, colaborativas e iterativas, alineadas con los principios de mejora continua, entrega incremental de valor y adaptación al cambio.

Las soluciones deberán desarrollarse mediante iteraciones cortas, con refinamiento, especificación, desarrollo, validación, automatización, despliegue y recogida de feedback.

La metodología deberá integrarse con DDD, DevOps, DevSecOps, SRE y Spec Driven Development, y garantizar trazabilidad entre requisitos, especificaciones, desarrollos, pruebas y despliegues.

## 4. Análisis

El adjudicatario deberá realizar, con carácter previo al diseño y desarrollo, el análisis funcional y/o técnico necesario para delimitar correctamente el alcance, las dependencias, los dominios afectados y el impacto sobre los sistemas existentes.

Dicho análisis deberá alinearse con la arquitectura Docks y con el modelo tecnológico de APB, basado en principios de Domain-Driven Design, arquitecturas orientadas a eventos, microservicios, cloud, DevOps y DevSecOps.

El análisis deberá documentarse de forma suficiente y someterse a validación por parte de APB y de los equipos que esta designe, especialmente en materia de arquitectura, ciberseguridad, calidad y negocio.

### 4.1. Análisis funcional

El análisis funcional deberá orientar la solución hacia modelos distribuidos, desacoplados y organizados por dominios de negocio. Como mínimo, incluirá las siguientes actividades:

- Captura, análisis, refinamiento y priorización de requisitos funcionales y no funcionales.
- Modelado funcional basado en Domain-Driven Design, incluyendo dominios, subdominios, bounded contexts, capacidades de negocio, entidades relevantes y eventos de dominio.
- Definición de procesos funcionales orientados a eventos y con bajo acoplamiento.
- Elaboración de historias de usuario, casos de uso, criterios de aceptación y especificaciones funcionales.
- Definición de contratos funcionales entre servicios, sistemas y actores implicados.
- Participación en enfoques de Spec Driven Development, garantizando que las especificaciones sean completas, verificables y trazables.
- Definición funcional de APIs, eventos, flujos de integración y contratos de intercambio de información.
- Coordinación con arquitectura y equipos técnicos para asegurar la coherencia entre necesidad funcional y solución técnica.
- Participación en validaciones funcionales, definición de pruebas de aceptación y verificación de la calidad funcional de la solución.
- Uso de herramientas de modelado, documentación colaborativa y gestión de requisitos, cuando proceda.

### 4.2. Análisis técnico

El análisis técnico deberá definir soluciones distribuidas cloud-native, escalables, seguras y alineadas con la arquitectura corporativa. Como mínimo, incluirá las siguientes actividades:

- Diseño de soluciones basadas en microservicios, contenedores y plataformas cloud.
- Definición de arquitecturas orientadas a eventos, mensajería asíncrona y modelos de publicación-suscripción.
- Aplicación de principios de Domain-Driven Design en el diseño técnico de servicios, componentes y dominios.
- Diseño de APIs REST, APIs event-driven y contratos de integración.
- Definición y mantenimiento de especificaciones técnicas versionadas y contract-first, cuando resulte aplicable.
- Establecimiento de estándares de integración, versionado, trazabilidad y gobierno de APIs y eventos.
- Diseño de soluciones resilientes, observables, mantenibles y seguras.
- Definición de estrategias de logging, monitorización, trazabilidad distribuida y observabilidad.
- Integración de prácticas DevOps y DevSecOps en el ciclo de desarrollo y despliegue.
- Conocimiento y aplicación de pipelines CI/CD, automatización de validaciones, análisis estático, control de calidad y automatización de pruebas.
- Definición de mecanismos de autenticación, autorización, gestión de secretos, hardening y seguridad en entornos cloud-native.
- Elaboración de documentación técnica de arquitectura, diagramas de integración, modelos de despliegue y especificaciones técnicas.

### 4.3. Dominios e integraciones

La identificación y definición de dominios funcionales y técnicos deberá diferenciar, como mínimo, entre dominios propios de la solución y dominios externos pertenecientes a otros procesos, sistemas, aplicaciones o plataformas integradas.

El adjudicatario deberá analizar las dependencias entre dominios, identificar eventos de negocio, definir contratos de integración y garantizar una delimitación clara de responsabilidades entre servicios, componentes y sistemas.

## 5. Infraestructura y plataforma cloud

Los servicios críticos de infraestructura deberán consumirse preferentemente en modalidad PaaS sobre la plataforma cloud corporativa, salvo excepción justificada y aprobada por APB.

Entre otros, se incluyen: Bases de datos, Servicios de mensajería, Bus de integración, Colas y sistemas de eventos, Almacenamiento, Servicios de monitorización y Observabilidad, Componentes de integración y automatización.

Cada entorno dispondrá de suscripciones y recursos segregados, garantizando el aislamiento, la trazabilidad y el cumplimiento de las políticas corporativas de seguridad y gobierno.

La infraestructura base será proporcionada por la APB, incluyendo redes, identidades, backup, control de acceso y servicios transversales. Los equipos adjudicatarios deberán diseñar las soluciones teniendo en cuenta esta realidad y usando configuración desacoplada, despliegues automatizados, gestión segura de secretos y compatibilidad con los mecanismos corporativos de observabilidad.

## 6. Arquitectura Docks

Las soluciones deberán diseñarse, analizarse, desarrollarse y desplegarse conforme a los principios de arquitectura definidos por la APB, basados en modelos cloud-native, arquitecturas desacopladas, orientación a dominios y automatización integral del ciclo de vida software.

### 6.1. Principios generales de arquitectura de desarrollo

Las soluciones deberán:

- Diseñarse bajo principios Cloud Native.
- Seguir modelos desacoplados basados en microservicios, DDD y Event-Driven Architecture.
- Favorecer bajo acoplamiento, alta cohesión, escalabilidad horizontal y resiliencia.
- Aplicar criterios API First y Spec Driven Development.
- Garantizar observabilidad, trazabilidad y monitorización extremo a extremo.
- Integrar DevOps y DevSecOps desde fases tempranas.
- Cumplir los estándares corporativos de seguridad, gobierno y protección de la información.
- Disponer y ejecutar con resultado exitoso de pruebas completas.

### 6.2. Estándares tecnológicos

Con carácter general, las soluciones deberán alinearse con los siguientes estándares tecnológicos definidos por la APB:

| Ámbito | Tecnología / estándar |
|--------|----------------------|
| Backend principal | .NET y C#. |
| Frontend corporativo | DevExpress / DevExtreme, con JavaScript o Blazor según el sistema de diseño. |
| APIs y servicios web | .NET para APIs REST y backend general; Django, Django REST Framework y GeoDjango para servicios GIS o geoespaciales. |
| Bases de datos | Azure SQL Database como persistencia relacional principal; Cosmos DB cuando esté técnicamente justificado; PostgreSQL/PostGIS para capacidades geoespaciales. |
| Mensajería e integración | Azure Service Bus y tecnologías corporativas definidas por Arquitectura. |

Cualquier incorporación de librerías, frameworks o componentes no previstos requerirá validación previa del equipo de Arquitectura.

### 6.3. Desarrollo y construcción

El desarrollo deberá realizarse utilizando exclusivamente los entornos, plantillas, repositorios, estándares y componentes autorizados por APB.

De forma general, los desarrollos deberán ajustarse a los siguientes criterios:

- Utilizar la plantilla corporativa Docks o la que APB determine en cada momento.
- Seguir las convenciones de nomenclatura, estructura de solución, ramas, paquetes y artefactos definidas por APB.
- Evitar el uso de librerías, frameworks o componentes no autorizados.
- Documentar adecuadamente el código, los módulos y las decisiones técnicas relevantes.
- Mantener un diseño limpio, mantenible y alineado con los principios de calidad y reutilización.
- Cuando exista una alternativa funcional viable, deberá priorizarse la reutilización de capacidades ya existentes frente a la creación de nuevos desarrollos redundantes.
- Coordinar posibles componentes transversales con Arquitectura.

### 6.4. Servicios, APIs y contratos de integración

Las APIs deberán incorporar mecanismos normalizados de autenticación, autorización, versionado, control de errores y trazabilidad. Los contratos deberán mantenerse versionados y alineados con Spec Driven Development.

### 6.5. Integración entre aplicaciones

Las integraciones entre aplicaciones deberán realizarse preferentemente mediante mecanismos desacoplados y estándares corporativos aprobados por APB.

Con carácter general, se utilizarán los siguientes mecanismos, según proceda:

- Mensajería asíncrona basada en eventos.
- Integraciones síncronas mediante API REST.

No se admitirán, salvo autorización expresa y justificada de APB, integraciones basadas en acceso directo a bases de datos, DBLinks, intercambio manual de ficheros no controlados, SOAP u otros mecanismos no alineados con la política tecnológica definida.

Toda integración deberá quedar documentada, versionada y trazada, incluyendo contrato de intercambio, dependencias, responsables y mecanismos de monitorización.

### 6.6. Integración con plataformas externas

Las integraciones con SaaS, PaaS o productos de mercado deberán alinearse con los principios de APB, garantizando seguridad, trazabilidad, aislamiento, reintentos y monitorización.

En estos casos, los equipos adjudicatarios deberán garantizar:

- Compatibilidad con los estándares corporativos de integración.
- Seguridad y trazabilidad de las comunicaciones.
- Aislamiento adecuado entre dominios.
- Gestión controlada de errores y reintentos.
- Monitorización de extremo a extremo.

Podrán darse, entre otros, los siguientes escenarios:

**Eventos originados en plataformas externas:** Cuando el origen de los eventos o flujos de integración corresponda a plataformas externas o productos de mercado, los mecanismos de publicación, mensajería, almacenamiento u otros servicios asociados deberán ser proporcionados y estar gestionados por la propia plataforma externa.

**Eventos originados en sistemas APB:** Cuando el origen de los eventos corresponda a sistemas o servicios de la APB, los mecanismos de integración, buses de eventos, middleware y servicios transversales serán proporcionados por la infraestructura corporativa definida por la APB. Las soluciones desarrolladas deberán integrarse utilizando dichos mecanismos corporativos y respetando las políticas de arquitectura, gobierno y seguridad establecidas.

### 6.7. Datos

Cuando el alcance incluya datos, migraciones o sincronizaciones, el adjudicatario deberá garantizar la integridad, consistencia, trazabilidad y validación de la información.

Toda migración de datos deberá contar con plan, validaciones previas, controles de calidad, trazabilidad de incidencias y mecanismos de reversión o recuperación cuando proceda.

### 6.8. Gobierno y validación arquitectónica

Durante análisis, diseño, construcción e implantación, los equipos deberán coordinarse con el arquitecto de referencia de la APB, que validará el cumplimiento de estándares, supervisará dominios e integraciones y aprobará excepciones arquitectónicas.

El equipo de Arquitectura, Ciberseguridad, Operaciones o QA de la APB definirá:

- Plantillas corporativas de pipelines.
- Herramientas homologadas.
- Reglas de calidad y seguridad.
- Estrategias de versionado y branching.
- Políticas de promoción entre entornos.
- Validaciones obligatorias para autorización de despliegues.

Los equipos adjudicatarios deberán adaptarse a dichas directrices y colaborar con el arquitecto de referencia designado por la APB para garantizar el cumplimiento del modelo corporativo CI/CD.

## 7. CI/CD

Las soluciones deberán integrarse plenamente en los procesos corporativos de CI/CD definidos por la APB, garantizando automatización, trazabilidad, repetibilidad, calidad y seguridad durante todo el ciclo de vida del software.

Los equipos adjudicatarios deberán adaptar sus procesos a los estándares QA, DevOps y DevSecOps corporativos y reducir al mínimo las tareas manuales siempre que sea técnicamente viable. Las soluciones deberán:

- Ser compatibles con pipelines corporativos de CI/CD definidos por la APB.
- Permitir despliegues automatizados, repetibles y auditables en todos los entornos.
- Garantizar trazabilidad completa entre código fuente, artefactos generados, versiones desplegadas, pruebas ejecutadas y cambios funcionales.
- Integrar controles automáticos de calidad, seguridad y validación durante el ciclo de integración y despliegue.
- Permitir rollback controlado y recuperación ante errores de despliegue.
- Minimizar riesgos operativos y reducir dependencias manuales durante la promoción entre entornos.

### 7.1. Repositorio y gestión de código fuente

Todo el código fuente, configuraciones, scripts, pipelines, infraestructura como código y artefactos asociados deberán almacenarse en los repositorios corporativos definidos por la APB.

Los equipos adjudicatarios deberán:

- Utilizar las estrategias de branching, versionado y gestión de repositorios definidas por Arquitectura.
- Mantener trazabilidad entre requisitos, incidencias, desarrollos y commits realizados.
- Garantizar que el código entregado sea compilable, ejecutable y desplegable de forma autónoma por la APB.
- Gestionar correctamente dependencias, paquetes y versiones utilizadas en la solución.
- Evitar la inclusión de secretos, credenciales o configuraciones sensibles dentro del código fuente.

### 7.2. Integración continua (CI)

Los pipelines incluirán, como mínimo, compilación automatizada, pruebas unitarias e integradas, análisis estático, validaciones de seguridad, validación de dependencias, generación de artefactos y validación de contratos cuando aplique Spec Driven Development.

La APB podrá definir herramientas, umbrales mínimos de calidad y políticas de validación obligatorias para la promoción del software.

### 7.3. Despliegue continuo (CD)

Los despliegues deberán ser automatizados, desacoplados y auditables, incorporando validaciones previas y posteriores, promoción controlada entre entornos, gestión de secretos y rollback controlado.

Los despliegues sobre entornos productivos estarán sujetos a los procedimientos de autorización y gobierno establecidos por la APB.

### 7.4. Infraestructura y configuración como código

Siempre que aplique, la infraestructura deberá definirse mediante IaC y la configuración como CaC, con scripts versionados, reproducibilidad de entornos y automatización de despliegues.

La APB podrá establecer herramientas, plantillas y frameworks corporativos obligatorios para dichas automatizaciones.

### 7.5. DevSecOps y seguridad integrada

Se incorporarán análisis automáticos de vulnerabilidades, escaneo de dependencias, validación de contenedores, gestión de secretos, hardening y validaciones de cumplimiento.

Las incidencias de seguridad detectadas deberán corregirse antes de la promoción a entornos superiores, salvo autorización expresa de la APB.

## 8. Calidad

La calidad será obligatoria durante todo el ciclo de vida del software y se alineará con la política corporativa de QA de la APB.

La validación final corresponderá a QA y Arquitectura de APB, o a un tercero designado, pero la ejecución de pruebas, evidencias y corrección de defectos será responsabilidad del adjudicatario.

No se autorizará la promoción de desarrollos a entornos de preproducción o producción cuando no se cumplan los requisitos mínimos de calidad, seguridad y validación establecidos por la APB.

Para más detalle, consultar el documento "Política de QA APB".

### 8.1. Plan de pruebas

El adjudicatario definirá, mantendrá y ejecutará el Plan de Pruebas de cada solución, incluyendo alcance, planificación, estrategia, recursos, criterios de entrada y salida, y dependencias funcionales y técnicas.

### 8.2. Tipología de pruebas

Como mínimo, y según aplique, se contemplarán:

- Pruebas unitarias.
- Pruebas funcionales.
- Pruebas de integración.
- Pruebas de regresión.
- Pruebas de rendimiento y carga.
- Pruebas de resiliencia y tolerancia a fallos.
- Pruebas de compatibilidad entre navegadores, dispositivos y resoluciones.
- Pruebas de seguridad.
- Pruebas de aceptación funcional (UAT).
- Validaciones de APIs, eventos e integraciones distribuidas.

Las pruebas deberán ejecutarse en los entornos definidos por la APB, incluyendo como mínimo TST y PRE.

### 8.3. Automatización y enfoque DevSecOps

Deberán automatizarse, siempre que sea viable, pruebas unitarias, integración, regresión, contratos, seguridad, calidad de código y pruebas de aceptación automatizables.

Las pruebas deberán ser reutilizables, exportables, trazables y ejecutables tras la entrega. Las evidencias generadas deberán entregarse junto con los artefactos software correspondientes.

### 8.4. Cobertura, mantenibilidad y calidad del código

La APB podrá definir umbrales mínimos de cobertura, complejidad, deuda técnica y vulnerabilidades. El adjudicatario deberá generar informes de calidad, evidencias y resultados de pruebas, manteniéndolos actualizados en las herramientas designadas.

Todos los defectos detectados deberán: registrarse, corregirse y revalidarse mediante nuevas ejecuciones de prueba. No se considerará aceptada ninguna funcionalidad mientras existan defectos críticos o bloqueantes pendientes de resolución.

## 9. Herramientas

La APB dispone de un entorno colaborativo corporativo para la gestión integral del ciclo de vida. El uso de las herramientas corporativas de APB será obligatorio para planificación, análisis, desarrollo, documentación, calidad y gobierno técnico.

| Herramienta | Descripción y uso requerido |
|-------------|----------------------------|
| Jira | Herramienta corporativa de ticketing y gestión de tareas utilizada para la gestión y seguimiento de mantenimientos evolutivos, correctivos, incidencias, backlog y trazabilidad de actividades. |
| GitHub | Servicio corporativo de control de versiones y desarrollo colaborativo basado en Git. Se utilizará para la gestión del código fuente, ramas, versionado y repositorios corporativos. El repositorio deberá mantenerse actualizado, como mínimo, en cada entrega. |
| Confluence | Plataforma colaborativa utilizada para la elaboración y mantenimiento de documentación funcional, técnica, operativa y de proyecto, así como para la gestión del conocimiento. |
| Product Discovery | Plataforma orientada a la identificación, organización y priorización de necesidades y funcionalidades, utilizada como soporte a procesos de análisis funcional, descubrimiento y priorización de producto. |
| Service Management | Solución corporativa de gestión de solicitudes, incidencias y servicios utilizada para la coordinación operativa y gestión de actividades cuando así lo requiera la APB. |
| Compass | Herramienta corporativa de gobierno técnico y catálogo de componentes utilizada para la gestión de dependencias, trazabilidad arquitectónica y visibilidad de componentes del sistema. |
| Visual Studio 2022 o superior | Entorno de desarrollo corporativo para soluciones .NET. La APB proporcionará plantillas y estructuras base alineadas con los estándares de Arquitectura para el desarrollo de componentes software. |
| .NET Aspire | Framework cloud-native orientado a aplicaciones distribuidas, observables y preparadas para producción, integrado dentro de las plantillas corporativas de desarrollo. |
| Docker Desktop / Podman Desktop | Herramientas de contenerización utilizadas para la creación, ejecución, validación y gestión de aplicaciones basadas en contenedores. |
| SQL Server Management Studio (SSMS) | Herramienta de administración y gestión de SQL Server y Azure SQL Database utilizada para tareas de validación, administración y soporte de persistencia de datos. |
| DevExpress / DevExtreme | Suite de componentes gráficos y controles de interfaz de usuario utilizada para el desarrollo frontend conforme al sistema de diseño corporativo. Las licencias necesarias correrán a cargo del adjudicatario. |
| Navegadores corporativos | Las aplicaciones deberán garantizar compatibilidad obligatoria con Microsoft Edge y Google Chrome, siendo deseable la compatibilidad con Firefox. Las soluciones deberán ser responsive para entornos desktop y tablet, y opcionalmente para dispositivos móviles. |
| SONAR | Plataforma corporativa de análisis continuo de calidad de código utilizada para validar mantenibilidad, cobertura, vulnerabilidades y deuda técnica conforme a los umbrales definidos por la APB. |
| Plataformas DevOps / CI-CD | Herramientas corporativas de integración continua y despliegue continuo utilizadas para automatización de validaciones, construcción y despliegues conforme a los procedimientos definidos por la APB. |

## 10. Uso de Inteligencia Artificial

El uso de herramientas de inteligencia artificial estará permitido únicamente bajo las condiciones autorizadas por la APB, con carácter asistencial y sin sustituir la responsabilidad técnica del adjudicatario.

Todo resultado asistido por IA deberá ser revisado por personal cualificado y no podrá incorporarse a repositorios, despliegues o entregables sin validación humana explícita.

No podrá introducirse en herramientas de IA información sensible, secretos, código no autorizado, arquitecturas internas, datos personales ni documentación protegida.

La APB podrá auditar el uso de IA y exigir trazabilidad sobre herramientas empleadas, fases, artefactos afectados y validación realizada.

Para más detalle, consultar el documento "Política APB - Uso de IA en para desarrollo de software y soporte técnico".

## 11. Evolución de estándares

APB podrá actualizar en cualquier momento los estándares tecnológicos, arquitectónicos, de calidad o de seguridad aplicables al servicio.

El adjudicatario deberá adaptarse a dichas actualizaciones siempre que no supongan una alteración sustancial del objeto contractual y se comuniquen por los cauces previstos en el contrato.

Cuando se incorporen nuevas herramientas, marcos de trabajo o productos homologados, estos podrán ser de uso obligatorio para los desarrollos afectados.

## 12. Documentación

El adjudicatario será responsable de mantener la documentación actualizada, clara y mantenible, y de obtener su validación por parte de la APB cuando proceda.

La documentación mínima de entrega incluirá, al menos:

| Documento | Contenido mínimo esperado |
|-----------|--------------------------|
| Manual de explotación | Procedimientos de despliegue, configuración, operación, monitorización, backup, recuperación, mantenimiento y soporte técnico de la solución. |
| Manual de usuario | Guías funcionales de uso de la aplicación, navegación, procesos operativos y funcionalidades disponibles para usuarios finales. |
| Manual de procedimiento operativo | Procedimientos operativos asociados al funcionamiento de la solución y coordinación con otros sistemas o equipos. |
| Análisis funcional | Requisitos funcionales, procesos, casos de uso, reglas de negocio, criterios de aceptación, dominios funcionales y flujos operativos. |
| Diseño / análisis técnico | Arquitectura técnica, diseño de componentes, integraciones, APIs, eventos, modelo de datos, diagramas, configuraciones y decisiones técnicas relevantes. |
| Documentación de APIs y contratos | Definición y documentación de APIs REST, eventos, contratos de integración y metadatos asociados (Swagger/OpenAPI, Scalar u otros estándares definidos por la APB). |
| Documentación DevOps y CI/CD | Pipelines, configuraciones de despliegue, automatizaciones, variables de entorno y procedimientos asociados al ciclo CI/CD. |
| Documentación QA | Planes de prueba, evidencias, resultados de validaciones, métricas de calidad y cobertura. |
| Inventario de componentes y dependencias | Relación de librerías, frameworks, servicios externos, componentes reutilizados y dependencias técnicas utilizadas. |

Al cierre del servicio, deberán realizarse las sesiones de transferencia de conocimiento necesarias hacia los equipos designados por la APB.

## 13. Criterios de aceptación

La aceptación técnica de cada entrega quedará condicionada, como mínimo, al cumplimiento de los siguientes extremos:

- Validación funcional y técnica por parte de APB o de quienes esta designe.
- Entrega de código fuente y artefactos asociados.
- Entrega de pruebas automatizadas y evidencias.
- Entrega de documentación actualizada.
- Corrección de incidencias críticas y no conformidades relevantes.
- Cumplimiento de los estándares de arquitectura, seguridad y calidad.

APB podrá rechazar total o parcialmente una entrega cuando no cumpla los estándares definidos en este anexo o cuando existan incidencias que comprometan la operatividad, la seguridad o la mantenibilidad de la solución.

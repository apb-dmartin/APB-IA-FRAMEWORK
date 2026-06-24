# Estudio de Capacidades v1.0

| Versión | Descripción | Autor | Acción | Fecha |
|---------|-------------|-------|--------|-------|
| v1.0 | Elaboración de la Guía | Oficina Técnica de Seguridad (Sothis) | Creación | 19/01/2026 |
| v1.0 | Revisión de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Revisión | 02/05/2026 |
| v1.0 | Aprobación de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Aprobación | 02/05/2026 |

**Tipo de documento:** Registro
**Nivel de seguridad:** Interno
**Propietario:** Responsable de Seguridad de la Información
**Área de difusión:** Todas las personas de la Autoritat Portuària de Barcelona

## 1. Objetivo

La Autoritat Portuària de Barcelona presta servicios esenciales para la gestión, coordinación y soporte de la operativa portuaria, apoyándose en sistemas de información, infraestructuras tecnológicas, recursos humanos e instalaciones que deben garantizar niveles adecuados de disponibilidad, rendimiento, continuidad y seguridad.

El objetivo del presente Estudio de Capacidades es asegurar que los recursos tecnológicos, humanos, operativos y materiales de la Autoritat Portuària de Barcelona sean suficientes para soportar la prestación de sus servicios, cumpliendo con los requisitos del SGSI, el Esquema Nacional de Seguridad (ENS) y la normativa aplicable.

Con carácter previo a la puesta en explotación de nuevos sistemas, servicios o ampliaciones relevantes, se llevará a cabo un análisis de capacidad que contemple las necesidades de procesamiento, almacenamiento de información, comunicaciones, personal, instalaciones y medios auxiliares, hardware y software.

## 2. Alcance

El presente estudio aplica a los sistemas de información, infraestructuras y recursos que soportan los servicios y actividades de la Autoritat Portuària de Barcelona, incluyendo, entre otros:

- La gestión operativa portuaria.
- La gestión administrativa, económica y corporativa.
- Los servicios tecnológicos y de comunicaciones.
- Los sistemas de soporte a la explotación, coordinación y supervisión de la actividad portuaria.
- Los servicios internos y externos cuya prestación dependa de activos tecnológicos o recursos críticos.

Incluye el análisis de demanda, la planificación de capacidad, la monitorización continua y la definición de acciones preventivas y correctivas necesarias para garantizar el cumplimiento de los niveles de servicio, seguridad y continuidad.

## 3. Roles y responsabilidades

Los distintos roles implicados en la gestión de capacidades de la Autoritat Portuària de Barcelona asumirán las responsabilidades necesarias para asegurar una adecuada planificación, supervisión y respuesta ante las necesidades de capacidad de los sistemas y activos críticos.

- **Responsable de Seguridad de la Información:** velará por que la gestión de capacidades se alinee con los requisitos de seguridad y no comprometa la disponibilidad, integridad o confidencialidad de los sistemas y servicios.
- **Responsable del Sistema o responsables técnicos/IT:** realizarán la monitorización, el análisis de capacidad, la gestión de alertas y la propuesta de medidas preventivas o correctivas relacionadas con hardware, software, procesamiento, almacenamiento y comunicaciones.
- **Responsable del Servicio:** supervisará que la capacidad disponible resulte adecuada para la prestación del servicio y comunicará las necesidades operativas que puedan requerir ajustes o ampliaciones.
- **Responsable de la Información:** identificará los requisitos vinculados al volumen, tratamiento, conservación y disponibilidad de la información que puedan tener impacto en la capacidad de los sistemas.
- **Comité de Gestión de Seguridad de la Información:** revisará la información relevante derivada del análisis de capacidades y promoverá las decisiones necesarias cuando existan riesgos o necesidades que puedan afectar a la continuidad o a la seguridad de los servicios.
- **Dirección General:** respaldará la adopción de las medidas necesarias y facilitará los recursos que resulten precisos conforme a la planificación, prioridades y procedimientos aplicables.

## 4. Desarrollo del Estudio de Capacidades

### 4.1. Herramientas de monitorización y gestión

La Autoritat Portuària de Barcelona emplea herramientas de monitorización y gestión que permiten supervisar el rendimiento de la infraestructura, detectar incidencias, analizar tendencias y anticipar necesidades de capacidad. Entre dichas soluciones se incluyen sistemas de monitorización de infraestructuras, sistemas y comunicaciones; plataformas de registro y análisis de eventos y logs; medios corporativos de supervisión y gestión técnica; plataformas de ticketing para la gestión de incidencias, peticiones y necesidades de capacidad; y, cuando proceda, soluciones proporcionadas por fabricantes o proveedores tecnológicos.

Las solicitudes, peticiones relacionadas con necesidades de capacidad se registrarán a través de la herramienta corporativa Jira ITSM, que actuará como canal formal para su trazabilidad, análisis y seguimiento.

Estas herramientas permiten establecer alertas, generar informes, analizar la evolución del consumo de recursos y facilitar la toma de decisiones sobre ampliaciones, sustituciones, refuerzos o mejoras.

### 4.2. Necesidades de procesamiento

Se monitoriza el uso de CPU, memoria, carga de trabajo y rendimiento de los sistemas que soportan la operativa y los servicios de la Autoritat Portuària de Barcelona, especialmente aquellos considerados críticos para el funcionamiento de la organización.

Este análisis podrá aplicarse a las plataformas de gestión operativa y administrativa, los servicios corporativos y de soporte a usuarios, los entornos de virtualización y servidores, las soluciones de supervisión, control y gestión tecnológica, y las aplicaciones críticas para la continuidad del servicio.

Se establecen los siguientes umbrales orientativos de control:

| Recurso | Umbral de advertencia | Umbral crítico |
|---------|----------------------|----------------|
| CPU | 75 % | 85 % |
| Memoria RAM | 75 % | 85 % |
| Capacidad de procesamiento en sistemas críticos | 70 % | 85 % |

La monitorización será continua en los activos críticos y su revisión se realizará periódicamente. Las alertas se gestionarán conforme a los procedimientos establecidos y, en caso de requerirse una actuación, se registrará la correspondiente solicitud en Jira ITSM.

Cuando el análisis evidencie una necesidad de ampliación, renovación o redistribución de carga, se valorarán las medidas técnicas más adecuadas conforme al procedimiento de gestión de capacidades.

### 4.3. Necesidades de almacenamiento de información

Los sistemas de Autoritat Portuària de Barcelona gestionan información crítica para la prestación de los servicios y para el funcionamiento interno de la organización, incluyendo información operativa, administrativa, técnica, económica y documental.

La capacidad de almacenamiento deberá ser suficiente para soportar el crecimiento de la información gestionada, las necesidades de explotación de los sistemas, las copias de seguridad y las políticas de retención, así como los requisitos legales, regulatorios y operativos aplicables.

Para ello, se tendrá en cuenta la disponibilidad de sistemas de almacenamiento escalables, mecanismos de ampliación controlada, políticas de copia de seguridad y retención, revisiones periódicas del consumo y crecimiento de la información, y medidas de optimización y depuración cuando proceda.

Con carácter orientativo, cuando el almacenamiento de sistemas o repositorios críticos alcance niveles próximos al 90 % de su capacidad útil, deberá analizarse la necesidad de ampliación, optimización o revisión de las políticas de conservación y retención.

### 4.4. Necesidades de comunicación

Las comunicaciones deben garantizar un funcionamiento adecuado de los servicios, el acceso seguro a los sistemas y la conectividad entre sedes, usuarios, equipos e infraestructuras.

El análisis de capacidad en este ámbito tendrá en cuenta, entre otros aspectos: el ancho de banda disponible; la ocupación de enlaces y redes; la disponibilidad y redundancia de las comunicaciones; la capacidad de los equipos de red y seguridad perimetral; las necesidades de acceso remoto y comunicaciones seguras.

La infraestructura de comunicaciones deberá permitir soportar la actividad de la Autoritat Portuària de Barcelona sin degradaciones significativas del servicio y con capacidad suficiente para absorber incrementos razonables de demanda, nuevos servicios o ampliaciones de uso previstas.

### 4.5. Necesidades de hardware

Las necesidades de hardware se identifican a partir de la monitorización de la infraestructura, del análisis de tendencias de uso, de la obsolescencia tecnológica, de las incidencias detectadas y de la evolución de los servicios soportados.

El análisis incluirá, entre otros componentes: servidores físicos y virtuales; cabinas o sistemas de almacenamiento; equipamiento de red y comunicaciones; dispositivos críticos de soporte a los servicios; equipamiento de usuario cuando resulte necesario para la operativa.

El hardware será objeto de seguimiento periódico para detectar saturaciones, degradaciones de rendimiento, carencias de capacidad o situaciones de obsolescencia. Cuando se identifique una necesidad de ampliación, sustitución o renovación, esta se documentará en Jira ITSM y se evaluará técnicamente.

Si la solución requiere adquisición de equipamiento, esta se tramitará de acuerdo con los procedimientos internos de compra y, en su caso, mediante el correspondiente proceso de contratación pública.

### 4.6. Necesidades de software

Las necesidades de software incluyen tanto las aplicaciones de soporte a la actividad como las herramientas técnicas necesarias para garantizar la operación, la administración, la seguridad, la monitorización y la continuidad de los servicios.

El análisis de capacidad en este ámbito tendrá en cuenta el número de licencias disponibles y su suficiencia, la capacidad funcional de las aplicaciones, la escalabilidad de las soluciones implantadas, la necesidad de nuevas herramientas o ampliaciones, su compatibilidad con la arquitectura tecnológica existente, y los requisitos de soporte, mantenimiento y seguridad.

Las necesidades identificadas se registrarán en Jira ITSM, desde donde se realizará su evaluación funcional y técnica. La obtención de nuevas soluciones, ampliaciones de licencias o implantación de aplicaciones se realizará, con carácter general, mediante los mecanismos de adquisición establecidos por la organización, incluyendo, cuando proceda, licitaciones o concursos públicos.

### 4.7. Necesidades de instalaciones y medios auxiliares

La capacidad de las instalaciones y de los medios auxiliares deberá ser adecuada para soportar tanto la infraestructura tecnológica como la actividad de los equipos que prestan soporte a la operativa de la Autoritat Portuària de Barcelona.

Este análisis incluirá, cuando resulte aplicable: disponibilidad de espacios y puestos de trabajo, adecuación de salas técnicas o emplazamientos de equipos, condiciones de alimentación eléctrica y climatización, requisitos de seguridad física, capacidad para albergar ampliaciones de equipamiento o incorporación de personal.

Cuando se identifiquen limitaciones de espacio, condiciones técnicas insuficientes o necesidades derivadas del crecimiento de servicios, proyectos o equipos, se impulsarán las actuaciones oportunas para su adaptación, coordinación o ampliación.

### 4.8. Necesidades de personal

La gestión de la capacidad operativa se apoya en el seguimiento de la carga de trabajo, la distribución de tareas, las incidencias, las peticiones de servicio y los proyectos en curso. Este análisis permite valorar si los recursos humanos disponibles son suficientes para atender la actividad ordinaria y las necesidades de evolución de la organización.

La dedicación del equipo podrá centrarse en las siguientes actividades: gestión de incidencias, atención de peticiones de servicio, administración y mantenimiento de sistemas, ejecución de proyectos de mejora y evolución, soporte técnico y funcional a los servicios de la organización.

Durante el análisis de capacidades deberán identificarse posibles riesgos asociados a la insuficiencia de recursos, a la dependencia de personas clave o a la falta de cobertura en funciones críticas.

En particular, en caso de jubilación de una persona, se evaluará con la suficiente antelación el impacto de la vacante, la transferencia de conocimiento necesaria y la conveniencia de iniciar la cobertura del puesto o de redistribuir temporalmente las funciones hasta que se formalice la solución definitiva.

Si resulta preciso incorporar personal estructural o cubrir puestos, su tramitación se realizará conforme al proceso de contratación pública o al procedimiento corporativo que resulte de aplicación en la organización.

Podrá valorarse la externalización del servicio o de funciones especializadas en aquellos supuestos en los que no se disponga internamente de los perfiles requeridos, o cuando dicha opción resulte más adecuada por razones técnicas, organizativas o de eficiencia, de conformidad con los procedimientos de contratación y supervisión aplicables.

Cuando se detecten limitaciones en la capacidad operativa, podrán adoptarse medidas como: refuerzo de recursos, formación continua del personal, transferencia de conocimiento, documentación de procedimientos críticos, automatización de tareas, mejora y simplificación de procesos.

Estas actuaciones contribuirán a garantizar la continuidad del servicio, reducir riesgos operativos y mejorar la resiliencia del equipo técnico y de soporte.

## 5. Revisión y actualización

El presente estudio será revisado al menos una vez al año o siempre que se produzcan cambios significativos en: la infraestructura tecnológica, los servicios prestados, el volumen de usuarios o de demanda, la organización interna, las necesidades de personal, las instalaciones y el marco normativo o de seguridad aplicable.

Las actualizaciones correspondientes serán elevadas para su validación y aprobación conforme al marco de gobierno interno establecido por la Autoritat Portuària de Barcelona.

## 6. Registros

- Registros de solicitudes y seguimiento en Jira ITSM corporativo.
- Evidencias asociadas a adquisiciones, licitaciones o actuaciones derivadas del análisis de capacidad.

## 7. Anexo. Glosario de términos

- **Capacidades:** Nivel de recursos disponibles para soportar de forma adecuada la operación, el rendimiento, la continuidad y la evolución de los sistemas, servicios, instalaciones y equipos de la organización.
- **Gestión de capacidades:** Proceso orientado a planificar, supervisar, analizar y ajustar los recursos necesarios para asegurar que la organización puede atender sus necesidades actuales y futuras sin degradación significativa del servicio.
- **Planificación de capacidades:** Actividad mediante la cual se prevén y organizan las necesidades futuras de recursos tecnológicos, humanos, físicos y organizativos, con el fin de garantizar la continuidad y la eficiencia operativa.

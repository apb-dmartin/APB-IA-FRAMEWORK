# Guía de Gestión de Capacidades v1.0

| Versión | Descripción | Autor | Acción | Fecha |
|---------|-------------|-------|--------|-------|
| v1.0 | Elaboración de la Guía | Oficina Técnica de Seguridad (Sothis) | Creación | 19/01/2026 |
| v1.0 | Revisión de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Revisión | 02/05/2026 |
| v1.0 | Aprobación de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Aprobación | 02/05/2026 |

**Tipo de documento:** Guía
**Nivel de seguridad:** Interno
**Propietario:** Responsable de Seguridad de la Información
**Área de difusión:** Todas las personas de la Autoritat Portuària de Barcelona

## 1. Objetivo

Este procedimiento se aplica a los recursos, activos y elementos necesarios para la prestación de los servicios de la Autoritat Portuària de Barcelona, incluyendo instalaciones, recursos humanos, hardware, software, licencias, sistemas, servidores, comunicaciones y demás componentes críticos cuya insuficiencia, degradación o indisponibilidad pueda afectar a la operativa portuaria, a la prestación de servicios o al normal desarrollo de las actividades de la organización.

## 2. Alcance

Este procedimiento abarca todos los dispositivos, servidores y componentes críticos de la infraestructura de la Autoritat Portuària de Barcelona que, de no estar disponibles, afectarían directamente a la operativa portuaria, a la prestación de servicios o al normal desarrollo de las actividades de la organización.

## 3. Roles y responsabilidades

Los distintos roles implicados en la gestión de capacidades de la Autoritat Portuària de Barcelona asumirán las responsabilidades necesarias para asegurar una adecuada planificación, supervisión y respuesta ante las necesidades de capacidad de los sistemas y activos críticos.

- **Responsable de la Información:** deberá identificar los requisitos de capacidad vinculados al tratamiento, almacenamiento, acceso y crecimiento de la información bajo su responsabilidad, comunicando cualquier necesidad o cambio que pueda afectar al correcto funcionamiento de los sistemas que la soportan.
- **Responsable del Servicio:** deberá determinar las necesidades de capacidad requeridas para garantizar la correcta prestación de los servicios, evaluando el impacto que una insuficiencia de recursos pudiera tener sobre la operativa, la continuidad y los niveles de servicio establecidos.
- **Responsable de Seguridad de la Información (RSI):** deberá asegurar que la gestión de capacidades de los activos críticos contemple los requisitos de seguridad de la información y que las actuaciones adoptadas en este ámbito sean coherentes con el marco de control y protección definido por la organización.
- **Responsable del Sistema:** deberá realizar el seguimiento técnico de la capacidad, disponibilidad y rendimiento de los sistemas bajo su responsabilidad, identificar desviaciones o riesgos, y proponer e implantar las medidas necesarias para corregir o prevenir situaciones de saturación o degradación.
- **Comité de Gestión de Seguridad de la Información:** deberá supervisar el estado general de la gestión de capacidades en relación con los activos críticos, revisar los riesgos e incidencias asociados y promover la adopción de decisiones y medidas de mejora.
- **Dirección General:** deberá proporcionar el apoyo organizativo y los recursos necesarios para la correcta aplicación de este procedimiento, así como impulsar las actuaciones que resulten necesarias para mantener la capacidad adecuada de las infraestructuras y servicios esenciales.

## 4. Desarrollo del Proceso de Gestión de Capacidades

La gestión de capacidades en la Autoritat Portuària de Barcelona tiene como finalidad asegurar que las instalaciones, los recursos humanos, la infraestructura tecnológica y las aplicaciones dispongan en todo momento de la capacidad adecuada para dar soporte a la operativa, a los servicios prestados y a las necesidades de evolución de la organización.

Este proceso comprende la revisión periódica de la capacidad disponible, la identificación de necesidades futuras, la gestión de solicitudes de ampliación o refuerzo, y la adopción de medidas preventivas o correctivas para evitar situaciones de saturación, degradación del rendimiento o insuficiencia de recursos.

Las necesidades detectadas podrán estar relacionadas con: las instalaciones y espacios físicos, la dotación de personal, el hardware, el software y las licencias o soluciones tecnológicas requeridas.

Con carácter general, las solicitudes e iniciativas asociadas a necesidades de capacidad se tramitarán a través de la herramienta corporativa Jira ITSM, sin perjuicio de que su ejecución deba continuar posteriormente por los cauces administrativos, técnicos o de contratación que correspondan.

### 4.1. Revisión de Capacidades

Se entenderá por capacidades el conjunto de recursos necesarios para garantizar el correcto funcionamiento de los sistemas, servicios e infraestructuras de la Autoritat Portuària de Barcelona.

La revisión de capacidades se realizará de forma periódica, y al menos con carácter mensual, sobre los elementos críticos cuya insuficiencia pueda afectar a la disponibilidad, continuidad o rendimiento de los servicios. Su finalidad será identificar necesidades actuales o futuras, detectar riesgos y definir, en su caso, las actuaciones de mejora o ampliación que resulten necesarias.

Esta revisión abarcará, como mínimo, los siguientes ámbitos:

- **Infraestructura tecnológica y hardware:** uso de CPU, memoria y almacenamiento, estado y capacidad de servidores, clústeres, cabinas, electrónica de red, sistemas de copia de seguridad, así como obsolescencia y necesidades de renovación.
- **Software:** capacidad funcional de las aplicaciones, suficiencia de licencias, necesidades de ampliación o nuevas herramientas, y compatibilidad con la infraestructura existente.
- **Personal:** suficiencia de recursos para atender la operativa, proyectos, soporte y mantenimiento, así como cobertura de funciones críticas y previsión de vacantes.
- **Instalaciones:** adecuación de espacios, puestos de trabajo, salas técnicas y condiciones de suministro, climatización, seguridad física y conectividad.

Toda revisión deberá quedar documentada, indicando el recurso o ámbito analizado, la situación observada, los riesgos detectados y las acciones propuestas.

Cuando la criticidad del activo o el volumen de recursos gestionados lo requiera, podrán establecerse revisiones más frecuentes y controles específicos.

### 4.2. Identificación y gestión de necesidades de capacidad

Las necesidades de capacidad podrán identificarse a partir de la monitorización técnica de infraestructuras y sistemas, de incidencias recurrentes o degradaciones del servicio, de solicitudes de nuevas necesidades operativas, de proyectos de transformación o evolución tecnológica, de incrementos previstos de actividad, de la incorporación de nuevas dependencias, servicios o usuarios, de jubilaciones o cambios organizativos que generen necesidades de cobertura, así como de requerimientos normativos, de seguridad o de continuidad.

Toda necesidad detectada deberá registrarse en Jira ITSM, dejando constancia, como mínimo, de su naturaleza, justificación, impacto previsto, prioridad y área afectada. A partir de este registro, se analizará la necesidad, se valorará su criticidad y se determinará la actuación más adecuada, así como su tramitación por el circuito técnico, organizativo, administrativo o de contratación que corresponda.

#### 4.2.1. Necesidades de instalaciones

Cuando se identifiquen necesidades relacionadas con espacios, puestos, salas técnicas o adecuaciones físicas, el área responsable analizará la disponibilidad existente y la viabilidad de adaptación o ampliación. Se valorará el impacto en la operativa, la urgencia de la necesidad y la coordinación con las áreas competentes en infraestructuras y servicios generales, a fin de adoptar las medidas oportunas.

#### 4.2.2. Necesidades de personal

Cuando se detecte que la capacidad de atención, operación, soporte o evolución no puede cubrirse adecuadamente con los recursos disponibles, se analizará la necesidad de refuerzo de personal. Para ello se tendrá en cuenta el volumen de trabajo actual y previsto, la criticidad de las funciones afectadas, los conocimientos y perfiles requeridos, la necesidad de cobertura estable o puntual y los riesgos derivados de la falta de recursos.

En caso de jubilación de una persona, deberá evaluarse con antelación suficiente el impacto de la vacante, la necesidad de transferencia de conocimiento y la conveniencia de iniciar la cobertura del puesto o de redistribuir temporalmente las funciones hasta la implantación de la solución definitiva.

La cobertura de puestos o la incorporación de personal se tramitará conforme a la normativa y a los procedimientos corporativos de selección, provisión o contratación de personal aplicables. Cuando no se disponga internamente de los perfiles requeridos, o cuando resulte más adecuado por razones técnicas, organizativas o de eficiencia, podrá valorarse la externalización del servicio o de funciones especializadas, de acuerdo con los procedimientos de contratación pública y supervisión que resulten de aplicación.

#### 4.2.3. Necesidades de hardware

Las necesidades de hardware se identificarán principalmente mediante la monitorización de la infraestructura, el análisis de tendencias de uso, la obsolescencia tecnológica, la evolución de los servicios y la aparición de incidencias por saturación o falta de rendimiento.

Cuando se detecte una necesidad de ampliación, sustitución o renovación, esta se registrará en Jira ITSM y se evaluará técnicamente para determinar la solución más adecuada, priorizando la continuidad de los servicios críticos y la eficiencia de la inversión. La adquisición o renovación de equipamiento se realizará conforme a los procedimientos internos de compra y, cuando proceda, a través del correspondiente proceso de contratación pública.

#### 4.2.4. Necesidades de software

Las necesidades de software incluirán nuevas aplicaciones, ampliaciones funcionales, incremento de licencias, herramientas de soporte, soluciones de monitorización o cualquier otro componente lógico necesario para atender las necesidades operativas o tecnológicas.

Estas necesidades deberán justificarse funcional y técnicamente, y se tramitarán inicialmente a través de Jira ITSM. Su provisión se realizará, con carácter general, mediante los mecanismos de adquisición establecidos por la organización, incluyendo, cuando corresponda, licitaciones o concursos públicos.

Antes de promover la adquisición, se valorará la existencia de soluciones corporativas ya disponibles, la compatibilidad con la arquitectura tecnológica existente, los requisitos de seguridad, mantenimiento, escalabilidad y soporte futuro.

### 4.3. Indicadores críticos de capacidad

Con el fin de anticipar situaciones de riesgo y activar medidas preventivas, se establecen indicadores críticos de capacidad para los ámbitos tecnológicos, de personal e instalaciones.

Con carácter orientativo, podrán utilizarse los siguientes umbrales o criterios de atención:

- **CPU y memoria RAM en sistemas críticos:** advertencia a partir del 75 % y criticidad a partir del 85 %.
- **Almacenamiento en sistemas o repositorios críticos:** criticidad a partir del 90 %.
- **Licencias o capacidades funcionales de aplicaciones:** situación de atención cuando la disponibilidad remanente no permita atender nuevas necesidades previstas.
- **Personal:** situación crítica cuando se detecte falta de cobertura de funciones esenciales, dependencia de una única persona o acumulación de tareas no asumibles en plazo razonable.
- **Instalaciones:** situación de atención cuando las limitaciones de espacio, suministro, climatización o seguridad física puedan comprometer la operativa o la ampliación prevista.

La superación de estos umbrales o la concurrencia de cualquiera de estas circunstancias deberá dar lugar al correspondiente análisis, a la valoración de medidas correctoras o preventivas y, en su caso, al registro y seguimiento de la actuación en Jira ITSM.

### 4.4. Planificación de Capacidades

La planificación de capacidades tiene por objeto asegurar que la Autoritat Portuària de Barcelona disponga de los recursos necesarios para mantener la continuidad, disponibilidad y rendimiento de sus sistemas, servicios, instalaciones y equipos.

La planificación se basará en la información obtenida de la monitorización, las revisiones periódicas, la evolución de la demanda, los cambios organizativos, las incidencias detectadas y las necesidades comunicadas por las áreas responsables.

Toda necesidad o iniciativa identificada deberá registrarse en la herramienta corporativa Jira ITSM, dejando constancia, como mínimo, de los siguientes aspectos: ID, fecha, necesidad o iniciativa, tipo, ámbito, servicio o activo afectado, justificación, impacto, actuación planificada, responsable, prioridad, fecha prevista, estado y seguimiento u observaciones.

A partir de este registro, se analizará cada caso para determinar su criticidad, su impacto en la operativa y la actuación más adecuada, que podrá consistir, entre otras medidas, en la ampliación o renovación de hardware, la adquisición de software o licencias, la adecuación de instalaciones, la redistribución de recursos, la incorporación de personal, la cobertura de vacantes o la externalización de servicios especializados.

Las actuaciones que requieran adquisición, contratación o cobertura de necesidades deberán tramitarse conforme a los procedimientos corporativos y administrativos que resulten de aplicación.

El seguimiento de las actuaciones se mantendrá actualizado en el registro del Plan de Capacidades hasta su cierre, dejando evidencia del estado de ejecución y de las observaciones que resulten necesarias.

La planificación de capacidades se revisará al menos una vez al año, sin perjuicio de revisiones extraordinarias cuando se produzcan cambios relevantes en la infraestructura, los servicios, la demanda o la organización.

### 4.5. Monitorización, ejecución y seguimiento de actuaciones

Los activos cuya indisponibilidad, degradación o falta de capacidad pueda afectar a la operativa o a la prestación de servicios de la Autoritat Portuària de Barcelona deberán estar sujetos a monitorización mediante las herramientas corporativas habilitadas a tal efecto.

La monitorización se realizará de forma continua, o con la frecuencia técnica que se determine en cada caso, con el fin de detectar de manera temprana incidencias, desviaciones, saturaciones o degradaciones del rendimiento. Serán objeto de monitorización, al menos, los servidores y plataformas de procesamiento, los sistemas de almacenamiento y copia de seguridad, la electrónica y redes de comunicaciones, los servicios y aplicaciones críticas, las infraestructuras virtualizadas o entornos de alta disponibilidad y cualesquiera otros activos tecnológicos que se consideren esenciales.

Las alertas e incidencias detectadas serán analizadas por los equipos responsables y, cuando proceda, darán lugar al registro de la correspondiente actuación en Jira ITSM para su seguimiento.

La información obtenida de la monitorización servirá de base para la revisión periódica de capacidades, la identificación de tendencias, la planificación de ampliaciones o renovaciones, la priorización de inversiones y la prevención de incidencias operativas.

Las actuaciones derivadas de este proceso podrán consistir, entre otras, en ajustes de configuración, redistribución o racionalización de recursos, ampliación o sustitución de hardware, adquisición o ampliación de software y licencias, adecuación de instalaciones, reorganización interna de tareas, cobertura de vacantes, tramitación de contrataciones o externalización de servicios especializados.

Todas las actuaciones deberán mantenerse bajo seguimiento hasta su cierre, dejando constancia del estado de la solicitud, de la solución adoptada y de la fecha de implantación.

## 5. Registros

- DTR - Gestión de capacidades
- DTR - Estudio de Capacidades
- Registros de solicitudes, análisis y seguimiento en la Herramienta corporativa Jira ITSM, evidencias de revisión periódica de capacidades y actuaciones adoptadas.

## 6. Anexo. Glosario de términos

- **Capacidad:** Nivel de recursos disponibles para soportar de forma adecuada la operación, el rendimiento, la continuidad y la evolución de los sistemas, servicios, instalaciones y equipos de la organización.
- **Gestión de capacidades:** Proceso orientado a planificar, supervisar, analizar y ajustar los recursos necesarios para asegurar que la organización puede atender sus necesidades actuales y futuras sin degradación significativa del servicio.
- **Planificación de capacidades:** Actividad mediante la cual se prevén y organizan las necesidades futuras de recursos tecnológicos, humanos, físicos y organizativos, con el fin de garantizar la continuidad y la eficiencia operativa.
- **Activo crítico:** Elemento tecnológico, físico, lógico o humano cuya indisponibilidad, degradación o insuficiencia puede afectar de forma relevante a la prestación de los servicios o al funcionamiento de la organización.

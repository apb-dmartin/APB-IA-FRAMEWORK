# PolíticasAPB - Procedimiento - Gestion de incumplimientos - v1(1)

ÍNDICE

1.	Introducción	4

2.	Definiciones	5

3.	Roles y responsabilidades	7

3.

1.	Responsables de políticas según su naturaleza	7

3.

2.	Roles operativos en la gestión de incumplimientos	8

3.

3.	Gobernanza del proceso	8

3.

4.	Matriz RACI	9

4.	Descripción del proceso	9

5.	Detección de incumplimientos	10

5.

1.	Detección automática	10

5.

2.	Detección manual	11

5.

3.	Notificación de incumplimientos	12

6.	Clasificación de incumplimientos	12

7.	Registro y evidencias de incumplimientos	13

7.

1.	Registro del incumplimiento	14

7.

2.	Generación automática de registros	15

7.

3.	Evidencias del incumplimiento	15

7.

4.	Estados del proceso de gestión	15

7.

5.	Principio de control y auditoría	16

8.	Escalado, seguimiento, corrección y cierre	16

8.

1.	Análisis del incumplimiento	16

8.

2.	Definición y ejecución de acciones correctivas	16

8.

3.	Seguimiento del incumplimiento	17

8.

4.	Escalado de incumplimientos	17

8.

5.	Validación de la corrección	17

8.

6.	Cierre del incumplimiento	18

8.

7.	Monitorización y cuadro de mando de incumplimientos	18

9.	Excepciones	19

9.

1.	Registro de la solicitud de excepción	19

9.

2.	Condiciones de las excepciones	20

9.

3.	Flujo de aprobación	20

9.

4.	Seguimiento de excepciones	21

9.

5.	Criterios de valoración de excepciones	21

9.

6.	Excepción de Emergencia (Fast-track).	24

9.

7.	Criterio Legacy y Compliance	25

9.

8.	Principio de no empeoramiento (Legacy)	26

9.

9.	Principio de no acumulación de excepciones	27

1

0.	Tiempos de resolución y gestión de excepciones	27

1

1.	Especificaciones según políticas concretas	28

11.

1.	QA en desarrollo a medida Docks	29

	

Introducción 

Objetivo

El presente procedimiento establece el marco para la detección, registro, gestión, seguimiento y resolución de los incumplimientos de las Políticas IT del Port de Barcelona (APB).

Las Políticas IT de APB definen las normas técnicas, organizativas y de seguridad que deben seguirse en el diseño, desarrollo, implantación, operación y mantenimiento de los sistemas de información.

Estas políticas tienen como finalidad:

Minimizar riesgos tecnológicos y de seguridad

Reducir riesgos operativos y de estabilidad en los sistemas

Evitar impactos económicos derivados de decisiones tecnológicas inadecuadas

Mejorar la mantenibilidad y evolución futura de los sistemas

Reducir la deuda técnica

Garantizar la calidad y coherencia tecnológica del ecosistema de sistemas

Asegurar el cumplimiento de marcos normativos aplicables, como el Esquema Nacional de Seguridad (ENS) o ISO 

27001.

Las políticas definidas por los Sistemas de Información del Port de Barcelona son de obligado cumplimiento para todos los equipos que participen en el ciclo de vida de los sistemas.

Antes de iniciar cualquier desarrollo, integración, implantación tecnológica o modificación relevante de un sistema, los equipos deberán consultar y revisar las políticas aplicables para garantizar su cumplimiento desde las fases iniciales del trabajo.

Todas las políticas definidas en el ámbito IT deben considerarse igualmente relevantes, independientemente de su naturaleza (seguridad, arquitectura, desarrollo, operación, datos, integración, workplace, técnica, documental, gobernanza, etc.). El cumplimiento homogéneo de estas políticas es un elemento fundamental para garantizar la gobernanza tecnológica y la gestión adecuada del riesgo.

Dado que las tecnologías, herramientas y necesidades operativas evolucionan de forma continua, las Políticas IT podrán actualizarse o ampliarse periódicamente. Por este motivo, deberán consultarse siempre en su versión vigente antes de iniciar cualquier trabajo.

Ámbito de aplicación

Este procedimiento aplica a todos los sistemas, servicios y activos tecnológicos gestionados por los Sistemas de Información del Port de Barcelona, así como a cualquier actividad tecnológica que se realice dentro de este ámbito. 

Este procedimiento aplica a todos los equipos y organizaciones que participen en el ciclo de vida de los sistemas, incluyendo: Equipos internos de Sistemas de Información, proveedores tecnológicos y empresas externas que desarrollen o mantengan sistemas para APB

Las Políticas IT pueden abarcar diferentes ámbitos, entre ellos:

Ciberseguridad

Arquitectura tecnológica

Desarrollo y calidad del software

Integración de sistemas

Gestión de datos y bases de datos

Uso y gobierno de servicios IaaS, PaaS y SaaS

Gestión de costes tecnológicos (FinOps)

Operación y gestión de plataformas

Infraestructura y workplace.

Normas técnicas o de gobernanza internas

Requisitos derivados de marcos regulatorios o de cumplimiento

Esta lista no es limitativa. Podrán existir otras políticas o normas técnicas adicionales definidas que también estarán sujetas a este procedimiento.

Cualquier desviación o incumplimiento de estas políticas deberá gestionarse conforme al presente procedimiento, garantizando su correcta trazabilidad, análisis, seguimiento y resolución.

El presente procedimiento podrá revisarse periódicamente para adaptarse a la evolución de las Políticas IT, a cambios en las herramientas corporativas o a mejoras en los mecanismos de control.

Definiciones

A efectos del presente procedimiento se establecen las siguientes definiciones:

Política IT

Conjunto de normas, directrices y requisitos técnicos u organizativos definidos por el área de Sistemas de Información del Port de Barcelona (APB) que establecen cómo deben diseñarse, desarrollarse, implantarse, operar o mantener los sistemas y servicios tecnológicos.

Las políticas IT son de obligado cumplimiento para todos los equipos internos y proveedores que trabajen con sistemas gestionados por APB.

Incumplimiento

Se considera incumplimiento cualquier desviación respecto a los requisitos establecidos en una Política IT vigente.

Los incumplimientos pueden originarse por diferentes causas, entre ellas:

Diseño o implementación técnica no alineada con la política

Omisión de controles obligatorios

Uso de tecnologías, configuraciones o infraestructura no permitidas

Falta de documentación requerida

Desviaciones detectadas mediante controles automáticos o revisiones técnicas

Los incumplimientos deberán registrarse, analizarse y gestionarse conforme a lo establecido en el presente procedimiento. El registro de incumplimientos deberá mantenerse actualizado y disponible para auditorías internas y externas.

Excepción

Autorización formal y temporal para permitir una desviación respecto a una Política IT cuando exista una justificación de negocio, técnica u operativa debidamente documentada.

La concesión de una excepción implica la aceptación explícita del riesgo asociado, así como el establecimiento de medidas compensatorias, un plan de corrección y una fecha límite de resolución

Las excepciones deberán seguir el flujo de aprobación definido en este procedimiento.

Riesgo aceptado

Situación en la que la organización decide asumir temporalmente el riesgo derivado de un incumplimiento, tras haber evaluado su impacto y haber autorizado formalmente la excepción correspondiente.

La aceptación de riesgos deberá quedar registrada y ser trazable, de acuerdo con los principios de gestión del riesgo definidos en el Esquema Nacional de Seguridad (ENS) y en ISO/IEC 

27001.

Medidas compensatorias

Controles técnicos u organizativos adicionales que se aplican para reducir el impacto del riesgo asociado a un incumplimiento, mientras la excepción se mantiene vigente. Estas medidas deben ser evaluadas y validadas por los equipos responsables correspondientes de la política. La aplicación de medidas compensatorias y la aceptación de riesgos se realizará conforme al principio de proporcionalidad definido en el ENS. 

Validación independiente

Proceso mediante el cual la corrección de un incumplimiento es verificada por un equipo distinto del que realizó la implementación o corrección.

Este principio garantiza la segregación de funciones, recomendada por ENS e ISO 27001, y asegura que la resolución del incumplimiento se ha realizado correctamente antes del cierre formal.

Incumplimiento activo

Incumplimiento que ha sido detectado y registrado pero que aún no ha sido corregido ni cerrado tras validación independiente. Mientras un incumplimiento esté activo deberá mantenerse en seguimiento.

Registro de incumplimientos

Repositorio o sistema de gestión donde se documentan los incumplimientos detectados, incluyendo:

Descripción del incumplimiento

Evidencias

Responsables asignados

Acciones de corrección

Estado de seguimiento

Validación final

Este registro garantiza la trazabilidad y auditabilidad del proceso.

Roles y responsabilidades

La gestión de los incumplimientos de las Políticas IT requiere la participación coordinada de distintos equipos y roles dentro de los Sistemas de Información del Port de Barcelona.

Con el fin de garantizar la claridad en la asignación de responsabilidades, se distinguen tres niveles:

Responsables de políticas según su naturaleza

Roles operativos en la gestión de incumplimientos

Gobernanza del proceso

Responsables de políticas según su naturaleza

Con el fin de garantizar una definición adecuada de las políticas, su correcta interpretación y la gestión efectiva de los posibles incumplimientos, cada política deberá tener asignado uno o varios equipos responsables en función de su naturaleza.

Los equipos responsables de cada política tendrán, entre otras funciones:

Definir y mantener las políticas correspondientes a su ámbito.

Interpretar y aclarar los requisitos establecidos en dichas políticas.

Participar en la evaluación técnica de los incumplimientos detectados.

Evaluar las solicitudes de excepción cuando afecten a las políticas bajo su responsabilidad.

Estos equipos corresponden al rol “Equipo responsable de la política” definido en el presente procedimiento.

Roles operativos en la gestión de incumplimientos

En el proceso de gestión de incumplimientos participan los siguientes roles operativos:

Gobernanza del proceso

El proceso de gestión de incumplimientos se encuentra supervisado por los siguientes roles de gobernanza:

Matriz RACI 

La siguiente matriz RACI define las responsabilidades de los distintos equipos en relación con la definición, cumplimiento, supervisión y gestión de excepciones de las Políticas IT.

R = Responsible (ejecuta)
A = Accountable (responsable último / decisión)
C = Consulted (consultado)
I = Informed (informado)

Descripción del proceso

La gestión de los incumplimientos de las Políticas IT de APB se basa en un proceso estructurado que permite detectar, registrar, analizar, corregir y validar las desviaciones respecto a las políticas definidas.

Este proceso garantiza que todos los incumplimientos:

Queden identificados de forma sistemática

Dispongan de trazabilidad completa

Tengan responsables claramente asignados

Sean corregidos o gestionados mediante excepciones formales

El proceso general de gestión de incumplimientos se compone de las siguientes fases:

Detección del incumplimiento

Registro formal del incumplimiento

Análisis del incumplimiento

Definición y ejecución de acciones correctivas

Validación independiente de la corrección

Cierre del incumplimiento

En aquellos casos en los que el incumplimiento no pueda corregirse de forma inmediata, podrá iniciarse un proceso formal de solicitud de excepción, conforme a lo establecido en este procedimiento.

Detección de incumplimientos

Los incumplimientos de las Políticas IT podrán detectarse mediante diferentes mecanismos de control establecidos dentro del ecosistema tecnológico de APB.

La detección podrá realizarse de forma automática o manual, dependiendo de la naturaleza de la política y de las herramientas disponibles. Siempre que sea posible, se priorizará la detección automatizada, con el objetivo de mejorar la eficiencia operativa, reducir errores humanos y garantizar controles continuos.

Detección automática 

Siempre que sea técnicamente posible, la detección y registro de los incumplimientos deberá realizarse de forma automática mediante herramientas corporativas. 

Entre los mecanismos de detección automatizada podrán incluirse, entre otros:

Validaciones en pipelines CI/CD

Herramientas de análisis de calidad de código

Herramientas de seguridad (SAST, SCA, escáneres de vulnerabilidades, etc.)

Controles automáticos de configuración de infraestructuras

Herramientas de monitorización

Controles de gestión de costes cloud

Validaciones de arquitectura o cumplimiento técnico

Controles sobre configuración de bases de datos o acceso a datos

La automatización permite:

Detectar incumplimientos de forma temprana

Reducir errores humanos

Garantizar controles continuos

Facilitar la trazabilidad y auditoría

Por este motivo, los equipos de SSI promoverán la automatización progresiva de los controles de cumplimiento siempre que sea viable técnicamente.

Los incumplimientos podrán detectarse automáticamente mediante herramientas o mecanismos técnicos integrados en las plataformas corporativas. Entre los mecanismos de detección automatizada se incluyen, entre otros:

Controles de desarrollo y calidad de software

Validaciones en pipelines CI/CD

Quality Gates de herramientas de análisis de código

Validaciones de versionado o estructura de repositorios

Controles de dependencias y librerías

Análisis de vulnerabilidades en código o dependencias

Controles de seguridad

Escáneres de vulnerabilidades

Herramientas SAST / DAST / SCA

Controles de configuración segura

Sistemas de monitorización de seguridad

Controles de arquitectura y estándares tecnológicos

Validaciones automáticas de arquitectura

Reglas de uso de frameworks o componentes autorizados

Validaciones de integración entre sistemas

Controles de infraestructura y operación

Monitorización de configuraciones de sistemas

Validaciones de infraestructura como código

Controles de despliegue en entornos operativos

Controles de gestión de datos

Validaciones de configuración de bases de datos

Controles de acceso a datos

Validaciones de cumplimiento de políticas de gestión de datos

Controles de uso de recursos tecnológicos

Herramientas de control de costes cloud

Monitorización de consumo de servicios tecnológicos

Validaciones de uso de recursos SaaS o plataformas cloud

Cuando un mecanismo automático detecte un incumplimiento, deberá generarse un registro formal del mismo, preferentemente de forma automática en la herramienta corporativa de seguimiento.

Detección manual

Cuando la detección automática no sea posible o resulte insuficiente, los incumplimientos podrán identificarse mediante revisiones manuales realizadas por los equipos responsables.

Entre los mecanismos de detección manual se incluyen:

Revisiones técnicas de arquitectura

Revisiones de seguridad

Revisiones de cumplimiento de políticas IT

Auditorías internas o externas

Revisiones operativas de sistemas

Revisiones de uso de recursos tecnológicos

Revisiones de cumplimiento de estándares técnicos

Cuando se identifique un incumplimiento mediante un proceso manual, este deberá registrarse igualmente en el sistema de seguimiento definido por la organización, garantizando su correcta trazabilidad.

En estos casos, el incumplimiento deberá registrarse manualmente en el sistema de seguimiento definido por la organización, garantizando igualmente:

La trazabilidad del incumplimiento

La asignación de responsables

El seguimiento hasta su resolución

Notificación de incumplimientos

Cualquier miembro de los equipos de SSI o proveedor autorizado que identifique un posible incumplimiento de una Política IT deberá notificarlo conforme a este procedimiento.

La notificación deberá incluir, siempre que sea posible:

Identificación del sistema o servicio afectado

Política o norma incumplida

Descripción del incumplimiento detectado

Evidencias disponibles

Fecha de detección

Una vez notificado, el incumplimiento deberá registrarse formalmente para su análisis y gestión.

Clasificación de incumplimientos

Con el objetivo de facilitar la priorización, seguimiento y resolución de los incumplimientos de las Políticas IT, estos podrán clasificarse en distintos niveles de criticidad en función de su impacto potencial en la organización.

La clasificación se realizará considerando factores como:

Impacto en la seguridad de la información

Impacto en la disponibilidad o estabilidad de los sistemas

Impacto en la integridad de los datos

Impacto económico o de costes tecnológicos

Impacto en la arquitectura o sostenibilidad tecnológica

Exposición al incumplimiento normativo o regulatorio

La siguiente tabla establece una referencia para la clasificación de los incumplimientos:

La clasificación de criticidad podrá utilizarse para:

Priorizar las acciones de corrección

Definir el nivel de seguimiento requerido

Facilitar la gestión del riesgo tecnológico

Establecer criterios de escalado

Apoyar procesos de auditoría y reporting

La clasificación deberá asignarse en el momento del registro del incumplimiento y podrá revisarse durante su análisis si se identifican nuevos elementos de impacto o riesgo.

Registro y evidencias de incumplimientos

El registro de incumplimientos tiene como finalidad garantizar la trazabilidad completa de las desviaciones respecto a las Políticas IT de APB, así como asegurar su correcta gestión hasta su resolución.

El registro formal de los incumplimientos permite:

Garantizar la trazabilidad de las desviaciones respecto a las políticas definidas.

Evitar la existencia de incumplimientos sin seguimiento o sin responsable asignado.

Facilitar la asignación clara de responsabilidades para su análisis y corrección.

Prevenir la generación de registros duplicados.

Permitir la validación independiente del cierre.

Facilitar procesos de auditoría, control interno y reporting.

Todo incumplimiento detectado deberá quedar registrado formalmente en la herramienta corporativa de seguimiento definida por Sistemas de Información (actualmente Jira).

Los registros de incumplimientos deberán conservarse durante un mínimo de 1 año, o el periodo que establezca la normativa interna o los marcos regulatorios aplicables.

Registro del incumplimiento

Cuando se detecte un incumplimiento, deberá generarse un registro formal que permita su seguimiento. El registro deberá incluir, como mínimo:

Cada incumplimiento deberá registrarse una única vez en el sistema de seguimiento. Cuando un mecanismo automático detecte un incumplimiento, deberá comprobar previamente si ya existe un registro abierto asociado al mismo incumplimiento.

En caso de existir un registro activo:

No se generará un nuevo registro

El incumplimiento continuará gestionándose en el registro existente

Este mecanismo permite evitar:

Duplicidad de registros

Pérdida de trazabilidad histórica

Inflado artificial de indicadores de incumplimiento

Un incumplimiento se considerará activo mientras no haya sido corregido y validado conforme a lo establecido en este procedimiento.

Generación automática de registros

Cuando el incumplimiento sea detectado mediante mecanismos automatizados, el sistema podrá generar automáticamente el registro correspondiente en la herramienta de seguimiento.

En estos casos, el registro podrá incluir información técnica obtenida directamente de las herramientas de detección, tales como:

Identificador del sistema o servicio

Repositorio o componente afectado

Entorno afectado

Métricas detectadas

Valores medidos y umbrales definidos

Evidencias técnicas (logs, informes de análisis, etc.)

La generación automática de registros permite mejorar la rapidez de detección, la precisión de la información registrada y la trazabilidad del proceso.

Evidencias del incumplimiento

Cada registro de incumplimiento deberá incluir evidencias suficientes que permitan verificar la existencia del incumplimiento detectado. Estas evidencias podrán incluir, entre otros:

Informes de herramientas de análisis

Resultados de escáneres de seguridad

Resultados de análisis de calidad de código

Logs de sistemas o pipelines

Capturas de configuraciones

Informes de auditoría

Documentación técnica

Las evidencias deberán asociarse al registro del incumplimiento para facilitar su análisis y revisión.

Estados del proceso de gestión

Los registros de incumplimientos deberán seguir un flujo de estados que permita su correcta gestión y seguimiento.

El flujo mínimo de estados deberá contemplar:

Incumplimiento detectado

En análisis

En corrección

Pendiente de validación

Validado y cerrado

Excepción aprobada – pendiente de corrección

Este flujo permitirá garantizar el seguimiento del incumplimiento desde su detección hasta su resolución definitiva.

Principio de control y auditoría

Todo incumplimiento deberá cumplir los siguientes principios:

Estar registrado formalmente.

Disponer de evidencias verificables.

Tener responsable asignado.

Mantener un estado trazable durante todo su ciclo de vida.

Requerir validación independiente antes de su cierre.

No podrá considerarse resuelto ningún incumplimiento que no haya sido verificado y validado por el equipo responsable de su validación, conforme a los roles definidos en este procedimiento

Escalado, seguimiento, corrección y cierre

Una vez registrado un incumplimiento de una Política IT, deberá iniciarse un proceso de análisis, seguimiento y corrección hasta su resolución o hasta la aprobación formal de una excepción.

El objetivo de este proceso es garantizar que los incumplimientos:

Sean analizados de forma adecuada

Dispongan de acciones correctivas definidas

Sean corregidos en un plazo razonable

Mantengan trazabilidad completa

Cuenten con validación independiente antes de su cierre

Análisis del incumplimiento

Una vez registrado el incumplimiento, el responsable del sistema o servicio afectado, junto con el equipo técnico correspondiente, deberá analizar:

La naturaleza del incumplimiento

La política IT afectada

El impacto potencial en seguridad, operación, costes o estabilidad

La causa raíz del incumplimiento

Las acciones necesarias para su corrección

En función de la naturaleza del incumplimiento, podrán participar en el análisis otros equipos SSI.

Definición y ejecución de acciones correctivas

Tras el análisis del incumplimiento, el equipo responsable del sistema deberá definir un plan de corrección que permita resolver la desviación respecto a la política IT.

Este plan podrá incluir, entre otras acciones:

Modificación de configuraciones técnicas

Corrección de código o componentes

Actualización de configuraciones de seguridad

Cambios en arquitectura o integraciones

Ajustes en consumo de recursos tecnológicos

Actualización de documentación técnica

Adopción de herramientas o controles adicionales

Las acciones correctivas deberán ejecutarse dentro del plazo establecido, teniendo en cuenta la criticidad del incumplimiento y su impacto potencial.

Seguimiento del incumplimiento

Mientras el incumplimiento permanezca activo, deberá mantenerse en seguimiento dentro del sistema de registro definido por la organización.

Durante este seguimiento se deberá garantizar:

Actualización del estado del incumplimiento

Seguimiento de las acciones correctivas definidas

Revisión periódica de incumplimientos abiertos

Visibilidad para los equipos responsables

En caso de incumplimientos de alta criticidad o impacto relevante, los equipos de Ciberseguridad, Arquitectura u otros podrán solicitar revisiones específicas o seguimiento reforzado.

Escalado de incumplimientos

Podrá iniciarse un proceso de escalado interno cuando un incumplimiento:

No sea corregido dentro del plazo previsto

Tenga un impacto relevante en seguridad, operación o costes

Afecte a sistemas críticos

Suponga un riesgo significativo para la organización

Solicite una excepción temporal

El escalado podrá implicar la intervención de:

Jefes de departamentos SSI

Arquitectura

Ciberseguridad

Dirección de SSI

El objetivo del escalado es priorizar la resolución del incumplimiento y asegurar la adopción de las medidas necesarias para mitigar el riesgo.

Validación de la corrección

Una vez ejecutadas las acciones correctivas, el equipo responsable deberá actualizar el registro del incumplimiento y aportar las evidencias de la corrección realizada.

Posteriormente se realizará una validación independiente, que confirmará que el incumplimiento ha sido efectivamente resuelto. Esta validación será realizada por el equipo correspondiente en función de la naturaleza del incumplimiento.

La validación independiente garantiza la segregación de funciones y la fiabilidad del proceso de cierre.

Cierre del incumplimiento

Un incumplimiento solo podrá considerarse cerrado cuando:

Se haya ejecutado la acción correctiva correspondiente

Existan evidencias documentadas de la corrección

Se haya realizado la validación independiente

Se haya actualizado el estado del registro correspondiente

En caso de que el incumplimiento no pueda corregirse en el plazo establecido, deberá iniciarse el procedimiento de gestión de excepciones, conforme a lo definido en el presente documento.

Herramienta y flujo

Con el objetivo de garantizar la trazabilidad, control y seguimiento centralizado de los incumplimientos de las Políticas IT, todos los incumplimientos deberán registrarse en una herramienta corporativa de gestión.

A estos efectos, Jira Service Management (JSM) se establece como el sistema de referencia para el registro, seguimiento y cierre de los incumplimientos.

Registro y control centralizado

Todo incumplimiento detectado deberá registrarse en Jira Service Management, donde se gestionará su ciclo completo, incluyendo:

Registro inicial del incumplimiento

Análisis y clasificación

Asignación de responsables

Seguimiento de acciones correctivas

Gestión de excepciones

Validación y cierre

El ticket registrado en JSM constituirá el registro único y oficial del incumplimiento, y deberá mantenerse actualizado en todo momento.

Gestión de acciones técnicas y desarrollo

Cuando la resolución de un incumplimiento requiera la ejecución de tareas técnicas gestionadas en herramientas de desarrollo, como Jira Software, se podrá crear un ticket técnico específico vinculado al incumplimiento original.

En estos casos:

El ticket en Jira Software tendrá como finalidad la ejecución técnica de la corrección

Deberá mantenerse una vinculación explícita entre ambos tickets

El progreso de la resolución deberá reflejarse en el ticket principal en JSM

El ticket técnico no sustituye al registro del incumplimiento, sino que actúa como soporte para su resolución.

Responsabilidad y cierre

El ticket de incumplimiento registrado en Jira Service Management será el elemento principal de control, y su cierre solo podrá realizarse cuando:

Se hayan ejecutado las acciones correctivas necesarias

Se disponga de evidencias de la corrección

Se haya realizado la validación independiente correspondiente

En ningún caso se considerará resuelto un incumplimiento únicamente por el cierre de un ticket técnico en herramientas de desarrollo.

Monitorización y cuadro de mando de incumplimientos

Con el objetivo de facilitar el seguimiento del cumplimiento de las Políticas IT y la gestión de los incumplimientos detectados, se deberán disponer de mecanismos de monitorización y visualización centralizada de los incumplimientos y excepciones activas.

Las herramientas corporativas utilizadas para el registro y seguimiento de incumplimientos (como Jira, PowerBI, Grafana u otras herramientas equivalentes) deberán permitir la generación de cuadros de mando o indicadores de cumplimiento.

Estos cuadros de mando deberán proporcionar, entre otros, los siguientes indicadores:

Número de incumplimientos abiertos por sistema o servicio.

Número de excepciones activas por sistema o activo tecnológico.

Distribución de incumplimientos por nivel de criticidad.

Evolución temporal de los incumplimientos detectados y corregidos.

Incumplimientos o excepciones que superen los plazos establecidos.

Asimismo, el sistema deberá permitir identificar de forma clara el estado de cumplimiento de cada activo tecnológico, mediante indicadores agregados o métricas de salud.

En particular, deberá existir un mecanismo que alerte cuando un sistema o activo tecnológico supere un número determinado de excepciones activas, ya que esta situación puede indicar un riesgo acumulado o un deterioro del cumplimiento de las Políticas IT.

Cuando se alcance o supere este umbral, los responsables de políticas o comité SSI podrán:

Iniciar un seguimiento específico del sistema afectado,

Requerir la elaboración de un plan de remediación, o

Evaluar la limitación o denegación de nuevas excepciones hasta reducir el número de incumplimientos existentes.

La definición de los umbrales y métricas utilizadas en estos cuadros de mando podrá ajustarse periódicamente en función de la evolución de las Políticas IT y de los mecanismos de control de la organización.

Excepciones

Como principio general, no se permite mantener sistemas, desarrollos, configuraciones o despliegues que presenten incumplimientos de las Políticas IT de APB. Los incumplimientos detectados deberán corregirse conforme al procedimiento establecido en este documento.

Únicamente en situaciones excepcionales, justificadas y debidamente documentadas, podrá autorizarse temporalmente la existencia de un incumplimiento mediante un procedimiento formal de solicitud de excepción.

La concesión de una excepción implica la aceptación explícita y documentada del riesgo asociado al incumplimiento, así como el compromiso de aplicar medidas compensatorias y de resolver el incumplimiento en un plazo definido.

Las excepciones deberán gestionarse conforme a los principios de gestión del riesgo establecidos en el Esquema Nacional de Seguridad (ENS) y en ISO/IEC 

27001.

Sin la autorización formal correspondiente, cualquier mecanismo de control técnico que impida la implantación o despliegue de un sistema deberá mantener el bloqueo activo.

Las excepciones constituyen un mecanismo extraordinario, y no deberán utilizarse como sustituto del cumplimiento de las Políticas IT.

Registro de la solicitud de excepción

Toda solicitud de excepción deberá registrarse formalmente en la herramienta corporativa de seguimiento (actualmente Jira), asociada al incumplimiento correspondiente.

La solicitud deberá incluir, como mínimo:

Cuando el incumplimiento tenga impacto en seguridad de la información, el riesgo deberá registrarse en el inventario corporativo de riesgos.

No se evaluará ninguna solicitud de excepción que no esté debidamente documentada.

Condiciones de las excepciones

Toda excepción concedida deberá cumplir las siguientes condiciones:

Ser temporal

Tener fecha de inicio

Tener fecha límite de corrección

Incluir plan de remediación

Disponer de medidas compensatorias

Mantenerse en seguimiento hasta su resolución

Las excepciones no podrán concederse de forma indefinida.

Si la fecha compromiso de resolución expira sin que el incumplimiento haya sido corregido:

El incumplimiento volverá a considerarse activo

Podrán reactivarse los mecanismos de control o bloqueo

Será necesario tramitar una nueva solicitud de excepción completa

Flujo de aprobación

La concesión de una excepción requerirá una evaluación y aprobación escalonada, garantizando tanto la validación de negocio como la evaluación técnica del riesgo asociado.

Con carácter general, toda excepción deberá contar con tres aprobaciones obligatorias:

Cuando el incumplimiento tenga impacto en seguridad de la información, deberá incorporarse la evaluación del CISO.

En los casos en los que una política disponga de un único responsable técnico, la segunda validación técnica deberá ser realizada por el equipo de Ciberseguridad, Arquitectura, siendo aprobada por el CISO o CTO, en función de la naturaleza del incumplimiento.

La excepción solo podrá considerarse aprobada cuando todos los niveles de aprobación hayan emitido su conformidad. El rechazo por cualquiera de los roles implicará la denegación de la excepción. Ninguna excepción podrá ser aprobada exclusivamente por responsables del área solicitante.

En ausencia de la aprobación formal correspondiente, los mecanismos técnicos de control deberán mantener el bloqueo del sistema o despliegue afectado.

Seguimiento de excepciones

Las excepciones aprobadas deberán mantenerse en seguimiento dentro del sistema de registro correspondiente.

Durante este seguimiento se verificará:

el cumplimiento de las medidas compensatorias definidas

El progreso del plan de corrección

El cumplimiento de la fecha compromiso establecida

El incumplimiento asociado a una excepción no podrá considerarse cerrado hasta que:

Se haya corregido el incumplimiento original

Se haya realizado la validación independiente de la corrección

Criterios de valoración de excepciones

Evaluación de excepciones

Las excepciones constituyen un mecanismo extraordinario que permite aceptar temporalmente un incumplimiento de las Políticas IT cuando su corrección inmediata no es viable sin generar un impacto mayor para la organización.

La concesión de una excepción implica la aceptación explícita del riesgo asociado, por lo que deberá estar debidamente justificada, documentada y aprobada conforme al proceso establecido en este procedimiento.

Antes de conceder una excepción, los responsables de su evaluación deberán analizar:

La naturaleza y el impacto del incumplimiento

Los riesgos asociados a mantener temporalmente la desviación

La existencia de medidas compensatorias

La viabilidad de un plan de corrección en un plazo razonable

La aprobación de excepciones deberá basarse en criterios objetivos de riesgo, impacto y necesidad operativa, evitando su uso como mecanismo para compensar deficiencias en la planificación, desarrollo o gestión, entre otras.

Preguntas orientativas para la evaluación de excepciones

Durante el proceso de evaluación, los responsables de aprobación podrán considerar, entre otras, las siguientes cuestiones:

Evaluación de negocio 

¿Existe una necesidad operativa real que justifique la excepción?

¿Qué impacto tendría para el negocio no conceder la excepción?

¿Existe un plan claro para resolver el incumplimiento dentro del plazo establecido?

Evaluación de seguridad 

¿Qué riesgos introduce el incumplimiento en términos de confidencialidad, integridad o disponibilidad de la información?

¿Existen medidas compensatorias suficientes para mitigar el riesgo durante el periodo de excepción?

¿El riesgo asumido es aceptable para la organización durante el tiempo solicitado?

Evaluación técnica

¿La excepción puede generar deuda técnica o comprometer la arquitectura tecnológica?

¿Existen alternativas técnicas viables que eviten el incumplimiento?

¿El plan de remediación es técnicamente realista y ejecutable en el plazo definido?

Criterios para la concesión de excepciones

Las solicitudes de excepción deberán estar basadas en circunstancias excepcionales, justificadas y debidamente documentadas, reservándose exclusivamente para situaciones verdaderamente excepcionales, en las que la corrección inmediata del incumplimiento no sea viable sin generar un impacto mayor para la organización. 

Incidentes críticos que requieran actuaciones urgentes.

Dependencias externas no controlables por la organización

Situaciones de continuidad del servicio.

Incompatibilidades técnicas debidamente justificadas.

Creación o modificación sustancial de una política.

En todos los casos, la concesión de una excepción requerirá una evaluación del riesgo asociado, la definición de medidas compensatorias y el establecimiento de un plan de corrección con una fecha límite de resolución

Entre otras, podrán considerarse las siguientes circunstancias:

Incidentes críticos que requieran actuaciones urgentes. Cuando sea necesario realizar acciones inmediatas para restaurar la disponibilidad del servicio o mitigar un incidente grave, y el cumplimiento estricto de las Políticas IT no pueda aplicarse temporalmente.

Dependencias externas no controlables por la organización. Cuando el incumplimiento derive de limitaciones o dependencias de terceros no gestionable por APB (fabricantes, servicios externos o plataformas), siempre que el riesgo esté evaluado y existan medidas compensatorias.

Situaciones de continuidad del servicio. Cuando la aplicación estricta de la política pudiera comprometer la continuidad del servicio o la operativa crítica de la organización.

Incompatibilidades técnicas debidamente justificadas. Cuando exista una incompatibilidad técnica real entre la política definida y la tecnología utilizada, debidamente analizada y documentada por los equipos técnicos responsables.

Creación o modificación sustancial de una política IT. Cuando se trate de una política recientemente creada o modificada de forma significativa y sea necesario un periodo razonable de adaptación para los sistemas afectados.

Criterios de denegación de excepciones

La concesión de excepciones basadas en causas evitables debilita el marco de control tecnológico y aumenta el riesgo operativo, por lo que deberá evitarse de forma sistemática. 

Las excepciones no constituyen un mecanismo para acelerar despliegues ni para compensar deficiencias en la planificación/ejecución de proyectos o posponer el cumplimiento de las Políticas IT. No se considerarán válidas las solicitudes de excepción basadas en causas derivadas de falta de planificación, desconocimiento o incumplimiento evitable de las Políticas IT.

La relación de situaciones descrita a continuación no tiene carácter exhaustivo.
Cualquier solicitud de excepción basada en causas evitables o derivadas de una planificación inadecuada podrá ser rechazada por el responsable correspondiente. No se aceptarán como justificación para la concesión de una excepción, entre otras, las siguientes situaciones.

Falta de capacidades técnicas o conocimiento especializado. Los equipos responsables deberán garantizar que disponen de las capacidades técnicas necesarias para cumplir las Políticas IT. No se aceptarán excepciones motivadas por falta de conocimiento, experiencia o dificultad técnica percibida para aplicar las políticas.

Problemas de planificación o gestión del proyecto. No se aceptarán excepciones derivadas de deficiencias en la planificación, estimación o gestión del proyecto, incluyendo detección tardía del incumplimiento, falta de tiempo para realizar correcciones, necesidad de rehacer desarrollos o retrasos acumulados.

Compromisos de fechas o presión operativa. Los compromisos de entrega, la presión por realizar despliegues en una fecha determinada o retrasos en el calendario del proyecto no justifican el incumplimiento de las Políticas IT.

Falta de recursos o tiempo. La falta de recursos técnicos o de tiempo asignado al proyecto no constituye una justificación válida. El cumplimiento de las Políticas IT forma parte del desarrollo y operación de los sistemas.

Incumplimientos evitables. No se aceptarán excepciones cuando el incumplimiento podría haberse evitado aplicando correctamente las políticas desde las fases iniciales de diseño y planificación.

Prácticas históricas o precedentes. Las Políticas IT vigentes deberán aplicarse con independencia de prácticas anteriores, decisiones adoptadas en proyectos previos o ausencia histórica de incidentes.

Minimización subjetiva del riesgo. No se aceptarán excepciones basadas en valoraciones informales del riesgo. La evaluación del riesgo deberá realizarse conforme a los procedimientos de gestión de riesgos definidos por la organización.

Transferencia de responsabilidad a terceros. Las decisiones de proveedores, configuraciones heredadas o decisiones de otros equipos no eximen al equipo responsable del sistema de cumplir las Políticas IT.

Argumentos basados exclusivamente en costes. La existencia de costes adicionales asociados a la corrección del incumplimiento no constituye una justificación válida.

Adquisición de soluciones no conformes. No se aceptarán excepciones derivadas de la adquisición de productos o servicios que no cumplen las Políticas IT cuando dicha situación podría haberse evitado mediante una evaluación técnica previa.

Falta de adaptación a cambios de políticas. No se aceptarán excepciones basadas en la falta de adaptación a políticas actualizadas cuando haya existido un plazo razonable para su implementación.

Cuestionamiento de las políticas vigentes. Si se considera que una política es inadecuada o necesita actualización, deberá solicitarse formalmente su revisión. Esta circunstancia no justifica una excepción mientras la política siga vigente.

Renovación de excepciones o falta de resolución tras una excepción previa. No se aceptarán nuevas excepciones cuando ya se haya concedido previamente un plazo razonable para corregir el incumplimiento.

Aprobaciones unilaterales o desacuerdos entre áreas. Las excepciones no pueden aprobarse unilateralmente por equipos de producto o responsables funcionales. En caso de desacuerdo, prevalecerá la evaluación de los equipos técnicos responsables de las Políticas IT.

Excepción de Emergencia (Fast-track). 

En situaciones excepcionales en las que sea necesario restaurar de forma inmediata la disponibilidad de un servicio crítico o mitigar un incidente grave, podrá aplicarse un procedimiento de excepción de emergencia (Fast-track).

Este procedimiento permite autorizar temporalmente un incumplimiento de una Política IT cuando el cumplimiento estricto de la misma pudiera retrasar la recuperación del servicio o agravar el impacto del incidente.

Condiciones de aplicación

El procedimiento de excepción de emergencia solo podrá utilizarse cuando concurran simultáneamente las siguientes circunstancias:

Existencia de un incidente crítico o degradación grave del servicio.

Necesidad de realizar una actuación inmediata para restaurar la disponibilidad o estabilidad del sistema.

Imposibilidad de seguir el procedimiento estándar de solicitud de excepción sin retrasar la resolución del incidente.

Este mecanismo deberá utilizarse únicamente cuando sea estrictamente necesario y no podrá emplearse como sustituto del procedimiento normal de gestión de excepciones.

Autorización de la excepción de emergencia

La excepción podrá ser autorizada vía mail por el responsable de la política IT afectada o por el responsable técnico designado para su validación.

Esta autorización permitirá realizar el despliegue o actuación técnica necesaria para resolver el incidente.

Regularización posterior

Toda excepción concedida mediante el procedimiento de emergencia deberá regularizarse posteriormente en el sistema de gestión de incumplimientos (Jira).

En un plazo máximo de 24 a 48 horas desde la actuación de emergencia deberá registrarse:

El incumplimiento asociado

La justificación de la actuación realizada

La autorización recibida

Las evidencias del incidente o situación que motivó la excepción

El plan de corrección o remediación, cuando proceda

Una vez registrado el ticket, el incumplimiento deberá continuar su gestión conforme al procedimiento habitual de gestión de incumplimientos y excepciones definido en este documento.

Seguimiento

El uso reiterado del procedimiento de excepción de emergencia para un mismo sistema o tipo de actuación podrá ser objeto de revisión específica por parte de los Sistemas de Información.

Criterio Legacy y Compliance

Cuando se cree una nueva Política IT o se realice una modificación sustancial de una política existente, podrá definirse una línea base inicial de cumplimiento con el objetivo de identificar la situación de los sistemas existentes en el momento de la entrada en vigor de la política.

Esta línea base permitirá distinguir entre:

Legacy - Sistemas o configuraciones existentes. Aquellos elementos que ya estaban implantados antes de la entrada en vigor de la política o de su modificación.

En estos casos podrá evaluarse la posibilidad de conceder una excepción temporal, siempre que:

El riesgo asociado haya sido evaluado,

Existan medidas compensatorias cuando sea necesario, y

Se establezca un plan de adaptación o remediación.

La existencia de elementos legacy no implica la concesión automática de una excepción, sino que deberá evaluarse caso por caso conforme al presente procedimiento.

La definición de una línea base permitirá facilitar la transición progresiva hacia el cumplimiento de las políticas, evitando impactos innecesarios en sistemas existentes y garantizando al mismo tiempo que las nuevas implantaciones se ajusten plenamente a los estándares definidos por la organización.

Compliance - Nuevos desarrollos, implantaciones o modificaciones. Cualquier nuevo sistema, desarrollo, integración o modificación relevante deberá cumplir íntegramente la política vigente desde su inicio.

En estos casos, cualquier incumplimiento deberá gestionarse mediante el procedimiento habitual de gestión de incumplimientos y excepciones definido en este documento.

Principio de no empeoramiento (Legacy)

Cuando existan sistemas, configuraciones o componentes identificados como legacy en la línea base definida para una política, cualquier modificación, evolución o intervención sobre dichos sistemas deberá evitar introducir nuevos incumplimientos o agravar los existentes.

En particular:

No deberán incorporarse nuevas desviaciones respecto a las Políticas IT vigentes.

Las modificaciones o evoluciones del sistema deberán mantener o mejorar el nivel de cumplimiento existente, siempre que sea técnicamente viable.

Cuando una intervención técnica permita corregir total o parcialmente un incumplimiento existente, se deberá evaluar la oportunidad de realizar dicha corrección.

Este principio tiene como objetivo evitar la acumulación o agravamiento de incumplimientos en sistemas existentes, favoreciendo una transición progresiva hacia el cumplimiento de las Políticas IT.

La existencia de elementos legacy no exime a los equipos responsables de planificar su progresiva adaptación a las políticas vigentes, conforme a las prioridades y planes de evolución tecnológica de la organización.

Principio de no acumulación de excepciones

Las excepciones concedidas deberán evaluarse no solo de forma individual, sino también considerando su impacto acumulado sobre el sistema o servicio afectado.

La existencia de múltiples excepciones activas sobre un mismo sistema, componente o servicio puede generar un riesgo tecnológico, operativo o de seguridad superior al evaluado para cada excepción de forma individual.

Por este motivo, durante el proceso de evaluación de una nueva solicitud de excepción, los responsables de técnicos podrán considerar:

El número de excepciones activas existentes en el sistema o servicio afectado

La naturaleza de los incumplimientos asociados

El impacto conjunto en seguridad, estabilidad, mantenibilidad o costes tecnológicos

Cuando se identifique una acumulación significativa de excepciones, podrá denegarse la solicitud o requerirse la definición de un plan de remediación global que permita reducir el riesgo acumulado. Los sistemas que mantengan múltiples excepciones activas podrán ser objeto de seguimiento específico con el objetivo de garantizar la progresiva corrección de los incumplimientos existentes.

Tiempos de resolución y gestión de excepciones

Con el objetivo de facilitar la priorización y el seguimiento de los incumplimientos de las Políticas IT, se establecen los siguientes plazos orientativos de resolución, en función de la criticidad del incumplimiento.

Estos plazos podrán ajustarse en función de la naturaleza del sistema afectado, la complejidad técnica de la corrección o el impacto operativo asociado.

Los plazos indicados tienen carácter orientativo y se utilizarán como referencia para:

Priorizar la resolución de incumplimientos

Facilitar el seguimiento por parte de los equipos responsables

Apoyar los procesos de control interno y auditoría

Superación de los plazos establecidos

Cuando un incumplimiento supere los plazos recomendados sin haber sido corregido, podrá iniciarse un proceso de escalado, conforme a lo establecido en el presente procedimiento.

Asimismo, cuando una excepción alcance su fecha límite sin que el incumplimiento haya sido corregido, el incumplimiento volverá a considerarse activo, pudiendo requerirse:

La corrección inmediata del incumplimiento

La aplicación de controles adicionales

O la evaluación de nuevas medidas de mitigación del riesgo

Los incumplimientos clasificados como críticos o relacionados con seguridad de la información podrán requerir plazos de corrección más restrictivos, en función de la evaluación de riesgo realizada por el equipo de Ciberseguridad.

Especificaciones según políticas concretas

El presente procedimiento establece el marco general para la gestión de los incumplimientos de las Políticas IT del Port de Barcelona, aplicable a cualquier política definida dentro del ámbito de SSI.

No obstante, determinadas políticas pueden requerir mecanismos específicos de detección, validación o gestión de incumplimientos, debido a la naturaleza técnica de los controles aplicados o a las herramientas utilizadas para su supervisión.

Por este motivo, en el presente apartado se recogen especificaciones adicionales aplicables a determinadas políticas concretas, que complementan lo establecido en este procedimiento general.

Estas especificaciones podrán incluir, entre otros aspectos:

Mecanismos específicos de detección automática de incumplimientos

Reglas técnicas de validación o bloqueo

Herramientas corporativas utilizadas para el control del cumplimiento

Flujos específicos de registro o seguimiento

Métricas o umbrales de cumplimiento definidos por la política correspondiente

Las especificaciones incluidas en este apartado no sustituyen el procedimiento general, sino que lo complementan para casos particulares.

Este apartado podrá ampliarse progresivamente para incorporar especificaciones adicionales asociadas a nuevas políticas o a la evolución de las políticas existentes.

QA en desarrollo a medida Docks

Detección Automática

Los incumplimientos serán identificados automáticamente durante la ejecución del pipeline CI/CD gestionado en Jenkins y SonarQube. Si se detectan incumplimientos en PRE o PRO el despliegue quedará bloqueado hasta completar la validación.

Registro automático del Incumplimiento

Tras la identificación automática del incumplimiento, el sistema creará automáticamente un ticket Jira que incluirá como mínimo:

Los incumplimientos críticos deberán registrarse también en el Registro de Riesgos corporativo.

Se considerará el ticket como “incumplimiento activo” hasta su resolución validada a través de los mecanismos automáticos.

Cuando se detecte un incumplimiento por primera vez:

Se generará automáticamente un ticket en Jira.

El ticket incluirá información técnica obtenida desde Jenkins y SonarQube.

El estado inicial será: Incumplimiento Detectado.

Asignado al Product Owner responsable de la aplicación según información en CMDB.

La responsabilidad inicial de análisis y corrección recaerá en el equipo de desarrollo.

Cuando el equipo considere corregido el incumplimiento, solicitará ejecutar de nuevo pipeline.

Solo tras esta validación independiente podrá cambiarse el estado a Validado y Cerrado. Sin esta validación formal el ticket no podrá cerrarse y el incumplimiento se considerará activo.

Excepciones 

Como principio general, no se permite el despliegue de desarrollos que presenten incumplimientos de la Política de QA en los entornos PRE o PRO. Únicamente en situaciones excepcionales, puntuales y debidamente justificadas, podrá considerarse la posibilidad de realizar un despliegue bajo un procedimiento específico y extraordinario.

Sin la autorización formal correspondiente, el despliegue permanecerá bloqueado de manera indefinida.

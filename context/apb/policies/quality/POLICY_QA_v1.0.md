# Políticas_de_QA_APB_v1(1)

Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 1 de 21 
 
 
Políticas de cumplimiento APB  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Política QA APB  
Requisitos técnicos para desarrollos y 
despliegues desarrollos Docks 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 2 de 21 
 
 
Políticas de cumplimiento APB  
Historial de revisiones 
 
Versión 
Descripción  
Autor 
Acción  
Fecha  
01.00 
Definición  
Veronica Cartagena 
Creación 
26-02-2026 
 
 
 
 
 
 
 
 
 
 
 
 
Débora Martin (CTO) 
Albert Prats (CISO) 
Aprobación 
1-04-2026 
 
 
 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 3 de 21 
 
 
Políticas de cumplimiento APB  
ÍNDICE 
 
1. 
Introducción ............................................................................................................... 4 
1.

1. 
Objetivo .................................................................................................................. 4 
1.

2. 
Ámbito de aplicación .............................................................................................. 4 
1.

3. 
Resumen Ejecutivo .................................................................................................. 5 
2. 
Definición de Código Nuevo (Compliance) y Código Existente (Línea Base Legacy) ..... 6 
3. 
Nivel de cumplimiento por entorno ............................................................................ 8 
4. 
Validaciones e implementación técnica....................................................................... 8 
4.

1. 
Validaciones Técnicas APB ...................................................................................... 8 
Authorize 9 
Bloques try/catch ................................................................................................................................... 10 
Uso de WebService ................................................................................................................................ 11 
Versionado de plantilla API/APP base ..................................................................................................... 12 
Documentación mínima ......................................................................................................................... 13 
Gestión de secretos ............................................................................................................................... 14 
Gestión de dependencias ....................................................................................................................... 16 
4.

2. 
SonarQube - Validaciones de Calidad y Seguridad ................................................. 16 
Blocker Severity Issues = 0 ..................................................................................................................... 17 
Cobertura mínima de pruebas (Coverage ≥ 60 %) .................................................................................. 17 
Maintainability Rating igual o superior a B ............................................................................................. 18 
Reliability Rating igual o superior a C ..................................................................................................... 18 
Security Rating igual o superior a C ........................................................................................................ 19 
4.

3. 
Jenkins - Criterios de implementación ................................................................... 20 
 
 
 
 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 4 de 21 
 
 
Políticas de cumplimiento APB  
1. Introducción 
1.

1. Objetivo 
El presente documento establece las políticas de cumplimiento técnico aplicables a los desarrollos y 
despliegues realizados en el marco tecnológico del Port de Barcelona (APB) dentro del framework de 
Docks.  
El objetivo fundamental del documento que se presenta a continuación es definir las políticas de 
cumplimiento técnico aplicables a todos los desarrollos sobre el framework de Docks. 
Estas políticas forman parte del Ciclo de Vida Seguro del Software (SSDLC) del Port de Barcelona y 
contribuyen al cumplimiento del Esquema Nacional de Seguridad (ENS), especialmente en lo relativo a 
control de cambios, seguridad del software, gestión de riesgos y trazabilidad. 
El objetivo es garantizar: 
- 
Calidad de código 
- 
Seguridad 
- 
Trazabilidad 
- 
Mejor mantenibilidad 
- 
Estabilidad en entornos productivos  
- 
Disminución progresiva de deuda técnica 
- 
Evolución tecnológica sostenible 
- 
Reducción de incidencias en producción 
El cumplimiento de estas políticas es obligatorio para todos los equipos internos y proveedores que 
desarrollen o mantengan software dentro del framework Docks. La supervisión del cumplimiento 
corresponde a los equipos de Arquitectura, Ciberseguridad y DevOps cada uno dentro de su ámbito de 
responsabilidad. 
Dado que la tecnología, las herramientas corporativas y las necesidades operativas evolucionan de 
manera continua, este documento debe entenderse como un documento vivo, sujeto a revisión y 
actualización periódica. Las políticas aquí descritas podrán modificarse o ampliarse en función de nuevas 
directrices, mejoras tecnológicas o requerimientos detectados por los equipos de desarrollo y operación. 
Su actualización se realizará mediante un proceso formal aprobado por Arquitectura y Ciberseguridad, 
garantizando trazabilidad y comunicación a todos los equipos afectados. Por este motivo, los usuarios 
deberán asegurarse de consultar siempre la versión vigente antes de iniciar cualquier proyecto o proceso 
de despliegue. 
1.

2. Ámbito de aplicación 
Este marco define los requisitos técnicos, las validaciones obligatorias y los criterios de calidad que deben 
cumplirse. 
Esta política aplica a:  
- 
Nuevos desarrollos. 
- 
Mantenimientos evolutivos, perfectivos y correctivos. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 5 de 21 
 
 
Políticas de cumplimiento APB  
- 
Evolutivos sobre sistemas existentes 
- 
APIs, microservicios y aplicaciones 
- 
Servicios desplegados en entornos TST, PRE y PRO 
- 
Pipelines gestionados mediante Jenkins 
- 
Proyectos sometidos a análisis de calidad mediante SonarQube 
- 
Equipos internos y proveedores externos que desarrollen o mantengan software dentro del 
framework Docks 
Se establecen dos modalidades de aplicación: 
Compliance → obligatorio y bloqueante. 
Legacy → informativo con plan de reducción de deuda técnica. 
Se considerará Legacy todo el código previo a la entrada en vigor de la política restrictiva (que no cumpla 
la normativa definida por APB, mientras que será Compliance todo el código nuevo desde la entrada en 
vigor y todo código previo que ya cumpla los requisitos establecidos.  
Los proyectos clasificados como Legacy deberán incluir un plan de transición hacia Compliance, con hitos 
y plazos concretos para la reducción de la deuda técnica. Aunque Compliance no puede transitar a un 
Legacy, un proyecto Legacy sí puede evolucionar a Compliance una vez que cumpla la normativa.  
La clasificación de un proyecto como Compliance o Legacy será determinada por Arquitectura en 
coordinación con Ciberseguridad, quedando registrada en Jira y en la CMDB.  
1.

3. Resumen Ejecutivo 
En la actualidad, todos los desarrollos son sometidos a un conjunto de validaciones técnicas y de seguridad 
que permiten conocer su nivel de calidad, identificar posibles riesgos y cuantificar la deuda técnica 
existente. Estas validaciones proporcionan visibilidad sobre el estado real del código y sirven como 
mecanismo de control para detectar deficiencias que puedan afectar a la estabilidad, la seguridad o la 
mantenibilidad del servicio. 
Hasta el momento, dicho proceso se ha aplicado de forma generalizada a todos los proyectos, 
independientemente de su naturaleza o antigüedad, permitiendo obtener información relevante, pero 
sin carácter restrictivo. Con el objetivo de elevar el estándar de calidad y asegurar que los nuevos 
desarrollos cumplan plenamente con las políticas definidas por la plataforma, se establece ahora un 
modelo más estricto para los servicios de nueva creación.  
Bajo este enfoque, los proyectos clasificados como Compliance deberán superar obligatoriamente todas 
las validaciones técnicas definidas en este documento, mientras que los servicios Legacy continuarán 
operando en modo permisivo durante un periodo de transición orientado a la reducción de deuda técnica. 
El modelo garantiza trazabilidad completa mediante Jenkins, SonarQube y Jira, permitiendo auditorías 
internas y externas. Cualquier desviación respecto a estas políticas requerirá un procedimiento formal de 
excepción, con evaluación de riesgos y aprobación escalonada. 
La supervisión del cumplimiento corresponde a los equipos de Arquitectura, Ciberseguridad y DevOps. 
Este marco permite disponer de un ecosistema de software más robusto, seguro y sostenible, reduciendo 
incidencias y facilitando la evolución futura de los sistemas. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 6 de 21 
 
 
Políticas de cumplimiento APB  
 
Para garantizar que los desarrollos del Port de Barcelona dentro del entorno Docks cumplen con 
estándares de calidad y seguridad, se aplican dos tipos principales de validaciones: 
1. Validaciones Técnicas APB 
Son controles básicos que todos los desarrollos deben respetar para asegurar coherencia dentro de la 
plataforma. Incluyen: 
- 
Seguridad y autorización: todos los servicios deben proteger sus operaciones mediante roles y 
permisos adecuados.  
- 
Buenas prácticas de código: evitar estructuras inseguras como try/catch que oculten errores y 
dificulten su detección, diagnóstico y corrección. 
- 
Uso de tecnologías homologadas: no se permite SOAP ni WebServices obsoletos; solo se autorizan 
tecnologías modernas como REST; Orientación a eventos en lugar de llamadas síncronas, etc… 
- 
Actualización tecnológica: los proyectos deben basarse en versiones recientes de las plantillas 
oficiales para garantizar compatibilidad y seguridad. Solo será aceptado en uso de las ultimes 2 
últimas versiones. 
- 
Documentación mínima obligatoria: cada servicio debe contar con documentación técnica y 
operativa básica.  
2. Validaciones de Calidad y Seguridad (SonarQube) 
Controlan la calidad global del código para reducir riesgos y garantizar su mantenibilidad: 
- 
Sin errores críticos: no se permite avanzar si existen incidencias graves (Blocker Issues = 0).  
- 
Pruebas suficientes: se requiere un mínimo de 60% de cobertura mediante tests automatizados. 
- 
Deuda técnica controlada: el proyecto debe alcanzar un nivel aceptable de mantenibilidad (≥ B). 
- 
Fiabilidad mínima: el código debe evitar defectos que puedan generar fallos en ejecución (≥ C). 
- 
Seguridad garantizada: el proyecto debe cumplir criterios mínimos de seguridad y no presentar 
vulnerabilidades graves (≥ C).  
Los desarrollos nuevos deben cumplir estas políticas de manera estricta (Compliance), mientras que los 
sistemas heredados (Legacy) pueden avanzar de forma más flexible, aunque siempre bajo seguimiento y 
con un plan de reducción de deuda técnica. 
Este marco permite al Port de Barcelona disponer de un ecosistema de software más robusto, seguro y 
sostenible, reduciendo incidencias y facilitando la evolución futura de sus sistemas. 
2. Definición de Código Nuevo (Compliance) y Código Existente (Línea 
Base Legacy) 
Se considera código nuevo todo aquel código que: 
- 
Se incorpora por primera vez al repositorio. 
- 
Forma parte de una nueva funcionalidad. 
- 
Es resultado de una modificación sustancial sobre código existente. 
- 
Ha sido añadido o modificado dentro del período de análisis definido en SonarQube. 
- 
Pertenece a nuevas clases, métodos o módulos creados. 
- 
Es resultado de refactorización que altera la lógica existente. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 7 de 21 
 
 
Políticas de cumplimiento APB  
En términos de análisis automático, el código nuevo corresponde al identificado por SonarQube como 
New Code dentro del periodo configurado (por ejemplo, desde la última versión o desde una fecha de 
referencia). 
Para dicho código nuevo se evaluarán las siguientes métricas mínimas: 
• 
Cobertura de código: debe ser mayor al 60%. 
• 
Porcentaje de líneas duplicadas: debe ser inferior al 3%. 
• 
Issues: no deben existir ningún tipo de issues. 
• 
Security Hotspots: sin ningún hostspost pendiente. 
Estos parametros estan definidos en Clean as you code methodology de SonarQube (Introduction | 
SonarQube Server 10.7 | Sonar Documentation) 
Se considera código existente o línea base Legacy todo aquel código que: 
- 
Ya formaba parte del repositorio antes de la entrada en vigor de la política. 
- 
No ha sido modificado en el período actual de desarrollo. 
- 
Pertenece a versiones anteriores del servicio. 
- 
Contiene deuda técnica histórica identificada. 
- 
Ha sido clasificado como Legacy por decisión organizativa. 
La línea base Legacy constituye el punto de partida técnico sobre el cual se construyen evolutivos y es el 
estado congelado de calidad del código en un momento determinado. 
Se utiliza para: 
- 
Evitar penalizar desarrollos nuevos por deuda histórica. 
- 
Medir exclusivamente la calidad del código añadido o modificado. 
- 
Controlar que no se incremente la deuda técnica existente. 
La línea base será definida: 
 
 
En la primera ejecución del pipeline bajo la nueva política. 
 
En la fecha de activación del proyecto como Compliance. 
Principio de NO Incremento de Deuda 
Aunque el código Legacy pueda contener deuda técnica histórica: 
- 
No se permite incrementar dicha deuda. 
- 
No se permite introducir nuevas vulnerabilidades. 
- 
No se permite degradar métricas existentes. 
La política se basa en los siguientes principios: 
- 
No se exige corrección inmediata sobre la deuda histórica 
- 
Sí se exige que todo código nuevo cumpla los estándares definidos y que cada evolución mejore 
progresivamente la calidad global del sistema. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 8 de 21 
 
 
Políticas de cumplimiento APB  
- 
Si se exige la planificación en un tiempo razonable de las correcciones de deuda técnica. 
3. Nivel de cumplimiento por entorno 
Entorno 
Nivel 
Compliance 
Legacy 
Comentario 
TST 
Permisivo 
No 
bloqueante 
No 
bloqueante 
Las validaciones se ejecutan siempre, pero en modo 
informativo. El propósito es facilitar iteraciones rápidas 
durante 
el 
desarrollo, 
sin 
restricciones 
fuertes, 
independientemente de la categoría del desarrollo. 
No se generan tickets Jira automáticos. 
PRE 
Restrictivo 
Bloqueante 
Informativo 
con 
seguimiento 
PRE actúa como entorno de validación completa.  
Los desarrollos Compliance deben cumplir todas las 
validaciones, en caso contrario el despliegue no se 
realizará. 
Los desarrollos Legacy pueden desplegar, pero sus 
incumplimientos quedan registrados en Jira de forma 
automática y deben ser gestionados conforme al plan de 
reducción de deuda técnica. 
PRO 
Muy 
restrictivo 
Bloqueante 
Informativo 
con 
seguimiento 
PRO representa el entorno crítico de explotación.  
Los desarrollos Compliance deben cumplir todas las 
validaciones, en caso contrario el despliegue no se 
realizará. 
Los desarrollos Legacy pueden desplegar, pero sus 
incumplimientos quedan registrados en Jira de forma 
automática  y deben ser gestionados conforme al plan de 
reducción de deuda técnica. 
 
4. Validaciones e implementación técnica 
Su finalidad es establecer un marco uniforme que permita a gestores y equipos técnicos evaluar la 
madurez de un desarrollo antes de su paso a entornos críticos, reduciendo riesgos operativos, 
controlando la deuda técnica y asegurando la compatibilidad con las prácticas definidas para la 
integración con framework APB. Se tiene las validaciones técnicas y también se emplea la herramienta 
Sonar. 
4.

1. Validaciones Técnicas APB 
Estas validaciones funcionan como el estándar mínimo que debe cumplir cualquier servicio o desarrollo 
que se integre en el framework de docks, asegurando coherencia técnica entre proyectos. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 9 de 21 
 
 
Políticas de cumplimiento APB  
Authorize  
Todos los endpoints deben estar protegidos mediante mecanismos de autorización: 
- 
Cumplimiento de políticas de seguridad. 
- 
Evita exposición de operaciones internas. 
- 
Previene ataques por ausencia de validación de identidad. 
Pueden estar definidos a nivel de método o clase, con los roles y scopes correspondientes: 
 
Los roles deben definirse dentro de cada aplicación o servicio según sus necesidades específicas. La 
autenticación mediante token de TGT se irá deprecando progresivamente, por lo que no debe utilizarse 
en nuevos desarrollos ni ampliarse su uso.  
El mecanismo corporativo vigente para la definición y gestión de roles y permisos es Azure Entra ID: 
• 
Toda autenticación deberá pasar por Azure Entra ID. 
• 
El consumo de los roles debe integrarse en el código mediante [Authorize(Roles = "...")]. 
• 
La autorización se realizará mediante roles, scopes y permisos definidos en App Registrations. 
 
 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 10 de 21 
 
 
Políticas de cumplimiento APB  
Todos los accesos quedan auditados en Sign-in events de Azure: 
 
Bloques try/catch 
No se permite el uso de bloques try/catch dentro del código, y en ningún caso debe emplearse como 
mecanismo de validación. 
Ejemplos de mal uso del try/catch: 
 
 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 11 de 21 
 
 
Políticas de cumplimiento APB  
 
Los errores inesperados son capturados por el framework de Docks y facilita la resolución de incidencias.  
 
Errores inesperados (no controlados) 
Son fallos técnicos que no forman parte del comportamiento normal del servicio y que deben registrarse 
siempre. No deben ocultarse dentro de un try/catch. 
Ejemplos: 
- 
Fallo de conexión a una base de datos. 
- 
NullPointerException u otras excepciones en tiempo de ejecución. 
- 
Error al parsear un JSON inesperado. 
- 
Fallos de infraestructura o dependencias externas. 
Errores controlados (funcionales) 
Son situaciones previstas dentro del flujo de negocio y deben gestionarse adecuadamente por el 
desarrollador. Estos errores no se consideran fallos del sistema, sino respuestas esperadas ante 
determinadas condiciones. 
Ejemplos: 
- 
Un usuario intenta registrarse con un email ya existente. 
- 
Se devuelve un error funcional con código HTTP 400 o similar, según corresponda. 
Uso de WebService  
APB no permite la utilización de tecnologías SOAP o WebService basados en WSDL. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 12 de 21 
 
 
Políticas de cumplimiento APB  
Esta tecnología se considera obsoleta y no cumple los requisitos de seguridad, mantenibilidad ni 
observabilidad de la arquitectura actual. 
Los servicios nuevos deben desarrollarse exclusivamente con tecnologías REST u otras que se encuentren 
homologadas en APB. 
Los sistemas Legacy que dependan de SOAP deberán disponer de un plan de eliminación progresiva 
aprobado por Arquitectura. 
 
Ejemplos de uso de webServices, que se debe evitar: 
 
 
Versionado de plantilla API/APP base 
Los servicios deben utilizar la versión actual de la plantilla Base o, como máximo, una versión 
inmediatamente inferior. 
El objetivo es garantizar compatibilidad con los mecanismos de seguridad y auditoría de la plataforma, 
evitar el uso de componentes obsoletos y reducir el riesgo operativo asociado a versiones desactualizadas. 
 
 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 13 de 21 
 
 
Políticas de cumplimiento APB  
Documentación mínima 
Cada desarrollo (aplicación o servicio) debe contar con la siguiente documentación mínima, elaborada 
siguiendo las plantillas y buenas prácticas definidas por APB. Todos los entregables deben incluir en copia 
al gestor de la aplicación en APB. 
La documentación mínima debe incluir: 
• 
Código fuente y scripts 
Contiene todo el código desarrollado, librerías, scripts y elementos necesarios para su compilación o 
despliegue. 
Destinatarios: Equipo de desarrollo y Arquitectura. 
• 
Manual de explotación 
Incluye los procedimientos de despliegue, rollback, configuración de entornos y requisitos de 
seguridad aplicables. 
Destinatarios: Operaciones y equipo de proyecto. 
• 
Análisis técnico 
Documentación técnica que describe la arquitectura del servicio, sus dependencias, frameworks 
utilizados, y cualquier componente o diagrama relevante. 
Destinatarios: Equipo de proyecto y Arquitectura. 
• 
Análisis funcional 
Describe el comportamiento funcional, flujos, reglas de negocio y requisitos funcionales del servicio 
o aplicación. 
Destinatarios: Equipo de proyecto y Arquitectura. 
• 
Manual para usuarios 
Contiene las instrucciones para el uso de la aplicación o servicio, casos de uso y guía para usuarios 
finales. 
Destinatarios: Equipo de proyecto, usuarios finales y HelpDesk. 
• 
Manual de administración 
Describe tareas de configuración, gestión y mantenimiento interno de la aplicación. 
Destinatarios: Equipo de proyecto. 
• 
Manual de desarrollador 
Especifica endpoints expuestos, contratos de entrada/salida, ejemplos de uso y particularidades 
funcionales relevantes para el desarrollo y evolución del servicio. 
(Este contenido se integra dentro de la documentación técnica y/o los entregables de proyecto según 
corresponda.) 
• 
Procedimiento SSI – Gestión de permisos (portal DOCKS) 
Define el proceso de alta, modificación y baja de permisos de acceso a la aplicación. 
Destinatarios: Equipo de proyecto, HelpDesk y Arquitectura. 
• 
Procedimiento de soporte operativo (horario laboral y guardias) 
Incluye los procesos de monitorización, alertas, troubleshooting y resolución de incidencias desde 
Operaciones. 
Destinatarios: Operaciones y equipo de proyecto. 
• 
Pruebas y evidencias 
Recoge los resultados de pruebas funcionales, técnicas y de integración necesarias para validar el 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 14 de 21 
 
 
Políticas de cumplimiento APB  
correcto funcionamiento. 
Destinatarios: Equipo de proyecto. 
• 
Auditoría de calidad 
Documenta los controles de calidad aplicados, incluyendo validaciones automáticas en los 
despliegues. 
Destinatarios: Equipo de proyecto y Arquitectura. (Opcional) 
La documentación debe elaborarse siguiendo los requerimientos, plantillas y repositorios definidos por 
APB, de forma que todos los proyectos mantengan un formato homogéneo y un nivel mínimo de calidad 
documental. El conjunto de documentos mínimos se define de forma general y puede consultarse en la 
definición correspondiente. 
Gestión de secretos 
La gestión de secretos se refiere al conjunto de prácticas destinadas a evitar que credenciales sensibles 
aparezcan expuestas en el código, asegurando que contraseñas, tokens, claves API y certificados se 
almacenen y utilicen de forma segura. 
En SonarQube: 
 
 
SonarQube valida la gestión adecuada de secretos dentro del proyecto y, por defecto, marca como 
problema (Security Rating) cualquier rastro de credenciales hardcodeadas, tales como: 
• 
Passwords incrustadas en código. 
• 
API Keys o Access Tokens. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 15 de 21 
 
 
Políticas de cumplimiento APB  
• 
Claves privadas (private keys). 
• 
Tokens de servicios cloud (Azure, AWS, GCP, GitHub…). 
• 
Cadenas con formato típico de secret (ej. Bearer ..., Basic ..., ssh-rsa, etc.). 
• 
Configuraciones con secretos dentro de archivos YAML, JSON, properties o environment. 
 
Cualquier secreto hardcodeado se considera una mala práctica y debe ser eliminado, externalizado o 
protegido mediante el mecanismo adecuado (vaults, variables de entorno, key vault, etc.). No se 
permite mantener secretos dentro del código fuente. 
 
Para garantizar un manejo seguro y consistente en todos los entornos: 
• 
Todos los secretos deben almacenarse obligatoriamente en Azure Key Vault, incluyendo 
contraseñas, tokens, API keys, certificados, cadenas de conexión y cualquier valor sensible. 
• 
Las aplicaciones deben consumir estos secretos a través de Azure App Configuration, que 
actuará como único punto de referencia para los distintos entornos (Desarrollo, Preproducción y 
Producción). 
 
 
 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 16 de 21 
 
 
Políticas de cumplimiento APB  
Gestión de dependencias 
La gestión de dependencias consiste en asegurar que todas las librerías, paquetes externos y 
componentes de terceros utilizados en un proyecto se mantengan actualizados, seguros y libres de 
vulnerabilidades conocidas. Su objetivo es evitar riesgos derivados de versiones obsoletas, inseguras o 
con fallos críticos. 
Se tiene definido en GitHub la supervisión automática de la seguridad y la calidad de las librerías utilizadas 
en el proyecto a través de Dependabot Alerts, funcionalidad que se encuentra habilitada. Este sistema 
analiza todas las dependencias declaradas y genera alertas cuando se detectan vulnerabilidades, 
versiones obsoletas o paquetes con fallos de seguridad conocidos. 
 
 
4.

2. SonarQube - Validaciones de Calidad y Seguridad  
El Quality Gate APB constituye el conjunto de umbrales mínimos definidos en SonarQbe que deben 
cumplirse para considerar que un proyecto posee la calidad técnica necesaria para su despliegue en 
entornos corporativos. 
El incumplimiento de alguno de los criterios descritos supone que el software no está en un estado óptimo 
para avanzar a entornos PRE o PRO, pudiendo afectar a la estabilidad de los servicios, incrementar la 
deuda técnica o introducir vulnerabilidades. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 17 de 21 
 
 
Políticas de cumplimiento APB  
 
Blocker Severity Issues = 0 
Esta métrica identifica incidencias de severidad crítica que pueden comprometer el funcionamiento del 
sistema, generar fallos en tiempo de ejecución, permitir comportamientos no controlados o introducir 
vulnerabilidades explotables. 
El requisito es no presentar ningún caso de severidad Blocker. Su presencia indica riesgos que no son 
compatibles con un despliegue seguro en entornos de validación avanzada. 
Sin errores: 
 
Con errores: 
 
Cobertura mínima de pruebas (Coverage ≥ 60 %) 
La cobertura mide la proporción de código alcanzada por pruebas unitarias. Se exige como mínimo el 60%. 
Este requisito permite reducir la probabilidad de que errores no detectados lleguen a entornos 
productivos y establece una base que facilita la estabilidad del software ante cambios futuros. 
Pasando la cobertura: 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 18 de 21 
 
 
Políticas de cumplimiento APB  
 
Sin pasar la cobertura: 
 
Maintainability Rating igual o superior a B 
El rating de mantenibilidad refleja la cantidad de deuda técnica acumulada. Exigir un nivel B asegura que 
la deuda se mantiene dentro de márgenes razonables y que el código es sostenible, legible y susceptible 
de ser evolucionado sin generar costes desproporcionados. Los niveles inferiores implican presencia 
significativa de duplicidad, complejidad excesiva o malas prácticas estructurales. 
Pasando Maintainability Rating: 
 
Reliability Rating igual o superior a C 
La fiabilidad evalúa la existencia de defectos que pueden provocar comportamientos no previstos o 
interrupciones del servicio. Requerir un nivel C garantiza que el software no presenta fallos graves que 
puedan comprometer su funcionamiento. Un nivel inferior sugeriría la posibilidad de errores en tiempo 
de ejecución, pérdida de estabilidad o mal manejo de excepciones. 
Pasando Reliability Rating:  

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 19 de 21 
 
 
Políticas de cumplimiento APB  
 
Sin pasar el Reliability Rating: 
 
Security Rating igual o superior a C 
Esta métrica determina si el código presenta vulnerabilidades o prácticas inseguras. Un mínimo de C 
asegura que no existen riesgos importantes que puedan afectar la integridad, confidencialidad o 
disponibilidad del sistema. Niveles inferiores son indicativos de fallos de validación, uso de dependencias 
inseguras, manejo incorrecto de credenciales o exposición potencial a ataques. 
Pasando el security rating: 
 
Sin pasar el security rating: 
 
 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 20 de 21 
 
 
Políticas de cumplimiento APB  
El security Rating también es el encargado de validar la gestión adecuada de secretos dentro del proyecto 
y, por defecto, marca como problema (Security Rating) cualquier rastro de credenciales hardcodeadas, 
tales como: 
- 
Passwords incrustadas en código. 
- 
API Keys o Access Tokens. 
- 
Claves privadas (private keys). 
- 
Tokens de servicios cloud (Azure, AWS, GCP, GitHub…). 
- 
Cadenas con formato típico de secret (ej. Bearer ..., Basic ..., ssh-rsa, etc.). 
- 
Configuraciones con secretos dentro de archivos YAML, JSON, properties o environment. 
4.

3. Jenkins - Criterios de implementación 
Con el fin de aplicar de forma automática y homogénea los niveles de exigencia definidos en la Política de 
QA, cada desarrollo deberá estar clasificado explícitamente como: Compliance o Legacy 
Dicha clasificación se implementará mediante etiquetas (labels) configuradas en el pipeline de Jenkins. 
 
 
Todo pipeline deberá tener definida explícitamente una etiqueta. 
No se permitirá: 
- 
Pipelines sin clasificación. 
- 
Cambios de etiqueta sin aprobación formal. 
- 
Eliminación manual de controles asociados a la etiqueta. 
En ausencia de etiqueta válida, el sistema deberá considerar el desarrollo como Compliance por defecto. 
La etiqueta no es un atributo administrativo, sino un mecanismo técnico de control de calidad y riesgo. 
Su correcta configuración es obligatoria para permitir el despliegue en entornos corporativos 
El cambio de clasificación requerirá validación de Arquitectura y/o Ciberseguridad. 
Toda modificación deberá quedar: 
- 
Documentada. 
- 
Justificada. 
- 
Trazable en Jira. 
- 
Reflejada en histórico de configuración del pipeline. 
La clasificación mediante etiquetas en Jenkins garantiza: 
- 
Aplicación automática de reglas. 
- 
Eliminación de criterios subjetivos. 

 
 
Sistemas de la Información 
Políticas_de_QA_APB_v1.docx 
Pàgina 21 de 21 
 
 
Políticas de cumplimiento APB  
- 
Homogeneidad entre equipos. 
- 
Transparencia en auditorías. 
- 
Imposibilidad de eludir controles manualmente.

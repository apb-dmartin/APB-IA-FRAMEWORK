# GUI - Protección de las Aplicaciones v1.0 - ES_firmado(1)

Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 1 de 8 
Versión 1.0 
 
 
 
 
 
 
 
 
 
 
 
 
Protección de las Aplicaciones 
Guía 
Autoritat Portuària de Barcelona 
 
 
 

Protección de las Aplicaciones 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 2 de 8 
Versión 1.0 
 
Información del documento: 
Título del documento 
Protección de las Aplicaciones 
Tipo de documento 
Guía 
Descripción 
La protección de las aplicaciones consiste en aplicar medidas de 
seguridad durante todo su ciclo de vida desde el diseño hasta su 
retirada para garantizar que gestionan la información de forma 
segura y resistente frente a amenazas. Incluye la definición de 
requisitos de seguridad, el desarrollo y configuración seguros, el 
control de accesos, la protección de los datos, la validación de 
entradas, la monitorización de la actividad y la gestión de 
vulnerabilidades e incidentes. 
Nivel de seguridad 
Interno 
Propietario del documento 
Responsable de Seguridad de la Información 
 
 
 
Historial de revisiones/aprobaciones 
 
Versión 
Descripción  
Autor 
Acción  
Fecha  
v1.0 
Procedimiento de 
Comunicación APB 
Oficina Técnica de Seguridad  
(Sothis) 
Creación 
15/04/2026 
v1.0 
Revisión de 
Procedimiento 
Responsable de Seguridad 
de la Información (CISO) 
Revisión 
17/04/2026 
v1.0 
Aprobación de 
Procedimiento 
Responsable de Seguridad 
de la Información (CISO) 
Aprobación 
02/05/2026 
 
 
 
 
 
 
 
 
 
Historial de versiones 
 
Versión 
Descripción  
Autor 
Fecha  
v1.0 
Versión inicial del documento 
Oficina Técnica de Seguridad 
(Sothis) 
15/07/2025 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Control de distribución 
Descripción 
Área de difusión 
Fecha  
Todas las personas de las áreas de difusión indicadas 
Ciberseguridad, Desarrollo, Sistemas de 
Información  
 
 
 
 
 
 
 
Aviso: Este documento es propiedad de la Autoritat Portuària de Barcelona y contiene información clasificada según el nivel de seguridad definido, 
debiendo aplicarse las medidas de uso y custodia pertinentes, de acuerdo con lo establecido en las Políticas de Seguridad de la Información. 

Protección de las Aplicaciones 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 3 de 8 
Versión 1.0 
 
 
Índice  
 
1. 
Introducción ......................................................................................................................... 4 
2. 
Alcance ................................................................................................................................. 4 
3. 
Roles y responsabilidades .................................................................................................... 4 
4. 
Protección de las aplicaciones durante su ciclo de vida ...................................................... 4 
4.1 
Definición de requisitos de seguridad ............................................................................. 4 
4.2 
Diseño seguro de la aplicación ......................................................................................... 5 
4.3 
Entornos de desarrollo y pruebas .................................................................................... 5 
4.4 
Desarrollo seguro ............................................................................................................. 5 
4.5 
Gestión de la configuración ............................................................................................. 5 
4.6 
Pruebas de seguridad ....................................................................................................... 5 
4.7 
Despliegue y paso a producción ...................................................................................... 6 
4.8 
Control de accesos y autenticación ................................................................................. 6 
4.9 
Protección de la información ........................................................................................... 6 
4.10 
Registro y trazabilidad...................................................................................................... 6 
4.11 
Gestión de vulnerabilidades ............................................................................................ 6 
4.12 
Gestión de incidentes ...................................................................................................... 7 
4.13 
Protección de aplicaciones web ....................................................................................... 7 
4.14 
Continuidad del servicio ................................................................................................... 7 
4.15 
Finalización y retirada ...................................................................................................... 7 
5. 
Registros .............................................................................................................................. 7 
6. 
Referencias .......................................................................................................................... 7 
 
 
 
 
 

Protección de las Aplicaciones 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 4 de 8 
Versión 1.0 
 
1. Introducción 
La Autoritat Portuària de Barcelona establece esta guía para definir las medidas operativas necesarias para proteger 
las aplicaciones durante todo su ciclo de vida, desde su diseño y desarrollo hasta su puesta en producción, operación 
y retirada. 
El objetivo es garantizar que las aplicaciones gestionan la información de forma segura, reducen su exposición a 
amenazas y mantienen un nivel adecuado de protección conforme al Esquema Nacional de Seguridad (ENS), ISO 
27001 y el Sistema de Gestión de Seguridad de la Información (SGSI). 
2. Alcance 
Esta guía aplica a todas las aplicaciones utilizadas por la Autoritat Portuària de Barcelona, tanto desarrolladas 
internamente como por terceros, con independencia de su tecnología o entorno de despliegue. 
Incluye: 
• 
Aplicaciones web, móviles y de escritorio  
• 
Servicios y aplicaciones expuestas a internet o redes internas  
• 
Aplicaciones desplegadas en entornos cloud, híbridos o on-premise  
• 
Sistemas en fase de desarrollo, pruebas, producción y retirada  
Abarca todo el ciclo de vida de las aplicaciones: diseño, desarrollo, pruebas, despliegue, operación, mantenimiento 
y finalización. 
3. Roles y responsabilidades 
La protección de las aplicaciones en la Autoritat Portuària de Barcelona requiere la participación coordinada de los 
siguientes roles: 
• 
Responsable de Seguridad de la Información: define los requisitos de seguridad, valida los controles 
aplicables y supervisa los riesgos asociados a las aplicaciones, asegurando su alineación con el ENS y la 
normativa vigente.  
• 
Responsable de Sistemas: garantiza la implantación técnica, la configuración segura y la integración de las 
aplicaciones en la infraestructura corporativa.  
• 
Responsable de Desarrollo: asegura que las aplicaciones se diseñan y desarrollan conforme a prácticas de 
desarrollo seguro durante todo su ciclo de vida.  
• 
Responsable de Servicio / Propietario de la Aplicación: valida el uso funcional de la aplicación y controla 
la información tratada durante su operación.  
• 
Equipos de desarrollo y operación: implementan, mantienen y supervisan los controles de seguridad 
definidos, gestionando incidencias, cambios y actualizaciones.  
• 
Proveedores de servicios: cumplen los requisitos de seguridad establecidos contractualmente y colaboran 
en la implantación, mantenimiento, auditoría y mejora de la seguridad de las aplicaciones.  
• 
Usuarios autorizados: utilizan las aplicaciones conforme a las políticas establecidas y comunican cualquier 
incidencia, anomalía o uso indebido detectado. 
4. Protección de las aplicaciones durante su ciclo de vida 
4.1 Definición de requisitos de seguridad 
Antes de iniciar cualquier desarrollo, modificación o adquisición de una aplicación, la Autoritat Portuària de 
Barcelona define los requisitos de seguridad aplicables durante todo su ciclo de vida. 

Protección de las Aplicaciones 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 5 de 8 
Versión 1.0 
 
Estos requisitos se establecen a partir del análisis de riesgos, teniendo en cuenta la criticidad del sistema, la 
sensibilidad de la información y las obligaciones legales, contractuales y normativas aplicables. 
Como mínimo, deben contemplarse mecanismos de autenticación, control de accesos, protección de la información, 
trazabilidad y seguridad de las comunicaciones. 
Los requisitos deben quedar documentados y mantenerse actualizados para servir de referencia durante el diseño, 
desarrollo, pruebas y operación de la aplicación. 
4.2 Diseño seguro de la aplicación 
La seguridad debe incorporarse desde las primeras fases del diseño, evitando depender de controles añadidos 
posteriormente. 
La arquitectura de la aplicación debe contemplar la separación de componentes y funciones, el control de accesos 
entre capas y la reducción de la superficie de ataque. Para ello, se aplican principios como mínimo privilegio y 
defensa en profundidad. 
También se identifican los componentes de la solución, incluidas librerías, servicios externos y sistemas de soporte, 
evaluando su estado de seguridad y nivel de exposición. Sobre esta base, se analizan las amenazas y se definen las 
medidas de mitigación necesarias antes de su implantación. 
4.3 Entornos de desarrollo y pruebas 
Los entornos de desarrollo, pruebas, preproducción y producción deben mantenerse separados, tanto a nivel técnico 
como de acceso, para evitar interferencias y reducir riesgos. 
• 
No se deben utilizar datos reales en entornos no productivos, salvo que exista justificación expresa y se 
apliquen medidas de protección adecuadas, como el anonimizado o enmascaramiento de la información. 
• 
El acceso a cada entorno se limita al personal autorizado según la función que desempeña, y sus 
configuraciones y permisos se revisan periódicamente para asegurar que siguen siendo adecuados. 
4.4 Desarrollo seguro 
Durante el desarrollo se aplican prácticas que reduzcan la aparición de vulnerabilidades y refuercen la seguridad de 
la aplicación. Se utilizan componentes y dependencias actualizados y de origen verificado, evitando versiones 
obsoletas o no confiables. La aplicación debe validar correctamente la información que recibe y genera, y gestionar 
los errores sin revelar información sensible ni detalles internos del sistema. 
Las credenciales, claves y parámetros de configuración deben protegerse adecuadamente y no incluirse en el código 
fuente. El desarrollo debe apoyarse, además, en sistemas de control de versiones y revisiones de código que 
permitan mantener la trazabilidad de los cambios y detectar errores antes de su puesta en producción. 
4.5 Gestión de la configuración 
Antes de su puesta en producción, la aplicación debe configurarse de forma segura, evitando configuraciones por 
defecto que puedan suponer un riesgo. Se habilitan únicamente los servicios, funciones y permisos necesarios para 
su funcionamiento, limitando la exposición de la aplicación. Los archivos de configuración, especialmente aquellos 
que contienen credenciales o parámetros sensibles, deben protegerse frente a accesos no autorizados. 
Asimismo, se aplica el principio de mínimo privilegio en la asignación de permisos a usuarios, procesos y servicios, 
garantizando que cada elemento dispone únicamente de los accesos imprescindibles para su función. 
4.6 Pruebas de seguridad 
Antes de la puesta en producción, la aplicación debe someterse a pruebas que verifiquen tanto su correcto 
funcionamiento como la eficacia de los controles de seguridad implementados. Estas pruebas incluyen análisis de 
vulnerabilidades, revisión de configuraciones y, cuando el nivel de riesgo lo requiera, pruebas de penetración. 
También se comprueba el correcto funcionamiento de los mecanismos de autenticación, control de accesos y 
registro de actividad. 

Protección de las Aplicaciones 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 6 de 8 
Versión 1.0 
 
Los resultados deben documentarse y evaluarse, de forma que cualquier debilidad detectada sea corregida antes 
del despliegue. 
4.7 Despliegue y paso a producción 
El paso a producción se realiza de forma controlada, asegurando que la aplicación cumple los requisitos definidos y 
no introduce riesgos para el entorno. Antes de su implantación, se valida su estado funcional y de seguridad, se 
registra en el inventario corporativo y se asignan los responsables de su gestión. Asimismo, se configuran los 
mecanismos de monitorización y se integra en los procesos de operación y gestión de incidencias. 
La puesta en producción solo se autoriza cuando se han superado todas las validaciones previstas. 
4.8 Control de accesos y autenticación 
Las aplicaciones deben garantizar que el acceso a sus funcionalidades está limitado a usuarios o sistemas 
autorizados. Para ello, se establecen mecanismos de identificación individual y se asignan permisos conforme al 
principio de mínimo privilegio, preferentemente mediante modelos basados en roles. Los accesos deben revisarse 
periódicamente y ajustarse cuando dejen de ser necesarios. 
En los casos que lo requieran, especialmente para accesos privilegiados o a información sensible, se aplican 
mecanismos de autenticación reforzada, como la autenticación multifactor, con el fin de reducir el riesgo de accesos 
no autorizados. 
4.9 Protección de la información 
Las aplicaciones deben proteger la información que gestionan en función de su nivel de sensibilidad y de los 
requisitos normativos aplicables. Para ello, se aplican medidas como el cifrado de datos en tránsito y, cuando sea 
necesario, también en reposo, garantizando que la información no pueda ser interceptada ni accedida por terceros 
no autorizados. Las credenciales y datos sensibles deben almacenarse y gestionarse de forma segura, evitando su 
exposición en código, configuraciones o respuestas del sistema. 
Asimismo, se controla el acceso a la información según su clasificación, asegurando que solo los usuarios autorizados 
puedan consultarla o modificarla, y evitando la inclusión de datos innecesarios en respuestas, mensajes de error o 
registros. 
4.10 Registro y trazabilidad 
Las aplicaciones deben disponer de mecanismos de registro que permitan conocer qué acciones se realizan, quién 
las ejecuta y cuándo se producen. Se registran, al menos, los accesos, operaciones relevantes, cambios de 
configuración y eventos de seguridad, incluyendo la identificación del usuario o sistema y el origen de la conexión. 
Estos registros deben ser suficientes para permitir la investigación de incidentes y la reconstrucción de eventos. 
Los logs deben protegerse frente a modificaciones, accesos no autorizados o pérdidas, y conservarse durante el 
tiempo definido por la organización. Su revisión periódica permite detectar comportamientos anómalos y mejorar 
la seguridad del sistema. 
4.11 Gestión de vulnerabilidades 
Durante la operación de la aplicación, se realiza un seguimiento continuo de las vulnerabilidades que puedan 
afectarla. Esto incluye la revisión periódica de componentes, librerías y dependencias, la aplicación de parches de 
seguridad y la actualización de versiones cuando sea necesario. También se llevan a cabo análisis de vulnerabilidades 
y revisiones técnicas para identificar posibles debilidades. 
Las vulnerabilidades detectadas se evalúan en función de su impacto y probabilidad, priorizando su corrección según 
el riesgo que representan, con el objetivo de reducir el tiempo de exposición. 
 

Protección de las Aplicaciones 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 7 de 8 
Versión 1.0 
 
4.12 Gestión de incidentes 
Las aplicaciones deben integrarse en el proceso corporativo de gestión de incidentes de seguridad. Cualquier 
incidente relevante debe notificarse de forma inmediata, permitiendo su análisis, la aplicación de medidas de 
contención y la recuperación del servicio en el menor tiempo posible. Cuando intervienen proveedores, estos deben 
colaborar en la resolución conforme a los acuerdos establecidos. 
Una vez resuelto el incidente, se analizan sus causas y se definen acciones correctoras o preventivas que eviten su 
repetición, contribuyendo a la mejora continua de la seguridad. 
4.13 Protección de aplicaciones web 
Las aplicaciones web, por su exposición a redes externas, requieren medidas específicas de protección frente a 
amenazas habituales. Se implementan controles para prevenir ataques como inyecciones, XSS o CSRF, mediante 
validación de entradas, control de sesiones y uso de tokens de seguridad. Todas las comunicaciones deben realizarse 
mediante HTTPS para garantizar la confidencialidad e integridad de los datos. 
Cuando el nivel de exposición lo requiera, se incorporan mecanismos adicionales como cortafuegos de aplicaciones 
web (WAF) y controles de acceso a las interfaces de administración, restringiendo su uso únicamente a personal 
autorizado y, cuando sea posible, desde redes seguras. 
4.14 Continuidad del servicio 
Las aplicaciones deben garantizar un nivel de disponibilidad acorde a su criticidad y al impacto que tendría su 
interrupción. Para ello, se establecen copias de seguridad periódicas, mecanismos de recuperación ante fallos y, 
cuando es necesario, soluciones de alta disponibilidad que permitan mantener el servicio ante incidencias. 
Además, se definen y revisan los planes de continuidad y recuperación, verificando su eficacia mediante pruebas 
periódicas, con el objetivo de asegurar que la aplicación puede restablecerse en condiciones aceptables en caso de 
incidente. 
4.15 Finalización y retirada 
Cuando una aplicación deja de utilizarse o es sustituida, su retirada debe realizarse de forma controlada y segura. 
Se garantiza la eliminación o transferencia de la información conforme a los requisitos establecidos, evitando la 
pérdida o exposición de datos. Asimismo, se revocan los accesos y credenciales asociados, se eliminan integraciones 
técnicas y se desactivan los servicios vinculados. 
Finalmente, se conservan las evidencias necesarias del proceso de cierre, asegurando la trazabilidad de las 
actuaciones realizadas y el cumplimiento de las obligaciones legales y organizativas. 
5. Registros 
CHL - CheckList Controles de Seguridad en el Desarrollo 
6. Referencias 
• 
Esquema Nacional de Seguridad (ENS) – Real Decreto 311/2022: marco normativo de referencia para la 
protección de la información en el sector público, especialmente en lo relativo a controles de seguridad, 
gestión de riesgos y protección de servicios digitales. 
• 
ISO/IEC 27001:2022: estándar internacional para la gestión de la seguridad de la información, que establece 
los requisitos para implantar, mantener y mejorar un sistema de gestión de seguridad (SGSI). 
• 
ISO/IEC 27002:2022: código de buenas prácticas que complementa a ISO 27001, proporcionando controles 
de seguridad aplicables, incluyendo aspectos relacionados con el desarrollo seguro y la protección de 
aplicaciones. 
• 
ISO/IEC 27017:2015: recomendaciones específicas para la seguridad en servicios cloud, aplicables cuando 
las APIs se despliegan o consumen en estos entornos. 

Protección de las Aplicaciones 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Protección de las Aplicaciones 
Página 8 de 8 
Versión 1.0 
 
• 
OWASP (Open Web Application Security Project): conjunto de guías y buenas prácticas para el desarrollo 
seguro, incluyendo OWASP Top 10 y OWASP API Security Top 10, referencia clave para identificar riesgos 
comunes en APIs. 
• 
CCN-STIC 823 – Seguridad en entornos Cloud: guía del Centro Criptológico Nacional para la protección de 
servicios en la nube conforme al ENS. 
• 
CCN-CERT BP/28 – Recomendaciones sobre Desarrollo Seguro: documento que establece buenas prácticas 
para integrar la seguridad en el ciclo de vida del desarrollo de software. 
• 
CCN-STIC 808 – Verificación del cumplimiento del ENS: guía que recoge los controles y evidencias necesarias 
para validar la implantación de medidas de seguridad, incluyendo aspectos aplicables a servicios, 
aplicaciones y APIs.

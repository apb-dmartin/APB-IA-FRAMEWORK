# GUI - Seguridad en Contenedores y Cloud v1.0 - ES_firmado

Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
Página 1 de 8 
Versión 1.0 
 
 
 
 
 
 
 
 
 
 
 
 
Seguridad en Contenedores y Cloud 
Guía 
Autoritat Portuària de Barcelona 
 
 
 

Seguridad en Contenedores y Cloud 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
Página 2 de 8 
Versión 1.0 
 
Información del documento: 
Título del documento 
Seguridad en Contenedores y Cloud 
Tipo de documento 
Guía 
Descripción 
Define las medidas de seguridad aplicables al despliegue, 
configuración, operación y supervisión de servicios y sistemas 
basados en contenedores y entornos cloud. Su objetivo es garantizar 
un uso seguro de estas tecnologías, protegiendo la información, 
controlando 
accesos, 
configuraciones, 
redes, 
imágenes, 
vulnerabilidades, continuidad del servicio y cumplimiento de los 
requisitos de seguridad aplicables. 
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
 

Seguridad en Contenedores y Cloud 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
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
Principios de seguridad en entornos cloud ......................................................................... 4 
5. 
Seguridad en contenedores ................................................................................................. 5 
5.

1. 
Gestión de Imágenes ........................................................................................................ 5 
5.

2. 
Control de vulnerabilidades ............................................................................................. 5 
6. 
Configuración segura ........................................................................................................... 5 
6.

1. 
Despliegue seguro ............................................................................................................ 5 
7. 
Gestión de identidades y accesos ........................................................................................ 5 
8. 
Protección de la información ............................................................................................... 6 
8.

1. 
Gestión de secretos .......................................................................................................... 6 
9. 
Seguridad de red .................................................................................................................. 6 
1

0. 
Monitorización y registro..................................................................................................... 6 
1

1. 
Gestión de vulnerabilidades ................................................................................................ 7 
1

2. 
Gestión de incidentes .......................................................................................................... 7 
1

3. 
Continuidad del servicio ...................................................................................................... 7 
1

4. 
Borrado y finalización .......................................................................................................... 7 
1

5. 
Cumplimiento y revisión ...................................................................................................... 7 
1

6. 
Registros .............................................................................................................................. 7 
1

7. 
Referencias .......................................................................................................................... 8 
 
 
 
 
 

Seguridad en Contenedores y Cloud 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
Página 4 de 8 
Versión 1.0 
 
1. Introducción 
La Autoritat Portuària de Barcelona establece esta guía para definir las medidas de seguridad aplicables al uso de 
tecnologías de contenedores y entornos cloud. 
Estos modelos proporcionan flexibilidad, escalabilidad y eficiencia en la gestión de los sistemas, pero también 
introducen riesgos derivados de la compartición de recursos, la automatización de despliegues y la exposición a 
redes externas. 
La aplicación de controles adecuados permite garantizar la protección de la información y de los servicios, 
asegurando su alineación con el Esquema Nacional de Seguridad (ENS) y con las buenas prácticas de seguridad en 
entornos cloud. 
2. Alcance 
La presente guía aplica a todas las interfaces de programación de aplicaciones (APIs) utilizadas por la Autoritat 
Portuària de Barcelona, con independencia del modelo de servicio o despliegue. 
Incluye: 
• 
Infraestructura cloud en sus diferentes modelos (IaaS, PaaS y SaaS).  
• 
Plataformas de contenedores (como Docker, Kubernetes u otras tecnologías equivalentes).  
• 
Sistemas, aplicaciones y servicios desplegados en estos entornos.  
Su aplicación abarca todo el ciclo de vida de los servicios, desde su diseño y despliegue hasta su operación, 
mantenimiento y retirada. 
3. Roles y responsabilidades 
La seguridad de las APIs en la Autoritat Portuària de Barcelona a requiere la participación coordinada de los 
siguientes roles: 
• 
Responsable de Seguridad de la Información: define los requisitos de seguridad y supervisa los riesgos 
asociados. 
• 
Responsable de Sistemas: gestiona la infraestructura, asegurando su configuración segura y operación. 
• 
Responsable del Área de Desarrollo: asegura la aplicación de prácticas de desarrollo seguro durante todo 
el ciclo de vida.  
• 
Jefe de Proyecto: supervisa el cumplimiento de los requisitos de seguridad hasta la puesta en producción.  
• 
Responsable Técnico: implementan las medidas de seguridad en despliegues, configuraciones y 
mantenimiento. 
• 
Proveedores cloud: garantizan la seguridad de los servicios prestados conforme a las condiciones 
contractuales. 
4. Principios de seguridad en entornos cloud 
La Autoritat Portuària de Barcelona aplica principios que guían el uso seguro de estos entornos: 
• 
Modelo de responsabilidad compartida: el proveedor asegura la infraestructura base, mientras que la APB 
es responsable de la configuración, el acceso y la protección de la información.  
• 
Configuración segura desde el inicio: los servicios deben desplegarse con controles de seguridad 
adecuados desde su puesta en funcionamiento.  
• 
Protección de la información: los datos deben tratarse conforme a su criticidad, especialmente en entornos 
externos.  

Seguridad en Contenedores y Cloud 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
Página 5 de 8 
Versión 1.0 
 
• 
Gestión centralizada de accesos: el control de identidades y permisos debe integrarse con los sistemas 
corporativos.  
La certificación del proveedor no exime de la responsabilidad de asegurar correctamente los servicios utilizados. 
5. Seguridad en contenedores 
5.

1. Gestión de Imágenes 
Las imágenes de contenedores constituyen la base del despliegue y deben gestionarse de forma controlada: 
• 
Se utilizan imágenes oficiales, verificadas o procedentes de repositorios confiables.  
• 
Se eliminan componentes innecesarios para reducir la superficie de ataque.  
• 
Se mantienen actualizadas, incorporando parches y versiones seguras. 
5.

2. Control de vulnerabilidades 
Las imágenes y sus dependencias deben revisarse de forma continua: 
• 
Se realizan escaneos de seguridad antes de su uso en entornos productivos.  
• 
Se evitan versiones obsoletas o con vulnerabilidades conocidas.  
• 
Se controla el uso de librerías y componentes externos. 
6. Configuración segura 
Los entornos cloud y contenedores deben configurarse minimizando riesgos: 
• 
Se eliminan configuraciones por defecto que puedan resultar inseguras.  
• 
Se habilitan únicamente los servicios y puertos necesarios.  
• 
Se aplica aislamiento entre contenedores y entornos para evitar accesos no autorizados. 
6.

1. Despliegue seguro 
La Autoritat Portuària de Barcelona establece que los despliegues en entornos cloud y de contenedores deben 
realizarse de forma controlada, trazable y segura, evitando configuraciones manuales que puedan introducir errores 
o vulnerabilidades. 
Los despliegues deben apoyarse en procesos automatizados (CI/CD), que garanticen la consistencia entre entornos 
y reduzcan la intervención manual. Estos procesos deben incorporar controles de seguridad, como validación de 
configuraciones, verificación de imágenes, revisión de dependencias y ejecución de pruebas antes de su puesta en 
producción. 
Antes de cualquier despliegue, se debe verificar que los componentes cumplen los requisitos de seguridad definidos 
y que no presentan vulnerabilidades conocidas o configuraciones inseguras. Asimismo, deben existir mecanismos 
de validación y aprobación previa que aseguren que el despliegue ha sido revisado desde el punto de vista técnico y 
de seguridad. 
La automatización de los despliegues debe realizarse en entornos controlados y con acceso restringido, garantizando 
la integridad de los procesos y evitando modificaciones no autorizadas. 
Este enfoque permite reducir riesgos operativos, mejorar la trazabilidad de los cambios y asegurar que los servicios 
se despliegan de forma coherente y conforme a los requisitos de seguridad establecidos. 
7. Gestión de identidades y accesos 
El acceso a los entornos cloud y plataformas de contenedores se gestiona de forma controlada: 

Seguridad en Contenedores y Cloud 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
Página 6 de 8 
Versión 1.0 
 
• 
Se utilizan identidades únicas e integradas con los sistemas corporativos.  
• 
Se aplica el principio de mínimo privilegio en la asignación de permisos.  
• 
Los accesos privilegiados se protegen mediante autenticación multifactor.  
• 
Se establecen roles diferenciados para administración, operación y desarrollo. 
8. Protección de la información 
La información tratada en estos entornos se protege conforme a su nivel de sensibilidad: 
• 
Se utiliza cifrado en tránsito y, cuando procede, en reposo.  
• 
Las claves criptográficas se gestionan de forma segura y controlada.  
• 
Se controla la ubicación de los datos, priorizando entornos con garantías adecuadas.  
Estas medidas reducen el riesgo de acceso no autorizado o exposición de información. 
8.

1. Gestión de secretos 
La Autoritat Portuària de Barcelona establece que todos los secretos utilizados en entornos cloud y de contenedores 
deben gestionarse de forma segura durante todo su ciclo de vida, con el fin de evitar accesos no autorizados o 
exposiciones accidentales. 
Se consideran secretos las credenciales, claves criptográficas, tokens, API keys, certificados y cualquier otro 
elemento que permita el acceso a sistemas o información sensible. 
Estos elementos no deben almacenarse en el código fuente, en imágenes de contenedores ni en archivos de 
configuración accesibles. En su lugar, deben gestionarse mediante soluciones específicas de gestión de secretos 
(vaults u otros mecanismos equivalentes), que permitan su almacenamiento seguro, control de accesos y auditoría 
de uso. 
El acceso a los secretos debe limitarse estrictamente a los servicios o usuarios que lo requieran, aplicando el principio 
de mínimo privilegio. Asimismo, deben establecerse mecanismos de rotación periódica, revocación y actualización, 
especialmente en casos de exposición o incidente de seguridad. 
Estas medidas permiten reducir el riesgo de compromiso de credenciales y asegurar un control adecuado sobre los 
elementos críticos de autenticación y protección de la información. 
 
9. Seguridad de red 
Las comunicaciones y accesos se protegen mediante controles específicos: 
• 
Se segmentan las redes para separar entornos y limitar la propagación de incidentes.  
• 
Se emplean mecanismos de filtrado y control del tráfico (firewalls, reglas de red).  
• 
Se restringen los accesos externos a los estrictamente necesarios. 
1

0. 
Monitorización y registro 
La Autoritat Portuària de Barcelona mantiene visibilidad sobre los entornos cloud: 
• 
Se registran accesos, cambios de configuración y eventos relevantes.  
• 
Se monitoriza la actividad para detectar comportamientos anómalos.  
• 
Los registros se protegen y conservan conforme a los criterios definidos.  
La monitorización permite actuar de forma temprana ante posibles incidentes. 

Seguridad en Contenedores y Cloud 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
Página 7 de 8 
Versión 1.0 
 
1

1. 
Gestión de vulnerabilidades 
Se aplican medidas continuas para mantener un nivel de seguridad adecuado: 
• 
Escaneo periódico de infraestructuras, contenedores y servicios.  
• 
Aplicación de parches y actualizaciones de seguridad.  
• 
Evaluación del riesgo asociado a vulnerabilidades detectadas.  
Cuando el nivel de criticidad lo requiera, se realizan pruebas de seguridad adicionales. 
1

2. 
Gestión de incidentes 
La Autoritat Portuària de Barcelona dispone de mecanismos para gestionar incidentes en entornos cloud: 
• 
Notificación inmediata a través de los canales establecidos.  
• 
Análisis del impacto y aplicación de medidas de contención.  
• 
Coordinación con el proveedor cuando el servicio dependa de terceros.  
Posteriormente, se revisan las causas y se definen acciones de mejora. 
1

3. 
Continuidad del servicio 
Los servicios deben garantizar un nivel adecuado de disponibilidad: 
• 
Se implementan copias de seguridad de la información crítica.  
• 
Se disponen planes de recuperación ante desastres.  
• 
Se diseñan soluciones con alta disponibilidad cuando el servicio lo requiera.  
Estas medidas permiten mantener o recuperar el servicio ante incidencias graves. 
1

4. 
Borrado y finalización 
Cuando un servicio deja de utilizarse: 
• 
Se realiza la eliminación segura de la información almacenada.  
• 
Se revocan accesos y credenciales asociados.  
• 
Se retiran los recursos y configuraciones desplegadas.  
Este proceso garantiza que no permanezcan datos o accesos no autorizados. 
1

5. 
Cumplimiento y revisión 
La Autoritat Portuària de Barcelona supervisa el cumplimiento de esta guía y verifica que los entornos cloud y de 
contenedores mantienen un nivel de seguridad adecuado. 
Se realizan revisiones periódicas para adaptar las medidas a la evolución tecnológica, a los riesgos identificados y a 
los requisitos normativos aplicables. Asimismo, se conservan evidencias de las configuraciones, controles 
implantados, registros de actividad e incidencias gestionadas, con el fin de asegurar la trazabilidad y la mejora 
continua. 
1

6. 
Registros 
• 
Inventario actualizado de servicios cloud, contenedores y recursos asociados 

Seguridad en Contenedores y Cloud 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad en Contenedores y Cloud 
Página 8 de 8 
Versión 1.0 
 
• 
Configuraciones de seguridad de infraestructuras, plataformas y entornos de contenedores 
• 
Imágenes de contenedores utilizadas y su estado de validación 
• 
Resultados de escaneos de vulnerabilidades y pruebas de seguridad realizadas 
• 
Registros de accesos, actividad y eventos relevantes de seguridad 
• 
Registro de incidencias, anomalías y actuaciones de respuesta 
• 
Evidencias de revisiones periódicas, auditorías y validaciones de seguridad 
• 
Documentación de proveedores cloud, configuraciones y acuerdos de nivel de servicio (SLA) 
1

7. 
Referencias 
• 
Esquema Nacional de Seguridad (ENS) – Real Decreto 311/2022 
• 
Guías CCN-STIC aplicables a entornos cloud y virtualización 
• 
OWASP (Open Web Application Security Project) 
• 
NIST SP 800-190 – Application Container Security Guide 
• 
CIS Benchmarks (Center for Internet Security) para Docker, Kubernetes y entornos cloud

# GUI - Seguridad de APIs v1.0 - ES_firmado

Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad de APIs 
Página 1 de 7 
Versión 1.0 
 
 
 
 
 
 
 
 
 
 
 
 
Seguridad de APIs 
Guía 
Autoritat Portuària de Barcelona 
 
 
 

Seguridad de APIs 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad de APIs 
Página 2 de 7 
Versión 1.0 
 
Información del documento: 
Título del documento 
Seguridad de APIs 
Tipo de documento 
Guía 
Descripción 
Establece las medidas de seguridad aplicables al diseño, desarrollo, 
publicación, consumo y mantenimiento de APIs utilizadas. Su 
finalidad es proteger los datos y servicios expuestos o consumidos a 
través de interfaces de programación, garantizando un control 
adecuado de accesos, autenticación, validación de peticiones, 
trazabilidad, monitorización y protección frente a abusos o 
vulnerabilidades. 
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
 

Seguridad de APIs 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad de APIs 
Página 3 de 7 
Versión 1.0 
 
Índice  
 
1. 
Introducción ......................................................................................................................... 4 
2. 
Alcance ................................................................................................................................. 4 
3. 
Roles y responsabilidades .................................................................................................... 4 
4. 
Principios de seguridad en APIs ........................................................................................... 5 
4.1 
Identificación y autenticación .......................................................................................... 5 
4.2 
Control de acceso y autorización ..................................................................................... 5 
4.3 
Protección de datos y respuestas .................................................................................... 5 
4.4 
Validación de entradas ..................................................................................................... 6 
4.5 
Seguridad en comunicaciones ......................................................................................... 6 
4.6 
Limitación de uso y protección frente a abuso ................................................................ 6 
4.7 
Registro y monitorización ................................................................................................ 6 
4.8 
Gestión de vulnerabilidades ............................................................................................ 6 
4.9 
Gestión de APIs de terceros ............................................................................................. 6 
5. 
Cumplimiento y revisión ...................................................................................................... 7 
6. 
Registros .............................................................................................................................. 7 
7. 
Referencias .......................................................................................................................... 7 
 
 
 
 
 

Seguridad de APIs 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad de APIs 
Página 4 de 7 
Versión 1.0 
 
1. Introducción 
La Autoritat Portuària de Barcelona establece esta guía para definir las medidas de seguridad aplicables al diseño, 
desarrollo, publicación, consumo y mantenimiento de APIs. 
Las APIs son un componente crítico en entornos digitales y cloud, ya que exponen funcionalidades y datos. Su uso 
incrementa la superficie de ataque, por lo que requieren controles específicos para garantizar la confidencialidad, 
integridad, disponibilidad y trazabilidad de la información. 
Esta guía se alinea con el Esquema Nacional de Seguridad (ENS), ISO 27001 y las recomendaciones del proyecto 
OWASP API Security Project. 
2. Alcance 
La presente guía aplica a todas las interfaces de programación de aplicaciones (APIs) utilizadas por la Autoritat 
Portuària de Barcelona, tanto si son desarrolladas internamente como si son proporcionadas por terceros. 
Su aplicación es independiente de la tecnología empleada, del modelo de arquitectura o del entorno en el que se 
despliegue la API, ya sea on-premise, cloud o híbrido, y abarca cualquier mecanismo de intercambio de información 
que deba gestionarse de forma segura y controlada. 
La guía incluye los siguientes tipos de APIs: 
• 
APIs REST, SOAP u otros modelos equivalentes: interfaces utilizadas para la comunicación entre sistemas 
que requieren controles específicos de autenticación, validación de datos y autorización.  
• 
APIs internas entre sistemas: interfaces empleadas para la integración de aplicaciones, servicios o 
plataformas dentro de la propia organización.  
• 
APIs públicas o expuestas a terceros: interfaces accesibles desde internet o utilizadas por organismos 
externos, empresas colaboradoras o ciudadanos, que requieren medidas reforzadas de protección.  
• 
APIs consumidas de proveedores externos: interfaces ofrecidas por terceros y utilizadas por la APB, cuya 
seguridad y nivel de acceso deben evaluarse y controlarse. 
3. Roles y responsabilidades 
La seguridad de las APIs en la Autoritat Portuària de Barcelona a requiere la participación coordinada de los 
siguientes roles: 
• 
Responsable de Seguridad de la Información: define los requisitos de seguridad, valida los controles y 
supervisa los riesgos asociados.  
• 
Responsable de Sistemas: garantiza la implantación técnica, la configuración segura y la integración de las 
APIs en la infraestructura corporativa.  
• 
Responsable del Área de Desarrollo: asegura la aplicación de prácticas de desarrollo seguro durante todo 
el ciclo de vida.  
• 
Jefe de Proyecto: supervisa el cumplimiento de los requisitos de seguridad hasta la puesta en producción.  
• 
Responsable Técnico: gestiona la configuración, despliegue, mantenimiento y actualización segura de la 
aplicación y de las APIs.  
• 
Responsable de Servicio / Propietario de la Aplicación: valida su uso funcional y controla el acceso a la 
información durante la operación.  
• 
Equipos de desarrollo: implementan los controles de seguridad en el diseño, desarrollo e integración de las 
APIs.  
• 
Usuarios y consumidores de APIs: utilizan las APIs conforme a las políticas establecidas y comunican 
incidencias o usos indebidos. 

Seguridad de APIs 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad de APIs 
Página 5 de 7 
Versión 1.0 
 
4. Principios de seguridad en APIs 
La Autoritat Portuària de Barcelona aplica un conjunto de principios que orientan la protección de las APIs desde 
su diseño hasta su retirada, garantizando un enfoque coherente y alineado con los riesgos actuales. 
• 
Seguridad desde el diseño (Security by Design): la seguridad se incorpora desde las fases iniciales del diseño 
y desarrollo, integrando controles en la arquitectura, la lógica de negocio y la gestión de accesos. 
• 
Validación continua basada en riesgos: las APIs se revisan periódicamente en función de su exposición, 
criticidad y evolución del entorno. 
• 
Control estricto de accesos: el acceso se limita a usuarios, sistemas o servicios autorizados. 
• 
Exposición mínima de datos: las APIs solo deben proporcionar la información necesaria para cada 
operación. 
• 
Monitorización y trazabilidad: las operaciones realizadas deben poder registrarse y analizarse para detectar 
anomalías e investigar incidentes.  
Estos principios se aplican durante todo el ciclo de vida de las APIs, dado que constituyen un punto habitual de 
interacción entre sistemas y un vector relevante de ataque en entornos digitales. 
4.1 Identificación y autenticación 
La Autoritat Portuària de Barcelona establece mecanismos de identificación y autenticación que permiten verificar 
de forma fiable la identidad de los usuarios o sistemas que acceden a las APIs. 
Todas las APIs deben requerir autenticación previa, evitando accesos anónimos salvo en casos expresamente 
justificados. Para ello, se emplean mecanismos robustos, como OAuth2, tokens seguros o certificados digitales, en 
función del tipo de servicio y del nivel de riesgo. 
Las credenciales no deben transmitirse ni almacenarse en texto plano y siempre deben protegerse mediante canales 
cifrados. En accesos con privilegios elevados o en servicios críticos, se aplicarán medidas reforzadas, como la 
autenticación multifactor. 
Una gestión adecuada de la autenticación es esencial para prevenir accesos no autorizados. 
4.2 Control de acceso y autorización 
El control de acceso en las APIs garantiza que cada usuario o sistema solo pueda realizar las acciones para las que ha 
sido autorizado. 
Para ello, se aplica el principio de mínimo privilegio y se prioriza el uso de modelos basados en roles (RBAC), que 
permiten estructurar y administrar los permisos de forma coherente. 
La autorización debe validarse en cada petición, asegurando que el acceso a recursos y operaciones se comprueba 
de forma continua y no solo en el momento de autenticación. 
Se prestará especial atención a evitar fallos de autorización, como el acceso a recursos pertenecientes a otros 
usuarios o sistemas no autorizados. 
4.3 Protección de datos y respuestas 
La Autoritat Portuària de Barcelona garantiza que las APIs gestionan la información de forma controlada, evitando 
la exposición innecesaria de datos. 
Las respuestas deben incluir únicamente la información estrictamente necesaria para la operación solicitada. 
También debe evitarse la divulgación de detalles técnicos o internos, como estructuras de base de datos, 
identificadores sensibles o información de configuración. 
Antes de su envío, las respuestas deben ser filtradas y validadas para asegurar que no contienen datos no 
autorizados, inconsistentes o manipulados. 

Seguridad de APIs 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad de APIs 
Página 6 de 7 
Versión 1.0 
 
4.4 Validación de entradas 
Toda información recibida a través de las APIs debe validarse antes de su procesamiento, con independencia de su 
origen. 
La validación debe comprobar el tipo de dato, formato, longitud y contenido permitido. Para ello, se prioriza el uso 
de listas blancas que definan de forma explícita los valores válidos. 
También deben aplicarse mecanismos de sanitización para eliminar o neutralizar caracteres o estructuras 
potencialmente maliciosas. 
Estas medidas permiten prevenir ataques como inyecciones, manipulación de parámetros, ejecución de código no 
autorizado o accesos indebidos a recursos internos. 
4.5 Seguridad en comunicaciones 
La Autoritat Portuària de Barcelona protege las comunicaciones de las APIs para garantizar la confidencialidad e 
integridad de la información intercambiada. 
Todas las comunicaciones deben realizarse mediante protocolos seguros, utilizando HTTPS con cifrado TLS. Se 
prohíbe el uso de comunicaciones en claro. 
Además, deben aplicarse medidas que permitan verificar la autenticidad de los extremos de la comunicación y 
reducir el riesgo de ataques de intermediario. 
4.6 Limitación de uso y protección frente a abuso 
La Autoritat Portuària de Barcelona implanta medidas de limitación de uso para evitar consumos abusivos de las 
APIs y reducir el riesgo de degradación o denegación de servicio. 
Estas medidas incluyen límites de peticiones, cuotas de uso, restricciones por usuario, sistema o dirección de origen 
y controles sobre operaciones que consuman recursos de forma intensiva. 
Los controles de consumo deben ajustarse a la criticidad del servicio y al patrón esperado de uso, protegiendo 
especialmente las operaciones de autenticación y los flujos de negocio sensibles. 
4.7 Registro y monitorización 
La Autoritat Portuària de Barcelona garantiza que las APIs disponen de capacidades suficientes de registro y 
monitorización para mantener la trazabilidad de su uso, detectar anomalías y facilitar la investigación de incidentes. 
Deben registrarse, al menos, los accesos, las operaciones relevantes, los cambios de configuración, los errores 
significativos y los eventos de seguridad necesarios para reconstruir lo ocurrido. 
Los registros deben permitir identificar al usuario o sistema que realiza la petición, el origen de la conexión, la 
operación ejecutada y su resultado, sin exponer información sensible innecesaria. Asimismo, deben protegerse 
frente a accesos no autorizados, alteraciones o pérdidas y conservarse durante el tiempo definido por la 
organización. 
4.8 Gestión de vulnerabilidades 
La Autoritat Portuària de Barcelona aplica un proceso continuo para identificar, evaluar y corregir las 
vulnerabilidades que puedan afectar a sus APIs. Este proceso incluye revisiones periódicas de configuración, análisis 
automatizados, comprobaciones sobre autenticación y autorización, validación de entradas, revisión de la 
exposición de datos y control de la seguridad de las dependencias utilizadas. 
Cuando la criticidad de la API o el análisis de riesgos lo requiera, se realizarán pruebas adicionales, como análisis de 
vulnerabilidades específicos o pruebas de penetración. 
4.9 Gestión de APIs de terceros 
Cuando la Autoritat Portuària de Barcelona consuma APIs proporcionadas por terceros, evaluará previamente su 
seguridad y el riesgo asociado a su integración. Esta evaluación debe considerar la autenticación requerida, la 

Seguridad de APIs 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Seguridad de APIs 
Página 7 de 7 
Versión 1.0 
 
protección de las comunicaciones, la información intercambiada, los límites de uso, la trazabilidad disponible y las 
garantías ofrecidas por el proveedor. 
La Autoritat Portuària de Barcelona limitará el acceso a estas APIs a las funciones e información estrictamente 
necesarias para la finalidad autorizada y establecerá controles sobre los datos intercambiados, las dependencias 
generadas y los posibles cambios del servicio que puedan afectar a la seguridad o disponibilidad de los sistemas 
internos. 
5. Cumplimiento y revisión 
La Autoritat Portuària de Barcelona revisa periódicamente la seguridad de sus APIs para asegurar que los controles 
implantados siguen siendo adecuados al nivel de exposición, a la evolución tecnológica y a los riesgos identificados. 
Estas revisiones deben contemplar tanto las APIs propias como las integraciones con terceros y permitir la 
adaptación de las medidas de seguridad cuando se introduzcan cambios relevantes en el diseño, el uso o el entorno 
de operación. 
Además, supervisa el cumplimiento de esta guía, conserva evidencias de los controles aplicados y adopta medidas 
correctoras cuando detecta desviaciones, debilidades o incumplimientos. 
6. Registros 
CHL - CheckList Controles de Seguridad en el Desarrollo 
Inventario de APIs internas y externas 
Configuraciones de seguridad de las APIs 
Resultados de pruebas de seguridad y análisis de vulnerabilidades 
Registro de incidencias y actuaciones realizadas 
Evidencias de revisiones y validaciones previas a producción 
7. Referencias 
OWASP (Open Web Application Security Project) 
CCN-CERT_BP-28 Recomendaciones sobre Desarrollo Seguro

# GUI - Ofuscación de Datos en Entornos no Productivos v1.0 - ES_firmado(1)

Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 1 de 19 
Versión 1.0 
 
 
 
 
 
 
 
 
 
 
 
 
Ofuscación de Datos en Entornos No 
Productivo  
Guía 
Autoritat Portuària de Barcelona 
 
 
 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 2 de 19 
Versión 1.0 
 
Información del documento: 
Título del documento 
Ofuscación de Datos en Entorno no Productivos 
Tipo de documento 
Guía 
Descripción 
Establece las reglas, responsabilidades y pasos operativos para evitar 
el uso de datos reales de producción en entornos no productivos y 
proteger la información sensible durante actividades de desarrollo, 
pruebas, formación, soporte, análisis técnico o resolución de 
incidencias. 
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
15/05/2026 
v1.0 
Revisión de 
Procedimiento 
Responsable de Seguridad 
de la Información (CISO) 
Revisión 
23/05/2026 
v1.0 
Aprobación de 
Procedimiento 
Responsable de Seguridad 
de la Información (CISO) 
Aprobación 
23/05/2026 
 
 
 
 
 
 
 
 
 
Historial de versiones 
 
Versión 
Descripción  
Autor 
Fecha  
v1.0 
Versión inicial del documento 
Oficina Técnica de Seguridad 
(Sothis) 
15/05/2026 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Control de distribución 
Descripción 
Área de difusión 
Fecha  
Todas las personas de las áreas de difusión indicadas 
Ciberseguridad, Desarrollo, Sistemas de 
Información  
 
 
 
 
 
 
 
Aviso: Este documento es propiedad de la Autoritat Portuària de Barcelona y contiene información clasificada según el nivel de seguridad definido, 
debiendo aplicarse las medidas de uso y custodia pertinentes, de acuerdo con lo establecido en las Políticas de Seguridad de la Información. 
 
Índice  
 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 3 de 19 
Versión 1.0 
 
1. 
Introducción ......................................................................................................................... 4 
2. 
Alcance ................................................................................................................................. 4 
3. 
Roles y responsabilidades .................................................................................................... 4 
4. 
Principio general .................................................................................................................. 5 
4.

1. 
Criterios de uso mínimo ................................................................................................... 5 
4.

2. 
Declaración de política interna ........................................................................................ 5 
4.

3. 
Buenas prácticas para equipos de desarrollo .................................................................. 5 
5. 
Clasificación y tipos de datos sujetos a ofuscación ............................................................. 6 
5.

1. 
Categorías de datos sujetas a ofuscación ........................................................................ 6 
5.

2. 
Datos que nunca deben copiarse a entornos no productivos ......................................... 7 
6. 
Entornos afectados .............................................................................................................. 7 
7. 
Técnicas de ofuscación ........................................................................................................ 7 
7.

1. 
Requisitos mínimos de los scripts .................................................................................... 8 
7.

2. 
Técnicas permitidas ......................................................................................................... 8 
7.2.

1. 
Sustitución o masking manual ............................................................................................................. 8 
7.2.

2. 
Seudonimización consistente .............................................................................................................. 8 
7.2.

3. 
Truncado o borrado parcial ................................................................................................................. 9 
7.2.

4. 
Borrado, nulificado o eliminación de campo ...................................................................................... 9 
7.2.

5. 
Randomización controlada .................................................................................................................. 9 
7.2.

6. 
Hash no reversible ............................................................................................................................... 9 
7.

3. 
Técnicas prohibidas ........................................................................................................ 10 
7.

4. 
Selección rápida de técnica ............................................................................................ 10 
8. 
Procedimiento operativo ................................................................................................... 10 
8.

1. 
Flujo básico..................................................................................................................... 11 
8.

2. 
Checklist obligatorio antes de usar los datos ................................................................ 13 
9. 
Controles y auditoría ......................................................................................................... 14 
1

0. 
Excepciones........................................................................................................................ 14 
1

1. 
Revisión y mejora continua ............................................................................................... 14 
1

2. 
Registros ............................................................................................................................ 15 
1

3. 
Referencias ........................................................................................................................ 15 
1

4. 
Anexos ................................................................................................................................ 16 
14.

1. Anexo I. Plantilla de solicitud de datos ofuscados ......................................................... 16 
14.

2. Anexo II. Plantilla de matriz de ofuscación .................................................................... 17 
14.

3. Anexo III. Plantilla de cabecera para scripts .................................................................. 17 
14.

4. Anexo IV. Reglas prácticas por tipo de soporte ............................................................. 17 
14.

5. Anexo V. Criterios de aceptación del dataset ofuscado ................................................ 18 
 
 
 
 
 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 4 de 19 
Versión 1.0 
 
1. Introducción 
La Autoritat Portuària de Barcelona establece las reglas, responsabilidades y pasos operativos para evitar el uso de 
datos reales de producción en entornos no productivos y proteger la información sensible durante actividades de 
desarrollo, pruebas, formación, soporte, análisis técnico o resolución de incidencias. 
El objetivo principal es que cualquier dato procedente de producción que deba ser utilizado fuera del entorno 
productivo sea previamente ofuscado mediante scripts controlados, reproducibles y trazables, de forma que: 
• 
No permita identificar directamente a personas físicas, usuarios, clientes, empleados, viajeros u otros 
interesados. 
• 
No contenga credenciales, secretos, tokens, claves o configuraciones reales. 
• 
Mantenga, cuando sea necesario, la integridad funcional de la aplicación para permitir pruebas válidas. 
• 
Reduzca el riesgo de fuga, acceso indebido o reidentificación. 
• 
Permita demostrar el cumplimiento dentro del marco S-SDLC. 
2. Alcance 
La presente guía aplica a cualquier solicitud de uso de datos reales o procedentes de producción en entornos no 
productivos de la Autoritat Portuària de Barcelona, incluyendo: 
• 
Bases de datos relacionales y no relacionales; 
• 
Ficheros planos, CSV, JSON, XML, Excel u otros formatos exportados; 
• 
Logs de aplicación, logs técnicos, trazas, volcados o evidencias de incidencias; 
• 
Exportaciones desde herramientas, informes, cuadros de mando o sistemas de terceros; 
• 
Copias parciales o completas de tablas, esquemas, colecciones, buckets o repositorios de documentos; 
• 
Adjuntos, imágenes, documentos escaneados o evidencias funcionales. 
3. Roles y responsabilidades 
La ofuscación de datos de producción para su uso en entornos no productivos en la Autoritat Portuària de Barcelona 
requiere la participación coordinada de los siguientes roles: 
• 
Responsable de Seguridad de la Información / CISO: define los requisitos mínimos de seguridad, valida los 
criterios de ofuscación, supervisa los riesgos asociados al uso de datos de producción y aprueba las 
excepciones que correspondan. 
• 
Responsable del Sistema / Propietario de la Aplicación: autoriza o rechaza la solicitud de uso de datos 
procedentes de producción, valida la necesidad funcional, confirma que el alcance es proporcional y 
asegura que los datos se utilizan únicamente para la finalidad aprobada. 
• 
Responsable de Sistemas / Operaciones: garantiza la extracción controlada de los datos, la custodia 
temporal de la información original, la aplicación técnica de los scripts de ofuscación y la carga segura del 
dataset ofuscado en el entorno destino. 
• 
Responsable del Área de Desarrollo: asegura que los equipos de desarrollo aplican el principio de no uso 
de datos reales en entornos no productivos y promueve el uso preferente de datos sintéticos o previamente 
ofuscados. 
• 
Jefe de Proyecto: supervisa que la solicitud, aprobación, ofuscación, validación y carga de los datos se 
realizan conforme a esta guía antes de su uso en actividades de desarrollo, pruebas o preproducción. 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 5 de 19 
Versión 1.0 
 
• 
Responsable Técnico: identifica las tablas, ficheros, campos y relaciones necesarias para las pruebas, 
colabora en la definición de las reglas de ofuscación y valida que el dataset mantiene la integridad funcional 
requerida. 
• 
DBA / Equipo técnico autorizado: recibe, revisa y ejecuta los scripts de ofuscación generados por el equipo 
de desarrollo,, conserva las evidencias técnicas, verifica la correcta transformación de los datos y asegura 
que no se entregan datos reales a los equipos no productivos. 
• 
Equipos de Desarrollo y QA: justifican la necesidad de los datos, utilizan únicamente datasets autorizados 
y ofuscados, evitan copias no controladas y comunican cualquier dato real detectado en entornos no 
productivos. Es responsable de la generación de los scripts de ofuscación conforme a los requisitos 
funcionales y de seguridad establecidos. 
• 
Delegado de Protección de Datos / DPO, cuando aplique: asesora en los casos que impliquen datos 
personales de especial sensibilidad, alto riesgo de reidentificación o excepciones que requieran valoración 
normativa adicional. 
• 
Usuarios autorizados del entorno no productivo: utilizan los datos ofuscados conforme a la finalidad 
aprobada, respetan las restricciones de acceso y comunican cualquier uso indebido, exposición accidental 
o sospecha de datos reales. 
4. Principio general 
Queda prohibido el uso de datos reales en cualquier entorno no productivo sin aplicar previamente técnicas de 
ofuscación autorizadas, documentadas y validadas. 
Siempre que sea posible, se priorizará el uso de datos sintéticos generados específicamente para pruebas. Solo se 
permitirá el uso de datos procedentes de producción cuando exista una necesidad técnica justificada y aprobada. 
4.

1. Criterios de uso mínimo 
Antes de solicitar datos de producción, el equipo solicitante deberá valorar, en este orden: 
1. Si la prueba puede realizarse con datos sintéticos; 
2. Si basta con un subconjunto reducido de datos; 
3. Si puede utilizarse una muestra agregada o anonimizada; 
4. Si es imprescindible utilizar datos procedentes de producción previamente ofuscados. 
No se autorizarán extracciones completas de producción si la necesidad puede cubrirse con una muestra menor. 
4.

2. Declaración de política interna 
Se prohíbe el uso de datos reales de producción en entornos de desarrollo, testing, preproducción, formación o 
soporte sin aplicar previamente técnicas de ofuscación aprobadas. Toda solicitud de datos procedentes de 
producción deberá estar justificada, autorizada, clasificada, tratada mediante scripts reproducibles y validada antes 
de su carga en cualquier entorno no productivo. Las credenciales, secretos, tokens y datos biométricos reales no 
podrán utilizarse en entornos no productivos, salvo excepción formal aprobada por el Responsable del Sistema y 
Seguridad/CISO, con medidas reforzadas de seguridad y caducidad definida. 
4.

3. Buenas prácticas para equipos de desarrollo 
• 
No solicitar datos de producción por defecto. 
• 
Usar datos sintéticos siempre que sea posible. 
• 
Diseñar pruebas automatizadas con datasets ficticios. 
• 
No guardar exportaciones en local salvo autorización. 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 6 de 19 
Versión 1.0 
 
• 
No subir datasets a repositorios de código. 
• 
No incluir datos reales en capturas, evidencias o tickets. 
• 
No pegar datos reales en herramientas colaborativas o chats. 
• 
Notificar inmediatamente si se detectan datos reales en DEV, TEST o PRE. 
• 
Revisar que las pruebas no envían emails, SMS o notificaciones a destinatarios reales. 
• 
Usar configuraciones de prueba para integraciones externas. 
5. Clasificación y tipos de datos sujetos a ofuscación 
La Autoritat Portuària de Barcelona debe aplicar la clasificación de datos de forma obligatoria antes de cualquier 
extracción, transformación o carga en entornos no productivos. No se podrá ejecutar el proceso si no se ha 
identificado previamente qué campos, ficheros o columnas contienen información sensible. 
5.

1. Categorías de datos sujetas a ofuscación 
Nivel alto: ofuscación obligatoria 
Los datos clasificados como nivel alto deberán ofuscarse siempre. No podrán cargarse en DEV, TEST o PRE en formato 
real. Incluyen, entre otros: 
• 
Datos personales identificativos: nombre; apellidos; DNI, NIE, pasaporte u otros documentos 
identificativos; dirección postal; teléfono; correo electrónico; fecha de nacimiento cuando permita 
identificar o perfilar a una persona; firma manuscrita o electrónica visible; imágenes de documentos 
personales. 
• 
Datos biométricos: huellas dactilares; imágenes faciales utilizadas para identificación; plantillas 
biométricas; datos de reconocimiento facial, iris, voz u otros rasgos biométricos. 
• 
Datos de control fronterizo o sistemas EES, si aplica: registros de entrada y salida asociados a personas 
identificables; documentos de viaje; itinerarios individuales; datos biométricos asociados a control 
fronterizo; decisiones, alertas o eventos asociados a un viajero concreto. 
• 
Credenciales y secretos: contraseñas; hashes de contraseñas reales; tokens de sesión; API keys; claves 
privadas; certificados; cadenas de conexión; secretos de configuración; códigos de recuperación; OTP o 
semillas MFA. 
Regla para nivel alto: estos datos deberán sustituirse, eliminarse, truncarse, seudonimizarse o reemplazarse por 
valores ficticios. Las credenciales y secretos no se ofuscan: se eliminan o sustituyen por valores inválidos de prueba. 
Nivel medio: ofuscación recomendada y evaluación obligatoria 
Los datos de nivel medio no siempre identifican directamente, pero pueden facilitar la reidentificación cuando se 
combinan con otros campos. Deberán evaluarse y, salvo justificación documentada, ofuscarse. 
• 
Incluyen: identificadores internos de usuario; IDs de cliente; matrículas; códigos de expediente; códigos de 
reserva; identificadores de operación; números de contrato; referencias de caso; logs con identificadores; 
historiales de acciones; direcciones IP; identificadores de dispositivo; identificadores de sesión; datos de 
actividad individualizada. 
Regla para nivel medio: se mantendrán solo cuando sean imprescindibles para conservar relaciones funcionales. En 
ese caso, deberán reemplazarse por identificadores ficticios consistentes. 
Nivel bajo: evaluación caso a caso 
Los datos de nivel bajo podrán utilizarse sin ofuscación únicamente cuando no permitan identificar directa ni 
indirectamente a una persona, sistema, cliente, operación o expediente. 
• 
Incluyen: datos agregados; estadísticas globales; contadores; métricas técnicas sin identificadores; 
metadatos sin identificación directa; catálogos genéricos sin datos personales. 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 7 de 19 
Versión 1.0 
 
Regla para nivel bajo: aunque no requieran ofuscación automática, deberán revisarse para evitar combinaciones 
que permitan reidentificación. 
5.

2. Datos que nunca deben copiarse a entornos no productivos 
No se permite cargar en DEV, TEST o PRE:  
• 
contraseñas reales o hashes reales de contraseñas;  
• 
tokens o sesiones activas; 
• 
claves privadas o certificados reales; 
• 
API keys reales; 
• 
semillas MFA; 
• 
datos biométricos reales salvo excepción formal con aprobación reforzada; 
• 
documentos oficiales escaneados reales salvo excepción formal con aprobación reforzada; 
• 
información que permita acceso a servicios reales de terceros. 
Si durante una extracción aparecen credenciales o secretos reales, se deberá comunicar a Seguridad y valorar la 
rotación de dichos secretos. 
6. Entornos afectados 
Este procedimiento aplica a los siguientes entornos: 
• 
DEV: desarrollo local, integración de desarrolladores, entornos compartidos de desarrollo y sandboxes. 
• 
TEST: pruebas funcionales, integración, regresión, rendimiento, automatización o QA. 
• 
PRE: preproducción, staging, certificación, validación de usuario o simulación previa al despliegue. 
También aplica a: 
• 
entornos temporales; 
• 
entornos cloud efímeros; 
• 
pipelines de CI/CD; 
• 
máquinas locales de desarrollo; 
• 
herramientas de análisis o soporte; 
• 
repositorios de evidencias; 
• 
espacios colaborativos donde se compartan exportaciones. 
Regla general: Queda prohibido el uso de datos reales en cualquier entorno no productivo sin aplicar previamente 
técnicas de ofuscación. 
Regla complementaria: La ofuscación deberá realizarse antes de que los datos estén disponibles para equipos de 
desarrollo, QA, proveedores o usuarios de entornos no productivos. 
7. Técnicas de ofuscación 
Las técnicas de ofuscación se implementarán mediante scripts SQL, Python u otros lenguajes aprobados por la 
organización. Los scripts deberán ser controlados, versionados, revisables y reutilizables. 
La técnica elegida dependerá del tipo de dato, del riesgo de reidentificación y de la necesidad funcional de la prueba. 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 8 de 19 
Versión 1.0 
 
7.

1. Requisitos mínimos de los scripts 
Todo script de ofuscación deberá cumplir los siguientes criterios: ser reproducible; estar versionado en repositorio 
autorizado o adjunto al ticket correspondiente; estar asociado a una solicitud aprobada; identificar claramente las 
tablas, campos, ficheros o columnas afectados; no contener credenciales embebidas; no guardar datos reales en 
logs de ejecución; permitir revisión técnica; generar evidencias de ejecución; preservar la integridad referencial 
cuando sea necesario; ejecutarse en una zona controlada, nunca directamente sobre producción salvo tareas 
estrictamente autorizadas de extracción. 
7.

2. Técnicas permitidas 
7.2.

1. Sustitución o masking manual 
Consiste en reemplazar valores reales por valores ficticios que mantengan el formato esperado por la aplicación. 
Ejemplos: 
• 
nombres reales → nombres ficticios; 
• 
apellidos reales → apellidos ficticios; 
• 
emails reales → usuario_000001@test.local; 
• 
teléfonos reales → 600000001, 600000002, etc.; 
• 
direcciones reales → Calle Ficticia 1, Ciudad Prueba; 
• 
matrículas reales → 0000-TEST. 
Uso recomendado: datos identificativos directos cuando la aplicación necesita un valor con formato válido. 
Buenas prácticas: 
• 
utilizar dominios no reales, por ejemplo test.local; 
• 
no usar nombres de personas reales conocidas; 
• 
no generar emails que puedan enviarse accidentalmente a dominios reales; 
• 
mantener longitud y formato si la aplicación lo requiere; 
• 
documentar el patrón utilizado. 
7.2.

2. Seudonimización consistente 
Consiste en reemplazar un identificador real por otro ficticio de forma consistente, manteniendo las relaciones entre 
tablas o ficheros. 
Ejemplo: 
• 
user_12345 → user_00001; 
• 
cliente_98765 → cliente_00001; 
• 
expediente_ABC123 → expediente_

00001. 
Uso recomendado: cuando la aplicación necesita conservar relaciones entre entidades, por ejemplo usuario-pedido, 
cliente-expediente o viajero-evento. 
Reglas: 
• 
la tabla de correspondencia, si existe, no deberá cargarse en entornos no productivos; 
• 
la correspondencia deberá almacenarse separada, cifrada o protegida, y solo mientras sea necesaria; 
• 
el acceso a la correspondencia quedará restringido a personal autorizado; 
• 
si no es necesario revertir el proceso, se preferirá una seudonimización no reversible. 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 9 de 19 
Versión 1.0 
 
7.2.

3. Truncado o borrado parcial 
Consiste en conservar solo una parte limitada del valor original, eliminando el resto. 
Ejemplos: 
• 
DNI 12345678A → 1234****; 
• 
IBAN ES7620770024003102575766 → **********************5766; 
• 
tarjeta 4111111111111111 → ************1111; 
• 
teléfono 612345678 → 612***

678. 
Uso recomendado: cuando se requiere mostrar parcialmente un dato para validar pantallas, formatos o 
integraciones, pero no es necesario conservar el valor completo. 
Limitación: no debe utilizarse si los caracteres conservados, junto con otros campos, permiten reidentificación 
razonable. 
7.2.

4. Borrado, nulificado o eliminación de campo 
Consiste en eliminar el dato sensible o sustituirlo por NULL, vacío o un valor fijo no sensible. 
Ejemplos: 
• 
token real → NULL; 
• 
contraseña → NULL; 
• 
clave privada → eliminada; 
• 
adjunto con documento real → sustituido por documento ficticio; 
• 
campo biométrico → NULL. 
Uso recomendado: credenciales, secretos, biométricos, documentos oficiales, adjuntos sensibles o campos no 
necesarios para la prueba. 
7.2.

5. Randomización controlada 
Consiste en alterar datos de forma aleatoria dentro de rangos definidos, manteniendo coherencia funcional. 
Ejemplos: 
• 
fechas desplazadas entre -30 y +30 días; 
• 
importes alterados dentro de un rango permitido; 
• 
códigos de oficina sustituidos por códigos válidos de prueba; 
• 
coordenadas generalizadas a una zona amplia. 
Uso recomendado: fechas, importes, métricas o valores numéricos que deben conservar distribución aproximada 
sin revelar valores reales. 
Buenas prácticas: 
• 
documentar el rango de alteración; 
• 
evitar que la aleatorización rompa reglas de negocio; 
• 
mantener coherencia entre campos relacionados, por ejemplo, fecha de alta anterior a fecha de baja; 
• 
no alterar importes de forma que se generen casos imposibles si son necesarios para pruebas. 
7.2.

6. Hash no reversible 
Consiste en transformar un valor mediante una función hash para obtener un identificador no legible. 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 10 de 19 
Versión 1.0 
 
Ejemplo: 
• 
email real → hash SHA-256; 
• 
ID externo → hash SHA-

256. 
Uso recomendado: identificadores que no deben leerse, pero deben compararse de forma consistente. 
Condiciones mínimas: 
• 
no utilizar hash simple para datos de baja entropía o fácilmente adivinables, como DNI, teléfono o email, 
sin medidas adicionales; 
• 
cuando sea necesario evitar ataques por diccionario, utilizar sal o clave secreta gestionada de forma segura; 
• 
no almacenar la sal o clave junto al dataset ofuscado; 
• 
no usar el hash como técnica única si el resto de campos, permite reidentificación. 
7.

3. Técnicas prohibidas 
Quedan prohibidas las siguientes prácticas: 
• 
copiar datos de producción directamente a DEV, TEST o PRE sin tratamiento; 
• 
compartir exportaciones reales por correo, mensajería o carpetas no autorizadas; 
• 
ofuscar manualmente sin script ni evidencia; 
• 
utilizar datos reales porque facilita la prueba; 
• 
dejar credenciales reales en bases de datos, ficheros o logs; 
• 
almacenar tablas de correspondencia en el mismo entorno que el dataset ofuscado; 
• 
aplicar ofuscación reversible sin autorización y sin control de acceso; 
• 
utilizar dominios de email reales para datos ficticios; 
• 
registrar en logs los valores originales antes de ofuscarlos; 
• 
reutilizar datasets antiguos sin verificar que siguen cumpliendo el procedimiento; 
• 
cargar datos ofuscados sin validación previa. 
7.

4. Selección rápida de técnica 
Necesidad funcional 
Técnica recomendada 
Probar pantallas con nombres y emails 
Sustitución por valores ficticios 
Mantener relaciones entre tablas 
Seudonimización consistente 
Mostrar solo parte de un dato 
Truncado o borrado parcial 
Campo no necesario para la prueba 
Borrado o nulificado 
Probar lógica con fechas realistas 
Randomización controlada 
Comparar igualdad sin revelar valor 
Hash con controles adicionales 
Eliminar credenciales reales 
Nulificado o sustitución por valor inválido 
8. Procedimiento operativo 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 11 de 19 
Versión 1.0 
 
8.

1. Flujo básico 
El proceso se realizará en cinco fases obligatorias. 
Fase 

1. Solicitud de datos 
El equipo solicitante deberá registrar una solicitud formal mediante el canal definido por la organización, 
herramienta ITSM o de gestión de proyectos corporativa. 
La solicitud deberá incluir como mínimo: 
• 
sistema o aplicación afectada; 
• 
responsable funcional o técnico solicitante; 
• 
finalidad de uso; 
• 
justificación de por qué no sirven datos sintéticos; 
• 
entorno destino: DEV, TEST o PRE; 
• 
tipo de datos solicitados; 
• 
volumen estimado; 
• 
periodo temporal requerido; 
• 
tablas, ficheros o entidades necesarias; 
• 
duración prevista de uso; 
• 
usuarios o equipos que accederán al dataset; 
• 
fecha prevista de eliminación; 
• 
aprobación del responsable del sistema. 
No se iniciará ninguna extracción sin solicitud registrada y aprobada. 
 
Fase 

2. Evaluación y clasificación 
Antes de extraer los datos, el responsable técnico, junto con Operaciones y Seguridad cuando aplique, deberá 
revisar: 
• 
qué campos contienen datos de nivel alto, medio o bajo; 
• 
qué datos son estrictamente necesarios; 
• 
qué datos pueden eliminarse de la extracción; 
• 
qué técnica de ofuscación se aplicará a cada campo; 
• 
si existen relaciones que deben mantenerse; 
• 
si hay riesgo de reidentificación por combinación de campos; 
• 
si hay credenciales, secretos o tokens que deban eliminarse. 
El resultado será una matriz de ofuscación por tabla, fichero o campo. 
 
Fase 

3. Extracción controlada 
La extracción será realizada únicamente por personal autorizado, normalmente Operaciones, DBA o equipo 
equivalente. 
Reglas de extracción: 
• 
extraer solo los datos aprobados; 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 12 de 19 
Versión 1.0 
 
• 
utilizar una muestra mínima suficiente; 
• 
evitar extracciones completas salvo autorización expresa; 
• 
almacenar temporalmente la extracción en una zona segura de tratamiento; 
• 
cifrar la transferencia si aplica; 
• 
restringir el acceso a la extracción original; 
• 
no entregar la extracción original a Desarrollo ni QA; 
• 
eliminar la extracción original una vez validada la ofuscación, salvo obligación justificada de conservación 
temporal. 
La extracción original se considera dato de producción y deberá protegerse como tal. 
 
Fase 

4. Ofuscación mediante scripts 
Operaciones, DBA o el equipo autorizado ejecutará los scripts de ofuscación en la zona controlada. 
Los scripts deberán: 
• 
aplicar las reglas definidas en la matriz de ofuscación; 
• 
sustituir, seudonimizar, truncar, borrar o aleatorizar según corresponda; 
• 
eliminar credenciales y secretos; 
• 
mantener integridad referencial cuando sea necesario; 
• 
generar log técnico de ejecución sin datos sensibles; 
• 
registrar fecha, hora, versión del script y responsable de ejecución. 
No se permitirá la edición manual de datos sin script, salvo casos excepcionales documentados y validados. 
 
Fase 

5. Validación 
Antes de cargar los datos en el entorno destino, se deberá validar que el dataset resultante cumple este 
procedimiento. 
La validación incluirá: 
• 
revisión de que no existen identificadores reales directos; 
• 
verificación de que no hay credenciales reales; 
• 
comprobación de que las relaciones funcionales necesarias se mantienen; 
• 
muestreo de tablas, ficheros y logs; 
• 
ejecución de consultas o reglas de detección de patrones sensibles; 
• 
revisión por responsable técnico o Seguridad cuando aplique. 
Si la validación falla, el dataset no podrá cargarse y deberá repetirse la ofuscación. 
 
Fase 

6. Carga en entorno destino 
Una vez validado, el dataset ofuscado podrá cargarse en DEV, TEST o PRE. 
Reglas de carga:  
• 
cargar únicamente el dataset ofuscado; 
• 
limitar permisos de acceso al equipo autorizado; 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 13 de 19 
Versión 1.0 
 
• 
evitar copias adicionales no controladas; 
• 
registrar fecha de carga; 
• 
asociar el dataset al ticket o registro de solicitud; 
• 
definir fecha de caducidad o eliminación; 
• 
no reutilizar el dataset para fines distintos a los aprobados sin nueva revisión. 
• 
 
Fase 

7. Eliminación o renovación 
Al finalizar la necesidad que motivó la solicitud, el dataset deberá eliminarse o renovarse con nueva aprobación. 
La eliminación deberá registrarse indicando: dataset eliminado; entorno; fecha; responsable; evidencia de 
eliminación cuando aplique. 
 
8.

2. Checklist obligatorio antes de usar los datos 
Antes de utilizar el dataset en un entorno no productivo se deberá confirmar: 
Control 
Sí/No 
Observaciones 
Existe solicitud registrada 
Existe justificación del uso de datos procedentes de producción 
El responsable del sistema ha autorizado la solicitud 
Se ha realizado clasificación de datos 
Se ha definido matriz de ofuscación 
 
 
No hay nombres, apellidos o documentos reales visibles 
No hay emails reales 
No hay teléfonos reales 
No hay direcciones reales 
No hay credenciales, tokens, API keys ni secretos reales 
Los datos biométricos reales han sido eliminados o sustituidos 
Los identificadores internos han sido seudonimizados si aplica 
No se puede reidentificar fácilmente a una persona 
Se mantiene la integridad funcional necesaria 
Se han validado relaciones entre tablas/ficheros 
Se han conservado los scripts usados 
 
 
Se ha registrado responsable, fecha y versión del dataset 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 14 de 19 
Versión 1.0 
 
Se ha definido fecha de caducidad o eliminación 
 
 
 
El dataset solo podrá utilizarse cuando todos los controles obligatorios estén marcados como satisfactorios o exista 
una excepción aprobada. 
9. Controles y auditoría 
Seguridad/CISO, o el área que se designe, realizará revisiones periódicas para comprobar que los datos utilizados en 
DEV, TEST y PRE han sido correctamente ofuscados y que no existen datos reales no autorizados. Estas revisiones se 
realizarán, como mínimo, de forma trimestral, o con mayor frecuencia en sistemas críticos o de alto riesgo. 
• 
Las revisiones podrán incluir la comprobación de las solicitudes aprobadas, los scripts utilizados, las 
evidencias de validación, los permisos de acceso y la caducidad de los datasets. También podrán realizarse 
muestreos sobre bases de datos, ficheros, logs o exportaciones para verificar que no contienen datos 
personales reales, credenciales, secretos, tokens u otra información sensible. 
• 
Cuando sea posible, se ejecutarán controles técnicos mediante consultas o scripts de verificación para 
detectar patrones de riesgo, como emails reales, DNI/NIE/pasaportes, teléfonos, claves, tokens, direcciones 
IP públicas no necesarias, adjuntos reales o datos biométricos no eliminados. 
El cumplimiento de esta guía podrá medirse mediante indicadores como el porcentaje de entornos revisados sin 
datos reales, el número de datasets ofuscados correctamente, el número de incidencias por uso indebido de datos, 
el porcentaje de solicitudes con evidencias completas, el número de excepciones aprobadas y el número de datasets 
eliminados al finalizar su uso. 
Si se detectan datos reales no autorizados en un entorno no productivo, se deberá restringir el acceso al dataset, 
notificar al Responsable del Sistema y a Seguridad/CISO, analizar el origen de la carga y eliminar o aislar los datos 
afectados. Además, se valorará si existe un incidente de seguridad o una posible brecha de datos personales, se 
corregirán las reglas o scripts aplicados y se documentarán las acciones correctivas. 
1

0. 
Excepciones 
Las excepciones a esta guía tendrán carácter extraordinario y solo podrán autorizarse cuando exista una necesidad 
técnica justificada y no sea viable utilizar datos sintéticos u ofuscados. 
• 
Toda excepción deberá estar documentada, aprobada y limitada a una finalidad, entorno, plazo y grupo de 
usuarios concretos. Para ello, se seguirá el Procedimiento de Solicitud de excepciones de incumplimiento 
de políticas IT corporativo. 
• 
La autorización requerirá, como mínimo, la aprobación del Responsable del Sistema y de Seguridad/CISO.  
• 
Cuando la excepción afecte a datos personales de especial sensibilidad, datos biométricos, información de 
alto riesgo o exista duda normativa, deberá consultarse también al Delegado de Protección de Datos / DPO. 
• 
Toda excepción deberá contar con medidas adicionales de seguridad como: acceso restringido por lista 
nominal, caducidad corta, registro de accesos, prohibición de copias no autorizadas, cifrado cuando aplique, 
eliminación verificada al finalizar el uso y revisión posterior de las lecciones aprendidas. 
• 
Las excepciones deberán registrarse indicando el sistema afectado: motivo, datos incluidos, entorno 
destino, aprobadores, fecha de caducidad, medidas adicionales y estado.  
• 
Al vencer la caducidad, la excepción deberá cerrarse formalmente y los datos deberán eliminarse o 
someterse a una nueva evaluación. 
1

1. 
Revisión y mejora continua 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 15 de 19 
Versión 1.0 
 
Este procedimiento deberá revisarse al menos una vez al año o cuando se produzca alguno de los siguientes eventos: 
• 
incorporación de nuevas tecnologías de base de datos; 
• 
cambios relevantes en arquitectura; 
• 
uso de nuevos entornos cloud o pipelines; 
• 
incidentes relacionados con datos reales en entornos no productivos; 
• 
cambios normativos o contractuales; 
• 
incorporación de herramientas automáticas de data masking; 
• 
resultados de auditoría que requieran mejora. 
Las lecciones aprendidas en pilotos S-SDLC deberán incorporarse al procedimiento antes de su extensión al resto de 
equipos de desarrollo. 
 
1

2. 
Registros 
• 
Solicitud de uso de datos de producción, incluyendo justificación, sistema afectado, entorno destino, 
responsable solicitante y aprobación correspondiente. 
• 
Matriz de clasificación y ofuscación de datos, indicando tablas, ficheros, campos afectados, nivel de 
sensibilidad y técnica de ofuscación aplicada. 
• 
CHL - Checklist de validación de datos ofuscados, donde se confirme que no existen datos reales 
identificativos, credenciales, secretos, tokens o información sensible no tratada. 
• 
Scripts de ofuscación utilizados, incluyendo versión, fecha de ejecución, responsable, sistema afectado y 
reglas aplicadas. 
• 
Evidencias de validación previa a la carga, como resultados de consultas, revisiones técnicas o 
comprobaciones realizadas antes de incorporar el dataset a DEV, TEST o PRE. 
• 
Registro de datasets ofuscados, indicando fecha de generación, entorno destino, responsable, caducidad y 
estado del dataset. 
• 
Registro de incidencias y actuaciones realizadas, en caso de detectarse datos reales no autorizados, errores 
de ofuscación o incumplimientos. 
• 
Registro de excepciones aprobadas, cuando se autorice de forma extraordinaria el uso de datos no 
ofuscados o parcialmente ofuscados. 
1

3. 
Referencias 
• 
OWASP - Open Web Application Security Project, como referencia general de buenas prácticas de seguridad 
en aplicaciones, protección de datos sensibles, gestión de secretos y controles de seguridad durante el 
desarrollo. OWASP mantiene guías prácticas, como sus Cheat Sheets, orientadas a ofrecer 
recomendaciones concretas y de alto valor para equipos técnicos y de desarrollo. 
• 
OWASP Cheat Sheet Series - User Privacy Protection, Database Security, Secrets Management y 
Cryptographic Storage, como apoyo para definir controles relacionados con privacidad, bases de datos, 
secretos, credenciales, cifrado y protección de información sensible. 
• 
OWASP Top 10, especialmente los riesgos asociados a exposición de información sensible, fallos de 
autenticación, credenciales y protección insuficiente de datos. 
• 
CCN-CERT BP/28 - Recomendaciones sobre Desarrollo Seguro, como referencia nacional de buenas 
prácticas para incorporar controles de seguridad a lo largo del ciclo de vida del desarrollo de software. El 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 16 de 19 
Versión 1.0 
 
CCN-CERT describe esta guía como un informe con recomendaciones detalladas para desarrollo seguro, 
incluyendo arquitectura, autenticación, sesiones y criptografía. 
 
1

4. 
Anexos 
14.

1. Anexo I. Plantilla de solicitud de datos ofuscados 
 
1. Datos generales 
• 
ID de solicitud/ticket: 
• 
Fecha: 
• 
Solicitante: 
• 
Equipo: 
• 
Sistema/aplicación: 
• 
Responsable del sistema: 
• 
Entorno destino: DEV / TEST / PRE 
2. Justificación 
• 
Finalidad de uso: 
• 
Motivo por el que no sirven datos sintéticos: 
• 
Pruebas o casos de uso afectados: 
• 
Fecha prevista de inicio: 
• 
Fecha prevista de fin: 
3. Datos requeridos 
• 
Tablas/ficheros/entidades solicitadas: 
• 
Campos necesarios: 
• 
Volumen estimado: 
• 
Periodo temporal: 
• 
¿Se requieren relaciones entre tablas? Sí / No 
• 
¿Se requieren adjuntos o documentos? Sí / No 
• 
¿Se requieren logs? Sí / No 
4. Clasificación inicial 
• 
Datos de nivel alto identificados: 
• 
Datos de nivel medio identificados: 
• 
Datos de nivel bajo identificados: 
• 
¿Existen credenciales o secretos? Sí / No 
• 
¿Existen datos biométricos? Sí / No 
• 
¿Existen datos EES o control fronterizo? Sí / No / No aplica 
5. Aprobaciones 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 17 de 19 
Versión 1.0 
 
• 
Responsable del sistema: 
• 
Seguridad/CISO, si aplica: 
• 
DPO/DPD, si aplica: 
 
14.

2. Anexo II. Plantilla de matriz de ofuscación 
Tabla/Fichero 
Campo 
Tipo de dato 
Nivel 
Técnica 
Regla concreta 
Mantener 
relación 
Validación esperada 
usuarios 
nombre 
Personal 
Alto 
Sustitución 
nombre ficticio 
No 
No 
aparecen 
nombres reales 
usuarios 
email 
Personal 
Alto 
Sustitución 
usuario_ID@tes
t.local 
Sí 
Todos terminan en 
@test.local 
usuarios 
id_usuario 
Identificador 
Medio 
Seudonimi
zación 
user_NNNNNN 
Sí 
Integridad 
con 
tablas hijas 
sesiones 
token 
Credencial 
Alto 
Nulificado 
NULL 
No 
 
14.

3. Anexo III. Plantilla de cabecera para scripts 
/* 
Nombre del script: mask_<sistema>_<dataset>_v1.sql 
Sistema: <nombre del sistema> 
Entorno destino: DEV / TEST / PRE 
Solicitud/Ticket: <ID> 
Versión: 1.0 
Fecha: <AAAA-MM-DD> 
Autor/Ejecutor: <nombre/equipo> 
Objetivo: Ofuscar datos procedentes de producción para uso no productivo. 
Tablas/Ficheros tratados: <lista> 
Campos sensibles tratados: <lista> 
Técnicas aplicadas: sustitución / seudonimización / truncado / nulificado / randomización / hash 
Reversible: Sí / No 
Ubicación de tabla de correspondencia, si aplica: <ubicación protegida o N/A> 
Validaciones posteriores: <consultas o controles> 
Observaciones: <texto> 
*/ 
14.

4. Anexo IV. Reglas prácticas por tipo de soporte 
Bases de datos 
• 
aplicar scripts en zona controlada; 
• 
evitar ejecución directa sobre producción; 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 18 de 19 
Versión 1.0 
 
• 
conservar scripts y logs técnicos; 
• 
validar integridad referencial; 
• 
eliminar tablas auxiliares con datos reales; 
• 
revisar campos libres, observaciones y comentarios, ya que suelen contener datos personales no 
estructurados. 
Ficheros CSV, Excel, JSON o XML 
• 
procesar mediante scripts Python, SQL externo o herramienta aprobada; 
• 
no editar manualmente salvo caso excepcional; 
• 
eliminar columnas no necesarias; 
• 
limpiar campos de texto libre; 
• 
validar que no quedan emails, teléfonos, documentos o identificadores reales; 
• 
guardar la versión ofuscada con nombre diferenciado. 
Logs 
• 
eliminar tokens, cabeceras de autenticación y cookies; 
• 
sustituir usuarios, emails, IPs y session IDs; 
• 
revisar trazas de error con parámetros de entrada; 
• 
no compartir logs completos si basta con fragmentos minimizados; 
• 
evitar que los logs ofuscados permitan reconstruir acciones individuales reales. 
Exportaciones e informes 
• 
priorizar agregación; 
• 
eliminar detalle individual si no es necesario; 
• 
sustituir identificadores; 
• 
revisar pestañas ocultas, metadatos y filtros; 
• 
validar que no hay datos reales en comentarios, nombres de hoja o propiedades del documento. 
Adjuntos, documentos e imágenes 
• 
sustituir por documentos ficticios; 
• 
eliminar documentos oficiales reales; 
• 
revisar metadatos del fichero; 
• 
no cargar imágenes faciales reales salvo excepción formal; 
• 
no incluir documentos escaneados reales en datasets de prueba. 
 
14.

5. Anexo V. Criterios de aceptación del dataset ofuscado 
Un dataset se considerará apto para uso en entornos no productivos cuando cumpla todos los criterios siguientes: 
1. La solicitud está aprobada y registrada. 
2. Existe clasificación de datos. 
3. Existe matriz de ofuscación. 
4. Se han aplicado scripts versionados. 

Ofuscación de Datos en Entornos No Productivos 
 
Oficina Técnica de Seguridad                               Interno 
GUI – Ofuscación de Datos en Entornos No Productivos 
Página 19 de 19 
Versión 1.0 
 
5. No contiene datos identificativos reales visibles. 
6. No contiene credenciales, secretos ni tokens reales. 
7. Los datos biométricos reales han sido eliminados o sustituidos. 
8. Los identificadores internos han sido sustituidos cuando exista riesgo de reidentificación. 
9. No se puede reidentificar razonablemente a personas mediante combinación de campos. 
1

0. Se mantiene la funcionalidad mínima necesaria para las pruebas. 
1

1. Existen evidencias de validación. 
1

2. Se ha definido caducidad o eliminación. 
1

3. El acceso al entorno destino está limitado a personas autorizadas. 
Si uno de estos criterios no se cumple, el dataset deberá rechazarse o tratarse como excepción formal.

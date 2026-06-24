# Política Backups v.1.5 - ES_firmado

Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 1 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
 
 
 
 
 
 
 
 
 
 
 
 
Copias de Seguridad 
Política 
Autoritat Portuària de Barcelona 
 
 
 
 

Política de copias de seguridad 
 
Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 2 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
Información del documento: 
Título del documento 
Política de Copias de Seguridad  
Tipo de documento 
Política 
Descripción 
Documento que establece las directrices básicas para la realización, 
almacenamiento y verificación de copias de seguridad de la 
información crítica, definiendo la frecuencia, los tipos de respaldo, 
los sistemas incluidos y las responsabilidades asociadas. Contempla 
la verificación periódica de la integridad de las copias y la realización 
de pruebas de restauración, con el fin de garantizar la disponibilidad 
y recuperación de la información ante incidentes, fallos técnicos o 
pérdidas de datos. 
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
v1.5 
Política de Copias de 
Seguridad 
Oficina Técnica de Seguridad 
(Sothis) 
Creación 
12/11/2025 
v1. 5 
Revisión de la Política 
Albert Prats- Responsable de 
Seguridad de la Información 
(CISO) 
Revisión 
12/11/2025 
v1. 5 
Revisión de la Política 
Albert Prats - Responsable 
de Seguridad de la 
Información (CISO) 
Aprobación 
12/11/2025 
 
 
 
 
 
 
 
Historial de versiones 
 
Versión 
Descripción  
Autor 
Fecha  
v1.0 
Versión Inicial del documento  
Omar Carazo (OTS) 
22/05/2019 
v1.1 
Procedimiento de Valoración de 
Riesgos 
Antonio Ponsico, Sergi Fernandez, 
Cristian Medrano 
23/05/2019 
v1.2 
Actualización del responsable de 
Seguridad 
Omar Carazo (OTS) 
25/05/2019 
V1.3 
Actualización del Responsable del 
Sistema 
Cristian Medrano 
27/05/2019 
v1.4 
Actualización del Responsable del 
Sistema 
Cristian Medrano 
17/04/2020 
v1.5 
Actualización de la Política de Copias 
de Seguridad 
Oficina Técnica de Seguridad 
(Sothis) 
12/11/2025 
 
 
Control de distribución 
 
Descripción 
Área de difusión 
Todas las personas de la Autoritat Portuària de Barcelona 
Todas 
 
 
 
 
 
 
Aviso: Este documento es propiedad de la Autoritat Portuària de Barcelona y contiene información clasificada según el nivel de seguridad definido, 
debiendo aplicarse las medidas de uso y custodia pertinentes, de acuerdo con lo establecido en las Políticas de Seguridad de la Información. 

Política de copias de seguridad 
 
Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 3 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
INDICE 
 
1. 
Introducción ......................................................................................................................... 4 
2. 
Alcance ................................................................................................................................. 4 
3. 
Roles y responsabilidades .................................................................................................... 4 
4. 
Inventario de bases de datos y repositorios de datos. ........................................................ 4 
5. 
Periodicidad de las copias de seguridad. ............................................................................. 5 
6. 
Almacenamiento de las copias de seguridad. ..................................................................... 5 
7. 
Conservación de las copias de seguridad. ........................................................................... 6 
8. 
Cifrado de las copias de seguridad. ..................................................................................... 6 
9. 
Acceso a las copias de seguridad ......................................................................................... 6 
1

0. 
Monitorización de las copias de seguridad. ........................................................................ 6 
1

1. 
Pruebas de recuperación. .................................................................................................... 7 
1

2. 
Borrado y gestión de soportes ............................................................................................. 7 
ANEXO I: GLOSARIO ......................................................................................................................... 7 
 
 
 

Política de copias de seguridad 
 
Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 4 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
1. Introducción 
La presente Política de Copias de Seguridad establece el marco de referencia para garantizar la protección y 
disponibilidad de la información crítica de la Autoritat Portuària de Barcelona mediante la realización sistemática 
de respaldos adecuados. Su finalidad es asegurar la continuidad de los servicios y la capacidad de recuperación de 
la información ante incidentes de seguridad, fallos técnicos o pérdidas de datos, definiendo principios comunes y 
responsabilidades para una gestión eficaz y controlada de las copias de seguridad. 
2. Alcance 
La presente política es de aplicación a los sistemas de información y activos digitales que soportan los servicios y 
procesos de la Autoritat Portuària de Barcelona y cuya pérdida o indisponibilidad pueda afectar a la continuidad de 
la actividad. 
El alcance comprende la información crítica, las aplicaciones, bases de datos, ficheros y repositorios de datos, así 
como las infraestructuras tecnológicas que los alojan o procesan, independientemente de su ubicación o del modelo 
de prestación del servicio. 
Asimismo, esta política será de obligado cumplimiento para el personal interno y terceros que intervengan en la 
gestión, ejecución o supervisión de las copias de seguridad. 
Quedan excluidos los sistemas o activos que, de forma justificada y documentada, no requieran copias de seguridad 
según los criterios de gestión de riesgos establecidos. 
3. Roles y responsabilidades 
• 
Responsable de Seguridad de la Información: vela por el cumplimiento de la política y su alineación con los 
requisitos legales y normativos. 
• 
Responsable de Sistemas: implanta y mantiene los mecanismos de copia de seguridad, asegurando su 
correcta ejecución y conservación. 
• 
Administradores de Sistemas: ejecutan y supervisan las copias de seguridad, gestionan los accesos y 
comunican incidencias. 
• 
Responsables de los Servicios o Activos: definen los requisitos de recuperación de los sistemas bajo su 
responsabilidad. 
4. Inventario de bases de datos y repositorios de datos. 
La gestión de las copias de seguridad se apoyará en un inventario actualizado de los servicios y sistemas de 
información que soportan la actividad de la Autoritat Portuària de Barcelona. Dicho inventario constituirá la 
referencia para la definición, planificación y control de las estrategias de respaldo. 
El inventario incluirá los repositorios de información y los sistemas asociados, tales como bases de datos, ficheros, 
aplicaciones, servidores y las configuraciones de la electrónica de red que soportan los servicios (routers, switches, 
firewalls y otros dispositivos de comunicaciones). Estos elementos se consideran información crítica para la 
recuperación de los sistemas y permiten identificar de forma clara los activos sujetos a copia de seguridad. 
Los servicios inventariados deberán clasificarse en función de su nivel de criticidad, con el fin de priorizar las medidas 
de protección y recuperación, estableciendo al menos las siguientes categorías: 
• 
Alto: Servicios cuya indisponibilidad inmediata, como consecuencia de un incidente, puede causar un 
impacto grave en la operativa y los objetivos de la organización. 
• 
Medio: Servicios cuya indisponibilidad puede afectar de forma significativa a la organización en el medio 
plazo. 

Política de copias de seguridad 
 
Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 5 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
• 
Bajo: Servicios cuya indisponibilidad tendría un impacto limitado o asumible en el largo plazo. 
La clasificación de los servicios y la definición de las estrategias de copia de seguridad deberán tener en cuenta los 
objetivos de recuperación asociados a cada uno de ellos, en particular el RPO (Recovery Point Objective) y el RTO 
(Recovery Time Objective) establecidos. 
5. Periodicidad de las copias de seguridad. 
La frecuencia de realización de las copias de seguridad se establecerá en función de un análisis previo que tendrá en 
cuenta, entre otros, los siguientes factores: 
• 
El volumen de información generada o modificada. 
• 
El impacto del coste de almacenamiento. 
• 
Los requisitos legales y regulatorios aplicables, en particular los relacionados con la protección de datos 
personales. 
De acuerdo con la normativa de protección de datos, deben aplicarse medidas que aseguren la disponibilidad y 
recuperación de la información, evitando la pérdida accidental de datos personales. 
En función de las necesidades de cada servicio y de su nivel de criticidad, se establece la siguiente periodicidad 
mínima para la realización de las copias de seguridad: 
• 
Copias incrementales diarias de los datos. 
• 
Copias completas semanales de la totalidad de la información. 
• 
Conservación mensual de al menos una de las copias completas semanales. 
6. Almacenamiento de las copias de seguridad. 
Para garantizar la disponibilidad y protección de la información, las copias de seguridad se almacenarán siguiendo 
el principio de múltiples copias y ubicaciones diferenciadas. En concreto, se mantendrán tres copias de seguridad, 
cumpliendo las siguientes condiciones: 
• 
Dos copias se almacenarán en soportes físicos distintos, separados y aislados de los datos originales. 
• 
Una tercera copia se almacenará en una ubicación diferente, preferiblemente externa. 
Almacenamiento en la Nube 
Al menos una de las copias de seguridad deberá almacenarse en la nube. Para los datos y servicios clasificados con 
criticidad alta, se aplicarán las siguientes medidas adicionales: 
• 
Almacenamiento en la nube de una copia completa semanal, con una retención de dos meses. 
• 
Almacenamiento en la nube de dos copias mensuales, con una retención de dos años. 
En el caso de servicios que ya se presten íntegramente en la nube, el proveedor deberá garantizar, mediante 
acuerdos de nivel de servicio (SLA), un plazo de restauración razonable que asegure la recuperación completa de los 
datos ante incidentes de seguridad o pérdidas de información. 
Seguridad y Separación de las Copias 
Las copias de seguridad y los procedimientos de recuperación deberán conservarse en una ubicación distinta de 
aquella en la que se encuentren los sistemas que tratan los datos, especialmente cuando se trate de información de 
carácter personal de alta sensibilidad, conforme a la normativa de protección de datos. 
Asimismo, los repositorios de copias de seguridad deberán mantenerse aislados del resto de sistemas, tanto a nivel 
de red y comunicaciones como de control de accesos. El acceso a estos repositorios estará restringido 
exclusivamente al personal autorizado y responsable de su gestión. 

Política de copias de seguridad 
 
Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 6 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
Cuando se utilicen servicios de almacenamiento en la nube, se deberán exigir al proveedor las garantías de seguridad 
necesarias, asegurando que se cumplen los requisitos establecidos por la organización y la normativa aplicable. 
Gestión de Soportes 
Deberá realizarse una revisión periódica del estado y ciclo de vida de los soportes de almacenamiento. Asimismo, 
todos los soportes utilizados para las copias de seguridad deberán estar inventariados y etiquetados, indicando, al 
menos, el tipo de copia, la fecha de realización, el responsable y los sistemas o datos incluidos. 
7. Conservación de las copias de seguridad. 
Las copias de seguridad se conservarán durante los siguientes periodos mínimos, en función de su tipo: 
• 
Copias incrementales diarias: conservación durante 30 días. 
• 
Copias completas semanales: conservación durante 2 meses. 
• 
Copias completas mensuales: conservación durante 2 años. 
Adicionalmente, se conservarán dos copias mensuales con retención indefinida, que no estarán sujetas al periodo 
de eliminación establecido. Estas copias deberán seleccionarse de forma que estén separadas en el tiempo de 
manera adecuada, preferiblemente con una diferencia aproximada de seis meses entre ellas. 
8. Cifrado de las copias de seguridad. 
Todas las copias de seguridad deberán almacenarse cifradas, independientemente del tipo de información que 
contengan y de su ubicación. Esta medida es obligatoria, especialmente cuando las copias se almacenen fuera de las 
instalaciones de la Autoritat Portuària de Barcelona, incluidos los entornos en la nube. 
La transmisión de las copias de seguridad hacia repositorios externos se realizará exclusivamente mediante canales 
seguros, utilizando protocolos de comunicación cifrados (por ejemplo, SSL/TLS). 
Las claves de cifrado deberán gestionarse de forma segura y no podrán almacenarse junto con las copias de 
seguridad cifradas. Asimismo, deberán protegerse frente a accesos no autorizados mediante controles adecuados. 
9. Acceso a las copias de seguridad 
El acceso a las copias de seguridad estará estrictamente limitado al personal autorizado, de acuerdo con el principio 
de mínimo privilegio, y únicamente para el desempeño de las funciones asignadas. 
• 
Los procesos o sistemas automatizados que realicen copias de seguridad dispondrán exclusivamente de 
permisos para la ejecución de las copias, sin capacidad para su borrado o modificación. 
• 
Se evitará el uso de cuentas genéricas para el acceso a las copias de seguridad. En aquellos casos en los que 
su uso resulte imprescindible, deberá garantizarse la trazabilidad, dejando constancia de los usuarios que 
acceden mediante dichas cuentas. 
• 
Las credenciales de acceso deberán cumplir criterios de robustez adecuados, incluyendo contraseñas de al 
menos 16 caracteres, con combinación de mayúsculas, minúsculas, números y símbolos, o mecanismos de 
autenticación equivalentes. 
1

0. Monitorización de las copias de seguridad. 
La organización dispondrá de un sistema centralizado de supervisión que permita controlar el estado de todas las 
copias de seguridad y revisar los registros asociados a su ejecución. 
Este sistema deberá garantizar, al menos, lo siguiente: 

Política de copias de seguridad 
 
Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 7 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
• 
Registro y revisión del estado de las copias, incluyendo fechas de ejecución, sistemas respaldados y posibles 
errores, eventos o alertas generadas. 
• 
Generación de informes automáticos sobre el estado y resultado de las copias de seguridad. 
• 
Registro de accesos a las copias de seguridad, conservando como mínimo la identificación del usuario, la 
fecha y hora, el recurso accedido, el tipo de acceso y si este ha sido autorizado o denegado. 
• 
Conservación de los registros durante un período mínimo de dos años, salvo que la normativa aplicable 
exija un plazo superior. 
Estas medidas permiten asegurar la trazabilidad, el control y la detección temprana de incidencias relacionadas con 
las copias de seguridad de la Autoritat Portuària de Barcelona. 
1

1. Pruebas de recuperación. 
La organización dispondrá de un Plan de Recuperación que defina de forma clara y documentada los pasos 
necesarios para restaurar la información y los servicios a partir de las copias de seguridad. 
Dicho plan deberá contemplar los siguientes aspectos: 
• 
Plazos de recuperación previamente definidos en función de la criticidad de los servicios y de los datos a 
recuperar. 
• 
Nivel mínimo de operación (ROL) requerido para cada servicio, que permita considerarlo operativo tras un 
incidente, aun cuando no se haya alcanzado su funcionamiento óptimo. 
• 
Procedimientos de restauración documentados para cada tipo de copia de seguridad, indicando las 
acciones a realizar y las personas responsables de su ejecución. 
• 
Realización periódica de pruebas de recuperación, con el fin de verificar la validez de las copias de seguridad 
y asegurar que los tiempos y niveles de recuperación definidos pueden cumplirse. 
1

2. Borrado y gestión de soportes 
La eliminación o reutilización de los soportes utilizados para las copias de seguridad se realizará de forma segura y 
controlada, garantizando la destrucción irreversible de la información contenida. 
En función del tipo de soporte, se aplicarán las siguientes medidas: 
• 
Soportes no electrónicos y soportes magnéticos: destrucción mediante triturado u otros métodos 
equivalentes que impidan la recuperación de la información. 
• 
Soportes electrónicos reutilizables: borrado mediante sobreescritura segura, asegurando la eliminación 
completa de los datos. 
• 
Soportes electrónicos no reutilizables: eliminación mediante desmagnetización o destrucción física, de 
forma que se imposibilite cualquier acceso posterior a la información. 
Estas acciones deberán realizarse conforme a los procedimientos internos establecidos y a la normativa de seguridad 
y protección de datos aplicable. 
ANEXO I: GLOSARIO 
• GDPR: El Reglamento General de Protección de Datos es el reglamento europeo relativo a la protección de las 
personas físicas en lo que respecta al tratamiento de sus datos personales y a la libre circulación de estos datos 
• RTO: Recovery Time Objective. Este parámetro mide el tiempo que una organización puede permitirse estar sin 
prestar un servicio determinado. 

Política de copias de seguridad 
 
Unitat Sistemes d’Informació 
Política Backups v.1.5 - ES.docx 
Pàgina 8 de 8 
Versión 1.5 
 
NOR – Normativa de Seguridad 01.00 
• RPO: Recovery Point Objective. Este parámetro mide el volumen de datos en riesgo de pérdida que la 
organización considera aceptable. 
• ROL: Revised Operating Level. Nivel mínimo de servicio que debe alcanzarse tras un incidente para considerar 
que un servicio ha sido recuperado de forma aceptable.

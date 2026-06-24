# Política de Bases de Datos Corporativas

## Alcance

Esta política establece las normas, responsabilidades y procedimientos para el diseño, administración, mantenimiento, seguridad y operación de las Bases de Datos utilizadas por la organización. Esta política busca reforzar la seguridad, garantizar el cumplimiento normativo y reducir riesgos operativos en el acceso a bases de datos en entornos Cloud.

Beneficios clave:

- Cumplimiento normativo (ENS, GDPR, ISO 27001).
- Menor riesgo de fuga de datos.
- Facilidad para auditorías externas.
- Mayor resiliencia ante incidentes.

Esta política aplica a todos los desarrolladores, administradores de bases de datos (DBA), personal de DevOps, proveedores y cualquier otra persona que interactúe con los sistemas de gestión de bases de datos en entornos de desarrollo, pruebas, preproducción, QA y producción.

En relación con el tipo de aplicaciones, se aplica solo desarrollos a medida; excluye SaaS y productos comerciales con bases de datos externas a APB. Esto significa que únicamente se consideran desarrollos a medida mantenidos por APB. Se excluyen todas aquellas aplicaciones del tipo Software as a Service (SaaS), así como productos comerciales que utilicen bases de datos que no estén dentro del entorno controlado por APB y que no se gestionen por el equipo de APB. 

Por otro lado, debido a la naturaleza específica de las tareas de BI y al uso intensivo de datos que suelen implicar, puede ser necesario desarrollar una política adicional que regule de forma más detallada los procedimientos, controles y requisitos de seguridad aplicables a los entornos de Business Intelligence. Esta política específica debería abordar aspectos como la gestión de grandes volúmenes de información, la integración con herramientas externas de análisis, el acceso seguro a datos sensibles y la protección frente a posibles riesgos derivados del tratamiento y explotación avanzada de los datos. Así, se garantizaría un marco normativo adaptado a las particularidades y necesidades de los proyectos de BI dentro de la organización.

Mientras no exista una política específica para Business Intelligence, la presente política se aplica también en dichas Bases de Datos.

## Motores soportados

La presente política establece los motores de bases de datos autorizados por la organización para los distintos entornos tecnológicos, incluyendo plataformas on-premise, entornos cloud, servicios gestionados e infraestructuras híbridas.

El objetivo de este apartado es definir las familias de motores corporativos que podrán utilizarse en nuevos desarrollos, evoluciones de sistemas existentes, migraciones tecnológicas o implantación de soluciones comerciales que requieran una base de datos propia o gestionada por APB.

A la hora de seleccionar el motor de base de datos más adecuado para cada caso, deberán tenerse en cuenta criterios técnicos, económicos, operativos, de seguridad, disponibilidad, mantenibilidad, integración con la arquitectura corporativa y capacidades internas de administración.

### Motores corporativos autorizados

Se establecen como motores de bases de datos autorizados los siguientes:

**Microsoft SQL Server / Azure SQL Database:** Incluye tanto despliegues on-premise o sobre infraestructura IaaS mediante Microsoft SQL Server, como despliegues cloud mediante Azure SQL Database o servicios equivalentes aprobados por la organización.

**PostgreSQL / Azure Database for PostgreSQL:** Incluye tanto despliegues PostgreSQL on-premise o sobre infraestructura IaaS, como despliegues cloud mediante Azure Database for PostgreSQL o servicios gestionados equivalentes aprobados por la organización.

**Bases de datos NoSQL documentales: Azure Cosmos DB / MongoDB:** Incluye el uso de Azure Cosmos DB en entornos cloud y MongoDB en aquellos casos en los que exista un requerimiento técnico específico, una necesidad derivada del modelo de datos o una dependencia de producto que justifique su uso.

**Oracle Database:** Oracle Database se considera un motor autorizado para los sistemas existentes que actualmente dependen de esta tecnología, especialmente en entornos on-premise o legacy de la organización. Su utilización se admite para garantizar la continuidad, evolución, mantenimiento y operación de sistemas ya implantados, así como para aquellos casos en los que existan dependencias técnicas, funcionales, operativas o económicas que hagan inviable su sustitución a corto o medio plazo.

Para nuevos desarrollos, Oracle Database no tendrá carácter preferente y su utilización deberá estar debidamente justificada y validada por el área de Sistemas de Información, atendiendo a criterios de necesidad técnica, compatibilidad con sistemas existentes, impacto de migración, coste, criticidad del servicio y disponibilidad de capacidades de administración

### Modalidades de despliegue

Los motores anteriores podrán desplegarse en distintas modalidades, siempre que se cumplan los requisitos de seguridad, operación, monitorización, backup, trazabilidad y continuidad definidos en esta política:

- **On-premise:** bases de datos desplegadas sobre infraestructura propia o gestionada por APB en sus centros de datos.
- **PaaS o servicio gestionado:** bases de datos proporcionadas como servicio gestionado por un proveedor cloud, donde determinadas responsabilidades de operación, disponibilidad, backup o actualización son asumidas por el proveedor.
- **Entornos híbridos:** arquitecturas que combinen bases de datos on-premise y cloud, o mecanismos de replicación, integración o sincronización entre ambos entornos.

La elección de la modalidad de despliegue deberá justificarse en función de los requisitos técnicos, la criticidad del servicio, la clasificación de los datos, los requisitos de rendimiento, la integración con otros sistemas, el modelo operativo, los costes y las capacidades de administración disponibles.

## Criterios para la selección del motor de base de datos

Para determinar el motor más adecuado en cada proyecto, se seguirá el siguiente orden de evaluación:

**Criterio técnico y funcional:** Se evaluará qué motor satisface mejor los requisitos funcionales, el modelo de datos, el volumen de información, concurrencia, criticidad, las necesidades de integración, los requisitos de rendimiento y las necesidades de disponibilidad del sistema.

**Alineación con la arquitectura corporativa:** Se priorizarán los motores que estén alineados con las plataformas tecnológicas corporativas, los estándares de seguridad, herramientas de monitorización y los procesos de despliegue, backup y mantenimiento de APB.

**Criterio operativo y de mantenibilidad:** Se valorará la capacidad real de administrar, monitorizar, parchear, securizar, respaldar y recuperar el motor seleccionado, tanto en modalidad on-premise como cloud. No deberá seleccionarse un motor si no existen capacidades suficientes para garantizar su operación segura y sostenible.

**Criterio económico:** En caso de que dos o más motores resulten técnicamente viables, se tendrá en cuenta el coste total de propiedad, incluyendo licenciamiento, infraestructura, almacenamiento, backup, alta disponibilidad, soporte, operación, mantenimiento, perfiles técnicos necesarios y posibles costes de migración.

**Uso de motores no preferentes o condicionados:** Cuando se proponga el uso de un motor no preferente para nuevos desarrollos, deberá existir una justificación técnica documentada y validación por parte del área de Sistemas de Información. Esta justificación deberá incluir, como mínimo, los motivos técnicos de la elección, alternativas evaluadas, impacto económico, riesgos operativos, modelo de soporte, estrategia de backup, alta disponibilidad y plan de ciclo de vida.

## Criterios de uso por motor

Microsoft SQL Server / Azure SQL Database

Ventajas técnicas:

Integración con el ecosistema Microsoft y con herramientas corporativas.

Adecuado para aplicaciones transaccionales corporativas, cargas OLTP y escenarios de integración con soluciones Microsoft.

Alineación natural con arquitecturas basadas en .NET y con aplicaciones corporativas existentes.

Cuando utilizarlo:

Aplicaciones corporativas basadas en tecnologías Microsoft o .NET.

Sistemas que requieran integración con herramientas corporativas Microsoft.

Si tu arquitectura es Docks.

Evolución de aplicaciones existentes que ya utilicen SQL Server.

PostgreSQL / Azure Database for PostgreSQL

Ventajas técnicas:

Motor relacional open source, robusto y ampliamente utilizado.

Open source, sin coste de licencia.

Adecuado para aplicaciones relacionales, datos mixtos y escenarios que requieran extensiones específicas.

Buen soporte para JSON, extensiones geoespaciales y determinados casos de analítica o tratamiento de datos semiestructurados.

Cuando utilizarlo:

Nuevos desarrollos que requieran un motor relacional robusto y flexible.

Aplicaciones con requisitos geoespaciales, datos semiestructurados o uso intensivo de JSON.

Proyectos en los que se busque optimizar costes sin renunciar a capacidades relacionales avanzadas.

Sistemas donde exista capacidad técnica suficiente para su administración y soporte.

Bases de datos NoSQL: Azure Cosmos DB / MongoDB

Ventajas técnicas:

Modelo documental flexible, adecuado para datos variables, semiestructurados o con esquemas cambiantes (documentos, clave-valor, grafos).

Alta escalabilidad, baja latencia, ingesta intensiva o arquitecturas distribuidas.

Adecuado para determinados casos de uso IoT, eventos, datos no estructurados o aplicaciones con patrones de acceso muy específicos.

Cuando utilizarlo:

Datos no estructurados o semiestructurados.

Necesidad de modelo documental flexible.

Aplicaciones con requisitos de escalabilidad horizontal o baja latencia.

Productos comerciales o soluciones específicas que requieran MongoDB como backend soportado.

Casos en los que el modelo relacional no resulte adecuado y exista justificación técnica documentada.

Motores adicionales (uso excepcional)

Oracle Database (uso estrictamente legacy)

Ventajas técnicas:

Motor maduro y robusto para cargas transaccionales y analíticas críticas.

Amplio uso en entornos corporativos y sistemas legacy.

Capacidades avanzadas de particionado, optimización, disponibilidad, recuperación y gestión de grandes volúmenes de datos.

Integración existente con determinados sistemas corporativos de APB.

Cuando utilizarlo:

Sistemas existentes profundamente integrados con Oracle.

Aplicaciones legacy cuya migración a otro motor no sea viable a corto o medio plazo por impacto técnico, operativo, económico o de riesgo.

Evoluciones funcionales o técnicas de sistemas que ya dependen de Oracle.

Aplicaciones que requieran funcionalidades específicas del motor no cubiertas adecuadamente por otros motores autorizados.

Escenarios en los que la continuidad operativa, la criticidad del servicio o las dependencias existentes justifiquen su mantenimiento.

## Recomendación resumida

## Roles y Responsabilidades

Este apartado define los principales roles y responsabilidades en la gestión y operación de bases de datos.

Administradores de Base de Datos (DBA) / DBA Lead o Ops

Gestionar usuarios, roles y permisos.

Supervisar el rendimiento y capacidad.

Realizar backups, restauraciones y pruebas de recuperación.

Asegurar la integridad y disponibilidad de los datos.

Aprobar cambios estructurales y de configuración.

configuración segura de motores y entornos Cloud, gestión de accesos y privilegios mínimos, aplicación de parches y actualizaciones.

Tech&Ops

Automatizar despliegues y provisión de BBDD.

Gestionar mecanismos de alta disponibilidad.

Integrar bases de datos en pipelines CI/CD.

Responsable de Seguridad de la Información con el rol de definir y supervisar las medidas de seguridad en BBDD.

TechLead equipo de desarrollo

Supervisa el diseño de los esquemas del proyecto siguiendo los estándares establecidos y dispone de una identidad dedicada con permisos de actualización del esquema de la aplicación, solo en el entorno de desarrollo. Solo se admite un techLead por equipo.

Desarrolladores

Diseñar esquemas siguiendo los estándares establecidos.

Desarrollar consultas optimizadas.

Garantizar que los datos sensibles no se utilicen en entornos no productivos.

Ejecutar migraciones de datos hasta un entorno determinado y con herramientas de ci/cd según procesos aprobados

## Seguridad y Control de Acceso

En este apartado se definen aspectos relacionados con el acceso a las BBDD, teniendo como objetivos:

Principio de mínimo privilegio

Limitar el acceso directo reduce la superficie de ataque.

Los desarrolladores deben interactuar con los datos mediante APIs o servicios intermedios, evitando credenciales directas que puedan ser comprometidas.

Reducción del riesgo de fuga de datos

Acceso directo implica exposición a datos sensibles (personales, financieros, etc.).

Centralizar el acceso permite aplicar controles como enmascaramiento, anonimización y auditoría antes de que los datos lleguen a entornos de desarrollo.

Cumplimiento normativo y auditoría

Normativas como GDPR, ISO 27001, SOC 2 y ENS exigen trazabilidad y control sobre quién accede a datos críticos.

Un único punto de acceso facilita la generación de logs completos, auditorías y correlación de eventos.

Prevención de configuraciones inseguras

Desarrolladores con acceso directo pueden crear conexiones inseguras, abrir puertos o usar credenciales en código.

Centralizar evita malas prácticas como credenciales hardcodeadas o cuentas con privilegios excesivos.

Control de credenciales y rotación

Arquitectura puede implementar gestión segura de secretos (Azure Key Vault, AWS Secrets Manager).

Esto asegura rotación periódica y evita exposición en repositorios.

Protección frente a ataques internos y externos

Acceso directo aumenta el riesgo de SQL Injection y explotación de errores humanos.

Centralización permite aplicar firewalls de base de datos, monitorización avanzada y alertas en tiempo real.

Separación de responsabilidades

Acceso a producción solo vía cuentas nominativas con MFA.

Arquitectura y operaciones garantizan la integridad y disponibilidad de los datos.

Desarrollo se centra en la lógica de negocio, reduciendo riesgos asociados a la gestión de datos.

Alineación con el ENS (Esquema Nacional de Seguridad)

La gestión segura de credenciales y el acceso a bases de datos es un pilar fundamental en la protección de los sistemas de información. Implementar buenas prácticas y herramientas especializadas permite garantizar la confidencialidad, integridad y disponibilidad de los datos, alineándose con los requisitos del Esquema Nacional de Seguridad.

Control de acceso: Aplicación del principio de mínimo privilegio y justificación de accesos.

Trazabilidad: Registro y auditoría completa de acciones sobre datos.

Protección de la información: Garantía de confidencialidad, integridad y disponibilidad.

Gestión de credenciales: Uso de gestores seguros y políticas de rotación.

Separación de entornos: Evita que desarrollo acceda a datos reales en producción.

Responsabilidad clara: Define un único responsable de la seguridad 

### Gestión de identidades y acceso

En los entornos Cloud, el acceso a las bases de datos deberá realizarse preferentemente mediante identidades de aplicación, identidades gestionadas o mecanismos equivalentes, evitando siempre que sea posible el uso de credenciales de usuario o contraseñas estáticas.

En los entornos on-premise, especialmente en aquellos sistemas ya existentes o legacy, se mantendrán los mecanismos de autenticación actualmente implantados, siempre que estén debidamente controlados, documentados y protegidos. No obstante, cuando sea técnicamente viable, estos entornos deberán alinearse progresivamente con los mismos principios de seguridad aplicados en cloud: mínimo privilegio, trazabilidad, separación de responsabilidades, gestión segura de credenciales y ausencia de contraseñas en código.

Además, centralizar y controlar el acceso a las bases de datos, tanto en cloud como en on-premise, contribuye directamente al cumplimiento del ENS y al refuerzo de la seguridad corporativa.

Beneficios del enfoque

Reducción del uso de credenciales estáticas.

Menor riesgo de fuga de credenciales, especialmente evitando contraseñas en código, scripts, repositorios o ficheros de configuración no protegidos.

Mayor trazabilidad sobre los accesos realizados por usuarios, aplicaciones y servicios.

Mejor control de permisos mediante roles, grupos o cuentas de servicio autorizadas.

Cumplimiento normativo y alineación con ENS, GDPR e ISO 

27001.

Identidades de aplicación, cuentas de servicio y credenciales de usuario

En entornos Cloud, las aplicaciones deberán autenticarse preferentemente usando identidades gestionadas, identidades de aplicación o credenciales almacenadas en un servicio seguro, como Azure Key Vault o solución equivalente aprobada.

En entornos on-premise, las aplicaciones podrán utilizar cuentas de servicio, autenticación integrada, usuarios técnicos o credenciales específicas del motor de base de datos, siempre que dichas credenciales estén controladas, documentadas y protegidas.

Las cuentas de servicio deberán estar asociadas a una aplicación, proceso o servicio concreto, evitando su uso manual por parte de usuarios.

Ningún miembro del equipo técnico deberá almacenar o compartir credenciales de bases de datos fuera de los mecanismos autorizados.

Siempre que sea posible, las credenciales deberán estar cifradas, protegidas y sujetas a rotación periódica o revisión de vigencia.

Cadenas de conexión y mecanismos de acceso

En entornos Cloud, se priorizará el uso de mecanismos basados en identidad, tokens temporales o servicios gestionados por el proveedor, evitando cadenas de conexión con usuario y contraseña.

En entornos on-premise, se permitirá el uso de cadenas de conexión cuando sea necesario por razones técnicas o por compatibilidad con sistemas existentes, siempre que no incluyan credenciales en claro ni se almacenen en ubicaciones no autorizadas.

Las cadenas de conexión, secretos, certificados o claves deberán almacenarse en repositorios seguros, herramientas corporativas de gestión de secretos, sistemas PAM, Key Vault o mecanismos equivalentes aprobados.

Queda prohibido almacenar credenciales de bases de datos en código fuente, repositorios Git, scripts no protegidos, documentación técnica, pipelines o ficheros accesibles sin control.

Gestión de usuarios y permisos

No se permiten cuentas compartidas para usuarios humanos.

Los accesos deberán concederse siguiendo el principio de mínimo privilegio.

Los DBA o equipos autorizados administrarán los permisos mediante roles, grupos o perfiles, evitando asignaciones directas siempre que sea posible.

Los desarrolladores no deberán disponer de permisos de escritura directa sobre bases de datos de producción, salvo autorización excepcional, justificada y temporal.

Integración con herramientas de gestión segura de credenciales

En entornos Cloud, Azure Key Vault o herramienta equivalente actuará como repositorio seguro para secretos, certificados y claves.

En entornos on-premise, se utilizarán las herramientas corporativas disponibles para la custodia segura de credenciales, tales como PAM, vault corporativo, repositorios cifrados o mecanismos equivalentes aprobados.

Las aplicaciones deberán consultar las credenciales mediante identidades o mecanismos autorizados, evitando el uso manual o la distribución directa de contraseñas.

Sistemas existentes y excepciones

Los sistemas on-premise existentes podrán mantener su modelo actual de autenticación siempre que se encuentre documentado, controlado y no suponga un riesgo no aceptable para la organización.

Cualquier nuevo desarrollo, evolución significativa o migración deberá valorar la adopción de mecanismos de autenticación más seguros y alineados con el modelo corporativo.

Cuando no sea posible aplicar el modelo objetivo por limitaciones técnicas, dependencia de producto o restricciones legacy, deberá quedar documentada la excepción y los controles compensatorios aplicados.

## Configuración

- Cifrado en tránsito obligatorio (TLS 1.2+).
- Cifrado en reposo obligatorio para todos los motores (algoritmos robustos AES-256).
- Auditoría habilitada en SQL Server, PostgreSQL y NoSQL.

### Seguridad

#### Cifrado

Cifrado en tránsito (TLS 1 3 o superior) obligatorio para todos los motores.

Cifrado en reposo mediante claves gestionadas por el proveedor Cloud o por APB (Azure Key Vault – Customer Managed Keys en casos críticos).

Prohibición de deshabilitar TLS, puertos heredados o mecanismos de cifrado obsoletos.

#### Acceso a red

Acceso únicamente desde redes privadas, VNets o endpoints seguros.

Prohibido exponer bases de datos a Internet y con el tráfico limitado por subredes privadas y security groups.

Entornos de dev, pre y pro separados en distintas VPCs.

Uso obligatorio de Private Endpoints para PaaS (Azure SQL, PostgreSQL, Cosmos DB).

Tráfico controlado por firewalls virtuales para permitir conexiones desde aplicaciones autorizadas, IP whitelisting.

#### Identidades y autenticación

Acceso exclusivo mediante Managed Identities o identidades de servicio validadas.

No se permiten usuarios SQL locales, salvo excepciones justificadas y aprobadas.

Integración obligatoria con Azure AD para autenticación y control de accesos.

### Parámetros de rendimiento y configuración

#### Parámetros de rendimiento

Definición de límites de conexiones, pool y timeouts según buenas prácticas del motor.

Monitorización de locking, deadlocks y planes de ejecución activada por defecto.

Planes de autoscaling definidos cuando aplique (Cosmos, PostgreSQL, SQL Server.).

#### Auditoría

Auditoría obligatoria de:

Autenticaciones y accesos.

Cambios de permisos.

Operaciones críticas (DROP, ALTER, TRUNCATE).

Ejecución de sentencias privilegiadas.

Retención mínima de 12 meses, integrada con Log Analytics y SIEM corporativo.

#### Automatización (IaC / CaC)

Toda instancia debe desplegarse mediante:

Terraform o Bicep (IaC) para infraestructura.

Ansible / scripts CI/CD para configuración extensible.

Prohibida la creación manual salvo emergencias documentadas.

Protección ante errores operativos

Point-in-time restore o snapshots activados en todos los motores que lo soporten.

#### Configuración para despliegues

Configuraciones versionadas en repositorios Git corporativos.

Revisión por pares obligatoria (DBA + arquitecto).

Validación automática mediante pipelines (linting, tests de seguridad).

Documentación mínima:

Motor utilizado.

Justificación técnica.

Parámetros configurados.

Políticas de backup y HA asociadas

## Estándares de Diseño y Desarrollo

### Buenas prácticas

Evitar SELECT *.

Aplicar normalización hasta 3FN, salvo casos justificados de desnormalización.

Definir claves primarias utilizando identificadores únicos.

Documentar cualquier cambio de esquema en el repositorio del proyecto.

### Convenciones de Nombres

Tablas: snake_case en PostgreSQL y NoSQL; PascalCase permitido en SQL Server.

Columnas: snake_case consistente con el estándar del motor.

Índices: prefijo idx_ + tabla + columna.

Restricciones: pk_, fk_, chk_, uq_.

### Especificaciones por Motor

#### SQL Server

TDE (Transparent Data Encryption) activado por def

Usar tipos nvarchar para textos con soporte Unicode.

Evitar TEXT/NTEXT (obsoletos).

Utilizar Stored Procedures para operaciones críticas.

Bloqueo de autenticación SQL, salvo justificación.

Database identifiers - SQL Server | Microsoft Learn

#### PostgreSQL

Forced SSL activado.

Usar jsonb para estructuras flexibles.

Aprovechar índices GIN/GIST cuando corresponda.

Evitar abuso de funciones en triggers que dificulten trazabilidad.

#### Oracle Database (solo uso excepcional)

Auditoría de SYS, SYSTEM y DBA habilitada.

Archivo de redo logs configurado para recuperación avanzada.

Esquemas protegidos mediante roles mínimos y tablespaces dedicados.

#### Bases NoSQL

Modelado basado en acceso, no en normalización.

Garantizar particionado adecuado.

Evitar documentos extremadamente grandes.

Definir TTL en colecciones que gestionen datos temporales.

### Protección de Datos Sensibles

Aplicar enmascaramiento, pseudonimización o tokenización según criticidad.

Clasificar datos por criticidad y según sensibilidad.

Proveer datasets anonimizados para QA.

Prohibido el uso de datos reales en entornos de desarrollo.

## Backups y Recuperación

La estrategia de backup y recuperación deberá garantizar la protección, disponibilidad y recuperabilidad de los datos en todos los entornos de bases de datos de la organización, tanto cloud como on-premise, IaaS, PaaS o servicios gestionados.

La estrategia deberá apoyarse, según corresponda, en las capacidades nativas del motor de base de datos, las capacidades del proveedor cloud, las herramientas corporativas de backup y la política de copias de seguridad corporativa vigente.

Para los datos críticos, deberá garantizarse la existencia de copias o mecanismos de recuperación en una ubicación separada del entorno principal. En entornos cloud, se priorizará la redundancia en regiones o zonas dentro de la Unión Europea cuando aplique. En entornos on-premise, deberá existir una protección equivalente mediante almacenamiento separado, CPD alternativo, repositorio corporativo de backup, copia externa o mecanismo equivalente aprobado por la organización.

### Frecuencia y tipos de Backup

Motores relacionales: SQL Server / Azure SQL Database y PostgreSQL / Azure Database for PostgreSQL

En entornos cloud PaaS, como Azure SQL Database o Azure Database for PostgreSQL, se utilizarán las capacidades nativas del proveedor para la generación, retención y recuperación de copias, incluyendo, cuando aplique:

Backups completos gestionados por el servicio.

Backups diferenciales o incrementales según las capacidades del motor.

Backups de logs o mecanismos equivalentes de recuperación punto en el tiempo, cuando estén disponibles.

Point-In-Time Restore cuando el servicio lo permita.

Retenciones extendidas cuando el servicio, la criticidad o la política corporativa lo requieran.

En entornos on-premise o IaaS, los backups deberán realizarse mediante las herramientas nativas del motor de base de datos, las herramientas corporativas de backup o una combinación de ambas, garantizando en todo caso la consistencia de las copias y la posibilidad de recuperación.

Como criterio general, y siempre que sea técnicamente posible, se aplicará la siguiente retención mínima, alineada con la política corporativa:

Retención diaria mínima: 30 días.

Retención semanal mínima: 8 semanas.

Retención mensual: 24 meses.

Retenciones extendidas o de larga duración cuando lo requiera la criticidad del sistema, la normativa aplicable o las necesidades de auditoría.

Motores NoSQL: Azure Cosmos DB / Mongo DB

En entornos cloud, como Azure Cosmos DB, se utilizarán las capacidades nativas del servicio para backup, retención y recuperación, incluyendo snapshots automáticos, Point-In-Time Restore o mecanismos equivalentes cuando estén disponibles.

En entornos on-premise, IaaS o servicios gestionados basados en MongoDB u otros motores NoSQL autorizados, deberán definirse mecanismos de copia adecuados al motor, tales como snapshots consistentes, backups lógicos, backups físicos, réplicas controladas o herramientas específicas del producto.

Como criterio general:

Se activará Point-In-Time Restore cuando esté disponible y sea necesario por criticidad.

Se mantendrá una retención mínima de 30 días para copias operativas.

Se conservarán copias mensuales durante 24 meses cuando aplique por criticidad, auditoría o política corporativa.

El diseño de backup deberá tener en cuenta el modelo de particionado, replicación, consistencia y volumen de datos del motor NoSQL.

Oracle Database

Oracle en Cloud (uso excepcional)

Oacle Database podrá estar desplegado en entornos on-premise, IaaS o, excepcionalmente, en modalidad de servicio gestionado. En todos los casos, la estrategia de backup deberá garantizar la recuperación de la base de datos conforme a los requisitos de RTO/RPO definidos para cada sistema.

Como criterio general, se utilizarán las capacidades nativas de Oracle y las herramientas corporativas de backup, incluyendo cuando aplique:

Backups RMAN programados.

Copias completas, incrementales o diferenciales según la política definida.

Gestión y retención de archivelogs acorde al RPO del servicio.

Copias adicionales sobre almacenamiento corporativo o repositorio de backup.

Snapshots de almacenamiento cuando estén disponibles y sean compatibles con la consistencia de la base de datos.

Copias mensuales con retención mínima de 24 meses cuando aplique por criticidad, auditoría o política corporativa.

Los snapshots de infraestructura o almacenamiento podrán utilizarse como mecanismo complementario, pero no deberán sustituir a la estrategia de backup del motor salvo que exista validación técnica expresa que garantice la consistencia y recuperabilidad de la base de datos.

Almacenamiento

Todas las copias deben almacenarse en almacenamiento aislado del entorno de producción.

Se mantiene la regla de tres ubicaciones lógicas:

Backup primario en el servicio PaaS.

Copia secundaria en almacenamiento geo-replicado (GRS/ZRS).

Copia mensual exportada a un repositorio de almacenamiento separado (otra región o suscripción), cumpliendo lo equivalente a la “ubicación diferente” del on-premise.

Acceso a las copias de seguridad

Acceso restringido exclusivamente a Tech&Ops y DBA.

No se permiten usuarios genéricos salvo registro completo.

Acceso siempre vía identidades gestionadas y redes privadas.

Pruebas de restauración

Prueba de restauración trimestral en cada tecnología (SQL, PostgreSQL, NoSQL, Oracle, MongoDB).

Restauraciones de validación a entornos PRE o entornos temporales.

Validación del RTO/RPO definidos para cada servicio crítico:

RTO y RPO deben estar definidos por cada aplicación que utilice la base de datos.

Los tiempos deben revisarse anualmente.

Borrado y rentención

indicado en el apartado 

13. Ciclo de vida de los datos. El fin del ciclo es siempre mediante borrado seguro y/o destrucción segura certificada de los soportes de información, manteniendo el registro de los procesos de eliminación.

La eliminación debe seguir los criterios de ciclo de vida de almacenamiento definidos por la política corporativa de la gestión de soporte de información

Monitoreo, Rendimiento y Mantenimiento

Monitoreo continuo de: consultas lentas, uso de CPU, IOPS, locking, deadlocks.

Reindexación semanal en PostgreSQL y SQL Server.

Mantenimiento de colecciones y TTL en bases NoSQL.

Alertas automatizadas.

Observabilidad 

Monitorizacion continua y observabilidad

Monitorización continua del estado de todas las bases de datos utilizando herramientas nativas del cloud y la plataforma corporativa de observabilidad (APM).

Seguimiento en tiempo real de:

Consultas lentas (slow queries) y planes de ejecución ineficientes.

Métricas de rendimiento: CPU, memoria, IOPS, latencia de disco, cache hit ratio.

Contención de recursos: locking, blocking, deadlocks, saturación de conexiones.

Métricas específicas según el motor (buffer pool en SQL Server, autovacuum en PostgreSQL, shards en NoSQL, etc.).

Integración con la plataforma de observabilidad para disponer de:

Dashboards de rendimiento unificados.

Seguimiento transaccional end-to-end (tracing distribuido).

Logs estructurados centralizados.

Correlación automática entre incidencias, logs y métricas.

Mantenimiento preventivo, optimización

PostgreSQL:

Reindexación semanal o programada según crecimiento de tablas.

Análisis periódico de estadísticas (ANALYZE).

SQL Server:

Reindexación y reorganización de índices semanal.

Actualización de estadísticas programada.

Limpieza de logs y optimización del transaction log.

Bases NoSQL (MongoDB, CosmosDB, etc.):

Mantenimiento periódico de colecciones.

Revisión de particiones, shards 

Revisión de tamaño de documentos y hot partitions.

Mantenimiento de índices.

Oracle

Reorganización de índices y tablas afectadas.

Limpieza de archivelogs.

Análisis de AWR/ASH para dimensionamiento.

Mantenimiento correctivo

Cuando la monitorización detecte degradación del sistema o alertas, se aplicarán medidas correctivas como:

Rediseño de índices.

Optimización de consultas.

Ajuste de parámetros del motor. 

Ajustes en el pool de conexiones.

Redistribución de particiones en NoSQL.Gestión de Cambios

Toda peticion del cambio debe ser auditable y registrable desde la herramienta ITSM de la compañía y tener su flujo de aprobación.

Despliegues automatizados. Todo cambio debe realizarse mediante scripts a través de pipelines CICD.

Uso obligatorio de herramientas de migración establecidas:  

Microsoft SQL Server Migration Assistant (SSMA)  de Oracle a SQL y Azure

Azure Data Factory: Ideal para cargas de trabajo programadas o flujos de datos complejos de extracción, transformación y carga (ETL).

SQL Data Sync: Excelente para mantener sincronizaciones bidireccionales o unidireccionales entre múltiples bases de datos en la nube o locales.

Elastic Queries: Permite realizar consultas Transact-SQL de una base de datos a otra o copiar datos entre ellas mediante tablas externas utilizando el motor de Azure SQL Azure SQL Database Elastic Query. 

Azure Database Migration Service: La herramienta nativa administrada para migraciones completas a gran escala con un tiempo de inactividad casi nulo.

Copia directa: Si necesitas clonar una base de datos entera en el mismo servidor o a otro, puedes usar la función nativa de copia a través de Transact-SQL, PowerShell o Azure Portal, descrita en Copiar una base de datos - Azure SQL Database.

Cambios en producción deben incluir plan de rollback.

Revisión de impacto en queries críticas mediante EXPLAIN/Execution Plan.

Validaciones de rendimiento antes de liberar a producción.

Procedimiento para acciones en entornos por parte de equipos de aplicación

Modificación de la estructura (tablas, campos): 

Se debe realizar una petición de despliegue mediante el formulario actual, usando migrations de code first.

El script debería estar libre de fallos y debería contener un apartado, indicando cual es el resultado esperado de su ejecución.

Se debe incluir un script de rollback en caso de que falle la ejecución.

Acceso/modificación de datos: 

A través de pantallas de mantenimiento de la aplicación.

Si no existen, usar las APIs proporcionadas por la aplicación.

Si no es posible, enviar petición CST a Tsystem con script y resultado esperado 

Se debe incluir un script de rollback en caso de que falle la ejecución.

(SLA urgente: 24h).

Volcado de datos entre entornos (PRO → PRE): 

Petición CST a Tsystem (SLA urgente: 24h).  Revisar: (GUI - Ofuscación de Datos en Entornos no Productivos v1.0 - ES_firmado)

Otras operaciones sobre BBDD (indexación, historificación, rendimiento, conexiones): 

Definir el objetivo, que problema se busca corregir o que mejora se espera.

Petición CST a Tsystem (SLA urgente: 24h).

Incidencias en producción con impacto en operativa: 

Abrir Jira a Ops y coordinar acción urgente inmediata con equipo BBDD y equipo de aplicación.

En resumen, 

Para los cambios de datos en entornos productivos, se deberá indicar si se requiere backup o establecer un punto de restauración, dependiendo de la tecnología de base de datos.

En entornos Cloud, el acceso a las bases de datos no se realiza mediante credenciales de usuario, sino mediante identidades de aplicación, lo que aporta ventajas en seguridad y control.

Se establece que el acceso directo a la base de datos (BBDD) en entornos Cloud será exclusivo del equipo de Arquitectura y Operaciones, no autorizando que otros perfiles dispongan de credenciales directas.

Los equipos de desarrollo y otros perfiles deberán interactuar con los datos únicamente mediante APIs, servicios intermedios o pantallas de mantenimiento. 

Para acciones más compleja, se solicitará vía ticket la ejecución de dicha tarea a los equipos autorizados.

Auditoría y Trazabilidad

Registrar accesos, cambios de permisos y operaciones críticas.

Toda acción relevante sobre las bases de datos debe quedar registrada: accesos, modificaciones, cambios de configuración, operaciones críticas.

Accesos: identificación única de cada usuario o servicio, registro de intentos fallidos y accesos exitosos. 

Trazabilidad de operaciones críticas: Alta/baja de usuarios, cambios de permisos, modificaciones de configuración, consultas masivas de datos sensibles.

Logs cifrados y almacenados de manera segura.

Auditoría periódica para verificar cumplimiento de controles.

Mantener logs por un mínimo de 12 meses.

Estos logs deben estar sí o sí:

• Accesos a la base de datos (exitosos y fallidos).

• Acciones de administradores y usuarios con privilegios elevados.

• Cambios en la configuración del motor o del servicio.

• Eventos de seguridad (intentos de acceso indebido, anomalías, errores críticos).

• Consultas o acciones realizadas fuera del canal habitual del aplicativo.

El objetivo que busca la politica es detectar accesos o acciones que no provienen de los canales habituales para garantizar la trazabilidad para detectar anomalías y responsabilidad, no auditar cada acción de los aplicativos. Esto es necesario únicamente en casos de datos de categoría muy sensible si el análisis de riesgos así lo exigiera y no es el caso.

Alta Disponibilidad

Réplicas automáticas según proveedor para los 3 motores.

Nivel 1 → Multi-site activo-activo + RPO≈0 (no hay)

Nivel 2 → DR warm + replicación asíncrona 

Nivel 3 → Backup + recuperación planificada 

Nivel 4 → Archivado + recuperación diferida

 

Herramientas Aprobadas

Microsoft SQL Server / Azure SQL: SQL Server Management Studio (SSMS), Azure Data Studio, o DBeaver 

Oracle: SQL*Plus, Oracle SQL Developer, TOAD  (o equivalente corporativo), o DBeaver (si credenciales en PAM y existe una auditoria de su uso)

PostgreSQL: psql (CLI), PgAdmin (si se autoriza), o DBeaver (si credenciales en PAM y existe una auditoria de su uso).

Acceso por drivers (ODBC/JDBC) solo desde aplicaciones o herramientas corporativas autorizadas y registradas (no desde equipos personales).

Acceso por drivers (ODBC/JDBC) solo desde aplicaciones o herramientas corporativas autorizadas y registradas (no desde equipos personales).

Consolas de administración registradas.

Herramientas de automatización y CI/CD corporativas, , con trazabilidad de cambios (Azure DevOps/Github/Jenkins corporativo).

Credenciales en PAM y auditoria de uso aplica a todas las acciones administrativas a no ser que haya incompatibilidad que no debería ser la norma/habitual. Debe quedar bien definido el listado para poder incluirlo en los requerimientos del pliego del PAM.

Para los requisitos de seguridad del puesto de trabajo, tenemos que usar politicas en el puesto de trabajo para acceso al PAM (algunas soluciones de PAM incorporan el ZTNA y/o los agentes de ZTNA de Fortinet EMS que debería implantar Comunicaciones.

Ciclo de Vida de los Datos

Retención definida por departamento jurídico y de auditoría.

Eliminación segura certificada.

Registro de operaciones de archivado y eliminación: qué se elimina, cuándo, quién autoriza, quién ejecuta, desde qué sistema.

Archivado en almacenamiento frío cuando corresponda.

Documentación de procesos de destrucción: procedimientos aprobados, responsables, herramientas, evidencias.

Compartición de datos entre aplicaciones

Cada aplicación mantiene su propio esquema/bbdd y es responsable de sus datos.

Mecanismos permitidos:

APIs corporativas, acceso a datos de otra aplicación solo via API

Eventos/Mensajería: Publicación de eventos (bus/cola)

CDC Replicación controlada

Mecanismos NO permitidos:

DBLinks

Vistas o tablas compartidas entre esquemas

Acceso cruzado/directo entre aplicaciones y esquemas de otras aplicaciones

Acceso a BBDD mediante credenciales compartidas Inteligencia artificial

La inteligencia artificial desempeña un papel cada vez más relevante en la gestión y administración de sistemas, permitiendo automatizar tareas complejas y optimizar procesos. A continuación, se detallan algunos de los principales casos de uso permitidos en este ámbito.

Casos de Uso Permitidos en administración y gestión

Optimización y Mantenimiento mediante IA

Recomendaciones automáticas de índices.

Análisis de patrones de carga y ajuste de configuraciones.

Detección de consultas lentas mediante algoritmos.

Predicciones de capacidad y consumo.

Seguridad Basada en IA

Detección de comportamientos anómalos.

Alertas de accesos sospechosos.

Clasificación automatizada de datos sensibles.

Operaciones y Automatización

Asistentes de IA para generación de consultas SQL.

Análisis semántico para mapear datos en migraciones.

Limpieza, enriquecimiento o validación de datos con IA.

Casos de Uso Restringidos o Prohibidos en administración y gestión

Prohibido enviar datos personales o confidenciales a IA generativas sin anonimización.

Prohibido ejecutar cambios automáticos sugeridos por IA sin revisión humana.

Restringido el uso de IA de terceros no aprobados por seguridad.

Prohibido almacenar salidas de IA que incluyan datos sensibles en ubicaciones no seguras.

Datos Permitidos y No Permitidos en Sistemas de IA

Permitidos

Metadatos de rendimiento.

Esquemas de bases de datos.

Consultas anonimizadas.

Logs sin información personal.

No Permitidos

Datos personales identificables (PII).

Datos financieros, clínicos o sujetos a regulación.

Contenido confidencial empresarial no anonimizado.

Requisitos de Seguridad para IA

Cifrado en tránsito obligatorio.

Cifrado en reposo para datos usados por modelos.

Tokenización o anonimización previa a cualquier envío a IA generativa.

Restricción de endpoints permitidos.

Controles IAM para limitar acceso.

Auditoría habilitada para todas las operaciones relacionadas con IA.

Evaluación y Validación de Resultados

Los DBA deben revisar toda recomendación automatizada antes de aplicarla.

La IA no puede ejecutar operaciones destructivas ni DROP/ALTER críticos.

Deben existir mecanismos de rollback para cambios aplicados tras recomendaciones.

Análisis de impacto solicitado antes de aplicar ajustes sugeridos.

Integración con Herramientas del Proveedor Cloud

Azure

Uso de Azure SQL Intelligent Performance.

Azure AI para detección de anomalías.

Azure Data Studio con copilotos aprobados.

AWS

Amazon DevOps Guru for RDS.

Amazon Macie para clasificación de datos.

Amazon SageMaker para modelos propios.

GCP

Cloud SQL Insights.

Vertex AI para auditorías y modelos.

BigQuery ML para optimización avanzada.

Gestión de Modelos y Trazabilidad

Documentar modelos usados, versiones, parámetros y datasets.

Mantener control de versiones.

Monitoreo de sesgos y drifts.

Registros obligatorios de decisiones automatizadas.

Riesgos Asociados y Controles

Riesgo de fuga de datos: mitigar mediante anonimización.

Riesgo de recomendaciones incorrectas: mitigación con doble validación.

Riesgo de dependencia tecnológica: asegurar alternativas no basadas en IA.

Monitoreo y Métricas de Cumplimiento

Alertas por accesos indebidos a servicios de IA.

Registro de modelos en uso y usuarios que los ejecutan.

Auditoría trimestral de casos de uso.

Capacitación Obligatoria

Formación anual en ética de IA.

Capacitación en protección de datos.

Buenas prácticas de IA aplicada a BBDD.

Conexión con Servicios de IA Externos (Generativos)

La conexión con servicios de IA externos representa una oportunidad para potenciar las capacidades tecnológicas, pero también implica una serie de riesgos y responsabilidades. Por ello, es fundamental establecer directrices claras que garanticen la seguridad y el cumplimiento normativo en su utilización.

Reglas Generales

El uso de modelos de IA generativa externos (OpenAI, Anthropic, LLMs SaaS, etc.) solo está permitido si se realiza a través de proveedores aprobados por Seguridad.

Queda estrictamente prohibido enviar datos sensibles, confidenciales o no anonimizados a plataformas externas.

Toda integración debe pasar por evaluación de riesgo y análisis de impacto en protección de datos.

Tipos de Datos Permitidos

Esquemas de bases de datos sin valores reales.

Consultas SQL anonimizadas.

Metadatos técnicos (latencias, planes de ejecución simplificados).

Estructuras lógicas o documentación no sensible.

Datos Prohibidos para IA Externa

Información personal identificable (PII).

Datos financieros o clínicos.

Logs con identificadores reales.

Contenido propietario crítico sin autorización.

Cualquier dato no aprobado por seguridad.

Requisitos Técnicos para Conectar IA Externa

Uso obligatorio de un middleware corporativo que provea:

Anonimización automática.

Filtrado de datos sensibles.

Auditoría de llamadas.

Control de tokens y credenciales.

Los endpoints de IA externa deben estar permitidos en listas blancas controladas.

Queda prohibida la conexión directa desde BBDD a modelos de IA externos.

Limitaciones Operativas

Las IA externas no podrán ejecutar consultas ni acciones contra bases de datos.

Solo podrán sugerir o generar código, nunca aplicarlo.

Las recomendaciones deben revisarse por DBA o arquitecto antes de implementarse.

Evaluación y Riesgos

Evaluación de proveedores según nivel de madurez en IA, seguridad, cumplimiento y residencia de datos.

Revisión anual del uso de IA generativa externa.

Mitigación de riesgos de fuga mediante herramientas de DLP.

Cumplimiento y consecuencias técnicas

Cualquier modificación o excepción relativa a las políticas aquí descritas deberá ser solicitada formalmente al departamento de Tech&Ops mediante los canales establecidos. Estas solicitudes serán evaluadas caso por caso, teniendo en cuenta los riesgos, el impacto en la seguridad, la normativa vigente y la alineación con los objetivos corporativos. Solo se autorizarán excepciones debidamente justificadas y documentadas, y siempre con la aprobación explícita de Tech&Ops y, en su caso, del CISO y/o de los departamentos jurídico y de auditoría.

El cumplimiento de estas políticas se garantiza a través de la implementación de Infraestructura como Código (IaC), Configuración como Código (CaC) y el despliegue de políticas automatizadas que aseguran la trazabilidad, el control, la auditoría continua y la corrección automática de desviaciones. Además, se realizan revisiones periódicas para verificar la eficacia de las medidas y detectar posibles incumplimientos, promoviendo así una cultura de seguridad y responsabilidad en el manejo de los datos.

El incumplimiento de esta política podrá resultar en revocación de accesos, bloqueo de despliegues entre entornos y acciones adicionales según la normativa interna

Practicas no autorizadas

Acoplamiento fuerte  de apps a BBDD

Accesos no autorizados

Dblinks

Vistas o consultas de otros esquemas

Cadenas de conexión personales en lugar de por aplicación

Uso de credenciales diectas por parte de equipos no Tech&Ops

Uso de cuentas compartidas (genéricas) o “admin” sin trazabilidad

Uso de credenciales en código, scripts, repositorios (Git), pipelines o documentación para acceso a las bases de datos.

Acceso a BBDD desde equipos no gestionados

Uso de sinónimos, grants globales, o permisos amplios para facilitar integraciones

Ejecución de cambios (DDL/DML) en producción sin previa petición, sin aprobación, sin ventana o sin plan de rollback.

Conexiones desde el cliente con permisos excesivos (SYS/SYSTEM)

 Aplicar en produccion recomendaciones de IA sin revisión y sin pruebas

# Protección de los Servicios en la Nube

| Versión | Descripción | Autor | Acción | Fecha |
|---------|-------------|-------|--------|-------|
| v1.0 | Elaboración de la Guía | Oficina Técnica de Seguridad (Sothis) | Creación | 12/02/2026 |
| v1.0 | Revisión de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Revisión | 02/05/2026 |
| v1.0 | Aprobación de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Aprobación | 02/05/2026 |

## 1. Introducción

La presente guía establece las medidas de seguridad aplicables al uso, contratación, configuración, operación y supervisión de servicios en la nube utilizados por la Autoritat Portuària de Barcelona.

Su finalidad es garantizar la protección de la información y de los servicios soportados en entornos cloud, asegurar un uso controlado y acorde con los requisitos del Esquema Nacional de Seguridad (ENS) y del resto del marco normativo aplicable, y reducir los riesgos derivados de la externalización de infraestructuras, plataformas o aplicaciones suministradas por terceros.

## 2. Alcance

La presente guía aplica a todos los servicios en la nube utilizados por la Autoritat Portuària de Barcelona, con independencia de su modelo de servicio, ya sea software como servicio (SaaS), plataforma como servicio (PaaS) o infraestructura como servicio (IaaS), así como de su modalidad de implantación.

También aplica a los sistemas que soportan dichos servicios, a la información tratada, a los usuarios que acceden a ellos, a los proveedores responsables de su prestación y a las áreas encargadas de su contratación, administración, supervisión y seguridad.

Su contenido comprende las actividades de evaluación, contratación, configuración, integración, operación, monitorización, revisión y finalización de los servicios en la nube.

## 3. Roles y responsabilidades

La gestión segura de los servicios en la nube requiere la participación coordinada de distintos roles de la Autoritat Portuària de Barcelona y de los proveedores implicados, cada uno con responsabilidades específicas.

- Responsable de Seguridad de la Información: supervisa el cumplimiento de los requisitos de seguridad aplicables a los servicios cloud, valida los controles definidos en esta guía, evalúa los riesgos asociados a su utilización y asegura su alineación con el ENS, con la normativa interna y con el resto del marco normativo aplicable.
- Responsable de Sistemas: gestiona la implantación, configuración, integración y operación de los servicios en la nube, asegurando que su uso se realiza conforme a los requisitos técnicos y de seguridad establecidos por la organización.
- Responsables de servicio o área: identifican la necesidad del servicio, validan su adecuación a los procesos de negocio y colaboran en la definición de los requisitos funcionales, operativos y de seguridad que deben cumplirse.
- Proveedor de servicios en la nube (CSP): presta el servicio conforme a las condiciones contractuales establecidas, aplica las medidas de seguridad exigibles y facilita la información, documentación y evidencias necesarias para su supervisión.
- Usuarios autorizados: utilizan los servicios en la nube de acuerdo con las políticas y normas corporativas, respetan las medidas de seguridad definidas y comunican cualquier incidencia, anomalía o sospecha de uso indebido que pueda afectar al servicio o a la información tratada.

## 4. Principios de seguridad en la nube

La Autoritat Portuària de Barcelona utiliza servicios en la nube conforme a principios de seguridad que permitan mantener el control sobre la información, reducir la exposición al riesgo y garantizar el cumplimiento de las obligaciones legales y organizativas.

La adopción de un servicio cloud debe responder a una necesidad justificada y apoyarse en un análisis previo de riesgos que tenga en cuenta la naturaleza de la información tratada, la dependencia del servicio, su criticidad y el impacto de una eventual indisponibilidad o incidente de seguridad.

La Autoritat Portuària de Barcelona aplica el modelo de responsabilidad compartida propio de los servicios en la nube, identificando con claridad qué obligaciones corresponden al proveedor y cuáles deben ser asumidas por la propia organización en materia de configuración, control de accesos, monitorización, protección de la información y cumplimiento.

La seguridad del servicio no se considera satisfecha únicamente por la certificación del proveedor. La Autoritat Portuària de Barcelona configura y utiliza los servicios cloud de forma segura, aplicando las guías CCN-STIC, las recomendaciones del fabricante y sus propias políticas de seguridad.

La información tratada en la nube se protege de acuerdo con su clasificación, nivel de sensibilidad y criticidad, aplicando medidas proporcionadas para garantizar su confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad.

El acceso a estos servicios se limita a los usuarios y sistemas autorizados, conforme al principio de mínimo privilegio, y se somete a mecanismos de control, registro y supervisión que permitan detectar anomalías, responder a incidentes y mantener evidencias suficientes sobre su uso.

### 4.1. Requisitos generales de seguridad en servicios cloud

Los servicios en la nube utilizados por la Autoritat Portuària de Barcelona deben cumplir las medidas de seguridad que correspondan en función del modelo de servicio prestado y de los riesgos asociados a su uso, conforme a las guías CCN-STIC y a los criterios internos de seguridad definidos por la organización.

Cuando los servicios sean prestados por terceros, la Autoritat Portuària de Barcelona verificará que los sistemas de información que los soportan son conformes con el Esquema Nacional de Seguridad o, en su defecto, que cumplen las medidas desarrolladas.

La evaluación de estos servicios tendrá en cuenta aspectos relacionados con la realización de auditorías técnicas o pruebas de penetración, el nivel de transparencia ofrecido por el proveedor, las medidas de cifrado y gestión de claves, y la ubicación o jurisdicción aplicable a los datos tratados.

La existencia de certificaciones o acreditaciones por parte del proveedor constituye un elemento favorable, pero no sustituye la obligación de la Autoritat Portuària de Barcelona de evaluar la adecuación del servicio, configurarlo de manera segura y controlar su uso efectivo.

### 4.2. Gestión de proveedores de servicios cloud

La Autoritat Portuària de Barcelona selecciona proveedores de servicios en la nube que ofrezcan garantías suficientes de seguridad, continuidad, cumplimiento normativo y capacidad operativa, en función del tipo de servicio contratado y de la criticidad de la información tratada.

En el proceso de selección y contratación se verifica que el proveedor dispone de controles de seguridad adecuados, certificaciones o evidencias equivalentes cuando resulten exigibles, y mecanismos que permitan demostrar el cumplimiento de los requisitos definidos por la organización.

Cuando el nivel de criticidad del servicio lo requiera, la Autoritat Portuària de Barcelona prioriza proveedores que dispongan de certificaciones reconocidas conforme al ENS o a metodologías de certificación aceptadas por los organismos competentes. Si el proveedor subcontrata parte del servicio, deberá exigir a sus subcontratistas condiciones de seguridad equivalentes a las que le han sido requeridas.

Los contratos formalizados con proveedores de servicios cloud deben incluir, como mínimo, los requisitos de seguridad aplicables, los acuerdos de nivel de servicio, las obligaciones de notificación y gestión de incidentes, las condiciones de continuidad y recuperación, el tratamiento de la información y las facultades de supervisión o auditoría por parte de la Autoritat Portuària de Barcelona.

### 4.3. Configuración segura de los servicios

La Autoritat Portuària de Barcelona configura los servicios en la nube de forma segura antes de su puesta en funcionamiento y mantiene dicha configuración revisada y actualizada durante todo el ciclo de vida del servicio.

La configuración se realiza conforme a las guías CCN-STIC que resulten de aplicación, a las recomendaciones del fabricante o proveedor y a las políticas internas de seguridad. Este criterio se aplica tanto a los servicios consumidos directamente como a los sistemas, máquinas virtuales, redes, repositorios, consolas de administración o componentes desplegados sobre plataformas cloud.

Se eliminan o modifican las configuraciones por defecto que puedan resultar inseguras y se habilitan únicamente los servicios, puertos, funciones y permisos estrictamente necesarios para la operación autorizada del servicio.

La configuración segura incluye, entre otros aspectos, la gestión adecuada de identidades y accesos, la protección de las interfaces de administración, la segregación de entornos, la restricción de servicios innecesarios y la protección de las comunicaciones y de la exposición a redes externas.

### 4.4. Protección de la información

La información tratada en servicios cloud se protege conforme a su nivel de sensibilidad, criticidad y requisitos normativos, aplicando medidas que permitan evitar accesos no autorizados, pérdidas, alteraciones o exposiciones indebidas.

La APB utiliza mecanismos de cifrado para proteger la información en tránsito y, cuando proceda, también en reposo. Estas medidas deben ser coherentes con la naturaleza del servicio, el tipo de información tratada y el riesgo asociado a su tratamiento en infraestructuras de terceros.

La gestión de claves criptográficas se realiza de forma segura, garantizando su protección, control de acceso y uso conforme a las políticas de la organización y a los requisitos técnicos del servicio.

La Autoritat Portuària de Barcelona evalúa y controla la ubicación de los datos y la jurisdicción aplicable al servicio, priorizando entornos que ofrezcan garantías adecuadas de protección jurídica y técnica, especialmente cuando la información esté sujeta a obligaciones regulatorias o contractuales específicas.

Cuando la naturaleza de la información lo requiera, se adoptan medidas adicionales para impedir el acceso del proveedor a los datos en claro o para limitar dicho acceso a supuestos expresamente autorizados y controlados.

### 4.5. Control de accesos y autenticación

El acceso a los servicios en la nube se gestiona de forma controlada, individualizada y trazable, de modo que cada usuario o sistema disponga únicamente de los permisos necesarios para el desempeño de sus funciones.

La Autoritat Portuària de Barcelona evita el uso de cuentas genéricas o compartidas y establece mecanismos que permitan identificar de forma unívoca a cada usuario que accede al servicio. Los permisos se asignan conforme al principio de mínimo privilegio y se revisan periódicamente para asegurar que siguen siendo necesarios y adecuados.

Los accesos con privilegios elevados o capacidad de administración se protegen mediante mecanismos de autenticación reforzada, incluyendo autenticación multifactor cuando resulte aplicable.

Siempre que sea posible, los servicios cloud se integran con los sistemas corporativos de gestión de identidades, autenticación y aprovisionamiento, con el fin de mantener una administración centralizada de accesos y reforzar el control sobre altas, modificaciones y bajas de usuarios.

### 4.6. Monitorización y registro

Los servicios en la nube deben proporcionar capacidades de registro y monitorización suficientes para permitir el seguimiento de la actividad, la detección de comportamientos anómalos y la investigación de incidentes.

La Autoritat Portuària de Barcelona mantiene trazabilidad sobre los accesos, cambios de configuración, acciones administrativas, eventos relevantes de seguridad y cualquier otra operación que resulte necesaria para controlar el uso del servicio.

Los registros deben protegerse frente a modificaciones no autorizadas, pérdidas o accesos indebidos, y conservarse durante el tiempo necesario conforme a los criterios establecidos por la organización y por la normativa aplicable.

La monitorización de estos eventos permite detectar usos anómalos, desviaciones de configuración, intentos de acceso indebido o incidentes que puedan comprometer la seguridad del servicio o de la información tratada.

### 4.7. Gestión de vulnerabilidades y actualizaciones

La Autoritat Portuària de Barcelona aplica medidas para identificar, evaluar y tratar las vulnerabilidades que puedan afectar a los servicios en la nube o a los componentes desplegados sobre ellos.

Estas medidas incluyen la revisión periódica de configuraciones, la aplicación de parches y actualizaciones de seguridad, el control de dependencias y componentes utilizados, y la verificación de que no se mantienen versiones obsoletas o configuraciones inseguras.

Cuando el nivel de criticidad del servicio o el análisis de riesgos lo requiera, se realizarán pruebas de seguridad adicionales, como análisis de vulnerabilidades, revisiones técnicas específicas o pruebas de penetración, directamente o a través del proveedor.

La gestión de vulnerabilidades debe orientarse a reducir el tiempo de exposición, priorizar las correcciones en función del riesgo y mantener el servicio en un estado de seguridad adecuado.

### 4.8. Gestión de incidentes

La Autoritat Portuària de Barcelona dispone de mecanismos para gestionar los incidentes de seguridad que puedan afectar a los servicios en la nube, con el fin de minimizar su impacto, restablecer el servicio y evitar su repetición.

Cualquier incidente relevante debe ser comunicado de forma inmediata a través de los canales establecidos por la organización. Una vez notificado, se analizará su naturaleza, su impacto potencial o real y las medidas de contención y corrección necesarias.

Cuando el incidente afecte a un servicio prestado por un tercero, el proveedor deberá colaborar activamente en su análisis, respuesta, resolución y seguimiento, conforme a las condiciones contractuales y a los tiempos de respuesta definidos.

La gestión de incidentes incluirá, cuando proceda, la investigación de causas, la recopilación de evidencias, la revisión de las medidas aplicadas y la definición de acciones correctoras o preventivas.

### 4.9. Continuidad del servicio

Los servicios en la nube utilizados por la Autoritat Portuària de Barcelona deben ofrecer un nivel de disponibilidad y resiliencia adecuado a las necesidades del servicio y al impacto que tendría su interrupción.

La Autoritat Portuària de Barcelona verifica que el proveedor dispone de medidas de respaldo, recuperación y continuidad, incluyendo copias de seguridad, procedimientos de recuperación ante desastres y compromisos de disponibilidad acordes con los niveles de servicio contratados.

Cuando el servicio lo requiera, se revisan los tiempos de recuperación, el alcance de los mecanismos de continuidad y la periodicidad con la que se prueban dichos planes, con el fin de asegurar que el servicio puede mantenerse o recuperarse en condiciones aceptables ante una incidencia grave.

Estas medidas contribuyen a reducir el riesgo de interrupción prolongada del servicio y a preservar la disponibilidad de la información y de los procesos soportados en la nube.

### 4.10. Borrado y finalización del servicio

Cuando un servicio cloud deja de utilizarse o cuando resulta necesario eliminar información tratada en él, la Autoritat Portuària de Barcelona garantiza que la baja del servicio y el borrado de datos se realizan de forma controlada y segura.

El proveedor debe ofrecer garantías suficientes de que la información eliminada no podrá recuperarse posteriormente y de que no permanecerán copias residuales no autorizadas en los sistemas o soportes que hayan intervenido en la prestación del servicio.

La finalización del servicio debe contemplar, además, la revocación de accesos, la recuperación o exportación de la información cuando proceda, la retirada de integraciones técnicas y la conservación de las evidencias necesarias para acreditar el cierre ordenado del servicio.

### 4.11. Cumplimiento y auditoría

La Autoritat Portuària de Barcelona supervisa el cumplimiento de esta guía y verifica que los servicios en la nube utilizados mantienen un nivel de seguridad adecuado a los requisitos definidos.

Para ello, podrá realizar revisiones técnicas y organizativas, solicitar evidencias al proveedor, analizar configuraciones, revisar registros y comprobar el grado de cumplimiento de los compromisos de seguridad y de los niveles de servicio establecidos.

Cuando resulte necesario, la Autoritat Portuària de Barcelona podrá ejercer las facultades de auditoría previstas contractualmente, directamente o a través de terceros autorizados, con el fin de comprobar la adecuación del servicio a las medidas de seguridad exigidas.

Los incumplimientos detectados darán lugar a la adopción de medidas correctoras, revisiones específicas o actuaciones adicionales, en función de su impacto y de la naturaleza del riesgo identificado.

## 5. Cumplimiento y revisión

La Autoritat Portuària de Barcelona revisa y actualiza periódicamente esta guía para mantenerla alineada con los servicios en la nube utilizados, los riesgos, la evolución tecnológica y la normativa aplicable.

- Supervisa su cumplimiento, adopta medidas correctoras ante desviaciones o incumplimientos y conserva evidencias sobre la implantación de los controles y las revisiones realizadas.
- La información relevante se registra en Jira ITSM o en los sistemas corporativos habilitados, garantizando su trazabilidad, integridad, disponibilidad y revisión posterior.

## 6. Registros

- Configuraciones de seguridad de los servicios cloud
- Registros de accesos y actividad
- Informes de auditoría, análisis de vulnerabilidades y pruebas de seguridad
- Registros de incidencias y actuaciones realizadas
- Evidencias de cumplimiento del ENS y de otros requisitos aplicables
- Documentación contractual del proveedor, incluidos acuerdos de nivel de servicio y compromisos de seguridad

## 7. Anexo. Glosario de Términos

- Cloud: modelo de prestación de servicios tecnológicos a través de infraestructuras accesibles por red, que permite el uso de recursos informáticos, almacenamiento, plataformas o aplicaciones sin necesidad de que estén alojados en sistemas propios.
- SaaS (Software as a Service): modalidad de servicio en la que el proveedor ofrece una aplicación completa accesible por red y gestionada íntegramente por él.
- PaaS (Platform as a Service): modalidad de servicio en la que el proveedor ofrece una plataforma sobre la que el cliente puede desplegar o ejecutar aplicaciones sin gestionar directamente la infraestructura subyacente.
- IaaS (Infrastructure as a Service): modalidad de servicio en la que el proveedor ofrece recursos de infraestructura, como proceso, almacenamiento o red, sobre los que el cliente despliega y administra sus propios sistemas.
- CSP (Cloud Service Provider): proveedor responsable de prestar el servicio en la nube.

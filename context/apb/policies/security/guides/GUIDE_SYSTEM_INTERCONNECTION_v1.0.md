# Interconexión de Sistemas

| Versión | Descripción | Autor | Acción | Fecha |
|---------|-------------|-------|--------|-------|
| v1.0 | Elaboración de la Guía | Oficina Técnica de Seguridad (Sothis) | Creación | 12/02/2026 |
| v1.0 | Revisión de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Revisión | 10/04/2026 |
| v1.0 | Aprobación de la Guía | Albert Prats - Responsable de Seguridad de la Información (CISO) | Aprobación | 02/05/2026 |

## 1. Introducción

La presente guía tiene por objeto regular las condiciones de seguridad aplicables a las interconexiones entre los sistemas de información de la Autoritat Portuària de Barcelona (APB) y los sistemas de terceros. Su finalidad es asegurar que cualquier intercambio de información o prestación de servicios con entidades externas se realice de forma autorizada, controlada y conforme a los requisitos de seguridad establecidos por la organización.

Este documento define las responsabilidades asociadas a la solicitud, aprobación, implantación, seguimiento, modificación y retirada de dichas interconexiones, con el fin de preservar la confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad de la información tratada.

## 2. Alcance

Esta guía se aplica a cualquier interconexión, ya sea lógica o física, que permita el intercambio de información o el acceso a servicios entre los sistemas de la Autoritat Portuària de Barcelona y sistemas pertenecientes a terceros.

Quedan comprendidas dentro de su alcance:

- Las conexiones permanentes o temporales;
- Los accesos remotos de terceros a recursos internos;
- Las integraciones mediante VPN, APIs, pasarelas, servicios publicados o enlaces dedicados;
- Las interconexiones establecidas con proveedores para fines de operación, soporte o mantenimiento.

Quedan excluidas del alcance las comunicaciones internas ordinarias entre sistemas y usuarios de la propia organización, salvo cuando estas impliquen relación o dependencia con dominios externos de seguridad.

## 3. Roles y responsabilidades

Los roles que intervienen en la gestión de la interconexión de sistemas y autorización de conexiones con terceros son los siguientes:

- Responsable del servicio: será quien justifique la necesidad de la interconexión, impulse su solicitud y confirme que su finalidad sigue siendo válida durante todo el tiempo que permanezca activa. También deberá verificar que el acceso solicitado se limita al ámbito estrictamente necesario.
- Responsable de Seguridad de la Información: será el encargado de validar las condiciones de seguridad, revisar la adecuación de los controles propuestos y autorizar la interconexión desde el punto de vista de seguridad. Supervisará que el procedimiento se aplique de forma coherente con las exigencias normativas y corporativas.
- Responsable de Sistemas: será responsable de la implantación técnica de la interconexión, de la aplicación de los controles perimetrales, de la segmentación, de la configuración de los mecanismos de monitorización y de la conservación de las evidencias técnicas asociadas.
- Entidad de terceros interconectados: deberá cumplir las condiciones de seguridad establecidas por la APB, mantener actualizados sus datos de contacto y comunicar sin demora cualquier incidente, cambio relevante o circunstancia que pueda afectar a la seguridad o continuidad de la interconexión.

## 4. Principios Generales

Toda interconexión con sistemas externos tendrá carácter excepcional y requerirá autorización previa expresa. No se permitirá ningún intercambio de información ni acceso entre sistemas si no existe una necesidad debidamente justificada y formalmente aprobada.

La Autoritat Portuària de Barcelona solo permitirá interconexiones cuando exista una necesidad operativa, técnica, legal o contractual acreditada, se hayan valorado previamente los riesgos y se hayan definido con claridad tanto los responsables internos como las medidas de seguridad aplicables.

Toda conexión deberá diseñarse con criterios de mínimo privilegio y mínima exposición. Esto implica que únicamente se autorizarán los accesos, servicios, protocolos y flujos estrictamente necesarios para la finalidad aprobada. Las interconexiones deberán mantenerse segregadas del resto de la red siempre que resulte necesario para reducir el riesgo y limitar el impacto de posibles incidentes.

## 5. Requisitos previos de autorización

Antes de autorizar una interconexión, deberá existir una solicitud formal a través de la plataforma Jira ITSM promovida por el responsable del Servicio de la Autoritat Portuària de Barcelona. Esta solicitud deberá identificar la finalidad de la conexión, la entidad tercera implicada, los sistemas o servicios afectados, la duración prevista y la justificación de la necesidad.

Junto con la solicitud, deberá realizarse un análisis de seguridad que permita valorar los riesgos asociados a la interconexión. Este análisis deberá considerar el posible impacto sobre la confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad de la información, así como la exposición derivada del uso de redes externas o de la dependencia de sistemas de terceros.

Cada interconexión deberá quedar formalmente documentada mediante una ficha o documento equivalente. En dicha documentación deberán recogerse de forma clara los sistemas origen y destino, las características de la interfaz, los protocolos y puertos autorizados, los mecanismos de autenticación, los requisitos de cifrado, la naturaleza de la información intercambiada, las obligaciones en materia de protección de datos, los responsables de operación y seguridad, y el proceso aplicable a su alta, modificación, suspensión y baja.

No podrá activarse ninguna interconexión si esta documentación no está completa, validada y aprobada por los responsables competentes.

## 6. Controles obligatorios de seguridad

### 6.1. Control perimetral

Toda comunicación con sistemas externos deberá realizarse a través de la infraestructura de seguridad perimetral autorizada por la Autoritat Portuària de Barcelona. No se permitirán conexiones directas que eludan los mecanismos corporativos de filtrado, inspección, registro y control.

Los flujos de entrada y salida deberán estar expresamente autorizados y limitados a los servicios, direcciones, puertos y protocolos previamente aprobados. Cualquier apertura adicional deberá tramitarse como una modificación de la interconexión existente.

### 6.2. Autenticación del extremo remoto

Antes de intercambiar información o prestar servicios a través de una interconexión, deberá garantizarse la autenticidad del sistema o entidad remota. Para ello se emplearán mecanismos robustos y aprobados por la organización, como certificados digitales, autenticación mutua, redes privadas virtuales autenticadas u otros mecanismos equivalentes.

La autenticación deberá ser coherente con la criticidad del servicio y con el nivel de exposición del canal. En ningún caso se admitirán mecanismos débiles o compartidos que impidan atribuir de forma fiable la identidad del tercero conectado.

### 6.3. Protección criptográfica

Cuando la comunicación discurra por redes externas al dominio de seguridad de la Autoritat Portuària de Barcelona, deberá protegerse mediante mecanismos de cifrado adecuados. La solución utilizada deberá garantizar la confidencialidad de la información en tránsito y reducir el riesgo de interceptación o acceso no autorizado.

La organización determinará los mecanismos criptográficos admisibles en función del contexto técnico y del nivel de protección requerido. En todo caso, no se autorizarán interconexiones que transmitan información sensible a través de canales no cifrados.

### 6.4. Segmentación

Las interconexiones con terceros deberán ubicarse en segmentos de red específicos o someterse a reglas de acceso diferenciadas que limiten su alcance. El acceso desde una interconexión externa se restringirá exclusivamente a los sistemas, servicios y recursos necesarios para la finalidad autorizada.

La segmentación deberá diseñarse de forma que una conexión externa no permita visibilidad ni acceso generalizado a otras partes de la red corporativa. Cuando resulte aplicable, se establecerán zonas separadas para usuarios, servicios y entornos de administración.

### 6.5. Registro y monitorización

Toda interconexión deberá disponer de mecanismos de registro suficientes para garantizar la trazabilidad de su uso. Como mínimo, deberán poder identificarse la entidad conectada, la fecha y hora de la conexión, los sistemas accedidos, las acciones relevantes ejecutadas y los eventos de seguridad asociados.

Estos registros deberán conservarse durante el tiempo definido por la organización y estar disponibles para su revisión en caso de incidente, auditoría o necesidad de investigación. Además, las interconexiones deberán someterse a monitorización periódica con el fin de detectar usos anómalos, intentos no autorizados o desviaciones respecto a las condiciones aprobadas.

## 7. Coordinación con terceros

Cuando una interconexión implique la participación de sistemas gestionados por distintas organizaciones, deberán establecerse mecanismos formales de coordinación entre las partes. Esta coordinación deberá definir con claridad las responsabilidades de operación, mantenimiento y seguridad, así como los canales de comunicación y escalado.

Asimismo, deberán acordarse las obligaciones relativas a la gestión de incidentes, la notificación de brechas o anomalías, la aplicación de cambios técnicos, la revocación de accesos y la aportación de evidencias cuando sea necesario analizar un evento de seguridad.

La coordinación con terceros será especialmente relevante cuando la autenticación, autorización o gestión de accesos se reparta entre distintos dominios de seguridad.

## 8. Gestión del ciclo de vida

Toda interconexión deberá gestionarse durante todo su ciclo de vida, desde su solicitud inicial hasta su retirada definitiva. En el momento de su aprobación deberá quedar registrada su fecha de alta, su periodo de vigencia y el criterio o fecha de revisión.

Las interconexiones vigentes deberán revisarse periódicamente para comprobar que siguen siendo necesarias, que mantienen las condiciones de seguridad aprobadas y que no han ampliado su alcance de forma no autorizada. Si una interconexión deja de ser necesaria, finaliza el contrato que la sustenta o cambia sustancialmente su finalidad, deberá tramitarse su modificación o baja formal.

Cualquier cambio que afecte al alcance, a los sistemas implicados, a los protocolos utilizados, a la información intercambiada o a los responsables designados requerirá una nueva validación de seguridad antes de su implantación.

## 9. Registros

- Herramienta Jira ITSM Corporación

## 10. Anexo. Glosario de Términos

- Interconexión de sistemas: Conexión entre sistemas de información de distintas entidades que permite el intercambio de información o la prestación de servicios.
- Sistema externo: Sistema de información que no pertenece al dominio de control de la APB.
- Tercero: Entidad externa (proveedor, organismo o colaborador) que requiere acceso o intercambio de información con la organización.
- Autorización de interconexión: Aprobación formal que permite establecer una conexión entre sistemas, tras validar su necesidad y condiciones de seguridad.
- Ficha de interconexión: Documento que recoge las características técnicas, requisitos de seguridad y condiciones de una interconexión concreta.
- Perímetro de seguridad: Conjunto de mecanismos que controlan y protegen el tráfico entre la red interna y redes externas.
- Segmentación de red: Separación lógica o física de la red para limitar el acceso a recursos y reducir el impacto de incidentes.
- VPN (Red Privada Virtual): Tecnología que permite establecer comunicaciones seguras y cifradas a través de redes no confiables.

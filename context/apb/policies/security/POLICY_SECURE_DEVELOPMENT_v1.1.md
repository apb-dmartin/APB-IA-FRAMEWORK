# Política de Desarrollo Seguro v1.1

| Versión | Descripción | Autor | Acción | Fecha |
|---------|-------------|-------|--------|-------|
| v1.0 | Versión inicial del documento | Oficina Técnica de Seguridad (Sothis) | Creación | 15/07/2025 |
| v1.1 | Actualización de la política | Oficina Técnica de Seguridad (Sothis) | Actualización | 15/04/2026 |
| v1.1 | Procedimiento de Comunicación APB | Oficina Técnica de Seguridad (Sothis) | Creación | 15/04/2026 |
| v1.1 | Revisión de Procedimiento | Responsable de Seguridad de la Información (CISO) | Revisión | 17/04/2026 |
| v1.1 | Aprobación de Procedimiento | Responsable de Seguridad de la Información (CISO) | Aprobación | 02/05/2026 |

**Tipo de documento:** Política  
**Nivel de seguridad:** Interno  
**Propietario:** Responsable de Seguridad de la Información  
**Área de difusión:** Ciberseguridad, Desarrollo, Sistemas de Información

## 1. Introducción

La Autoritat Portuària de Barcelona establece la presente política para definir los principios y requisitos generales de seguridad aplicables al desarrollo, adquisición, modificación, implantación, operación y mantenimiento de aplicaciones y componentes software.

Su finalidad es garantizar que las soluciones utilizadas por la organización se gestionan con un nivel de seguridad adecuado durante todo su ciclo de vida, protegiendo la confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad de la información tratada, y asegurando el cumplimiento del Esquema Nacional de Seguridad (ENS), de la normativa aplicable y del Sistema de Gestión de Seguridad de la Información (SGSI).

Esta política constituye el marco de referencia corporativo para integrar la seguridad en el ciclo de vida del software y resulta de aplicación tanto a desarrollos internos como a soluciones suministradas o mantenidas por terceros.

## 2. Alcance

Esta política aplica a todas las aplicaciones, componentes software, integraciones, desarrollos y evolutivos realizados para la Autoritat Portuària de Barcelona, tanto si son desarrollados internamente como si son suministrados, mantenidos o modificados por terceros.

Su cumplimiento es obligatorio para todo el personal interno y externo que participe en actividades de análisis, diseño, desarrollo, configuración, pruebas, despliegue, soporte, mantenimiento o administración de aplicaciones.

También aplica a los entornos, herramientas, repositorios, componentes de terceros y servicios tecnológicos utilizados durante el ciclo de vida del software, incluidos, cuando corresponda, servicios en la nube, APIs e infraestructuras contenerizadas.

## 3. Roles y responsabilidades

**Jefe de Proyecto:** Responsable de garantizar el cumplimiento de esta política durante la fase de desarrollo del proyecto, hasta la puesta en producción de la aplicación.

**Propietario de la Aplicación:** Asegura la aplicación continua de esta política durante la fase de operación, una vez que la aplicación está en producción.

**Responsable del Servicio:** Supervisa el cumplimiento global de esta política en todas las aplicaciones bajo su ámbito, asegurando la coordinación entre los distintos actores implicados.

**Responsable del Área de Desarrollo:** Garantiza que los desarrolladores aplican correctamente las prácticas de seguridad durante todo el ciclo de vida del desarrollo.

**Responsable de Seguridad de la Información:** Define, revisa y valida las directrices de seguridad que deben cumplirse en el desarrollo de software, asegurando la alineación con la normativa vigente (ENS, RGPD, ISO 27001, etc.).

**Responsable Funcional:** Supervisa el uso correcto de las aplicaciones desde el punto de vista del negocio, velando por que se cumplan los requisitos funcionales y de seguridad.

**Responsable Técnico:** Se encarga de la correcta administración técnica de la aplicación, incluyendo su configuración, despliegue y mantenimiento seguro.

## 4. Principios generales de desarrollo seguro

La Autoritat Portuària de Barcelona aplica un enfoque de desarrollo seguro en todo el ciclo de vida de las aplicaciones, integrando la seguridad desde las fases iniciales del proyecto hasta su retirada.

Todo desarrollo, modificación o adquisición debe partir de requisitos de seguridad definidos a partir del análisis de riesgos, la criticidad del sistema, la sensibilidad de la información tratada, las obligaciones legales y contractuales aplicables y, cuando resulte pertinente, las lecciones aprendidas de incidentes previos.

Las aplicaciones deben diseñarse, desarrollarse, probarse, desplegarse y mantenerse con criterios de seguridad proporcionales al riesgo, garantizando que las medidas implantadas responden a su nivel de exposición y al impacto que tendría un incidente.

Los entornos de desarrollo, pruebas y producción deben mantenerse diferenciados y controlados, evitando interferencias, accesos indebidos o exposiciones innecesarias de información. Esta separación se aplicará tanto a nivel técnico como de acceso.

Los desarrollos internos y los realizados por terceros deben cumplir los mismos principios y requisitos de seguridad, con independencia del origen del software o de la modalidad de prestación del servicio.

La configuración, operación y mantenimiento de las aplicaciones debe orientarse a reducir la exposición al riesgo, prevenir configuraciones inseguras y detectar de forma temprana vulnerabilidades, desviaciones o incidentes de seguridad.

La organización conservará evidencias suficientes que permitan demostrar el cumplimiento de esta política. El desarrollo operativo de estos principios se concreta en las guías específicas de seguridad aplicables.

## 5. Requisitos generales del ciclo de vida del software

Toda aplicación deberá gestionarse conforme a un ciclo de vida de desarrollo seguro que integre la seguridad de forma estructurada y trazable en cada una de sus fases.

Como mínimo, este ciclo de vida deberá contemplar la definición y documentación de requisitos de seguridad, el diseño seguro de la solución, el uso de entornos segregados, la aplicación de prácticas de desarrollo seguro, la validación funcional y de seguridad antes de la puesta en producción, el control de cambios y configuraciones, la gestión de vulnerabilidades durante la operación y la retirada o cierre seguro al final de su ciclo de vida.

La metodología de desarrollo adoptada por la organización o por sus proveedores deberá incorporar controles de seguridad, responsabilidades definidas y puntos de verificación adecuados a la criticidad del sistema.

La organización establecerá controles y puntos de verificación en estas fases para asegurar que la seguridad se integra de forma efectiva, coherente y trazable, y que su cumplimiento puede acreditarse mediante las evidencias correspondientes.

### 5.1. Autenticidad

La Autoritat Portuària de Barcelona garantizará que los usuarios, sistemas y componentes que interactúan con las aplicaciones sean identificados de forma fiable y solo puedan acceder a las funcionalidades para las que estén autorizados.

Para ello, las aplicaciones deberán incorporar mecanismos de autenticación robustos, medidas adecuadas de control de accesos y salvaguardas que eviten la suplantación de identidad, el uso indebido de credenciales y el acceso no autorizado.

Las medidas concretas de autenticación, autorización, gestión de sesiones, protección de credenciales y control de accesos deberán ajustarse al riesgo, a la criticidad del sistema y a la información tratada. Su desarrollo operativo se concreta en las guías aplicables.

### 5.2. Integridad

Las aplicaciones deberán proteger la integridad de la información durante su entrada, procesamiento, almacenamiento, intercambio y salida.

A tal efecto, se aplicarán mecanismos que garanticen la validación de los datos, el control de cambios, la protección frente a manipulaciones no autorizadas y el uso seguro de componentes propios y de terceros.

La organización establecerá medidas para prevenir errores de diseño o implementación que puedan comprometer la integridad de la información o el funcionamiento de la aplicación, incluyendo controles adecuados sobre dependencias, componentes externos y actualizaciones.

### 5.3. Confidencialidad

Las aplicaciones deberán proteger la información frente a accesos, divulgaciones o exposiciones no autorizadas.

La Autoritat Portuària de Barcelona aplicará medidas de protección adecuadas sobre credenciales, datos sensibles, ficheros de configuración, comunicaciones y registros, así como controles que limiten el acceso a la información según su clasificación y necesidad de uso.

Las aplicaciones no deberán exponer información innecesaria a usuarios, sistemas externos o componentes no autorizados.

### 5.4. Disponibilidad

Las aplicaciones deberán diseñarse y mantenerse de forma que ofrezcan un nivel de disponibilidad adecuado a su criticidad y al impacto que tendría su interrupción.

La organización establecerá medidas para prevenir fallos, reducir el riesgo de degradación del servicio y facilitar la recuperación ante incidentes, incluyendo prácticas de mantenimiento seguro, gestión de errores, actualización de componentes, respaldo y continuidad del servicio cuando resulte necesario.

### 5.5. Trazabilidad

Las aplicaciones deberán permitir registrar y reconstruir las acciones relevantes realizadas sobre ellas, especialmente aquellas que afecten a la seguridad, al acceso a la información, a la administración del sistema o a la integridad de los datos.

Los registros deberán ser suficientes para detectar incidentes, facilitar su investigación y acreditar el cumplimiento de las medidas de seguridad aplicables, sin incluir información sensible innecesaria.

## 6. Requisitos de seguridad para la subcontratación

Cuando el desarrollo, mantenimiento, soporte o evolución de aplicaciones sea realizado por terceros, la Autoritat Portuària de Barcelona exigirá que se apliquen requisitos de seguridad equivalentes a los establecidos internamente.

Los proveedores deberán comprometerse contractualmente al cumplimiento de la normativa aplicable, de los requisitos del ENS que correspondan al sistema afectado y de las condiciones de seguridad definidas por la organización.

La evaluación y contratación de proveedores deberá considerar, al menos, su capacidad técnica y organizativa para desarrollar o mantener software de forma segura, su experiencia y madurez en seguridad, las garantías de cumplimiento normativo, la gestión de componentes de terceros y dependencias, la segregación de entornos, la protección de la información tratada, la notificación y gestión de incidentes y la devolución o destrucción segura de la información al finalizar el servicio.

Los contratos deberán incluir cláusulas específicas sobre confidencialidad, control de accesos, auditoría, subcontratación, pruebas de seguridad, propiedad del código, continuidad del servicio y finalización segura del contrato.

## 7. Cumplimiento y revisión

La Autoritat Portuària de Barcelona supervisará el cumplimiento de esta política y adoptará las medidas correctoras necesarias cuando detecte desviaciones o incumplimientos.

La política se revisará periódicamente y se actualizará cuando se produzcan cambios relevantes en la normativa, en la tecnología, en los riesgos identificados o en el modelo de desarrollo y operación de las aplicaciones.

La organización conservará las evidencias necesarias para acreditar la aplicación de esta política y la implantación de los controles asociados.

## 8. Registros

- CHL - CheckList de Controles de Seguridad en el Desarrollo
- Documentación de requisitos de seguridad
- Evidencias de validación y aprobación
- Registros de revisiones y auditorías
- Documentación contractual y de seguridad de proveedores
- Inventarios y registros asociados a aplicaciones, componentes y servicios

## 9. Referencias

- OWASP (Open Web Application Security Project)
- RD 311/2022 Esquema Nacional de Seguridad
- CCN-CERT_BP-28 Recomendaciones sobre Desarrollo Seguro
- Guía de Protección de las Aplicaciones
- Guía de Seguridad de las APIs
- Guía de Seguridad en Contenedores y Cloud

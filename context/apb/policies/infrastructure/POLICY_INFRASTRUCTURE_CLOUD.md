# Política de Infraestructura: Enfoque hacia Soluciones en la Nube

## Contexto

En los últimos años hemos estado migrando gradualmente nuestros servicios y aplicaciones hacia entornos en la nube. Esta transición responde a una estrategia alineada con los objetivos de la empresa y el plan de SSI, que busca optimizar recursos, mejorar la escalabilidad y garantizar una mayor flexibilidad en nuestras aplicaciones. En este contexto, es importante destacar que el entorno On-Premise NO debe seguir creciendo y debemos ir migrando hacia la nube.

## ¿En qué consiste la nueva política?

Cualquier solicitud de nuevos proyectos o ampliaciones de infraestructura deberá ser evaluada bajo esta política.

### Para aplicaciones de desarrollo a medida nuevas

- **Despliegue en Cloud Azure:** Las aplicaciones nuevas se desplegarán en contenedores Docker en Azure.
- **Transformación a Cloud:** Para las aplicaciones que ya están en desarrollo pero aún no han salido a producción, se estudiará caso por caso cuándo realizar la migración a la nube. Sin embargo, antes de su salida a PRO se realizará la adaptación y despliegue en Cloud.
- **Gestión de identidades:** Se implementará Entra ID como gestor de identidades, integrado con Microsoft 365 como proveedor de SSO (Single Sign-On).
- **Gestión documental:** El almacenamiento de documentos de las aplicaciones se gestionará en Cloud, utilizando SharePoint o Azure, según las necesidades específicas de cada aplicación.

### Para productos de mercado nuevos o migraciones de productos On-Premise a Cloud

- **Gestión de identidades:** Se utilizará Entra ID como gestor de identidades, junto con Microsoft 365 como SSO.
- **Gestión documental:** El almacenamiento será responsabilidad del producto en cuestión y deberá estar alojado en Cloud. No se proporcionará almacenamiento a través de recursos de APB.
- **Infraestructura:** Siempre que sea posible se contratarán productos SaaS. Si el fabricante no lo proporciona, la alternativa será un producto dockerizado que se desplegará en Cloud.

### Proyectos en paralelo para aplicaciones existentes

Actualmente, estamos trabajando en dos proyectos clave para migrar las aplicaciones existentes:

1. **Migración de gestor de identidades y SSO:** Para centralizar y modernizar la gestión de identidades y la autenticación unificada, para posteriormente dar de baja CAS, AD y LDAP. La autenticación que antes se hiciera con certificado a través de la integración con Clave de AGE se mantiene, pero puede ser necesario hacer adaptaciones en función de la aplicación.
2. **Migración Gestión documental:** Trasladar el almacenamiento de las aplicaciones existentes a la nube, para posteriormente dar de baja Alfresco.

## ¿Qué implica esto?

A partir de ahora, cualquier solicitud de nuevos proyectos o ampliaciones de infraestructura deberá ajustarse a esta política. Esto significa que:

- No se debería adquirir o ampliar infraestructura virtual, hardware o software On-Premise, salvo en casos excepcionales y debidamente justificados.
- Se priorizarán soluciones en la nube para cualquier nueva iniciativa, asegurando que estén alineadas con nuestra estrategia tecnológica.
- Trabajaremos en la migración progresiva de los servicios actuales que aún operan en entornos On-Premise hacia la nube.

Entendemos que este cambio puede generar dudas o requerir ajustes en ciertos procesos, por lo que el equipo de Tecnología está a disposición para brindar el apoyo necesario durante esta transición. Si tienes alguna pregunta o necesitas más detalles, no dudes en contactar con el área de Tecnologia i Operacions.

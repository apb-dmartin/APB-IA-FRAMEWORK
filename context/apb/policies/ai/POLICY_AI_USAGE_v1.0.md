# Política APB Uso de IA en para desarrollo de software y soporte técnico_v1(1)

Sistemas de la Información 
Uso de IA en para desarrollo de software y soporte técnico 
Pàgina 1 de 6 
 
 
Políticas de cumplimiento APB  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Política APB  
Uso de IA en para desarrollo de software 
y soporte técnico 

 
 
Sistemas de la Información 
Uso de IA en para desarrollo de software y soporte técnico 
Pàgina 2 de 6 
 
 
Políticas de cumplimiento APB  
Historial de revisiones 
 
Versión 
Descripción  
Autor 
Acción  
Fecha  
01.00 
Definición  
Débora Martín 
Creación 
27-04-2026 
 
 
 
 
 
 
 
 
 
 
 
 
Débora Martin (CTO) 
Albert Prats (CISO) 
Aprobación 
06-05-2026 
 
 
 

 
 
Sistemas de la Información 
Uso de IA en para desarrollo de software y soporte técnico 
Pàgina 3 de 6 
 
 
Políticas de cumplimiento APB  
ÍNDICE 
 
1. 
Objetivo ............................................................................................................................... 4 
2. 
Ámbito de aplicación ........................................................................................................... 4 
3. 
Principios generales ............................................................................................................. 4 
4. 
Herramientas autorizadas ................................................................................................... 4 
5. 
Reglas de uso ....................................................................................................................... 4 
6. 
Resultados generados por IA ............................................................................................... 5 
7. 
Revisión humana obligatoria ............................................................................................... 5 
8. 
Seguridad técnica ................................................................................................................. 5 
9. 
Propiedad intelectual y reutilización ................................................................................... 5 
1

0. 
Trazabilidad y auditoría ....................................................................................................... 5 
1

1. 
Incumplimientos .................................................................................................................. 6 
1

2. 
Excepciones.......................................................................................................................... 6 
1

3. 
Evolución tecnológica .......................................................................................................... 6 
1

4. 
Guía corporativa .................................................................................................................. 6 
 
 
 
 

 
 
Sistemas de la Información 
Uso de IA en para desarrollo de software y soporte técnico 
Pàgina 4 de 6 
 
 
Políticas de cumplimiento APB  
1. Objetivo 
La presente política regula el uso de herramientas de inteligencia artificial, como por ejemplo  
GitHub Copilot, en APB y en todos los trabajos realizados para APB por personal interno o proveedores 
externos. Su finalidad es permitir el uso controlado de IA en actividades de desarrollo y soporte técnico, 
garantizando la confidencialidad, la seguridad de la información, la trazabilidad de las decisiones técnicas, 
la calidad del software y la protección de la propiedad intelectual de APB. 
2. Ámbito de aplicación 
Esta política aplica a todo el personal de APB y a todo proveedor externo que participe en cualquier fase 
del ciclo de vida del software o de los servicios tecnológicos de APB, incluyendo desarrollo a medida, 
mantenimiento, QA, DevOps, seguridad, consultoría, soporte, data/IA, infraestructura como código y 
configuración como código. La política se aplica a todos los proyectos, sistemas y activos de APB, con 
independencia de su criticidad o del tipo de información tratada. 
3. Principios generales 
El uso de IA se permite como apoyo a la productividad, pero no sustituye la responsabilidad profesional 
ni la obligación de cumplir las políticas de seguridad de APB. Todo resultado generado o asistido por IA 
debe ser revisado y validado por un técnico senior antes de su incorporación, despliegue o ejecución. La 
responsabilidad sobre el resultado final recaerá en el proveedor y en el técnico revisor designado, según 
lo establecido contractualmente y sin perjuicio de las obligaciones de APB como titular del entorno y de 
la información. 
4. Herramientas autorizadas 
Las herramientas de IA, incluida GitHub Copilot, solo podrán usarse si han sido previamente aprobadas 
por el equipo de ciberseguridad de APB y el responsable técnico correspondiente, como por ejemplo CTO. 
APB podrá autorizar, limitar o revocar en cualquier momento el uso de una herramienta concreta, de una 
funcionalidad específica o de un modelo determinado cuando existan motivos de seguridad, 
confidencialidad, cumplimiento o riesgo operativo. Esta política es extensible a otras herramientas de IA 
que puedan incorporarse en el futuro. 
La autorización por APB del uso de herramientas de inteligencia artificial no implica obligación alguna de 
suministrar licencias, suscripciones o credenciales. Salvo autorización expresa en contrario, el proveedor 
será responsable de disponer y costear los medios de acceso necesarios para su personal, incluyendo las 
licencias de las herramientas aprobadas. 
5. Reglas de uso 
Queda prohibido introducir en herramientas de IA información clasificada, sensible o protegida por ENS, 
así como credenciales, secretos, claves API, tokens, certificados, arquitectura interna, código fuente no 
autorizado, configuraciones, logs, tickets internos, documentación técnica no pública, datos personales y 
cualquier otro dato que APB haya clasificado como restringido. De forma recomendable, y salvo 
autorización expresa y control reforzado, no deberá utilizarse IA con información anonimizada si existe 

 
 
Sistemas de la Información 
Uso de IA en para desarrollo de software y soporte técnico 
Pàgina 5 de 6 
 
 
Políticas de cumplimiento APB  
riesgo de reidentificación. El uso de IA pública no corporativa solo se permitirá en supuestos 
excepcionales, justificados y autorizados previamente por APB. 
6. Resultados generados por IA 
Todo código, script, prueba automática, consulta SQL, infraestructura como código, configuración como 
código, documentación técnica o cualquier otro artefacto generado o asistido por IA deberá marcarse 
como tal. La regla es simple: todo uso de IA se marca. La identificación se realizará mediante etiquetas en 
commits, marcas en comentarios, metadatos en pull requests y campos específicos en Jira, de forma que 
pueda auditarse el origen del trabajo y la intervención humana en su revisión. 
7. Revisión humana obligatoria 
Ningún contenido generado o asistido por IA podrá incorporarse a repositorios, ejecutarse en entornos 
de APB ni entregarse como resultado de trabajo sin revisión previa de un técnico senior. La revisión deberá 
confirmar corrección funcional, seguridad, cumplimiento de estándares de desarrollo, ausencia de 
secretos, adecuación a la arquitectura y compatibilidad con el entorno objetivo. La evidencia mínima 
exigible será la aprobación humana registrada en el sistema de trabajo definido por APB. 
8. Seguridad técnica 
Todo trabajo asistido por IA deberá someterse a los controles de seguridad aplicables antes de su 
integración, incluyendo análisis estático, análisis dinámico cuando proceda, revisión de dependencias, 
detección de secretos, validación de licencias, inspección de configuraciones y controles equivalentes 
definidos por APB. Queda prohibido usar IA para introducir o modificar componentes de alto riesgo, como 
autenticación, autorización, cifrado, firma, gestión de identidades o logging de seguridad, sin aprobación 
previa y expresa de APB. 
9. Propiedad intelectual y reutilización 
Todo entregable desarrollado para APB, con o sin uso de IA, será titularidad de APB conforme al contrato 
y a las condiciones aplicables.  
Cualquier skill, patrón, código, prueba, prompt estructurado, configuración, plantilla o artefacto utilizado 
en trabajos para APB deberá ponerse a disposición de APB para su reutilización futura por el equipo 
completo de desarrollo o técnico correspondiente. Las conversaciones, prompts, respuestas de IA y 
configuraciones de agentes vinculadas a trabajo de APB se considerarán parte del material de trabajo y 
estarán sujetas a confidencialidad. 
1

0. Trazabilidad y auditoría 
APB podrá auditar en cualquier momento el cumplimiento de esta política. Los proveedores y el personal 
interno deberán poder justificar qué herramientas de IA se han utilizado, en qué fase del ciclo de vida y 
qué técnico senior ha aprobado el resultado. La conservación de evidencias se ajustará al plazo que 
determine APB en su política de retención o en el expediente de proyecto correspondiente. 

 
 
Sistemas de la Información 
Uso de IA en para desarrollo de software y soporte técnico 
Pàgina 6 de 6 
 
 
Políticas de cumplimiento APB  
1

1. Incumplimientos 
Cualquier uso no autorizado de IA, cualquier introducción accidental de información sensible en una 
herramienta de IA o cualquier incumplimiento de esta política deberá tramitarse mediante el 
procedimiento corporativo de gestión de incumplimientos, abriendo el correspondiente ticket en Jira. APB 
podrá ordenar la retirada inmediata del material afectado, la corrección del incidente, la revisión 
contractual y cualesquiera otras medidas correctoras o disciplinarias que correspondan. 
1

2. Excepciones 
Cualquier excepción a esta política deberá ser solicitada y aprobada previamente por APB, con 
justificación de necesidad, alcance, duración, riesgo residual y medidas compensatorias. Las excepciones 
tendrán vigencia limitada y deberán revisarse o renovarse según determine APB. La autorización podrá 
revocarse en cualquier momento si cambia el riesgo, la herramienta o el uso previsto. 
1

3. Evolución tecnológica 
Esta política se aplica a GitHub Copilot y a cualquier otra solución de IA que APB autorice en el futuro. 
Toda nueva herramienta deberá someterse al mismo proceso de aprobación, control, trazabilidad, 
revisión humana y condiciones de seguridad y confidencialidad antes de su uso en cualquier trabajo 
relacionado con APB. 
1

4. Guía corporativa 
La presente política desarrolla y concreta, para el ámbito específico del desarrollo de software, los 
servicios tecnológicos y el uso de herramientas de inteligencia artificial como GitHub Copilot, lo 
establecido en la Guía de Gestión de Herramientas de Inteligencia Artificial de la Autoritat Portuària de 
Barcelona. En caso de conflicto interpretativo, prevalecerá lo dispuesto en la normativa corporativa de 
seguridad de la información y en la citada Guía, así como en el Esquema Nacional de Seguridad y en la 
legislación vigente que resulte de aplicación.

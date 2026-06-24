# Procedimiento - Evaluación de riesgos en incumplimientos - Política QA para desarrollos Docks - v1(1)

ÍNDICE

1.	Introducción	4

2.	Principios generales	4

3.	Criterios de evaluación de riesgos	4

4.	Análisis de riesgos por incumplimiento	6

4.

1.	Riesgo de seguridad y control de acceso	6

4.

2.	Riesgo de ocultación de errores y degradación de la operabilidad	7

4.

3.	Riesgo por uso de SOAP/WebService no homologado	7

4.

4.	Riesgo por uso de plantillas base desactualizadas	8

4.

5.	Riesgo por documentación insuficiente	8

4.

6.	Riesgo por incumplir el Quality Gate de Sonar	8

4.

7.	Riesgo por eludir la clasificación Compliance/Legacy y controles del pipeline	10

4.

8.	Riesgo de despliegue con incumplimientos en PRE/PRO	11

5.	Catálogo de riesgos corporativo	11

6.	Riesgos transversales	15

6.

1.	Riesgo de pérdida de trazabilidad y auditabilidad	15

6.

2.	Riesgo de acumulación de deuda técnica y excepciones	15

6.

3.	Riesgo de debilitamiento del control preventivo	15

6.

4.	Riesgo normativo y de gestión del riesgo insuficiente	15

7.	Autorización de excepciones	15

8.	Informe (Plantilla)	16

	

Introducción 

El presente documento establece:

Los criterios corporativos para la evaluación de riesgos 

El modelo oficial de registro de riesgos (risk register) 

El catálogo base de riesgos de referencia 

El objetivo es garantizar una gestión homogénea, trazable y alineada con:

Esquema Nacional de Seguridad (ENS) 

ISO/IEC 27001 (Sistema de Gestión de Seguridad de la Información)

Este procedimiento tiene como objetivo definir los criterios para evaluar los riesgos de los incumplimientos detectados en la política relacionada con QA y seguridad en Desarrollo a medida Docks. Tiene en cuenta:

Qué riesgo introduce cada familia de incumplimientos y cuándo ese riesgo tendería a ser alto o crítico a efectos de autorizar o no una excepción.  

Qué efectos puede tener sobre confidencialidad, integridad, disponibilidad, trazabilidad, mantenibilidad, operación y cumplimiento.

Además que la criticidad debe valorarse considerando impacto en seguridad, disponibilidad/estabilidad, integridad de datos, sostenibilidad tecnológica y exposición normativa. 

Principios generales

La gestión de riesgos en IT se basa en los siguientes principios:

Responsabilidad: todo riesgo tiene un propietario (Risk Owner) 

Trazabilidad: toda decisión debe quedar registrada 

Proporcionalidad: el tratamiento del riesgo debe ser acorde a su nivel 

Temporalidad: toda aceptación de riesgo es temporal 

Prevención: se prioriza evitar y mitigar sobre aceptar

Criterios de evaluación de riesgos

Identificación del riesgo

Todo riesgo debe definirse en formato:

“Existe riesgo de [amenaza] debido a [vulnerabilidad/incumplimiento], afectando a [activo]”

Ejemplo:

Riesgo de acceso no autorizado debido a falta de autenticación en endpoints, afectando al sistema de gestión de clientes.

Dimensiones de impacto (ENS)

Cada riesgo se evalúa en cuatro dimensiones:

Escala de impacto

Impacto total = máximo (C, I, D, T)

Probabilidad

Riesgo inherente

RIESGO_INHERENTE = IMPACTO × PROBABILIDAD

Controles compensatorios

Riesgo residual

RIESGO_RESIDUAL = RIESGO_INHERENTE + AJUSTE_CONTROLES

Clasificación del riesgo

Tratamiento del riesgo (ISO 27001)

Todo riesgo debe tener un tratamiento definido:

Criterios de aceptación del riesgo

Análisis de riesgos por incumplimiento 

Riesgo de seguridad y control de acceso

La política exige que todos los endpoints estén protegidos mediante mecanismos de autorización.

Riesgo si no se cumple

El incumplimiento de este control introduce un riesgo directo de:

Acceso no autorizado a operaciones o datos. 

Ejecución de funciones internas por actores no previstos. 

Elevación indebida de privilegios si la autorización es incompleta o inconsistente. 

Ruptura de segregación funcional entre perfiles. 

Valoración cualitativa

Alta si el endpoint opera sobre datos sensibles, operaciones administrativas o servicios expuestos. 

Crítica si permite acciones con impacto sobre integridad, disponibilidad o trazabilidad. 

Riesgo de ocultación de errores y degradación de la operabilidad

La política prohíbe usar try/catch como mecanismo de validación ya que los errores inesperados deben registrarse siempre, no ocultarse. El framework Docks los captura y facilita la resolución de incidencias. 

Riesgo si no se cumple

No cumplir esta regla genera riesgo de:

Ocultación de fallos reales. 

Diagnósticos incompletos o falsos positivos de funcionamiento correcto. 

Retraso en la detección de defectos. 

Mayor MTTR por falta de Observabilidad. 

Tratamiento incorrecto de errores técnicos como si fueran errores funcionales. 

Argumento del riesgo

La política distingue expresamente entre errores inesperados y errores funcionales. Si se capturan y absorben fallos técnicos dentro de lógica de aplicación, se degrada el registro de evidencias y la capacidad de diagnóstico. El riesgo es pérdida de visibilidad operativa y, por tanto, aumento del tiempo y complejidad de resolución de incidentes.

Valoración cualitativa

Media-Alta por impacto operativo. 

Alta si el servicio es crítico o si la captura de excepciones puede ocultar fallos de infraestructura, persistencia o parsing. 

Riesgo por uso de SOAP/WebService no homologado

La política QA prohíbe SOAP/WSDL. 

Riesgo si no se cumple

El uso o mantenimiento no controlado de SOAP/WebService introduce riesgo de:

Aumento de complejidad técnica y de integración. 

Menor capacidad de observación uniforme respecto al estándar actual. 

Ampliación del coste y plazo de futuras migraciones. 

Argumento del riesgo

No cumple los requisitos actuales de APB en seguridad, mantenibilidad y Observabilidad, siendo una desalineación con el marco técnico corporativo, que incrementa exposición operativa y deuda de integración.

Valoración cualitativa

Alta cuando el sistema nuevo nazca ya fuera del estándar. 

Media-Alta en legacy si existe plan de retirada y aislamiento. 

Riesgo por uso de plantillas base desactualizadas

La política exige versiones mínimas para garantizar compatibilidad con mecanismos de seguridad y auditoría y reducir el riesgo operativo asociado a versiones desactualizadas. 

Riesgo si no se cumple

Incompatibilidad con controles corporativos. 

Pérdida o degradación de capacidades de auditoría. 

Divergencia entre proyectos. 

Aumento de defectos de despliegue o integración con pipeline/plataforma. 

Deuda técnica estructural desde el arranque. 

Argumento del riesgo

La propia política conecta el versionado con seguridad y auditoría. Por tanto, usar plantillas antiguas puede dejar al servicio fuera del perímetro previsto de control y soporte.

Valoración cualitativa

Media en componentes internos de bajo impacto. 

Alta si afecta a mecanismos transversales de seguridad, logging o despliegue. 

Riesgo por documentación insuficiente

La política exige documentación técnica y de explotación mínima para permitir comprensión, mantenimiento y operación. 

Riesgo si no se cumple

Dependencia excesiva de conocimiento tácito. 

Mayor probabilidad de error en operación, soporte y cambios. 

Retrasos en recuperación ante incidencias. 

Dificultad para validar cumplimiento y para auditar. 

Riesgo de cambio inseguro por entendimiento incompleto del servicio. 

Argumento del riesgo

Aquí el daño suele ser menos inmediato que en seguridad, pero es muy real en continuidad y gobernanza. Si un sistema no está suficientemente documentado, su mantenibilidad y operabilidad se vuelven dependientes de personas concretas, lo que contradice directamente el objetivo declarado de trazabilidad, mantenibilidad y estabilidad. 

Valoración cualitativa

Media por defecto. 

Alta si se combina con rotación de equipos, servicio crítico o incidentes recurrentes. 

Riesgo por incumplir el Quality Gate de Sonar

La política establece umbrales mínimos de QA puede afectar a estabilidad, deuda técnica o vulnerabilidades. 

Blocker Issues > 0

Las incidencias Blocker pueden comprometer el funcionamiento, generar fallos en ejecución o introducir vulnerabilidades explotables, y que no son compatibles con un despliegue seguro. 

Riesgo

Fallo severo en ejecución. 

Comportamiento no controlado. 

Exposición a vulnerabilidades explotables. 

Valoración

Alta o crítica por definición del propio criterio en Sonar. 

Cobertura < 60 %

La cobertura mínima porque reduce la probabilidad de que errores no detectados lleguen a producción y facilita la estabilidad del software ante cambios futuros. 

Riesgo

Regresiones no detectadas. 

Baja confianza en cambios y refactorizaciones. 

Aumento de fallos post-despliegue. 

Menor velocidad segura de evolución. 

Argumento
La baja cobertura no prueba por sí sola que el software falle, pero sí aumenta razonablemente la incertidumbre operativa y el riesgo de defectos no descubiertos antes de PRE/PRO.

Valoración

Media-Alta. sube a Alta si el cambio es grande o el servicio es crítico. 

Maintainability < B

Niveles inferiores implican duplicidad, complejidad excesiva o malas prácticas estructurales.

Riesgo

Incremento de coste y plazo de cambio. 

Mayor probabilidad de introducir defectos al modificar. 

Dependencia de conocimiento experto puntual. 

Acumulación de deuda técnica. 

Valoración

Media a corto plazo. 

Alta como riesgo acumulativo y arquitectónico. 

Reliability < C

Defectos que pueden provocar comportamientos no previstos o interrupciones del servicio. 

Riesgo

Errores en tiempo de ejecución. 

Inestabilidad. 

Degradación de disponibilidad. 

Incidentes productivos. 

Valoración

Media por defecto. 

Alta si el servicio es relevante o crítico. 

Security < C

Vulnerabilidades o prácticas inseguras que afectan a confidencialidad, integridad o disponibilidad. 

Riesgo

Vulnerabilidades explotables. 

Tratamiento inseguro de credenciales o validaciones. 

Exposición de datos o manipulación indebida. 

Valoración

Alta por defecto.

Crítica si hay datos sensibles o exposición externa. 

Riesgo por eludir la clasificación Compliance/Legacy y controles del pipeline

La política exige que todo pipeline tenga etiqueta explícita, prohíbe pipelines sin clasificación o cambios sin aprobación formal. 

Riesgo si no se cumple

Bypass de controles. 

Aplicación inconsistente de exigencias entre equipos. 

Pérdida de homogeneidad y de trazabilidad. 

Riesgo de que software que debería ser compliance se trate como legacy o viceversa. 

Debilitamiento del modelo de auditoría. 

Argumento del riesgo

Este punto es especialmente sensible porque afecta al sistema de control, no sólo al código. Si se degrada el mecanismo que decide qué validaciones aplican, se debilita la fiabilidad del cumplimiento entero.

Valoración cualitativa

Alta por impacto de gobernanza y control interno. 

Riesgo de despliegue con incumplimientos en PRE/PRO

Riesgo si no se cumple

Materialización de defectos no validados en entornos críticos. 

Pérdida de eficacia del control preventivo. 

Precedente organizativo que trivializa el bloqueo. 

Incremento del riesgo residual agregado si se acumulan excepciones. 

Argumento del riesgo

Cuando un control está diseñado como bloqueante antes de PRE/PRO, autorizar su incumplimiento no sólo acepta el defecto concreto: también acepta no aplicar el último filtro preventivo antes de entornos críticos.

Valoración cualitativa

Alta por diseño del propio proceso. 

Crítica si el incumplimiento afecta a seguridad, fiabilidad o autorización. 

Catálogo de riesgos corporativo

Desarrollo seguro

QA

Integración 

Riesgos transversales 

Riesgo de pérdida de trazabilidad y auditabilidad

El procedimiento exige registro formal, evidencias, responsables, estados trazables y validación independiente antes del cierre. 

Cuando se incumplen controles de y además se relajan registro/seguimiento, el problema deja de ser sólo técnico: pasa a ser también de gobernanza. Siendo más difícil analizar causa raíz o sostener una aceptación de riesgo ante auditoría.

Riesgo de acumulación de deuda técnica y excepciones

La política QA incorpora el principio de no incremento de deuda y el procedimiento general prevé limitar o denegar nuevas excepciones si se acumulan. 

Una excepción aislada puede ser tolerable. varias excepciones sobre el mismo servicio cambian el perfil de riesgo del sistema completo.

Riesgo de debilitamiento del control preventivo

Si se habitúa a autorizar incumplimientos en controles que nacieron para bloquear PRE/PRO, el riesgo residual real ya no es el de un ticket concreto, sino el de normalizar el bypass del control. 

Riesgo normativo y de gestión del riesgo insuficiente

La aceptación de riesgos y las excepciones se han definido de forma alineada ENS e ISO 

27001. Por tanto, una excepción mal argumentada, sin medidas compensatorias ni fecha de corrección, no sólo aumenta riesgo técnico: también debilita el marco formal de gestión del riesgo.

Autorización de excepciones

En términos de autorización de excepciones, sólo deberían admitirse cuando el incumplimiento no comprometa de forma significativa seguridad, estabilidad o capacidad de validación, y exista una remediación acotada. 

No cumplir la política de QA no es sólo un problema de “calidad de código”, introduce riesgo directo de fallos en ejecución, defectos no detectados, exposición de operaciones, deuda técnica creciente, menor capacidad de auditoría y degradación de la estabilidad en PRE/PRO. 

Excepción no autorizable

Los incumplimientos que:

Afecten a autorización/autenticación de endpoints. 

Mantengan blocker issues o security/ reliability por debajo del umbral mínimo. 

Impliquen bypass de controles del pipeline o clasificación incorrecta de compliance/legacy. 

Se justifique por falta de tiempo, planificación deficiente o presión de entrega, el procedimiento general de gestión de incumplimientos lo define expresamente. 

Excepciones potencialmente aceptables

Riesgo residual bajo o medio. 

Existencia de controles compensatorios efectivos. 

Carácter temporal. 

Plan de remediación definido. 

Aprobación formal documentada. 

Informe (Plantilla)

Identificación

Objeto: Evaluación del riesgo derivado del incumplimiento de políticas de QA 

Sistema/Activo: [Completar] 

Responsable del sistema: [Completar] 

Fecha: [Completar] 

Analista: [Completar] 

Resumen ejecutivo

Resumen del informe con enfoque en gestores y funcionales.

Análisis de riesgos 

Tabla resumen con los riesgos y su nivel

Evaluación de riesgos

Observaciones de auditoría

Espacio para comentarios adicionales del tipo: carencias de documentación, evidencia, gobernanza o trazabilidad

Decisión

Resultado: [AUTORIZADO / NO AUTORIZADO] 

Justificación: [Basada en riesgo residual] 

Condiciones: 

Controles compensatorios 

Fecha límite 

Plan de remediación 

Aprobación

Responsable Servicio: [Completar]

Responsable Seguridad: [Completar]

Responsable Arquitectura: [Completar]

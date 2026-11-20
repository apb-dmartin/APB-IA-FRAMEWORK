---
id: "third-roboflow-supervision-v1.0"
name: "Skill: Computer Vision Detection & Tracking (roboflow/supervision)"
description: "Utilidades reutilizables de visión artificial — anotación de detecciones/segmentación, tracking multi-objeto entre frames, análisis por zonas, conversión de datasets (YOLO/COCO/Pascal VOC) y métricas de evaluación de modelos (mAP, matriz de confusión) — adaptadas del repositorio público roboflow/supervision. Sin caso de uso APB confirmado a la fecha de incorporación."
version: "1.0.0"
status: "draft"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
source_repo: "https://github.com/roboflow/supervision"
source_license: "MIT"
source_commit: "fd3de344dc9ba2dacd1e996ee6416b60d5e4d0d2"
created_date: "2026-07-07"
review_date: "2026-07-07"
---

# Skill: Computer Vision Detection & Tracking (roboflow/supervision)

---

## Descripción

Adaptación como skill de referencia del repositorio público `roboflow/supervision`
(MIT, ~47k ⭐, +1M descargas/mes en PyPI, activo). Es una librería Python que
estandariza el post-procesado de salidas de modelos de detección/segmentación:
anotación visual, tracking, conteo por zonas, gestión de datasets y métricas de
evaluación — agnóstica del modelo de detección usado (soporta salidas de
Ultralytics/YOLO, Roboflow Inference, Hugging Face Transformers, SAM, Detectron2,
MMDetection, YOLO-NAS, PaddleDetection, entre otros).

> **Nota de gobernanza (obligatoria — principio `apb-dev-simplicity-first-v1.0`):**
> esta skill se incorpora al catálogo **a petición explícita**, verificada contra
> el repositorio real (licencia MIT confirmada vía API de GitHub, commit real fijado
> — no `HEAD`). **No existe hoy ningún caso de uso de negocio confirmado por
> Arquitectura APB ni por Débora** para visión artificial dentro del framework: no
> hay ninguna otra mención a visión artificial, cámaras, detección de objetos o
> tracking en el resto del repositorio (verificado por grep exhaustivo, 2026-07-07).
> Por tanto:
> - `consumed_by` se deja vacío — **ningún agente/workflow la invoca todavía**.
> - No se inventa un dominio de negocio (p. ej. "analítica de cámaras portuarias")
>   para justificar su incorporación — sería especulación no confirmada.
> - Antes de conectarla a cualquier agente o workflow real, Arquitectura APB debe
>   identificar y documentar el caso de uso concreto (igual que se hizo para otras
>   skills sin consumidor claro, ver `third-lum1104-knowledge-graph-v1.0`).

## Capacidades

- **Anotadores de detección/segmentación:** bounding boxes, máscaras de
  segmentación, labels y trazas ("traces"), sobre imagen o vídeo frame a frame.
- **Tracking multi-objeto:** asignación de IDs persistentes entre frames de vídeo
  (integra ByteTrack).
- **Análisis por zonas:** conteo y filtrado de detecciones dentro de polígonos
  definidos (zonas de interés).
- **Gestión de datasets:** carga y conversión entre formatos YOLO, COCO y
  Pascal VOC.
- **Métricas de evaluación de modelos:** mAP, matrices de confusión y otras
  métricas estándar de benchmarking de modelos de visión.

## Inputs

- `model_output`: salida cruda de un modelo de detección/segmentación soportado
  (Ultralytics/YOLO, Roboflow Inference, Transformers, SAM, Detectron2,
  MMDetection, YOLO-NAS, PaddleDetection u otro compatible)
- `media`: imagen o secuencia de vídeo sobre la que anotar/trackear
- `zones` (opcional): definición de polígonos para conteo/filtrado por zona
- `dataset_format` (opcional): formato de origen/destino para conversión de
  datasets (`yolo`, `coco`, `pascal_voc`)

## Outputs

- `annotated_media`: imagen o vídeo con anotaciones (boxes/máscaras/labels)
  aplicadas
- `tracked_detections`: detecciones con ID persistente asignado entre frames
- `zone_counts`: conteos/filtrados de detecciones por zona definida
- `evaluation_metrics`: mAP, matriz de confusión u otras métricas calculadas

## Restricciones

- **Requiere Python ≥ 3.9** — verificar compatibilidad con el stack de despliegue
  real antes de cualquier uso (APB estandariza en .NET/Azure; cualquier
  componente que use esta skill implica una pieza Python nueva en el stack,
  decisión que corresponde a Arquitectura, no a esta skill).
- No incluye modelo de detección propio — depende de un modelo externo ya
  entrenado (Ultralytics/YOLO u otro) cuya procedencia, licencia y gobernanza de
  datos de entrenamiento deben evaluarse aparte si se llega a usar.
- No hay caso de uso ni agente consumidor confirmado — no debe wirearse a
  ningún agente/workflow real sin que Arquitectura APB documente antes el caso
  de uso concreto (ver Nota de gobernanza arriba).
- Si en el futuro se conecta a fuentes de vídeo/imagen reales (p. ej. CCTV
  portuaria), aplican consideraciones de protección de datos (RGPD) e ISO 27001
  que esta skill no cubre — deben evaluarse con `apb-sec-risk-analysis-v1.0` y
  `apb-gov-org-risk-report-v1.0` antes de cualquier despliegue.

## Ejemplo de Uso

```
Invocar: third-roboflow-supervision-v1.0
Input: { model_output: "<salida YOLOv8 sobre vídeo de prueba>",
         media: "video_prueba.mp4",
         zones: [{"nombre": "carril_entrada", "poligono": [...]}] }
Output: Vídeo anotado con bounding boxes + IDs de tracking persistentes +
        conteo de detecciones en "carril_entrada" por frame
```

---
*Adaptado por APB AI Framework. Licencia MIT original respetada. Sin consumidor
real todavía — ver Nota de gobernanza.*

---
id: "apb-dev-gis-django-v1.0"
name: "Desarrollo de Servicios GIS con Django/GeoDjango"
description: "Desarrollar servicios de Sistemas de Información Geográfica (GIS) usando Django, GeoDjango y PostGIS. Incluye modelos espaciales, consultas geoespaciales, APIs REST para datos geográficos y visualización."
version: "1.0.0"
status: "draft"
owner: "Desarrollo <arquitectura@portdebarcelona.cat>"
domain: "development"
autonomy_level: 1
created_date: "2026-06-20"
review_date: "2026-06-22"
---

# Desarrollo de Servicios GIS con Django/GeoDjango

---

## 🎯 Propósito

Desarrollar servicios de Sistemas de Información Geográfica (GIS) usando Django, GeoDjango y PostGIS. Incluye modelos espaciales, consultas geoespaciales, APIs REST para datos geográficos y visualización.

---

## ⚡ Trigger

Cuando un proyecto requiere funcionalidades geoespaciales: mapas, rutas, zonas, coordenadas, análisis espacial.

---

## 📥 Input

- Requisitos de funcionalidad geoespacial
- Datos geográficos de origen (shapefiles, GeoJSON, KML)
- Especificación de modelos de datos
- Requisitos de performance (volumen de datos espaciales)

---

## 📤 Output

- Modelos Django con campos geoespaciales
- APIs REST (Django REST Framework) para operaciones espaciales
- Consultas geoespaciales optimizadas
- Serializadores GeoJSON
- Documentación de endpoints geográficos

---

## 🔄 Proceso

1. **Diseño de modelo de datos**: Definir campos geoespaciales (Point, LineString, Polygon, MultiPolygon).
2. **Configuración de PostGIS**: Verificar extensión PostGIS, SRID apropiado (usualmente 4326 WGS84).
3. **Implementación de modelos**: Crear modelos Django con GeoDjango fields.
4. **Implementación de APIs**: Endpoints CRUD + operaciones espaciales (intersección, distancia, within, contains).
5. **Optimización**: Crear índices espaciales (GiST), simplificar geometrías para visualización.
6. **Serialización**: GeoJSON para consumo frontend, formatos estándar OGC cuando aplique.
7. **Testing**: Tests con datos espaciales de prueba, verificar precisión de cálculos.
8. **Documentación**: Ejemplos de uso, SRID utilizado, limitaciones conocidas.

---

## 📋 Reglas y Constraints

- Usar SRID 4326 (WGS84) por defecto para datos geográficos.
- Crear índices espaciales GiST en todas las columnas geoespaciales.
- Validar geometrías antes de persistir (is_valid).
- No calcular distancias en coordenadas geográficas sin transformación apropiada.
- Limitar complejidad de geometrías en respuestas API (simplificación).
- Documentar precisión y unidades de medida (metros, grados).
- Considerar tiling para visualización de grandes volúmenes de datos.

---

## 🛠 Stack Tecnológico Relevante

- Python 3.11+
- Django 5+, GeoDjango
- PostGIS 3+
- Django REST Framework
- GeoJSON, WKT, WKB
- Leaflet / OpenLayers (frontend)
- GDAL, GEOS, PROJ

---

## 💡 Ejemplos de Uso

**Ejemplo 1 — API de zonas de servicio:**
> Modelo: ServiceZone (PolygonField)
> Endpoint: POST /api/zones/validate — verifica si un punto está dentro de alguna zona.
> Query: ServiceZone.objects.filter(geom__contains=point)

**Ejemplo 2 — API de rutas:**
> Modelo: Route (LineStringField)
> Endpoint: GET /api/routes/nearby?lat=40.4&lon=-3.7&radius=1000
> Query: Route.objects.filter(geom__distance_lte=(point, D(m=1000)))

---

## 🔗 Dependencias

- `apb-dev-implement-v1.0`
- `apb-sub-dev-django-v1.0`

---

## 📝 Notas

- GeoDjango requiere configuración específica de GDAL/GEOS en entornos de desarrollo.
- Para análisis espacial complejo, evaluar PostGIS directamente vs ORM.
- Considerar caché espacial (Redis) para consultas frecuentes.

---

*Skill generada por Arquitectura APB — APB AI Framework v1.0.0-draft*

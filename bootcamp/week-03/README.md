# 📍 Semana 03: Rutas, Parámetros y Query Strings

## 🎯 Objetivos de la Semana

Al finalizar esta semana, serás capaz de:

- ✅ Diseñar rutas RESTful siguiendo convenciones
- ✅ Trabajar con path parameters tipados
- ✅ Usar query parameters con valores por defecto
- ✅ Combinar múltiples fuentes de parámetros
- ✅ Implementar filtrado, ordenamiento y paginación

---

## 📚 Contenido

### 1. Teoría

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-rutas-basicas.md](1-teoria/01-rutas-basicas.md) | Rutas RESTful, métodos HTTP, diseño de URLs | 25 min |
| [02-path-parameters.md](1-teoria/02-path-parameters.md) | Parámetros de ruta, tipado, validación | 25 min |
| [03-query-parameters.md](1-teoria/03-query-parameters.md) | Query params, opcionales, múltiples valores | 25 min |
| [04-request-body.md](1-teoria/04-request-body.md) | Body + params, Form data, File uploads | 25 min |
| [05-parametros-avanzados.md](1-teoria/05-parametros-avanzados.md) | Header, Cookie, Depends para params | 20 min |

### 2. Prácticas

| Ejercicio | Descripción | Duración |
|-----------|-------------|----------|
| [ejercicio-01](2-practicas/01-ejercicio-rutas/) | Rutas CRUD básicas | 30 min |
| [ejercicio-02](2-practicas/02-ejercicio-path-params/) | Path parameters con validación | 35 min |
| [ejercicio-03](2-practicas/03-ejercicio-query-params/) | Filtrado y paginación | 40 min |
| [ejercicio-04](2-practicas/04-ejercicio-combinados/) | Parámetros combinados | 35 min |

### 3. Proyecto

[**API de Catálogo de Productos**](3-proyecto/)

API completa con:
- CRUD de productos y categorías
- Búsqueda y filtrado avanzado
- Paginación y ordenamiento
- Upload de imágenes

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| Teoría | 2 horas |
| Prácticas | 2.5 horas |
| Proyecto | 1.5 horas |
| **Total** | **6 horas** |

---

## 📋 Requisitos Previos

- ✅ Semana 01: Fundamentos de FastAPI
- ✅ Semana 02: Pydantic v2

---

## 🗂️ Estructura de la Semana

```
week-03/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
│   ├── 01-http-methods.svg
│   ├── 02-url-anatomy.svg
│   └── 03-params-flow.svg
├── 1-teoria/
│   ├── 01-rutas-basicas.md
│   ├── 02-path-parameters.md
│   ├── 03-query-parameters.md
│   ├── 04-request-body.md
│   └── 05-parametros-avanzados.md
├── 2-practicas/
│   ├── README.md
│   ├── 01-ejercicio-rutas/
│   ├── 02-ejercicio-path-params/
│   ├── 03-ejercicio-query-params/
│   └── 04-ejercicio-combinados/
├── 3-proyecto/
│   ├── README.md
│   ├── starter/
│   └── solution/
├── 4-recursos/
│   ├── README.md
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 📌 Entregable

**Proyecto: [Catálogo de Productos](3-proyecto/)**

API de catálogo de productos funcionando con:

- [ ] Path parameters con validación
- [ ] Query parameters para filtrado y paginación
- [ ] Combinación de parámetros en endpoints complejos
- [ ] Documentación Swagger completa

---

## 🔗 Navegación

[← Semana 02: Pydantic v2](../week-02/) | [Semana 04: Responses y Errores →](../week-04/)

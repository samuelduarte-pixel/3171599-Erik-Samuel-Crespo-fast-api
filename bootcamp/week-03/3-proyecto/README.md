# 🛒 Proyecto Semana 03: API de Catálogo con Búsqueda Avanzada

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.
> Consulta tu asignación en el registro de la ficha.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Entidad Catálogo | Categorías | Filtros Sugeridos |
|---------|-----------------|------------|-------------------|
| 🍝 **Restaurante** | Platillos | Entradas, Principales, Postres | price, vegetarian, spicy_level |
| 📚 **Biblioteca** | Libros | Ficción, No Ficción, Académico | author, year, available |
| 🏥 **Clínica Veterinaria** | Servicios | Consultas, Vacunas, Cirugías | species, duration, price |
| 💊 **Farmacia** | Medicamentos | Analgésicos, Antibióticos, Vitaminas | requires_prescription, price, stock |
| 🏋️ **Gimnasio** | Clases | Cardio, Fuerza, Flexibilidad | instructor, level, schedule |

---

## 📋 Descripción

Construirás una **API completa para gestionar un catálogo** de tu dominio con categorías, incluyendo búsqueda avanzada, filtrado, paginación y ordenamiento.

---

## 🎯 Objetivos

- ✅ Implementar CRUD completo de entidades y categorías
- ✅ Crear búsqueda y filtrado avanzado
- ✅ Implementar paginación con metadatos
- ✅ Aplicar ordenamiento flexible
- ✅ Combinar múltiples tipos de parámetros

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### 1. Categorías

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/categories` | Listar todas las categorías |
| GET | `/categories/{id}` | Obtener una categoría |
| POST | `/categories` | Crear categoría |
| PUT | `/categories/{id}` | Actualizar categoría |
| DELETE | `/categories/{id}` | Eliminar categoría |

### 2. Entidades del Catálogo

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/{entidades}` | Listar con filtros |
| GET | `/{entidades}/{id}` | Obtener una entidad |
| POST | `/{entidades}` | Crear entidad |
| PUT | `/{entidades}/{id}` | Actualizar entidad |
| PATCH | `/{entidades}/{id}` | Actualizar parcialmente |
| DELETE | `/{entidades}/{id}` | Eliminar entidad |

**Ejemplos de rutas:**
- Restaurante: `/dishes`, `/dishes/1`
- Biblioteca: `/books`, `/books/1`
- Gimnasio: `/classes`, `/classes/1`

### 3. Filtrado y Búsqueda (Diseña según tu dominio)

El endpoint GET debe soportar **mínimo 6 filtros**:

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `search` | string | Buscar en nombre y descripción |
| `category_id` | int | Filtrar por categoría |
| `min_{campo}` | number | Mínimo de campo numérico |
| `max_{campo}` | number | Máximo de campo numérico |
| `{booleano}` | bool | Filtro booleano del dominio |
| `tags` | list[str] | Filtrar por tags |

**Ejemplos por dominio:**
```bash
# Restaurante
GET /dishes?search=pasta&category_id=1&min_price=100&vegetarian=true

# Biblioteca
GET /books?search=python&category_id=2&available=true&min_year=2020

# Gimnasio
GET /classes?category_id=1&instructor=María&level=beginner
```

### 4. Paginación

| Parámetro | Default | Descripción |
|-----------|---------|-------------|
| `page` | 1 | Número de página |
| `per_page` | 10 | Items por página (máx 50) |

Respuesta paginada:
```json
{
  "items": [...],
  "total": 100,
  "page": 1,
  "per_page": 10,
  "pages": 10,
  "has_next": true,
  "has_prev": false
}
```

### 5. Ordenamiento

| Parámetro | Valores | Default |
|-----------|---------|---------|
| `sort_by` | name, {campo}, created_at | name |
| `order` | asc, desc | asc |

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py           # Punto de entrada
├── routers/
│   ├── __init__.py
│   ├── categories.py # Rutas de categorías
│   └── {entidad}.py  # Rutas de tu entidad
├── schemas.py        # Modelos Pydantic
├── database.py       # Base de datos simulada
├── dependencies.py   # Dependencias reutilizables
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| CRUD completo de categorías | 10 |
| CRUD completo de entidad | 15 |
| Filtrado con 6+ parámetros | 15 |
| **Adaptación al Dominio** (35%) | |
| Entidad coherente con dominio | 12 |
| Filtros específicos del negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Paginación con metadatos | 10 |
| Ordenamiento flexible | 8 |
| Código limpio y modular | 7 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

Este proyecto debe reflejar **tu dominio único asignado**:

- ❌ **No uses** "productos" genéricos
- ❌ **No copies** filtros de otros dominios
- ✅ **Diseña** categorías específicas de tu negocio
- ✅ **Implementa** filtros relevantes para tu contexto

> 💡 Dos proyectos con las mismas entidades/filtros serán evaluados como **copia**.

---

## 📚 Recursos

- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

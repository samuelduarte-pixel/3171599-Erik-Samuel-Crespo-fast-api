# 📦 Proyecto Semana 02: API CRUD con Validación Pydantic

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.
> Consulta tu asignación en el registro de la ficha.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Entidad Principal | Campos Sugeridos |
|---------|------------------|------------------|
| 🍝 **Restaurante** | Platillo | name, price, category, available, chef |
| 📚 **Biblioteca** | Libro | title, author, isbn, available, genre |
| 🏥 **Clínica Veterinaria** | Mascota | name, species, breed, owner_name, age |
| 💊 **Farmacia** | Medicamento | name, price, stock, requires_prescription |
| 🏋️ **Gimnasio** | Miembro | name, email, membership_type, start_date |

---

## 🎯 Objetivo

Construir una **API REST CRUD completa** para gestionar la entidad principal de tu dominio usando Pydantic v2 para validación de datos.

---

## 📋 Descripción

Crearás una API que permita:

- Crear entidades con validación estricta
- Listar entidades con paginación
- Buscar entidades por campo único
- Actualizar entidades parcialmente
- Eliminar entidades

---

## 🛠️ Requisitos Técnicos (Adapta a tu Dominio)

### Modelo de tu Entidad Principal

Diseña un modelo con **mínimo 8 campos** adaptado a tu dominio:

```python
# Ejemplo para Restaurante (Platillo)
Dish:
    id: int (autogenerado)
    name: str (2-100 caracteres)
    description: str | None
    price: float (mayor a 0)
    category: DishCategory (enum)
    is_available: bool (default: True)
    chef: str | None
    tags: list[str] (máximo 5 tags)
    created_at: datetime
    updated_at: datetime | None

# Ejemplo para Biblioteca (Libro)
Book:
    id: int (autogenerado)
    title: str (2-200 caracteres)
    author: str (2-100 caracteres)
    isbn: str (formato ISBN-13)
    genre: BookGenre (enum)
    is_available: bool (default: True)
    published_year: int (1450-actualidad)
    tags: list[str] (máximo 5 tags)
    created_at: datetime
    updated_at: datetime | None
```

### Schemas Requeridos

1. **{Entity}Base**: Campos comunes
2. **{Entity}Create**: Para POST (sin id, timestamps)
3. **{Entity}Update**: Para PATCH (todos opcionales)
4. **{Entity}Response**: Para respuestas (con id, timestamps)
5. **{Entity}List**: Lista paginada con total

### Endpoints (Adapta rutas a tu entidad)

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/{entidades}` | Crear entidad |
| GET | `/{entidades}` | Listar con paginación |
| GET | `/{entidades}/{id}` | Obtener por ID |
| GET | `/{entidades}/search/{campo}` | Buscar por campo único |
| PATCH | `/{entidades}/{id}` | Actualizar parcialmente |
| DELETE | `/{entidades}/{id}` | Eliminar |
| POST | `/{entidades}/{id}/toggle-status` | Cambiar estado |

**Ejemplos de rutas por dominio:**
- Restaurante: `/dishes`, `/dishes/1`, `/dishes/search/lasagna`
- Biblioteca: `/books`, `/books/1`, `/books/isbn/978-3-16-148410-0`
- Gimnasio: `/members`, `/members/1`, `/members/email/ana@gym.com`

---

## ✅ Criterios de Aceptación

### Validaciones Obligatorias (Adapta a tu dominio)

- [ ] Campo único debe validar duplicados (error 409)
- [ ] Campos numéricos con rangos apropiados
- [ ] Tags deben estar en minúsculas sin duplicados
- [ ] Strings deben normalizarse (strip, capitalize donde aplique)

### Validadores Requeridos

- [ ] `@field_validator` para normalizar campos de texto
- [ ] `@field_validator` para validar formato de campo único
- [ ] `@field_validator` para procesar tags
- [ ] `@model_validator` para validaciones cruzadas

### Response Models

- [ ] Usar `response_model` en todos los endpoints
- [ ] No exponer datos internos innecesarios
- [ ] Usar status codes apropiados (201, 204, 404, 409, 422)

---

## 📁 Estructura del Proyecto

```
starter/
├── main.py           # Aplicación FastAPI y endpoints
├── schemas.py        # Modelos Pydantic (TODO)
├── database.py       # Simulación de base de datos
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## 🚀 Cómo Empezar

### 1. Levantar el proyecto

```bash
cd starter
docker compose up --build
```

### 2. Acceder a la documentación

Visita http://localhost:8000/docs

### 3. Implementar schemas.py

Adapta los schemas a tu dominio:

1. Crear `{Entity}Base` con campos comunes
2. Crear `{Entity}Create` con validadores
3. Crear `{Entity}Update` con campos opcionales
4. Crear `{Entity}Response` con from_attributes
5. Crear `{Entity}List` para paginación

### 4. Probar los endpoints

Usa Swagger UI o curl para probar cada endpoint.

---

## 🧪 Casos de Prueba (Adapta a tu Dominio)

### Ejemplo: Restaurante - Crear Platillo

```bash
curl -X POST http://localhost:8000/dishes \
  -H "Content-Type: application/json" \
  -d '{
    "name": "  lasagna bolognesa  ",
    "description": "Clásica italiana",
    "price": 185.50,
    "category": "pasta",
    "chef": "Mario",
    "tags": ["Italian", "Popular", "italian"]
  }'
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "name": "Lasagna Bolognesa",
  "description": "Clásica italiana",
  "price": 185.50,
  "category": "pasta",
  "is_available": true,
  "chef": "Mario",
  "tags": ["italian", "popular"],
  "created_at": "2025-12-31T10:00:00",
  "updated_at": null
}
```

### Ejemplo: Biblioteca - Crear Libro

```bash
curl -X POST http://localhost:8000/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "  don quijote  ",
    "author": "miguel de cervantes",
    "isbn": "9783161484100",
    "genre": "classic",
    "published_year": 1605,
    "tags": ["Spanish", "Classic", "spanish"]
  }'
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Schemas correctamente definidos | 15 |
| Endpoints CRUD funcionando | 15 |
| Manejo de errores apropiado | 10 |
| **Adaptación al Dominio** (35%) | |
| Entidad coherente con dominio | 15 |
| Validaciones específicas del negocio | 10 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Validadores implementados | 10 |
| Response models aplicados | 8 |
| Código limpio | 7 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

Este proyecto debe reflejar **tu dominio único asignado**:

- ❌ **No copies** schemas de otros aprendices
- ❌ **No uses** entidades diferentes a tu dominio
- ✅ **Diseña** campos específicos para tu negocio
- ✅ **Implementa** validaciones relevantes

> 💡 Si dos proyectos tienen la misma entidad con los mismos campos, ambos serán evaluados como **copia**.

---

## 💡 Hints

1. **Normalizar strings**: Usa `.strip().title()` en validadores
2. **Tags únicos**: Usa `set()` para eliminar duplicados
3. **Campo único**: Revisa en la "base de datos" antes de crear/actualizar
4. **exclude_unset**: Usa `model_dump(exclude_unset=True)` para PATCH

---

## 📚 Recursos

- [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

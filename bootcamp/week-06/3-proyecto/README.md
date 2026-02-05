# 🏗️ Proyecto Semana 06: API con Service Layer y Relaciones N:M

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Entidad A | Entidad B | Relación N:M |
|---------|----------|----------|--------------|
| 🍝 **Restaurante** | Platillo | Ingrediente | Platillos tienen muchos ingredientes |
| 📚 **Biblioteca** | Libro | Categoría | Libros pertenecen a muchas categorías |
| 🏥 **Clínica Veterinaria** | Mascota | Servicio | Mascotas reciben muchos servicios |
| 💊 **Farmacia** | Medicamento | Proveedor | Medicamentos de muchos proveedores |
| 🏋️ **Gimnasio** | Miembro | Clase | Miembros asisten a muchas clases |

---

## 🎯 Objetivo

Construir una **API con arquitectura por capas** implementando:

- Service Layer para lógica de negocio
- Relaciones N:M con tabla intermedia
- Eager loading para optimización
- DTOs/Schemas separados por capa

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Entidades (Mínimo 3: 2 principales + tabla intermedia)

```python
# Ejemplo: Platillo-Ingrediente
{EntityA}:           # Platillo
    id, name, description, price, category
    ingredients: list[{EntityB}]  # Relación N:M

{EntityB}:           # Ingrediente  
    id, name, unit, cost_per_unit
    dishes: list[{EntityA}]  # Relación inversa

{EntityA}{EntityB}:  # Tabla intermedia (dish_ingredients)
    {entity_a}_id, {entity_b}_id
    quantity: float  # Campo extra en relación
```

### Arquitectura por Capas

```
Routers (Controllers) → Services → Repositories → Models
         ↓                  ↓             ↓
     Schemas           Business      SQLAlchemy
     (DTOs)             Logic         Queries
```

### Endpoints Requeridos

| Método | Endpoint | Service Method |
|--------|----------|----------------|
| GET | `/{entidades_a}` | `service.get_all()` |
| GET | `/{entidades_a}/{id}` | `service.get_by_id()` |
| POST | `/{entidades_a}` | `service.create()` |
| POST | `/{entidades_a}/{id}/{entidades_b}` | `service.add_relation()` |
| DELETE | `/{entidades_a}/{id}/{entidades_b}/{id_b}` | `service.remove_relation()` |

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── database.py
├── models/
│   ├── {entity_a}.py
│   ├── {entity_b}.py
│   └── associations.py   # Tabla N:M
├── schemas/
│   ├── {entity_a}.py
│   └── {entity_b}.py
├── services/             # ← Capa de negocio
│   ├── __init__.py
│   ├── {entity_a}_service.py
│   └── {entity_b}_service.py
├── routers/
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Relación N:M funcional | 15 |
| CRUD completo | 15 |
| Eager loading implementado | 10 |
| **Adaptación al Dominio** (35%) | |
| Entidades coherentes | 12 |
| Relación lógica para el negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Service Layer implementado | 12 |
| Separación de responsabilidades | 8 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** "Blog/Post/Tag" genéricos
- ✅ **Diseña** relaciones específicas de tu dominio
- ✅ **Implementa** lógica de negocio real

---

## 📚 Recursos

- [SQLAlchemy Many-to-Many](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2.5 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

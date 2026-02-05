# 📚 Proyecto Semana 05: API con SQLAlchemy ORM

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.
> Consulta tu asignación en el registro de la ficha.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Entidad Principal | Entidad Secundaria | Relación |
|---------|------------------|-------------------|----------|
| 🍝 **Restaurante** | Platillo | Chef | N:1 (muchos platillos por chef) |
| 📚 **Biblioteca** | Libro | Autor | N:1 (muchos libros por autor) |
| 🏥 **Clínica Veterinaria** | Mascota | Dueño | N:1 (muchas mascotas por dueño) |
| 💊 **Farmacia** | Medicamento | Laboratorio | N:1 (muchos medicamentos por lab) |
| 🏋️ **Gimnasio** | Clase | Instructor | N:1 (muchas clases por instructor) |

---

## 🎯 Objetivo

Construir una **API REST completa** usando SQLAlchemy ORM con SQLite, implementando relaciones 1:N entre dos entidades de tu dominio.

---

## 📋 Descripción

Crearás una API que:

- Gestione dos entidades relacionadas (1:N)
- Use SQLAlchemy para persistencia
- Implemente operaciones CRUD completas
- Maneje relaciones con eager/lazy loading
- Use Alembic para migraciones

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Entidades (Mínimo 2 relacionadas)

**Entidad Secundaria** (el "uno" de la relación):
```python
# Ejemplo: Chef, Autor, Dueño, Laboratorio, Instructor
{Secondary}:
    id: int (PK, auto)
    name: str (2-100)
    email: str (único)
    specialty: str | None
    is_active: bool (default: True)
    created_at: datetime
```

**Entidad Principal** (el "muchos" de la relación):
```python
# Ejemplo: Platillo, Libro, Mascota, Medicamento, Clase
{Primary}:
    id: int (PK, auto)
    name: str (2-200)
    description: str | None
    {secondary}_id: int (FK)
    status: {Status}Enum
    {campo_especifico}: tipo
    created_at: datetime
    updated_at: datetime | None
```

### Endpoints Requeridos

**Entidad Secundaria:**
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/{secundarios}` | Crear |
| GET | `/{secundarios}` | Listar con paginación |
| GET | `/{secundarios}/{id}` | Obtener con sus {primarios} |
| PATCH | `/{secundarios}/{id}` | Actualizar |
| DELETE | `/{secundarios}/{id}` | Eliminar (si no tiene dependencias) |

**Entidad Principal:**
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/{primarios}` | Crear (validar FK) |
| GET | `/{primarios}` | Listar (con filtro por {secundario}) |
| GET | `/{primarios}/{id}` | Obtener con {secundario} |
| PATCH | `/{primarios}/{id}` | Actualizar |
| DELETE | `/{primarios}/{id}` | Eliminar |

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── database.py       # Engine y sesión
├── models/
│   ├── __init__.py
│   ├── {secundario}.py
│   └── {primario}.py
├── schemas/
│   ├── __init__.py
│   ├── {secundario}.py
│   └── {primario}.py
├── routers/
│   ├── __init__.py
│   ├── {secundarios}.py
│   └── {primarios}.py
├── alembic/          # Migraciones
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| CRUD de ambas entidades | 15 |
| Relación 1:N funcional | 15 |
| Migraciones con Alembic | 10 |
| **Adaptación al Dominio** (35%) | |
| Entidades coherentes con dominio | 12 |
| Campos específicos del negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Modelos SQLAlchemy correctos | 10 |
| Schemas Pydantic separados | 8 |
| Código modular | 7 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** "Book/Author" genéricos
- ❌ **No copies** modelos de otros dominios
- ✅ **Diseña** entidades específicas de tu negocio
- ✅ **Implementa** campos y validaciones relevantes

> 💡 Dos proyectos con las mismas entidades serán evaluados como **copia**.

---

## 📚 Recursos

- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2.5 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

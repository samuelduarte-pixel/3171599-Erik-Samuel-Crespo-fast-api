# 🚀 Proyecto Semana 04: API con Responses y Manejo de Errores

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.
> Consulta tu asignación en el registro de la ficha.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Entidad Principal | Estados | Acciones Especiales |
|---------|------------------|---------|---------------------|
| 🍝 **Restaurante** | Orden | pending, preparing, ready, delivered | mark_preparing, mark_ready |
| 📚 **Biblioteca** | Préstamo | active, overdue, returned | extend, mark_returned |
| 🏥 **Clínica Veterinaria** | Cita | scheduled, in_progress, completed, cancelled | start, complete, cancel |
| 💊 **Farmacia** | Venta | pending, paid, delivered | process_payment, deliver |
| 🏋️ **Gimnasio** | Reservación | booked, confirmed, completed, no_show | confirm, check_in |

---

## 📋 Descripción

Construirás una **API REST completa** para gestionar una entidad de tu dominio aplicando todo lo aprendido sobre responses, status codes, manejo de errores y documentación OpenAPI.

---

## 🎯 Objetivos

Al completar este proyecto serás capaz de:

- ✅ Diseñar response models que protejan datos sensibles
- ✅ Usar status codes HTTP correctos para cada operación
- ✅ Implementar manejo de errores consistente y profesional
- ✅ Documentar APIs con OpenAPI de forma completa
- ✅ Crear una API lista para producción

---

## 📝 Requerimientos Funcionales (Adapta a tu Dominio)

### Entidad Principal

Diseña una entidad con **mínimo 10 campos** incluyendo estados y timestamps:

```python
# Ejemplo para Restaurante (Orden)
Order:
    id: int (auto-generado)
    table_number: int (1-50)
    customer_name: str (2-100 caracteres)
    items: list[OrderItem]
    status: OrderStatus (pending, preparing, ready, delivered)
    priority: Priority (low, normal, high)
    notes: str | None (máx 500)
    total: float (calculado)
    created_at: datetime
    updated_at: datetime | None
    completed_at: datetime | None

# Ejemplo para Biblioteca (Préstamo)
Loan:
    id: int (auto-generado)
    book_id: int
    member_id: int
    status: LoanStatus (active, overdue, returned)
    due_date: date
    return_date: date | None
    extensions: int (máx 2)
    fine_amount: float (calculado)
    created_at: datetime
    updated_at: datetime | None
```

### Endpoints Requeridos (Adapta rutas)

| Método | Endpoint | Descripción | Status Code |
|--------|----------|-------------|-------------|
| GET | `/{entidades}` | Listar con filtros | 200 |
| GET | `/{entidades}/{id}` | Obtener por ID | 200 / 404 |
| POST | `/{entidades}` | Crear nueva entidad | 201 |
| PUT | `/{entidades}/{id}` | Actualizar completa | 200 / 404 |
| PATCH | `/{entidades}/{id}/status` | Cambiar estado | 200 / 404 / 400 |
| DELETE | `/{entidades}/{id}` | Eliminar | 204 / 404 |
| GET | `/{entidades}/stats` | Estadísticas | 200 |

**Ejemplos de rutas por dominio:**
- Restaurante: `/orders`, `/orders/1/status`, `/orders/stats`
- Biblioteca: `/loans`, `/loans/1/status`, `/loans/stats`
- Gimnasio: `/reservations`, `/reservations/1/check-in`

### Filtros para Listado

- `status`: filtrar por estado
- `{campo_secundario}`: filtro específico de tu dominio
- `skip`: paginación (offset)
- `limit`: paginación (máximo 100)

---

## 🔒 Response Models

Debes crear schemas separados para:

1. **{Entity}Create**: Para crear (sin id, timestamps)
2. **{Entity}Update**: Para actualizar (todos opcionales)
3. **{Entity}Response**: Para respuestas (sin campos internos)
4. **{Entity}ListResponse**: Para listados con paginación
5. **{Entity}Stats**: Para estadísticas de tu dominio

---

## ⚠️ Manejo de Errores

Implementa errores consistentes con este formato:

```json
{
  "error": {
    "code": "ENTITY_NOT_FOUND",
    "message": "No se encontró la entidad con ID 123",
    "details": {"entity_id": 123}
  }
}
```

### Errores Requeridos (Adapta a tu dominio)

| Código | HTTP Status | Cuándo usarlo |
|--------|-------------|---------------|
| `{ENTITY}_NOT_FOUND` | 404 | Entidad no existe |
| `INVALID_STATUS_TRANSITION` | 400 | Cambio de estado inválido |
| `{ENTITY}_ALREADY_EXISTS` | 409 | Duplicado |
| `VALIDATION_ERROR` | 422 | Datos inválidos |

---

## 🏗️ Estructura del Proyecto

```
starter/
├── main.py            # Archivo principal
├── models.py          # Schemas Pydantic
├── database.py        # Simulación de DB
├── exceptions.py      # Excepciones personalizadas
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Endpoints CRUD completos | 15 |
| Transiciones de estado | 10 |
| Estadísticas funcionando | 8 |
| Status codes correctos | 7 |
| **Adaptación al Dominio** (35%) | |
| Entidad coherente con dominio | 12 |
| Estados y transiciones lógicas | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Response models correctos | 10 |
| Manejo de errores consistente | 10 |
| Documentación OpenAPI | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

Este proyecto debe reflejar **tu dominio único asignado**:

- ❌ **No uses** "Task" o "Tarea" genérica
- ❌ **No copies** estados de otros dominios
- ✅ **Diseña** estados lógicos para tu negocio
- ✅ **Implementa** transiciones válidas

> 💡 Si dos proyectos tienen las mismas entidades/estados, ambos serán evaluados como **copia**.

---

## 📚 Recursos

- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

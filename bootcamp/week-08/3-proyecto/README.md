# 🏗️ Proyecto Semana 08: API con Arquitectura MVC/Capas

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Módulos | DTOs |
|---------|---------|------|
| 🍝 **Restaurante** | orders, menu, tables | OrderDTO, DishDTO |
| 📚 **Biblioteca** | catalog, loans, members | BookDTO, LoanDTO |
| 🏥 **Clínica Veterinaria** | patients, appointments, treatments | PetDTO, AppointmentDTO |
| 💊 **Farmacia** | inventory, sales, prescriptions | MedicineDTO, SaleDTO |
| 🏋️ **Gimnasio** | members, classes, attendance | MemberDTO, ClassDTO |

---

## 🎯 Objetivo

Implementar una **arquitectura MVC/Capas completa** con:

- Controllers/Routers separados
- Services con lógica de negocio
- Repositories para acceso a datos
- DTOs para transferencia de datos
- Mappers para conversiones
- Exception Handlers globales

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Arquitectura Completa

```
┌─────────────────────────────────────────┐
│              Presentation               │
│  (Routers + Schemas de Request/Response)│
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│              Application                │
│     (Services + DTOs + Mappers)         │
└────────────────────┬────────────────────┘
                     ▼
┌─────────────────────────────────────────┐
│             Infrastructure              │
│    (Repositories + ORM Models)          │
└─────────────────────────────────────────┘
```

### DTOs y Mappers

```python
# DTO interno (Application layer)
@dataclass
class {Entity}DTO:
    id: int
    name: str
    # Campos específicos del dominio

# Mapper
class {Entity}Mapper:
    @staticmethod
    def to_dto(model: {Entity}Model) -> {Entity}DTO: ...
    
    @staticmethod
    def to_model(dto: {Entity}DTO) -> {Entity}Model: ...
```

### Exception Handlers

```python
@app.exception_handler({Domain}Error)
async def handle_{domain}_error(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.code, "message": exc.message}
    )
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── presentation/
│   ├── routers/
│   └── schemas/
├── application/
│   ├── services/
│   ├── dtos/
│   └── mappers/
├── infrastructure/
│   ├── models/
│   └── repositories/
├── core/
│   ├── exceptions.py
│   └── config.py
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| CRUD completo funcionando | 15 |
| Separación de capas correcta | 15 |
| Exception handlers globales | 10 |
| **Adaptación al Dominio** (35%) | |
| DTOs específicos del dominio | 12 |
| Lógica de negocio coherente | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Mappers implementados | 8 |
| Arquitectura limpia | 10 |
| Código modular | 7 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** "E-Commerce/Product/Cart" genéricos
- ✅ **Diseña** DTOs específicos de tu dominio
- ✅ **Implementa** mappers y servicios reales

---

## 📚 Recursos

- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2.5 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

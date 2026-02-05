# 🏛️ Proyecto Semana 07: API con Repository Pattern

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Repositorios | Unit of Work |
|---------|-------------|--------------|
| 🍝 **Restaurante** | DishRepository, OrderRepository | OrderUoW (order + items) |
| 📚 **Biblioteca** | BookRepository, LoanRepository | LoanUoW (loan + book status) |
| 🏥 **Clínica Veterinaria** | PetRepository, AppointmentRepository | AppointmentUoW |
| 💊 **Farmacia** | MedicineRepository, SaleRepository | SaleUoW (sale + stock) |
| 🏋️ **Gimnasio** | MemberRepository, AttendanceRepository | AttendanceUoW |

---

## 🎯 Objetivo

Implementar el **Repository Pattern** y **Unit of Work** para:

- Abstraer el acceso a datos
- Facilitar testing con fakes/mocks
- Aplicar inversión de dependencias
- Manejar transacciones atómicas

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Interfaces de Repositorio

```python
# Ejemplo genérico
class I{Entity}Repository(Protocol):
    def get_by_id(self, id: int) -> {Entity} | None: ...
    def get_all(self, filters: {Filter}Params) -> list[{Entity}]: ...
    def add(self, entity: {Entity}) -> {Entity}: ...
    def update(self, entity: {Entity}) -> {Entity}: ...
    def delete(self, id: int) -> bool: ...
```

### Unit of Work

```python
class I{Domain}UnitOfWork(Protocol):
    {entities}: I{Entity}Repository
    {related}: I{Related}Repository
    
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
```

### Implementaciones

1. **SQLAlchemy Repository**: Para producción
2. **Fake Repository**: Para testing (in-memory)

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── domain/
│   ├── entities/         # Entidades de dominio
│   └── interfaces/       # Interfaces/Protocols
├── infrastructure/
│   ├── repositories/     # Implementaciones SQLAlchemy
│   └── unit_of_work.py
├── application/
│   └── services/         # Casos de uso
├── tests/
│   ├── fakes/            # Fake repositories
│   └── test_services.py
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Repositories implementados | 15 |
| Unit of Work funcional | 15 |
| Tests con fakes | 10 |
| **Adaptación al Dominio** (35%) | |
| Entidades coherentes | 12 |
| Operaciones específicas del negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Interfaces bien definidas | 10 |
| Inversión de dependencias | 10 |
| Código testeable | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** "Task/TaskRepository" genéricos
- ✅ **Diseña** repositorios específicos de tu dominio
- ✅ **Implementa** operaciones de negocio reales

---

## 📚 Recursos

- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)
- [Unit of Work](https://martinfowler.com/eaaCatalog/unitOfWork.html)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2.5 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

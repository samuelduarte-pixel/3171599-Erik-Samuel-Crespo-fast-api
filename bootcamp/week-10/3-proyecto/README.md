# 🔷 Proyecto Semana 10: API con Arquitectura Hexagonal Completa

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Aggregate Root | Value Objects | Domain Events |
|---------|---------------|---------------|---------------|
| 🍝 **Restaurante** | Order | Money, TableNumber | OrderPlaced, OrderCompleted |
| 📚 **Biblioteca** | Loan | ISBN, MemberID | BookBorrowed, BookReturned |
| 🏥 **Clínica Veterinaria** | Appointment | PetID, TimeSlot | AppointmentScheduled |
| 💊 **Farmacia** | Sale | PrescriptionCode | SaleCompleted, StockUpdated |
| 🏋️ **Gimnasio** | Membership | MemberID, PlanType | MembershipActivated |

---

## 🎯 Objetivo

Implementar una **Arquitectura Hexagonal completa** con:

- Domain Layer (Entities, Value Objects, Domain Events)
- Application Layer (Use Cases, DTOs)
- Infrastructure Layer (Repositories, Adapters)

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Capas de la Arquitectura

```
┌────────────────────────────────────────────┐
│              INFRASTRUCTURE                │
│  (FastAPI, SQLAlchemy, External Services)  │
└─────────────────────┬──────────────────────┘
                      │ depends on
┌─────────────────────▼──────────────────────┐
│               APPLICATION                  │
│     (Use Cases, DTOs, Ports/Interfaces)    │
└─────────────────────┬──────────────────────┘
                      │ depends on
┌─────────────────────▼──────────────────────┐
│                 DOMAIN                     │
│ (Entities, Value Objects, Domain Events)   │
└────────────────────────────────────────────┘
```

### Domain Layer

```python
# Aggregate Root
class {Entity}(AggregateRoot):
    id: {Entity}Id
    # Value Objects como atributos
    
    def {action}(self, ...) -> None:
        # Lógica de negocio
        self._raise_event({DomainEvent}(...))

# Value Object
@dataclass(frozen=True)
class {ValueObject}:
    value: ...
    
    def __post_init__(self):
        # Validaciones
```

### Application Layer (Use Cases)

```python
class {Action}{Entity}UseCase:
    def __init__(self, repository: I{Entity}Repository):
        self._repository = repository
    
    async def execute(self, command: {Command}) -> {Result}:
        # Orquestar lógica
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── domain/
│   ├── entities/
│   ├── value_objects/
│   ├── events/
│   └── exceptions.py
├── application/
│   ├── use_cases/
│   ├── dtos/
│   └── ports/
├── infrastructure/
│   ├── api/
│   ├── persistence/
│   └── adapters/
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Domain Layer completo | 15 |
| Use Cases implementados | 15 |
| Infrastructure funcional | 10 |
| **Adaptación al Dominio** (35%) | |
| Aggregate Root coherente | 12 |
| Value Objects del negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Separación de capas | 10 |
| Domain Events implementados | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** "Task/TaskManagement" genéricos
- ✅ **Diseña** un Aggregate Root de tu dominio
- ✅ **Implementa** Value Objects específicos

---

## 📚 Recursos

- [Domain-Driven Design](https://martinfowler.com/tags/domain%20driven%20design.html)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

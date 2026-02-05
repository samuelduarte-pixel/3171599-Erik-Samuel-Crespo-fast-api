# 🏆 Proyecto Semana 16: API Completa Lista para Producción

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Este proyecto final integra TODO lo aprendido en 16 semanas aplicado a tu dominio único.

### 💡 Ejemplos de Proyecto Final por Dominio

| Dominio | Entidades (4+) | Features Clave |
|---------|---------------|----------------|
| 🍝 **Restaurante** | Menu, Dish, Order, Table, Chef | Pedidos en tiempo real, RBAC (chef/waiter/manager) |
| 📚 **Biblioteca** | Book, Member, Loan, Reservation, Author | Préstamos con vencimiento, notificaciones |
| 🏥 **Clínica Veterinaria** | Pet, Owner, Vet, Appointment, MedicalRecord | Historial médico, agenda por veterinario |
| 💊 **Farmacia** | Medicine, Prescription, Sale, Supplier, Stock | Control de inventario, recetas validadas |
| 🏋️ **Gimnasio** | Member, Class, Trainer, Membership, Attendance | Reservas de clases, seguimiento de asistencia |

---

## 🎯 Objetivo

Construir una **API RESTful completa** que demuestre dominio de:

- Arquitectura limpia (Domain → Application → Infrastructure)
- Autenticación JWT + RBAC
- Testing con >50% cobertura
- Docker + CI/CD
- Documentación OpenAPI

---

## 📦 Requisitos Obligatorios (Adapta a tu Dominio)

### Arquitectura

```
src/
├── domain/
│   ├── entities/         # Entidades del dominio
│   ├── value_objects/    # VOs específicos
│   └── exceptions.py
├── application/
│   ├── use_cases/        # Casos de uso
│   ├── dtos/
│   └── ports/            # Interfaces
├── infrastructure/
│   ├── api/              # FastAPI routers
│   ├── persistence/      # SQLAlchemy repos
│   └── auth/             # JWT, OAuth2
└── main.py
```

### Entidades Mínimas (4+)

```python
# Ejemplo para Restaurante
class Dish(Entity):      # Entidad principal
class Order(AggregateRoot):  # Aggregate con lógica
class Table(Entity):     # Entidad secundaria
class Chef(Entity):      # Usuario con rol

# Ejemplo para Biblioteca
class Book(Entity):
class Loan(AggregateRoot):
class Member(Entity):
class Author(Entity):
```

### Autenticación y RBAC

- Registro y login con JWT
- Access + Refresh tokens
- Mínimo 3 roles específicos del dominio
- Protección de endpoints por rol

### Testing

- Unit tests para servicios/use cases
- Integration tests para endpoints
- Cobertura mínima: **50%**

### DevOps

- Dockerfile multi-stage
- docker-compose.yml funcional
- GitHub Actions CI pipeline

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (35%) | |
| CRUD completo 4+ entidades | 15 |
| JWT + RBAC funcional | 12 |
| Testing >50% coverage | 8 |
| **Adaptación al Dominio** (35%) | |
| Entidades coherentes con negocio | 12 |
| Lógica de dominio significativa | 13 |
| Originalidad total (no copia) | 10 |
| **Arquitectura y Código** (20%) | |
| Arquitectura limpia | 10 |
| Código limpio y documentado | 10 |
| **DevOps** (10%) | |
| Docker funcional | 5 |
| CI/CD pasando | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

> **ATENCIÓN**: Este es el proyecto final. La originalidad es CRÍTICA.

- ❌ **Copia detectada = Reprobación automática**
- ❌ **No uses** Task Manager, Blog, E-commerce genéricos
- ✅ **Implementa** tu dominio asignado completamente
- ✅ **Demuestra** comprensión, no solo código funcional

### Verificación de Originalidad

El instructor verificará:
1. Coherencia entre dominio y entidades
2. Lógica de negocio específica
3. Nombres y terminología del dominio
4. Commits incrementales (no un solo commit final)

---

## 📚 Recursos

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)
- [Política Anticopia](../../../_instructor-only/POLITICA-ANTICOPIA-FASTAPI.md)

---

## 📅 Entrega

- **Fecha límite**: Última sesión de la semana 16
- **Formato**: Repositorio GitHub con README completo
- **Demo**: Presentación de 10 minutos

---

**Tiempo estimado:** 6-8 horas

[← Volver a Semana 16](../)

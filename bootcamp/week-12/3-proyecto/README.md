# 🧪 Proyecto Semana 12: Test Suite Completo con pytest

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Entidad a Testear | Edge Cases | Validaciones |
|---------|------------------|------------|--------------|
| 🍝 **Restaurante** | Order | Empty cart, Invalid table | Price > 0, Quantity > 0 |
| 📚 **Biblioteca** | Loan | Expired loan, Max loans | Valid ISBN, Member active |
| 🏥 **Clínica Veterinaria** | Appointment | Past date, Overlapping | Valid pet_id, Vet available |
| 💊 **Farmacia** | Sale | Invalid prescription | Stock available, Valid dose |
| 🏋️ **Gimnasio** | Membership | Expired plan, Frozen | Valid dates, Plan exists |

---

## 🎯 Objetivo

Implementar **testing completo** para tu API:

- Unit tests (services, utilities)
- Integration tests (endpoints)
- Fixtures y factories
- Cobertura mínima 80%

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Estructura de Tests

```
tests/
├── conftest.py              # Fixtures globales
├── factories.py             # Factories para test data
├── unit/
│   ├── test_services.py     # Tests de lógica de negocio
│   └── test_validators.py   # Tests de validaciones
└── integration/
    ├── test_auth.py         # Tests de autenticación
    └── test_{entities}.py   # Tests de endpoints CRUD
```

### Fixtures

```python
# conftest.py
@pytest.fixture
def {entity}_factory():
    def create_{entity}(**kwargs):
        defaults = {
            # Valores por defecto del dominio
        }
        defaults.update(kwargs)
        return {Entity}Create(**defaults)
    return create_{entity}

@pytest.fixture
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
```

### Tests por Tipo

```python
# Unit Test
def test_{entity}_validation():
    # Probar validaciones Pydantic del dominio
    with pytest.raises(ValidationError):
        {Entity}Create(invalid_field="bad_value")

# Integration Test
@pytest.mark.asyncio
async def test_create_{entity}(test_client, {entity}_factory):
    data = {entity}_factory().model_dump()
    response = await test_client.post("/{entities}/", json=data)
    assert response.status_code == 201
```

### Cobertura Mínima

| Componente | Cobertura Requerida |
|------------|---------------------|
| Services | 90% |
| Routers | 80% |
| Models | 70% |
| **Total** | **80%** |

---

## 🗂️ Estructura del Proyecto

```
starter/
├── src/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── routers/
├── tests/
│   ├── conftest.py
│   ├── factories.py
│   ├── unit/
│   └── integration/
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Unit tests completos | 15 |
| Integration tests completos | 15 |
| Cobertura >= 80% | 10 |
| **Adaptación al Dominio** (35%) | |
| Factories coherentes | 12 |
| Edge cases del dominio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Fixtures bien estructuradas | 10 |
| Tests aislados e independientes | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** tests genéricos sin contexto
- ✅ **Diseña** casos de prueba específicos
- ✅ **Implementa** edge cases de tu dominio

---

## 📚 Recursos

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

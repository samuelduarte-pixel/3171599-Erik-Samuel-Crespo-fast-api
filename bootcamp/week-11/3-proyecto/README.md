# 🔐 Proyecto Semana 11: API con Autenticación JWT y RBAC

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Roles | Recursos Protegidos | Permisos Especiales |
|---------|-------|---------------------|---------------------|
| 🍝 **Restaurante** | chef, waiter, manager | Menu, Orders | chef: update_dishes |
| 📚 **Biblioteca** | librarian, member, admin | Books, Loans | librarian: manage_loans |
| 🏥 **Clínica Veterinaria** | vet, receptionist, owner | Pets, Appointments | vet: view_medical_records |
| 💊 **Farmacia** | pharmacist, cashier, admin | Medicines, Prescriptions | pharmacist: validate_prescription |
| 🏋️ **Gimnasio** | trainer, member, admin | Classes, Memberships | trainer: assign_routines |

---

## 🎯 Objetivo

Implementar **autenticación y autorización completa**:

- JWT (Access + Refresh tokens)
- OAuth2 Password Flow
- RBAC (Role-Based Access Control)
- Protección de endpoints por rol

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Autenticación

```python
# Registro de usuarios
@app.post("/{domain}/auth/register")
async def register(user: UserCreate) -> UserResponse:
    # Crear usuario con rol por defecto
    ...

# Login con JWT
@app.post("/{domain}/auth/login")
async def login(form: OAuth2PasswordRequestForm) -> Token:
    # Retornar access_token + refresh_token
    ...
```

### Autorización (RBAC)

```python
# Dependencia de rol
def require_role(*roles: str):
    async def role_checker(user: User = Depends(get_current_user)):
        if user.role not in roles:
            raise HTTPException(403, "Insufficient permissions")
        return user
    return role_checker

# Endpoint protegido
@app.delete("/{entities}/{{id}}", dependencies=[Depends(require_role("admin"))])
async def delete_{entity}(id: int):
    # Solo admin puede eliminar
    ...
```

### Roles Mínimos (3 roles)

1. **user** - Acceso básico (lectura propia)
2. **staff** - Gestión de recursos del dominio  
3. **admin** - Control total

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── auth/
│   ├── jwt.py           # Token generation/validation
│   ├── oauth2.py        # OAuth2 password flow
│   ├── dependencies.py  # get_current_user, require_role
│   └── password.py      # Hashing (bcrypt)
├── models/
│   ├── user.py          # User + Role models
│   └── {entity}.py      # Domain entity
├── schemas/
│   ├── auth.py          # Token, UserCreate, etc.
│   └── {entity}.py
├── routers/
│   ├── auth.py
│   └── {entities}.py
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| JWT funcional (access + refresh) | 15 |
| RBAC implementado (3+ roles) | 15 |
| Endpoints protegidos correctamente | 10 |
| **Adaptación al Dominio** (35%) | |
| Roles coherentes con el dominio | 12 |
| Permisos específicos del negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Dependencias bien estructuradas | 10 |
| Manejo seguro de contraseñas | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** roles genéricos sin contexto
- ✅ **Diseña** roles específicos de tu dominio
- ✅ **Protege** recursos según la lógica de negocio

---

## 📚 Recursos

- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [JWT.io](https://jwt.io/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

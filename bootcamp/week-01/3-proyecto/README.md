# 🎯 Proyecto Semana 01: API Básica de tu Dominio

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.
> Consulta tu asignación en el registro de la ficha.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Entidad Principal | Endpoint de Bienvenida | Endpoint de Info |
|---------|------------------|------------------------|------------------|
| 🍝 **Restaurante** | Platillo | `GET /cliente/{nombre}` | `GET /platillo/{nombre}/info` |
| 📚 **Biblioteca** | Libro | `GET /lector/{nombre}` | `GET /libro/{titulo}/info` |
| 🏥 **Clínica Veterinaria** | Mascota | `GET /cliente/{nombre}` | `GET /mascota/{nombre}/info` |
| 💊 **Farmacia** | Medicamento | `GET /cliente/{nombre}` | `GET /medicamento/{nombre}/info` |
| 🏋️ **Gimnasio** | Miembro | `GET /miembro/{nombre}` | `GET /clase/{nombre}/info` |

---

## 📋 Descripción

En este proyecto integrador, crearás una **API básica** para tu dominio asignado que aplica todos los conceptos aprendidos en la semana:

- Configuración de Docker
- Type hints en Python
- Programación asíncrona
- Endpoints FastAPI con parámetros

---

## 🎯 Objetivos

Al completar este proyecto, habrás demostrado que puedes:

- ✅ Configurar un proyecto FastAPI con Docker
- ✅ Usar type hints correctamente
- ✅ Crear endpoints con path y query parameters
- ✅ Adaptar conceptos genéricos a tu dominio específico
- ✅ Documentar tu API

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### RF-01: Endpoint de Información de la API
- **Ruta**: `GET /`
- **Descripción**: Retorna información de tu API adaptada al dominio
- **Respuesta**: `{"name": "[Tu Dominio] API", "version": "1.0.0", "domain": "[tu-dominio]"}`

**Ejemplos por dominio:**
```json
// Restaurante
{"name": "Restaurante Italiano API", "version": "1.0.0", "domain": "restaurante"}

// Biblioteca
{"name": "Biblioteca Municipal API", "version": "1.0.0", "domain": "biblioteca"}

// Gimnasio
{"name": "FitGym API", "version": "1.0.0", "domain": "gimnasio"}
```

### RF-02: Bienvenida Personalizada
- **Ruta**: `GET /{entidad}/{nombre}`
- **Descripción**: Mensaje de bienvenida personalizado para tu dominio
- **Parámetros**: 
  - `nombre` (path): Nombre de la persona/entidad
  - `language` (query, default="es"): Idioma del mensaje (es, en, fr)

**Ejemplos por dominio:**
```bash
# Restaurante
GET /cliente/Carlos?language=es
→ {"message": "¡Bienvenido a nuestro restaurante, Carlos!"}

# Biblioteca  
GET /lector/Ana?language=en
→ {"message": "Welcome to the library, Ana!"}

# Gimnasio
GET /miembro/Pedro?language=es
→ {"message": "¡Bienvenido al gimnasio, Pedro!"}
```

### RF-03: Información de Entidad
- **Ruta**: `GET /{entidad}/{nombre}/info`
- **Descripción**: Información detallada de una entidad de tu dominio
- **Parámetros**:
  - `nombre` (path): Nombre/identificador
  - `detail_level` (query, default="basic"): Nivel de detalle (basic, full)

**Ejemplos por dominio:**
```bash
# Restaurante - información de platillo
GET /platillo/lasagna/info?detail_level=full
→ {"name": "Lasagna", "category": "pasta", "price": 180.00}

# Biblioteca - información de libro
GET /libro/quijote/info?detail_level=basic
→ {"title": "Don Quijote", "available": true}

# Gimnasio - información de clase
GET /clase/yoga/info?detail_level=full
→ {"name": "Yoga", "instructor": "María", "capacity": 20}
```

### RF-04: Servicio/Acción según Horario
- **Ruta**: `GET /servicio/horario`
- **Descripción**: Respuesta diferente según la hora del día
- **Parámetros**:
  - `hour` (query): Hora del día (0-23)
- **Lógica horaria**: Adapta a tu dominio
  - 6-11: Mensaje de mañana
  - 12-17: Mensaje de tarde
  - 18-23 o 0-5: Mensaje de noche

**Ejemplos por dominio:**
```bash
# Restaurante
GET /servicio/horario?hour=8
→ {"message": "Servimos desayuno", "available": ["huevos", "café"]}

# Biblioteca
GET /servicio/horario?hour=10
→ {"message": "Horario matutino - Sala de lectura abierta"}

# Gimnasio
GET /servicio/horario?hour=7
→ {"message": "Clases matutinas", "classes": ["yoga", "spinning"]}
```

### RF-05: Health Check
- **Ruta**: `GET /health`
- **Descripción**: Estado de la API
- **Respuesta**: `{"status": "healthy", "domain": "[tu-dominio]"}`

---

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md              # Este archivo
├── starter/               # Código inicial
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── pyproject.toml
│   └── src/
│       └── main.py        # Implementar aquí
└── solution/              # ⚠️ Solo instructores
    └── ...
```

---

## 📝 Instrucciones

### 1. Configurar el Proyecto

```bash
cd bootcamp/week-01/3-proyecto/starter
```

### 2. Implementar la API (Adaptar a tu dominio)

Abre `src/main.py` y completa los TODOs adaptándolos a tu dominio:

1. **TODO 1**: Crear FastAPI con nombre de tu dominio
2. **TODO 2**: Implementar endpoint raíz
3. **TODO 3**: Implementar bienvenida personalizada
4. **TODO 4**: Implementar información de entidad
5. **TODO 5**: Implementar servicio según horario
6. **TODO 6**: Implementar health check

### 3. Ejecutar y Probar

```bash
docker compose up --build

# Probar (adapta las URLs a tu dominio)
curl http://localhost:8000/
curl http://localhost:8000/health
```

### 4. Verificar Documentación

Visita `http://localhost:8000/docs`

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Endpoint raíz funciona | 8 |
| Bienvenida personalizada con idiomas | 10 |
| Información de entidad con niveles | 10 |
| Servicio según horario | 12 |
| **Adaptación al Dominio** (35%) | |
| Coherencia con dominio asignado | 15 |
| Entidades correctamente modeladas | 10 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Type hints correctos | 8 |
| Documentación en `/docs` | 10 |
| Código limpio y comentado | 7 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

Este proyecto debe reflejar **tu dominio único asignado**:

- ❌ **No copies** el código de otros aprendices
- ❌ **No uses** un dominio diferente al asignado
- ✅ **Adapta** todos los conceptos a tu contexto
- ✅ **Personaliza** mensajes, entidades y lógica

> 💡 Si dos proyectos tienen código idéntico, ambos serán evaluados como **copia**.

---

## 📚 Recursos

- [Teoría: Introducción a FastAPI](../1-teoria/05-intro-fastapi.md)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

**Tiempo estimado:** 1.5-2 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

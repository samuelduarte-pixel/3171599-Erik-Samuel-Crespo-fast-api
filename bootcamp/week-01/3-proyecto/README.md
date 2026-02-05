# 🎯 Proyecto Semana 01: API de Saludo

## 📋 Descripción

En este proyecto integrador, crearás una **API de Saludo** completa que aplica todos los conceptos aprendidos en la semana:

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
- ✅ Implementar lógica de negocio básica
- ✅ Documentar tu API

---

## 📦 Requisitos Funcionales

### RF-01: Endpoint de Saludo Básico
- **Ruta**: `GET /`
- **Descripción**: Retorna información de la API
- **Respuesta**: `{"name": "Greeting API", "version": "1.0.0"}`

### RF-02: Saludo Personalizado
- **Ruta**: `GET /greet/{name}`
- **Descripción**: Saluda a una persona por su nombre
- **Parámetros**: 
  - `name` (path): Nombre de la persona
  - `language` (query, default="es"): Idioma del saludo (es, en, fr)
- **Ejemplo**: `GET /greet/Carlos?language=en` → `{"greeting": "Hello, Carlos!"}`

### RF-03: Saludo Formal
- **Ruta**: `GET /greet/{name}/formal`
- **Descripción**: Saludo formal con título
- **Parámetros**:
  - `name` (path): Nombre
  - `title` (query, default="Sr./Sra."): Título (Dr., Ing., Prof., etc.)
- **Ejemplo**: `GET /greet/García/formal?title=Dr.` → `{"greeting": "Estimado/a Dr. García"}`

### RF-04: Saludos por Hora del Día
- **Ruta**: `GET /greet/{name}/time-based`
- **Descripción**: Saludo según la hora del día
- **Parámetros**:
  - `name` (path): Nombre
  - `hour` (query): Hora del día (0-23)
- **Lógica**:
  - 5-11: "Buenos días"
  - 12-17: "Buenas tardes"
  - 18-23 o 0-4: "Buenas noches"

### RF-05: Health Check
- **Ruta**: `GET /health`
- **Descripción**: Estado de la API
- **Respuesta**: `{"status": "healthy"}`

---

## 🏗️ Estructura del Proyecto

```
3-proyecto/
├── README.md              # Este archivo
├── starter/               # Código inicial (para el estudiante)
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── pyproject.toml
│   └── src/
│       └── main.py        # Implementar aquí
└── solution/              # ⚠️ Solo instructores (no en repo)
    └── ...
```

---

## 📝 Instrucciones

### 1. Configurar el Proyecto

```bash
cd bootcamp/week-01/3-proyecto/starter
```

Revisa los archivos de configuración:
- `Dockerfile` - Ya configurado
- `docker-compose.yml` - Ya configurado
- `pyproject.toml` - Ya configurado

### 2. Implementar la API

Abre `src/main.py` y completa los TODOs:

1. **TODO 1**: Crear la instancia de FastAPI
2. **TODO 2**: Implementar el endpoint raíz
3. **TODO 3**: Implementar saludo personalizado
4. **TODO 4**: Implementar saludo formal
5. **TODO 5**: Implementar saludo por hora
6. **TODO 6**: Implementar health check

### 3. Ejecutar y Probar

```bash
# Construir y ejecutar
docker compose up --build

# En otra terminal, probar endpoints
curl http://localhost:8000/
curl http://localhost:8000/greet/Carlos
curl http://localhost:8000/greet/Carlos?language=en
curl http://localhost:8000/greet/García/formal?title=Dr.
curl http://localhost:8000/greet/Ana/time-based?hour=10
curl http://localhost:8000/health
```

### 4. Verificar Documentación

Visita `http://localhost:8000/docs` y verifica que:
- Todos los endpoints aparecen documentados
- Los parámetros tienen descripciones claras
- Los ejemplos funcionan correctamente

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Endpoint raíz funciona | 10 |
| Saludo personalizado con idiomas | 20 |
| Saludo formal con títulos | 20 |
| Saludo por hora del día | 25 |
| Health check | 10 |
| Documentación completa en `/docs` | 15 |
| **Total** | **100** |

### Niveles de Logro

- **🥉 Básico (60-69)**: Endpoints funcionan pero sin validación
- **🥈 Competente (70-84)**: Todos los endpoints con type hints
- **🥇 Destacado (85-100)**: Código limpio, documentado y con casos edge

---

## 💡 Pistas

### Diccionario de Saludos por Idioma

```python
GREETINGS = {
    "es": "¡Hola, {name}!",
    "en": "Hello, {name}!",
    "fr": "Bonjour, {name}!",
    "de": "Hallo, {name}!",
    "it": "Ciao, {name}!",
}
```

### Lógica de Hora del Día

```python
def get_time_greeting(hour: int) -> str:
    if 5 <= hour < 12:
        return "Buenos días"
    elif 12 <= hour < 18:
        return "Buenas tardes"
    else:
        return "Buenas noches"
```

---

## 📚 Recursos de Apoyo

- [Teoría: Introducción a FastAPI](../1-teoria/05-intro-fastapi.md)
- [Ejercicio 04: Primera API](../2-practicas/04-ejercicio-primera-api/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

## 🚀 ¡Manos a la Obra!

1. Abre `starter/src/main.py`
2. Lee cada TODO cuidadosamente
3. Implementa paso a paso
4. Prueba cada endpoint antes de continuar
5. ¡No olvides la documentación!

**Tiempo estimado:** 1.5-2 horas

---

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

# 🚀 Proyecto Semana 15: API Production-Ready con Docker y CI/CD

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Servicios Docker | Variables de Entorno | Health Endpoints |
|---------|-----------------|---------------------|------------------|
| 🍝 **Restaurante** | api, db, redis | KITCHEN_TIMEOUT, MAX_TABLES | /health, /ready |
| 📚 **Biblioteca** | api, db | MAX_LOANS, RESERVATION_DAYS | /health, /ready |
| 🏥 **Clínica Veterinaria** | api, db | APPOINTMENT_DURATION | /health, /ready |
| 💊 **Farmacia** | api, db, redis | STOCK_ALERT_THRESHOLD | /health, /ready |
| 🏋️ **Gimnasio** | api, db | CLASS_MAX_CAPACITY | /health, /ready |

---

## 🎯 Objetivo

Implementar **infraestructura production-ready**:

- Dockerfile multi-stage optimizado
- Docker Compose para desarrollo
- GitHub Actions para CI/CD
- Seguridad en contenedores

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Dockerfile Multi-Stage

```dockerfile
# Build stage
FROM python:3.14-slim AS builder
WORKDIR /app
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev

# Production stage
FROM python:3.14-slim
WORKDIR /app

# Security: non-root user
RUN adduser --disabled-password --gecos "" appuser
USER appuser

COPY --from=builder /app/.venv /app/.venv
COPY src/ ./src/

ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/{domain}
      - {DOMAIN}_CONFIG_VAR=value
    depends_on:
      db:
        condition: service_healthy
    
  db:
    image: postgres:17
    environment:
      - POSTGRES_DB={domain}
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5
```

### GitHub Actions CI/CD

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.14"
      - name: Install dependencies
        run: pip install uv && uv sync
      - name: Run tests
        run: uv run pytest --cov

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker image
        run: docker build -t {domain}-api .
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── src/
│   ├── main.py
│   ├── config.py        # Settings con Pydantic
│   ├── models/
│   ├── schemas/
│   └── routers/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env.example
├── pyproject.toml
└── README.md
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Dockerfile multi-stage funcional | 15 |
| Docker Compose con health checks | 15 |
| CI/CD pipeline pasando | 10 |
| **Adaptación al Dominio** (35%) | |
| Variables de entorno coherentes | 12 |
| Servicios específicos del negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Seguridad (non-root, secrets) | 10 |
| Documentación clara | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** configuraciones genéricas
- ✅ **Diseña** variables de tu dominio
- ✅ **Implementa** servicios necesarios

---

## 📚 Recursos

- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

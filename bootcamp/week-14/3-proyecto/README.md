# 🛡️ Proyecto Semana 14: API Segura con Observabilidad

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Rate Limit por Recurso | Métricas Clave | Logs Críticos |
|---------|----------------------|----------------|---------------|
| 🍝 **Restaurante** | 100/min pedidos | orders_total, avg_prep_time | order_placed, payment_failed |
| 📚 **Biblioteca** | 50/min búsquedas | loans_active, books_available | book_borrowed, late_return |
| 🏥 **Clínica Veterinaria** | 30/min citas | appointments_day, patients_waiting | appointment_scheduled, emergency |
| 💊 **Farmacia** | 20/min recetas | sales_hour, stock_alerts | prescription_validated, low_stock |
| 🏋️ **Gimnasio** | 60/min reservas | active_members, class_occupancy | membership_expired, class_full |

---

## 🎯 Objetivo

Implementar **seguridad y observabilidad**:

- Rate Limiting (slowapi)
- Security Headers (CORS, CSP, HSTS)
- Logging estructurado (structlog)
- Métricas Prometheus
- Health Checks

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Rate Limiting

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.get("/{entities}/")
@limiter.limit("100/minute")  # Ajusta según tu dominio
async def list_{entities}(request: Request):
    ...
```

### Security Headers Middleware

```python
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    return response
```

### Métricas Prometheus

```python
from prometheus_client import Counter, Histogram, generate_latest

{ENTITY}_CREATED = Counter("{entity}_created_total", "Total {entities} created")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency")

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
```

### Logging Estructurado

```python
import structlog

logger = structlog.get_logger()

@app.post("/{entities}/")
async def create_{entity}(data: {Entity}Create):
    logger.info("{entity}_created", {entity}_id=result.id, user=current_user.id)
    return result
```

### Health Checks

```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": await check_db(),
        "redis": await check_redis(),
    }
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── middleware/
│   ├── security.py      # Security headers
│   └── rate_limit.py    # Rate limiting
├── observability/
│   ├── logging.py       # Structlog config
│   ├── metrics.py       # Prometheus metrics
│   └── health.py        # Health checks
├── routers/
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
| Rate Limiting funcional | 12 |
| Security Headers correctos | 10 |
| Métricas Prometheus | 10 |
| Health Checks completos | 8 |
| **Adaptación al Dominio** (35%) | |
| Límites coherentes con negocio | 12 |
| Métricas específicas del dominio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Middleware bien estructurado | 10 |
| Logs informativos | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** métricas genéricas sin contexto
- ✅ **Diseña** rate limits según tu negocio
- ✅ **Implementa** métricas significativas

---

## 📚 Recursos

- [slowapi Documentation](https://slowapi.readthedocs.io/)
- [Prometheus Python Client](https://prometheus.github.io/client_python/)
- [structlog](https://www.structlog.org/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

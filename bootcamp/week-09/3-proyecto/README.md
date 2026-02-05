# 🔌 Proyecto Semana 09: API con Ports & Adapters

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Servicio Multi-Canal | Puertos | Adaptadores |
|---------|---------------------|---------|-------------|
| 🍝 **Restaurante** | Notificaciones de pedidos | IOrderNotifier | Email, SMS, Push |
| 📚 **Biblioteca** | Alertas de préstamos | ILoanNotifier | Email, WhatsApp |
| 🏥 **Clínica Veterinaria** | Recordatorios de citas | IAppointmentReminder | SMS, Email |
| 💊 **Farmacia** | Alertas de stock/recetas | IStockAlert | Email, Slack |
| 🏋️ **Gimnasio** | Recordatorios de clases | IClassReminder | Push, Email |

---

## 🎯 Objetivo

Implementar un **servicio multi-canal** usando Ports & Adapters para:

- Definir puertos (interfaces) del dominio
- Crear adaptadores intercambiables
- Aplicar inversión de dependencias
- Facilitar testing y extensibilidad

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Arquitectura Ports & Adapters

```
                 ┌─────────────────┐
                 │    Dominio      │
                 │  (Entidades)    │
                 └────────┬────────┘
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
    ┌─────────┐     ┌─────────┐     ┌─────────┐
    │  Port   │     │  Port   │     │  Port   │
    │(Interface)    │(Interface)    │(Interface)
    └────┬────┘     └────┬────┘     └────┬────┘
         │               │               │
    ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
    │ Adapter │     │ Adapter │     │ Adapter │
    │ (Email) │     │  (SMS)  │     │ (Push)  │
    └─────────┘     └─────────┘     └─────────┘
```

### Puertos (Interfaces)

```python
class I{Service}Port(Protocol):
    async def send(self, recipient: str, message: {Message}) -> bool: ...
    async def get_status(self, id: str) -> {Status}: ...
```

### Adaptadores

Implementa **mínimo 3 adaptadores** diferentes:
1. Adaptador principal (Email/DB)
2. Adaptador secundario (SMS/Cache)
3. Adaptador de pruebas (Mock/Console)

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── domain/
│   ├── entities/
│   └── ports/           # ← Interfaces
├── adapters/
│   ├── primary/         # API, CLI
│   └── secondary/       # Email, SMS, DB
├── application/
│   └── services/
├── tests/
│   └── adapters/        # Test adapters
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| Puertos definidos correctamente | 15 |
| 3+ adaptadores implementados | 15 |
| Servicio multi-canal funcional | 10 |
| **Adaptación al Dominio** (35%) | |
| Servicio coherente con dominio | 12 |
| Canales lógicos para el negocio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Inversión de dependencias | 10 |
| Adaptadores intercambiables | 10 |
| Código testeable | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** "NotificationService" genérico
- ✅ **Diseña** un servicio específico de tu dominio
- ✅ **Implementa** canales relevantes para tu negocio

---

## 📚 Recursos

- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2.5 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

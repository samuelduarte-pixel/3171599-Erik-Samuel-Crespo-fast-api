# 💬 Proyecto Semana 13: WebSocket y Comunicación en Tiempo Real

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplos de Adaptación por Dominio

| Dominio | Salas/Canales | Eventos en Tiempo Real | Notificaciones |
|---------|--------------|------------------------|----------------|
| 🍝 **Restaurante** | Mesas, Cocina | Nuevo pedido, Plato listo | Mesa servida |
| 📚 **Biblioteca** | Secciones | Libro devuelto, Reserva disponible | Recordatorio vencimiento |
| 🏥 **Clínica Veterinaria** | Consultorios, Espera | Turno llamado, Consulta finalizada | Próxima cita |
| 💊 **Farmacia** | Mostrador, Bodega | Receta validada, Stock bajo | Pedido listo |
| 🏋️ **Gimnasio** | Clases, Zonas | Clase iniciada, Equipo libre | Reserva confirmada |

---

## 🎯 Objetivo

Implementar **comunicación en tiempo real**:

- WebSocket para mensajes bidireccionales
- Server-Sent Events (SSE) para notificaciones
- Rooms/Canales para agrupación
- Broadcast y mensajes privados

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### WebSocket Manager

```python
class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, list[WebSocket]] = {}  # room -> connections
    
    async def connect(self, websocket: WebSocket, room: str):
        await websocket.accept()
        if room not in self.active_connections:
            self.active_connections[room] = []
        self.active_connections[room].append(websocket)
    
    async def broadcast(self, message: str, room: str):
        for connection in self.active_connections.get(room, []):
            await connection.send_text(message)
```

### Endpoints WebSocket

```python
@app.websocket("/{domain}/{room}/ws")
async def websocket_endpoint(websocket: WebSocket, room: str):
    await manager.connect(websocket, room)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{data}", room)
    except WebSocketDisconnect:
        manager.disconnect(websocket, room)
```

### Server-Sent Events

```python
@app.get("/{domain}/events")
async def event_stream():
    async def event_generator():
        while True:
            event = await get_next_event()  # Del dominio
            yield f"data: {event.json()}\\n\\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── websocket/
│   ├── manager.py       # ConnectionManager
│   └── handlers.py      # Handlers por tipo de mensaje
├── sse/
│   └── events.py        # SSE endpoints
├── models/
│   └── {entity}.py
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| WebSocket con rooms | 15 |
| SSE implementado | 15 |
| Broadcast y privados | 10 |
| **Adaptación al Dominio** (35%) | |
| Rooms coherentes con negocio | 12 |
| Eventos específicos del dominio | 13 |
| Originalidad (no copia) | 10 |
| **Calidad del Código** (25%) | |
| Manager bien estructurado | 10 |
| Manejo de desconexiones | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No uses** "Chat" genérico
- ✅ **Diseña** canales según tu dominio
- ✅ **Implementa** eventos de negocio reales

---

## 📚 Recursos

- [FastAPI WebSockets](https://fastapi.tiangolo.com/advanced/websockets/)
- [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2-3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)

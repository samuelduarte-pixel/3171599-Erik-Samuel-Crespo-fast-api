from fastapi import FastAPI, Query

# ============================================
# CONFIGURACIÓN DE LA API
# ============================================

app = FastAPI(
    title="Tienda Deportiva API",
    description="API para Tienda de Equipamiento Deportivo",
    version="1.0.0"
)

# ============================================
# DATOS SIMULADOS DE PRODUCTOS
# ============================================

productos = [
    {"id": 1, "nombre": "Balón de fútbol", "precio": 30},
    {"id": 2, "nombre": "Raqueta de tenis", "precio": 80},
    {"id": 3, "nombre": "Zapatillas running", "precio": 120},
]

# ============================================
# ENDPOINT RAÍZ
# ============================================

@app.get("/")
async def root() -> dict:
    """Información de la API."""
    return {
        "name": "Tienda Deportiva API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": ["/productos", "/producto/{id}", "/health"]
    }

# ============================================
# ENDPOINT: LISTAR PRODUCTOS
# ============================================

@app.get("/productos")
async def get_productos():
    """Retorna la lista de productos disponibles."""
    return productos

# ============================================
# ENDPOINT: DETALLE DE UN PRODUCTO
# ============================================

@app.get("/producto/{producto_id}")
async def get_producto(producto_id: int):
    """Retorna el detalle de un producto por ID."""
    for p in productos:
        if p["id"] == producto_id:
            return p
    return {"error": "Producto no encontrado"}

# ============================================
# ENDPOINT: SALUDO PERSONALIZADO
# ============================================

GREETINGS = {
    "es": "¡Hola, {name}!",
    "en": "Hello, {name}!",
    "fr": "Bonjour, {name}!"
}

@app.get("/greet/{name}")
async def greet(name: str, language: str = "es") -> dict:
    """Saluda a una persona en el idioma especificado."""
    template = GREETINGS.get(language, GREETINGS["es"])
    return {"greeting": template.format(name=name), "language": language, "name": name}

# ============================================
# ENDPOINT: SALUDO FORMAL
# ============================================

@app.get("/greet/{name}/formal")
async def greet_formal(name: str, title: str = "Sr./Sra.") -> dict:
    """Saludo formal con título."""
    return {
        "greeting": f"Estimado/a {title} {name}, es un placer saludarle.",
        "title": title,
        "name": name
    }

# ============================================
# ENDPOINT: SALUDO SEGÚN LA HORA
# ============================================

def get_day_period(hour: int) -> tuple[str, str]:
    """Determina saludo según la hora."""
    if 5 <= hour < 12:
        return ("Buenos días", "morning")
    elif 12 <= hour < 18:
        return ("Buenas tardes", "afternoon")
    else:
        return ("Buenas noches", "night")

@app.get("/greet/{name}/time-based")
async def greet_time_based(name: str, hour: int = Query(..., ge=0, le=23)) -> dict:
    """Saluda según la hora del día."""
    greeting, period = get_day_period(hour)
    return {"greeting": f"{greeting}, {name}!", "hour": hour, "period": period}

# ============================================
# ENDPOINT: HEALTH CHECK
# ============================================

@app.get("/health")
async def health_check() -> dict:
    """Verifica el estado de la API."""
    return {"status": "healthy", "service": "tienda-deportiva-api", "version": "1.0.0"}

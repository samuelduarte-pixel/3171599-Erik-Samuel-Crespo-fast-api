"""
Tienda de Equipamiento Deportivo - API
======================================

API REST para catálogo de equipamiento deportivo con búsqueda avanzada.
"""

from fastapi import FastAPI
from routers import categories, products

app = FastAPI(
    title="SPORTYK RETAIL",
    description="""
API para gestión de catálogo de equipamiento deportivo.

## Funcionalidades
- **CRUD completo** de categorías y productos
- **Filtros avanzados**: marca, talla, género, precio, stock, tags
- **Búsqueda full-text** en nombre y descripción
- **Paginación** y **ordenamiento** configurable
- **Estadísticas** por categoría deportiva
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(categories.router)
app.include_router(products.router)


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "🏅 Sportyk Retail API",
        "docs": "/docs",
        "version": "1.0.0",
        "endpoints": {
            "categories": "/categories",
            "products": "/products",
            "stats": "/products/stats"
        }
    }


@app.get("/health", tags=["Root"])
async def health_check():
    return {"status": "healthy", "service": "Tienda Deportiva API"}
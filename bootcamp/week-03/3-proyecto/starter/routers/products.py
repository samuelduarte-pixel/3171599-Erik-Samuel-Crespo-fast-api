"""
Router de Productos
===================

CRUD con filtrado avanzado, paginación y ordenamiento
para la Tienda de Equipamiento Deportivo.
"""

from fastapi import APIRouter, Path, HTTPException, status
from datetime import datetime
import math

from database import products_db, categories_db, get_next_product_id
from schemas import ProductCreate, ProductUpdate, ProductResponse, SortOrder
from dependencies import PaginationDep, ProductFiltersDep, SortingDep

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Product not found"}}
)


def enrich_product(product: dict) -> dict:
    """Añade los datos de categoría al producto."""
    enriched = {**product}
    enriched["category"] = categories_db.get(product["category_id"])
    return enriched


# ============================================
# GET /products - Listar con filtros
# ============================================

@router.get("/")
async def list_products(
    pagination: PaginationDep,
    filters: ProductFiltersDep,
    sorting: SortingDep
):
    """
    Listar productos con filtrado avanzado, paginación y ordenamiento.

    Filtros disponibles:
    - **search**: Buscar en nombre y descripción
    - **category_id**: Filtrar por categoría
    - **min_price / max_price**: Rango de precios
    - **in_stock**: Solo productos disponibles
    - **brand**: Filtrar por marca
    - **gender**: men, women, kids, unisex
    - **size**: Talla del producto
    - **tags**: Etiquetas (puede enviar múltiples)
    """
    products = list(products_db.values())

    # Filtro: search en name y description
    if filters.search:
        term = filters.search.lower()
        products = [
            p for p in products
            if term in p["name"].lower() or (p.get("description") and term in p["description"].lower())
        ]

    # Filtro: category_id
    if filters.category_id is not None:
        products = [p for p in products if p["category_id"] == filters.category_id]

    # Filtro: min_price
    if filters.min_price is not None:
        products = [p for p in products if p["price"] >= filters.min_price]

    # Filtro: max_price
    if filters.max_price is not None:
        products = [p for p in products if p["price"] <= filters.max_price]

    # Filtro: in_stock
    if filters.in_stock is not None:
        if filters.in_stock:
            products = [p for p in products if p["stock"] > 0]
        else:
            products = [p for p in products if p["stock"] == 0]

    # Filtro: brand
    if filters.brand:
        products = [
            p for p in products
            if p.get("brand") and filters.brand.lower() in p["brand"].lower()
        ]

    # Filtro: gender
    if filters.gender:
        products = [
            p for p in products
            if p.get("gender") and p["gender"].lower() == filters.gender.lower()
        ]

    # Filtro: size
    if filters.size:
        products = [
            p for p in products
            if p.get("size") and p["size"].lower() == filters.size.lower()
        ]

    # Filtro: tags (al menos uno en común)
    if filters.tags:
        products = [
            p for p in products
            if any(tag in p.get("tags", []) for tag in filters.tags)
        ]

    # Ordenamiento
    reverse = sorting.order == SortOrder.desc
    sort_key = sorting.sort_by.value
    products = sorted(products, key=lambda p: p.get(sort_key) or "", reverse=reverse)

    # Paginación
    total = len(products)
    pages = math.ceil(total / pagination.per_page) if total > 0 else 1
    paginated = products[pagination.offset: pagination.offset + pagination.per_page]

    return {
        "items": [enrich_product(p) for p in paginated],
        "total": total,
        "page": pagination.page,
        "per_page": pagination.per_page,
        "pages": pages,
        "has_next": pagination.page < pages,
        "has_prev": pagination.page > 1
    }


# ============================================
# GET /products/stats - Estadísticas
# ============================================

@router.get("/stats")
async def get_product_stats():
    """Estadísticas de productos por categoría."""
    stats = {}
    for cat_id, cat in categories_db.items():
        cat_products = [p for p in products_db.values() if p["category_id"] == cat_id]
        prices = [p["price"] for p in cat_products]
        stats[cat["name"]] = {
            "category_id": cat_id,
            "sport_type": cat.get("sport_type"),
            "total_products": len(cat_products),
            "in_stock": sum(1 for p in cat_products if p["stock"] > 0),
            "out_of_stock": sum(1 for p in cat_products if p["stock"] == 0),
            "avg_price": round(sum(prices) / len(prices), 2) if prices else 0,
            "min_price": min(prices) if prices else 0,
            "max_price": max(prices) if prices else 0,
            "total_stock": sum(p["stock"] for p in cat_products),
        }
    return stats


# ============================================
# GET /products/{id} - Obtener uno
# ============================================

@router.get("/{product_id}")
async def get_product(
    product_id: int = Path(..., gt=0, description="Product ID")
):
    """Obtener un producto por ID con datos de categoría."""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found"
        )
    return enrich_product(products_db[product_id])


# ============================================
# POST /products - Crear
# ============================================

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    """Crear un nuevo producto en la tienda deportiva."""
    if product.category_id not in categories_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category {product.category_id} does not exist"
        )
    new_id = get_next_product_id()
    new_product = {
        "id": new_id,
        **product.model_dump(),
        "created_at": datetime.now()
    }
    products_db[new_id] = new_product
    return enrich_product(new_product)


# ============================================
# PUT /products/{id} - Reemplazar
# ============================================

@router.put("/{product_id}")
async def replace_product(
    product_id: int = Path(..., gt=0),
    product: ProductCreate = ...
):
    """Reemplazar un producto completamente."""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found"
        )
    if product.category_id not in categories_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category {product.category_id} does not exist"
        )
    existing_created_at = products_db[product_id]["created_at"]
    updated = {
        "id": product_id,
        **product.model_dump(),
        "created_at": existing_created_at
    }
    products_db[product_id] = updated
    return enrich_product(updated)


# ============================================
# PATCH /products/{id} - Actualizar parcial
# ============================================

@router.patch("/{product_id}")
async def update_product(
    product_id: int = Path(..., gt=0),
    product: ProductUpdate = ...
):
    """Actualizar un producto parcialmente."""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found"
        )
    updates = product.model_dump(exclude_unset=True)
    if "category_id" in updates and updates["category_id"] not in categories_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Category {updates['category_id']} does not exist"
        )
    products_db[product_id].update(updates)
    return enrich_product(products_db[product_id])


# ============================================
# DELETE /products/{id} - Eliminar
# ============================================

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int = Path(..., gt=0)
):
    """Eliminar un producto."""
    if product_id not in products_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found"
        )
    del products_db[product_id]
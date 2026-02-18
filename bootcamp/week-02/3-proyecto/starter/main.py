from fastapi import FastAPI, HTTPException, Query
from datetime import datetime

from schemas import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductList,
)

from database import products_db, get_next_id, find_by_sku


app = FastAPI(
    title="API Tienda de Equipamiento Deportivo",
    version="1.0.0",
)


@app.post("/products", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate):

    if find_by_sku(product.sku):
        raise HTTPException(
            status_code=409,
            detail="Product with this SKU already exists",
        )

    product_id = get_next_id()

    new_product = {
        "id": product_id,
        **product.model_dump(),
        "created_at": datetime.now(),
        "updated_at": None,
    }

    products_db[product_id] = new_product
    return new_product


@app.get("/products", response_model=ProductList)
async def list_products(
    page: int = Query(ge=1, default=1),
    per_page: int = Query(ge=1, le=100, default=10),
):

    products = list(products_db.values())
    total = len(products)

    start = (page - 1) * per_page
    end = start + per_page

    return ProductList(
        items=products[start:end],
        total=total,
        page=page,
        per_page=per_page,
    )


@app.get("/products/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]


@app.get("/products/by-sku/{sku}", response_model=ProductResponse)
async def get_product_by_sku(sku: str):
    product = find_by_sku(sku)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.patch("/products/{product_id}", response_model=ProductResponse)
async def update_product(product_id: int, product: ProductUpdate):

    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")

    stored = products_db[product_id]
    update_data = product.model_dump(exclude_unset=True)

    if "sku" in update_data:
        existing = find_by_sku(update_data["sku"])
        if existing and existing["id"] != product_id:
            raise HTTPException(status_code=409, detail="SKU already in use")

    for key, value in update_data.items():
        stored[key] = value

    stored["updated_at"] = datetime.now()

    return stored


@app.delete("/products/{product_id}", status_code=204)
async def delete_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")

    del products_db[product_id]

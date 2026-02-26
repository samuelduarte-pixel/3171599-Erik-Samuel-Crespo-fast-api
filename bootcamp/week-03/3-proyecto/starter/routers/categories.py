"""
Router de Categorías
====================

CRUD completo para categorías de equipamiento deportivo.
"""

from fastapi import APIRouter, Path, HTTPException, status
from datetime import datetime

from database import categories_db, get_next_category_id
from schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    responses={404: {"description": "Category not found"}}
)


@router.get("/", response_model=list[CategoryResponse])
async def list_categories():
    """Listar todas las categorías deportivas."""
    return list(categories_db.values())


@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(
    category_id: int = Path(..., gt=0, description="Category ID")
):
    """Obtener una categoría por ID."""
    if category_id not in categories_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_id} not found"
        )
    return categories_db[category_id]


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate):
    """Crear una nueva categoría deportiva."""
    new_id = get_next_category_id()
    new_category = {
        "id": new_id,
        **category.model_dump(),
        "created_at": datetime.now()
    }
    categories_db[new_id] = new_category
    return new_category


@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: int = Path(..., gt=0),
    category: CategoryCreate = ...
):
    """Actualizar una categoría completamente."""
    if category_id not in categories_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_id} not found"
        )
    existing = categories_db[category_id]
    updated = {
        "id": category_id,
        **category.model_dump(),
        "created_at": existing["created_at"]
    }
    categories_db[category_id] = updated
    return updated


@router.patch("/{category_id}", response_model=CategoryResponse)
async def patch_category(
    category_id: int = Path(..., gt=0),
    category: CategoryUpdate = ...
):
    """Actualizar una categoría parcialmente."""
    if category_id not in categories_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_id} not found"
        )
    existing = categories_db[category_id]
    updates = category.model_dump(exclude_unset=True)
    existing.update(updates)
    return existing


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int = Path(..., gt=0)
):
    """Eliminar una categoría."""
    if category_id not in categories_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category {category_id} not found"
        )
    del categories_db[category_id]
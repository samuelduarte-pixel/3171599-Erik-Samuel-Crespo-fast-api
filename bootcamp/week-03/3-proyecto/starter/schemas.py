"""
Schemas Pydantic
================

Modelos de datos para la Tienda de Equipamiento Deportivo.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


# ============================================
# ENUMS
# ============================================

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


class ProductSortField(str, Enum):
    name = "name"
    price = "price"
    created_at = "created_at"
    stock = "stock"


class SportType(str, Enum):
    football = "football"
    basketball = "basketball"
    tennis = "tennis"
    swimming = "swimming"
    running = "running"
    cycling = "cycling"
    gym = "gym"
    outdoor = "outdoor"
    other = "other"


# ============================================
# CATEGORY SCHEMAS
# ============================================

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Category name")
    description: str | None = Field(default=None, max_length=200)
    sport_type: SportType = Field(default=SportType.other, description="Sport type")


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    description: str | None = Field(default=None, max_length=200)
    sport_type: SportType | None = None


class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}


# ============================================
# PRODUCT SCHEMAS
# ============================================

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Product name")
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(..., gt=0, description="Price in USD")
    stock: int = Field(default=0, ge=0, description="Units in stock")
    brand: str | None = Field(default=None, max_length=50, description="Brand name")
    size: str | None = Field(default=None, max_length=20, description="Size: S, M, L, XL, 42, etc.")
    color: str | None = Field(default=None, max_length=30)
    gender: str | None = Field(default=None, description="unisex, men, women, kids")
    tags: list[str] = Field(default=[], description="Tags for search")


class ProductCreate(ProductBase):
    category_id: int = Field(..., gt=0, description="Category ID")


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    category_id: int | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)
    brand: str | None = None
    size: str | None = None
    color: str | None = None
    gender: str | None = None
    tags: list[str] | None = None


class ProductResponse(ProductBase):
    id: int
    category_id: int
    created_at: datetime
    category: CategoryResponse | None = None

    model_config = {"from_attributes": True}


# ============================================
# PAGINATION SCHEMAS
# ============================================

class PaginatedResponse(BaseModel):
    items: list
    total: int
    page: int
    per_page: int
    pages: int
    has_next: bool
    has_prev: bool
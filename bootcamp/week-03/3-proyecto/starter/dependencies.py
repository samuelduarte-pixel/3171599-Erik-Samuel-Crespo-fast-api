"""
Dependencias Reutilizables
==========================

Define dependencias para paginación, filtros y ordenamiento.
"""

from fastapi import Query, Depends
from typing import Annotated
from schemas import SortOrder, ProductSortField


# ============================================
# PAGINACIÓN
# ============================================

class PaginationParams:
    def __init__(
        self,
        page: int = Query(default=1, ge=1, description="Page number"),
        per_page: int = Query(default=10, ge=1, le=50, description="Items per page")
    ):
        self.page = page
        self.per_page = per_page
        self.offset = (page - 1) * per_page


PaginationDep = Annotated[PaginationParams, Depends()]


# ============================================
# FILTROS DE PRODUCTOS
# ============================================

class ProductFilters:
    def __init__(
        self,
        search: str | None = Query(default=None, min_length=2, description="Search in name and description"),
        category_id: int | None = Query(default=None, gt=0, description="Filter by category ID"),
        min_price: float | None = Query(default=None, ge=0, description="Minimum price"),
        max_price: float | None = Query(default=None, ge=0, description="Maximum price"),
        in_stock: bool | None = Query(default=None, description="Only show in-stock products"),
        brand: str | None = Query(default=None, min_length=2, description="Filter by brand"),
        gender: str | None = Query(default=None, description="Filter by gender: men, women, kids, unisex"),
        size: str | None = Query(default=None, description="Filter by size"),
        tags: list[str] = Query(default=[], description="Filter by tags"),
    ):
        self.search = search
        self.category_id = category_id
        self.min_price = min_price
        self.max_price = max_price
        self.in_stock = in_stock
        self.brand = brand
        self.gender = gender
        self.size = size
        self.tags = tags


ProductFiltersDep = Annotated[ProductFilters, Depends()]


# ============================================
# ORDENAMIENTO
# ============================================

class SortingParams:
    def __init__(
        self,
        sort_by: ProductSortField = Query(default=ProductSortField.name, description="Field to sort by"),
        order: SortOrder = Query(default=SortOrder.asc, description="Sort order")
    ):
        self.sort_by = sort_by
        self.order = order


SortingDep = Annotated[SortingParams, Depends()]
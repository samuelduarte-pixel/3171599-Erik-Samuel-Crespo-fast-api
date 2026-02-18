from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    sku: str = Field(..., min_length=3, max_length=20)
    category: str = Field(..., min_length=2, max_length=50)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    sku: Optional[str] = Field(None, min_length=3, max_length=20)
    category: Optional[str] = Field(None, min_length=2, max_length=50)


class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]


class ProductList(BaseModel):
    items: List[ProductResponse]
    total: int
    page: int
    per_page: int

"""
Sportyk Retail - Schemas Pydantic
Semana 04 - Proyecto

Define los schemas para validación y serialización de equipamiento deportivo.
"""

from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class OrderStatus(str, Enum):
    """Estados posibles de un pedido"""
    pending = "pending"
    confirmed = "confirmed"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class ProductCategory(str, Enum):
    """Categorías de equipamiento deportivo"""
    running = "running"
    cycling = "cycling"
    swimming = "swimming"
    gym = "gym"
    team_sports = "team_sports"
    outdoor = "outdoor"


class PaymentStatus(str, Enum):
    """Estado del pago"""
    unpaid = "unpaid"
    paid = "paid"
    refunded = "refunded"


# ============================================
# ERROR SCHEMAS
# ============================================

class ErrorDetail(BaseModel):
    code: str = Field(..., description="Código único del error")
    message: str = Field(..., description="Mensaje descriptivo")
    details: dict | None = Field(None, description="Detalles adicionales")


class ErrorResponse(BaseModel):
    error: ErrorDetail

    model_config = {
        "json_schema_extra": {
            "example": {
                "error": {
                    "code": "ORDER_NOT_FOUND",
                    "message": "Order with id 99 not found",
                    "details": None
                }
            }
        }
    }


# ============================================
# ORDER SCHEMAS
# ============================================

class OrderCreate(BaseModel):
    """Schema para crear un pedido"""
    customer_name: str = Field(..., min_length=2, max_length=100, description="Nombre del cliente")
    customer_email: str = Field(..., description="Email del cliente")
    product_name: str = Field(..., min_length=2, max_length=100, description="Nombre del producto")
    product_category: ProductCategory = Field(..., description="Categoría del producto")
    quantity: int = Field(..., ge=1, le=100, description="Cantidad de productos")
    unit_price: float = Field(..., gt=0, description="Precio unitario en USD")
    shipping_address: str = Field(..., min_length=10, max_length=300, description="Dirección de envío")
    notes: str | None = Field(None, max_length=500, description="Notas adicionales")

    model_config = {
        "json_schema_extra": {
            "example": {
                "customer_name": "Carlos Rodríguez",
                "customer_email": "carlos@example.com",
                "product_name": "Zapatillas Nike Air Zoom Pegasus",
                "product_category": "running",
                "quantity": 1,
                "unit_price": 129.99,
                "shipping_address": "Calle 100 #15-20, Bogotá, Colombia",
                "notes": "Talla 42, color negro"
            }
        }
    }


class OrderUpdate(BaseModel):
    """Schema para actualizar un pedido (PUT)"""
    customer_name: str | None = Field(None, min_length=2, max_length=100)
    customer_email: str | None = None
    product_name: str | None = Field(None, min_length=2, max_length=100)
    product_category: ProductCategory | None = None
    quantity: int | None = Field(None, ge=1, le=100)
    unit_price: float | None = Field(None, gt=0)
    shipping_address: str | None = Field(None, min_length=10, max_length=300)
    notes: str | None = Field(None, max_length=500)

    model_config = {
        "json_schema_extra": {
            "example": {
                "quantity": 2,
                "notes": "Cambio a talla 43"
            }
        }
    }


class StatusUpdate(BaseModel):
    """Schema para cambiar el status (PATCH)"""
    status: OrderStatus = Field(..., description="Nuevo estado del pedido")


class PaymentUpdate(BaseModel):
    """Schema para actualizar el pago (PATCH)"""
    payment_status: PaymentStatus = Field(..., description="Nuevo estado del pago")


class OrderResponse(BaseModel):
    """Schema de respuesta para un pedido"""
    id: int
    order_code: str
    customer_name: str
    customer_email: str
    product_name: str
    product_category: ProductCategory
    quantity: int
    unit_price: float
    total_price: float
    status: OrderStatus
    payment_status: PaymentStatus
    shipping_address: str
    notes: str | None
    created_at: datetime
    updated_at: datetime | None
    confirmed_at: datetime | None
    shipped_at: datetime | None
    delivered_at: datetime | None

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "order_code": "ORD-20240115-001",
                "customer_name": "Carlos Rodríguez",
                "customer_email": "carlos@example.com",
                "product_name": "Zapatillas Nike Air Zoom Pegasus",
                "product_category": "running",
                "quantity": 1,
                "unit_price": 129.99,
                "total_price": 129.99,
                "status": "pending",
                "payment_status": "unpaid",
                "shipping_address": "Calle 100 #15-20, Bogotá",
                "notes": "Talla 42",
                "created_at": "2024-01-15T10:30:00",
                "updated_at": None,
                "confirmed_at": None,
                "shipped_at": None,
                "delivered_at": None
            }
        }
    }


class OrderListResponse(BaseModel):
    """Schema para listado paginado de pedidos"""
    orders: list[OrderResponse]
    total: int
    skip: int
    limit: int


class OrderStats(BaseModel):
    """Schema para estadísticas de pedidos"""
    total: int
    by_status: dict[str, int]
    by_category: dict[str, int]
    by_payment: dict[str, int]
    total_revenue: float
    pending_revenue: float
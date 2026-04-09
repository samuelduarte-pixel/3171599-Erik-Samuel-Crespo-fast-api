"""
Tienda Deportiva API - Archivo Principal
Semana 04 - Proyecto

API REST para gestión de pedidos de equipamiento deportivo con:
- Response models tipados
- Status codes apropiados
- Manejo de errores consistente
- Documentación OpenAPI completa
"""

from datetime import datetime
from typing import Annotated
from fastapi import FastAPI, Path, Query, status
from fastapi.responses import JSONResponse

from models import (
    OrderStatus,
    ProductCategory,
    PaymentStatus,
    OrderCreate,
    OrderUpdate,
    StatusUpdate,
    PaymentUpdate,
    OrderResponse,
    OrderListResponse,
    OrderStats,
    ErrorResponse,
)
from database import orders_db, get_next_id, generate_order_code
from exceptions import (
    SportStoreException,
    OrderNotFoundError,
    InvalidStatusTransitionError,
    DuplicateOrderError,
    InvalidPaymentTransitionError,
    sport_store_exception_handler,
)


# ============================================
# APP CONFIGURATION
# ============================================

tags_metadata = [
    {
        "name": "orders",
        "description": "Gestión de pedidos de equipamiento deportivo. Crear, consultar, actualizar y eliminar pedidos.",
    },
    {
        "name": "stats",
        "description": "Estadísticas y métricas de los pedidos de la tienda.",
    },
    {
        "name": "health",
        "description": "Verificación del estado del servicio.",
    },
]

app = FastAPI(
    title="Tienda Deportiva API",
    description="""
## 🏅 API de Gestión de Pedidos - Equipamiento Deportivo

API REST para gestionar pedidos de una tienda de equipamiento deportivo.

### Funcionalidades principales

- **CRUD completo** de pedidos
- **Transiciones de estado** controladas (pending → confirmed → shipped → delivered)
- **Gestión de pagos** (unpaid → paid → refunded)
- **Filtros y paginación** en listados
- **Estadísticas** de ventas y categorías

### Flujo de un pedido

```
pending → confirmed → shipped → delivered
    ↓           ↓
 cancelled   cancelled
```

### Categorías disponibles
- 🏃 `running` - Zapatillas, ropa técnica
- 🚴 `cycling` - Bicicletas, accesorios
- 🏊 `swimming` - Gafas, trajes de baño
- 💪 `gym` - Pesas, máquinas
- ⚽ `team_sports` - Balones, uniformes
- 🏕️ `outdoor` - Camping, montañismo
    """,
    version="1.0.0",
    contact={
        "name": "Erik Crespo",
        "email": "erik@tiendadeportiva.com",
    },
    license_info={
        "name": "MIT",
    },
    openapi_tags=tags_metadata,
)


# ============================================
# EXCEPTION HANDLERS
# ============================================

app.add_exception_handler(SportStoreException, sport_store_exception_handler)


# ============================================
# HELPER FUNCTIONS
# ============================================

VALID_TRANSITIONS = {
    OrderStatus.pending: [OrderStatus.confirmed, OrderStatus.cancelled],
    OrderStatus.confirmed: [OrderStatus.shipped, OrderStatus.cancelled],
    OrderStatus.shipped: [OrderStatus.delivered],
    OrderStatus.delivered: [],
    OrderStatus.cancelled: [],
}

VALID_PAYMENT_TRANSITIONS = {
    PaymentStatus.unpaid: [PaymentStatus.paid],
    PaymentStatus.paid: [PaymentStatus.refunded],
    PaymentStatus.refunded: [],
}


def validate_status_transition(current: OrderStatus, target: OrderStatus) -> bool:
    """Valida si una transición de estado de pedido es permitida."""
    return target in VALID_TRANSITIONS.get(current, [])


def validate_payment_transition(current: PaymentStatus, target: PaymentStatus) -> bool:
    """Valida si una transición de pago es permitida."""
    return target in VALID_PAYMENT_TRANSITIONS.get(current, [])


def check_duplicate_order(customer_email: str, product_name: str, exclude_id: int | None = None) -> bool:
    """
    Verifica si ya existe un pedido activo (no cancelado/entregado)
    del mismo producto para el mismo cliente.
    """
    active_statuses = {OrderStatus.pending, OrderStatus.confirmed, OrderStatus.shipped}
    for order_id, order in orders_db.items():
        if exclude_id and order_id == exclude_id:
            continue
        if (
            order["customer_email"].lower() == customer_email.lower()
            and order["product_name"].lower() == product_name.lower()
            and order["status"] in active_statuses
        ):
            return True
    return False


# ============================================
# ENDPOINTS
# ============================================

@app.get(
    "/orders",
    tags=["orders"],
    response_model=OrderListResponse,
    summary="Listar pedidos",
    description="Retorna todos los pedidos con filtros opcionales por estado, categoría y paginación.",
    responses={
        200: {"description": "Lista de pedidos obtenida exitosamente"},
    }
)
async def list_orders(
    status_filter: Annotated[
        OrderStatus | None,
        Query(alias="status", description="Filtrar por estado del pedido")
    ] = None,
    category_filter: Annotated[
        ProductCategory | None,
        Query(alias="category", description="Filtrar por categoría de producto")
    ] = None,
    payment_filter: Annotated[
        PaymentStatus | None,
        Query(alias="payment_status", description="Filtrar por estado de pago")
    ] = None,
    skip: Annotated[int, Query(ge=0, description="Número de registros a omitir")] = 0,
    limit: Annotated[int, Query(ge=1, le=100, description="Máximo de resultados")] = 10,
):
    """Lista todos los pedidos con filtros opcionales y paginación."""
    filtered = list(orders_db.values())

    if status_filter:
        filtered = [o for o in filtered if o["status"] == status_filter]

    if category_filter:
        filtered = [o for o in filtered if o["product_category"] == category_filter]

    if payment_filter:
        filtered = [o for o in filtered if o["payment_status"] == payment_filter]

    total = len(filtered)
    paginated = filtered[skip: skip + limit]

    return OrderListResponse(
        orders=paginated,
        total=total,
        skip=skip,
        limit=limit
    )


@app.get(
    "/orders/{order_id}",
    tags=["orders"],
    response_model=OrderResponse,
    summary="Obtener pedido por ID",
    responses={
        200: {"description": "Pedido encontrado"},
        404: {"model": ErrorResponse, "description": "Pedido no encontrado"},
    }
)
async def get_order(
    order_id: Annotated[int, Path(ge=1, description="ID del pedido")]
):
    """Obtiene un pedido específico por su ID."""
    if order_id not in orders_db:
        raise OrderNotFoundError(order_id)
    return orders_db[order_id]


@app.post(
    "/orders",
    tags=["orders"],
    status_code=status.HTTP_201_CREATED,
    response_model=OrderResponse,
    summary="Crear pedido",
    description="Crea un nuevo pedido de equipamiento deportivo. El estado inicial siempre es `pending`.",
    responses={
        201: {"description": "Pedido creado exitosamente"},
        409: {"model": ErrorResponse, "description": "Ya existe un pedido activo igual"},
    }
)
async def create_order(order: OrderCreate):
    """Crea un nuevo pedido en estado `pending`."""
    if check_duplicate_order(order.customer_email, order.product_name):
        raise DuplicateOrderError(order.customer_email, order.product_name)

    order_id = get_next_id()
    now = datetime.now()
    total_price = round(order.quantity * order.unit_price, 2)

    orders_db[order_id] = {
        "id": order_id,
        "order_code": generate_order_code(order_id),
        "customer_name": order.customer_name,
        "customer_email": order.customer_email,
        "product_name": order.product_name,
        "product_category": order.product_category,
        "quantity": order.quantity,
        "unit_price": order.unit_price,
        "total_price": total_price,
        "status": OrderStatus.pending,
        "payment_status": PaymentStatus.unpaid,
        "shipping_address": order.shipping_address,
        "notes": order.notes,
        "created_at": now,
        "updated_at": None,
        "confirmed_at": None,
        "shipped_at": None,
        "delivered_at": None,
    }

    return orders_db[order_id]


@app.put(
    "/orders/{order_id}",
    tags=["orders"],
    response_model=OrderResponse,
    summary="Actualizar pedido",
    description="Actualiza los datos de un pedido. Solo aplica para pedidos en estado `pending` o `confirmed`.",
    responses={
        200: {"description": "Pedido actualizado exitosamente"},
        404: {"model": ErrorResponse, "description": "Pedido no encontrado"},
        409: {"model": ErrorResponse, "description": "Conflicto con pedido duplicado"},
    }
)
async def update_order(
    order_id: Annotated[int, Path(ge=1)],
    order_update: OrderUpdate
):
    """Actualiza los campos de un pedido existente."""
    if order_id not in orders_db:
        raise OrderNotFoundError(order_id)

    order = orders_db[order_id]

    # Verificar duplicado si cambia email o producto
    new_email = order_update.customer_email or order["customer_email"]
    new_product = order_update.product_name or order["product_name"]

    if (new_email != order["customer_email"] or new_product != order["product_name"]):
        if check_duplicate_order(new_email, new_product, exclude_id=order_id):
            raise DuplicateOrderError(new_email, new_product)

    update_data = order_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        order[field] = value

    # Recalcular precio total si cambió cantidad o precio
    if "quantity" in update_data or "unit_price" in update_data:
        order["total_price"] = round(order["quantity"] * order["unit_price"], 2)

    order["updated_at"] = datetime.now()

    return order


@app.patch(
    "/orders/{order_id}/status",
    tags=["orders"],
    response_model=OrderResponse,
    summary="Cambiar estado del pedido",
    description="""
Cambia el estado de un pedido siguiendo el flujo permitido:

- `pending` → `confirmed` o `cancelled`
- `confirmed` → `shipped` o `cancelled`
- `shipped` → `delivered`
- `delivered` y `cancelled` son estados finales
    """,
    responses={
        200: {"description": "Estado actualizado"},
        400: {"model": ErrorResponse, "description": "Transición de estado inválida"},
        404: {"model": ErrorResponse, "description": "Pedido no encontrado"},
    }
)
async def update_order_status(
    order_id: Annotated[int, Path(ge=1)],
    status_update: StatusUpdate
):
    """Actualiza el estado de un pedido validando las transiciones permitidas."""
    if order_id not in orders_db:
        raise OrderNotFoundError(order_id)

    order = orders_db[order_id]
    current = order["status"]
    target = status_update.status

    if current == target:
        return order

    if not validate_status_transition(current, target):
        raise InvalidStatusTransitionError(current.value, target.value)

    now = datetime.now()
    order["status"] = target
    order["updated_at"] = now

    if target == OrderStatus.confirmed:
        order["confirmed_at"] = now
    elif target == OrderStatus.shipped:
        order["shipped_at"] = now
    elif target == OrderStatus.delivered:
        order["delivered_at"] = now

    return order


@app.patch(
    "/orders/{order_id}/payment",
    tags=["orders"],
    response_model=OrderResponse,
    summary="Actualizar estado de pago",
    description="""
Actualiza el estado de pago de un pedido:

- `unpaid` → `paid`
- `paid` → `refunded`
    """,
    responses={
        200: {"description": "Pago actualizado"},
        400: {"model": ErrorResponse, "description": "Transición de pago inválida"},
        404: {"model": ErrorResponse, "description": "Pedido no encontrado"},
    }
)
async def update_order_payment(
    order_id: Annotated[int, Path(ge=1)],
    payment_update: PaymentUpdate
):
    """Actualiza el estado de pago de un pedido."""
    if order_id not in orders_db:
        raise OrderNotFoundError(order_id)

    order = orders_db[order_id]
    current = order["payment_status"]
    target = payment_update.payment_status

    if current == target:
        return order

    if not validate_payment_transition(current, target):
        raise InvalidPaymentTransitionError(current.value, target.value)

    order["payment_status"] = target
    order["updated_at"] = datetime.now()

    return order


@app.delete(
    "/orders/{order_id}",
    tags=["orders"],
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar pedido",
    responses={
        204: {"description": "Pedido eliminado exitosamente"},
        404: {"model": ErrorResponse, "description": "Pedido no encontrado"},
    }
)
async def delete_order(
    order_id: Annotated[int, Path(ge=1)]
):
    """Elimina un pedido por su ID."""
    if order_id not in orders_db:
        raise OrderNotFoundError(order_id)

    del orders_db[order_id]
    return None


@app.get(
    "/orders/stats/summary",
    tags=["stats"],
    response_model=OrderStats,
    summary="Estadísticas de pedidos",
    description="Retorna estadísticas completas: totales por estado, categoría, pago e ingresos.",
)
async def get_order_stats():
    """Obtiene estadísticas y métricas de todos los pedidos."""
    all_orders = list(orders_db.values())
    total = len(all_orders)

    by_status = {s.value: 0 for s in OrderStatus}
    by_category = {c.value: 0 for c in ProductCategory}
    by_payment = {p.value: 0 for p in PaymentStatus}
    total_revenue = 0.0
    pending_revenue = 0.0

    for order in all_orders:
        by_status[order["status"].value] += 1
        by_category[order["product_category"].value] += 1
        by_payment[order["payment_status"].value] += 1

        if order["payment_status"] == PaymentStatus.paid:
            total_revenue += order["total_price"]
        elif order["payment_status"] == PaymentStatus.unpaid:
            if order["status"] not in [OrderStatus.cancelled]:
                pending_revenue += order["total_price"]

    return OrderStats(
        total=total,
        by_status=by_status,
        by_category=by_category,
        by_payment=by_payment,
        total_revenue=round(total_revenue, 2),
        pending_revenue=round(pending_revenue, 2),
    )


# ============================================
# HEALTH CHECK
# ============================================

@app.get(
    "/health",
    tags=["health"],
    summary="Health check",
    response_description="Estado del servicio"
)
async def health_check():
    """Verifica que el servicio está funcionando correctamente."""
    return {
        "status": "healthy",
        "service": "tienda-deportiva-api",
        "version": "1.0.0",
        "total_orders": len(orders_db)
    }
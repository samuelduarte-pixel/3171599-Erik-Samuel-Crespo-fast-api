"""
Tienda Deportiva API - Excepciones Personalizadas
Semana 04 - Proyecto
"""

from fastapi import Request
from fastapi.responses import JSONResponse


class SportStoreException(Exception):
    """Base exception for Sport Store API."""

    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = 400,
        details: dict | None = None
    ):
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details
        super().__init__(message)


class OrderNotFoundError(SportStoreException):
    """Order not found exception."""

    def __init__(self, order_id: int):
        super().__init__(
            code="ORDER_NOT_FOUND",
            message=f"Order with id {order_id} not found",
            status_code=404
        )


class InvalidStatusTransitionError(SportStoreException):
    """Invalid status transition exception."""

    def __init__(self, current_status: str, target_status: str):
        super().__init__(
            code="INVALID_STATUS_TRANSITION",
            message=f"Cannot transition order from '{current_status}' to '{target_status}'",
            status_code=400,
            details={
                "current_status": current_status,
                "target_status": target_status,
                "allowed_transitions": {
                    "pending": ["confirmed", "cancelled"],
                    "confirmed": ["shipped", "cancelled"],
                    "shipped": ["delivered"],
                    "delivered": [],
                    "cancelled": []
                }
            }
        )


class DuplicateOrderError(SportStoreException):
    """Duplicate order exception."""

    def __init__(self, customer_email: str, product_name: str):
        super().__init__(
            code="DUPLICATE_ORDER",
            message=f"An active order for '{product_name}' already exists for '{customer_email}'",
            status_code=409,
            details={
                "customer_email": customer_email,
                "product_name": product_name
            }
        )


class InvalidPaymentTransitionError(SportStoreException):
    """Invalid payment status transition."""

    def __init__(self, current: str, target: str):
        super().__init__(
            code="INVALID_PAYMENT_TRANSITION",
            message=f"Cannot change payment from '{current}' to '{target}'",
            status_code=400,
            details={"current_payment_status": current, "target_payment_status": target}
        )


# ============================================
# EXCEPTION HANDLERS
# ============================================

async def sport_store_exception_handler(
    request: Request,
    exc: SportStoreException
) -> JSONResponse:
    """Handler para SportStoreException."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details
            }
        }
    )
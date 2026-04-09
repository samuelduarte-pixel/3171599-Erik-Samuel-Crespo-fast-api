"""
Tienda Deportiva API - Simulación de Base de Datos
Semana 04 - Proyecto

Base de datos en memoria para pedidos de equipamiento deportivo.
"""

from datetime import datetime
from models import OrderStatus, ProductCategory, PaymentStatus


# Simulated database (in-memory)
orders_db: dict[int, dict] = {}
order_id_counter: int = 0


def get_next_id() -> int:
    """Generate next order ID"""
    global order_id_counter
    order_id_counter += 1
    return order_id_counter


def generate_order_code(order_id: int) -> str:
    """Generate a unique order code like ORD-YYYYMMDD-XXX"""
    today = datetime.now().strftime("%Y%m%d")
    return f"ORD-{today}-{order_id:03d}"


def seed_database() -> None:
    """Seed database with sample orders"""
    global orders_db, order_id_counter

    sample_orders = [
        {
            "customer_name": "Carlos Rodríguez",
            "customer_email": "carlos@example.com",
            "product_name": "Zapatillas Nike Air Zoom Pegasus",
            "product_category": ProductCategory.running,
            "quantity": 1,
            "unit_price": 129.99,
            "status": OrderStatus.delivered,
            "payment_status": PaymentStatus.paid,
            "shipping_address": "Calle 100 #15-20, Bogotá, Colombia",
            "notes": "Talla 42, color negro",
        },
        {
            "customer_name": "Ana Martínez",
            "customer_email": "ana@example.com",
            "product_name": "Bicicleta Trek FX 3",
            "product_category": ProductCategory.cycling,
            "quantity": 1,
            "unit_price": 899.00,
            "status": OrderStatus.shipped,
            "payment_status": PaymentStatus.paid,
            "shipping_address": "Carrera 7 #32-10, Medellín, Colombia",
            "notes": None,
        },
        {
            "customer_name": "Luis García",
            "customer_email": "luis@example.com",
            "product_name": "Gafas Speedo Futura Biofuse",
            "product_category": ProductCategory.swimming,
            "quantity": 2,
            "unit_price": 34.99,
            "status": OrderStatus.confirmed,
            "payment_status": PaymentStatus.paid,
            "shipping_address": "Av. El Dorado #68-72, Bogotá, Colombia",
            "notes": "Color azul marino",
        },
        {
            "customer_name": "María López",
            "customer_email": "maria@example.com",
            "product_name": "Mancuernas Bowflex SelectTech 552",
            "product_category": ProductCategory.gym,
            "quantity": 1,
            "unit_price": 399.00,
            "status": OrderStatus.pending,
            "payment_status": PaymentStatus.unpaid,
            "shipping_address": "Calle 85 #11-92, Bogotá, Colombia",
            "notes": None,
        },
        {
            "customer_name": "Pedro Sánchez",
            "customer_email": "pedro@example.com",
            "product_name": "Balón Adidas Champions League",
            "product_category": ProductCategory.team_sports,
            "quantity": 3,
            "unit_price": 49.99,
            "status": OrderStatus.pending,
            "payment_status": PaymentStatus.unpaid,
            "shipping_address": "Cra 15 #93-75, Bogotá, Colombia",
            "notes": "Para torneo escolar",
        },
    ]

    for order_data in sample_orders:
        order_id = get_next_id()
        now = datetime.now()
        total = order_data["quantity"] * order_data["unit_price"]

        confirmed_at = None
        shipped_at = None
        delivered_at = None

        if order_data["status"] in [OrderStatus.confirmed, OrderStatus.shipped, OrderStatus.delivered]:
            confirmed_at = now
        if order_data["status"] in [OrderStatus.shipped, OrderStatus.delivered]:
            shipped_at = now
        if order_data["status"] == OrderStatus.delivered:
            delivered_at = now

        orders_db[order_id] = {
            "id": order_id,
            "order_code": generate_order_code(order_id),
            "customer_name": order_data["customer_name"],
            "customer_email": order_data["customer_email"],
            "product_name": order_data["product_name"],
            "product_category": order_data["product_category"],
            "quantity": order_data["quantity"],
            "unit_price": order_data["unit_price"],
            "total_price": round(total, 2),
            "status": order_data["status"],
            "payment_status": order_data["payment_status"],
            "shipping_address": order_data["shipping_address"],
            "notes": order_data["notes"],
            "created_at": now,
            "updated_at": None,
            "confirmed_at": confirmed_at,
            "shipped_at": shipped_at,
            "delivered_at": delivered_at,
        }


# Initialize with sample data
seed_database()
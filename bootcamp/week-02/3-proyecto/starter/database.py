"""
Simulación de Base de Datos
===========================

Base de datos en memoria para el proyecto
"Tienda de Equipamiento Deportivo".
"""

# Base de datos en memoria
products_db: dict[int, dict] = {}

# Contador de IDs
_id_counter = 0


def get_next_id() -> int:
    global _id_counter
    _id_counter += 1
    return _id_counter


def find_by_sku(sku: str) -> dict | None:
    sku_upper = sku.upper()
    for product in products_db.values():
        if product["sku"].upper() == sku_upper:
            return product
    return None


def reset_db() -> None:
    global _id_counter
    products_db.clear()
    _id_counter = 0

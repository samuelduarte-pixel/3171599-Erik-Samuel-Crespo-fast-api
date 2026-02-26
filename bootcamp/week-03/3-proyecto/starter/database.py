"""
Base de Datos Simulada
======================

Datos en memoria para la Tienda de Equipamiento Deportivo.
"""

from datetime import datetime

# ============================================
# CATEGORÍAS
# ============================================

categories_db: dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Fútbol",
        "description": "Equipamiento y accesorios para fútbol",
        "sport_type": "football",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    2: {
        "id": 2,
        "name": "Baloncesto",
        "description": "Ropa, calzado y balones de baloncesto",
        "sport_type": "basketball",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    3: {
        "id": 3,
        "name": "Running",
        "description": "Zapatillas, ropa y accesorios para correr",
        "sport_type": "running",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    4: {
        "id": 4,
        "name": "Gimnasio",
        "description": "Equipamiento y ropa para entrenamiento en gimnasio",
        "sport_type": "gym",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    5: {
        "id": 5,
        "name": "Natación",
        "description": "Trajes de baño, gafas y accesorios de natación",
        "sport_type": "swimming",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
    6: {
        "id": 6,
        "name": "Ciclismo",
        "description": "Bicicletas, cascos, ropa y accesorios de ciclismo",
        "sport_type": "cycling",
        "created_at": datetime(2024, 1, 1, 10, 0, 0)
    },
}

next_category_id = 7

# ============================================
# PRODUCTOS
# ============================================

products_db: dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Balón de Fútbol Nike Strike",
        "description": "Balón oficial de entrenamiento con tecnología AeroW Trac",
        "price": 39.99,
        "category_id": 1,
        "stock": 80,
        "brand": "Nike",
        "size": "5",
        "color": "Blanco/Negro",
        "gender": "unisex",
        "tags": ["balon", "futbol", "entrenamiento", "nike"],
        "created_at": datetime(2024, 1, 15, 9, 0, 0)
    },
    2: {
        "id": 2,
        "name": "Guayos Adidas Predator",
        "description": "Guayos de alta tracción para césped natural",
        "price": 89.99,
        "category_id": 1,
        "stock": 45,
        "brand": "Adidas",
        "size": "42",
        "color": "Negro/Rojo",
        "gender": "men",
        "tags": ["guayos", "futbol", "adidas", "cesped"],
        "created_at": datetime(2024, 2, 1, 10, 0, 0)
    },
    3: {
        "id": 3,
        "name": "Zapatillas Nike Air Zoom Pegasus",
        "description": "Zapatillas de running con amortiguación Zoom Air",
        "price": 129.99,
        "category_id": 3,
        "stock": 60,
        "brand": "Nike",
        "size": "40",
        "color": "Azul/Blanco",
        "gender": "unisex",
        "tags": ["zapatillas", "running", "nike", "amortiguacion"],
        "created_at": datetime(2024, 1, 20, 14, 0, 0)
    },
    4: {
        "id": 4,
        "name": "Mancuernas Ajustables PowerBlock",
        "description": "Set de mancuernas ajustables de 2 a 32 kg",
        "price": 299.99,
        "category_id": 4,
        "stock": 20,
        "brand": "PowerBlock",
        "size": "2-32kg",
        "color": "Negro",
        "gender": "unisex",
        "tags": ["mancuernas", "gym", "pesas", "ajustable"],
        "created_at": datetime(2024, 3, 1, 8, 0, 0)
    },
    5: {
        "id": 5,
        "name": "Traje de Baño Speedo Endurance",
        "description": "Traje de baño de competición resistente al cloro",
        "price": 54.99,
        "category_id": 5,
        "stock": 35,
        "brand": "Speedo",
        "size": "M",
        "color": "Azul Marino",
        "gender": "men",
        "tags": ["natacion", "speedo", "competicion", "resistente"],
        "created_at": datetime(2024, 2, 15, 11, 0, 0)
    },
    6: {
        "id": 6,
        "name": "Casco Ciclismo Giro Agilis",
        "description": "Casco aerodinámico con ventilación optimizada MIPS",
        "price": 149.99,
        "category_id": 6,
        "stock": 25,
        "brand": "Giro",
        "size": "L",
        "color": "Rojo Mate",
        "gender": "unisex",
        "tags": ["casco", "ciclismo", "giro", "mips", "seguridad"],
        "created_at": datetime(2024, 2, 20, 16, 0, 0)
    },
    7: {
        "id": 7,
        "name": "Pelota de Baloncesto Spalding",
        "description": "Pelota oficial NBA para interiores y exteriores",
        "price": 49.99,
        "category_id": 2,
        "stock": 0,
        "brand": "Spalding",
        "size": "7",
        "color": "Naranja",
        "gender": "unisex",
        "tags": ["baloncesto", "spalding", "nba", "oficial"],
        "created_at": datetime(2024, 3, 5, 9, 0, 0)
    },
    8: {
        "id": 8,
        "name": "Camiseta Compresión Under Armour",
        "description": "Camiseta de compresión HeatGear para entrenamiento intenso",
        "price": 34.99,
        "category_id": 4,
        "stock": 100,
        "brand": "Under Armour",
        "size": "M",
        "color": "Negro",
        "gender": "men",
        "tags": ["camiseta", "compresion", "gym", "under-armour"],
        "created_at": datetime(2024, 3, 10, 10, 0, 0)
    },
    9: {
        "id": 9,
        "name": "Gafas Natación Aqua Sphere Kayenne",
        "description": "Gafas de natación con lente panorámica antifog",
        "price": 29.99,
        "category_id": 5,
        "stock": 50,
        "brand": "Aqua Sphere",
        "size": "única",
        "color": "Negro/Transparente",
        "gender": "unisex",
        "tags": ["gafas", "natacion", "antifog", "aquasphere"],
        "created_at": datetime(2024, 3, 12, 9, 0, 0)
    },
    10: {
        "id": 10,
        "name": "Leggings Running Mujer Nike Epic",
        "description": "Mallas de compresión con bolsillos y tecnología Dri-FIT",
        "price": 59.99,
        "category_id": 3,
        "stock": 70,
        "brand": "Nike",
        "size": "S",
        "color": "Morado",
        "gender": "women",
        "tags": ["leggings", "running", "mujer", "nike", "dri-fit"],
        "created_at": datetime(2024, 3, 15, 11, 0, 0)
    },
}

next_product_id = 11


# ============================================
# HELPER FUNCTIONS
# ============================================

def get_next_category_id() -> int:
    global next_category_id
    current = next_category_id
    next_category_id += 1
    return current


def get_next_product_id() -> int:
    global next_product_id
    current = next_product_id
    next_product_id += 1
    return current
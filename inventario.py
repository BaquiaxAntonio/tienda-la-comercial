# -*- coding: utf-8 -*-
# Modulo de inventario de La Comercial

PRODUCTOS = [
    {"codigo": "A001", "nombre": "Cuaderno espiral", "precio": 22.00, "stock": 40},
    {"codigo": "A002", "nombre": "Lapicero azul", "precio": 3.50, "stock": 200},
    {"codigo": "B003", "nombre": "Cafe molido 500g", "precio": 58.00, "stock": 30},
    {"codigo": "C002", "nombre": "Jabon de manos", "precio": 15.00, "stock": 80},
    {"codigo": "C005", "nombre": "Escoba plastica", "precio": 42.00, "stock": 15},
]

def buscar_producto(codigo):
    for producto in PRODUCTOS:
        if producto["codigo"] == codigo:
            return producto
    return None

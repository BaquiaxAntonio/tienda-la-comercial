# -*- coding: utf-8 -*-
# Modulo de inventario de La Comercial

PRODUCTOS = [
    {"codigo": "A001", "nombre": "Cuaderno espiral", "precio": 25.00, "stock": 40},
    {"codigo": "A002", "nombre": "Lapicero azul", "precio": 3.50, "stock": 200},
    {"codigo": "B003", "nombre": "Café molido 500g", "precio": 60.00, "stock": 35},
    {"codigo": "C002", "nombre": "Jabón de manos", "precio": 16.00, "stock": 80},
    {"codigo": "C005", "nombre": "Escoba plástica", "precio": 42.00, "stock": 15},
]

def buscar_producto(codigo):
    for producto in PRODUCTOS:
        if producto["codigo"] == codigo:
            return producto
    return None

def hay_stock(codigo, cantidad):
    producto = buscar_producto(codigo)
    if producto is None:
        return False
    return producto["stock"] >= cantidad

def valor_inventario():
    total = 0
    for producto in PRODUCTOS:
        total = total + producto["precio"] * producto["stock"]
    return total

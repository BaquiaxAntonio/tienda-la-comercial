# -*- coding: utf-8 -*-
# Modulo de facturacion de La Comercial

from inventario import buscar_producto

NOMBRE_TIENDA = "La Comercial"

def calcular_subtotal(items):
    # items es una lista de tuplas (codigo, cantidad)
    subtotal = 0
    for codigo, cantidad in items:
        producto = buscar_producto(codigo)
        if producto:
            subtotal = subtotal + producto["precio"] * cantidad
    return subtotal

def imprimir_factura(cliente, items):
    subtotal = calcular_subtotal(items)
    print("-" * 38)
    print(NOMBRE_TIENDA)
    print("-" * 38)
    print("Cliente: " + cliente)
    print("Subtotal:".ljust(28) + ("Q" + format(subtotal, ".2f")).rjust(10))

if __name__ == "__main__":
    venta = [("A001", 2), ("B003", 1)]
    imprimir_factura("Juana Morales", venta)

# -*- coding: utf-8 -*-
# Modulo de reportes de La Comercial

from inventario import PRODUCTOS

def reporte_inventario():
    print("REPORTE DE INVENTARIO")
    print("-" * 40)
    for producto in PRODUCTOS:
        linea = producto["codigo"] + "  " + producto["nombre"]
        valor = "Q" + format(producto["precio"], ".2f")
        print(linea.ljust(32) + valor.rjust(8))
    print("-" * 40)

if __name__ == "__main__":
    reporte_inventario()

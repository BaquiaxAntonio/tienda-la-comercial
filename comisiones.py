# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin

COMISION_ALTA = 0.08
COMISION_BASE = 0.05

VENTAS_MINIMAS_COMISION_ALTA = 30000
VENTAS_MINIMAS_BONO = 50000

BONO_ALTO_VENDEDOR = 500


# lista de vendedores
VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calc():
    TOTAL_COMISIONES = 0

    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    for vendedor in VENDEDORES:

        if vendedor[1] > VENTAS_MINIMAS_COMISION_ALTA:
            comision = vendedor[1] * COMISION_ALTA

            if vendedor[1] > VENTAS_MINIMAS_BONO:
                bono = BONO_ALTO_VENDEDOR
            else:
                bono = 0

            total_vendedor = round(comision + bono, 2)

        else:
            comision = vendedor[1] * COMISION_BASE
            bono = 0

            total_vendedor = round(comision + bono, 2)

        TOTAL_COMISIONES = TOTAL_COMISIONES + total_vendedor

        print(vendedor[0] + ": Q " + str(total_vendedor))

    print("-" * 44)
    print("Total a pagar: Q " + str(round(TOTAL_COMISIONES, 2)))


calc()
# -*- coding: utf-8 -*-
"""
Módulo de cierre de caja para La Comercial.

Calcula las ventas del día, IVA incluido,
comisión del POS y depósito neto.
"""

# Constantes del negocio
TIPO_EFECTIVO = "EF"
TIPO_TARJETA = "TJ"

IVA = 0.12
COMISION_POS = 0.05


# Ventas registradas durante el día.
# Cada venta contiene: (método de pago, monto)
VENTAS_DIA = [
    ("EF", 150.00),
    ("TJ", 89.50),
    ("EF", 45.25),
    ("TJ", 210.00),
    ("EF", 78.00),
    ("TJ", 156.75),
    ("EF", 92.50),
    ("EF", 34.00),
    ("TJ", 67.25),
    ("EF", 125.00),
]


def calcular_totales_por_metodo(ventas):
    """
    Separa las ventas según el método de pago.
    Retorna los totales de efectivo y tarjeta.
    """
    total_efectivo = 0
    total_tarjeta = 0

    for metodo_pago, monto in ventas:
        if metodo_pago == TIPO_EFECTIVO:
            total_efectivo += monto
        elif metodo_pago == TIPO_TARJETA:
            total_tarjeta += monto

    return total_efectivo, total_tarjeta


def calcular_iva_incluido(total):
    """
    Obtiene el valor del IVA incluido dentro de un monto final.
    """
    return round(total - (total / (1 + IVA)), 2)


def calcular_comision(total_tarjeta):
    """
    Calcula la comisión generada por pagos con tarjeta.
    """
    return round(total_tarjeta * COMISION_POS, 2)


def generar_reporte(total_efectivo, total_tarjeta):
    """
    Genera el resumen del cierre de caja.
    """
    iva_efectivo = calcular_iva_incluido(total_efectivo)
    iva_tarjeta = calcular_iva_incluido(total_tarjeta)

    comision = calcular_comision(total_tarjeta)

    total_dia = total_efectivo + total_tarjeta
    deposito_neto = total_dia - comision

    print("=" * 42)
    print("      CIERRE DE CAJA - LA COMERCIAL")
    print("=" * 42)
    print(f"Ventas en efectivo:      Q {total_efectivo:.2f}")
    print(f"IVA incluido efectivo:   Q {iva_efectivo:.2f}")
    print(f"Ventas con tarjeta:      Q {total_tarjeta:.2f}")
    print(f"IVA incluido tarjeta:    Q {iva_tarjeta:.2f}")
    print(f"Comisión del POS:        Q {comision:.2f}")
    print("-" * 42)
    print(f"Total del día:           Q {total_dia:.2f}")
    print(f"Depósito neto:           Q {deposito_neto:.2f}")


def main():
    """
    Punto de entrada del programa.
    """
    total_efectivo, total_tarjeta = calcular_totales_por_metodo(VENTAS_DIA)

    generar_reporte(
        total_efectivo,
        total_tarjeta
    )


if __name__ == "__main__":
    main()

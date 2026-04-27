def calcular_descuento(monto):
    if not isinstance(monto, (int, float)):
        raise ValueError("El monto debe ser numérico")

    if monto > 1000:
        return monto * 0.9
    elif monto > 500:
        return monto * 0.95
    else:
        return monto
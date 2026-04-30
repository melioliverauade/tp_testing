from app.descuentos import calcular_descuento

def main():
    try:
        monto = float(input("Ingrese el monto de la compra: "))
        resultado = calcular_descuento(monto)
        print(f"El total con descuento es: ${resultado}")
    except ValueError:
        print("Error: debe ingresar un número válido")

if __name__ == "__main__":
    main()
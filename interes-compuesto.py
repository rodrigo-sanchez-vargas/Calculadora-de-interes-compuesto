while True:
    try:
        ahorro = int(
            input("Ingrese el monto a ahorrar mensualmente: ").replace(".", "")
        )

        if ahorro >= 0:
            break
    except ValueError:
        print("Ingrese solo valores numericos, ej: 100.000")

while True:
    try:
        años, meses = map(
            int, (input("Ingrese la cantidad años y meses de ahorro: ").split())
        )

        if años >= 0 and meses >= 0:
            break
    except ValueError:
        print("Ingrese solo valores numericos, ej: 4 6 (4 años y 6 meses)")

while True:
    try:
        interes_anual = float(input("Ingrese el porcentaje de interes: ")) / 100

        if interes_anual > 0:
            break
    except ValueError:
        print("El interes debe ser mayor a 0")

tiempo = (años * 12) + meses
interes_mensual = (1 + interes_anual) ** (1 / 12) - 1

valor_futuro = ahorro * ((((1 + interes_mensual) ** tiempo) - 1) / interes_mensual)
ganancias_intereses = valor_futuro - (ahorro * tiempo)

print(
    f"Dinero obtenido solo de los intereses: ${ganancias_intereses:,.0f} pesos chilenos.".replace(
        ",", "."
    )
)
print(
    f"El monto ahorrado es de: ${valor_futuro:,.0f} pesos chilenos.".replace(",", ".")
)

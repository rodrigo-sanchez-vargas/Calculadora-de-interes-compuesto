while True:
    try:
        ahorro = int(input("Monto ahorro mensual: ").replace(".", ""))

        if ahorro >= 0:
            break
    except ValueError:
        print("Ingrese solo valores numericos, ej: 100.000")

while True:
    try:
        años, meses = map(int, (input("Cantidad años y meses de ahorro: ").split()))

        if años >= 0 and meses >= 0:
            break
    except ValueError:
        print("Ingrese solo valores numericos, ej: 4 6 (4 años y 6 meses)")

while True:
    try:
        interes_anual = float(input("Porcentaje de interes: ")) / 100

        if interes_anual > 0:
            break
    except ValueError:
        print("El interes debe ser mayor a 0")

tiempo = (años * 12) + meses
interes_mensual = (1 + interes_anual) ** (1 / 12) - 1


def interes_compuesto(ahorros, time, i_mensual):
    monto_final = ahorros * ((((1 + i_mensual) ** time) - 1) / i_mensual)
    intereses = monto_final - (ahorros * time)

    return monto_final, intereses


valor_futuro, ganancias_intereses = interes_compuesto(ahorro, tiempo, interes_mensual)

print(
    f"Ganancias de intereses: ${ganancias_intereses:,.0f} pesos chilenos.".replace(
        ",", "."
    )
)
print(f"Monto total ahorrado: ${valor_futuro:,.0f} pesos chilenos.".replace(",", "."))

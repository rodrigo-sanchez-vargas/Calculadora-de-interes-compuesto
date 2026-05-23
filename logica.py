monto = input("Ingrese el monto a ahorrar mensualmente: ")
monto_corregido = int(monto.replace(".", ""))

años, meses = map(int, (input("Ingrese la cantidad años y meses de ahorro: ").split()))
tiempo = (años * 12) + meses
 
interes_anual = float(input("Ingrese el porcentaje de interes: ")) / 100
interes_mensual = (1 + interes_anual) ** (1 / 12) - 1

valor_futuro = monto_corregido * ( ( ( (1 + interes_mensual) **tiempo) - 1) / interes_mensual)
ganancias_intereses = valor_futuro - (monto_corregido * tiempo)

print(f"Dinero obtenido solo de los intereses: ${ganancias_intereses:,.0f} pesos chilenos.".replace(",", "."))
print(f"El monto ahorrado es de: ${valor_futuro:,.0f} pesos chilenos.".replace(",", "."))
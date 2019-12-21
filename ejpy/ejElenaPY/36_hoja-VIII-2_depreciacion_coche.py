# Ejercicio 36 - Hoja VIII (2) - Calcular la depreciación de un coche según la formulación indicada

otro="s"

while otro=="s":
        year=1
        vidautil=int(input("Introduce la vida útil del coche:\n"))
        coste=float(input("Introduce el coste inicial del vehículo:\n"))
        valorresidual=float(input("Introduce su valor residual:\n"))

        while (year<=vidautil):
                valorreal=(coste-valorresidual)/year
                depreacu=coste-valorreal
                print(f"Año: {2006+year} Valor real: {valorreal:.2f} Depreciación acumulada: {depreacu:.2f}.")
                year+=1

        otro=input("\n¿Deseas ver el coste de otra venta (s/n)?\n")

# Ejercicio 35 - Hoja VIII (1) - Coste cantidad de lápices según tarifa dada

otro="s"

print("A partir de 1.000 lápices, el coste es 90 euros. Si es menor es 85 euros.\n");

while otro=="s":

        unidades=int(input("Introduce el número de de lápices:\n"))
        # Si la compra es de 1.000 o más lápices el coste será de 85€, si no será de 90€
        if unidades>=1000:
                print(f"El coste de {unidades} lápices es de 85 euros")
        else:
                print(f"El coste de {unidades} lápices es de 90 euros")

        otro=input("\n¿Deseas ver el coste de otra venta (s/n)?")

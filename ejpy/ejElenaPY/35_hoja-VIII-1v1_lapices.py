# Ejercicio 35 - Hoja VIII (1) - Coste cantidad de lápices según tarifa dada por pantalla

otro="s"

coste=float(input("Introduce el coste inicial de los lápices:\n"))
unidsup=int(input("Indica a partir de qué cantidad de de lápices se reduce el coste:\n"))
costesup=float(input("Indica el coste reducido a partir de %i lápices:\n"))

print(f"A partir de {unidsup} lápices, el coste es {costesup:.2f} euros. Si es menor es {coste:.2f} euros.\n")

while otro=="s":

        unidades=int(input("Introduce el número de de lápices:\n"))

        if unidades>=unidsup:
                print(f"El coste de {unidades} lápices es de {costesup} euros")
        else:
                print(f"El coste de {unidades} lápices es de {coste} euros")

        otro=input("\n¿Deseas ver el coste de otra venta (s/n)?\n")

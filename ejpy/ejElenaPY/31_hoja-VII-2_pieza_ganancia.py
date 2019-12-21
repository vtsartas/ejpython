# Ejercicio 31 - Hoja VII (2) - Calcular precio de venta de una pieza para obtener un porcentaje dado de ganancia

# Creamos una función para calcular el importe
def importe(p,pg):  
        return (p*((100+pg)/100))

otro="s"

while otro=="s":
        precio=float(input("\nAVISO: usar el punto para los decimales:\nIntroduce el precio de coste de la pieza:\n"))
        porcganancia=float(input("Introduce el porcentaje de ganancia que deseas obtener:\n"))
        print(f"Para obtener un {porcganancia:.2f}% de ganancia en la pieza (coste {precio:.2f}) deberás venderla a {importe(precio,porcganancia):.2f}.")
        otro=input("\n¿Quieres introducir los datos de una nueva pieza (s/n)?\n")

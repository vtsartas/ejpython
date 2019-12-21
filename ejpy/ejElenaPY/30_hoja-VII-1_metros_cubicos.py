# Ejercicio 30 - Hoja VII (1) - Indicar el coste del agua de una piscina

# Creamos una función para calcular el importe
def impfinal(p,vol):  
        return (p*vol)

# Creamos una función para calcular el volumen de la piscina
def volum(anch,larg,prof):
        return (anch*larg*prof)

otro="s"

# Pedimos el coste por m3, que será el mismo durante la ejecución del programa
precio=float(input("AVISO: usar el punto para los decimales:\nIntroduce el precio por metro cúbico:\n"))

while otro=="s":
        
         # Pedimos las dimensiones de la piscina
        ancho=float(input("Introduce (en metros) el ancho de la piscina:\n"))
        largo=float(input("Introduce (en metros) el largo de la piscina:\n"))
        profundidad=float(input("Introduce (en metros) la profundidad de la piscina:\n"))
        print(f"\nLa piscina tiene {volum(ancho,largo,profundidad):.2f} metros cúbicos de agua.")
        print(f"\nEl importe para esta piscina es de {impfinal(precio,volum(ancho,largo,profundidad)):.2f}.");

        otro=input("\n¿Quieres introducir los datos de una nueva piscina? (s/n)\n")
        print(f"\nRecuerda que el importe por m3 es de {precio:.2f}.\n")

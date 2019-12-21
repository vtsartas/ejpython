# Ejercicio 33 - Hoja VII (4) - Calcular el tiempo que tardará una bicicleta
# en realizar un trayecto suponiendo que su velocidad sea constante

# Importamos el módulo 'math', necesario para poder usar la función 'trunc()'
import math

# Creamos una función para calcular las horas, minutos y segundos
def homiseg(tiemp):
        hor=math.trunc(tiemp)
        minu=math.trunc((tiemp-math.trunc(tiemp))*60)
        segu=math.trunc((((tiemp-math.trunc(tiemp))*60)-math.trunc((tiemp-math.trunc(tiemp))*60))*60)
        return (hor,minu,segu)

otro="s"

while otro=="s":
        velocidad=float(input("\nAVISO: utiliza el punto para los decimales.\nIndica (en kph) la velocidad media de la bicicleta:\n"))
        espacio=float(input("Indica (en kilómetros) la distancia entre las dos ciudades:\n"))
        
        # calculamos lo que tarda y con la función 'homiseg()' lo pasamos a un array con las horas, minutos y segundos
        hms=homiseg(espacio/velocidad)
        print(f"La bicicleta tardará {hms[0]} horas, {hms[1]} minutos y {hms[2]} segundos en realizar el trayecto indicado")
        
        otro=input("\n¿Quieres calcular otro trayecto (s/n)\n?")

# Ejercicio 6 - Si 'a' es negativo o cero mostrar un error, si no mostrar su cuadrado y su raiz

# importamos math para la raiz cuadrada
import math

# Pedimos por pantalla los dos valores con los que operaremos
a = int(input("Introduzca un valor: "))

# Comparamos para indicar cuál es mayor o si son iguales
if a<=0:
    texto="ERROR: el valor indicado ({}) es negativo o cero."
    print(texto.format(a))
else:
    cuadrado=a*a
    raiz=math.sqrt(a)
    texto="El cuadrado de 'a'({}) es {} y su raiz cuadrada {}."
    print(texto.format(a,cuadrado,raiz))

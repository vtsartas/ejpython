# Ejercicio 11v1b - Indicar si un número es par o impar. Si es cero volver a pedir otro número hasta tres veces,
# en cuyo caso avisaremos del fallo y mostraremos si un número aleatorio es par o impar

# Importamos las funciones 'seed' y 'randint' para poder generar enteros de forma aleatoria
from random import seed
from random import randint

# Preguntamos por pantalla un primer valor para 'número'
numero = int(input("Introduce un número del que quieras saber si es par o impar: "))

intentos=1 # inicializamos intentos a uno porque ya hemos leído una vez

# Si el número es cero y no llevamos tres intentos pedimos otro

while (numero==0) and (intentos<3):
    intentos=intentos+1
    numero = int(input("El número indicado es cero. Indica otro número para saber si es par ni impar: "))

# Del anterior bucle salimos si 'numero' es distinto de cero o si se ha introducido 0 tres veces
# por lo que conprobando si el número es cero ya sabemos si debemos averiguar si es par o no
else:

#Si el número es 0 indicaremos el fallo y modificaremos el valor para que diga si un aleatorio es par o impar

    if numero==0:
        # seed(2) # inicializa la semilla para obtener el aleatorio
        numero=randint(1,1000) #randint es la función que nos dará el aleatorio en el rango desead (entre 1 y 1.000 en este caso)
        texto="ERROR: Has introducido tres veces cero. Vamos a averiguar si un número aleatorio ({}) es par o impar."
        print(texto.format(numero))

# Si el resto de num/2 es cero el número es par, si no es impar
    if numero%2 == 0:
        texto="El número indicado ({}) es par."
        print(texto.format(numero))
# Si no, será impar
    else:
        texto="El número indicado ({}) es impar."
        print(texto.format(numero))

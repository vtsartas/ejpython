# // Ejercicio 11v1b - Indicar si un número es par o impar. Si es cero volver a pedir otro número hasta tres veces

# Preguntamos por pantalla un número
numero = int(input("Introduce un número del que quieras saber si es par o impar: "))

intentos=1 # inicializamos intentos a uno porque ya hemos leído una vez

# Si el número es cero y no llevamos tres intentos pedimos otro

while (numero==0) and (intentos<3):
    intentos=intentos+1
    numero = int(input("El número indicado es cero. Indica otro número para saber si es par ni impar: "))
# Del anterior bucle salimos si 'numero' es distinto de cero o si se ha introducido 0 tres veces
# por lo que conprobando si el número es cero ya sabemos si debemos averiguar si es par o no
else:
    if numero!=0:
        # Si el resto de num/2 es cero el número es par, si no es impar
        if numero%2 == 0:
            texto="El número indicado ({}) es par."
            print(texto.format(numero))
        # Si no, será impar
        else:
            texto="El número indicado ({}) es impar."
            print(texto.format(numero))
    else:
        print("ERROR: Has introducido tres veces cero.")

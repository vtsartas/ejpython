# // Ejercicio 11 - Indicar si un número es par o impar. Si es cero volver a pedir otro número hasta que no lo sea

# Preguntamos por pantalla un número
numero = int(input("Introduce un número del que quieras saber si es par o impar: "))

# Si el número es cero volvemos a pedir otro número
while numero==0:
    numero = int(input("El número indicado es cero. Indica otro número para saber si es par ni impar: "))
# Si no es cero, si su resto al dividirlo entre 2 es cero decimos que es par
else:
    if numero%2==0:
        texto="El número indicado ({}) es par."
        print(texto.format(numero))
# Si no, será impar
    else:
        texto="El número indicado ({}) es impar."
        print(texto.format(numero))

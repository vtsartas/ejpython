# Ejercicio 9 - Decir si un número entero es par, impar o cero

# Pedimos por pantalla un número
numero = int(input("Introduzca un número para averiguar si es par, impar o cero: "))

# Si el número es cero lo indicamos
if numero==0:
    print("El número indicado es cero, no es par ni impar.")
# Si no, si su resto al dividirlo entre 2 es cero decimos que es par
elif numero%2==0:
    texto="El número indicado ({}) es par."
    print(texto.format(numero))
# Si no, será impar
else:
    texto="El número indicado ({}) es impar."
    print(texto.format(numero))

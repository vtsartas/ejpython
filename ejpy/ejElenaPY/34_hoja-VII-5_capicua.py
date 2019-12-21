# Ejercicio 34 - Hoja VII (5) - Indicar si un número de 3 cifras dado es capicúa

# Importamos el módulo 'math', necesario para poder usar la función 'trunc()'
import math

# Función para ver si el número tiene 3 cifras
def trescifras(n3):
        if num>99 and num<1000:
                return True
        else:
                return False

# Función para ver si el número dado es capicúa
def capicua(n):
        unidades=n%10
        centenas=math.trunc(n/100)
        if unidades==centenas:
                return "sí"
        else:
                return "no"

otro="s"

while otro=="s":
        num=int(input("\nIntroduce el número de 3 cifras del que quieres saber si es o no capicúa:\n"))
        
        if trescifras(num):
                print(f"El número {num} {capicua(num)} es capicúa.")
        else:
                print("ERROR: el número indicado es incorrecto.")

        otro=input("\n¿Deseas comprobar si otro número es capicúa (s/n)?")

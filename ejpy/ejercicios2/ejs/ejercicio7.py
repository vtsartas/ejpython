"""
7. Programa que lea números enteros por teclado y para cada número introducido indique
si es positivo o negativo y si es par o impar. Se deben realizar tres versiones del programa:
    a) En la primera versión se utilizará un bucle while.
        La lectura de números finalizará cuando se introduzca un cero.
    b) En la segunda versión se utilizará un bucle do .. while.
        La lectura de números en esta versión también finaliza cuando se introduzca un cero.
    c) En la tercera versión también se utilizará un bucle do .. while pero en este caso
        la lectura de números finaliza cuando se responda ‘N’ ó ‘n’ a
        la pregunta “Desea introducir más números? (S/N):”
"""
from utils.utiles import *

def sietea():
    numeroa=int(input("Introduce un número para saber si es positivo/negativo y par/impar o '0' para salir: "))
    while (numeroa!=0):
        posneg="positivo" if (espositivo(numeroa)) else "negativo"
        parimpar="par" if (espar(numeroa)) else "impar"
        print(f"El número {numeroc} es {parimpar} y {posneg}.")
        numeroa=int(input("Introduce otro número o '0' para salir: "))
        
def sieteb():
    numerob=int(input("Introduce un número para saber si es positivo/negativo y par/impar o '0' para salir: "))
    while True:
        posneg="positivo" if (espositivo(numerob)) else "negativo"
        parimpar="par" if (espar(numerob)) else "impar"
        print(f"El número {numeroc} es {parimpar} y {posneg}.")
        numerob=int(input("Introduce otro número a comprobar o '0' para salir: "))
        if numerob==0:
            break

def sietec():
    numeroc=str(input("Introduce un número para saber si es positivo/negativo y par/impar o 'n'/'N' para salir: "))
    while True:
        if (numeroc=='n' or numeroc=='N'):
            break
        numeroc=int(numeroc)
        if (numeroc!=0):
            posneg="positivo" if (espositivo(numeroc)) else "negativo"
            parimpar="par" if (espar(numeroc)) else "impar"
            print(f"El número {numeroc} es {parimpar} y {posneg}.")
        else:
            print("Has introducido '0' que es par, pero ni positivo ni negativo.")
        numeroc=str(input("Introduce otro número a comprobar o 'n'/'N' para salir: "))
        

swcase={
    'a': sietea,
    'b': sieteb,
    'c': sietec
    }

def default():
   print("Opcion no válida")

def switchcs(case):
   return swcase.get(case, default)()


def ejercicio7():
    # iniciamos 'otro7' para que entre en el while
    otro7="s"

    while (otro7=="s"):
        # preguntamos qué versión se quiere ejecutar
        print("¿Qué versión del ejercicio quieres usar?")
        print("a. Con un bucle 'while'. Salida introduciendo '0': ")
        print("b. Emulando un bucle 'while' (no hay do...while en Python). Saluda con '0': ")
        print("c. Emulando un bucle 'while' (no hay do...while en Python). Salida con 'n' o 'N': ")

        version=str(input("¿Qué ejercicio deseas ejecutar (introducir el número de ejercicio)? "))

        switchcs(version)

        # preguntamos si queremos ejecutar de nuevo el ejercicio
        otro7=str(input("\n¿Deseas hacer de nuevo el ejercicio eligiendo la versión del mismo (s/n)? "))

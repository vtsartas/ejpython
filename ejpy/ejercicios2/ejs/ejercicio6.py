"""
6. Programa que pida que se introduzcan dos números enteros por teclado y
muestre los números enteros que van desde el menor hasta el mayor de los
números introducidos. Los dos números introducidos deben ser distintos.
Si son iguales se mostrará un mensaje indicandolo y se vuelven a introducir.
"""

# from utils.utiles import *

def ejercicio6():
    # iniciamos 'otro6' para que entre en el while
    otro6="s"

    while (otro6=="s"):
        # pedimos la pareja de números
        num1=int(input("Introduce el primer número: "))
        num2=int(input("Introduce el segundo número: "))
        
        # nos aseguramos de que son diferentes
        while (num1==num2):
            print("ERROR: los dos números introducidos son iguales. Introduce otra pareja de valores")
            num1=int(input("Introduce el primer número: "))
            num2=int(input("Introduce el segundo número: "))
        
        # ordenamos los valores
        if (num1>num2):
            comodin=num1
            num1=num2
            num2=comodin

        for i in range(num1,num2,1):
            print(f"{i}")
            if (i<num2):
                print(",")

        # preguntamos si queremos mostrar otra serie
        otro6=str(input("\n¿Deseas ver los números entre otros dos enteros (s/n)? "))
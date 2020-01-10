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
        
        print("¿En qué orden quieres mostrar los números?")
        print("1. De menor a mayor.")
        print("2. De mayor a menor.")
        orden=int(input())
        while (orden!=1 and orden!=2):
            orden=int(input("ERROR: vuelve a introducir 1 o 2 según el orden preferido"))
        if (orden==1):
            for i in range(num1,num2+1,1):
                print(f"{i}", end='')
                if (i<num2):
                    print(", ", end='')
        else:
            for i in range(num2,num1-1,-1):
                print(f"{i}", end='')
                if (i>num1):
                    print(", ", end='')

        # preguntamos si queremos mostrar otra serie
        otro6=str(input("\n¿Deseas ver los números entre otros dos enteros (s/n)? "))
# 1. Programa que lea un número entero por teclado y calcule si es par o impar.
def ejercicio1():
    # iniciamos 'otro1' para que entre en el while
    otro1="s"

    while (otro1=="s"):
        # pedimos el número
        num1=int(input("Introduce el número a comprobar: "))
        # imprimimos si es par o impar usando el operador ternario
        print("El número indicado es","par." if num1%2==0 else "impar.")
        # preguntamos si queremos comprobar otro
        otro1=str(input("¿Deseas comprobar si otro número es par o impar (s/n)? "))
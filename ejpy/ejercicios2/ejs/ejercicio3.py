# 3. Programa que diga cuál es el mayor de tres enteros

def ejercicio3():
    # iniciamos 'otro3' para que entre en el while
    otro3="s"

    while (otro3=="s"):
        # pedimos el primer número
        num1=int(input("Introduce el primer número: "))
        num2=int(input("Introduce el segundo número: "))
        while(num2==num1):
            num2=int(input("ERROR: El número introducido es igual al primero. Introduce otro: "))
        num3=int(input("Introduce el tercer número: "))
        while(num3==num1 or num3==num2):
            num3=int(input("ERROR: El número introducido es igual a uno de los anteriores. Introduce otro: "))

        if (num1>num2 and num1>num3):
            print("El primer número(",num1,") es mayor que",num2,"y",num3)
        elif (num2>num3):
            print("El segundo número(",num2,") es mayor que",num1,"y",num3)
        else:
            print("El tercer número(",num3,") es mayor que",num1,"y",num2)
        

        # preguntamos si queremos comprobar otros tres números
        otro3=str(input("¿Deseas comprobar otros tres números (s/n)? "))
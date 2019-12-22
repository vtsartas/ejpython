# Ejercicio 38 - Hoja VIII (4) - Mostrar las tablas de multiplicar

for op1 in range(1,10+1):
        print(f"\nTABLA DEL {op1}")
        print("-------------")
        for op2 in range (1,10+1):
                print(f"{op1} x {op2} = {op1*op2}")
        print("-------------")

if input("\n¿Te gustaría calcular la tabla de multiplicar de números más allá de 10 (s/n)?\n")=="s":
        n=int(input("¿Hasta qué número superior a 10 deseas ver la tabla?\n"))
        for op1 in range(11,n+1):
                print(f"\nTABLA DEL {op1}")
                print("-------------")
                for op2 in range (1,10+1):
                        print(f"{op1} x {op2} = {op1*op2}")
        print("-------------")

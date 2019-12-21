# Ejercicio 27 - Hoja VI (4) - Averiguar el mayor, el menor y la media de una serie de números dados

maximo=0
contador=0
suma=0

# Leemos por 1a vez un número sin entrar al bucle.
# Necesario por si es 0 y para inicializar 'minimo' (de inicio no puede ser 0)

num=int(input("Introduce un número. Si introduces 0 se indicará cuál\nes el mayor y menor número introducido, así como su media aritmética:\n"))
minimo=num
while num!=0:
        suma=suma+num
        contador+=1
        if num>maximo:
                maximo=num
        if num<minimo:
                minimo=num
        num=int(input(f"Introduce un número (ya has introducido {contador}) o 0 para terminar:\n"))
if contador==0:
        print("Has indicado directamente cero")
else:
        media=suma/contador
        print(f"Has introducido {contador} números que suman {suma}.\nSu media aritmética es {media:.2f}.\nEl mayor ha sido {maximo} y el menor {minimo}.")

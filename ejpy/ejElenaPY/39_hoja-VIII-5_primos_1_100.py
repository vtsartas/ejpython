# Ejercicio 39 - Hoja VIII (5) - Mostrar los números primos del 1 al 100

# Montamos un bucle que recorra los primeros 100 números
texto=""
for n1 in range(1,101):
        primo=True # De entrada, consideramos que el número es primo salvo que en el siguiente bucle detectemos lo contrario
        #Hacemos un bucle para dividir el número entre todos los menores o iguales que él
        for n2 in range(1,n1):
            # Si el número es divisible entre algún número de los comprendidos entre 1 y si mismo NO ES PRIMO
            if ((n2>1) and (n2<n1) and (n1%n2==0)):
                # Cambiamos el valor a 'no primo'
                primo=False
        # Comprobamos si tras el bucle el número es o no primo.
        # Si lo es, lo almacenamos en una cadena de caracteres que mostraremos al final
        if primo:
                texto=texto+str(n1)+" "
print(f"{texto}")

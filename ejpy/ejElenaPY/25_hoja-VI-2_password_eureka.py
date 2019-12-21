# Ejercicio 25 - Hoja VI (2) - Verificar si se introduce una contraseña de forma correcta con 3 intentos

intentos=0
while intentos<3:
        password=input(f"Introduce la contraseña. Tienes {3-intentos} intentos:\n")
        intentos+=1 # En python no se pueden hacer incrementos de 1 con ++ como en otros lenguajes y se usa "variable+=1"
        if password=="eureka":
                # si la contraseña es correcta terminamos el 'while' y terminamos el programa
                print("La contraseña que has introducido es CORRECTA\n")
                break
        elif intentos<3:
                # si quedan intentos pediremos otra
                print("La contraseña introducida es INCORRECTA. Prueba otra vez.\n")
        else:
                # si no quedan intentos, terminamos
                print("ERROR: Has introducido mal la contraseña 3 veces y el programa ha terminado.")
# fin del while con los 3 intentos

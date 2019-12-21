# Ejercicio 12v1b - Mostrar el cubo de los primeros n números naturales

# Inicializamos la variable 'numero' con el primer valor natural
numero=1

# Pedimos de cuántos de los primeros naturales mostrar el cubo
n = int(input("Indica de cuántos de los primeros números naturales quieres calcular su cubo: "))


# // Mientras 'numero' sea menor de n+1 mostraremos su cubo y le añadiremos 1 para el siguiente cálculo
while numero<(n+1):
        cubo=numero*numero*numero
        texto="El cubo de {} es {}."
        print(texto.format(numero,cubo))
        numero=numero+1 # sumamos 1 para obtener el valor del siguiente número natural

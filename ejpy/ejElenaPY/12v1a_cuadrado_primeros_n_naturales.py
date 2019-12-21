# Ejercicio 12v1a - Mostrar el cuadrado de los primeros n números naturales

# Inicializamos la variable 'numero con el primer valor natural
numero=1

# Pedimos de cuántos de los primeros naturales mostrar el cuadrado
n = int(input("Indica de cuántos de los primeros números naturales quieres calcular su cuadrado: "))


# // Mientras 'numero' sea menor de n+1 mostraremos su cuadrado y le añadiremos 1 para el siguiente cálculo
while numero<(n+1):
        cuadrado=numero*numero
        texto="El cuadrado de {} es {}."
        print(texto.format(numero,cuadrado))
        numero=numero+1 # sumamos 1 para obtener el valor del siguiente número natural

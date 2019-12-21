# // Ejercicio 12 - Mostrar el cuadrado de los primeros 9 números naturales

# Inicializamos la variable 'numero con el primer valor natural
numero=1

# Mientras 'numero' sea menor de 10 mostraremos su cuadrado
while numero<10:
        cuadrado=numero*numero
        texto="El cuadrado de {} es {}."
        print(texto.format(numero,cuadrado))
        numero=numero+1 # sumamos 1 para obtener el valor del siguiente número natural

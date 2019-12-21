# Ejercicio 13 - Mostrar la suma de los primeros 'n' números naturales

contador=1 # inicialicamos el contador con el primer número natural
suma=0 # inicializamos la suma a cero

# Pedimos de cuántos de los primeros naturales mostrar el cubo
n = int(input("Introduce un número. Se calculará la suma de los números naturales hasta esa cifra:"))

# Mientras el contador sea menor o igual al número dado se añadira el contador a la suma
while contador<=n:
        texto="El valor de suma ({}) + {} es igual a {}."
        print(texto.format(suma,contador,suma+contador))
# sumamos el valor del contador
        suma=suma+contador
# añadimos 1 al contador para tener el valor del siguiente número natural
        contador=contador+1 

# Mostramos el resultado final
texto="La suma de los {} primeros números naturales es {}."
print(texto.format(n,suma))

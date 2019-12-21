# Ejercicio 14 - Mostrar la suma de los primeros 'n' números pares

# Pedimos de cuántos de los primeros naturales mostrar el cubo
n = int(input("Introduce un número. Se calculará la suma de primeros n números pares: "))

contador=1 #Inicialicamos el contador a 1. Será la variable que cuente cuántos pares hemos encontrado
num=1 # inicializamos el valor donde estarán las cifras a comprobar si son par o impar
suma=0 # inicializamos la suma a cero

# mientras n sea menor o igual que el contador añadiremos el valor de contador a la suma solo cuando sea par
while contador<=n:

#comprobamos si el número a comprobar es par
        if (num%2==0):
                suma=suma+num # al ser par sumamos el valor de 'num' a la suma
                contador=contador+1 # al haber obtenido un número par incrementamos su contador en 1
                texto="Se ha sumado {} y la suma ya es {}."
                print(texto.format(num,suma))
# añadimos 1 a 'num' para analizar si el siguiente número es par o impar
        num=num+1; 

# muestra el valor final de la suma de los n primeros números pares
texto="La suma de los {} primeros números pares es {}."
print(texto.format(n,suma))

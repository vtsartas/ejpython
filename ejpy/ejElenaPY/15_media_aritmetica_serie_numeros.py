# Ejercicio Ejercicio 15 - Mostrar la media de una serie de números que dejaremos de introducir al indicar -1

contador=0 # inicialicamos el contador a 0 por si lo primero introducido es -1
suma=0 #inicializamos la suma a cero

# Pedimos un primer número
n = int(input("Introduce otro número o -1 si deseas terminar: "))

# Mientras el número introducido no sea -1 lo añadiremos a la suma y sumaremos 1 al contador
while n!=-1:
        suma=suma+n;
        contador=contador+1;
        n = int(input("Introduce otro número o -1 si deseas terminar: "))

# Si el contador es 0 es porque directamente se ha introducido -1 y no haremos la media, sí la hacemos en caso contrario
if contador==0:
        print("Has terminado directamente con -1 por lo que no se hará la media")
else:
        texto="La media de los {} números que has introducido es {}."
        print(texto.format(contador,suma/contador))

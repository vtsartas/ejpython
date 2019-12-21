# Ejercicio 1 - Operaciones básicas usando dos variables

# Pedimos por pantalla los dos valores con los que operaremos
a = int(input("Indique el primer valor: "))
b = int(input("Indique el segundo valor: "))

# Mostramos su suma
suma=a+b
texto="La suma de {} más {} es igual a {}."
print(texto.format(a,b,suma))

# Mostramos su resta
resta=a-b
texto="La resta de {} menos {} es igual a {}."
print(texto.format(a,b,resta))

# Mostramos el producto
producto=a*b
texto="El producto de {} por {} es igual a {}."
print(texto.format(a,b,producto))

# Mostramos la división salvo que el segundo valor sea cero
if (b==0):
    print("ERROR: el segundo valor es cero y no es posible dividir")
else:
    division=a/b
    texto="La división de {} entre {} es igual a {}."
    print(texto.format(a,b,division))

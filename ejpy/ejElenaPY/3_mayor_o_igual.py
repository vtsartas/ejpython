# Ejercicio 3 - Determinar cuál de los dos valores dados es mayor o si son iguales

# Pedimos por pantalla los dos valores con los que operaremos
a = int(input("Indique el primer valor: "))
b = int(input("Indique el segundo valor: "))

# Comparamos para indicar cuál es mayor o si son iguales
if a>b:
    texto="El valor de 'a'({}) es mayor que el de 'b'({})."
    print(texto.format(a,b))
elif a<b:
    texto="El valor de 'b'({}) es mayor que el de 'a'({})."
    print(texto.format(b,a))
else:
    texto="Los valores de 'a'({}) y 'b'({}) son iguales."
    print(texto.format(a,b))

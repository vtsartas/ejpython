# Ejercicio 4 - Determinar cuál de los tres valores dados es mayor

# Pedimos por pantalla los dos valores con los que operaremos
a = int(input("Indique el primer valor: "))
b = int(input("Indique el segundo valor: "))
c = int(input("Indique el tercer valor: "))

# Comparamos para indicar cuál es mayor o si son iguales
if a>b and a>c:
    texto="El mayor valor es el de 'a'({}) ('b' es {} y 'c' es {})."
    print(texto.format(a,b,c))
elif b>c:
    texto="El mayor valor es el de 'b'({}) ('a' es {} y 'c' es {})."
    print(texto.format(b,a,c))
else:
    texto="El mayor valor es el de 'c'({}) ('a' es {} y 'b' es {})."
    print(texto.format(c,a,b))

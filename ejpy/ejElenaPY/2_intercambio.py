# Ejercicio 2 - Intercambiar el valor de dos variables

# Pedimos por pantalla los dos valores con los que operaremos
a = int(input("Indique el primer valor: "))
b = int(input("Indique el segundo valor: "))
texto="El valor ORIGINAL de 'a' es {} y el de 'b' {}."
print(texto.format(a,b))

# Las intercambiamos usando una variable auxiliar
c=a
a=b
b=c
texto="El valor FINAL de 'a' es {} y el de 'b' {}."
print(texto.format(a,b))

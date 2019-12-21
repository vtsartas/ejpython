# Si 'a' es negativo hacer el producto de a*b*c, si no hacer la suma

# Pedimos por pantalla los dos valores con los que operaremos
a = int(input("Indique el primer valor: "))
b = int(input("Indique el segundo valor: "))
c = int(input("Indique el tercer valor: "))

# Comparamos para indicar cuál es mayor o si son iguales
if a<0:
    producto=a*b*c
    texto="'a'({}) es negativo, el producto de {}*{}*{} es {}."
    print(texto.format(a,a,b,c,producto))
else:
    suma=a+b+c
    texto="'a'({}) es cero o positivo, la suma de {}+{}+{} es {}."
    print(texto.format(a,a,b,c,suma))

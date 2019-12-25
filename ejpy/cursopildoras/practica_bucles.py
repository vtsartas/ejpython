from math import sqrt
for i in [1,2,3,"Ho@la"]:
    print ("Número",i)

for i in range(5):
    print ("Contador "+str(i))

for i in range(1,21,1):
    print(f"Valor de la variable {i}")

valido=False

email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("El email es correcto")
else:
    print("Incorrecto")

i=1
while i<11:
    print(f"while {i}")
    i+=1

edad=int(input("Introduce tu edad"))
while edad<0 or edad>120:
    print("Error, edad incorrecta")
    edad=int(input("Introduce tu edad: "))
print(f"Edad correcta ({edad})")


print ("Cálculo de raiz cuadrada")
numero=int(input("Introduce un número: "))
intentos=0
while numero<0:
    intentos+=1
    print(f"Has introducido {numero}. No se puede calcular la raiz de un número negativo")
    if intentos>2:
        print("Has agotado los 3 intentos")
        break
    else:
        print(f"Te quedan {3-intentos} intentos")
    numero=int(input("Introduce un número: "))
if intentos<3:
    solucion=sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {solucion}")

for letra in "Python":
    if letra=="h":
        continue
    print("Viendo la letra: "+letra)

nombre="Píldoras informáticas"
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1
    print(i)
else:
    print("Se ha terminado de recorrer el bucle")
    
print(f"En 'nombre' hay {len(nombre)} caracteres")
print(f"En la variable 'nombre' hay {contador} letras")

class miClase:
    # 'pass' no hace nada, pero completa métodos que necesitan algo
    pass



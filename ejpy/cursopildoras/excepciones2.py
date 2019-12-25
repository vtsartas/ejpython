import math

def evaluaEdad(edad):
    if edad<0:
        raise TypeError("Has introducido un valor negativo")

    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "cuídate..."

print(evaluaEdad(int(input("Introduce tu edad: "))))

def raizcuadrada(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=int(input("Número del que se calculará la raiz cuadrada: "))
try:
    print("La raiz cuadrada de ",op1," es ",raizcuadrada(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("Cálculo terminado")
# Ejercicio 23 (hoja V, 8) - Pedir un número del 1 al 100 y decir cuántos dígitos tiene (versión Elena)

# Importamos el módulo 'math', necesario para poder usar la función 'trunc()'
import math

# Pedimos por pantalla el número a verificar
num = int(input("Introduce un número del 1 al 100: "))
cifras=0
temporal=num
divisor=10

# Si el número está entre 1 y 100 indicamos cuántos dígitos tiene. Para ello comprobamos el valor de sus centenas y decenas
if (num>0 and num<101):
        while (temporal>0):
                temporal=math.trunc(num/divisor)
                cifras=cifras+1;
                divisor=divisor*10;
        texto="El número {} tiene {} dígitos"
        print(texto.format(num,cifras))
        
else:
# si el número no está entre 1 y 100 o tiene más de 3 dígitos lo indicamos
        print("ERROR.")

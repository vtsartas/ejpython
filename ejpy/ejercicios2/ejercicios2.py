from ejs.ejercicio1 import *
from ejs.ejercicio2 import *
from ejs.ejercicio3 import *
from ejs.ejercicio4 import *
from ejs.ejercicio5 import *
from ejs.ejercicio6 import *

# necesario para la salida del programa
import sys

def default():
   print("Opcion no válida")

def salir():
   sys.exit()

sw = {
       1: ejercicio1,
       2: ejercicio2,
       3: ejercicio3,
       4: ejercicio4,
       5: ejercicio5,
       6: ejercicio6,
       0: salir
    }

def switch(case):
   return sw.get(case, default)()

otroej="s"
while(otroej=="s"):
    print("1. Decir si un número es par o impar.")
    print("2. Decir si un carácter está en mayúsculas o minúsculas.")
    print("3. Decir cuál es el mayor de tres números.")
    print("4. Comprobar si una hora facilitada es válida.")
    print("5. Decir los días que tiene un mes.")
    print("6. Mostrar ordenados dos números.")
    print("7. Mostrar si un número es +/- o par/impar (tres versiones).")
    print("8. Mostrar cuántos + y - hay en un listado y su media diferenciada.")
    print("9. Listar en un array y mostrar los primeros 20 números pares.")
    print("10. Mostrar cuántos +,- y ceros hay en un array dado.")
    print("0. SALIR DEL PROGRAMA.")

    numej=int(input("¿Qué ejercicio deseas ejecutar (introducir el número de ejercicio)? "))

    switch(numej)

    otroej=str(input("¿Deseas ejecutar otro ejercicio (s/n)?\n"))


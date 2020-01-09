"""
# 5. Programa que lea una variable entera mes y compruebe si el valor
# corresponde a un mes de 30 días, de 31 o de 28. Supondremos que
# febrero tiene 28 días. Se mostrará además el nombre del mes. Se debe
# comprobar que el valor introducido esté comprendido entre 1 y 12.
"""
from utils.utiles import *

def ejercicio5():
    # iniciamos 'otro5' para que entre en el while
    otro5="s"

    while (otro5=="s"):
        # pedimos el año
        anyo=int(input("Introduce el año: "))
        mes=int(input("Introduce el mes: "))
        dias=diasmesbisi(mes) if (bisiesto(anyo)) else diasmes(mes)
        print(f"El mes de {mestexto(mes)} de {anyo} tiene {dias} días.")
    
        # preguntamos si queremos comprobar otro mes
        otro5=str(input("¿Deseas ver los días de otro mes (s/n)? "))
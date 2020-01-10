"""
9. Programa que crea un array de 20 elementos
llamado Pares y guarde los 20 primeros números pares.
Mostrar por pantalla el contenido del array creado.
"""
from utils.utiles import espar
import array

def ejercicio9():
    Pares=[]
    TOTALPARES=20
    contadorpares=0
    num=0
    while (contadorpares<TOTALPARES):
        if (espar(num)):
            Pares.append(num)
            contadorpares+=1
        num+=1
    print(Pares)
"""
10. Programa que guarda en un array 10 números enteros que se
leen por teclado. A continuación se recorre el array y calcula
cuántos números son positivos, cuántos negativos y cuántos ceros.
"""

from utils.utiles import *

import array

def ejercicio10():
    otro10="s"
    CANTNUM=10
    while (otro10=="s"):
        numeros=[]
        for i in range (0,CANTNUM,1):
            numeros.append(int(input(f"Introduce el {ordinales(i+1)} número: ")))
            
        resultado=positnegat(numeros)
        print("Has introducido {0:d} positivos, {1:d} negativos y {2:d} ceros".format(resultado.getContapos(),resultado.getContaneg(),resultado.getContaceros()))

        otro10=str(input("¿Quieres comprobar otra lista de números (s/n)? "))
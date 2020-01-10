"""
8. Programa que lea por teclado 10 números enteros y los guarde
en un array. A continuación calcula y muestra por separado la
media de los valores positivos y la de los valores negativos.
"""

from utils.utiles import *
import array

def ejercicio8():
    otro8="s"
    CANTNUM=10
    while (otro8=="s"):
        numeros=[]
        for i in range (0,CANTNUM,1):
            numeros.append(int(input(f"Introduce el {ordinales(i+1)} número: ")))
            while numeros[i]==0:
                numeros[i]=int(input(f"Has introducido 0.\nIntroduce otro número para el {ordinales(i+1)} valor: "))
                         
        resultado=positnegat(numeros)
        if (resultado.getContapos()!=0):
            mediapos=resultado.getSumapos()/resultado.getContapos()
            print("La media de los {0:d} positivos que has introducido es {1:.2f}".format(resultado.getContapos(),float(mediapos)))
        else:
            print("No has introducido ningún número positivo.")
            
        if (resultado.getContaneg()!=0):
            medianeg=resultado.getSumaneg()/resultado.getContaneg()
            print("La media de los {0:d} negativos que has introducido es {1:.2f}".format(resultado.getContaneg(),float(medianeg)))
        else:
            print("No has introducido ningún número negativo.")

        otro8=str(input("¿Quieres comprobar otra lista de números (s/n)? "))


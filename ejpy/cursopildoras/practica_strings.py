nomusu=input("Introduce tu nombre de usuario: ")
print("El nombre es: ", nomusu.upper())
print("El nombre es: ", nomusu.capitalize())
print("El nombre es: ", nomusu.lower())

edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
    edad=input("Introduce la edad: ")


if (int(edad)<18):
    print("Menor de edad")
else:
    print("Mayor de edad")

# hacer el ejercicio del vídeo 33
# Crea un programa que pida introducir una dirección de email por teclado.
# El programa debe imprimir en consola si la dirección de email es correcta o no
# en función de si esta tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta.
# Si tiene más de una o ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo
# de la dirección de email o al final, la dirección también será errónea,

# http://pyspanishdoc.sourceforge.net/lib/string-methods.html"""

correcto=False
while(correcto==False):
    email=input("\nIntroduce tu email: ")
    if (email.startswith("@")==False):
        if (email.endswith("@")==False):
            if (email.count("@")==1):
                correcto=True
                print("Tu email",email," es correcto")
                break
    print("La dirección introducida (",email,") no es correcta\nIntroduce otra.")

        



# 2. Programa que lea un carácter por teclado y compruebe si es una letra mayúscula

def ejercicio2():
    # iniciamos 'otro2' para que entre en el while
    otro2="s"

    while (otro2=="s"):
        # pedimos la letra y comprobamos que solo sea 1 carácter
        letra="nula"
        while(len(letra)!=1):
            letra=str(input("Introduce la letra a comprobar: "))
            if (len(letra)!=1):
                print("ERROR: debes introducir solo una letra.")
        
        # imprimimos si es par o impar usando el operador ternario y el método '.isupper()'
        print("La letra indicada (",letra,") está en ","mayúsculas." if letra.isupper() else "minúsculas.")

        # preguntamos si queremos comprobar otra
        otro2=str(input("¿Deseas comprobar otra letra (s/n)? "))
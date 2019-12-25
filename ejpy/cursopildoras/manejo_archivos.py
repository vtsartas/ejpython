from io import open

# creamos un archivo (si no existe)
archivo_texto=open("archivo.txt","w")

frase="25 de diciembre de 2019.\nEs navidad."

# le añadimos contenido
archivo_texto.write(frase)

# cerramos el fichero de texto
archivo_texto.close()

# leemos el contenido del fichero
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)

# leemos el fichero por líneas ()
archivo_texto=open("archivo.txt","r")
lineas_texto=archivo_texto.readlines()
print("Primera línea:")
print(lineas_texto[0])
print("Segunda línea:")
print(lineas_texto[1])
archivo_texto.close()

# añadimos contenido
archivo_texto=open("archivo.txt","a")
archivo_texto.write("\nTercera línea añadida con el modo 'a' (append)")
archivo_texto.close()

# con seek podemos llevar el puntero de lectura a la posición deseada
archivo_texto=open("archivo.txt","r")
archivo_texto.seek(12)
texto=archivo_texto.read()
print("\nDesde la posición 12: \n",texto)

archivo_texto.seek(0)
texto=archivo_texto.read()
print(texto)
print("\nDesde la posición 0: \n",texto)

# podemos obtener la longitud del texto (recordad poner el puntero al inicio)
archivo_texto.seek(0)
longitud_texto=len(archivo_texto.read())
print("Longitud: ",longitud_texto)
archivo_texto.seek(longitud_texto/2)
texto=archivo_texto.read()
print(texto)
print("\nMedio texto: \n",texto)

archivo_texto.close()

# "r+" es modo de apertura de lectura y escritura 
archivo_texto=open("archivo.txt","r+")
lineas_texto=archivo_texto.readlines()
lineas_texto[1]="Línea de texto insertada después.\n"
archivo_texto.seek(0)
archivo_texto.writelines(lineas_texto)
archivo_texto.close()
# leemos y mostramos el resultado
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
print(texto)
archivo_texto.close()

import pickle

lista_nombres=["Pedro","Ana","María","Isabel"]

fichero_binario=open("lista_nombres","wb")

# guardamos la información de la lista en el fichero de forma binaria
pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del(fichero_binario)


fichero=open("lista_nombres","rb")
lista=pickle.load(fichero)
print(lista)
fichero.close()
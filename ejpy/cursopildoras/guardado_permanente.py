import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)


class ListaPersonas:
    personas=[]

    def __init__(self):
        listadePax=open("ficheroPax","ab+")
        listadePax.seek(0)
        try:
            self.personas=pickle.load(ListaPersonas)
            print("Se cargaron {} personas del fichero".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listadePax.close()
            del(listadePax)
    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasFichExt()
    
    def mostrarPersonas(self):
        for i in self.personas:
            print(i)

    def guardarPersonasFichExt(self):
        ListaPersonas=open("ficheroPax","wb")
        pickle.dump(self.personas,ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)
    
    def mostrarPaxFichero(self):
        print("La info de personas en el fichero es la siguiente:")
        for p in self.personas:
            print(p)

miListaP=ListaPersonas()

p1=Persona("Sandra","F","23")
miListaP.agregarPersonas(p1)

p2=Persona("Pepe","M","23")
miListaP.agregarPersonas(p2)

p3=Persona("Ana","F","33")
miListaP.agregarPersonas(p3)



miListaP.mostrarPaxFichero

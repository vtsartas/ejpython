class Vehiculos():
    # método constructor de los atributos de la clase 'Vehiculos'
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.frena=False
        self.acelera=False

    # comportamientos

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\n¿En marcha?: ",
        self.enmarcha,"\n¿Acelerando?:",self.acelera,"\n¿Frenando?:",self.frena)

# creamos una clase 'VElectricos'
class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100

    def cargarEnergia(self): 
        self.cargando=True

# la subclase biciElectrica hereda de dos superclases
class biciElectrica(VElectricos):
    def estado(self):
        super().estado()
        print("Autonomía:",self.autonomia)


# creamos una clase 'Furgoneta' heredera de la clase 'Vehiculo'
class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

# creamos la subclase 'Moto' a partir de la superclase 'Vehiculos'
class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\n¿En marcha?: ",
        self.enmarcha,"\n¿Acelerando?:",self.acelera,"\n¿Frenando?:",self.frena," ",self.hcaballito)


miMoto1=Moto("Yamaha","YZR")

miMoto1.caballito()

miMoto1.estado()

print ("\nFurgonetas:")
miFurgoneta1=Furgoneta("Renault","Kangoo")

miFurgoneta1.arrancar()
miFurgoneta1.estado()
print(miFurgoneta1.carga(True))

# BICICLETA ELÉCTRICA
print ("\nBicicletas:")

miBici=biciElectrica("Orbea","Rayito")

miBici.estado()


####################################
# ESCRITURA EN BINARIO DE OBJETOS  #
import pickle
coche1=Vehiculos("Peugeot","207")
coche2=Vehiculos("Ferrari","F40")
coche3=Vehiculos("Porsche","911")

coches=[coche1,coche2,coche3]

# grabamos los objetos instanciados...
fichero=open("losCoches","wb")
pickle.dump(coches,fichero)
fichero.close()
del(fichero)

# ... pero para que esto funcione deben estar definidas las clases
ficheroApertura=open("losCoches","rb")
misCoches=pickle.load(ficheroApertura)
for c in misCoches:
    print(c.estado())
ficheroApertura.close()
# no podríamos usarlo en otro módulo donde no estén las clases (pueden ser importadas)
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
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\n¿En marcha?: ",self.enmarcha,"\n¿Acelerando?:",self.acelera,"\n¿Frenando?:",self.frena)

class Moto(Vehiculos):
    pass

miMoto1=Moto("Yamaha","YZR")

miMoto1.estado()
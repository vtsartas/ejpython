class Coche():
    # Método constructor de la clase Coche
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__puertas=3
        self.__enmarcha=False

   # Método que muestra el estado de los atributos del coche
    def estado(self):
        print("El coche tiene ",self.__ruedas," ruedas. Un ancho de ",self.__anchoChasis," y un largo de ",
        self.__largoChasis,".")


    # Método que cambia el estado del atributo enmarcha
    def arrancarparar(self,arrancamos):
        self.__enmarcha=arrancamos

        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha."
        elif (self.__enmarcha and chequeo==False):
            return "Problema en el chequeo inicial del coche"
        else:
            return "El coche está parado."


    def __chequeo_interno(self):
        print("Realizando chequeo interno.")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


print("Coche 1")
# instanciamos un objeto 'miCoche' de la clase 'Coche'
miCoche=Coche()
# mostramos sus atributos con el método 'estado()'
miCoche.estado()

# Cambiamos con el método 'arrancarparar()' el valor del atributo 'enmarcha' del coche (se muestra el nuevo estado) 
print(miCoche.arrancarparar(True))
print(miCoche.arrancarparar(False))

# instanciamos un objeto 'miCoche2' de la clase 'Coche'
print("Coche 2")
miCoche2=Coche()

miCoche2.ruedas=2
miCoche2.estado()
print(miCoche2.arrancarparar(False))

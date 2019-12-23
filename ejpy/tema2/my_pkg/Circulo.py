from math import pi

class Circulo():

    # método contructor de la clase
    def __init__(self):
        self.__posx=0
        self.__posy=0
        self.__radio=0

    # get/set

    def getval(self):
        return self

    def setval(self,px,py,r):
        self.__posx=px
        self.__posy=py
        self.__radio=r

    # métodos propios de la clase

    def PerimetroCirc(self):
        return 2*self.__radio*pi
    
    def AreaCirc(self):
        return 2*(self.__radio**2)
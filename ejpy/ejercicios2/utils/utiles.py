def diasmes(mesa):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    return dias[mesa-1]

def diasmesbisi(mesb):
    dias=[31,29,31,30,31,30,31,31,30,31,30,31]
    return dias[mesb-1]

def mestexto(mestxt):
    mes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return mes[mestxt-1]

def bisiesto(a):
    return True if ((a%4==0 and a%100!=0) or (a%100==0 and a%400==0)) else False

def espositivo(n):
    return True if (n>0 and n!=0) else False

def espar(num):
    return True if (num%2==0) else False

def ordinales(nu):
    ordi=["primer","segundo","tercer","cuarto","quinto","sexto","séptimo","octavo","noveno","décimo"]
    return ordi[nu-1]

class PosiNega():
   
    # defino el método contructor de la clase

    def __init__(self,contapos,contaneg,contaceros,sumapos,sumaneg):
        self.__contapos=contapos
        self.__contaneg=contaneg
        self.__contaceros=contaceros
        self.__sumapos=sumapos
        self.__sumaneg=sumaneg
   
   
    # métodos get/set
    
    def getContapos(self):
        return self.__contapos
    def setContapos(self,valor):
        self.__contapos=valor
    
    def getContaneg(self):
        return self.__contaneg
    def setContaneg(self,valor):
        self.__contaneg=valor

    def getContaceros(self):
        return self.__contaceros
    def setContaceros(self,valor):
        self.__contaceros=valor

    def getSumapos(self):
        return self.__sumapos
    def setSumapos(self,valor):
        self.__sumapos=valor
    
    def getSumaneg(self):
        return self.__sumaneg
    def setSumaneg(self,valor):
        self.__sumaneg=valor
        

def positnegat(listanum):
    opera=PosiNega(0,0,0,0,0)
    for i in range (0,len(listanum),1):
        if listanum[i]>0:
            opera.setContapos(opera.getContapos()+1)
            opera.setSumapos(opera.getSumapos()+listanum[i])
        elif listanum[i]<0:
            opera.setContaneg(opera.getContaneg()+1)
            opera.setSumaneg(opera.getSumaneg()+listanum[i])
        else:
            opera.setContaceros(opera.getContaceros()+1)
    return opera

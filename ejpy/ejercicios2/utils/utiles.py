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
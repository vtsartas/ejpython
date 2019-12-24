"""def generaPares(Limite):
    num=1
    miLista=[]
    while num<Limite:
        miLista.append(num*2)
        num+=1
    
    return miLista"""

def generaPares(Limite):
    num=1
    while num<Limite:
        yield num*2
        num+=1

devuelvePares=generaPares(10)

#for i in devuelvePares:
    #print (i)

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))

print("Aquí podría ir más código")

print(next(devuelvePares))

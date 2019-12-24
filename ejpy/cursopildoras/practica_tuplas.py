miTupla1=("Juan","Pepe",13,18,2019,13)
print(miTupla1[1])
miLista1=list(miTupla1)
print(miTupla1)
print(miLista1)
miTupla2=tuple(miLista1)
print(miTupla2)
print(13 in miTupla2)
print(165 in miTupla2)
print(miTupla1.count(13))
print(len(miTupla1))

n1,n2,n3,n4,n5,n6=miTupla1

print(n1,n2,n3,n4,n5,n6)
print(miTupla1.index(13))
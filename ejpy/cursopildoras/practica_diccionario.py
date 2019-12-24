miDiccionario1={"España":"Madrid","Alemania":"Berlín","Francia":"París"}
miDiccionario1["Italia"]="Lisbos"
print(miDiccionario1)
# modificar valor de una clave
miDiccionario1["Italia"]="Roma"
print(miDiccionario1)
# borrar una clave
del miDiccionario1["Francia"]
print(miDiccionario1)
miDiccionario2={23:"Jordan",10:"Messi","Mosqueteros":3}
print(miDiccionario2)
miTupla1=("Juan","Pepe",13,18,2019,13)
miDiccionario3={miTupla1[0]:"Madrid",miTupla1[1]:"Paris"}
print(miDiccionario3)
print(miDiccionario3["Juan"])
miDiccionario5={23:"Jordan","Equipo":"Bulls","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario5["anillos"])
print(miDiccionario5.keys())
print(miDiccionario5.values())
print(len(miDiccionario5))
print(miDiccionario5)
miLista1=["Pepe","Luis","María","Jose"]

print("Índice 2",miLista1[2])
print(miLista1[:])
print("Indice -3",miLista1[-3])
print(miLista1[1:3])

miLista1.append("Antonio")
print(miLista1[:])
miLista1.append("Luis")
print(miLista1.count("Luis"))
miLista1.insert(2,"Sandra")
miLista1.extend(["Manuel","Jorge",5,"Ana",True,78.35])
print(miLista1[:])
print(miLista1.index("Luis"))
print("Luis" in miLista1)
print("Isi" in miLista1)
print(5+miLista1[miLista1.index(5)])
miLista1.remove("Jorge")
print(miLista1[:])
miLista1.pop()
print(miLista1[:])

miLista2=["Isidoro","Guillermo"]

miLista3=miLista1+(miLista2*2)

print(miLista3[:])
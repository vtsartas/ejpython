# Ejercicio 18 (V-3) - Calcular el reparto de ganancias en proporción al número de acciones sobre el total

# Pedimos el monto de las ganancias y el número de acciones de cada socio
ganancias = int(input("Introduce el montante de las ganancias obtenidas: "))
acciones1 = int(input("Introduce el número de acciones del PRIMER socio: "))
acciones2 = int(input("Introduce el número de acciones del SEGUNDO socio: "))
acciones3 = int(input("Introduce el número de acciones del TERCER socio: "))

# Calculamos el total de acciones y de la proporción sacamos las ganancias de cada socio
totalacciones=acciones1+acciones2+acciones3
ganancias1=ganancias*(acciones1/totalacciones)
ganancias2=ganancias*(acciones2/totalacciones)
ganancias3=ganancias*(acciones3/totalacciones)

texto="El 1er socio obtiene {} ganancias, el 2o {} y el 3o {}."
print(texto.format(ganancias1,ganancias2,ganancias3))

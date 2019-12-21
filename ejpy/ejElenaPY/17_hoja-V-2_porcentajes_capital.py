# Ejercicio 17 (V-2) - Calcular el capital total y el porcentaje de cada socio

lados=0 # inicialicamos el contador a 0
sumalados=0 # inicializamos la suma a cero

# Pedimos el capital de cada socio
capitalmiguel = int(input("Introduce el capital aportado por Miguel: "))
capitaleva = int(input("Introduce el capital aportado por Eva: "))
capitaleduardo = int(input("Introduce el capital aportado por Eduardo: "))

# Calculamos y mostramos el capital total así como el porcentaje aportado por cada socio
capitaltotal=capitalmiguel+capitaleva+capitaleduardo
texto="El capital total de la sociedad es de {}."
print(texto.format(capitaltotal))

porcmiguel=(capitalmiguel*100)/capitaltotal
porceva=(capitaleva*100)/capitaltotal
porceduardo=(capitaleduardo*100)/capitaltotal

texto="Miguel tiene un {}% del total, Eva un {}% y Eduardo un {}%."
print(texto.format(porcmiguel,porceva,porceduardo))




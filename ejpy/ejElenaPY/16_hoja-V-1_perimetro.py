# Ejercicio 16 (V-1) - Calcular el perímetro de un terreno

lados=0 # inicialicamos el contador a 0
sumalados=0 # inicializamos la suma a cero

# Pedimos el valor de un primer lado
lado = int(input("Introduce la longitud del primer lado del terreno (mínimo 3 lados): "))

# Mientras el valor del lado no sea -1 y a la vez tengamos 3 lados o más, seguiremos pidiendo lados
while lados<3:

# Solo sumaremos el valor del lado si no es -1, en cuyo caso indicaremos el error
        if lado!=-1:
                sumalados=sumalados+lado
                lados=lados+1
                texto="Introduce otro lado (llevas {} lados) o -1 si deseas terminar: "
                lado = int(input(texto.format(lados)))
        else:
                texto="Has introducido -1 pero aún no has indicado 3 lados ({}). Introduce otro lado: "
                lado = int(input(texto.format(lados)))
# Pediremos lados adicionales a los 3 mínimos, pararemos con -1
while lado!=-1:
        sumalados=sumalados+lado
        lados=lados+1
        texto="Introduce otro lado (llevas {} lados) o -1 si deseas terminar: "
        lado = int(input(texto.format(lados)))
        
# Mostraremos por pantalla el número total de lados introducido y su suma (el perímetro)
texto="Has introducido datos de un terreno de {} lados cuyo perímetro es de {}."
print(texto.format(lados,sumalados))

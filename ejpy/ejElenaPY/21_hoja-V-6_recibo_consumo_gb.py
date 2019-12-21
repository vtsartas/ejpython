# Ejercicio 21 (hoja V, 6) - Calcular recibo de operador según GB consumidos

# Pedimos por pantalla el consumo en GB realizado
consumo = int(input("Introduce el consumo total del mes del cliente en GB: "))

# Si el consumo es 4 GB o menos el importe será 45€, hasta 8GB de 85€ y los GB adicionales a 4.5€
if consumo<=4:
        print("El recibo es de 45 euros.")
elif consumo<=8:
        print("El recibo es de 85 euros.")
else:
        coste=85+((consumo-8)*4.5)
        texto="El recibo es de {} euros."
        print(texto.format(coste))

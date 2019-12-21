# Ejercicio 8 - Aplicar descuento del 15% si el mes actual es octubre

# Pedimos por pantalla el precio del artículo y el mes actual
precio = int(input("Introduzca el precio del artículo: "))
mes_actual = str(input("Introduzca el mes actual (en minúsculas): "))
importe=precio
# Si el mes actual es octubre aplicamos el descuento
if mes_actual=="octubre":
    importe=precio*((100-15)/100)
    texto="El importe del artículo es {} y tiene descuento por ser "+mes_actual+" (su precio original era {})."
    print(texto.format(importe,precio))

# Si no, mostramos el importe sin descuento
else:
    texto="El importe del artículo es {} y no tiene descuento por ser "+mes_actual+"."
    print(texto.format(importe))

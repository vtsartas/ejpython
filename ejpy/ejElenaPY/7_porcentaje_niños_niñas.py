# Ejercicio 7 - Calcular los porcentajes de niños y niñas

# Pedimos por pantalla el número de niños y niñas
num_ninos = int(input("Introduzca el número de NIÑOS: "))
num_ninas = int(input("Introduzca el número de NIÑAS: "))

# Calculamos el porcentaje de niños y niñas y lo mostramos
porc_ninos=(100*num_ninos)/(num_ninos+num_ninas)
porc_ninas=100-porc_ninos
texto="El porcentaje de NIÑOS es del {}% y el de NIÑAS un {}%."
print(texto.format(porc_ninos,porc_ninas))

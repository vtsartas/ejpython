# Ejercicio 19 (V-4) - Calcular los sueldos básico, bruto y neto según plantea el ejercicio sobre unos datos dados

# Pedimos por pantalla el total de horas trabajadas este mes y la tarifa a aplicar
horas = int(input("Introduce el número de horas trabajadas: "))
tarifa = int(input("Introduce la tarifa por hora a aplicar para calcular el sueldo: "))

# Calculamos el importe de cada tipo de sueldo
sueldobasico=horas*tarifa;
sueldobruto=sueldobasico*1.18;
sueldoneto=sueldobruto*0.88;

texto="El salario básico que le corresponde a este trabajador por realizar {} horas a {} de coste/hora es de {}."
print(texto.format(horas,tarifa,sueldobasico))

texto="Su salario bruto será de {} y su sueldo neto de {}."
print(texto.format(sueldobruto,sueldoneto))

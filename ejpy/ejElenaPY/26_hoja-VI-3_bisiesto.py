# Ejercicio 26 - Hoja VI (3) - Verificar si el año dado es bisiesto según las indicaciones dadas

otro="s"
while otro=="s":
        year=int(input("Introduce el año del que deseas comprobar si es o no bisiesto:"))
        # Comprobamos según las indicaciones dadas si es o no bisiesto
        if ((year%4==0 and year%100!=0) or (year%100==0 and year%400==0)):
                print(f"El año {year} es bisiesto.")
        else:
                print(f"El año {year} NO es bisiesto.")
        otro=input("¿Deseas evaluar otro año (s/n)?")

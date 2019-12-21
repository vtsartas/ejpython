# Ejercicio 29 - Hoja VI (6) - Comprobar si una fecha introducida con cifras es correcta y poner el nombre del mes

# Creamos una función para comprobar si el año es o no bisiesto
def bisiesto(ano):  
        if ((ano%4==0 and ano%100!=0) or (ano%100==0 and ano%400==0)):
                return True
        else:
                return False

otro="s"

while otro=="s":
        # Pedimos los datos de la fecha a comprobar
        day=int(input("Introduce el día:\n"))
        month=int(input("Introduce el mes:\n"))
        year=int(input("Introduce el año:\n"))
        if (bisiesto(year)==True):
            print("El año indicado es bisiesto\n")

        # El año debe ser mayor a 0
        if year>0:
            # El mes debe ser mayor que cero y menor de 13
                if month>0 and month<13:
                        # El día deberá estar entre 1-31, 1-30 y 1-28 según el mes (no tenemos en cuenta los años bisiestos)
                        if ((month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and (day>0 and day<32)) or ((month==4 or month==6 or month==9 or month==11) and (day>0 and day<31)) or (month==2 and day>0 and day<30 and bisiesto(year)==True) or (month==2 and day>0 and day<29 and bisiesto(year)==False):
                            print("La fecha introducida es correcta.\n")
                            meses = {1: "enero",2: "febrero",3: "marzo",4: "abril",5: "mayo",6: "junio",7: "julio",8: "agosto",9: "septiembre",10: "octubre",11: "noviembre",12: "deciembre"}
                            print(f"Fecha: {day} de {meses[month]} de {year}.\n")
                        # Terminamos el 'Si' de la comprobación de si el día es correcto
                        else:
                            print("ERROR: El día introducido no es posible en el mes indicado.")
                        # Terminamos el 'Si' de la comprobación de si el mes es correcto
                else:
                        print("ERROR: El mes es incorrecto.")

        # Terminamos el 'Si' de la comprobación de si el año es correcto
        else:
            print("ERROR: El año indicado es incorrecto.")


        # preguntamos si se quiere comprobar otra fecha
        otro=input("\n¿Quieres comprobar otra fecha? (s/n)\n")

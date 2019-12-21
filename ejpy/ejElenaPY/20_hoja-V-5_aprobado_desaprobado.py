# Ejercicio 20 (V-5) - Decir si un alumno está o no aprobado según unas condiciones dadas

# Pedimos por pantalla la nota del alumno
nota = float(input("Introduce la nota del alumno (usa el punto para los decimales): "))

# Si la nota es inferior a 12.50 está desaprobado
if nota<12.50:
        print("El alumno está desaprobado.")
elif nota<20:
        print("El alumno está aprobado.")
else:
        print("Error, la nota es superior a 20")

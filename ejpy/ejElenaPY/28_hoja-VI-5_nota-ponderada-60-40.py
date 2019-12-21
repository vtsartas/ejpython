# Ejercicio 28 - Hoja VI (5) - Indicar la nota ponderada según el criterio dado
# (parte teórica 60%, práctica 40%) de cada uno de un número determinado de alumnos

numalumnos=int(input("Introduce el número total de alumnos:\n"))
print("Usa el punto '.' para los decimales")
for contador in range(1,numalumnos+1):
        print(f"\nDatos del alumno número {contador} de {numalumnos}:")
        teorica=float(input("- Introduce la nota de la parte teórica: "))
        practica=float(input("- Introduce la nota de la parte practica: "))
        nota=(teorica*60/100)+(practica*40/100)
        print(f"La nota final del alumno número {contador} es {nota:.2f}.\n")
print("Ya se han calculado todas las notas.")

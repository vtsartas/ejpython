# Ejercicio 10 - Decir si el interesado puede acceder al ciclo formativo pro haber hecho bachillerato o la prueba de acceso.

# Preguntamos por pantalla si se ha realizado el bachillerato
bachiller = str(input("¿Has realizado el bachillerato (s/n)?"))

# Si lo ha realizado indicamos que puede entrar al ciclo
if bachiller=="s":
    print("Puedes acceder al ciclo formativo al contar con el bachillerato.")
# Si no, preguntamos si ha superado la prueba de acceso
else:
    prueba = str(input("¿Has superado la prueba de acceso (s/n)?"))
    if prueba=="s":
        print("Puedes acceder al ciclo formativo al haber superado la prueba de acceso.")
# Si no, no puede ingresar en el ciclo
    else:
        print("No puedes acceder al ciclo formativo al no tenr bachillerato ni haber superado la prueba de acceso.")

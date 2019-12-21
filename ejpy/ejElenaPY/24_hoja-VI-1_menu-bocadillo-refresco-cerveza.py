# Ejercicio 24 - Hoja VI (1) - Indicar importe menú según cantidades consumidas y precios fijos

otro="s"
importe=0
total=0
preciobocadillo=1.50
preciorefresco=1.05
preciocerveza=0.75
    
while otro=="s":
        print("Introduce los artículos consumidos por el cliente:")
        bocadillos=int(input("- Número de bocadillos de jamón:"))
        refrescos=int(input("- Número de refrescos:"))
        cervezas=int(input("- Número de cervezas:"))
        importe=(bocadillos*preciobocadillo)+(cervezas*preciocerveza)+(refrescos*preciorefresco)
        total=total+importe
        texto="El importe para este cliente es {:.2f}.\nEl total acumulado en caja es {:.2f}.\n"
        print(texto.format(importe,total))
        otro = input("¿Quieres introducir datos de una nueva cuenta (s/n)?\n")

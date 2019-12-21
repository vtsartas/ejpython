# Ejercicio 22 (hoja V, 7) - Pedir un número de tres cifras y si lo es invertir el orden de estas

# Pedimos por pantalla el número a verificar
num = int(input("Introduce un número de tres cifras (100 a 999): "))

# Si el número está entre 100 y 999 tendrá 3 cifras y lo pondremos al revés
if num>99 and num<1000:
        # las unidades serán el resto de dividir el número entre 10
        unidades=int(num%10)
        texto="Unidades={}"
        print(texto.format(unidades))
        # las decenas serán el resto de dividir el número menos las unidades entre 100 entre 10
        decenas=int(((num-unidades)%100)/10)
        texto="Decenas={}"
        print(texto.format(decenas))
        # las centenas serán el resto de dividir el número menos las unidades y las decenas entre 100 entre 100
        centenas=int((((num-unidades)-(decenas*10))%1000)/100)
        texto="Centenas={}"
        print(texto.format(centenas))
        
        # el número al revés se obtendra convirtiendo las unidades en centenas, las decenas tal cual y las centenas se dejan como unidades
        numfinal=int((unidades*100)+(decenas*10)+centenas)
        texto="El numero original ({}) al revés es {}."
        print(texto.format(num,numfinal))
else:
        # si el número no tiene 3 cifras lo indicamos
        print("Número incorrecto: tiene más o menos de tres cifras")

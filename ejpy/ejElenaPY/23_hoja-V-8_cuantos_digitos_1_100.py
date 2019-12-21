# Ejercicio 23 (hoja V, 8) - Pedir un número del 1 al 100 y decir cuántos dígitos tiene

# Pedimos por pantalla el número a verificar
num = int(input("Introduce un número del 1 al 100: "))

# Si el número está entre 1 y 100 indicamos cuántos dígitos tiene. Para ello comprobamos el valor de sus centenas y decenas
if num<101:
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
        
        if centenas>0:
                texto="El número {} tiene tres dígitos"
                print(texto.format(num))
        elif decenas>0:
                texto="El número {} tiene dos dígitos"
                print(texto.format(num))
        else:
                texto="El número {} tiene un dígito"
                print(texto.format(num))
else:
# si el número no está entre 1 y 100 o tiene más de 3 dígitos lo indicamos
        if num<1000:
                print("Número incorrecto: aunque tiene 3 dígitos es mayor a 100.")
        else:
            print("Número incorrecto: tiene cuatro dígitos o más.")

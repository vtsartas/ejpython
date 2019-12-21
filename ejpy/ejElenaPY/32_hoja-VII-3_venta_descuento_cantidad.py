# Ejercicio 32 - Hoja VII (3) - Calcular importe según descuento que dependerá de las unidades

# Creamos una función para calcular el importe
def importe(u,p,desc):  
        return (u*(p*((100-desc)/100)))

otro="s"
  
precio=float(input("AVISO: usar el punto para los decimales:\nIntroduce el precio de venta habitual:\n"))
descuento1=float(input("Indica el descuento inicial:\n"))
descunid=int(input("Introduce a partir de cuántas unidades habrá un descuento superior:\n"))
descuento2=float(input(f"Indica el descuento a aplicar si se compran más de {descunid} unidades:\n"))

while otro=="s":
        unidades=int(input("Unidades vendidas:\n"))
        if unidades<descunid:           
                print(f"\nImporte= {importe(unidades,precio,descuento1):.2f} (aplica un {descuento1:.2f}% de descuento).")
        else:
                print(f"\nImporte= {importe(unidades,precio,descuento2):.2f} (aplica un {descuento2:,2f}% de descuento).")
        otro=input("\n¿Quieres ver el importe de una nueva compra del mismo artículo (s/n)\n?")

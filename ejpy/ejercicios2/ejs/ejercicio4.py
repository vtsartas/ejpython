# 4. Programa que lea por teclado tres números enteros H, M, S
# correspondientes a hora, minutos y segundos respectivamente,
# y comprueba si la hora que indican es una hora válida. 

def ejercicio4():
    # iniciamos 'otro4' para que entre en el while
    otro4="s"

    while (otro4=="s"):
        # pedimos la hora
        hora=int(input("Introduce la hora: "))
        mins=int(input("Introduce los minutos: "))
        segs=int(input("Introduce los segundos: "))

        correccion=" no " if not(hora>=0 and hora<24 and mins>=0 and mins<60 and segs>=0 and segs<60) else " "
        print(f"La hora indicada ({str(hora).zfill(2)}:{str(mins).zfill(2)}:{str(segs).zfill(2)}){correccion}es correcta")
    
        # preguntamos si queremos comprobar otra hora
        otro4=str(input("¿Deseas comprobar otra hora (s/n)? "))
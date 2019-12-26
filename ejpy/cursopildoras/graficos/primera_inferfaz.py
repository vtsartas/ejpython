from tkinter import Tk,Frame

raiz=Tk()

raiz.title("Ventana de pruebas 1")
raiz.iconbitmap("favicon.ico")
#raiz.geometry("1000x600") # lo correcto es darle tamaño al frame 
raiz.config(bg="#eeeeff")
# raiz.resizable(0,0)

miFrame=Frame()
miFrame.config(bg="#ddeeff",relief="sunken")
miFrame.config(width="1000", height="600")
#miFrame.pack(side="left",anchor="nw") # empaquetamos el frame dentro de la raiz
#miFrame.pack(expand="True",fill="both")
miFrame.config(cursor="hand2")
miFrame.pack()

raiz.mainloop()
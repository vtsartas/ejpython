from tkinter import Tk,Frame,Label,PhotoImage

root=Tk()

root.title("Ventana de pruebas 2")
root.iconbitmap("favicon.ico")

miFrame=Frame(root,width=500,height=400)
miFrame.pack()

miImagen=PhotoImage(file="logoqmph.png")

#miLabel=Label(miFrame,text="Hola a todos", fg="red",font=("Courier",22))

miLabel=Label(miFrame,image=miImagen)

miLabel.place(x=10,y=10)

root.mainloop()
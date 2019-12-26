from tkinter import Tk,Frame,Entry,Label

root=Tk()

root.title("Ventana de pruebas 2")
root.iconbitmap("favicon.ico")

miFrame=Frame(root,width=1200,height=600)
miFrame.pack()

nomCuadro=Entry(miFrame)
#cuadroTxt1.place(x=50,y=50)
nomCuadro.grid(row=0,column=1,padx=10,pady=10)
nomCuadro.config(fg="red",justify="center")

apellCuadro=Entry(miFrame)
apellCuadro.grid(row=1,column=1,padx=10,pady=10)

passCuadro=Entry(miFrame)
passCuadro.grid(row=2,column=1,padx=10,pady=10)
passCuadro.config(show="*")

direccCuadro=Entry(miFrame)
direccCuadro.grid(row=3,column=1,padx=10,pady=10)

nomLabel=Label(miFrame,text="Nombre:")
#nomLabel.place(x=50,y=50)
nomLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

apellLabel=Label(miFrame,text="Apellido:")
apellLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Contraseña:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

direccLabel=Label(miFrame,text="Dirección de casa:")
direccLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

root.mainloop()
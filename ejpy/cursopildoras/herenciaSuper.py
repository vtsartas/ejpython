class Persona():
    def __init__(self,nombre,edad,Lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.Lugar_residencia=Lugar_residencia

    def descripcion(self):
        print("\nNombre: ",self.nombre," Edad: ",self.edad," Residencia: ",self.Lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario," Antigüedad: ",self.antiguedad)

empleado1=Empleado(1500,15,"Manuel",55,"Colombia")
empleado2=Persona("Pepe",55,"Colombia")

empleado1.descripcion()

if (isinstance(empleado1,Empleado)):
    print("empleado1 es de la clase 'Empleado'")
else:
    print("empleado1 NO es de la clase 'Empleado'")

if (isinstance(empleado1,Persona)):
    print("empleado1 es de la clase 'Persona'")
else:
    print("empleado1 NO es de la clase 'Persona'")

empleado2.descripcion()

if (isinstance(empleado2,Empleado)):
    print("empleado1 es de la clase 'Empleado'")
else:
    print("empleado2 NO es de la clase 'Empleado'")

if (isinstance(empleado2,Persona)):
    print("empleado2 es de la clase 'Persona'")
else:   
    print("empleado2 NO es de la clase 'Persona'")
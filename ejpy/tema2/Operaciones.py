# En Python no hay operadores "++" ni "--" para adición o substracción de 1 a la variable
# La forma abreviada sería "x+=1" y "x*=1". Del mismo modo están "x*=n" (multiplica por 'n'),
# "x/=1" (divide por 'n'), "x%=n" (módulo al dividir por 'n'), "x**=n" (x elevado a n) y
# "x//=n" (el entero más cercano al resultado de dividir x entre n)

class Operaciones():
    # método constructor de la clase 'Operaciones'
    def __init__(self):
        self.__valor=0

    # métodos get/set (propios)

    def asignaval(self,val):
        self.__valor=val
    
    def recuperaval(self):
        return self.__valor
    
    # métodos de operaciones de la clase
    def suma_plusplus(self):
        self.__valor+=1
    def resta_plusplus(self):
        self.__valor-=1
    def multi(self,n2):
        self.__valor*=n2
    def divi(self,n2):
        if (n2>0):
            self.__valor/=n2
        else:
            self.__valor=0
    def resto(self,n2):
        if (n2>0):
            self.__valor%=n2
        else:
            self.__valor=0
    def elevado(self,n2):
        self.__valor**=n2
    def suelo(self,n2):
        if (n2>0):
            self.__valor//=n2
        else:
            self.__valor=0

# creamos un objeto de la clase 'Operaciones()'
num1=Operaciones()
# le damos un valor por teclado mediante 'asignaval()'
num1.asignaval(int(input("Introduce el primer valor: ")))

# mostramos el efecto de los métodos propios suma_plusplus() y resta_plusplus, que hacen el "++"" y el "--"
print("Valor inicial de num1=",num1.recuperaval())
num1.suma_plusplus()
print("Si le aplicamos nuestro método ++ (suma_plusplus()) es ",num1.recuperaval())
num1.resta_plusplus()
print("Si ahora le aplicamos nuestro método -- (resta_plusplus()) es ",num1.recuperaval())

# ahora pediremos un segundo valor y mostraremos el uso del resto de métodos
num2=int(input("Introduce el segundo valor: "))

num1.multi(num2)
print("Al multiplicar num1 por ",num2," obtenemos",num1.recuperaval())

num1.multi(num2)
print("Al dividir num1 por ",num2," obtenemos",num1.recuperaval())

num1.resto(num2)
print("El resto de dividir num1 por ",num2," es ",num1.recuperaval())

# pedimos un nuevo valor para ambos números por si nos quedamos en 0
num1.asignaval(int(input("Introduce el primer valor: ")))
num2=int(input("Introduce el segundo valor: "))

num1.elevado(num2)
print("El resultado de elevar num1 a",num2,"es ",num1.recuperaval())

# pedimos un nuevo valor para ambos números por si nos quedamos en 0
num1.asignaval(int(input("Introduce el primer valor: ")))
num2=int(input("Introduce el segundo valor: "))

num1.suelo(num2)
print("El resultado redondeado a la baja de num1 entre",num2,"es ",num1.recuperaval())
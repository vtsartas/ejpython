# En Python no hay operadores "++" ni "--" para adición o substracción de 1 a la variable
# La forma abreviada sería "x+=1" y "x*=1". Del mismo modo están "x*=n" (multiplica por 'n'),
# "x/=1" (divide por 'n'), "x%=n" (módulo al dividir por 'n'), "x**=n" (x elevado a n) y
# "x//=n" (el XXXXXXXXXXXXX de x entre n)

class Operadores():

    def suma_plusplus(n1):
        n1+=1
        return n1
    def resta_plusplus(n1):
        n1-=1
        return n1
    def multi(n1,n2):
        return n1*n2
    def divi(n1,n2):
        if (n2>0):
            return n1/n2
        else:
            return 0
    def resto(n1,n2):
        if (n2>0):
            return n1%n2
        else:
            return 0
    def elevado(n1,n2):
        return n1**n2
    def suelo(n1,n2):
        if (n2>0):
            return n1//n2
        else:
            return 0

num1=int(input("Introduce el primer valor: "))
num2=int(input("Introduce el segundo valor: "))

print(num1,"++ es ",suma_plusplus)
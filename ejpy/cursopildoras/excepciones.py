def sumar(op1,op2):
    return op1+op2

def restar(op1,op2):
    return op1-op2

def muliplicar(op1,op2):
    return op1*op2

def divide(op1,op2):
    try:
        return op1/op2    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación erronea"

while True:
    try:
        ope1=int(input("1er operador: "))
        ope2=int(input("2o operador: "))
        break
    except ValueError:
        print("Los valores introducidos no sin correctos. Inténtalo de nuevo")

operacion=input("Indica la operación a realizar: ")

if operacion=="suma":
    print(sumar(ope1,ope2))
elif operacion=="resta":
    print(restar(ope1,ope2))
elif operacion=="multiplica":
    print(muliplicar(ope1,ope2))
elif operacion=="dividir":
    print(divide(ope1,ope2))
else:
    print("operación erronea")


def divide2():
    try:
        op1=(float(input("Introduce el 1er valor")))
        op2=(float(input("Introduce el 2o valor")))
        print(f"La división es {str(op1/op2)}")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except ValueError:
        print("El valor introducido es erróneo")
    finally:
        print("Cálculo finalizado")
divide2()
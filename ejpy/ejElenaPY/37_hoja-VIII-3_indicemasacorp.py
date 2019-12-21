# Ejercicio 37 - Hoja VIII (3) - Calcular el IMC según la edad, peso y estatura dadas

# En esta función calculamos el IMC (pasamos los centímetros a metros)
def imccalc (p1,e1):
        return (p1/(e1*e1/10000))

# Función que devuelve un texto sobre lo que indica el IMC según el peso
def imcpeso (imc1):
        if imc1<18.5:
                texto="Se considera que tu peso es INFERIOR al normal."
        if imc1>=18.5 and imc1<25:
                texto="Se considera que tu peso es NORMAL."
        if imc1>=25 and imc1<30:
                texto="Se considera que tu peso es SUPERIOR al normal."
        if imc1>=30:
                texto="Sería indicativo de una posible OBESIDAD."
        return texto

# Función que devuelve un texto sobre lo que indica el IMC según la edad
def imcedad (imc2,e):
        if ((e>=19 and e<25) and (imc2>=19 and imc2<=24)) or ((e>=25 and e<35) and (imc2>=20 and imc2<=25)) or ((e>=35 and e<45) and (imc2>=21 and imc2<=26)) or ((e>=45 and e<55) and (imc2>=22 and imc2<=27)) or ((e>=55 and e<65) and (imc2>=23 and imc2<=28)) or ((e>=65) and (imc2>=24 and imc2<=29)):
                text="tu peso es normal."
        else:
                text="tu peso NO se considera normal."
        return text

otro="s"
while otro=="s":
        edad=int(input("Introduce tu edad:\n"))
        estatura=float(input("Introduce tu altura en centímetros:\n"))
        peso=float(input("Introduce tu peso (en Kg, usa el punto . para los decimales):\n"))

        print(f"\nTu IMC es {imccalc(peso,estatura):.2f}. {imcpeso(imccalc(peso,estatura))}")
        print(f"Para tu edad ({edad} años) e IMC, {imcedad(imccalc(peso,estatura),edad)}\n") 

        otro=input("¿Deseas calcular el IMC de otra persona (s/n)?\n")

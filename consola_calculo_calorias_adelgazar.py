import calculadora_indices as calc
def nivelDePeso(IMC):
    if IMC <16.00:
        return("Delgadez severa")
    elif 16.00 <= IMC <= 16.99:
        return("Delgadez moderada")
    elif 17.00 <= IMC <= 18.49:
        return("Delgadez aceptable")
    elif 18.5 <= IMC <= 24.99:
        return("Peso normal")
    elif 25.00 <= IMC <= 29.99:
        return("Sobrepeso")
    elif 30.00 <= IMC <= 34.99:
        return("Obesidad tipo I")
    elif 35.00 <= IMC <= 39.99:
        return("Obesidad tipo II")
    elif 40.00 <= IMC <= 49.99:
        return("Obesidad tipo III")
    elif IMC >= 50.00:
        return("OBESIDAD")

peso = float(input("peso de la persona en (Kg): "))
altura = float(input("altura de la persona en (m):"))
print ("Su nivel de peso es: ", nivelDePeso(calc.calcular_IMC(peso,altura)))


import random  # sentencia que nos ayuda a tener la docs rondom.


def adivina_el_numero(x): # Es una funcion ..

    print("===========================")
    print("  !You welcom to the game.")
    print("===========================")
    print("Tu meta es adivinar el numero generado por la PC")

    numero_aleatorio = random.randint(1, x) # numero aleatorio entero "random.randint" entre 1 y x

    posible_numero = 0 # Es la prediccion del posible numero.

    while posible_numero != numero_aleatorio: # Se utiliza el ciclo while ya que no sabemos cuantas veces se debe repetir.
        posible_numero = int(input(f"Adivina un numero entre 1 y {x}: ")) # Aqui se pide que adivne un numero entre 1 y x


        if posible_numero < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño.")
        elif posible_numero > numero_aleatorio:
            print("Intenta otra vez. Este numero en muy grande")
            
    print("!Felicitaciones! Adivinastes el numero correctamente: ")


adivina_el_numero(10) # Este es el llamado a la funcion 

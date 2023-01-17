import random


def adivina_el_num_pc(x): # x es el limite superior del intervalo


    print("==============================")
    print("       ! You welcom! ")
    print("==============================")
    print(f"Selecciona un numero entre 1 y {x} para que la PC intente adivinarlo...")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        # Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # tambien podria ser el limite_superior.

        respuesta = input(f"Mi prediccion es {prediccion}. Si el numero es muy baja, ingresa (b). Si el numero es muy alta ingresa (a). Si es correcta,ingresa (c)").lower()

        if respuesta == "a":
            limite_superior = prediccion -1
        elif respuesta == "b":
            limite_inferior = prediccion +1

    print(f"La computadora adivino tu numero correctamente: {prediccion}")

adivina_el_num_pc(10)  
# intervalo inicial :(1, 10), limite _inferio = 1, limite-superior = 10
# posible prediccion: 6 
# respuest : "a"
# se cambia el intervalo de (7, 10)
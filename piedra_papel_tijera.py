import random


def jugar():
    usuario = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel y 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi','pa','ti']) # random.choice, es para que la computadora de forma aleatoria escoga una de las tre opciones.
    if usuario == computadora:
        return "!Empate"
    if gano_el_jugador(usuario, computadora):
        return "!Ganastes"
    return "!Perdistes"

def gano_el_jugador(jugador, oponente):
    # Esta funcion retorna True, si gana el jugador.
    # Piedra gana a tijera (pi > ti)
    # tijera gana a papel (ti > pa)
    # papel gana a piedra (pa > pi)
    if ((jugador == 'pi' and oponente == 'ti') or (jugador == 'ti' and oponente == 'pa') or (jugador == 'pa' and oponente == 'pi')): # utilizo doble parentecis para poder dividir las lineas en varias lineas. 
        return True
    else:
        return False


print(jugar())      
       


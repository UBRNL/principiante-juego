import random # buqueda aleatoria 
import time # tiempo de la busqueda


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo, limite_inferior = None, limite_superior = None):
    if limite_inferior is None:
        limite_inferior = 0 

    if limite_superior is None:
        limite_superior = len(lista) -1

    if limite_superior < limite_inferior:
        return -1

    punto_medio = (limite_inferior + limite_superior) // 2
    ## esto nos sumara limite inferior mas limite superior
    # y lo divide en tre 2 y nos retorna un numero entero.
    # lista C, limite inferio = 0, limite superior = 4
    # punto medio es = (0 + 4) = 4 ( 4/2) = 2  nos retornaria el numero 3

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio -1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio +1, limite_superior)

    if _name_=="_main_": # Crear una lista ordenada con 10000 numeros aleatorios

       tamaño = 100
       conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
        lista_ordenada = sorted(lista(conjunto_inicial))
        # medir el tiempo de busqueda ingenua.
        inicio = time.time()
        for objetivo in lista_ordenada:
            busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")
    # medir el tiempo de busqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")

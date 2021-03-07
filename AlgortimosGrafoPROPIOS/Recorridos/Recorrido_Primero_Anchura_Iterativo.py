##################################################################################
# TITLE: Recorrido Primero en Anchura (Breadth First Search)
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION: Utiliza Lista abierta de tipo Cola (FIFO)
#              Utilizamos Lista de adyacencia para representar Grafo (Diccionario)
##################################################################################
from collections import deque

#Paso 1: Definimos el Grafo mediante un Diccionario

grafo={
        "A":["B","C","D"],
        "B":["E","F"],
        "C":["A","C","G"],
        "D":["A","E"],
        "E":["B","D","I"],
        "F":["B","C","G","H","I"],
        "G":["C","F","I"],
        "H":["F","G","I"],
        "I":["E","F","H"]}
#Paso 2: Implementamos el Algoritmo
def bfs_non_recursive(grafo,inicio):
    if inicio is None or inicio not in grafo:
        return "invalid input"

    recorrido = []
    lista_abierta=deque()
    lista_abierta.append(inicio)

    while(len(lista_abierta) != 0):
        s=lista_abierta.pop()#Sacamos por la derecha
        if s not in recorrido:
            recorrido.append(s)
            if s not in grafo:
                #Nodo hoja
                continue
            for vecino in grafo[s]:
                lista_abierta.appendleft(vecino)#Metemos por la izquierda
        else:
            continue

    return " ".join(recorrido)

#Paso 3: Probamos el Algortimo
BFS_recorrido=bfs_non_recursive(grafo,"A")
print(BFS_recorrido)
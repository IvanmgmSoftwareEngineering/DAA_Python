############################################
# TITLE: Recorrido Primero en Profundidad (Deep First Search)
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION: Utiliza Lista abierta de tipo Pila (LIFO)
#              Utilizamos Lista de adyacencia para representar Grafo (Diccionario)
############################################
from collections import deque

#Paso 1: Definimos el Grafo mediante un Diccionario

grafo={
        "A":["D","C","B"],
        "B":["F","E"],
        "C":["D","C","A"],
        "D":["E","A"],
        "E":["I","D","B"],
        "F":["I","H","G","C","B"],
        "G":["I","F","C"],
        "H":["I","G","F"],
        "I":["H","F","E"]}
#Paso 2: Implementamos el Algoritmo
def dfs_non_recursive(grafo,inicio):
    if inicio is None or inicio not in grafo:
        return "invalid input"

    recorrido = []
    lista_abierta=deque()
    lista_abierta.append(inicio)

    while(len(lista_abierta) != 0):
        s=lista_abierta.popleft() #Sacamos por la iquierda
        if s not in recorrido:
            recorrido.append(s)
            if s not in grafo:
             #Nodo hoja
             continue
            for vecino in grafo[s]:
               lista_abierta.appendleft(vecino)#Metemos por la ziquierda
        else:
            continue

    return " ".join(recorrido)

#Paso 3: Probamos el Algortimo
DFS_recorrido=dfs_non_recursive(grafo,"A")
print(DFS_recorrido)

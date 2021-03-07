#Recorrido Primero en Profundidad (DFS=Depth First Search)
#Versión iterativa
#Primero en Profundidad=> Lista de tipo PILA (LIFO)

from collections import deque


def bfsAux(grafo,visited,vertice):
    #Implementamos una Lista de tipo FIFO = COLA
    cola=deque() #Bicola: es una cola que se pueden hacer insercciones y borrados por el principio y por el final
    #Marcamos el nodo como visitado
    visited[vertice]=True
    print(vertice,end=" ")
    #Metemos el Nodo en la cola
    cola.append(vertice)
    while cola:
        aux=cola.popleft()#saco de la cola el Nodo 1
        for vertice_adyacente in grafo[vertice]:
            if not visited[vertice]:
                visited[vertice_adyacente] = True
                print(vertice_adyacente, end =" ")
                cola.append(vertice_adyacente)
def dfs_iterativo (grafo):
    n=len(grafo)
    visited = [False] * n

    for vertice in range (1,n):#Límite inferior siempre inclusivo y el límite superior se excluye
        if not visited[vertice]:
            bfsAux(grafo,visited,vertice)
#Hemos utilzado una Pila FIFO
#Lo implementamos de forma iterativa
#Paso 1: Definimos el Grafo
    #Una lista de listas se indexa como un array
    #grafo[0]=[] lista vacía
    #grafo[3]=[2,4,5]
    #grafo[4][2]=3
grafo=[
      [],
      [2,4,8],# El vertice 1 está conectado a los vértices 2, 4 y 8
      [1,3,4],# El vertice 2 está conectado a los vértices 1, 3 y 4
      [2,4,5],# El vertice 3 está conectado a los vértices 2, 4 y 5
      [1,2,3,7],# El vertice 4 está conectado a los vértices 1, 2, 3 y 7
      [3,6],# El vertice 5 está conectado a los vértices 3 y 6
      [5,7],# El vertice 6 está conectado a los vértices 5 y 7
      [4,6,9],# El vertice 7 está conectado a los vértices 4, 6 y 9
      [1,9],# El vertice 8 está conectado a los vértices 1 y 9
      [7,8] # El vertice 9 está conectado a los vértices 7 y 8
      ]

#Probamos
dfs_iterativo(grafo)
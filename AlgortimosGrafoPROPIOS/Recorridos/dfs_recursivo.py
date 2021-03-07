#Recorrido Primero en Profundidad (DFS=Depth First Search)
#Versión Recursiva

#Implementamos el recorrido en Profundidad de forma recursiva
#Marcamos cada elemento visitado y para elemento no visitado llamamos a una función recursiva
#visited es un array con los nodos visitados = Lista Cerrada
#Hemos utilzado una Pila LIFO
#Lo implementamos de forma recursiva
def dfsRec(grafo, visited, vertice):
    visited[vertice] = True
    print(vertice,end =" ")
    for vertice_adyacente in grafo[vertice]:
        if not visited[vertice_adyacente]:
            dfsRec(grafo,visited,vertice_adyacente)
def dfs(grafo):
    n=len(grafo)#devuelve 10, len(grafo[4]) devuelve 4
    visited = [False]*n #Crea un array de tamoño n con elementos todos con valor FALSE
    for vertice in range(1,n): #El primero (1) es inclusivo y el ultimo (n) es exclusivo
        if not visited[n]:     #Este bucle me hace que revisemos aquellos nodos que aún están por visitar, y controla si el grafo no es conexo (nodos sumidero o trampa)
            dfsRec(grafo, visited, vertice)

#Paso 1: Definimos el Grafo
    #Una lista de listas se indexa como un array
    #grafo[0]=[] lista vacía
    #grafo[3]=[2,4,5]
    #grafo[4][2]=3
grafo=[
      [], #Lista vacia ¿Para?
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
dfs(grafo)
#¿Alguien detecta algún problema en esta implementación recursiva? Con un Grafo con muchos nodos, las llamadas recursivas se producirá un Stack Over flow.
#Es recomendable implementar el Recorrido Primera en Profundidad de forma Iterativa
#Además es interesante intentar optimizar esta implementación
#Complejidad:
#- Se recorren todos los nodos
#- Se recorren todas las Aristas
#La compleidad vendrá determinada por el máximo de entre el Número de nodos y el Número de Aristas. Normalmente el número de arcos es siempre mayor que el número de Nodos
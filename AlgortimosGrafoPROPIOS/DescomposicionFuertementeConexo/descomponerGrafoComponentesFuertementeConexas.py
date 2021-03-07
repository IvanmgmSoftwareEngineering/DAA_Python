############################################
# TITLE: Descomposición de un grafo en sus compenentes fuertemente conexas
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 07th March
# DESCRIPTION: Dado un Grafo (G),
#              Paso 1) Aplicamos ordenación topologíca sobre (grafo)
#              Paso 2) Obtenemos el Grafo Traspuesto (grafoTraspuesto)
#              Paso 3) Aplicamos búsqueda en profundidad sobre (grafoTraspuesto),
#                      iniciando la búsqueda en los nodos de mayor a menor tiempo
#                      de finalización obtenidos en la primera ejecución de búsqueda
#                      en profundidad
#               El reusultado será un bosque de árboles. Cada árbol será una componente
#               fuertemente conexo
############################################
#Primero: definimos el grafo sin ciclos
grafo={
        "calcetines":["zapatos"],
        "zapatos":[],
        "pantalon":["zapatos","cinturon"],
        "cinturon":[],
        "camisa":["cinturon","jersey"],
        "jersey":[],}
#Segundo: empezamos con cada uno de los pasos
#   Paso 1) Aplicamos ordenación topologíca sobre (grafo)
from collections import deque
def topSortVisit(data,u):
    #Lo primero que haremos es marcar el nodo como visitado
    data["state"][u]="VISITED"
    # Empezamos el marcado a gris, es decir, en d de todos los nodos y almacenamos el orden en que los visitamos
    data["time"]=data["time"]+1
    data["d"][u]=data["time"]
    for adyacentes in data["graph"][u]: #En la variable adyacentes se van guardando los valores de una determinada clave del grafo, es decir, los nodos adyacentes al nodo "u"
        if data["state"][adyacentes] == "NOT VISITED":
            data["parent"][adyacentes]=u
            topSortVisit(data,adyacentes) # Llamada recursiva para repetir el proceso hasta que todos los nodos estén etiquetados como "VISITED"
    data["state"][u] = "FINISH" #Etiquetamos con FINISH al último Nodo visitado y esto marcará el final del marcado en gris
    #Empezamos el marcado a negro, es decir, en f de todos los nodos y almacenamos el orden en que los visitamos
    data["time"] = data["time"] +1
    data["f"][u] = data["time"]
    data["list"].appendleft(u)#Almacenamos en la solución

def topSort(grafo):
    n=len(grafo)
    data={ #Creo una estructura de datos y lo utilizo a modo de registro.
          # Meto toda la info. relevante en la estrucutra de datos creada de forma propia llamada DATA
          # Me creo un Diccionario vacío dentro de Data, en state
        "graph": grafo, #El grafo con toda la información de la que dispongo
        "state":dict(), #Diccionario vacío
        "parent":dict(), #Diccionario vacio donde almaceno la info del Padre de cada Nodo, es decir, para cada nodo debemos saber quien es el padre. ¿Y si un Nodo tiene dos Padres? Por eso la Ordenación topológica no es única, tomamos como el padre de un Nodo al primer nodo Padre que encuentre
        "d":dict(), #Vector que contiene los números que me permiten etiquetar los nodos de gris (lo que está izquierda de la barra). Decimos que es un vector porque cada elemento del Diccionario tendrá un único elemento y será un entero
        "f": dict(),  # Vector que contiene los números que me permiten etiquetar los nodos de negro (lo que está derecha de la barra). Decimos que es un vector porque cada elemento del Diccionario tendrá un único elemento y será un entero
        "time": 0, #time lo utilizamos para marcar el paso por cada Nodo (Paso 1, 2, 3 ,4,...
        "list":deque() #En esta lista es la que me almacena la ordenación Topológica. La implementaremos con una Bicola
    }

    for k in grafo.keys():# La función keys() devuelve las claves del Diccionario en forma de un Iterable. Notar que las claves del Diccionario Grafo son cada uno de los nodos del Grafo (ni uno más ni uno menos)
    #INICIALIZAMOS
        #Inicializo el diccionario "state" todo a no visitado
        data["state"][k]="NOT VISITED" #Indexamos el Diccionario "state" por la clave que es el nombre del Nodo
        #Inicializo el diccionario "parent" todo a NULL
        data["parent"][k] = None
        #Inicializo vector d
        data["d"][k]=0
        # Inicializo vector d
        data["f"][k]=0

    #Empezamos con la parte del Recorrido (Muy similar al Recorrido Primero en Profundidad)
    for k in grafo.keys():
        if data["state"][k] == "NOT VISITED": #Si se cumple esta condición empezamos el recorrido
            topSortVisit(data,k)
    return data["list"]
def aplicamosOrdenacionTopologica(grafo,list):
    grafoOdenadoTopologicamente=dict()
    for i in range(0,len(list)):
        grafoOdenadoTopologicamente[list[i]]=grafo[list[i]]
    return grafoOdenadoTopologicamente

#   Paso 2) Obtenemos el Grafo Traspuesto (grafoTraspuesto)
def calculaGrafoTraspuesto (grafo):
    grafoTraspuesto=dict()
    for i in grafo.keys():
        grafoTraspuesto[i]=[]
    for i in grafo.keys():
        for j in range(0,len(grafo[i])):
            for k in grafo.keys():
                if k not in grafo[i] and k!=i and k not in grafoTraspuesto[i]:
                    grafoTraspuesto[i].append(k)
    return grafoTraspuesto

#   Paso 3) Aplicamos búsqueda en profundidad sobre (grafoTraspuesto),
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
    return recorrido




#Resultados
listaOdenTopologico=topSort(grafo)
print(listaOdenTopologico)
grafoOdenadoTopologicamente=aplicamosOrdenacionTopologica(grafo,listaOdenTopologico)
print(grafoOdenadoTopologicamente)
grafoTraspuesto=calculaGrafoTraspuesto(grafoOdenadoTopologicamente)
print(grafo)
print(grafoTraspuesto)
DFS_recorrido=dfs_non_recursive(grafoTraspuesto,"camisa")
print(DFS_recorrido)
DFS_recorrido_inverso=[]
DFS_recorrido_inverso=DFS_recorrido[::-1]
print(DFS_recorrido_inverso)

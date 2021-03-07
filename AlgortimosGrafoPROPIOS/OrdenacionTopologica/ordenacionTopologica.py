##################################################################################
# TITLE: Búsqueda Topológica
# AUTHOR: Iván Martín Gómez
# DATE: Miércoles 03th February
# DESCRIPTION: La Búsqueda topológica se descompone en dos partes:
#              Parte 1: Exploración Topológica
#              Parte 2: Búsqueda Topológica utilizando la Exploración usada en la Parte 1
# Objetivo de este problema:
#   Objetivo 1: utilizar el Recorrido Primero en profundidad para ordenar
#   Objetivo 2: familiarizarnos con los diccionarios
#
##################################################################################
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
    print(data["list"])
    return data["list"]
def aplicamosOrdenacionTopologica(grafo,list):
    grafoOdenadoTopologicamente=dict()
    for i in range(0,len(list)):
        grafoOdenadoTopologicamente[list[i]]=grafo[list[i]]
    return grafoOdenadoTopologicamente
grafo={
        "calcetines":["zapatos"],
        "zapatos":[],
        "pantalon":["zapatos","cinturon"],
        "cinturon":[],
        "camisa":["cinturon","jersey"],
        "jersey":[],}

listaOdenTopologico=topSort(grafo)
grafoOdenadoTopologicamente=aplicamosOrdenacionTopologica(grafo,listaOdenTopologico)
print(grafo)
print(grafoOdenadoTopologicamente)

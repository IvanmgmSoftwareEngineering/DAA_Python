############################################
# TITLE: Grafo Traspuesto
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 06th March
# DESCRIPTION: Dado un Grafo (grafo),
#              obtiene el Grafo Traspuesto (grafoTraspuesto)
############################################
#Paso 1: Definimos el Grafo mediante un Diccionario
grafo={
        "A":["D","C","B"],
        "B":["F","E"],
        "C":["D","E","A"],
        "D":["E","A"],
        "E":["I","D","B"],
        "F":["I","H","G","C","B"],
        "G":["I","F","C"],
        "H":["I","G","F"],
        "I":["H","F","E"]}
print(grafo)
#Paso 2: Implementamos el Algoritmo
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

grafoTraspuesto=calculaGrafoTraspuesto(grafo)
print(grafoTraspuesto)
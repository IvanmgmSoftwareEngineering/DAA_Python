'''
Title: ORDENACION POR INSERCCIÓN DIRECTA O(n^2) Cuadrática
Date: Feb 13, 2021
Autor: IvanMGM
'''
#Teoría general Algortimos
#    - Complejidad: O(1)<<O(log(n))<<O(n)<<O(nlog(n))<<O(n^2)<<O(n^3)<<...<<O(a^n)
#    - Constante<<Logarítmica<<Lineal<<Casi Lineal<<Cuadrática<<Cúbica<<...<Exponencial
#---------------------------------------------------------------------------------------
#Es una forma muy natutal de ordenar para los humanos. Se puede utilizar para ordenar un mazo de cartas
#Funcionamiento: Se toma un conjunto ordenado que empieza teniendo un único elemento (por eso afirmamos que es ordenado)
# Se aumenta uno a uno el conjunto introduciendolo en el conjunto de forma ordenada.

#---------------------------------------------------------------------------------------
def insercionDirecta(lista,tam):
    for i in range(1,tam):
        v=lista[i]
        j=i-1
        while j >= 0 and lista[j] > v:
            lista[j+1] = lista[j]
            j=j-1
        lista[j+1]=v

def imprimeLista(lista,tam):
    for i in range(0,tam):
        print lista[i]

def leeLista():
    lista=[]
    cn=int(raw_input("Cantidad de numeros a ingresar: "))

    for i in range(0,cn):
        lista.append(int(raw_input("Ingrese numero %d : " % i)))
    return lista

A=leeLista()
insercionDirecta(A,len(A))
imprimeLista(A,len(A))

'''
Title: ORDENACION BURBUJA (BUBBLE SORT) O(n^2) Cuadrática
Date: Feb 13, 2021
Autor: IvanMGM
'''

#Teoría general Algortimos
#    - Complejidad: O(1)<<O(log(n))<<O(n)<<O(nlog(n))<<O(n^2)<<O(n^3)<<...<<O(a^n)
#    - Constante<<Logarítmica<<Lineal<<Casi Lineal<<Cuadrática<<Cúbica<<...<Exponencial
#---------------------------------------------------------------------------------------
#Funcionamiento: Es un sencillo algortimo de ordenacion. Este algortimo recibe su nombre por el modo en que
#suben los elementos por la lista a medida que son ordenados.
#Recorre la lista, comparando cada elemento con el siguiente.
#En caso de ser el elemento actual menor que el siguiente, los intercambia de posición.
#Es necesario recorrer varias veces la lista hasta que no se necesiten más intecambios
#---------------------------------------------------------------------------------------

def ordenamientoBurbuja(lista,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j] > lista[j+1]):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k;
 
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
ordenamientoBurbuja(A,len(A))
imprimeLista(A,len(A))
'''
Title: ORDENACION MONTÍCULOS (HEAP SORT) O(nlog(n)) Casi Lineal
Date: Feb 13, 2021
Autor: IvanMGM
'''

#Teoría general Algortimos
#    - Complejidad: O(1)<<O(log(n))<<O(n)<<O(nlog(n))<<O(n^2)<<O(n^3)<<...<<O(a^n)
#    - Constante<<Logarítmica<<Lineal<<Casi Lineal<<Cuadrática<<Cúbica<<...<Exponencial
#---------------------------------------------------------------------------------------
#Este algortimo es no recursivo y no estable
#Funcionamiento: Se almacenan todos los elementos del vector a ordenar en un montículo
# y luego extraer el nodo que queda como raíz (cima) en sucesivas iteraciones, obteniendo el conjunto ordenado.
#---------------------------------------------------------------------------------------
def heapsort(lista,tam):
    for k in range(tam-1,-1,-1):
        for i in range(0,k):
            item=lista[i]
            j=(i+1)/2
            while j>=0 and lista[j]<item:
                lista[i]=lista[j]
                i=j
                j=j/2
            lista[i]=item
        temp=lista[0];
    lista[0]=lista[k];
    lista[k]=temp;
 
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
heapsort(A,len(A))
imprimeLista(A,len(A))

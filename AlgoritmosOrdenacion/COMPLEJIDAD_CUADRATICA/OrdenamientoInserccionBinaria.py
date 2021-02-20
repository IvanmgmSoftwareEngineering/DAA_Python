'''
Title: ORDENACION POR INSERCCIÓN BINARIA O(n^2) Cuadrática
Date: Feb 13, 2021
Autor: IvanMGM
'''
#Teoría general Algortimos
#    - Complejidad: O(1)<<O(log(n))<<O(n)<<O(nlog(n))<<O(n^2)<<O(n^3)<<...<<O(a^n)
#    - Constante<<Logarítmica<<Lineal<<Casi Lineal<<Cuadrática<<Cúbica<<...<Exponencial
#---------------------------------------------------------------------------------------
#Funcionamiento: 

#---------------------------------------------------------------------------------------

def insercionBinaria(lista,tam):
    for i in range(1,tam):
        aux=lista[i]
        izq=0
        der=i-1
        while izq<=der:
                m=(izq+der)/2
                if aux < lista[m]:
                        der=m-1
                else:
                        izq=m+1
 
        j=i-1
        while j>=izq:
                lista[j+1]=lista[j]
                j=j-1
        lista[izq]=aux
 
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
insercionBinaria(A,len(A))
imprimeLista(A,len(A))
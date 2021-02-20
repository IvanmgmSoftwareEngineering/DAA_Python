'''
Title: Busqueda Lineal O() 
Date: Feb 13, 2021
Autor: IvanMGM
'''
#Teoría general Algortimos
#    - Complejidad: O(1)<<O(log(n))<<O(n)<<O(nlog(n))<<O(n^2)<<O(n^3)<<...<<O(a^n)
#    - Constante<<Logarítmica<<Lineal<<Casi Lineal<<Cuadrática<<Cúbica<<...<Exponencial
#---------------------------------------------------------------------------------------
#Este algortimo es NO Informado o Ciego (NO maneja una heurística)
#Es necesario que la lista este ordenada
#Funcionamiento: 
#---------------------------------------------------------------------------------------

def busqueda_lineal(lista, x):
    """ Búsqueda lineal.
    Si x está en lista devuelve su posición en lista, de lo
    contrario devuelve -1.
    """

    # Estrategia: se recorren uno a uno los elementos de la lista
    # y se los compara con el valor x buscado.
    i=0 # i tiene la posición actual en la lista, comienza en 0

    # el ciclo for recorre todos los elementos de lista:
    for z in lista:
    # estamos en la posicion i, z contiene el valor de lista[i]

    # si z es igual a x, devuelve i
        if z == x:
            return i

    # si z es distinto de x, incrementa i, y continúa el ciclo
    i=i+1

# si salió del ciclo sin haber encontrado el valor, devuelve -1
    return -1
'''
Title: Busqueda Binaria O() 
Date: Feb 13, 2021
Autor: IvanMGM
'''
#Teoría general Algortimos
#    - Complejidad: O(1)<<O(log(n))<<O(n)<<O(nlog(n))<<O(n^2)<<O(n^3)<<...<<O(a^n)
#    - Constante<<Logarítmica<<Lineal<<Casi Lineal<<Cuadrática<<Cúbica<<...<Exponencial
#---------------------------------------------------------------------------------------
#Este algortimo es NO Informado o Ciego (NO maneja una heurística)
#Es necesario que la lista este ordenada
#Funcionamiento: Utiliza el Diseño de Divide y Venceras
#---------------------------------------------------------------------------------------


def busquedaBinaria(unaLista, item):
        primero = 0
        ultimo = len(unaLista)-1
        encontrado = False
    
        while primero<=ultimo and not encontrado:
            puntoMedio = (primero + ultimo)//2
            if unaLista[puntoMedio] == item:
                encontrado = True
            else:
                if item < unaLista[puntoMedio]:
                    ultimo = puntoMedio-1
                else:
                    primero = puntoMedio+1
    
        return encontrado
    
listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busquedaBinaria(listaPrueba, 3))
print(busquedaBinaria(listaPrueba, 13))
'''
Title: Busqueda Secuencial O() 
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
def busquedaSecuencial(unaLista, item):
        pos = 0
        encontrado = False
    
        while pos < len(unaLista) and not encontrado:
            if unaLista[pos] == item:
                encontrado = True
            else:
                pos = pos+1
    
        return encontrado
    
listaPrueba = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(busquedaSecuencial(listaPrueba, 3))
print(busquedaSecuencial(listaPrueba, 13))
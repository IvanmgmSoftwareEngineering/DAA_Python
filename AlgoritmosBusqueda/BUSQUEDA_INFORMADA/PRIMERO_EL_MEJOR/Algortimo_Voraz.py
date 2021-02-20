'''
Title: Busqueda Voraz o Greedy O()) 
Date: Feb 13, 2021
Autor: IvanMGM
'''
#Teoría general Algortimos
#    - Complejidad: O(1)<<O(log(n))<<O(n)<<O(nlog(n))<<O(n^2)<<O(n^3)<<...<<O(a^n)
#    - Constante<<Logarítmica<<Lineal<<Casi Lineal<<Cuadrática<<Cúbica<<...<Exponencial
#---------------------------------------------------------------------------------------
#Este algortimo esta dentro de la familia de algortimos Búsqueda Primero el Mejor
#Este algortimo es informado (maneja una heurística)
#Elementos:
'''
Conjunto de candidatos: candidates_set
Conjunto de candidatos selecionados: candidates_selected_set
Función solución: Comprueba si un conjunto de candidatos seleccionados es una solución válida. Represetada mediante is_solution()
Función selección: Selecciona el candidato más prometedor del conjunto de candidatos. Representada mediante: select()
Función de factibilidad: Comprueba que el conjunto de candidatos seleccionados se puede expandir añadiendo un candidato seleccionado. Representada mediante: feasible()
Función objetivo: Función que asocia un valor a una solución de nuestro algoritmo devorador, y que queremos minimizar o maximizar (optimizar) según nuestro objetivo.
Objetivo: Minimizar, maximizar.
'''
#Características:
'''
El candidato más prometedor, puede ser no único.
Una vez elegido un candidato, nunca más vuelve a ser procesado.
Puede que la solución no exista o no pueda ser encontrada.
Aunque se encuentre una solución, puede que no sea la más óptima.
Se emplean normalmente en problemas de optimización.
'''
#Funcionamiento: 
#---------------------------------------------------------------------------------------
def greedy(candidates_set):

    candidates_selected_set = None

    while not is_solution(candidates_selected_set) and candidates_set:
        
        candidate_selected = select(candidates_set)
        candidates_set.remove(candidate_selected)
        
        if feasible(candidates_selected_set, candidate_selected):
            
            candidates_selected_set.append(candidate_selected)
     
    return candidates_selected_set   


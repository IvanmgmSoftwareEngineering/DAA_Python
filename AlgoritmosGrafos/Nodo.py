'''
Created on Feb 13, 2021

@author: IvanMGM
'''

''' Clase que representa un Nodo del Grafo '''
class Nodo:
    '''Constructor clase Nodo'''
    def __init__ (self,Nombre,Valor,esNodoInicial,esNodoHoja,Hijos):
        self.Nombre=Nombre
        self.Valor=Valor
        self.esNodoInicial=esNodoInicial
        self.esNodoHoja=esNodoHoja
        self.Hijos=Hijos
        



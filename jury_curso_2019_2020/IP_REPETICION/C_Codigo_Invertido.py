############################################
# TITLE: Código Invertido
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: N : número a invertir
#   Salida 1: número de cifras que tiene el numero
#   Salida 2: número invertido
############################################
import array
from collections import deque

import numpy as np

N=input()
longitud=str(len(N))
N_invertida=N[::-1]
print (longitud + " "+ N_invertida)

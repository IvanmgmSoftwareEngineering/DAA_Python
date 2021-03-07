############################################
# TITLE: Euclides niño prodigio
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: C: número de parejas de números que se recibirán
#   Entrada 2: M y N: pareja de nñumeros
#   Salida: MCD
############################################
from collections import deque

def maximo_comun_divisor_recursivo (m,n):
    r=m%n
    if r==0:
        return n
    else:
        return maximo_comun_divisor_recursivo(n,r)

C=int(input())
vector_MCD_s=deque()
for i in range(1,C+1):
    M, N = map(int, input().strip().split())
    MCD=maximo_comun_divisor_recursivo(int(M),int(N))
    vector_MCD_s.append(MCD)
for i in range(0,len(vector_MCD_s)):
    print(vector_MCD_s[i])

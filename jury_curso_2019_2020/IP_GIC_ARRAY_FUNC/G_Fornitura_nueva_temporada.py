############################################
# TITLE: Fornitura nueva temporada
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: N: número de jugadores
#   Entrada 2: M: puntiación jugador 1
#   Entrada 3: M: puntiación jugador 1
#   ...
#   Entrada N+1: M: puntiación jugador N
#   Salida: nombre de lo potros en mayúscula
############################################
N=int(input())
matriz=[]
indice_menor=0
puntuacion_menor=100000
for i in range(N):
    matriz.append(int(input()))
for i in range(N):
    if puntuacion_menor>matriz[i]:
        puntuacion_menor=matriz[i]
        indice_menor=i
for i in range(N):
    matriz[i]=matriz[i]-puntuacion_menor
for i in range(N):
    if matriz[i]!=0:
        print(str(matriz[i]))

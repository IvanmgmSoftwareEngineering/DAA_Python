############################################
# TITLE: Elecciones
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: N: 6 enteros (número votos de cada partido)
#   Salida: suma lados triángulos generados
############################################
P1,P2,P3,P4,P5,P6 = map(int, input().strip().split())
matriz=[P1,P2,P3,P4,P5,P6]
ganador_indice=0
ganador_votos=0
for i in range(1,7):
    print(str(i) + " ", end="")
    if ganador_votos < int(matriz[i-1]):
        ganador_indice=i
        ganador_votos=matriz[i-1]
    for j in range(int(matriz[i-1])):
        print("=",end="")
    print(" ")
print("El ganador es el partido "+str(ganador_indice)+" con "+str(ganador_votos)+" votos")
############################################
# TITLE: ¡¡¡A COMER!!!
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: N: numero de nombres que recibiremos
#   Salida: nombre de lo potros en mayúscula
############################################
N=int(input())
matriz=[]
for i in range(N):
    nombre=input()
    nombre_mayuscula=nombre.upper()
    matriz.append(nombre_mayuscula)

for i in range(N):
    print(matriz[i])
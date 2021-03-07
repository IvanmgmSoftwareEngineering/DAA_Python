############################################
# TITLE: Matriz
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: A : Dimensión de la matriz cuadrada
#   Salida: matriz
############################################
A = int(input())
k=1
for i in range(1,A+1):
    for j in range(1,A+1):
        print (k,end="")
        print(" ",end="")
        k=k+1
    print (" ")

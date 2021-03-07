############################################
# TITLE: Factorial
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: N : entero positivo del cuál queremos obtener el factorial
#   Salida: resultado del factorial
############################################
A = int(input())
factorial=1
for i in range(A,0,-1):
    factorial=factorial*i
print(factorial)
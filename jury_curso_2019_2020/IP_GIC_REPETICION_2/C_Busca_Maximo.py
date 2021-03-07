############################################
# TITLE: Busca Maximo
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: N : número de datos entrada
#   Entrada 2: número entero 1
#   Entrada 3: número entero 2
#   Entrada ...
#   Entrada N+1: número entero N

#   Salida: máximo entero recibido en la entrada
############################################
argc=int(input())
if argc!=0:
    if argc!=1:
        M=0
        N=int(input())
        argc=argc-1
        for i in range(1,argc+1):
            M=int(input())
            if N <M:
                N=M
        print (N)
    else:
        print(int(input()))



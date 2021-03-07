############################################
# TITLE: Alquiler
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: n : precio/día en euros
#   Entrada 2: M: el més elegido
#   Salida: metros recorridos
############################################
n, m = map(int, input().strip().split())
if 50 <= n <= 500:
    if 1 <= m <= 6:
        if m == 2:
            cost = n * 28
        else:
            if m % 2 != 0:
                cost = n * 31
            else:
                cost = n * 30
    else:
        if m % 2 != 0:
            cost = n * 30
        else:
            cost = n * 31

print (cost)
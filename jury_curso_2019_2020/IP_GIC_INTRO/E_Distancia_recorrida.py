############################################
# TITLE: Alquiler
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: N : milimetros que abarca una zancada
#   Entrada 2: M: número de zancadas
#   Salida: metros recorridos
############################################
N, M = map(int, input().strip().split())
numero_pasos="{0:.1f}".format(round(N*0.001*M,1)).replace(".",",")
print(numero_pasos)
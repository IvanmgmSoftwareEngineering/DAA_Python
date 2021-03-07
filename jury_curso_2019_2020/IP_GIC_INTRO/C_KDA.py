############################################
# TITLE: KDA
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: N :kills
#   Entrada 2: M: deaths
#   Entrada 3: K: assists
#   Salida: KDA (Kills, Deaths and assists) del jugador
############################################
N=int(input())
M=int(input())
K=int(input())
KDA="{0:.2f}".format(round((N+K)/M,2)).replace(".",",")
print(KDA)


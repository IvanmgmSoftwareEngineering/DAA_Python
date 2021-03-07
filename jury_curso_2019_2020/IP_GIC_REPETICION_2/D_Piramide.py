############################################
# TITLE: Pirámide
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: A : Altura o número de niveles de la pirámide
#   Salida: dibujo pirámide con *
############################################
A=int(input())
for i in range (1,A+1):
    print(("*")*i)
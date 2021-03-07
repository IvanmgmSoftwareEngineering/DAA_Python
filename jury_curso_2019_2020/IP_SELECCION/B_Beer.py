############################################
# TITLE: Beer
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: n : IBU(International Bittering Unit) de la cerveza (Amargor)
#   Salida: calidad cerveza
############################################
n= int(input())
if n>46 :
    calidad="MUY BUENA"
elif n>=36 and n<=46:
    calidad = "BUENA"
elif n>=21 and n<=35:
    calidad = "REGULAR"
elif n>=11 and n<=20:
    calidad = "MALA"
elif n>=0 and n<=10:
    calidad = "CRUZCAMPO"
print(calidad)

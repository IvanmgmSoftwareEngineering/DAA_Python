############################################
# TITLE: Bisiesto
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: n : año a consultar
#   Salida: SI o NO es Bisiesto
############################################
n = int(input())
if n%4 == 0:
    resultado = "SI"
else:
    resultado = "NO"
print(resultado)

############################################
# TITLE: Alquiler
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: N : milimetros que abarca una zancada
#   Entrada 2: M: número de zancadas
#   Salida: SI o NO es válido el Código de Barras
############################################
N1, N2, N3, N4, N5, N6, N7, C =map(int, input().strip().split())

suma=N1*3+N2*1+N3*3+N4*4+N5*5+N6*6+N7*7
suma_1=suma/10
if suma_1-5 > round(suma_1):
    suma_2=round(suma_1)
else:
    suma_2=round(suma_1)+1
suma_2=suma_2*10
if suma_2-suma == C:
    resultado = "SI"
else:
    resultado = "NO"
print (resultado)






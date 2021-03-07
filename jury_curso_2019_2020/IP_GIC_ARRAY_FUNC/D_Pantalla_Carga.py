############################################
# TITLE: Pantalla Carga
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: l: longitud lado triángulo inicial
#   Salida: suma lados triángulos generados
############################################
l=int(input())
suma=0
contador=0
flag=True
while flag:
    if l==1:
        suma = suma + 3*3**contador
        flag=False
    else:
        suma = suma + 3*l*3**contador
        contador +=1
        l=round(l/2)
print (suma)


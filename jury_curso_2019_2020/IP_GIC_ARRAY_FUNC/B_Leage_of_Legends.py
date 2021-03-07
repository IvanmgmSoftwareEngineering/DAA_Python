############################################
# TITLE: Leage of Legends
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Línea 1: M y N:número de rondas que se jugaran en el torneo y  número de contrincantes
#   Línea 2:  M enteros con la puntuación en cada una de las M rondas
#   Línea 3:  M enteros con las puntuaciones del contrincante 1
#   Línea 4:  M enteros con las puntuaciones del contrincante 2
#   ...
#   Línea N+2:  M enteros con las puntuaciones del contrincante N


#   Salida: El número de veces que Yassuo ha conseguido más muertes que sus contrincantes en cada ronda
############################################
from collections import deque

#M, N = map(int, input().strip().split())
name_file_in="./samples-B/5.in"
name_file_out="./samples-B/5.out"

file_in=open(name_file_in)
linea= file_in.readline()
M , N = linea.split()
matriz_in=[]
resultado=[]
for i in range (int(M)):
    resultado.append(0)
for linea in file_in:
        matriz_in.append(linea)
puntuación_Yasuo=matriz_in[0].split()
for i in range(1,int(N)+1):
    puntuación_otros=matriz_in[i].split()
    for j in range(0,int(M)):
        if int(puntuación_Yasuo[j])>=int(puntuación_otros[j]):
            resultado[j]=resultado[j]+1
for i in range(int(M)):
    print (str(resultado[i])+" ", end="")

#Adicionalmente comparo con el fichero de salida que nos proporcionan
print(" ")
file_out= open(name_file_out)
linea_out=file_out.readline()
resultado_oficial=linea_out.split()
for i in range (int(M)):
    if int(resultado_oficial[i])== int(resultado[i]):
        print ("OK ",end="")
    else:
        print("W ", end="")






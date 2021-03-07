############################################
# TITLE: Dora la Programadora
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: N: identificadores empleado (termina en -1)
#   Salida: número de veces que un empleado a mirado la red social de Dora
############################################
name_file_in="./samples-C/1.in"
name_file_out="./samples-C/1.out"

resultado_aux =[]
resultado=[]
for i in range(10):
    resultado_aux.append(0)

file_in=open(name_file_in)
linea= file_in.readline()
linea_manejable=linea.split()
for i in range(len(linea_manejable)-1):
    if int(linea_manejable[i])!=-1:
        resultado_aux[int(linea_manejable[i])]=resultado_aux[int(linea_manejable[i])]+1
for i in range(10):
    if(resultado_aux[i]>=3):
        resultado.append(i)
        print (str(i)+" ",end="")


#Adicionalmente comparo con el fichero de salida que nos proporcionan
print(" ")
file_out= open(name_file_out)
linea_out=file_out.readline()
resultado_oficial=linea_out.split()
for i in range (3):
    if int(resultado_oficial[i])== int(resultado[i]):
        print ("OK ",end="")
    else:
        print("W ", end="")

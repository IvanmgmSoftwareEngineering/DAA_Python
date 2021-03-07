############################################
# TITLE: Lista Regalos
# AUTHOR: Iván Martín Gómez
# DATE: Tuesday 2nd March 2021
# DESCRIPTION:
#   Entrada 1: N: numero de regalos disponibles para elegir
#   Entrada 2: C, P y U: nombre regalo, precio y unidades disponibles del regalo 1
#   Entrada 3: C, P y U: nombre regalo, precio y unidades disponibles del regalo 2
#   ...
#   Entrada N+1: C, P y U: nombre regalo, precio y unidades disponibles del regalo N
#   Entrada N+2: M: numero de estudiantes que piden regalo
#   Entrada N+3: E y R: numero regalos E ha pedido el estudiante 1  y una lista con E enteros con el id del regalo
#   ...
#   Entrada N+M+1: E y R: numero regalos E ha pedido el estudiante M y una lista con E enteros con el id del regalo
#   Salida: se imprime por pantalla el nombre de un regalo por cada vez que un estudiante lo haya pedido y si hay suficientes unidades.
#           Finalmente se imprime el coste total de los regalos pedidos
############################################
nombre_regalos=[]
precio_regalos=[]
unidades_regalos=[]
cuenta_total=0
cuenta_lineas=0;
name_file_in="./samples-A/7.in"
name_file_out="./samples-A/7.out"
file_in=open(name_file_in)
file_out=open(name_file_out)

N=file_in.readline()
for i in range(1,int(N)+1):
    linea=file_in.readline().strip().split()
    nombre_regalos.append(linea[0])
    precio_regalos.append(linea[1])
    unidades_regalos.append(linea[2])

M=file_in.readline()
for i in range(0,int(M)):
    linea=file_in.readline().strip().split()
    for j in range(1,int(linea[0])+1):
        if int(unidades_regalos[int(linea[j])]) >0:
            unidades_regalos[int(linea[j])]=int(unidades_regalos[int(linea[j])])-1
            cuenta_total=cuenta_total+int(precio_regalos[int(linea[j])])
            print(nombre_regalos[int(linea[j])])
            linea_oficial=file_out.readline().strip()
            if nombre_regalos[int(linea[j])] == linea_oficial:
                continue
            else:
                print("Diferencia con respecto a solución oficial")

if  cuenta_total != int(file_out.readline()):
    print("Diferencia con respecto a solución oficial")
print(cuenta_total)
file_in.close()
file_out.close()


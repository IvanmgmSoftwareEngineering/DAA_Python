############################################
# TITLE: Simulador Combate
# AUTHOR: Iván Martín Gómez
# DATE: Tuesday 2nd March 2021
# DESCRIPTION:
#   Entrada 1: N enteros: numero de jugadores por equipo
#   Entrada 2: N enteros: puntos de ataque de cada jugador del equipo 1
#   Entrada 3: N enteros: puntos de ataque de cada jugador del equipo 2
#   Entrada 4: M: número de ataques que se han producido en la partida
#   Entrada 5: E, P1 y P2: Equipo que ataca, jugador que ataca, jugador que recibe el ataque
#   ...
#   Entrada M+1: E, P1 y P2: Equipo que ataca, jugador que ataca, jugador que recibe el ataque
#   Salida: Tres enteros T, D y P separados por un espacio.
#           (T)Equipo que ha ganado (0,1)
#           (D)Daño total realizado por el equipo ganador
#           (P)Jugador del equipo ganador que más daño a inflijido
############################################
name_file_in="./samples-B/1.in"
name_file_out="./samples-B/1.out"
puntos_ataque_equipo_1=[]
puntos_ataque_equipo_2=[]
resultado=[0,0,0]
daño_recibido_equipo_1=0
daño_recibido_equipo_2=0
daño_realizado_equipo_1=0
daño_realizado_equipo_2=0
daño_realizado_jugadores_quipo_1=[]
daño_realizado_jugadores_quipo_2=[]
file_in=open(name_file_in)
file_out=open(name_file_out)

numero_jugadores_por_equipo=file_in.readline().strip()

for j in range(0,2):
    linea = file_in.readline().strip().split()
    for i in range(0,int(numero_jugadores_por_equipo)):
        if j==0:
            puntos_ataque_equipo_1.append(linea[i])
        else:
            puntos_ataque_equipo_2.append(linea[i])
        daño_realizado_jugadores_quipo_1.append(0)
        daño_realizado_jugadores_quipo_2.append(0)

numero_ataques_partida=file_in.readline().strip()
for i in range(0,int(numero_ataques_partida)):
    linea= file_in.readline().strip().split()
    if int(linea[0])==0:
        daño_realizado_equipo_1=daño_realizado_equipo_1+int(puntos_ataque_equipo_1[int(linea[1])])
        daño_recibido_equipo_2 = daño_recibido_equipo_2 + int(puntos_ataque_equipo_1[int(linea[1])])
        daño_realizado_jugadores_quipo_1[int(linea[1])]=daño_realizado_jugadores_quipo_1[int(linea[1])]+int(puntos_ataque_equipo_1[int(linea[1])])
    else:
        daño_realizado_equipo_2=daño_realizado_equipo_2+int(puntos_ataque_equipo_2[int(linea[1])])
        daño_recibido_equipo_1 = daño_recibido_equipo_1 +int(puntos_ataque_equipo_2[int(linea[1])])
        daño_realizado_jugadores_quipo_2[int(linea[1])]=daño_realizado_jugadores_quipo_2[int(linea[1])]+int(puntos_ataque_equipo_2[int(linea[1])])

if (daño_realizado_equipo_1 - daño_recibido_equipo_1) < (daño_realizado_equipo_2 - daño_recibido_equipo_2):
    #Gana Equipo 2
    print("1 ",end="")
    print(str(daño_realizado_equipo_2) +" ", end="")
    maximo=0
    indice_maximo=0
    for i in range(0,int(numero_jugadores_por_equipo)):
        if daño_realizado_jugadores_quipo_2[i]>maximo:
            maximo=daño_realizado_jugadores_quipo_2[i]
            indice_maximo=i
    print(indice_maximo)
    resultado=[1,daño_realizado_equipo_2,indice_maximo]
else:
    # Gana Equipo 1
    print("0 ", end="")
    print(str(daño_realizado_equipo_1) +" ", end="")
    maximo=0
    indice_maximo=0
    for i in range(0,int(numero_jugadores_por_equipo)):
        if daño_realizado_jugadores_quipo_1[i]>maximo:
            maximo=daño_realizado_jugadores_quipo_1[i]
            indice_maximo=i
    print(indice_maximo)
    resultado=[0,daño_realizado_equipo_1,indice_maximo]

#Chekeo con solución oficial
linea=file_out.readline().strip().split()
for i in range(0,3):
    if int(linea[i])!=int(resultado[i]):
        print("Resultado diferente con respecto solución oficial")

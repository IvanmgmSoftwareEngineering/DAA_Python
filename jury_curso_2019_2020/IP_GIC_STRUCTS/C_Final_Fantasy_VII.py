############################################
# TITLE: Final Fantasy VII
# AUTHOR: Iván Martín Gómez
# DATE: Tuesday 2nd March 2021
# DESCRIPTION:
#   Entrada 1: PV, PA y PM (3 enteros): Personaje 1
#               PV = Puntos de Vida Personaje 1
#               PA = Puntos de Ataque Personaje 1
#               PM = Magía Personaje Personaje 1
#   Entrada 2: PV, PA y PM (3 enteros): Personaje 2
#               PV = Puntos de Vida Personaje 2
#               PA = Puntos de Ataque Personaje 2
#               PM = Magía Personaje Personaje 2
#   Entrada 3: PV, PA y PM (3 enteros): Personaje 3
#               PV = Puntos de Vida Personaje 3
#               PA = Puntos de Ataque Personaje 3
#               PM = Magía Personaje Personaje 3
#   Entrada 4: M: número de enemigos
#   Entrada 5: EV(entero), EA(entero), EF(real) y EM(real): Enemigo 1
#               EV = Puntos de Vida Enemigo 1
#               EA = Puntos de Ataque Enemigo 1
#               EF = Resistencia Física Enemigo 1
#               EM = Magía Enemigo 1
#   Entrada 6: Entero con numero de ataques (A) y (A) enteros con el jugador al que ataca el Enemigo 1
#   ...
#   Entrada 4+M: EV(entero), EA(entero), EF(real) y EM(real): Enemigo M
#               EV = Puntos de Vida Enemigo M
#               EA = Puntos de Ataque Enemigo M
#               EF = Resistencia Física Enemigo M
#               EM = Magía Enemigo M
#   Entrada 4+M+1: Entero con numero de ataques (A) y (A) enteros con el jugador al que ataca el Enemigo M

#   Salida: Número de enemigos que es capaz de derrotar el equipo
#
############################################
name_file_in="./samples-C/1.in"
name_file_out="./samples-C/1.out"
personaje_1=[]
personaje_2=[]
personaje_3=[]
enemigos=[]
ataques=[]
file_in=open(name_file_in)
file_out=open(name_file_out)

linea=file_in.readline().strip().split()
personaje_1.append(linea[0])
personaje_1.append(linea[1])
personaje_1.append(linea[2])
linea=file_in.readline().strip().split()
personaje_2.append(linea[0])
personaje_2.append(linea[1])
personaje_2.append(linea[2])
linea=file_in.readline().strip().split()
personaje_3.append(linea[0])
personaje_3.append(linea[1])
personaje_3.append(linea[2])

numero_enemigos=file_in.readline()
for i in range(0,int(numero_enemigos)):
    linea=file_in.readline().strip().split()
    enemigos.append(linea)
    linea=file_in.readline().strip().split()
    ataques.append(linea)


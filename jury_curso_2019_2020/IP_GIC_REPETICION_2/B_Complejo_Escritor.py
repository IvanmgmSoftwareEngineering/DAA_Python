############################################
# TITLE: Complejo Escritor
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1: C : número de capítulos
#   Entrada 2: S: secciones de todos los capítulos
#   Entrada 3: B: subsecciones de cada sección
#   Salida: imprimir un índice
############################################
C, S, B = map(int, input().strip().split())
for i in range(1,C+1):
    print("Capitulo "+ str(i))
    for j in range(1,S+1):
        print(" Seccion " + str(i)+"."+str(j))
        for k in range(1,B+1):
            print("  Subseccion " + str(i) + "." + str(j)+ "." + str(k))
print("Fin")
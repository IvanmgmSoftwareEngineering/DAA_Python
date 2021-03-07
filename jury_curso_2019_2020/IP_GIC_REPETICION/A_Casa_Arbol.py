############################################
# TITLE: Casa Árbol
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: A : minutos Homer en el sótano
#   Entrada 2: B : número de veces que Homer escribe su frase en un minuto
#   Salida 1: "Sin tele, sin cerveza, Homer pierde la cabeza"
#   Salida ...
#   Salida n: "Sin tele, sin cerveza, Homer pierde la cabeza"
############################################
A, B = map(int, input().strip().split())
for i in range(1,A*B+1):
    print("Sin tele y sin cerveza, Homer pierde la cabeza")


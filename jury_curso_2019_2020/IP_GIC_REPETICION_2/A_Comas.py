############################################
# TITLE: Comas
# AUTHOR: Iván Martín Gómez
# DATE: Sunday 28th February
# DESCRIPTION:
#   Entrada 1:  Cadena de carácteres terminada en *
#   Salida: número de comas que hay en lña entrada
############################################
cuenta=0
flag=True
while flag:
    A=input()
    if A=="*":
        flag=False
    elif A== ",":
        cuenta=cuenta+1
print(cuenta)



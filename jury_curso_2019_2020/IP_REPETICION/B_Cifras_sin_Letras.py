############################################
# TITLE: Cifras sin Letras
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: N : numero a descomponer
#   Salida: metros recorridos
############################################
N=int(input())
millares=round(N/1000)
flag_millares=False
flag_centenas=False
flag_decenas=False

millares=N/1000
if millares >=1:
    flag_millares = True
    flag_centenas = True
    flag_decenas = True
    millares_1=round(millares)
    if millares - millares_1 < 0:
        millares_1 = millares_1 -1
    centenas = (N - (millares_1 * 1000)) / 100
    centenas_1=round(centenas)
    if centenas-centenas_1<0:
        centenas_1 = centenas_1-1
    decenas = (N - (millares_1 * 1000 + centenas_1 * 100)) / 10
    decenas_1=round(decenas)
    if decenas - decenas_1 <0:
        decenas_1=decenas_1-1
    unidades = N - (millares_1 * 1000 + centenas_1 * 100 + decenas_1 * 10)
else:
    centenas=N/100
    if centenas >=1:
        flag_centenas = True
        flag_decenas = True
        centenas_1 = round(centenas)
        if centenas - centenas_1 < 0:
            centenas_1 = centenas_1 - 1
        decenas = (N - (centenas_1 * 100)) / 10
        decenas_1 = round(decenas)
        if decenas - decenas_1 < 0:
            decenas_1 = decenas_1 - 1
        unidades = N - (centenas_1 * 100 + decenas_1 * 10)

    else:
        decenas=N/10
        if decenas >= 1:
            flag_decenas = True
            decenas_1 = round(decenas)
            if decenas - decenas_1 < 0:
                decenas_1 = decenas_1 - 1
            unidades = N - (decenas_1 * 10)
        else:
            unidades=N

print(str(unidades) + " unidades")
if flag_decenas:
    print(str(decenas_1) + " decenas")
if flag_centenas:
    print(str(centenas_1) + " centenas")
if flag_millares:
    print(str(millares_1) + " millares")









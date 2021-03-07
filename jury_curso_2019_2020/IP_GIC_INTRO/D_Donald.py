############################################
# TITLE: Donald
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: N :mililitros de vacuana
#   Entrada 2: M: millones de habitantes
#   Salida: número de botellas de lejia que deben comprar
############################################
N=int(input())
M=int(input())
numero_botellas=round(N*0.001*M*1000000*1/2)
print (numero_botellas)
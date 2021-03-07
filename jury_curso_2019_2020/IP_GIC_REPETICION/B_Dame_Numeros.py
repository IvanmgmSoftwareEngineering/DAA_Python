############################################
# TITLE: Dame Números
# AUTHOR: Iván Martín Gómez
# DATE: Saturday 27th February
# DESCRIPTION:
#   Entrada 1: A :
#   Entrada 2: B :
#   Salida 1: A
#   Salida 2: A+1
#   ...
#   Salida n-1: B-1
#   Salida n: B
############################################
A, B = map(int, input().strip().split())
if A>B:
    for i in range(A,B-1,-1):
        print(i)
elif A<B:
    for i in range(A,B+1):
        print(i)
else:
    print (A)
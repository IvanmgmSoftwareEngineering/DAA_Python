'''
Created on Feb 18, 2021

@author: IvanMGM
'''
import math
def imc (N,M):
    return "{0:.2f}".format(round(N/(M/100)**2,2))

N,M=map(int,input().strip().split());
print(imc(N,M));
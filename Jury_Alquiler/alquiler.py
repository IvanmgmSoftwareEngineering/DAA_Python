'''
Created on Feb 17, 2021

@author: IvanMGM
'''


def alquiler(n, m):
    if 50 <= n <= 500:
        if 1 <= m <= 6:
            if m == 2:
                cost = n * 28
            else:
                if m % 2 != 0:
                    cost = n * 31
                else:
                    cost = n * 30
        else:
            if m % 2 != 0:
                cost = n * 30
            else:
                cost = n * 31
    return cost


n, m = map(int, input().strip().split())
print(alquiler(n, m))

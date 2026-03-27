import numpy.random as rd
import numpy as np

# Exercice 1


def norcentreereduite():
    l=[rd.random() for _ in range(12)]
    x=0
    for i in range(12):
        x+=l[i]
    return x-6

print(norcentreereduite())



def normal(m,s):
    return m+s*norcentreereduite()

def normalN(m,s,N):
    l=[normal(m,s) for _ in range(N)]
    return l

print(normalN(0,1,10))



# Exercice 2

def expo(l):
    return -(1/l)*np.log(1-rd.random())
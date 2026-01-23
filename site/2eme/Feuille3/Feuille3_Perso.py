# Exercice 1

# 1)
import random as rd
def X():
    return 1 if rd.random() < 0.2 else 0

# 2)
def S(n):
    return sum((X() for _ in range(n)))/n

print(S(10000))

# OU plus rapide



# Exercice 2:

# 1)

from numpy import random
def U2(n):
    u=2*[i for i in range(1, n+1)]
    Y=0
    while True:
        Y+=1
        b1, b2 = rd.sample(u, 2)
        if b1==b2:
            return Y
        
print(U2(10))
random.randint # numpy exclu
rd.randint # random inclu
# 2)
def Z(n):
    return sum([U2(i) for i in range(n, 0, -1)])

print(Z(10))

# Exercice 3

# 1)

def simul_X():
    a=random.random()
    if a<0.2:
        return 0
    elif a<0.7:
        return 2
    elif a<0.9:
        return 5
    else:
        return 10

print(simul_X())
# 2)
def simul_Xn(n):
    values = [simul_X() for _ in range(n)]
    return values, sum(values)/n
print(simul_Xn(10))


# Exercice 4
# 1)
import math
def uniforme(n, m):
    return math.floor(random.random()*(m-n))+n
print([uniforme(5, 10) for _ in range(5)])


def unibis(n, m, N):
    return [uniforme(n, m) for _ in range(N)]



# Exercice 5

# 1)

def B(p):
    return 1 if random.random()<p else 0

# 2)

def Bn(n, p):
    return [B(p) for _ in range(n)]


# Exercice 6

def binomiale(n, p):
    i=0
    for _ in range(n):
        i+=B(p)
    return i
print(binomiale(10, 0.3))

def binomiale_simul(n, p, N):
    return [binomiale(n, p) for _ in range(N)]

print(binomiale_simul(10, 0.3, 5))

# Exercice 7

# 1)

def geom(p):
    i=1
    while B(p)==0:
        i+=1
    return i

# 2)

def GEOM(P, N):
    return [geom(P) for _ in range(N)]

# 3)

print(sum(GEOM(0.2, 10000))/10000)


# Exercice 8

# 3)
import numpy as np
import matplotlib.pyplot as plt

nb_faces=int(input("Nombre de faces : "))
nb_lignes=5
nb_colonnes=2
for i in range(1, nb_lignes+1):
    nb_lancers=20*i
    x=np.arange(1,nb_lancers+1 )
    y=np.floor(nb_faces*random.random(nb_lancers))+1
    plt.subplot ( nb_lignes , nb_colonnes , nb_colonnes*(i-1)+1)
    plt.bar(x,y)
    plt.subplot ( nb_lignes , nb_colonnes , nb_colonnes*(i-1)+2)
    plt.hist(y, range = (0, nb_faces+1), bins = nb_faces+1, color = "yellow",edgecolor = "red", density = True)

plt.show()


nb_lignes=3
nb_colonnes=3
for i in range(1, nb_lignes+1):
    for j in range(1, nb_colonnes+1):
        nb_lancers=20*i
        x=np.arange(1,nb_lancers+1 )
        y=np.floor(nb_faces*random.random(nb_lancers))+1
        plt.subplot ( nb_lignes , nb_colonnes , nb_colonnes*(i-1)+j)
        plt.hist(y, range = (0, nb_faces+1), bins = nb_faces+1, color = "yellow",edgecolor = "red", density = True)

plt.show()
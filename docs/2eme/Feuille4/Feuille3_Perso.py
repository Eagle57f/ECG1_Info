# Exercice 1

import numpy.random as rd
import numpy as np
def series(m):
    N=np.ones(m)
    simule=rd.random(m)<0.5
    for k in range(m-1):
        N[k+1]=N[k]
        if simule[k+1]!=simule[k]:
            N[k+1]=N[k]+1
    return N

# m=int(input('m='))
# moy=np.zeros(m)
# for k in range(100000):
#     moy=moy+series(m)
# print(moy/100000)


# Exercice 2
def tirage(x, y):
    return 0 if rd.random() < x / (x + y) else 1

def experience(a,b,n):
    x,y=a,b
    for k in range(n):
        r=tirage(x,y)
        if r==0:
            x+=1
        else:
            y+=1
    return x-a

print(experience(3,2,10))
def simulation(a,b,n,m):
    l=np.zeros(n)
    for _ in range(m):
        l[experience(a,b,n)-1]+=1
    return l/m

print(simulation(3,2,10,1000))



# Exercice 3

def tirage(n):
    urnes = np.zeros(n)
    X=0
    choix=rd.randint(1,n+1)
    while max(urnes)<2:
        urnes[choix-1] = urnes[choix-1] + 1
        choix = rd.randint(1,n+1)
        X = X+1
    return X        

print([tirage(5) for i in range(100)])

def Esperance(n,m):
    s=0
    for k in range(m):
        s=s+tirage(n)
    return s/m

print(Esperance(5,1000))


# Exercice 4

def XYG(a, p):
    X=0
    Y=0
    G=0
    while rd.random() > a:
        if rd.random() < p:
            G+=1
            Y+=1
        else:
            G-=1
        X+=1
    return X, Y, G

print(XYG(0.2, 0.5))


# Exercice 5

def X():
    return rd.random()
def M(n):
    return max([X() for i in range(n)])
def Y(n):
    return n*(1-M(n))



def Exp():
    return rd.exponential(1)
def Z(n):
    return [Exp() for i in range(n)]

# import matplotlib.pyplot as plt

# plt.hist(Z(1000), range=[0,10], bins=10, density=True, label='Y(n)')
# plt.show()

# plt.hist([Y(10) for i in range(1000)], range=[0,10], bins=10, density=True, label='Z(n)')
# plt.show()


# Exercice 6
# a) P(Z1=n-1)=1/2, P(Z1=n+1)=1/2, sinon = 0

# b) 

def Z(n, k):
    b=n
    r=n
    for _ in range(k):
        if rd.random()<b/(b+r):
            b+=1
            r-=1
        else:
            b-=1
            r+=1
    return b
print(Z(10,5))

# c)

def esperance(n, k):
    s=0
    for _ in range(1000):
        s=s+Z(n,k)
    return s/1000
print(esperance(10,5))
        




# Exercice 7
# Soit J est devant, soit P.
# Etre séparé par m personnes signifie que la difference de leur
# positions est m+1.
# 
# Soit d=m+1
# Soit i et j les positions respectives de J et P.
# On a abs(i-j)=d
# 
# Il faut donc compter le nombre de couples (i,j) tq abs(i-j)=d
# Si P devant : j=i+d ainsi i peut varier de 1 a n-d
# Si J devant : i=j+d ainsi j peut varier de 1 a n-d
# Donc le nombre de couples est 2*(n-d)
# 
# Il y a n(n-1) couples possibles (i,j) avec i!=j
# Ainsi P(J et P séparés par m personnes)=2*(n-(m+1))/(n(n-1))
# 
# Soit f(x)=2*(n-(x+1))/(n(n-1))
# max de f(x) pour x dans [0,n-2] atteint en x=0
# Donc la probabilité est maximale quand J et P sont côte à côte
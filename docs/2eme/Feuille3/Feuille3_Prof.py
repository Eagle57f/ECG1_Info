#Feuille 3

from numpy.random import*
import numpy.random as rd
import matplotlib.pyplot as plt
import numpy as np

#Exercice 1


##1)
def simule():
    X=rd.random()
    if X<0.2:
        sortie=1
    else:
        sortie=0
    return sortie


def simule():
    X=rd.random()
    if X<0.2:
        sortie=1
    else:
        sortie =0
    return sortie
##2)

print('Frequence=',np.mean([simule() for k in range(10000)]))

print('Frequence=',sum([simule() for k in range(10000)])/10000)

s=0
for k in range (10000):
    s=s+simule()
print('Frequence=', s/10000)

#Exercice 2

#1)
def simuleU(n):
    Y=0
    while rd.random()>1/(2*n-1):
        Y=Y+1
    return Y
#ou
def simuleU2(m):
    urne=2*[i for i in range(1,m+1)]
    Y=0
    while True:
        Y+=1
        b1,b2=random.sample(urne,2)
        if b1==b2:
            return Y
#2)

n=int(input('n='))
z=0
for k in range(n,0,-1):
    z=z+simuleU(k)
print("le nmbre de tirage nécessaire pour vider l'urne est", z)

#ou
print('La valeur Z=', sum(simuleU(i) for i in range (n, 0, -1)))


#ex3

def simuleX():
    Lancer=rd.random()
    if 0<Lancer<=1/5:
        x=0
    elif 1/5<Lancer<=7/10:
        x=2
    elif 7/10<Lancer<=9/10:
        x=5
    else:
        x=10
    return x

print('Moyenne empirique pour =', np.mean([simuleX() for k in range (10000)]))

#q3
n=int(input('n='))
E=0
for k in range(n):
    E+=simuleX()
print('Moyenne empirique pour n=',n, 'est', E/n, 'à comparer avec E=3')


#ex4

#1)

def Uniforme(n,m):
    return(int(m-n)*rd.random())+n
#retourne le résultat d'1 réalisa° d'1 loi uniforme sur l'ensemble des entiers i
#tels que n<=i<=m-1 avec n et m-1 des entiers relatifs

#2)

def Uniforme2(n,m,N):
    v=np.zeros(N)
    for k in range(N):
        v[k]=Uniforme(n,m)
    return v

#ex5

def Bernoulli(p):
    u=0
    if rd.random()<=p:
        u=1
    return u

def Bernoulli(p):
    lancer=rd.random()
    if lancer<p:
        u=1
    else:
        u=0
    return u


def BernoulliN(p,N):
    v=np.zeros(N)
    for k in range(N):
        v[k]=Bernoulli(p)
    return v


#ex6

def binomiale(n,p):
    s=0
    for k in range(n):
        s=s+Bernoulli(p)
    return(s)

def binomiale(n,p):
    s=0
    for k in range (n):
        alea=rd.random()<p
        s=s+alea
    return(s)


def binomialeN(n,p,N):
    v=np.zeros(N)
    for k in range(N):
        v[k]=binomiale(n,p)
    return v

#ex7

def geometrique(p):
    x=1
    while rd.random()>p:
        x+=1
    return x

def GEOM(P,N):
    L=[]
    for k in range(N):
        L.append(geometrique(P))
    return L

N=int(input('N='))
P=float(input('P='))
MOYENNE=np.mean(GEOM(P,N))
print(('Espérance=', MOYENNE))


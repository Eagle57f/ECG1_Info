#Feuille 4

from numpy.random import*
import numpy.random as rd
import matplotlib.pyplot as plt
import numpy as np


##EX 1
#a

def series(m):
    N=np.ones(m)
    simule=rd.random(m)<0.5
    for k in range(m-1):
        N[k+1]==N[k]
        if simule[k+1]!=simule[k]:
            N[k+1]=N[k]+1
    return N
    
#b
m=int(input('m='))
moyennes=np.zeros(m)
for k in range(100000):
    moyennes=moyennes+series(m)
print('moyennes=', moyennes/100000)
        
        
    
  
## EX 2

def tirage(x,y):
    r=rd.random()
    if r<x(x+y):
        res=0
    else:
        res=1
    return res
    
def experience(a,b,n):
    x,y=a,b
    for k in range (n):
        r=tirage(x,y)
        if r==0:
            x=x+1
        else:
            y=y+1
    return x-a

#2c

def simulation(a,b,n,m):
    loi=np.zeros(n+1)
    for k in range(n+1):
        r=experience(a,b,n)
        loi[r]=loi[r]+1
    return loi/m
        
    
## EX3

#1     
import numpy.random as rd
from math import*
def EML(n):
    b=1
    r=2
    s=0
    for k in range(n):
        x=rd.random()
        if x<=r/(b+r)  :
            r=r+1
            s=s+1
        else:
            b=b+1
    return s

#2
n=int(input('n'))
m=int(input('m'))
moyenne=0
for k in range(m):
    moyenne=moyenne+EML(n)
print('La moyenne=', moyenne/m)


##EX4
def simulX(a,b,r):
    i=1
    while rd.random()<(a+(i-1)*r)/(a+b+(i-1)*r):
        i= i+1
    return i

def Moyenne(a,b,r,N):
    S=0
    for k in range (N):
        S=S+simulX(a,b,r)
    return S/N

def Moyenne1(a,b,r,N):
    return sum(simulX(a,b,r)for k in range(N))/N
    

##Ex5


n=int(input('la taille de la file est n='))
N=int(input("le nombre d'experiences ='"))
M=np.zeros(n-1)
file=np.arange(n)
simulation=np.zeros(N)
for k in range(N):
    permute=rd.permutation(file)
    permute_liste=list(permute)
    m=abs(permute_liste.index(0)-permute_liste.index(1))-1
    simulation[k]=m
    M[m]=M[m]+1
plt.hist(simulation, range=(0,n-1), bins=9, color="yellow", edgecolor="black")
print("loi=", M/N)

##EX6

def HEC2022(n):
    tableau=[0]
    nb_boules_differentes=0
    nb_tirages=0
    while nb_boules_differentes<n:
        numero_b=rd.randint(1,n+1)
        nb_tirages+=1
        if tableau[numero_b-1]==0:
            tableau[numero_b-1]=1
            nb_boules_differentes+=1
    return nb_tirages
    
def simulation_moyenne(n):
    moyenne=0
    for k in range(1000):
        moyenne+=HEC2022(n)
    return moyenne/1000
    
def simulation_moyenne1(n):
    moyenne=np.mean([HEC2022(n) for k in range(1000)])
    return moyenne
    

##ex7
def simuler_XY():
    X=0
    Y=0
    tirage=0
    while X==0 or Y==0:
        tirage+=1
        r=rd.randint(1,4)
        if r==1 and X==0:
            X=tirage
        elif r==2 and Y==0:
            Y=tirage
    return X,Y
    
    

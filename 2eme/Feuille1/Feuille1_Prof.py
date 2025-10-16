# Merci à Bérénice pour avoir recopié la correction du prof
#
# Date de dernière mise à jour de la correction: 03.09.2025
# ===========================================================


import numpy as np  # pour calcul matriciel
import matplotlib.pyplot as plt  #ma biblio pour la représenta graphique en 2D
from math import*

#Exo 1

#1) Correction

#version1
n=int(input('Donner un entier naturel n:'))
L=[k**3 for k in range (n+1)]
S=sum(L)
print("La liste L est",L,"et la somme est",S)


#version 2

n=int(input('Donner un entier naturel n:'))
L=[]  #liste vide
s=0
for k in range(n+1):
    L=L+[k**3]  #construction d'une liste à l'aide d'une concaténation
    s=s+k**3  # calcul de la somme

#2)  Correction

#version 1

def inverse1(L):
    M=[1/k for k in L if k!=0]
    return M

#version 2

def inverse2(L):
    L_inv=[]
    for k in L:
        if k!=0:
            L_inv.append(1/k)
    return L_inv


#3)

#version 1
n=int(input('le nmbre de notes est:'))
notes=[]
listecoeffs=[]  #initialisation de la liste
Sprod=0  #initialisation de la somme
Scoeffs=0
for k in range(n):
    print('note', k+1,' :')
    note=float(input(' '))
    print('Coef', k+1, ' :')
    coeff=float(input(' '))
    Scoeffs= Scoeffs+coeff
    Sprod= Sprod+note*coeff
print("La moyenne est ", Sprod/Scoeffs)


#version 2

notes= eval(input('donner la liste des notes:'))
listecoeffs=eval(input('Donner la liste des coefs:'))
S=0
for k in range (len(notes)):
    S=S+notes[k]*listecoeffs[k]
    M=S/sum(listecoeffs)
print("La moyenne est", M)


#4)

def echange(L,i,j):
    if 0<=i<=len(L)-1 and 0<=j<=len(L)-1:
        #les indices vont de 0 à longueur -1
        L[i], L[j]=L[j],L[i]
    else:
        L='changer i ou j'
    return L



def echange2(L,i,j):
    if 0 <=i<=len(L)-1 and 0<=j<=len(L)-1:
        X=L[i]
        L[i]=L[j]
        L[j]=X
    else:
        L="changer l'un des argument-s i ou j"
    return L

##5)

def supp1(L,x):
    L1=[y for y in L if y!=x]
    return L1

# ou

def supp2(L,x):
    L2=[]
    for k in range (0,len(L)):
        if L[k]!=x:
            L2.append(L[k])
    return L2

def supp3(L,x):
    L3=[]
    for l in L:
        if l!=x:
            L3=L3+[l]
    return L3

##6

def insertion(L,i,x):
    if 0<=i<=len(L)-1:

       L1=L[0:i]   #extraction d'une liste de 0 à i-1
       L2=L[i:len(L)]   #extraction d'une liste de i à longueur -1
       L=L1+[x]+L2
    else:
        L="l'indice i n'appartient à l'intervalle"
    return L

def insertion2(L,i,x):
    if 0<=i<=len(L)-1:
        L.insert(i,x)
    else:
        L="l'indice i n'appartient à l'intervalle"
    return L

##7
def mesmax1(L):
    maxi=max(L)
    return maxi, L.count(maxi)

def mesmax2(L):
    maxi=L[0] #on suppose que le 1er terme est le max
    c=0
    for x in L:
        if x>maxi:
            maxi=x
            c=1
        elif x==maxi:
            c=c+1
    return maxi, c


##8

def supdouble(L):
    NL=[]
    for x in L:
        if x not in NL:
            NL=NL+[x]
    return NL

##9

def appro(L):
    ecart=abs(L[0]-L[1])
    a,b=L[0], L[1]
    for i in range(0,len(L)):
        for j in range (i+1, len(L)):
            if abs(L[i]-L[j]) <ecart:
                ecart=abs(L[i]-L[j])
                a,b=L[i], L[j]
    return a,b


##10

n=int(input("n?"))
L=[i+j for i in range(0,n) for j in range (i+1, n+1)]
print('sommeV1', sum(L))


n=int(input("n?"))
S=0
for i in range (0,n):
    for j in range(i+1,n+1):
        S=S+i+j
print('sommev2=',S)

def sommedouble(n):
    s=0
    for i in range (0,n):
        for j in range (i+1,n+1):
            s=s+i+j
    return 'sommev3=',s



#exercice 1


def factorielle(n):
    P=1
    for k in range(1,n+1):
        P=P*k
    return P
x=range(0,50) #axe des abcisse
u=[factorielle(n)/n**n for n in x]
plt.plot(x,u, 'xg')
plt.show()


n=int(input('N?'))
P=1
u=[]
for k in range(1,n+1):
    P=P*k
    u.append(P/k**k)
x=range(0,n) #axe des abcisses
plt.plot(x,u,'*r')
plt.show()


 #exercice 2

def f(n,x):
    y=x**n+x-1
    return y

def dicho(n):
    a,b=0,1
    while abs(b-a)>10**(-3):
        m=(a+b)/2
        if f(n,m)==0:
            a,b= m,m
        elif f(n,a)*f(n,m)<0:
            b=m
        elif f(n,a)*f(n,m)>0:
            a=m
    return (a+b)/2


n=int(input('n?'))
x=np.linspace(0,1,501)
for k in range (1,n+1):
    y= f(k,x)
    plt.plot(x,y)
    plt.plot(dicho(k),0,'rx')
plt.grid()
plt.show()


#exercice 3

#version 1

def suiteuV1(n):
    u,v=0,1
    for k in range (2,n+1):
        w=u+v  #un+2=un+1+un
        u,v=v,w # un+1=un et un+1=un+2
    return v

#version 2

def suiteuV2(n):
    u,v=0,1
    for k in range (2,n+1):
        w=u+v
        u=v
        v=w
    return v

def nb_or():
    rho=(1+sqrt(5)/2)
    p=1
    while abs(suiteuV1(p+1)/suiteuV1(p))-rho>10**-10:
        p=p+1
    return p

#exercice 4

def Edhec21():
    s=0
    u=1
    k=0 #compteur
    while s<=1000:
        s=s+u
        u=sqrt(u**2+u)
        k=k+1
    return k

def Edhec21b():
    u=1
    k=0
    while u**2-1<=1000:
        u=sqrt(u**2+u)
        k=k+1
    return k
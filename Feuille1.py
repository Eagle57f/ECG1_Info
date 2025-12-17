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
    note=float(input(' ')
    print('Coef', k+1, ' :')
    coeff=float(input(' '))
    Scoeffs= Scoeffs+coeff
    Sprod= Sprod+note*coeff
print("La moyenne est ", Sprod/scoeffs)


#version 2

notes= eval(input('donner la liste des notes:'))
listecoeffs=eval(input('Donner la liste des coefs:'))
S=0
for k in range (len(notes)):
    S=S+notes[k]*listecoeffs[k]
    M=S/sum(listecoeffs, notes)
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
    L1=[y for y in L if y=!x]
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
            if abs(L[i])-L[j]) <ecart:
                ecart=abs(L[i]-L[j])
                a,b=L[i], L[j]
    return a,b


##10

n=int(input("n?"))
L=[i+j for i in range(0,n), for j in range (i+1, n+1)]
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
u=[factorielle(n)/n*/n for n in x]
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
 plt.show


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
    while abs(suiteuV1(p+1)/suiteuV1(p))-rho)>10**-10:
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

def Edhec21b:
    u=1
    k=0
    while u**2-1<=1000:
        u=sqrt(u**2+u)
        k=k+1
    return k

#Feuille 2

#exercice 1

def f(x):
    y=1/(1+x**2)
    return y
epsilone=float(input('donner un réel positif assez petit eps='))
Rn=0
N=int(np.floor(1/2*epsilone)))
for k in range (1,N+1):
    Rn=Rn+1/N*f(k/N)
 print('la valeur approchée de pi à ', epsilone, 'près est', 4*Rn)

 #exercice 2

 #a

 def Lagrange(L,x,k):  #Lk(x) L=[x0,x1...xn]
    n=len(L)
    p=1
    for j in range (0,n):
        if j!=k:
            p=p*(x-L[j]/(L[k]-L[j])
    return p

Lagrange([-2,-1,0,1,2],-2,0))  #L0x0

#b

import matplotlib.pyplot as plt
L=eval(input('donner les valeurs de la liste L'))
n=len(L)
x= np.linspace(-3,3,150)   #domaine d'étude de la fonction L-k
for k in range (0,n):
    y=Lagrange(L,x,k)  #calcul des images de l'intervalle d'étude x
    plt.plot(x,y) #représentation de x en fct de y
 plt.grid()
 plt.grid

 #exercice 3

def f(x):
    y= x + np.log(x)
    return y
def df(x):
    y=1+1/x
    return y
a= float(input('a=')) #le 1er terme de la suite an est a0= a
epsilone= float(input('epsilone='))
k=0
while abs(f(a)/df(a))>espislone:
    a=a-f(a)/df(a)  #calcul des termes de an
    k=k+1  #calcul du nombre d'itéra° nécessaire pour calculer valeur approc de x0
    print('la valeur approchée de l'équation g(x)=0 est x0=',a, 'le nouveau)


#exercice 4

def eval_poly(P,x0):
    z=0
    n=len(P) #calcul de la dimension du vecteur polynôme P
    for k in range (n-1, -1, -1):
        z=z*x0+ P[k]  #évalue poly en x0
    return z

#exercice 6
def a(n) :  #cette fct est juste pour tourner la fct somme
    return 1+0.5**n
def somme(n):
    denominateur=s=0
    for k in range (1,n+1):
        denominateur=denominateur + a(k)
        s+=k/denominateur
    return s

#exercice 7

import matplotlib.pyplot as plt
import numpy as np
from math import *
n=1
S=atan(1/2)-atan(0)
while 1/2*(pi/2-atan(n))>=0.001:
    S=S+atan(n+1/2)-atan(n)
    n=n+1
print('n=',n,"S=", S)


for n in range (0,floor(tan(pi/2-0.002))+1):
    S=S+atan(n+1/2)-atan(n)
print("S_méthode2= ", S)


#exercice 8

def EML2015():
    n=0
    s=0
    while (exp(-n)/(-1+(e(1))>10**-4:
        n=n+1
        s+=1/(n**3*exp(n))
    return s

#♥ Méthode 2

def EML2015M2():
    s=0
    for k in range (1, 1+ floor(-log((e-1)*0.0001))):
        s+=1/(n**3*exp(n))
        return s

def iteration(p):
    liste_iter=[k for k in range (0,p)]
    for i range (0,p):
        x=h(10**(i-1))
        liste_iter[i]=x[i]  #nombre d'iteration
    return liste_inter

def iteration2(p):
    return [h(10**(-i))[1] for i in range (1,p+1)]



#Feuille 3

from numpy.random import*
import numpy.random as rd
import matplotlib.pyplot as plt

#Exercice 1


##1)def simule():
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
    return sortie69
##2)

print('Frequence='np.mean([simule() for k in range(10000)])

print('Frequence='sum([simule() for k in range(10000)])/10000)

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

#q369
n=int(input('n='))
E=0
for k in range(n):
    E+=simuleX()
print('Moyenne empirique pour n=',n, 'est', E/n, 'à comparer avec E=3')


#ex4

#1)

def uniforme(n,m):
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
    while rd.random()>:
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

#OU
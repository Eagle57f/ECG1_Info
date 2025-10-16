#Feuille 2
import numpy as np

#exercice 1


def f(x):
    y=1/(1+x**2)
    return y
epsilone=float(input('donner un réel positif assez petit eps='))
Rn=0
N=int(np.floor(1/2*epsilone))
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
            p=p*(x-L[j])/(L[k]-L[j])
    return p

Lagrange([-2,-1,0,1,2],-2,0)  #L0x0

#b

import matplotlib.pyplot as plt
L=eval(input('donner les valeurs de la liste L'))
n=len(L)
x= np.linspace(-3,3,150)   #domaine d'étude de la fonction L-k
for k in range (0,n):
    y=Lagrange(L,x,k)  #calcul des images de l'intervalle d'étude x
    plt.plot(x,y) #représentation de x en fct de y
plt.grid()
plt.show()

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
while abs(f(a)/df(a))>epsilone:
    a=a-f(a)/df(a)  #calcul des termes de an
    k=k+1  #calcul du nombre d'itéra° nécessaire pour calculer valeur approc de x0
    print("la valeur approchée de l'équation g(x)=0 est x0=",a)


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
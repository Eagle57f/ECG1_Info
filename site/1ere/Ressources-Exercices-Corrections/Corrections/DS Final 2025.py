# Des erreurs peuvent êtes présentes dans ce fichier, si vous en trouvez, merci de me le signaler.
# J'ai surtout répondu aux questions python, pas à celles de maths.

# Sujet : DS Final 2025

# Exercice 1

# 1)

import numpy as np

def Liste(n):
    L=[]
    for i in np.linspace(1,20,n):
        L.append(int(i))
    return L
print(Liste(30))

# 2)

def Som(L):
    s=0
    for i in L:
        if i%2==0:
            s+=i
    return s
print(Som([1,2,3,4,5,6,7,2,3,9,34,63]))

# 3)
L=[114, 15, 20, 152, 45, 87, 26, 153, 0, -7, 147, 158, 1258]
print(Som(L))

# Exercice 2

def FACTO(n):
    if n==0 or n==1:
        return 1
    return FACTO(n-1)*n

# Exercice 3

# 1)

from math import sqrt

def suite(n):
    if n==0:
        return 0.5
    elif n==1:
        return 1
    return sqrt(suite(n-1))+sqrt(suite(n-2))
print(suite(5))


# Exercice 4

def pal(L):
    Lbis=L.copy()
    Lbis.reverse()
    return L==Lbis

print(pal([1,2,3,2,1]))
print(pal([1,2,3,4]))

# OU

def pal(L):
    return L==L[::-1]

print(pal([1,2,3,2,1]))
print(pal([1,2,3,4]))


# Exercice 5

# 1)

def SIMPLE(L):
    Lbis=[]
    for i in L:
        if i not in Lbis:
            Lbis.append(i)
    return Lbis
print(SIMPLE([1,3,4,2,1,4,6,2,9,0,1]))


# 2)

def PREMS(L, elem):
    if elem in L:
        return L.index(elem)
    else:
        return -1
print(PREMS([1,2,4,5,2], 2))
print(PREMS([1,2,4,5,2], 6))


# Exercice 6

LISTE=[1,4,5,2,6,3,6,6,5] # Exemple

def f(LISTE):
    m=max(LISTE)
    for _ in range(LISTE.count(m)):
        LISTE.remove(m)
    return max(LISTE)
print(f(LISTE))


# Exercice 7

# Partie A

# 1)

import matplotlib.pyplot as plt


# 2)

plt.show()


# Partie B

mois = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"]
temperatures = [5, 7, 12, 15, 20, 24]
precipitation = [120, 90, 80, 65, 50, 30]

import matplotlib.pyplot as plt

plt.plot(mois, temperatures)
plt.title("Evolution des températures")
plt.xlabel("Mois")
plt.ylabel("Températures")
plt.grid()
plt.show()


# Partie C

import matplotlib.pyplot as plt
import numpy as np

def f(x): return (x-2)/(x+3)

x=np.linspace(-2, 5, 100)
y=f(x)
plt.plot(x,y)
plt.show()


# Exercice 8

# 1)

# Renvoie [34, -91, 5, 67]


# 2)

# Renvoie [-91, 5, 67, -89, 23, 56.12, 3, 73, 82, -19, 50, 6, -11]


# 3)

# Renvoie [45, 12, 78.5, 34, -91, 5, 67, -89, -5, 23, 56.12, 3, 73, 82, -19, 50, 6, -11]


# 4)

# Renvoie une erreur, car -1 n'est pas dans la liste. Si on ignore l'erreur (Hors Programme),
# on obtient la même liste que la question précédente.


# 5)

# Renvoie [-91, 23, -19]


# Exercice 9

import matplotlib.pyplot as plt
abscisses = [1, 2.5, 2, 2, 0, 0, -0.5, 1]
ordonnees =[3, 2, 2, 0, 0, 2, 2, 3]
plt.plot(abscisses, ordonnees)
plt.grid()
plt.show()


# Exercice 10

from math import *
def suite(n):
    if n%2==0:
        u=log(3)/4
        for k in range(2, n+1, 2):
            u = 4*u - 00000000 # Je n'ai pas la formule obtenue à la question précédente
    else:
        u=log(2/sqrt(3))
        for k in range(3, n+1, 2):
            u = 4*u - 00000000 # Je n'ai pas la formule obtenue à la question précédente
    return u
print(suite(10))
# Des erreurs peuvent êtes présentes dans ce fichier, si vous en trouvez, merci de me le signaler.
# J'ai surtout répondu aux questions python, pas à celles de maths.

# Sujet : DS Final 2024

# I Exercices sur les suites

# 1.1 Suites récurrentes

# 1.

n=int(input("Donnez n: "))
def u1(n):
    if n==0:
        return 2
    return 3*(u1(n-1))**2 - 1
print(u1(n))


# 2.

import math

n=int(input("Donnez n: "))
def u2(n):
    if n==1:
        return 0
    return math.exp(-u2(n-1))
print(u2(n))


# 3.

n=int(input("Donnez n: "))
def u3(n):
    if n==0 or n==1:
        return 1
    return u3(n-1) + u3(n-2)
print(u3(n))


# 4. Version avec la somme

n=int(input("Donnez n: "))
def u4(n):
    if n==0:
        return 1
    s=0
    for i in range(n):
        s=s+(u4(i)/(i**2+1))
    return s
print(u4(n))


# 4. Version sans la somme

n=int(input("Donnez n: "))
def u4bis(n):
    if n==0:
        return 1
    return u4bis(n-1)*((n-1)**2+2)/((n-1)**2+1)
print(u4bis(n))


# 1.2 Suites imbriquées

# 2.

n=int(input("Donnez n: "))
def suites(n):
    def a(n):
        if n==0:
            return 0
        return 2*a(n-1) + b(n-1)

    def b(n):
        if n==0:
            return 1
        return 2*a(n-1) + 3*b(n-1)
    

    return a(n), b(n)

print(suites(n))


# 1.3 Suites définies par une somme ou un produit

# 1.

n=int(input("Donnez n: "))
s=0
for i in range(1,n+1):
    s=s+1/i**2
print(s)


# 2.b

n=int(input("Donnez n: "))
p=1
for i in range(2,n+1):
    p=p*(1-1/i**2)
print(p)


# 2.f

a=eval(input("Donnez a: "))
def seuil(a):
    n=2
    v=3/4
    while v-1/2>a:
        v=(n+1)/2**n
        n=n+1
    return n
print(seuil(a))


# 3.c

n=int(input("Donnez n: "))

def a(n):
    s=0
    for i in range(1,n+1):
        s=s+i
    return s**4

def b(n):
    s=0
    for i in range(1,n+1):
        s=s+i**4
    return s

def difference(n):
    return a(n) - b(n)

print(difference(n))



# II Simulation et fréquences

# II.1 Simulation 1

# 1.

from random import *
x=random()
if x<1/3:
    piece="PILE"
else:
    piece="FACE"
print(piece)


# 2.

def simulX():
    i=0
    for _ in range(3):
        x=random()
        if x<1/3:
            i+=1
    return i
print(simulX())


# II.2 Simulation 2

# 1.

def simul2X():
    for i in range(1, 5):
        if random() < 1/3:
            return i
    return 4
print(simul2X())


# 2. Version simple

n=int(input("Donnez n: "))
def simultipleX(n):
    s=0
    for i in range(n):
        s=s+simul2X()
    return s/n
print(simultipleX(n))


# 2. Version avancée

n=int(input("Donnez n: "))
def simultipleXbis(n):
    return sum([simul2X() for _ in range(n)])/n
print(simultipleXbis(n))



# III Matrices

# 1.

import numpy as np


# 2.

import numpy as np
A=np.array([[1,2,3], [2,-7,6]])


# 3.

import numpy as np
B=np.array([[1,2], [3,4], [5,6]]) # Ligne non demandée, pour éviter les erreurs dans ce fichier, ne pas la mettre dans le DS
np.dot(A,B)


# 4.

import numpy as np
np.eye(n)


# 5.

print(np.size(A)) # Renvoie 6


# 6.

print(A[1,2]) # Renvoie 6, car on commence à compter les lignes et colonnes à partir de 0, et non de 1.



# IV Opérations sur les listes

# 1.

# Réponse : 1


# 2.
corr0 = [4, 2, 1, 4, 3, 1, 3, 3, 2, 1, 1, 3, 3, 2, 4, 4, 2, 1, 3, 3]
print(corr0[17]) # Renvoie 1, car le premier item de la liste à l'indice 0


# 3.

# Réponse : False


# 4.

copTM = [4, 1, 2, 4, 3, 3, 1, 4, 3, 3, 2, 1, 3, 2, 4, 1, 3, 3, 2, 3]

corrTM = [True, False, False, True, True, False, False, False, False, False, False, False, True, True, True, False, False, False, False, True]

# Approfondissement : Algorithme pour générer cette liste automatiquement :
corrTM = [copTM[i]==corr0[i] for i in range(len(copTM))]
print(corrTM)


# 5.

def note(cop,corr):
    n=0
    for i in range(len(cop)):
        if corr[i]==cop[i]:
            n+=1
    return n

print(note(copTM, corr0))


# 6. Version simple

def reussite(cop,corr):
    if note(cop,corr) >= 10:
        return "Réussite"
    else:
        return "Echec"
print(reussite(copTM, corr0))


# 6. Version en une ligne

def reussite(cop,corr):
    return "Réussite" if note(cop,corr)>=10 else "Echec"
print(reussite(copTM, corr0))


# 7.

def notebonus(cop,corr):
    n=0
    for i in range(len(cop)):
        if corr[i]==cop[i]:
            n+=1 # Pareil que d'écrire n=n+1
            if n==4:
                if note(cop,corr) + 2 <= 20:
                    return note(cop,corr) + 2
                else:
                    return 20
        else:
            n=0
    return note(cop,corr)

print(notebonus(copTM, corr0))



# V Courbes représentatives de fonctions

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 2, 200)
y = np.exp(x**2)

plt.plot(x, y, label='f(x) = e^{x²}')
plt.title('Courbe représentative de f(x) = e^{x²}')
plt.legend()
plt.show()
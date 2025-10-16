# En cours

# Exercice 1:

"""import numpy as np

def f(x):
    return 1/(1+x**2)

eps=float(input("eps ? "))
Rn=0
N=int(np.floor(1/eps))+1 # N tel que 1/N < eps
for k in range(1,N+1):
    Rn=Rn+1/N*f(k/N)
print(4*Rn, eps)"""

# Exercice 2:
"""n=10 # int(input("n ? "))
def L(k,X, x):
    p=1
    for j in range(len(X)):
        p*=(x-X[j])/(X[k]-X[j]) if j!=k else 1
    return p
print(L(3,[1,2,3,4,5,6,7,8,9,10,11],1.5))

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,100)
l=[-2, -1, 0, 1, 2]
for k in range(len(l)):
    y=[L(k, l, xi) for xi in x]
    plt.plot(x,y)
plt.grid()
plt.show()"""


# Exercice 3:

"""import numpy as np

def f(x): return x+np.log(x)

def df(x): return 1+1/x


def newton(f, df, a, eps):
    an=a
    anp=an-f(an)/df(an)
    i=1
    while abs(anp-an)>eps:
        an=anp
        anp=an-f(an)/df(an)
        i+=1
    return an, i

print(newton(f, df, 1, 10e-10))"""


# Exercice 4: 
"""p=[1, 0, -2, 1]  # x^3 - 2x + 1
def eval_poly(p, x0):
    r=p[0]
    for i in range(1, len(p)):
        r=r*x0+p[i]
    return r
print(eval_poly(p, 2))"""


# Exercice 5:

# 1)

"""from numpy import exp, sqrt
n=0
while exp(-sqrt(n))>10e-4:
    n+=1
print(n)"""

# Exercice 6:
"""import numpy as np

def f(x): return np.exp(x)*x**3
n=0
S=0
while 1/((np.e-1)*np.exp(n))>10e-4:
    n+=1
    S+=1/f(n)
print(n, S)"""


# Exercice 7:

"""eps=10e-2
x=2

k=1
while 1/(k+1)**x>eps: k+=1

print(sum([((-1)**(k+1))/k**x for k in range(1,k+1)]), k)"""


# Exercice 8

"""# 5)
from math import factorial, pi
from numpy import zeros
def I(n):
    u=zeros(2*n+2)
    u[0]=0
    u[1]=1
    for i in range(2, 2*n+2):
        u[i]=((factorial(2*n)/(2**n*factorial(n)))**2)*(pi/2) if i%2==0 else ((factorial(n)*2**n)**2)/factorial(2*n+1)
    y=u
    return y

print(I(3))


# 6)

def SI(n):
    return sum(I(n)[:n+1])

print(SI(3))"""


# Exercice 9

"""# 2)
from math import sqrt
def h(e):
    k=0
    a=sqrt(3)/2
    b=1/2
    while abs((9*2**k*(a/(2+b)))-(2**k*(2*a+a/b)))>e:
        a=sqrt((1-b)/2)
        b=sqrt((1+b)/2)
        k+=1
    x=((9*2**k*(a/(2+b)))+(2**k*(2*a+a/b)))/2
    return x,k
print(h(10e-5))

import matplotlib.pyplot as plt
def evol(p):
    l=[]
    for i in range(1,p+1):
        l.append(h(10**-(1*i))[1])
    plt.scatter(range(1,p+1), l)
    plt.show()
    
evol(30)


# On remarque une évolution linéaire jusqu'à 10**-16, puis une stagnation.
# Ceci est du à la précision des floats python (base 64 donc environ 15 à 17 decimales)."""


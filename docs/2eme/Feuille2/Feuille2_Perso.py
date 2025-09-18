# En cours

# Ex 2
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

import numpy as np

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

print(newton(f, df, 1, 10e-10))

# Exercice 4: 

